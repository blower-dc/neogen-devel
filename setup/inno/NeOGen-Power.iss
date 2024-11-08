; Script generated by the Inno Script Studio Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppDirRoot "R:\WORK\NOG"
#define MyAppName "NeOGen-Power"
#define MyAppVersion "1.3.0.6.a1"
#define MyAppPublisher "Dean Blower"
#define MyAppURL "http://www.molecularfisherieslaboratory.com.au/neogen-software/"
#define MyAppExeName "NOGP.exe"
#define MyAppExeVersion "v1_3_0_6_a1"
#define MyAppInnoSetupVersionDir "v1_3_0_6_a1"
#define MyAppSetupExeOutputDirRoot "setup"
#define MyAppReleaseDir "release"
#define VCmsg "Installing Microsoft Visual C++ Redistributable...."


[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
;ArchitecturesAllowed=x64
AppId={{5FFE7385-3143-4C12-9F54-3873E9E0B57C}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
;DefaultDirName={pf}\{#MyAppName}
DefaultDirName={sd}\NOG
;DisableDirPage=yes
DefaultGroupName=NeOGen
AllowNoIcons=yes
OutputDir={#MyAppDirRoot}\{#MyAppInnoSetupVersionDir}\{#MyAppSetupExeOutputDirRoot}
OutputBaseFilename=Setup-NeoGen-Power_{#MyAppInnoSetupVersionDir}
Compression=lzma
SolidCompression=yes
UninstallDisplayIcon={app}\{#MyAppExeName}

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Dirs]
Name: {app}; Permissions: users-full

[Files]
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\INSTALL_README_NeOGen_Power.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\NOGP.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\NOGP.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\0-Run_FE_DEBUG.bat"; DestDir: "{app}"; Flags: ignoreversion
;Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\NeOGen-Power.exe.log"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\python27.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\Settings.ini"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\SharkSimFE_CURRENT_DIALOG_AGE_COHORT_BY_SEX_MORTALITY.ui"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\SharkSimFE_CURRENT_DIALOG_AGE_COHORT_SAMPLING.ui"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\SharkSimFE_CURRENT_FORM.ui"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\SharkSimFE_CURRENT_HELP_NONMODAL_DIALOG_WV.ui"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\SharkSimFE_CUSTOM_WIDGET_DOUBLE_SPINBOX_SLIDER.ui"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\SharkSimFE_CUSTOM_WIDGET_DOUBLE_SPINBOX_SLIDER_SS.ui"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\w9xpopen.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\depends\*"; DestDir: "{app}\depends"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\lib\*"; DestDir: "{app}\lib"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\mpl-data\*"; DestDir: "{app}\mpl-data"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\usr\*"; DestDir: "{app}\usr"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\registry\*"; DestDir: "{app}\registry"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#MyAppDirRoot}\{#MyAppExeVersion}\{#MyAppReleaseDir}\resources\*"; DestDir: "{app}\resources"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{app}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Parameters:"--debug_logging"
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Parameters:"--debug_logging"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon; Parameters:"--debug_logging"
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon; Parameters:"--debug_logging"

[Run]
Filename: "{app}\resources\vcredist_2008_x64.exe"; StatusMsg: "{#VCmsg}"; Check: IsWin64 and not VCinstalled; Parameters: "/q:a /c:""VCREDI~3.EXE /q:a /c:""""msiexec /i vcredist.msi /qn"""" """;
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent; Parameters:"--debug_logging"

[Registry]
Root: "HKCU"; Subkey: "Software\Microsoft\Windows\Windows Error Reporting"; ValueType: dword; ValueName: "DontShowUI"; ValueData: "1"; Flags: createvalueifdoesntexist deletevalue

[InstallDelete]
Type: filesandordirs; Name: "{app}"

[Code]
function VCinstalled: Boolean;
 // By Michael Weiner <mailto:spam@cogit.net>
 // Function for Inno Setup Compiler
 // 13 November 2015
 // Returns True if Microsoft Visual C++ Redistributable is installed, otherwise False.
 // The programmer may set the year of redistributable to find; see below.
 var
  names: TArrayOfString;
  i: Integer;
  dName, key, year: String;
 begin
  // Year of redistributable to find; leave null to find installation for any year.
  year := '2008';
  Result := False;
  key := 'Software\Microsoft\Windows\CurrentVersion\Uninstall';
  // Get an array of all of the uninstall subkey names.
  if RegGetSubkeyNames(HKEY_LOCAL_MACHINE, key, names) then
   // Uninstall subkey names were found.
   begin
    i := 0
    while ((i < GetArrayLength(names)) and (Result = False)) do
     // The loop will end as soon as one instance of a Visual C++ redistributable is found.
     begin
      // For each uninstall subkey, look for a DisplayName value.
      // If not found, then the subkey name will be used instead.
      if not RegQueryStringValue(HKEY_LOCAL_MACHINE, key + '\' + names[i], 'DisplayName', dName) then
       dName := names[i];
      // See if the value contains both of the strings below.
      Result := (Pos(Trim('Visual C++ ' + year),dName) * Pos('Redistributable',dName) <> 0)
      i := i + 1;
     end;
   end;
 end;