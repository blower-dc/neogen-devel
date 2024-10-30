@echo off
echo --------------------------------------------------------
echo --- This will DELETE the RELEASE environ. Are you sure? ---
echo --------------------------------------------------------
pause
set build_path=R:\WORK\NOG\v1_3_0_6_a1\release
echo -- Deleting build path files: del %build_path% /F /Q
del %build_path% /F /Q
echo --
echo -- Removing build path and all subdirectories: rmdir %build_path% /S /Q
rmdir %build_path% /S /Q
echo -- 
echo -- Making build path: mkdir %build_path%
mkdir %build_path%
echo --------------------------------------------------------
echo --- Copy Binaries from DEVEL ---
echo --------------------------------------------------------
robocopy R:\WORK\NOG\v1_3_0_6_a1\devel\ R:\WORK\NOG\v1_3_0_6_a1\release\ /E /Z /XF "NOGP.exe.log" "0-Run_FE_DEBUG.bat" /XD R:\WORK\NOG\v1_3_0_6_a1\devel\build R:\WORK\NOG\v1_3_0_6_a1\devel\usr\var\backend\work R:\WORK\NOG\v1_3_0_6_a1\devel\usr\etc R:\WORK\NOG\v1_3_0_6_a1\devel\usr\logs R:\WORK\NOG\v1_3_0_6_a1\devel\usr\doc R:\WORK\NOG\v1_3_0_6_a1\devel\resources
echo --------------------------------------------------------
echo --- Copy /usr/etc/ from SETUP ---
echo --------------------------------------------------------
robocopy R:\WORK\NOG\v1_3_0_6_a1\setup\etc R:\WORK\NOG\v1_3_0_6_a1\release\usr\etc /E /Z
echo --------------------------------------------------------
echo --- Copy /usr/doc/ From SETUP ---
echo --------------------------------------------------------
robocopy R:\WORK\NOG\v1_3_0_6_a1\setup\doc R:\WORK\NOG\v1_3_0_6_a1\release\usr\doc /E /Z 
echo --------------------------------------------------------
echo --- Copy /resources/ From SETUP ---
echo --------------------------------------------------------
robocopy R:\WORK\NOG\v1_3_0_6_a1\setup\install_resources\resources R:\WORK\NOG\v1_3_0_6_a1\release\resources /E /Z 
echo --------------------------------------------------------
echo --- Make usr/logs/ ---
echo --------------------------------------------------------
mkdir R:\WORK\NOG\v1_3_0_6_a1\release\usr\logs
pause

