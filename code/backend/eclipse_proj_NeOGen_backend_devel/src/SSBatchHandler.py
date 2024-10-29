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
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS

#------------------< Import python modules
from datetime import datetime
import sys
from os import path as os__path
from memory_profiler import profile
from logging import getLogger as logging__getLogger
#------------------< Import DCB_General modules
from FileHandler import FileHandler
from handler_Logging import Logging
#------------------< Import SharkSim modules
#from SSReplicateHandler import SSReplicateHandler
from SSReplicateHandler import SSReplicateOperation
#from SSParameterHandler import SSParameterHandler
from SSOutputHandler import SSOutputHandler
from globals_SharkSim import globalsSS
#from globals_SharkSimFE import globalsSSFE
from SSErrorHandler import SSErrorOperation
from SSConfigHandler import SSConfigOperation
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
gstringModuleName='SSBatchHandler.py'
gstringClassName='SSBatchOperation'

# class SSBatchHandler(object):
#     """Handle FileOperation objects"""
#     def __enter__(self):
#         
#         def __init__(self):
#             
#             pass
#         
class SSBatchOperation(object):

    def __enter__(self):
    
        return self
    
    
    def __init__(self, list_Params):

        #self.obj_Log_Default = logging__getLogger(__name__)
        #self.obj_Log_Debug = logging__getLogger('app_debug')                

        objSSParameters = list_Params[0]
        self.obj_SSParams = objSSParameters
        
        self.obj_Log_RD = logging__getLogger(globalsSS.Logger_Run_Display.static_Logger_Name__Run_Display)
    
        return None


    def method_Batch_Processing(self):    
        
        '''
        -------------------------------------
        Process each batch - Comprising multiple replicates
        -------------------------------------
        '''
        
        intCurrentBatch = 0
        
        for int_Current_Batch in range(0, self.obj_SSParams.intBatches):

            '''
            -------------------------------------
            Read the Batch config files to get the batch initialisation info
            -------------------------------------
            '''
    
            '''
            -------------------
            REad or Test INI files
            -------------------
            '''
            bool_Create_INI_Files = False
            if bool_Create_INI_Files:
                self.method_Create_Config_Files() 
                 
                ''' abort SS '''
                sys.exit()     
            else:
                self.method_Read_Batch_Config_Files()
            pass
        
        
            self.obj_SSParams.dateBatchRunStartTime = datetime.now()

#             with SSOutputHandler() as SSOutputOperation:
#                 listOutputDestinations = ['console', self.obj_SSParams.outputFileNameSummaryLogAllBatches, self.obj_SSParams.outputFileNameTimingSummaryLogAllBatches]
#                 SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Batch Started', boolIsHeader=True, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
#                             
            self.obj_Log_RD.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
            self.obj_Log_RD.info('Batch Started')
            self.obj_Log_RD.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
                            
            intCurrentBatch = intCurrentBatch + 1
            self.obj_SSParams.intCurrentBatch = intCurrentBatch

            '''
            -------------------------------------
            Start  processing this BATCH
            -------------------------------------
            '''
            self.obj_SSParams.method_Batch_Pre_Processing()

            
            '''
            -------------------------------------
            Process each replicate within a batch
            -------------------------------------
            '''
            with SSReplicateOperation([self.obj_SSParams]) as obj_SSReplicate:
                obj_SSReplicate.method_Replicate_Processing()

                #DEBUG_ON
                #Check that garbage collection is working
                #intCollected = gc.collect()
                #with SSOutputHandler() as SSOutputOperation:
                #    listOutputDestinations = ['console', obself.obj_SSParamsutputFileNameSummaryLogAllBatches]
                #    SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, "Garbage collector: collected %d objects." % (intCollected))
                #print("Garbage collector: collected %d objects." % (intCollected))
                #raw_input("\n Check RAM... \n")
                #DEBUG_OFF
            pass
        
            '''
            -------------------------------------
            Batch processing finished
            -------------------------------------
            '''
            ''' Log finishing datetime and time for batch run '''
            self.obj_SSParams.dateBatchRunFinishTime = datetime.now()
    
            dateTimeRunTime = self.obj_SSParams.dateBatchRunFinishTime - self.obj_SSParams.dateBatchRunStartTime
