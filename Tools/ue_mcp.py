"""Development helper for the official local Unreal MCP server; not game logic."""
import argparse
import json
import urllib.request


class UnrealMCP:
    def __init__(self, url="http://127.0.0.1:8000/mcp"):
        self.url = url
        self.session = None
        self.sequence = 0
        self.rpc("initialize", {
            "protocolVersion": "2024-11-05", "capabilities": {},
            "clientInfo": {"name": "TouchAndTriggerTools", "version": "1.0"},
        })
        self.rpc("notifications/initialized", notification=True)

    def rpc(self, method, params=None, notification=False):
        self.sequence += 1
        payload = {"jsonrpc": "2.0", "method": method}
        if not notification:
            payload["id"] = self.sequence
        if params is not None:
            payload["params"] = params
        headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
        if self.session:
            headers["Mcp-Session-Id"] = self.session
        request = urllib.request.Request(self.url, json.dumps(payload).encode(), headers)
        with urllib.request.urlopen(request, timeout=90) as response:
            self.session = response.headers.get("Mcp-Session-Id", self.session)
            raw = response.read().decode("utf-8-sig")
        if not raw.strip():
            return None
        if raw.lstrip().startswith("data:") or raw.lstrip().startswith("event:"):
            messages = [line[5:].strip() for line in raw.splitlines() if line.startswith("data:")]
            raw = messages[-1]
        result = json.loads(raw)
        if "error" in result:
            raise RuntimeError(result["error"])
        return result.get("result")

    def tool(self, name, arguments=None):
        result = self.rpc("tools/call", {"name": name, "arguments": arguments or {}})
        if result.get("isError"):
            raise RuntimeError(result)
        texts = [item["text"] for item in result.get("content", []) if item.get("type") == "text"]
        if len(texts) == 1:
            try:
                return json.loads(texts[0])
            except json.JSONDecodeError:
                return texts[0]
        return result

    def describe(self, toolset):
        return self.tool("describe_toolset", {"toolset_name": toolset})

    def call(self, toolset, tool, **arguments):
        return self.tool("call_tool", {"toolset_name": toolset, "tool_name": tool, "arguments": arguments})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default="http://127.0.0.1:8000/mcp")
    parser.add_argument("--request", help="JSON file containing toolset, tool and arguments")
    parser.add_argument("--describe", help="Toolset name to inspect")
    args = parser.parse_args()
    client = UnrealMCP(args.url)
    if args.describe:
        output = client.describe(args.describe)
    elif args.request:
        with open(args.request, encoding="utf-8-sig") as source:
            request = json.load(source)
        output = client.call(request["toolset"], request["tool"], **request.get("arguments", {}))
    else:
        playing = client.call("EditorToolset.EditorAppToolset", "IsPIERunning").get("returnValue", False)
        output = {"play_in_editor": True} if playing else client.call("editor_toolset.toolsets.scene.SceneTools", "get_current_level")
    print(json.dumps(output, ensure_ascii=False, indent=2))
