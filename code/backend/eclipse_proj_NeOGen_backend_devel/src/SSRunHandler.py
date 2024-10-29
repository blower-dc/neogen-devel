'''
Created on 25/01/2016

@author: Dean
'''
'''
-----------------------------------------------
                RELEASE INFO
-----------------------------------------------
'''
#------------------------------------< Import app details modules
from version import version as app_details
'''
-----------------------------------------------
                PACKAGE IMPORTS
-----------------------------------------------
'''
#------------------------------------< Import python modules
from logging import getLogger as logging__getLogger
from datetime import datetime
from os import path as os__path
import sys
#
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS
#------------------< Import python modules
from datetime import datetime
from logging import getLogger as logging__getLogger
from os import path as os__path
from os import getcwd as os__getcwd
from os import extsep as os__extsep
import sys
#------------------< Import DCB_General modules
from globals_DCB_General import globalsDCBGen
from FileHandler import FileHandler
from handler_Logging import Logging
#------------------< Import SharkSim modules
#from globals_SharkSim import globalsSS
from SSBatchHandler import SSBatchOperation
from SSParameterHandler import SSParameterHandler
from SSOutputHandler import SSOutputHandler
import globals_SharkSim 
from globals_SharkSim import globalsSS
#from globals_SharkSimFE import globalsSSFE
from SSErrorHandler import SSErrorOperation
from SSConfigHandler import SSConfigOperation
from object_SSConfigSamplingStrategy import object_SSConfigSamplingStrategy
from object_SSConfigBatchScenario import object_SSConfigBatchScenario
from object_SSConfigBatchSettings import object_SSConfigBatchSettings
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
gstringModuleName='SSRunHandler.py'
gstringClassName='SSRunOperation'

class SSRunOperation(object):

    def __enter__(self):
    
        return self
    
    def __init__(self, tup_Command_Line_Args):

        self.tup_Command_Line_Args = tup_Command_Line_Args
        bool_App_Started_From_Command_Line, str_App_Run_Path_And_File, str_App_Arg_Output_Base_Path, str_App_Arg_Config_Path_And_File, list_int_App_Arg_Run_Processing_Steps, list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use = self.tup_Command_Line_Args

        self.obj_Log_Run_Display = None
        self.obj_Log_Default_Display = None
        
        self.bool_App_Started_From_Command_Line = bool_App_Started_From_Command_Line
        self.str_App_Run_Path_And_File = str_App_Run_Path_And_File
        self.str_App_Arg_Output_Base_Path = str_App_Arg_Output_Base_Path
        self.str_App_Arg_Config_Path_And_File = str_App_Arg_Config_Path_And_File
        self.list_int_App_Arg_Run_Processing_Steps = list_int_App_Arg_Run_Processing_Steps
        self.list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use = list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use
        
        self.obj_SSParams = None


    
        #DEBUG_ON
        #raw_input("\n Press return to continue... \n")
        #import time
        #time.sleep(5) # delays for 5 seconds        
        #DEBUG_OFF  
                    
        return None
    
    def method_Initialize_Loggers(self):

        ''' Get Run Display Logger '''
        self.obj_Log_Run_Display = None
        if globalsSS.Logger_Run_Display.bool_Run_Display:
            obj_Logging = Logging()
            obj_Logging.strLogFile = self.obj_SSParams.strUniqueRunID + '__' + globalsSS.Logger_Run_Display.static_Logger_File_Name__Run_Display + globalsSS.Logger_Run_Display.static_Logger_File_Suffix__Run_Display
            obj_Logging.strLogPath = self.obj_SSParams.str_Current_Run_Path__Logs
            obj_Logging.bool_LogToConsole = True
            obj_Logging.bool_LogToFile = True
            obj_Logging.str_Logger_Name = globalsSS.Logger_Run_Display.static_Logger_Name__Run_Display 
            obj_Logging.str_Logger_Level = 'info'
            obj_Logging.func_Initialise_New_Logger()
            self.obj_Log_Run_Display = logging__getLogger(globalsSS.Logger_Run_Display.static_Logger_Name__Run_Display)
            self.obj_Log_Run_Display.info('Log initialised: ' + globalsSS.Logger_Run_Display.static_Logger_File_Name__Run_Display)
        pass
        ''' Get Default Display Logger '''
        self.obj_Log_Default_Display = None
        if globalsSS.Logger_Default_Display.bool_Default_Display:
            obj_Logging = Logging()
            obj_Logging.strLogFile = self.obj_SSParams.strUniqueRunID + '__' + globalsSS.Logger_Default_Display.static_Logger_File_Name__Default_Display + globalsSS.Logger_Default_Display.static_Logger_File_Suffix__Default_Display
            obj_Logging.strLogPath = self.obj_SSParams.str_Current_Run_Path__Logs
            obj_Logging.bool_LogToConsole = globalsSS.Logger_Default_Display.static_Logger_bool_LogToConsole
            obj_Logging.bool_LogToFile = globalsSS.Logger_Default_Display.static_Logger_bool_LogToFile
            obj_Logging.str_Logger_Name = globalsSS.Logger_Default_Display.static_Logger_Name__Default_Display 
            obj_Logging.str_Logger_Level = 'info'
            obj_Logging.func_Initialise_New_Logger()
            '''NOTE: Get this logger to display info '''
