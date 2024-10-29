@echo off

cd %~dp0

del Ne2Bulk_FAILED_Files.txt
del Ne2Bulk_FAILED_Run.txt

dir *.FAILED /s /b /a-d > Ne2Bulk_FAILED_Files.txt

for /f "tokens=*" %%a in (Ne2Bulk_FAILED_Files.txt) do call :processline %%a

pause
goto :EOF

:processline
echo line=%*
Set filename=%*
For %%A in ("%filename%") do (
    Set Folder=%%~dpA
    Set Name=%%~nxA

    
)
Set NameNoExt=%Name%
Set NameNew=%NameNoExt:FAILED=bat%
Set FolderNameNew=%Folder%%NameNew%
echo.Running BAT file: %FolderNameNew%
echo.%FolderNameNew% >> Ne2Bulk_FAILED_Run.txt
start %FolderNameNew%
cd %~dp0

:EOF
