; === App Info ===
#define MyAppName "Mouse control"
#define MyAppVersion "1.5.4"
#define MyAppPublisher "Akshay Jain"
#define MyAppURL "4791akshayjain@gmail.com"
#define MyAppExeName "GG_beta4.exe"

[Setup]
AppId={{9539C1AB-7C15-4768-A6CC-0FDA9DDA5A1C}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}

DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}

UninstallDisplayIcon={app}\{#MyAppExeName}

ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

; Admin mode (required for HKLM startup)
PrivilegesRequired=admin

OutputDir=F:\
OutputBaseFilename=GG_setup_beta5
SetupIconFile=F:\app\vi.ico

Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

; === Files ===
[Files]
Source: "F:\app\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\app\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

; === Start Menu Shortcut ===
[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"

; === Startup Registry (AUTO ENABLED) ===
[Registry]
Root: HKLM; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; \
ValueType: string; ValueName: "{#MyAppName}"; \
ValueData: """{app}\{#MyAppExeName}"""; \
Flags: uninsdeletevalue

; === Run After Install ===
[Run]
Filename: "{app}\{#MyAppExeName}"; \
Description: "Launch {#MyAppName}"; \
Flags: nowait postinstall skipifsilent