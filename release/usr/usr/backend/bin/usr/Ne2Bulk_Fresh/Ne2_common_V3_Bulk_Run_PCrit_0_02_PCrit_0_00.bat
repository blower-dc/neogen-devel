cd %~dp0

:process_PC2
type Ne2_common_V3_PC2.param1 > Ne2_common_V3_PC2.param_run
type Ne2_Bulk_Filenames.txt >> Ne2_common_V3_PC2.param_run
type Ne2_common_V3_PC2.param2 >> Ne2_common_V3_PC2.param_run
del Ne2_common_V3_Bulk_Run_PCrit_0_02.FAILED
del Ne2_common_V3_Bulk_Run_PCrit_0_02.COMPLETE
del Ne2_common_CAOB_V3_PC2xLD.txt
del Ne2_common_CAOB_V3_PC2.out
Ne2 c:Ne2_common_V3_PC2.param_run
IF %ERRORLEVEL% NEQ 0 (
goto :error_PC2 
) else (
goto :complete_PC2
)

:process_PC0
type Ne2_common_V3_PC0.param1 > Ne2_common_V3_PC0.param_run
type Ne2_Bulk_Filenames.txt >> Ne2_common_V3_PC0.param_run
type Ne2_common_V3_PC0.param2 >> Ne2_common_V3_PC0.param_run
del Ne2_common_V3_Bulk_Run_PCrit_0_00.FAILED
del Ne2_common_V3_Bulk_Run_PCrit_0_00.COMPLETE
del Ne2_common_CAOB_V3_PC2xLD.txt
del Ne2_common_CAOB_V3_PC2.out
Ne2 c:Ne2_common_V3_PC0.param_run
IF %ERRORLEVEL% NEQ 0 (
goto :error_PC0
) else (
goto :complete_PC0
)

:error_PC2
echo Ne2_common_V3_Bulk_Run_PCrit_0_02 Failed with error #%errorlevel%. > Ne2_common_V3_Bulk_Run_PCrit_0_02.FAILED
goto :process_PC0

:complete_PC2
echo Ne2_common_V3_Bulk_Run_PCrit_0_02 Completed successfully. > Ne2_common_V3_Bulk_Run_PCrit_0_02.COMPLETE
goto :process_PC0

:error_PC0
echo Ne2_common_V3_Bulk_Run_PCrit_0_00 Failed with error #%errorlevel%. > Ne2_common_V3_Bulk_Run_PCrit_0_00.FAILED
goto :EOR

:complete_PC0
echo Ne2_common_V3_Bulk_Run_PCrit_0_00 Completed successfully. > Ne2_common_V3_Bulk_Run_PCrit_0_00.COMPLETE
goto :EOR

:EOR
echo %~n0 Completed successfully.
goto :EOF

:EOF
exit