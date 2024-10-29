#@echo off

Set SourceFolder=I:\DCB\MUI\MUI_Sync_Auto\MUI_A_Analyses\Shared_Data\Ne2Bulk_Fresh

    Setlocal EnableDelayedExpansion
    cls
    set currentDirectory=%SourceFolder%
    FOR /D %%g IN ("*") DO (
        Pushd %CD%\%%g
        FOR /D %%f IN ("*") DO (
            copy "%currentDirectory%\*" "%%~ff"
        )
    Popd
    )
pause