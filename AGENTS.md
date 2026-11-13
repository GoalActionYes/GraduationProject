# TouchAndTrigger

- This is the only active graduation game project. BallPuzzle is a retired reference; do not continue gameplay work there.
- Use Unreal Engine 5.8.4. Keep project paths and asset names ASCII.
- Gameplay must be implemented in editable Blueprints using engine classes. Do not add a project C++ module or depend on BallPuzzle native classes.
- Use material graphs and Niagara for appearance. The student authors and understands the final contamination, water, and VFX work.
- Prefer the official Unreal MCP editor tools when connected. Plugin enablement is not proof that a client is connected.
- Build and verify a small Blueprint change before broad automation. Report graph compilation, runtime behavior, and visual review separately.
- Start with a Blueprint rolling pawn and camera, then contact-driven local contamination and washing.
- Preserve student-authored assets. Do not overwrite or regenerate their work without inspecting it.
- Startup map is /Game/Game/Maps/L_InteractionLab. BP_RollingBall is the editable Pawn; BP_ExplorationMode selects it. See Docs/Progress.md before continuing work.
- Do not import the old game wholesale. Inspect native dependencies before reusing any assets or maps.
- The user has authorized milestone commits and pushes to https://github.com/GoalActionYes/GraduationProject after a substantial feature is implemented and verified. Use GitHub, not Bitbucket. Check local and remote hashes after pushing. Never force-push.
- README.md is the single project entry; Docs/Progress.md records the actual handoff and verification. Keep documentation compact and Chinese, with ASCII file names.
- Routine foundations, folder setup, naming, debugging and editor tooling do not require repeated approval. Keep core gameplay choices and final authored VFX for the student to review and make.
- Distinguish tutorials to follow from references for knowledge. Explain exactly how each exercise connects to this project; do not assign a multi-hour snow tutorial as if it directly implements a rolling ball.
- Official MCP DSL and node identifiers can depend on editor language. Discover current schemas and actual node IDs. Use low-level Blueprint tools if DSL assumptions fail; do not change the student's editor language to work around a tool bug.
- Do not invoke modal Save As dialogs through synchronous MCP tools: the dialog can block the game-thread tool queue. Prefer non-modal asset tools; ask for minimal manual interaction when a modal is unavoidable.
- Editor helper Python must not implement runtime game behavior. Do not commit throwaway generator scripts from Saved or regenerate student assets.
