@echo off
echo --------------------------------------------------------
echo --- This will DELETE the RELTEST environ. Are you sure? ---
echo --------------------------------------------------------
pause
set build_path=R:\WORK\NOG\v1_3_0_6_a1\reltest
echo -- Deleting build path files: del %build_path% /F /Q
del %build_path% /F /Q
echo --
echo -- Removing build path and all subdirectories: rmdir %build_path% /S /Q
rmdir %build_path% /S /Q
echo -- 
echo -- Making build path: mkdir %build_path%
mkdir %build_path%
echo --------------------------------------------------------
echo --- Copy Everything from RELEASE ---
echo --------------------------------------------------------
robocopy R:\WORK\NOG\v1_3_0_6_a1\release\ R:\WORK\NOG\v1_3_0_6_a1\reltest\ /E /Z 
pause