#             with SSOutputHandler() as SSOutputOperation:
#                 #listOutputDestinations = ['console', outputFileNameSummaryLog]
#                 listOutputDestinations = ['console', self.obj_SSParams.outputFileNameSummaryLogAllBatches, self.obj_SSParams.outputFileNameTimingSummaryLogAllBatches]
#                 SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'Batch Run Started: ' + self.obj_SSParams.dateBatchRunStartTime.strftime("%Y-%m-%d %H:%M:%S"))
#                 SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'Batch Run Finished: ' + self.obj_SSParams.dateBatchRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
#                 SSOutputOperation.methodOutput_SimGeneralMessage(False, True, listOutputDestinations, 'Batch Run took: ' + str(dateTimeRunTime))

            self.obj_Log_RD.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
            self.obj_Log_RD.info('SIM BATCH: Started: ' + self.obj_SSParams.dateBatchRunStartTime.strftime("%Y-%m-%d %H:%M:%S"))
            self.obj_Log_RD.info('SIM BATCH: Finished: ' + self.obj_SSParams.dateBatchRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
            self.obj_Log_RD.info('SIM BATCH: Took: ' + str(dateTimeRunTime))
            self.obj_Log_RD.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
        
        pass

        return True

    def method_Read_Batch_Config_Files_RETIRE(self):
    
        with SSConfigOperation(self.obj_SSParams) as obj_ConfigOp:
            if self.obj_SSParams.bool_App_Started_From_Command_Line:
                obj_Config_Batch_Scenario = obj_ConfigOp.func_Verify_And_Read_Config_File__BATCH_SCENARIO(self.obj_SSParams.str_App_Arg_Config_Path_And_File__Local)
                self.obj_SSParams.obj_Config_Batch_Scenario = obj_Config_Batch_Scenario
                
                ''' Read the Batch Settings file using the Path and Filename from Batch Scenario '''
                if obj_Config_Batch_Scenario.config_parser_Config != None:
                    
                    ''' <<<<<<< SECTION: Batch_Settings '''
                    bool_Section_Exists = False
                    ''' Specify SECTION to get '''
                    str_Section = obj_Config_Batch_Scenario.static_str_Section__Scenario_Batch_Settings
                    ''' Check if SECTION exists in config file '''
                    bool_Section_Exists = obj_Config_Batch_Scenario.func_Check_If_Config_File_SECTION_Is_Expected(obj_Config_Batch_Scenario, str_Section, True)
                    '''Its NOT OK if the SECTION does not exist, however if the SECTION exists, read the option '''
                    if bool_Section_Exists:
                        ''' Specify OPTION to get '''
                        str_Option = obj_Config_Batch_Scenario.static_str_Option__Scenario_Batch_Settings_File
                        value_Type = ''
                        '''Its NOT OK if the OPTION does not exist'''
                        '''Read the OPTION'''
                        bool_Option_Exists = False 
                        bool_Option_Exists, value_Option = obj_Config_Batch_Scenario.func_Read_OPTION(True, False, obj_Config_Batch_Scenario, str_Section, str_Option, value_Type)
                        if bool_Option_Exists:
                            str_Batch_Settings_File_Path_And_Name__Original = value_Option
                        pass
                    pass
                    bool_Exists = bool_Section_Exists and bool_Option_Exists
                    bool_str_Scenario_Batch_Settings_File__Current__FOUND = bool_Exists
                    
                    if bool_str_Scenario_Batch_Settings_File__Current__FOUND:              
                        str_Path__Config_File, str_Name__Config_File = os__path.split(str_Batch_Settings_File_Path_And_Name__Original)
                        str_Batch_Settings_File_Path_And_Name__Local = os__path.join(self.obj_SSParams.str_Current_Run_Path, str_Name__Config_File)
                    pass
                    
                    ''' Read the Batch Settings config file '''
                    obj_Config_Batch_Settings = obj_ConfigOp.func_Verify_And_Read_Config_File__BATCH_SETTINGS(str_Batch_Settings_File_Path_And_Name__Local)  
                    if obj_Config_Batch_Settings.config_parser_Config != None:
                        self.obj_SSParams.obj_Config_Batch_Settings = obj_Config_Batch_Settings
                    pass
                
                if globalsSS.Run_Processing_Step.static_int_Run_Processing_Step__SAMP_STRAT in self.obj_SSParams.list_int_App_Arg_Run_Processing_Steps:
                    ''' Read the Sampling Strategy file using the Path and Filename from Batch Scenario '''
                    if obj_Config_Batch_Scenario.config_parser_Config != None:
                        
                        ''' <<<<<<< SECTION: Sampling_Strategy_Settings '''
                        bool_Section_Exists = False
                        ''' Specify SECTION to get '''
                        str_Section = obj_Config_Batch_Scenario.static_str_Section__Scenario_Sampling_Strategy_Settings
                        ''' Check if SECTION exists in config file '''
                        bool_Section_Exists = obj_Config_Batch_Scenario.func_Check_If_Config_File_SECTION_Is_Expected(obj_Config_Batch_Scenario, str_Section, True)
                        '''Its NOT OK if the SECTION does not exist, however if the SECTION exists, read the option '''
                        if bool_Section_Exists:
                            ''' Specify OPTION to get '''
                            str_Option = obj_Config_Batch_Scenario.static_str_Option__Scenario_Sampling_Strategy_Settings_File
                            value_Type = ''
                            '''Its NOT OK if the OPTION does not exist'''
                            '''Read the OPTION'''
                            bool_Option_Exists = False 
                            bool_Option_Exists, value_Option = obj_Config_Batch_Scenario.func_Read_OPTION(True, False, obj_Config_Batch_Scenario, str_Section, str_Option, value_Type)
                            if bool_Option_Exists:
                                str_Sampling_Strategy_File_Path_And_Name__Original = value_Option
                            pass
                        pass
                        bool_Exists = bool_Section_Exists and bool_Option_Exists
                        bool_str_Sampling_Strategy_Path_And_File__Current__FOUND = bool_Exists                             

                        if bool_str_Sampling_Strategy_Path_And_File__Current__FOUND:                          
                            str_Path__Config_File, str_Name__Config_File = os__path.split(str_Sampling_Strategy_File_Path_And_Name__Original)
                            str_Sampling_Strategy_File_Path_And_Name__Local = os__path.join(self.obj_SSParams.str_Current_Run_Path, str_Name__Config_File)
                        pass

                        ''' Read the Sampling Strategy config file '''
                        obj_Config_Sampling_Strategy = obj_ConfigOp.func_Verify_And_Read_Config_File__SAMPLING_STRATEGY(str_Sampling_Strategy_File_Path_And_Name__Local)  
                        if obj_Config_Sampling_Strategy.config_parser_Config != None:
                            self.obj_SSParams.obj_Config_Sampling_Strategy = obj_Config_Sampling_Strategy
                        pass
                    pass
            pass
        pass
    
        return True

    def method_Read_Batch_Config_Files_PREV(self):

        if globalsSS.Run_Processing_Step.static_int_Run_Processing_Step__POP_SIM in self.obj_SSParams.list_int_App_Arg_Run_Processing_Steps:
        
            with SSConfigOperation(self.obj_SSParams) as obj_ConfigOp:
                if self.obj_SSParams.bool_App_Started_From_Command_Line:
                    obj_Config_Batch_Scenario = obj_ConfigOp.func_Verify_And_Read_Config_File__BATCH_SCENARIO(self.obj_SSParams.str_App_Arg_Config_Path_And_File__Local)
                    self.obj_SSParams.obj_Config_Batch_Scenario = obj_Config_Batch_Scenario
                    
                    ''' Read the Batch Settings file using the Path and Filename from Batch Scenario '''
                    if obj_Config_Batch_Scenario.config_parser_Config != None:
                        
                        ''' <<<<<<< SECTION: Batch_Settings '''
                        bool_Section_Exists = False
                        ''' Specify SECTION to get '''
                        str_Section = obj_Config_Batch_Scenario.static_str_Section__Scenario_Batch_Settings
                        ''' Check if SECTION exists in config file '''
                        bool_Section_Exists = obj_Config_Batch_Scenario.func_Check_If_Config_File_SECTION_Is_Expected(obj_Config_Batch_Scenario, str_Section, True)
                        '''Its NOT OK if the SECTION does not exist, however if the SECTION exists, read the option '''
                        if bool_Section_Exists:
                            ''' Specify OPTION to get '''
                            str_Option = obj_Config_Batch_Scenario.static_str_Option__Scenario_Batch_Settings_File
                            value_Type = ''
                            '''Its NOT OK if the OPTION does not exist'''
                            '''Read the OPTION'''
                            bool_Option_Exists = False 
                            bool_Option_Exists, value_Option = obj_Config_Batch_Scenario.func_Read_OPTION(True, False, obj_Config_Batch_Scenario, str_Section, str_Option, value_Type)
                            if bool_Option_Exists:
                                str_Batch_Settings_File_Path_And_Name__Original = value_Option
                            pass
                        pass
                        bool_Exists = bool_Section_Exists and bool_Option_Exists
                        bool_str_Scenario_Batch_Settings_File__Current__FOUND = bool_Exists
                        
                        if bool_str_Scenario_Batch_Settings_File__Current__FOUND:              
                            str_Path__Config_File, str_Name__Config_File = os__path.split(str_Batch_Settings_File_Path_And_Name__Original)
                            str_Batch_Settings_File_Path_And_Name__Local = os__path.join(self.obj_SSParams.str_Current_Run_Path, str_Name__Config_File)
                        pass
                        
                        ''' Read the Batch Settings config file '''
                        obj_Config_Batch_Settings = obj_ConfigOp.func_Verify_And_Read_Config_File__BATCH_SETTINGS(str_Batch_Settings_File_Path_And_Name__Local)  
                        if obj_Config_Batch_Settings.config_parser_Config != None:
                            self.obj_SSParams.obj_Config_Batch_Settings = obj_Config_Batch_Settings
                        pass
                    pass
                pass
            pass
        pass
    
        if globalsSS.Run_Processing_Step.static_int_Run_Processing_Step__SAMP_STRAT in self.obj_SSParams.list_int_App_Arg_Run_Processing_Steps:
            ''' Read the Sampling Strategy file using the command lined entered base path '''
            str_Path__Config_Path, str_Path__Config_File = os__path.split(self.obj_SSParams.str_App_Arg_Config_Path_And_File__Local)




            
            str_Search_Path = self.obj_SSParams.str_App_Arg_Output_Base_Path
            with FileHandler() as obj_FileOp:
                bool_Success = obj_FileOp.method_Path_Exists(str_Search_Path)
                if bool_Success:
                    bool_Success = False
                    str_File_Search_Pattern = 'Sampling_Strategy_*.ini'
                    bool_Files_Found, list_Files_Found = obj_FileOp.func_Locate_Files(str_Search_Path, str_File_Search_Pattern, bool_Print_Search_Result = False, bool_Search_Sub_Folders = False)
                    if bool_Files_Found:
                        if len(list_Files_Found) == 1:
                            str_Sampling_Strategy_File_Path_And_Name__Local = list_Files_Found[0]
                            bool_Success = True
                        else:
                            with SSErrorOperation([]) as obj_SSErrorOp:
                                str_Message_Text = 'Only one file can be processed. More than one file found: \n' + '\n'.join(list_Files_Found)
                                int_Stack_Trace_Level = 2
                                obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
                            pass
                        pass
                    else:
                        with SSErrorOperation([]) as obj_SSErrorOp:
                            str_Message_Text = 'Files of this search pattern: ' + str_File_Search_Pattern + ' ; Could not be found on search path: ' + str_Search_Path
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
            
            if bool_Success:
                ''' Read the Sampling Strategy config file '''
                obj_Config_Sampling_Strategy = obj_ConfigOp.func_Verify_And_Read_Config_File__SAMPLING_STRATEGY(str_Sampling_Strategy_File_Path_And_Name__Local)  
                if obj_Config_Sampling_Strategy.config_parser_Config != None:
                    self.obj_SSParams.obj_Config_Sampling_Strategy = obj_Config_Sampling_Strategy
                pass
            pass
    
        return True
    
    def method_Read_Batch_Config_Files(self):

        bool_Success = False
        
        '''
        ---------------------------------------------------------------
        Find and read the config files required for the run in question
        The Bach_Scenario or Sampling_Strategy INI filename is always provided as a command line arg,...
        but to ensure flexibility of re-run (without having to edit the innards of the INI files)...
        the other required files are searched for on the Output Base path (also entered as command line arg)
        
        This requires that user ALWAYS provide the expected filename prefix for each of the INI files
        ---------------------------------------------------------------
        '''
        
        if globalsSS.Run_Processing_Step.static_int_Run_Processing_Step__POP_SIM in self.obj_SSParams.list_int_App_Arg_Run_Processing_Steps:
        
            bool_Success = False
            
            ''' From the known local file and path, read the BATCH SCENARIO config file '''
            str_Config_Path_And_File = self.obj_SSParams.str_App_Arg_Config_Path_And_File__Local
            bool_Success = self.func_Read_Config_File__Batch_Scenario(str_Config_Path_And_File)
            
            ''' The BATCH SETTING file is always read at the end of this function '''
        pass
    
        if globalsSS.Run_Processing_Step.static_int_Run_Processing_Step__SAMP_STRAT in self.obj_SSParams.list_int_App_Arg_Run_Processing_Steps:

            
            bool_Success = False
            
            if len(self.obj_SSParams.list_int_App_Arg_Run_Processing_Steps) == 1:
                
                bool_Success = False
                
                ''' From the known local file and path, read the SAMPLING STRATEGY config file '''
                str_Config_Path_And_File = self.obj_SSParams.str_App_Arg_Config_Path_And_File__Local
                bool_Success = self.func_Read_Config_File__Sampling_Strategy(str_Config_Path_And_File)
                
                if bool_Success:
                    bool_Success = False
                    
                    self.obj_SSParams.str_Config_Sampling_Strategy_Path_And_File__Local = str_Config_Path_And_File
                    
                    ''' Find & Read the BATCH SCENARIO config file '''
        
                    #str_Search_Path = self.obj_SSParams.str_App_Arg_Output_Base_Path
                    str_Search_Path, _ = os__path.split(self.obj_SSParams.str_App_Arg_Config_Path_And_File__Local)
                    #str_File_Search_Pattern = '*' + globalsSSFE.App_File.static_str__App_File_Prefix__Batch_Scenario + '*' + globalsSSFE.App_File.static_str__App_File_Extension__Config_File
                    str_File_Search_Pattern = '*' + globalsSS.App_File.static_str__App_File_Prefix__Batch_Scenario + '*' + globalsSS.App_File.static_str__App_File_Extension__Config_File
                    
                    bool_Success, self.obj_SSParams.str_Config_Batch_Scenario_Path_And_File__Local = self.func_Search_For_Config_Path_And_File(str_Search_Path, str_File_Search_Pattern)
                    
                    if bool_Success:
                        bool_Success = False
                        ''' Read the file '''
                        bool_Success = self.func_Read_Config_File__Batch_Scenario(self.obj_SSParams.str_Config_Batch_Scenario_Path_And_File__Local)
                    pass
                pass
            else:
                
                bool_Success = False
                
                ''' Find & Read the SAMPLING STRATEGY config file '''
                
                #str_Search_Path = self.obj_SSParams.str_App_Arg_Output_Base_Path
                str_Search_Path, _ = os__path.split(self.obj_SSParams.str_App_Arg_Config_Path_And_File__Local)
                #str_File_Search_Pattern = '*' + globalsSSFE.App_File.static_str__App_File_Prefix__Sampling_Strategy + '*' + globalsSSFE.App_File.static_str__App_File_Extension__Config_File
                str_File_Search_Pattern = '*' + globalsSS.App_File.static_str__App_File_Prefix__Sampling_Strategy + '*' + globalsSS.App_File.static_str__App_File_Extension__Config_File
                
                bool_Success, self.obj_SSParams.str_Config_Sampling_Strategy_Path_And_File__Local = self.func_Search_For_Config_Path_And_File(str_Search_Path, str_File_Search_Pattern)
                
                if bool_Success:
                    bool_Success = False
                    ''' Read the file '''
                    bool_Success = self.func_Read_Config_File__Sampling_Strategy(self.obj_SSParams.str_Config_Sampling_Strategy_Path_And_File__Local)
                pass
                
            pass
        pass
    
        if bool_Success:
            bool_Success = False
            ''' Find & Read the BATCH SETTINGS config file '''

            #str_Search_Path = self.obj_SSParams.str_App_Arg_Output_Base_Path
            str_Search_Path, _ = os__path.split(self.obj_SSParams.str_App_Arg_Config_Path_And_File__Local)
            #str_File_Search_Pattern = '*' + globalsSSFE.App_File.static_str__App_File_Prefix__Batch_Settings + '*' + globalsSSFE.App_File.static_str__App_File_Extension__Config_File
            str_File_Search_Pattern = '*' + globalsSS.App_File.static_str__App_File_Prefix__Batch_Settings + '*' + globalsSS.App_File.static_str__App_File_Extension__Config_File
            
            bool_Success, self.obj_SSParams.str_Config_Batch_Settings_Path_And_File__Local = self.func_Search_For_Config_Path_And_File(str_Search_Path, str_File_Search_Pattern)
            
            if bool_Success:
                bool_Success = False
                ''' Read the file '''
                bool_Success = self.func_Read_Config_File__Batch_Settings(self.obj_SSParams.str_Config_Batch_Settings_Path_And_File__Local)
            pass
        pass
    
        return bool_Success

    def func_Search_For_Config_Path_And_File(self, str_Search_Path, str_File_Search_Pattern):
        
        bool_Success = False
        
        with FileHandler() as obj_FileOp:
            bool_Success = obj_FileOp.method_Path_Exists(str_Search_Path)
            if bool_Success:
                bool_Success = False
                bool_Files_Found, list_Files_Found = obj_FileOp.func_Locate_Files(str_Search_Path, str_File_Search_Pattern, bool_Print_Search_Result = False, bool_Search_Sub_Folders = False)
                if bool_Files_Found:
                    if len(list_Files_Found) == 1:
                        str_Config_File_Path_And_Name__Local = list_Files_Found[0]
                        bool_Success = True
                    else:
                        with SSErrorOperation([]) as obj_SSErrorOp:
                            str_Message_Text = 'Only one file can be processed. More than one file found: \n' + '\n'.join(list_Files_Found)
                            int_Stack_Trace_Level = 2
                            obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))  
                        pass
                    pass
                else:
                    with SSErrorOperation([]) as obj_SSErrorOp:
                        str_Message_Text = 'Files of this search pattern: ' + str_File_Search_Pattern + ' ; Could not be found on search path: ' + str_Search_Path
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
        
        return bool_Success, str_Config_File_Path_And_Name__Local
        
    def func_Read_Config_File__Batch_Scenario(self, str_Config_Path_And_File):    
    
        bool_Success = False
        obj_Config = None
        
        with SSConfigOperation(self.obj_SSParams) as obj_ConfigOp:
            obj_Config = obj_ConfigOp.func_Verify_And_Read_Config_File__BATCH_SCENARIO(str_Config_Path_And_File)
            self.obj_SSParams.obj_Config_Batch_Scenario = obj_Config
            if obj_Config.config_parser_Config != None:
                bool_Success = True
            pass
        pass
    
        return bool_Success
    
    def func_Read_Config_File__Batch_Settings(self, str_Config_Path_And_File):    
    
        bool_Success = False
        obj_Config = None
        
        with SSConfigOperation(self.obj_SSParams) as obj_ConfigOp:
            obj_Config = obj_ConfigOp.func_Verify_And_Read_Config_File__BATCH_SETTINGS(str_Config_Path_And_File)
            self.obj_SSParams.obj_Config_Batch_Settings = obj_Config
            if obj_Config.config_parser_Config != None:
                bool_Success = True
            pass
        pass
            
        return bool_Success
    
    def func_Read_Config_File__Sampling_Strategy(self, str_Config_Path_And_File):    
    
        bool_Success = False
        obj_Config = None
        
        with SSConfigOperation(self.obj_SSParams) as obj_ConfigOp:
            obj_Config = obj_ConfigOp.func_Verify_And_Read_Config_File__SAMPLING_STRATEGY(str_Config_Path_And_File)
            self.obj_SSParams.obj_Config_Sampling_Strategy = obj_Config
            if obj_Config.config_parser_Config != None:
                bool_Success = True
            pass
        pass
        
        return bool_Success

        
    def method_Locate_Batch_Scenario_Run_Folder_RETIRE(self):
    
        if globalsSS.Run_Processing_Step.static_int_Run_Processing_Step__SAMP_STRAT in self.obj_SSParams.list_int_App_Arg_Run_Processing_Steps:
            ''' Locate the Batch Scenario run -  It should be the only SS_*_Run FOLDER in the command lined\ entered base path '''
            
            str_Search_Path = self.obj_SSParams.str_App_Arg_Output_Base_Path
            with FileHandler() as obj_FileOp:
                bool_Success = obj_FileOp.method_Path_Exists(str_Search_Path)
                if bool_Success:
                    bool_Success = False
                    str_Folder_Search_Pattern = app_details.str_Project__Prefix + '_*_Run_*'
                    bool_Folders_Found, list_Folders_Found = obj_FileOp.func_Locate_Folders(str_Search_Path, str_Folder_Search_Pattern, bool_Print_Search_Result = False, bool_Search_Sub_Folders = False)
                    if bool_Folders_Found:
                        if len(list_Folders_Found) == 1:
                            self.obj_SSParams.str_Batch_Scenario_Run_Folder = list_Folders_Found[0]
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
                    
        pass
    
        return True
    
    def method_Create_Config_Files(self):
    
        '''
        -------------------
        Test INI files
        -------------------
        '''
        bool_Test_INI_Files = True
        if bool_Test_INI_Files:
            bool_Create_INI = True
            
            self.obj_SSParams.str_PROJECTS_Config_File_Path_And_Name = self.obj_SSParams.str_Application_Projects_Path + '\\' + 'Projects' + '.ini'
            self.obj_SSParams.str_PROJECT_Config_File_Path = self.obj_SSParams.str_Application_Projects_Path
            self.obj_SSParams.str_PROJECT_Config_File_Path_And_Name = self.obj_SSParams.str_Application_Projects_Path + '\\' + 'Project_' + self.obj_SSParams.str_INI_UID_DateTime_Stamp + '.ini'
            self.obj_SSParams.str_SCENARIOS_Config_File_Path_And_Name = self.obj_SSParams.str_Application_Scenario_Config_Files_Path + '\\' + 'Scenarios' + '.ini'
            self.obj_SSParams.str_BATCH_SETTINGS_Config_File_Path_And_Name = self.obj_SSParams.str_Application_Specifc_Scenario_Config_Files_Path + '\\' + 'Batch_Settings_' + self.obj_SSParams.str_INI_UID_DateTime_Stamp + '.ini'
            self.obj_SSParams.str_BATCH_SCENARIO_Config_File_Path_And_Name = self.obj_SSParams.str_Application_Specifc_Scenario_Config_Files_Path + '\\' + 'Batch_Scenario_' + self.obj_SSParams.str_INI_UID_DateTime_Stamp + '.ini'
            self.obj_SSParams.str_SAMPLING_STRATEGY_Config_File_Path_And_Name = self.obj_SSParams.str_Application_Specifc_Scenario_Config_Files_Path + '\\' + 'Sampling_Strategy_' + self.obj_SSParams.str_INI_UID_DateTime_Stamp + '.ini'
            
            bool_Create_INI_With_Defaults = False
            if bool_Create_INI and bool_Create_INI_With_Defaults and not self.obj_SSParams.bool_App_Started_From_Command_Line:
                with SSConfigOperation(self.obj_SSParams) as obj_Config:
                    list_Path_And_ALL_Files = []
                    #obj_Config.func_Create_Config_File_PROJECTS(self.obj_SSParams.str_PROJECTS_Config_File_Path_And_Name)
                    #obj_Config.func_Create_Config_File_PROJECT(self.obj_SSParams.str_PROJECT_Config_File_Path_And_Name)
                    obj_Config.func_Create_Config_File_SCENARIOS(self.obj_SSParams.str_SCENARIOS_Config_File_Path_And_Name, list_Path_And_ALL_Files)
                    #obj_Config.func_Create_Config_File_BATCH_SETTINGS(self.obj_SSParams.str_BATCH_SETTINGS_Config_File_Path_And_Name)
                    #obj_Config.func_Create_Config_File_BATCH_SCENARIO(self.obj_SSParams.str_BATCH_SCENARIO_Config_File_Path_And_Name)
                    #obj_Config.func_Create_Config_File_SAMPLING_STRATEGY(self.obj_SSParams.str_SAMPLING_STRATEGY_Config_File_Path_And_Name)
                pass
            pass
        
            bool_Create_INI_From_Existing_Batch_Scenarios = True
            if bool_Create_INI_From_Existing_Batch_Scenarios:
                bool_Create_PROJECTS_INI_From_Existing_Batch_Scenarios = True
                if bool_Create_PROJECTS_INI_From_Existing_Batch_Scenarios:
                    list_Search_Paths = []
                    str_Input_FileName = '*' + 'Batch_Scenario_' + '*.ini'
                    str_File_Search_Pattern = str_Input_FileName
                    str_Search_Path = self.obj_SSParams.str_Application_Projects_Path
                    list_Search_Paths.append(str_Search_Path)
                    list_Project_Files_Path_And_ALL_Files = self.method_Search_For_Files(str_File_Search_Pattern, list_Search_Paths)    
                    with SSConfigOperation(self.obj_SSParams) as obj_Config:
                        obj_Config.func_Create_Config_File_PROJECTS(self.obj_SSParams.str_PROJECTS_Config_File_Path_And_Name, list_Path_And_ALL_Files)
                    pass        
                pass    
                bool_Create_PROJECT_INI_From_Existing_Batch_Scenarios = True
                if bool_Create_PROJECT_INI_From_Existing_Batch_Scenarios:
                    list_Search_Paths = []
                    str_Input_FileName = '*' + 'Batch_Scenario_' + '*.ini'
                    str_File_Search_Pattern = str_Input_FileName
                    str_Search_Path = self.obj_SSParams.str_Application_Projects_Path
                    list_Search_Paths.append(str_Search_Path)
                    list_Path_And_ALL_Files = self.method_Search_For_Files(str_File_Search_Pattern, list_Search_Paths)    
                    with SSConfigOperation(self.obj_SSParams) as obj_Config:
                        obj_Config.func_Create_Config_File_PROJECT(self.obj_SSParams.str_PROJECT_Config_File_Path, list_Path_And_ALL_Files)
                    pass        
                pass
