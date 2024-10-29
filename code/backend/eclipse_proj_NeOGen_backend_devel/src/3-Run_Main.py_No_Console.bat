for /f "skip=1" %%x in ('wmic os get localdatetime') do if not defined mydate set mydate=%%x
echo %mydate%
set mydate=%mydate:+=-%
set mydate=%mydate:.=-%
echo %mydate%
python main.py > C:\DCB\MUI\MUI_Sync_Controlled\MUI_SC_SharkSim\dcb_logging\%mydate%.log
pause