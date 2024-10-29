'''
Created on 29 Jan 2015

@author: dblowe
'''
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS
#
#------------------< Import python modules
# DEBUG Imports
from logging import getLogger as logging__getLogger
from handler_Debug import Timer2
from handler_Debug import Debug_Location as dcb_Debug_Location
#
import sys
#
from os import path as os__path
from os import getcwd as os__getcwd
#
import traceback
#
#------------------< Import DCB_General modules
from globals_DCB_General import globalsDCBGen
from FileHandler import FileHandler
from handler_Logging import Logging
#------------------< Import SharkSim modules
#from SSReplicateHandler import SSReplicateHandler
#from SSReplicateHandler import SSReplicateOperation
#from SSParameterHandler import SSParameterHandler
#from SSOutputHandler import SSOutputHandler
from globals_SharkSim import globalsSS
#from SSConfigHandler import SSConfigOperation
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
gstringModuleName='SSErrorHandler.py'
gstringClassName='SSErrorOperation'

  
class SSErrorOperation(object):

    def __enter__(self):
    
        return self
    
    def __init__(self, list_Params):

        ''' Get all the loggers required for monitoring this object '''
        self.func_Initialise_Monitor_Loggers()

        return None      

    def func_Initialise_Monitor_Loggers(self):
        
        ''' 
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get all the loggers required for monitoring this object
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        ''' Get Run Display Logger '''
        self.obj_Log_Run_Display = logging__getLogger(globalsSS.Logger_Run_Display.static_Logger_Name__Run_Display)
                   
        ''' Get Default Logger '''
        self.obj_Log_Default_Display = logging__getLogger(globalsSS.Logger_Default_Display.static_Logger_Name__Default_Display)

        ''' Get Debug Logger '''
        self.obj_Log_Debug_Display = logging__getLogger(globalsSS.Logger_Debug_Display.static_Logger_Name__Debug_Display)

        ''' Get Debug Timer '''
        self.obj_Log_Debug_Timing = None
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            self.obj_Log_Debug_Timing = logging__getLogger(globalsSS.Logger_Debug_Timing.static_Logger_Name__Debug_Timing)
        pass

        return True

    def func_Main(self):
        
        return True

    def func_Run_Status__FAILED_CAUGHT(self, str_Run_Status_Base_Path, str_Run_Status_UID = '', str_Run_Status_Message = ''):
        
        bool_Success = False

        str_Run_Status_Path_And_File = ''
        if str_Run_Status_UID == '':
            str_Run_Status_UID = 'SS_Run'
        pass
        str_Run_Status_Path = os__path.join(str_Run_Status_Base_Path, globalsDCBGen.Run_Status.static_str_Run_Status__Path)
        str_Run_Status_Path_And_File = os__path.join(str_Run_Status_Path, str_Run_Status_UID +  '.' + globalsDCBGen.Run_Status.static_str_Run_Status__FAILED_CAUGHT)

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
                        obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text)  
                    pass              
                pass
            pass
        pass
        
        return bool_Success
    
    def func_Error_Handler__Caught_Exceptions(self, int_Stack_Trace_Level, str_Message_Text, tup_Args=(), bool_Log_Trace=True, int_Display_Trace_Levels=0):

        with dcb_Debug_Location() as obj_DebugLoc:
            str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True, int_Stack_Trace_Level_Override=int_Stack_Trace_Level)
        pass
        str_Message_Prefix = '!!UNEXP_ERR!!'
        str_Message = str_Message_Location + ' ; ' + str_Message_Prefix + ' ; ' + str_Message_Text
        sys.stdout.flush()
        
        if bool_Log_Trace:
            stack = traceback.extract_stack()
            stack_List = traceback.format_list(stack)
            if int_Display_Trace_Levels == 0:
                ''' Display all '''
                pass
            else:
                stack = stack[:int_Display_Trace_Levels]
            pass
            str_Stack = '\n'.join(traceback.format_list(stack))
            self.obj_Log_Default_Display.error(str_Message + '\n' + str_Stack)
        else:
            self.obj_Log_Default_Display.error(str_Message)
        pass

        str_Run_Status_Base_Path = os__getcwd()
        self.func_Run_Status__FAILED_CAUGHT(str_Run_Status_Base_Path, str_Run_Status_UID='', str_Run_Status_Message='')
 
        if tup_Args != ():
            if len(tup_Args) == 2:
                str_Run_Status_Base_Path, str_Run_Status_UID = tup_Args
            
                if str_Run_Status_Base_Path != '':
                    self.func_Run_Status__FAILED_CAUGHT(str_Run_Status_Base_Path, str_Run_Status_UID)
                pass
            pass
        pass
                
        ''' End the application as gracefully as possible'''
        raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__Caught_Error)
        #sys.exit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__Caught_Error)
        
        return True

    def func_Run_Status__FAILED_UNCAUGHT(self, str_Run_Status_Base_Path, str_Run_Status_UID = '', str_Run_Status_Message = ''):
        
        bool_Success = False

        str_Run_Status_Path_And_File = ''
        if str_Run_Status_UID == '':
            str_Run_Status_UID = 'SS_Run'
        pass
        str_Run_Status_Path = os__path.join(str_Run_Status_Base_Path, globalsDCBGen.Run_Status.static_str_Run_Status__Path)
        str_Run_Status_Path_And_File = os__path.join(str_Run_Status_Path, str_Run_Status_UID +  '.' + globalsDCBGen.Run_Status.static_str_Run_Status__FAILED_UNCAUGHT)

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
                        obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text)  
                    pass              
                pass
            pass
        pass
        
        return bool_Success
    
    def func_Error_Handler__UNCaught_Exceptions(self, exc_type, exc_value, exc_traceback):

        ''' Get the very last frame which contains the error '''
        traceback_Obj = exc_traceback
        while True:
            if traceback_Obj.tb_next == None:
                break
            else:
                traceback_Obj = traceback_Obj.tb_next
            pass
        pass

        ''' Get the error frame '''
        frame = traceback_Obj.tb_frame

        ''' Get the error info '''
        str_Origin_LineNo = str(frame.f_lineno)
        str_Origin_Func = str(frame.f_code.co_name)
        str_Origin_Class_PathAndFileName = str(frame.f_code.co_filename)
        str_Origin_Class_Path, str_Origin_Class_FileName = os__path.split(str_Origin_Class_PathAndFileName)
        str_Location = str_Origin_Class_FileName + '.' + str_Origin_Func + '; ' + 'line: ' + str_Origin_LineNo
        
        str_Exec_Type = str(exc_type)
        str_Exec_Value = str(exc_value)
        str_Message_Prefix = '!!UNHAN_ERR!!'
        str_Message_Text = 'Uncaught exception'
        str_Message__Log = str_Message_Prefix + ' ; ' + str_Message_Text
        sys.stdout.flush()
        ''' NOTE: cant use Log_Run_Disply here as the SSRunHandler deletes all its handlers when it exits '''
        self.obj_Log_Default_Display.error(str_Message__Log, exc_info=(exc_type, exc_value, exc_traceback))

        str_Path__Run_Status__FAILED_UNCAUGHT = os__getcwd()
        self.func_Run_Status__FAILED_UNCAUGHT(str_Path__Run_Status__FAILED_UNCAUGHT, str_Run_Status_UID='', str_Run_Status_Message='')
                    
        ''' End the application as gracefully as possible'''
        raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)
        #sys.exit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)
        
        return True

    
    def __exit__(self, type, value, traceback): 

        ''' Close loggers '''
        #self.obj_Log_BL.handlers = []
        
        return None

    '''            
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS FINALIZATION
    '''