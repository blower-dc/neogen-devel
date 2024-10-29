@echo off

set build_name=NeOGen
set build_type=devel
set build_version=v1_3_0_6_a1
set build_path=R:\WORK\NOG\%build_version%\%build_type%\build\%build_name%
set exe_path=R:\WORK\NOG\%build_version%\%build_type%\usr\usr\backend\bin

echo -- Building py2exe executable for:
echo -- build_name: %build_name%
echo -- build_version: %build_version%
echo -- build_path: %build_path%
echo -- 

echo -- Building with python: python setup_PY2EXE.py py2exe
python setup_PY2EXE.py py2exe 
echo --

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
echo -- Copying project build to work build destination: robocopy %~dp0\py2exe %build_path% * /E
robocopy %~dp0\py2exe %build_path% * /E 
echo --

echo --
echo -- Making accessories build path: mkdir %build_path%\dist\usr\Ne2Bulk_Fresh
mkdir %build_path%\dist\usr\Ne2Bulk_Fresh
echo --
echo -- Copying accessories to accessories build path: robocopy %~dp0\usr\Ne2Bulk_Fresh %build_path%\dist\usr\Ne2Bulk_Fresh * /E
robocopy %~dp0\usr\Ne2Bulk_Fresh %build_path%\dist\usr\Ne2Bulk_Fresh * /E
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

echo -- Build completed
echo --
echo -- Run the EXE?: %exe_path%\%build_name%.exe
pause
%exe_path%\%build_name%.exe
pause