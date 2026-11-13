@echo off
setlocal
set "UE_EDITOR=E:\UE\UE_5.8\Engine\Binaries\Win64\UnrealEditor.exe"
set "TAT_PROJECT_FILE=%~dp0TouchAndTrigger.uproject"
if not exist "%UE_EDITOR%" (
  echo UE 5.8 editor was not found. Open TouchAndTrigger.uproject with UE 5.8.
  pause
  exit /b 1
)
powershell.exe -NoProfile -Command "$editor = Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'UnrealEditor.exe' -and $_.CommandLine -and $_.CommandLine.Replace('\','/').Contains($env:TAT_PROJECT_FILE.Replace('\','/')) } | Select-Object -First 1; if ($editor) { $shellApp = New-Object -ComObject WScript.Shell; [void]$shellApp.AppActivate([int]$editor.ProcessId); exit 0 }; exit 1"
if not errorlevel 1 exit /b 0
start "" "%UE_EDITOR%" "%TAT_PROJECT_FILE%"
