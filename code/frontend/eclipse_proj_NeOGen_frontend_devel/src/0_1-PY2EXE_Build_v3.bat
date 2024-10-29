@echo off

set build_name=NOGP
set build_type=devel
set build_version=v1_3_0_6_a1
set build_path=R:\WORK\NOG\%build_version%\%build_type%\build\%build_name%
set exe_path=R:\WORK\NOG\%build_version%

echo -- Building py2exe executable for:
echo -- build_name: %build_name%
echo -- build_version: %build_version%
echo -- build_path: %build_path%
echo -- 

echo -- Building with python: python setup_PY2EXE.py py2exe
python setup_PY2EXE.py py2exe 
IF %ERRORLEVEL% NEQ 0 (
goto :error_setup_PY2EXE 
) else (
goto :proceed
)

:error_setup_PY2EXE
echo command python setup_PY2EXE.py py2exe FAILED with  #%errorlevel%.
goto :EOF

:proceed
echo --
echo -- Deleting build path files: del %build_path% /F /Q
del %build_path% /F /Q
echo --
echo -- Removing build path and all subdirectories: rmdir %build_path% /S /Q
rmdir %build_path% /S /Q
echo -- 
echo --> Making build path: mkdir %build_path%
mkdir %build_path%
echo -- 

echo --
echo -- Copying project source to work build destination: robocopy %~dp0 %build_path% *
robocopy %~dp0 %build_path% *
echo --

echo --
echo -- Copying project dist to work build destination: robocopy %~dp0\py2exe %build_path% * /E /XD build*
robocopy %~dp0\py2exe %build_path% * /E /XD build*
echo --

echo -- Removing exe destination path: rd %exe_path% /S /Q
rd %exe_path% /S /Q
echo --
echo -- Making exe destination path: mkdir %exe_path%
mkdir %exe_path%
echo --
echo -- Copying build to exe destination: robocopy %build_path%\dist %exe_path% * /E 
robocopy %build_path%\dist %exe_path% * /E
echo --
goto :EOR

:EOR
echo %~n0 Completed successfully.
echo -- Build completed
echo --
echo -- Run the EXE?: %exe_path%\%build_name%.exe
pause
%exe_path%\%build_name%.exe
pause
goto :EOF

:EOF
exit