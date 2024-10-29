@echo off

set build_name=NOGP
set build_type=devel
set build_version=v1_3_0_6_a1
set build_path=R:\WORK\NOG\%build_version%\%build_type%\build\%build_name%
set exe_path=R:\WORK\NOG\%build_version%\%build_type%

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
echo -- Deleting build path files: del %build_path%\dist\lib /F /Q
del %build_path%\dist\lib /F /Q
echo -- Deleting build path files: del %build_path%\dist\mpl-data /F /Q
del %build_path%\dist\mpl-data /F /Q
echo -- Deleting build path files: del %build_path%\dist\*.exe /F /Q
del %build_path%\dist\*.exe /F /Q
echo -- Deleting build path files: del %build_path%\dist\*.dll /F /Q
del %build_path%\dist\*.dll /F /Q
echo -- Deleting build path files: del %build_path%\dist\*.ui /F /Q
del %build_path%\dist\*.ui /F /Q
echo -- Deleting build path files: del %build_path%\dist\*.bat /F /Q
del %build_path%\dist\*.bat /F /Q
echo -- Deleting build path files: del %build_path%\dist\*.log /F /Q
del %build_path%\dist\*.log /F /Q
echo --
echo -- Removing build path and all subdirectories: rmdir %build_path%\dist\lib /S /Q
rmdir %build_path%\dist\lib /S /Q
echo -- Removing build path and all subdirectories: rmdir %build_path%\dist\mpl-data /S /Q
rmdir %build_path%\dist\mpl-data /S /Q
echo -- 
#echo --> Making build path: mkdir %build_path%
#mkdir %build_path%
echo -- 

echo -- 
echo -- Deleting exe path files: del %exe_path%\lib /F /Q
del %exe_path%\lib /F /Q
echo -- Deleting exe path files: del %exe_path%\mpl-data /F /Q
del %exe_path%\mpl-data /F /Q
echo -- Deleting exe path files: del %exe_path%\*.exe /F /Q
del %exe_path%\*.exe /F /Q
echo -- Deleting exe path files: del %exe_path%\*.dll /F /Q
del %exe_path%\*.dll /F /Q
echo -- Deleting exe path files: del %exe_path%\*.ui /F /Q
del %exe_path%\*.ui /F /Q
echo -- Deleting exe path files: del %exe_path%\*.bat /F /Q
del %exe_path%\*.bat /F /Q
echo -- Deleting exe path files: del %exe_path%\*.log /F /Q
del %exe_path%\*.log /F /Q
echo --
echo -- Removing exe path and all subdirectories: rmdir %exe_path%\lib /S /Q
rmdir %exe_path%\lib /S /Q
echo -- Removing exe path and all subdirectories: rmdir %exe_path%\mpl-data /S /Q
rmdir %exe_path%\mpl-data /S /Q
echo -- 
#echo --> Making exe path: mkdir %exe_path%
#mkdir %exe_path%
echo -- 

echo --
echo -- Copying additonalonal distributable files to project build path: 
copy SharkSimFE_CURRENT_FORM.ui %~dp0\py2exe\dist\* 
copy SharkSimFE_CURRENT_DIALOG_AGE_COHORT_BY_SEX_MORTALITY.ui %~dp0\py2exe\dist\*
copy SharkSimFE_CURRENT_DIALOG_AGE_COHORT_SAMPLING.ui %~dp0\py2exe\dist\*
copy SharkSimFE_CURRENT_HELP_NONMODAL_DIALOG_WV.ui %~dp0\py2exe\dist\*
copy SharkSimFE_CUSTOM_WIDGET_DOUBLE_SPINBOX_SLIDER.ui %~dp0\py2exe\dist\*
copy SharkSimFE_CUSTOM_WIDGET_DOUBLE_SPINBOX_SLIDER_SS.ui %~dp0\py2exe\dist\*
copy 0-Run_FE_DEBUG.bat %~dp0\py2exe\dist\*
copy Settings.ini %~dp0\py2exe\dist\*
echo --

echo --
echo -- Copying project source to work build destination: robocopy %~dp0 %build_path% *
robocopy %~dp0 %build_path% *
echo --

echo --
echo -- Copying project dist to work build destination: robocopy %~dp0\py2exe %build_path% * /E /XD build*
robocopy %~dp0\py2exe %build_path% * /E /XD build*
echo --

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