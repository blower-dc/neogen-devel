python setup_PY2EXE.py py2exe

copy SharkSimFE_CURRENT_FORM.ui %~dp0\py2exe\dist\* 
copy SharkSimFE_CURRENT_DIALOG_AGE_COHORT_BY_SEX_MORTALITY.ui %~dp0\py2exe\dist\*
copy SharkSimFE_CURRENT_DIALOG_AGE_COHORT_SAMPLING.ui %~dp0\py2exe\dist\*
copy SharkSimFE_CURRENT_HELP_NONMODAL_DIALOG_WV.ui %~dp0\py2exe\dist\*
copy SharkSimFE_CUSTOM_WIDGET_DOUBLE_SPINBOX_SLIDER.ui %~dp0\py2exe\dist\*
copy SharkSimFE_CUSTOM_WIDGET_DOUBLE_SPINBOX_SLIDER_SS.ui %~dp0\py2exe\dist\*
#copy Settings.ini %~dp0\py2exe\dist\*
copy 0-Run_FE_DEBUG.bat %~dp0\py2exe\dist\*
makedir %~dp0\py2exe\dist\usr\backend\bin

echo Run the EXE?
pause

%~dp0\py2exe\dist\Main.exe
pause