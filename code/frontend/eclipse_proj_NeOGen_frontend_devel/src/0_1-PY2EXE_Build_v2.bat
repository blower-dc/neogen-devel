set build_path="R:\WORK\NOG\v1_3_0_6_a1\devel"

del %build_path% /F /Q
mkdir %build_path%

python setup_PY2EXE.py py2exe 

mkdir %build_path%\py2exe\dist\usr\Ne2Bulk_Fresh
copy %~dp0\usr\Ne2Bulk_Fresh\*.*  %build_path%\py2exe\dist\usr\Ne2Bulk_Fresh\*.*

rd %build_path%\usr\usr\backend\bin /S /Q
mkdir %build_path%\usr\usr\backend\bin
robocopy %build_path%\py2exe\dist %build_path%\usr\usr\backend\bin * /E

echo Run the EXE?
pause

%build_path%\usr\usr\backend\bin\NeOGen.exe

pause