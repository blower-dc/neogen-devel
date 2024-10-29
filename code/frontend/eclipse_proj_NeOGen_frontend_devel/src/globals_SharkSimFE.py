'''
Created on 29 Jan 2015

@author: Dean C Blower
'''
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< RELEASE INFO
from version import version
__project__ = version.__project__
__author__ = version.__author__
__version__ = version.__version__
__date__ = version.__date__
__copyright__ = version.__copyright__
__license__ = version.__license__
#------------------< Import python modules
from datetime import datetime
#
#------------------< Import DCB_General modules
#
#------------------< Import SharkSim modules
#
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DECLARATIONS
global_dateTimeLastGeneralMessage = datetime
#
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
class globalsSSFE(object):

    class Debug(object):
         
        static_global_Debug = False

    class Parameter_Group(object):
        
        static_str__Parameter_Group__OBJECT_SPECIFIC_PARAM = 'OBJECT_SPECIFIC_PARAM'
        
        static_str__Parameter_Group__BATCH_SCENARIO_PARAM = 'BATCH_SCENARIO_PARAM'
        static_str__Parameter_Group__SAMPLING_STRATEGY_PARAM = 'SAMPLING_STRATEGY_PARAM'
            
    class Parameter_Status(object):
        
        static_str__Parameter_Status__FLAG__REQUIRES_USER_EDIT = '*'
        
        static_str__Parameter_Status__BS_REQUIRES_USER_EDIT = 'BS_REQUIRES_USER_EDIT'
        static_str__Parameter_Status__BS_EDITED_BY_USER = 'BS_EDITED_BY_USER'
        static_str__Parameter_Status__BS_USER_ADD_EDIT_WARNING_COUNT__OBJECT_SPECIFIC = 'BS_USER_ADD_EDIT_WARING_COUNT__OBJECT_SPECIFIC'
        static_str__Parameter_Status__BS_USER_ZERO_EDIT_WARNING_COUNT__OBJECT_SPECIFIC = 'BS_USER_ZERO_EDIT_WARING_COUNT__OBJECT_SPECIFIC'
                
        static_str__Parameter_Status__SS_REQUIRES_USER_EDIT = 'SS_REQUIRES_USER_EDIT'
        static_str__Parameter_Status__SS_EDITED_BY_USER = 'SS_EDITED_BY_USER'
        static_str__Parameter_Status__SS_USER_ADD_EDIT_WARNING_COUNT__OBJECT_SPECIFIC = 'SS_USER_ADD_EDIT_WARING_COUNT__OBJECT_SPECIFIC'
        static_str__Parameter_Status__SS_USER_ZERO_EDIT_WARNING_COUNT__OBJECT_SPECIFIC = 'SS_USER_ZERO_EDIT_WARING_COUNT__OBJECT_SPECIFIC'
        
        static_str__Parameter_Status__Key__Status = 'Status'
        static_str__Parameter_Status__Key__Label = 'Label'
        static_str__Parameter_Status__Key__Edit_Warning_Count__Object_Specific = 'Edit_Warning_Count__Object_Specific'
        
#         static_str__App_Path_Prefix__Project = 'P'
#         static_str__App_Path_Prefix__Batch_Scenario = 'BS'
#         static_str__App_Path_Prefix__Sampling_Strategy = 'SS'
#         
#         static_str__App_Path_Prefix__Results = 'results'
#         static_str__App_Path_Prefix__Result_Plots = 'plots'
#         static_str__App_Path_Prefix__Result_Thumnail_Images = 'thumbs'
        pass
    
    class App_Path(object):
        
#         static_str__App_Path_Prefix__Projects = 'PS'
#         static_str__App_Path_Prefix__Project = 'P'
#         static_str__App_Path_Prefix__Batch_Scenario = 'BS'
#         static_str__App_Path_Prefix__Sampling_Strategy = 'SS'
#         
#         static_str__App_Path_Prefix__Results = 'results'
#         static_str__App_Path_Prefix__Result_Plots = 'plots'
#         static_str__App_Path_Prefix__Result_Thumnail_Images = 'thumbs'
        pass
        
    class App_File(object):
        
        static_str__App_File_Prefix__Settings = 'Settings'
        static_str__App_File_Prefix__Projects = 'Projects'
        static_str__App_File_Prefix__Project = 'Project'
        static_str__App_File_Prefix__Batch_Scenario = 'Batch_Scenario'
        static_str__App_File_Prefix__Batch_Settings = 'Batch_Settings'
        static_str__App_File_Prefix__Sampling_Strategy = 'Sampling_Strategy'

        static_str__App_File_Name__Thumbnail = 'thumb'
        
        static_str__App_File_Extension__Config_File = 'ini'