#             self.obj_Log_Default_Display = logging__getLogger(globalsSSFE.Logger_Default_Display.static_Logger_Name__Default_Display)
#             self.obj_Log_Default_Display.info('Log initialised: ' + globalsSSFE.Logger_Default_Display.static_Logger_File_Name__Default_Display)
            self.obj_Log_Default_Display = logging__getLogger(globalsSS.Logger_Default_Display.static_Logger_Name__Default_Display)
            self.obj_Log_Default_Display.info('Log initialised: ' + globalsSS.Logger_Default_Display.static_Logger_File_Name__Default_Display)
        pass
        ''' Get Debug Timing Logger '''
        self.obj_Log_Debug_Timing = None
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing or globalsSS.Logger_Debug_Timing.bool_Debug_Timing_Override:
            obj_Logging = Logging()
            obj_Logging.strLogFile = self.obj_SSParams.strUniqueRunID + '__' + globalsSS.Logger_Debug_Timing.static_Logger_File_Name__Debug_Timing + globalsSS.Logger_Debug_Timing.static_Logger_File_Suffix__Debug_Timing
            obj_Logging.strLogPath = self.obj_SSParams.str_Current_Run_Path__Logs
            obj_Logging.bool_LogToConsole = True
            obj_Logging.bool_LogToFile = True
            obj_Logging.str_Logger_Name = globalsSS.Logger_Debug_Timing.static_Logger_Name__Debug_Timing 
            obj_Logging.str_Logger_Level = 'debug'
            obj_Logging.func_Initialise_New_Logger()
            self.obj_Log_Default_Display.info('Log initialised: ' + globalsSS.Logger_Debug_Timing.static_Logger_File_Name__Debug_Timing)
        pass
        ''' Get Debug Display Logger '''
        self.obj_Log_Debug_Display = None
        if globalsSS.Logger_Debug_Display.bool_Debug_Display:
            obj_Logging = Logging()
            obj_Logging.strLogFile = self.obj_SSParams.strUniqueRunID + '__' + globalsSS.Logger_Debug_Display.static_Logger_File_Name__Debug_Display + globalsSS.Logger_Debug_Display.static_Logger_File_Suffix__Debug_Display
            obj_Logging.strLogPath = self.obj_SSParams.str_Current_Run_Path__Logs
            obj_Logging.bool_LogToConsole = globalsSS.Logger_Debug_Display.static_Logger_bool_LogToConsole
            obj_Logging.bool_LogToFile = globalsSS.Logger_Debug_Display.static_Logger_bool_LogToFile
            obj_Logging.str_Logger_Name = globalsSS.Logger_Debug_Display.static_Logger_Name__Debug_Display 
            obj_Logging.str_Logger_Level = 'debug'
            obj_Logging.func_Initialise_New_Logger()
            '''NOTE: Get this logger to display info '''
            self.obj_Log_Debug_Display = None