#                     bool_Create_SCENARIOS_INI_From_Existing_Batch_Scenarios = True
#                     if bool_Create_SCENARIOS_INI_From_Existing_Batch_Scenarios:
#                         for str_Project_Path_And_file in list_Project_Files_Path_And_ALL_Files:
#                             list_Search_Paths = []
#                             str_Input_FileName = '*' + 'Batch_Scenario_' + '*.ini'
#                             str_File_Search_Pattern = str_Input_FileName
#                             str_Search_Path = self.obj_SSParams.str_Application_Projects_Path
#                             list_Search_Paths.append(str_Search_Path)
#                             list_Path_And_ALL_Files = self.method_Search_For_Files(str_File_Search_Pattern, list_Search_Paths)    
#                             with SSConfigOperation(self.obj_SSParams) as obj_Config:
#                                 obj_Config.func_Create_Config_File_SCENARIOS(self.obj_SSParams.str_SCENARIOS_Config_File_Path_And_Name, list_Path_And_ALL_Files)
#                             pass        
#                     pass
            pass
            
            bool_Read_INI = False
            if bool_Read_INI:
                with SSConfigOperation(self.obj_SSParams) as obj_Config:
                    if self.obj_SSParams.bool_App_Started_From_Command_Line:
                        #str_Config_File_Path_And_Name = self.obj_SSParams.str_Current_Run_Base_Path
                        
                        list_Search_Paths = []
                        str_Input_FileName = '*' + 'Project' + '*.ini'
                        str_File_Search_Pattern = str_Input_FileName
                        str_Search_Path = self.obj_SSParams.str_Current_Run_Base_Path
                        list_Search_Paths.append(str_Search_Path)
                        
                        ''' Get ALL the files to plot from list of search paths '''
                        list_Path_And_ALL_Files = []
                        with FileHandler() as obj_FileHandler:
                            bool_Files_Located = False
                            for str_Search_Path in list_Search_Paths:
                        
                                bool_Files_Located, list_Path_And_Files = obj_FileHandler.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
                                list_Path_And_ALL_Files.extend(list_Path_And_Files)
                            pass
                        pass
                    
                        if bool_Files_Located:
                            if len(list_Path_And_Files) == 1: 
                                str_Config_File_Path_And_Name = list_Path_And_ALL_Files[0]                  
                                config_parser_Config = obj_Config.func_Read_Config_File_PROJECT(str_Config_File_Path_And_Name)
                            pass
                        pass
                    else:
                        str_Config_File_Path_And_Name = self.obj_SSParams.str_Current_Run_Base_Path + '\\' + 'Project_' + self.obj_SSParams.str_INI_UID_DateTime_Stamp + '.ini'
                        obj_Config.func_Read_Config_File_PROJECT(str_Config_File_Path_And_Name)
                    pass
                pass
            pass
            ''' Make SS fail '''
            return True        
        pass

        return True
            
    def method_Search_For_Files(self, str_File_Search_Pattern, list_Search_Paths):
        
        list_Path_And_ALL_Files = []
        bool_Files_Located = False
        
        if len(list_Search_Paths) > 0:
            ''' Get ALL the files to plot from list of search paths '''
            
            with FileHandler() as obj_FileHandler:
                for str_Search_Path in list_Search_Paths:
            
                    bool_Files_Located, list_Path_And_Files = obj_FileHandler.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
                    list_Path_And_ALL_Files.extend(list_Path_And_Files)
                pass
            pass
        pass
    
        return list_Path_And_ALL_Files
    
    def __exit__(self, type, value, traceback): 

        return None

    '''            
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS FINALIZATION
    '''