cd %~dp0

:process_PC5
type Ne2_common_V3_PC5.param1 > Ne2_common_V3_PC5.param_run
type Ne2_Bulk_Filenames.txt >> Ne2_common_V3_PC5.param_run
type Ne2_common_V3_PC5.param2 >> Ne2_common_V3_PC5.param_run
del Ne2_common_V3_Bulk_Run_PCrit_0_05.FAILED
del Ne2_common_V3_Bulk_Run_PCrit_0_05.COMPLETE
del Ne2_common_CAOB_V3_PC5xLD.txt
del Ne2_common_CAOB_V3_PC5.out
Ne2 c:Ne2_common_V3_PC5.param_run
IF %ERRORLEVEL% NEQ 0 (
goto :error_PC5 
) else (
goto :complete_PC5
)

:process_PC2
type Ne2_common_V3_PC2.param1 > Ne2_common_V3_PC2.param_run
type Ne2_Bulk_Filenames.txt >> Ne2_common_V3_PC2.param_run
type Ne2_common_V3_PC2.param2 >> Ne2_common_V3_PC2.param_run
del Ne2_common_V3_Bulk_Run_PCrit_0_02.FAILED
del Ne2_common_V3_Bulk_Run_PCrit_0_02.COMPLETE
del Ne2_common_CAOB_V3_PC5xLD.txt
del Ne2_common_CAOB_V3_PC5.out
Ne2 c:Ne2_common_V3_PC2.param_run
IF %ERRORLEVEL% NEQ 0 (
goto :error_PC2 
) else (
goto :complete_PC2
)

:error_PC5
echo Ne2_common_V3_Bulk_Run_PCrit_0_05 Failed with error #%errorlevel%. > Ne2_common_V3_Bulk_Run_PCrit_0_05.FAILED
goto :process_PC2

:complete_PC5
echo Ne2_common_V3_Bulk_Run_PCrit_0_05 Completed successfully. > Ne2_common_V3_Bulk_Run_PCrit_0_05.COMPLETE
goto :process_PC2

:error_PC2
echo Ne2_common_V3_Bulk_Run_PCrit_0_02 Failed with error #%errorlevel%. > Ne2_common_V3_Bulk_Run_PCrit_0_02.FAILED
goto :EOR

:complete_PC2
echo Ne2_common_V3_Bulk_Run_PCrit_0_02 Completed successfully. > Ne2_common_V3_Bulk_Run_PCrit_0_02.COMPLETE
goto :EOR

:EOR
echo %~n0 Completed successfully.
goto :EOF

:EOF
exit