#             self.obj_Log_Debug_Display = logging__getLogger(globalsSSFE.Logger_Debug_Display.static_Logger_Name__Debug_Display)
#             self.obj_Log_Debug_Display.info('Log initialised: ' + globalsSSFE.Logger_Debug_Display.static_Logger_File_Name__Debug_Display)   
            self.obj_Log_Debug_Display = logging__getLogger(globalsSS.Logger_Debug_Display.static_Logger_Name__Debug_Display)
            self.obj_Log_Debug_Display.info('Log initialised: ' + globalsSS.Logger_Debug_Display.static_Logger_File_Name__Debug_Display)   

        pass
        ''' Get Debug AgeNe Logger '''
        self.obj_Log_Debug_AgeNe = None
        if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
            obj_Logging = Logging()
            obj_Logging.strLogFile = self.obj_SSParams.strUniqueRunID + '__' + globalsSS.Logger_Debug_AgeNe.static_Logger_File_Name__Debug_AgeNe + globalsSS.Logger_Debug_AgeNe.static_Logger_File_Suffix__Debug_AgeNe
            obj_Logging.strLogPath = self.obj_SSParams.str_Current_Run_Path__Logs
            obj_Logging.bool_LogToConsole = globalsSS.Logger_Debug_AgeNe.static_Logger_bool_LogToConsole
            obj_Logging.bool_LogToFile = globalsSS.Logger_Debug_AgeNe.static_Logger_bool_LogToFile
            obj_Logging.str_Logger_Name = globalsSS.Logger_Debug_AgeNe.static_Logger_Name__Debug_AgeNe 
            obj_Logging.str_Logger_Level = 'debug'
            obj_Logging.func_Initialise_New_Logger()
            self.obj_Log_Default_Display.info('Log initialised: ' + globalsSS.Logger_Debug_AgeNe.static_Logger_File_Name__Debug_AgeNe)
        pass

        return True
    
    def method_Parameter_Initializaton(self):
        
        '''
        Create an SSParameter object - All the run/batch/replicate parameters are contained within the parameters object
        '''
        objSSParameters = None

        with SSParameterHandler() as objSSParameters:
            '''
            Initialise Global Variable General Message DateTime
            '''
            globals_SharkSim.global_dateTimeLastGeneralMessage = datetime.now()
            objSSParameters.dateSimRunStartTime = datetime.now()
        pass

    
        return objSSParameters
    
    def func_Get_Local_Copy_Of_Config_Files(self, str_File_Name__Copy_Pattern):
        
        bool_Success = False
        
        ''' Copy  config files to working folder '''
        with FileHandler() as obj_FileOp:
        
            bool_Success = obj_FileOp.method_Path_Exists(self.str_App_Arg_Output_Base_Path)
            if bool_Success:
                bool_Success = False
                #str_Path__File_Copy_Source, _ = os__path.split(self.str_App_Arg_Config_Path_And_File)
                str_Path__File_Copy_Source = self.str_App_Arg_Output_Base_Path
                str_Path__File_Copy_Destination = self.obj_SSParams.str_Current_Run_Path
                bool_Success = obj_FileOp.method_Copy_Files_By_Pattern(str_Path__File_Copy_Source, str_Path__File_Copy_Destination, str_File_Name__Copy_Pattern)
            else:
                with SSErrorOperation([]) as obj_SSErrorOp:
                    str_Message_Text = 'Job Output Base Path does not exist: ' + self.str_App_Arg_Output_Base_Path
                    int_Stack_Trace_Level = 2
                    obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
                pass
            pass   
        pass

        return bool_Success

    def method_Locate_Batch_Scenario_Run_Folder_RETIRE(self):
    
        ''' Locate the Batch Scenario run -  It should be the only SS_*_Run FOLDER in the command line entered base path '''
        
        str_Search_Path = self.obj_SSParams.str_App_Arg_Output_Base_Path
        with FileHandler() as obj_FileOp:
            bool_Success = obj_FileOp.method_Path_Exists(str_Search_Path)
            if bool_Success:
                bool_Success = False
                str_Folder_Search_Pattern = app_details.str_Project__Prefix + '_*_Run_*'
                bool_Folders_Found, list_Folders_Found = obj_FileOp.func_Locate_Folders(str_Search_Path, str_Folder_Search_Pattern, bool_Print_Search_Result = False, bool_Search_Sub_Folders = False)
                if bool_Folders_Found:
                    if len(list_Folders_Found) == 1:
                        #self.obj_SSParams.str_Batch_Scenario_UID_Folder__Previous_Run = list_Folders_Found[0]
                        str_Batch_Scenario_UID_Folder__Previous_Run = list_Folders_Found[0]
                        bool_Success = True
                    else:
                        with SSErrorOperation([]) as obj_SSErrorOp:
                            str_Message_Text = 'Only one Batch Scenario run folder can be processed. ' + str(len(list_Folders_Found)) + ' folders found with search pattern: ' + str_Folder_Search_Pattern + ' ; found on search path: ' + str_Search_Path + '\n' + '\n'.join(list_Folders_Found)
                            int_Stack_Trace_Level = 2
                            obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
                        pass
                    pass
                else:
                    with SSErrorOperation([]) as obj_SSErrorOp:
                        str_Message_Text = 'Folders of this search pattern: ' + str_Folder_Search_Pattern + ' ; Could not be found on search path: ' + str_Search_Path
                        int_Stack_Trace_Level = 2
                        obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
                    pass 
                pass
            else:
                with SSErrorOperation([]) as obj_SSErrorOp:
                    str_Message_Text = 'Job Output Base Path does not exist: ' + self.str_App_Arg_Output_Base_Path
                    int_Stack_Trace_Level = 2
                    obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
                pass
            pass 
        pass
                    
        return bool_Success, str_Batch_Scenario_UID_Folder__Previous_Run

    def method_Locate_Batch_Scenario_Run_Folder(self):
    
        ''' Locate the Batch Scenario run -  It should be the only SS_*_Run FOLDER in the command line entered base path '''
        
        str_Search_Path = self.obj_SSParams.str_App_Arg_Output_Base_Path
        with FileHandler() as obj_FileOp:
            bool_Success = obj_FileOp.method_Path_Exists(str_Search_Path)
            if bool_Success:
                bool_Success = False
                str_Folder_Search_Pattern = app_details.str_Project__Prefix + '_*_Run_*'
                bool_Folders_Found, list_Folders_Found = obj_FileOp.func_Locate_Folders(str_Search_Path, str_Folder_Search_Pattern, bool_Print_Search_Result = False, bool_Search_Sub_Folders = False)
                if bool_Folders_Found:
                    ''' Note the BS run used '''
                    if len(list_Folders_Found) > 1:
                        ''' Sort list to always get the last run '''
                        list_Folders_Found.sort(reverse=True)
                        print('Multiple Batch Scenario Runs found. Using run: ' + str(list_Folders_Found[0]) + ' from runs: ' + str(list_Folders_Found) + ' on search path: ' + str_Search_Path)
                    else:
                        print('Single run found. Using run: ' + str(list_Folders_Found[0]) + ' on search path: ' + str_Search_Path)
                    pass
                    str_Batch_Scenario_UID_Folder__Previous_Run = list_Folders_Found[0]
                    bool_Success = True
                else:
                    with SSErrorOperation([]) as obj_SSErrorOp:
                        str_Message_Text = 'Folders of this search pattern: ' + str_Folder_Search_Pattern + ' ; Could not be found on search path: ' + str_Search_Path
                        int_Stack_Trace_Level = 2
                        obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
                    pass 
                pass
            else:
                with SSErrorOperation([]) as obj_SSErrorOp:
                    str_Message_Text = 'Job Output Base Path does not exist: ' + self.str_App_Arg_Output_Base_Path
                    int_Stack_Trace_Level = 2
                    obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
                pass
            pass 
        pass
                    
        return bool_Success, str_Batch_Scenario_UID_Folder__Previous_Run


    def method_Locate_Batch_Scenario_Run_Folder_From_Batch_Settings_Config_File(self):

        bool_Success = False
        
        ''' From the known local file and path, read the SAMPLING STRATEGY config file '''
        str_Config_Path_And_File = self.obj_SSParams.str_App_Arg_Config_Path_And_File__Original
        obj_Config = object_SSConfigSamplingStrategy()
        obj_Config_Sampling_Strategy = self.func_Read_Config_File(str_Config_Path_And_File, obj_Config)

        ''' Read the Batch Settings file using the Path and Filename from Batch Scenario '''
        if obj_Config.config_parser_Config == None:
            with SSErrorOperation([]) as obj_SSErrorOp:
                str_Message_Text = 'obj_Config_Sampling_Strategy.config_parser_Config == None for config file: ' + str_Config_Path_And_File
                int_Stack_Trace_Level = 2
                obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
            pass
            return False, '' 
        pass
               
        ''' <<<<<<< SECTION: Batch_Scenario '''
        bool_Section_Exists = False
        ''' Specify SECTION to get '''
        str_Section = obj_Config.static_str_Section__Sampling_Strategy_Batch_Scenario
        ''' Check if SECTION exists in config file '''
        bool_Section_Exists = obj_Config.func_Check_If_Config_File_SECTION_Is_Expected(obj_Config_Sampling_Strategy, str_Section, True)
        '''Its NOT OK if the SECTION does not exist, however if the SECTION exists, read the option '''
        if bool_Section_Exists:
            ''' Specify OPTION to get '''
            str_Option = obj_Config.static_str_Option__Sampling_Strategy_Scenario_File
            value_Type = ''
            '''Its NOT OK if the OPTION does not exist'''
            '''Read the OPTION'''
            bool_Option_Exists = False 
            bool_Option_Exists, value_Option = obj_Config.func_Read_OPTION(True, False, obj_Config, str_Section, str_Option, value_Type)
            if bool_Option_Exists:
                str_Batch_Scenario_File_Path_And_Name__Original = value_Option
            pass
        pass
        bool_Exists = bool_Section_Exists and bool_Option_Exists
        bool_str_Scenario_Batch_Scenario_File__Current__FOUND = bool_Exists

        if not bool_str_Scenario_Batch_Scenario_File__Current__FOUND:
            with SSErrorOperation([]) as obj_SSErrorOp:
                str_Message_Text = 'Unable read OPTION in config file: ' + str_Config_Path_And_File
                int_Stack_Trace_Level = 2
                obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
            pass
            return False, '' 
        pass
    
        _, str_Batch_Scenario_File_Name__Original = os__path.split(str_Batch_Scenario_File_Path_And_Name__Original)
        str_Config_Path_And_File = os__path.join(self.obj_SSParams.str_App_Arg_Output_Base_Path, str_Batch_Scenario_File_Name__Original)
        obj_Config = object_SSConfigBatchScenario()
        obj_Config = self.func_Read_Config_File(str_Config_Path_And_File, obj_Config)
    
        ''' Read the Batch Settings file using the Path and Filename from Batch Scenario '''
        if obj_Config.config_parser_Config == None:
            with SSErrorOperation([]) as obj_SSErrorOp:
                str_Message_Text = 'obj_Config_Batch_Scenario.config_parser_Config == None for config file: ' + str_Config_Path_And_File
                int_Stack_Trace_Level = 2
                obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
            pass
            return False, '' 
        pass
                
        ''' <<<<<<< SECTION: Batch_Settings '''
        bool_Section_Exists = False
        ''' Specify SECTION to get '''
        str_Section = obj_Config.static_str_Section__Scenario_Batch_Settings
        ''' Check if SECTION exists in config file '''
        bool_Section_Exists = obj_Config.func_Check_If_Config_File_SECTION_Is_Expected(obj_Config, str_Section, True)
        '''Its NOT OK if the SECTION does not exist, however if the SECTION exists, read the option '''
        if bool_Section_Exists:
            ''' Specify OPTION to get '''
            str_Option = obj_Config.static_str_Option__Scenario_Batch_Settings_File
            value_Type = ''
            '''Its NOT OK if the OPTION does not exist'''
            '''Read the OPTION'''
            bool_Option_Exists = False 
            bool_Option_Exists, value_Option = obj_Config.func_Read_OPTION(True, False, obj_Config, str_Section, str_Option, value_Type)
            if bool_Option_Exists:
                str_Batch_Settings_File_Path_And_Name__Original = value_Option
            pass
        pass
        bool_Exists = bool_Section_Exists and bool_Option_Exists
        bool_str_Scenario_Batch_Settings_File__Current__FOUND = bool_Exists

        if not bool_str_Scenario_Batch_Settings_File__Current__FOUND:
            with SSErrorOperation([]) as obj_SSErrorOp:
                str_Message_Text = 'Unable read OPTION in config file: ' + str_Config_Path_And_File
                int_Stack_Trace_Level = 2
                obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
            pass
            return False, '' 
        pass
    
        _, str_Batch_Settings_File_Name__Original = os__path.split(str_Batch_Settings_File_Path_And_Name__Original)
        str_Config_Path_And_File = os__path.join(self.obj_SSParams.str_App_Arg_Output_Base_Path, str_Batch_Settings_File_Name__Original)
        obj_Config = object_SSConfigBatchSettings()
        obj_Config = self.func_Read_Config_File(str_Config_Path_And_File, obj_Config)
    
        if obj_Config.config_parser_Config == None:
            with SSErrorOperation([]) as obj_SSErrorOp:
                str_Message_Text = 'obj_Config_Batch_Settings.config_parser_Config == None for config file: ' + str_Config_Path_And_File
                int_Stack_Trace_Level = 2
                obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
            pass
            return False, '' 
        pass
                            
        ''' <<<<<<< SECTION: Batch_Setting_Last_Batch_Scenario_Run_Details '''
        ''' Specify SECTION to get '''
        str_Section = obj_Config.static_str_Section__Batch_Setting_Last_Batch_Scenario_Run_Details
        ''' Check if SECTION exists in config file '''
        bool_Section_Exists = obj_Config.func_Check_If_Config_File_SECTION_Exists(obj_Config.config_parser_Config, str_Section)
        '''Its OK if the SECTION does not exist, however if the SECTION exists, read the option '''
        if bool_Section_Exists:
            ''' Specify OPTION to get '''
            str_Option = obj_Config.static_str_Option__Batch_Setting_Last_Batch_Scenario_Run_UID
            value_Type = ''
            '''Its NOT OK if the OPTION does not exist'''
            '''Read the OPTION'''
            bool_Option_Exists = False 
            bool_Option_Exists, value_Option = obj_Config.func_Read_OPTION(True, False, obj_Config, str_Section, str_Option, value_Type)
            if bool_Option_Exists:
                str_Batch_Setting_Last_Batch_Scenario_Run_UID = value_Option
            pass
        pass
        bool_Exists = bool_Section_Exists and bool_Option_Exists
        bool_str_Batch_Setting_Last_Batch_Scenario_Run_UID__FOUND = bool_Exists         
        
        str_Batch_Scenario_UID_Folder__Previous_Run = ''
        if bool_str_Batch_Setting_Last_Batch_Scenario_Run_UID__FOUND:
            str_Batch_Scenario_UID_Folder__Previous_Run = str_Batch_Setting_Last_Batch_Scenario_Run_UID
        pass
    
        return bool_Success, str_Batch_Scenario_UID_Folder__Previous_Run


    def func_Read_Config_File(self, str_Config_File_Path_And_Name, obj_Config):

        with SSConfigOperation(None) as obj_ConfigOp:
            with FileHandler() as obj_FileHandler:
                if obj_FileHandler.fileExists(str_Config_File_Path_And_Name):
                    obj_Config = obj_ConfigOp.func_Read_Any_Config_File(str_Config_File_Path_And_Name, obj_Config)
                    if obj_Config.config_parser_Config == None:
                        with SSErrorOperation([]) as obj_SSErrorOp:
                            str_Message_Text = 'obj_Config.config_parser_Config = None'
                            int_Stack_Trace_Level = 2
                            obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
                        pass
                    pass
                else:
                    with SSErrorOperation([]) as obj_SSErrorOp:
                        str_Message_Text = 'Non-existant config file: ' + str_Config_File_Path_And_Name
                        int_Stack_Trace_Level = 2
                        obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
                    pass
                pass
            pass
        pass
        return obj_Config

    def func_Disable_Native_Exception_Handling(self):
        ''' Intercept and handle uncaught exceptions TO ENABLE ERROR LOGGING TO FILE'''
        bool_Disable_Native_Exception_Handling = False
        if bool_Disable_Native_Exception_Handling:
            with SSErrorOperation([]) as obj_SSErrorOp:
                sys.excepthook = obj_SSErrorOp.func_Error_Handler__UNCaught_Exceptions
            pass
        pass
    
        return True
          
        
    def func_Run_Status(self, str_Run_Status_Base_Path, str_Run_Status):
        
        bool_Success = False

        str_Run_Status_Path_And_File = ''
        str_Run_Status_Path = os__path.join(str_Run_Status_Base_Path, globalsDCBGen.Run_Status.static_str_Run_Status__Path)
        str_Run_Status_Path_And_File = os__path.join(str_Run_Status_Path, self.obj_SSParams.strUniqueRunID + '.' + str_Run_Status)

        with FileHandler() as obj_FileOp:
            bool_Success = obj_FileOp.method_FileSystem_Prep_For_File_Save(str_Run_Status_Path_And_File, bool_Delete=True)
            
            if bool_Success:
                bool_Success = False
                fileHandle = obj_FileOp.fileOpen(str_Run_Status_Path_And_File, 'write')
                if fileHandle != None:
                    bool_Success = True
                else:
                    with SSErrorOperation([]) as obj_SSErrorOp:
                        str_Message_Text = 'Unable to create Run Status File : ' + str_Run_Status_Path_And_File
                        int_Stack_Trace_Level = 2
                        obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (str_Run_Status_Base_Path, self.obj_SSParams.strUniqueRunID))  
                    pass              
                pass
            pass
        pass
        
        return bool_Success   
    
    def func_Run_Start(self):    

        '''
        Set run wide parms
        '''
        #simu_pop.setOptions(numThreads=8, name='mt19937_1999', seed=0)
              
        self.method_Run_Initiation()
        
        return True
       
    def method_Run_Initiation(self):    

        '''
        Initialise simulation parameters prior to run
        '''
        #objSSParameters = self.method_Parameter_Initializaton()
        self.obj_SSParams = self.method_Parameter_Initializaton()
        #self.method_Run_Processing(objSSParameters)
        self.method_Run_Processing()
                  
        return True

            
    def method_Run_Processing(self):    
        
        
        '''
        -------------------------------------------
        Setup simulation run paths & parameters
        -------------------------------------------
        '''
        
        self.obj_SSParams.bool_App_Started_From_Command_Line = self.bool_App_Started_From_Command_Line
        self.obj_SSParams.str_App_Run_Path, self.obj_SSParams.str_App_Run_File = os__path.split(self.str_App_Run_Path_And_File)
        self.obj_SSParams.str_App_Arg_Output_Base_Path = self.str_App_Arg_Output_Base_Path
        self.obj_SSParams.str_App_Arg_Config_Path_And_File__Original = self.str_App_Arg_Config_Path_And_File
        self.obj_SSParams.list_int_App_Arg_Run_Processing_Steps = self.list_int_App_Arg_Run_Processing_Steps

        ''' 
        -------------------------------------------
        If this is a Sampling Strategy run, get the run UID folder that contains the Batch Scenario files
        For a Sampling Stratgy run the Batch Scenario Run UID folder must be located at the Output Base Path along with 
        the config and shell files
        -------------------------------------------
        '''
        ''' Check that only the Sampling STrategy processing step is requested, NOT the BS or multiple steps '''
        if len(self.obj_SSParams.list_int_App_Arg_Run_Processing_Steps) == 1:
            if globalsSS.Run_Processing_Step.static_int_Run_Processing_Step__SAMP_STRAT in self.obj_SSParams.list_int_App_Arg_Run_Processing_Steps: 
                bool_success = False
                
                if self.obj_SSParams.bool_App_Started_From_Command_Line:
                    bool_success, str_Batch_Scenario_UID_Folder__Previous_Run = self.method_Locate_Batch_Scenario_Run_Folder()
                else:
                    bool_success, str_Batch_Scenario_UID_Folder__Previous_Run = self.method_Locate_Batch_Scenario_Run_Folder_From_Batch_Settings_Config_File()
                pass
                self.obj_SSParams.str_Batch_Scenario_UID_Folder__Previous_Run = str_Batch_Scenario_UID_Folder__Previous_Run
            pass
        pass
    
        '''
        -------------------------------------------
        Set up run parameters such as the unique run ID
        -------------------------------------------
        '''
        self.obj_SSParams.method_Run_Pre_Processing__Application_Specs()
        self.obj_SSParams.method_Run_Pre_Processing__Environment_Specs()

        '''
        -------------------------------
        Run Status Update
        -------------------------------
        '''        
        #self.func_Run_Status(os__getcwd(), globalsDCBGen.Run_Status.static_str_Run_Status__STARTED)
        self.func_Run_Status(self.str_App_Arg_Output_Base_Path, globalsDCBGen.Run_Status.static_str_Run_Status__STARTED)

        '''
        -------------------------------
        More parameter initialisation
        -------------------------------
        '''        
        self.obj_SSParams.method_Simulation_Run_Level_Parameters_Initialization()


        '''
        -------------------------------
        Get copys of config files to use and archive in the current run path
        -------------------------------
        '''
        bool_Local_Copy_For_Archive = True
        bool_success = False
        if bool_Local_Copy_For_Archive:
            str_File_Name__Copy_Pattern = '*.ini'
            bool_Success = self.func_Get_Local_Copy_Of_Config_Files(str_File_Name__Copy_Pattern)        
            str_File_Name__Copy_Pattern = '*.bat'
            bool_Success = self.func_Get_Local_Copy_Of_Config_Files(str_File_Name__Copy_Pattern)        
        pass   
        _, str_Name__Config_File = os__path.split(self.str_App_Arg_Config_Path_And_File)
        self.obj_SSParams.str_App_Arg_Config_Path_And_File__Local = os__path.join(self.obj_SSParams.str_Current_Run_Path, str_Name__Config_File)    
     
        '''
        -------------------------------------------
        Get loggers
        -------------------------------------------
        '''
        self.method_Initialize_Loggers()
 
        '''
        -------------------------------------------
        Initialise RUN-WIDE ERROR HANDLING
        -------------------------------------------
        '''  
        self.func_Disable_Native_Exception_Handling()      
  
        '''
        -------------------------------------------
        Display Command Line info
        -------------------------------------------
        '''
        self.obj_Log_Default_Display.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
        self.obj_Log_Default_Display.info('>>>> Command Line Arguments <<<<')
        #self.obj_Log_Run_Display.info('Arguments list: ' + str(self.tup_Command_Line_Args))
        #self.obj_Log_Run_Display.info('Arguments:')
        self.obj_Log_Default_Display.info('Config_INI_Path_And_File: ' + self.str_App_Arg_Config_Path_And_File)
        self.obj_Log_Default_Display.info('Output_Path: ' + self.str_App_Arg_Output_Base_Path)
        self.obj_Log_Default_Display.info('Processing_Step: ' + str(self.list_int_App_Arg_Run_Processing_Steps))
        self.obj_Log_Default_Display.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)

        '''
        -------------------------------------------
        Display Environment info
        -------------------------------------------
        '''
        self.obj_Log_Run_Display.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
        self.obj_Log_Run_Display.info('SIM Run Started: ')
        self.obj_Log_Run_Display.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)

        ''' Display current simuPOP debug options '''
        with SSOutputHandler() as objSSOutputOperation:
            objSSOutputOperation.method_Log_Output__SimuPopEnvironmentInfo(self.obj_Log_Default_Display)
            #raw_input("\n Review SimuPop environment information. Press return to close this window... \n")
        pass
    
        '''
        ----------------------------------------------------------------------------
        Start Run Processing - Process each batch - Comprising multiple replicates
        ----------------------------------------------------------------------------
        '''
        self.obj_Log_Run_Display.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
        self.obj_Log_Run_Display.info('SIM Batch Processing Initiated: ')
        self.obj_Log_Run_Display.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
        
        #DEBUG_ON 
        #For testing - The following Crashes program with unhandled exception error    
        #with SSBatchOperation as obj_Batch:
        #DEBUG_OFF
        with SSBatchOperation([self.obj_SSParams]) as obj_Batch:
            obj_Batch.method_Batch_Processing()
        pass
    
        '''
        ----------------------------------------------------------------------------
        Run processing ended
        ----------------------------------------------------------------------------
        '''
        ''' Log finishing datetime and time for complete run '''
        self.obj_SSParams.dateSimRunFinishTime = datetime.now()
        dateTimeRunTime = self.obj_SSParams.dateSimRunFinishTime - self.obj_SSParams.dateSimRunStartTime

        self.obj_Log_Run_Display.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
        self.obj_Log_Run_Display.info('SIM : Started: ' + self.obj_SSParams.dateSimRunStartTime.strftime("%Y-%m-%d %H:%M:%S"))
        self.obj_Log_Run_Display.info('SIM : Finished: ' + self.obj_SSParams.dateSimRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
        self.obj_Log_Run_Display.info('SIM : Took: ' + str(dateTimeRunTime))
        self.obj_Log_Run_Display.info('SIM Output Folder: ' + self.obj_SSParams.str_Current_Run_Path)
        self.obj_Log_Run_Display.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)

        '''
        -------------------------------
        Run Finalisation - Run status Update & close files
        -------------------------------
        '''
        #self.func_Run_Status(os__getcwd(), globalsDCBGen.Run_Status.static_str_Run_Status__ENDED)
        self.func_Run_Status(self.str_App_Arg_Output_Base_Path, globalsDCBGen.Run_Status.static_str_Run_Status__ENDED)
           
        #raw_input('pausing...')  

        ''' Close loggers '''
        self.obj_Log_Default_Display.handlers = []
        self.obj_Log_Run_Display.handlers = []
                  
        return True

          
    def __exit__(self, type, value, traceback): 

#         ''' Ensure loggers are closed at run end so no file handles are left open'''
#         ''' Close loggers '''
#         if self.obj_Log_Default_Display != None:
#             self.obj_Log_Default_Display.handlers = []
#         pass
#         if self.obj_Log_Run_Display != None:
#             self.obj_Log_Run_Display.handlers = []
#         pass

    
        return None
        
    '''            
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS FINALIZATION
    '''