#         static_str__App_File_Extension__Image_File = 'png'

    class Exe_File(object):
        
        static_str__App_File_Extension__Windows_DOS_Batch_File = 'bat'

    class Run_Status(object):
        
        static_str_Run_Status_File_Prefix = 'SS_Run'
        
    class Name(object):
        
        static_str__Name__Project = 'PR'
        static_str__Name__Batch_Scenario = 'SC'
        static_str__Name__Sampling_Strategy = 'SS'
                                
    class Logger_Run_Display(object):
        
        bool_Run_Display = True #You will not want to turn this off.
        
        static_Logger_File_Name__Run_Display = 'Run_Display_Log'
        static_Logger_Name__Run_Display = 'log_Run_Display'
        static_Logger_File_Suffix__Run_Display = '.log_Run_Display_ssim'
        
    class Logger_Default_Display(object):
        
        bool_Default_Display = True #You will not want to turn this off.
        
        static_Logger_File_Name__Default_Display = 'Default_Display_Log'
        static_Logger_Name__Default_Display = 'log_Default_Display'
        static_Logger_File_Suffix__Default_Display = '.log_Default_Display_ssim'
        
        static_Logger_bool_LogToConsole = True
        static_Logger_bool_LogToFile = True #You will not want to turn this off.
        
    class Logger_Error_Display(object):
        
        bool_Error_Display = True #You will not want to turn this off.
        
        static_Logger_File_Name__Error_Display = 'Error_Display_Log'
        static_Logger_Name__Error_Display = 'log_Error_Display'
        static_Logger_File_Suffix__Error_Display = '.log_Error_Display_ssim'

        static_Logger_bool_LogToConsole = False
        static_Logger_bool_LogToFile = False
        
        static_str_Logger_Message_Prefix = '!!ERR!!; '
        
    class Logger_Debug_Display(object):
        
        bool_Debug_Display = True #You will not want to turn this off.
        
        static_Logger_File_Name__Debug_Display = 'Debug_Display_Log'
        static_Logger_Name__Debug_Display = 'log_Debug_Display'
        static_Logger_File_Suffix__Debug_Display = '.log_Debug_Display_ssim'

        static_Logger_bool_LogToConsole = True
        static_Logger_bool_LogToFile = True #You will not want to turn this off.
        
        static_str_Logger_Message_Prefix = '>>; '
        
    class Logger_Debug_Timing(object):
        
        bool_Debug_Timing_Override = False #Use this to just create the logger and use manually placed timers in the code
        
        bool_Debug_Timing = False #Use this to display timings on all functions that has this standard debug timer
        
        bool_Debug_Timing__Pause = False
        
        static_Logger_File_Name__Debug_Timing = 'Debug_Timing_Log'
        static_Logger_Name__Debug_Timing = 'log_Debug_Timing'
        static_Logger_File_Suffix__Debug_Timing = '.log_Debug_Timing_ssim'

    class Logger_Debug_Events_RETIRE(object):
        
        bool_Debug_Events = False
        
        static_Logger_File_Name__Debug_Events = 'Debug__Events_Log'
        static_Logger_Name__Debug_Events = 'log_Debug__Events'
        static_Logger_File_Suffix__Debug_Events = '.log_Debug__Events_ssim'

        static_Logger_bool_LogToConsole = True
        static_Logger_bool_LogToFile = False

        static_str_Logger_Message_Prefix = '>>; '

    class Output_Display_Constants(object):
        
        static_str_Message_Separator = '-------------------------------------------------------------------------------------'        
        static_str_Message_Header = 'MH-------------------------------------------------------------------------------------MH'        
        static_str_Message_Footer = 'MF-------------------------------------------------------------------------------------MF'        

    class StringDelimiters(object):
        
        static_stringDelimiter = ';'
        static_stringDelimiter1 = '_'
        static_stringDelimiter2 = ','
        static_stringDelimiter3 = '|'
        static_stringDelimiterTAB = '\t'
        static_stringDelimiterSPACE = ' '
        static_stringDelimiter_SPACE = ' '
        static_stringDelimiter_RESULTS_START = '<>'
        static_stringDelimiter_DOT = '.'
        static_stringDelimiter_UNDERSCORE = '_'
        static_stringDelimiter_HYPHEN = '-'
        static_stringDelimiter_SEMI_COLON = ';'
        static_stringDelimiter_COMMA = ','
        
    class StringUnexpectedResults(object):
        
        static_stringError_Reporting_IDNotFound = 'ID_NOT_FOUND'
        static_stringNotApplicable = 'NA'
        static_stringSuppressed = 'SUP'
        static_stringError_ReportingPropertyNameNotFound = 'PROP NAME NOT FOUND'
        static_stringError_ReportingPropertyObjectNotFound = 'PROP NOT FOUND'
        static_stringError_ReportingPropertyLabelsNotFound = 'PROP LABELS NOT FOUND'

    class Main_Form_QToolBox_Tab_Index(object):
        
        static_int_Main_Form_QToolBox_Tab_Index__Admin = 0
        static_int_Main_Form_QToolBox_Tab_Index__Select_Project_And_Scenario = 1 #0
        static_int_Main_Form_QToolBox_Tab_Index__Modify_Scenario = 2 #1
        static_int_Main_Form_QToolBox_Tab_Index__Run_Scenario = 3 #2
        static_int_Main_Form_QToolBox_Tab_Index__View_Results_Scenario = 4 #3
        static_int_Main_Form_QToolBox_Tab_Index__Create_Sampling_Strategy = 5 #4
        static_int_Main_Form_QToolBox_Tab_Index__Modify_Sampling_Strategy = 6 #4
        static_int_Main_Form_QToolBox_Tab_Index__Run_Sampling_Strategy = 7 #5
        static_int_Main_Form_QToolBox_Tab_Index__View_Results_Sampling_Strategy = 8 #6
        
    class Age_Cohort_Group(object): 
        
        static_int_Age_Cohort__Juveniles = 1
        static_int_Age_Cohort__Adults = 2
        