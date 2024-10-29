cd %~dp0

del %~n0.FAILED
del %~n0.COMPLETE
del Ne2_common_CAOB_V3_PC5xLD.txt
del Ne2_common_CAOB_V3_PC5.out

type Ne2_common_V3_PC5.param1 > Ne2_common_V3_PC5.param_run
type Ne2_Bulk_Filenames.txt >> Ne2_common_V3_PC5.param_run
type Ne2_common_V3_PC5.param2 >> Ne2_common_V3_PC5.param_run

set /p Ne_Estimator_Ver=<Ne_Estimator_Version_To_Use.param
echo using Ne Estimator Version: %Ne_Estimator_Ver%
 
%Ne_Estimator_Ver% c:Ne2_common_V3_PC5.param_run || goto :error
goto :EOR

:error
echo %~n0 Failed with error #%errorlevel%. > %~n0.FAILED
exit /b %errorlevel%

:EOR
echo %~n0 Completed successfully. > %~n0.COMPLETE
goto :EOF

:EOF
exit