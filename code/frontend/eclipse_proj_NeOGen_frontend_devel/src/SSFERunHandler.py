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
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS
#------------------< Import python modules
import logging
import sys
import traceback
#import ctypes
#from ctypes import *
from datetime import datetime
from logging import getLogger as logging__getLogger
from os import path as os__path
from os import extsep as os__extsep
from collections import OrderedDict
#------------------< Import DCB_General modules
# DEBUG Imports
from handler_Debug import Debug_Location as dcb_Debug_Location
from handler_Debug import Timer2
#
from FileHandler import FileHandler
from handler_Logging import Logging
from unicodedata import category as unicodedata__category
from PyQt4 import QtCore, QtGui, uic
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
#import simuPOP as simu_pop
#------------------< Import SharkSim modules
import globals_SharkSimFE
from globals_SharkSimFE import globalsSSFE
from SSFEParameterHandler import SSFEParameters
#from SSConfigHandler import SSConfigOperation
from SSFEGUIHandler import SSFEGUIOperation
from SSConfigHandler import SSConfigOperation
from object_SSConfigFiles import object_SSConfigFiles
from object_SSConfigSettings import object_SSConfigSettings
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
gstringModuleName='SSFERunHandler.py'
gstringClassName='SSFERunOperation'

class SSFERunOperation(object):

    def __enter__(self):
    
        return self
    
    def __init__(self, str_App_Run_Path_And_File, str_App_Arg_Working_Base_Path, bool_App_Arg_Debug_Logging, bool_App_Arg_Devel_Mode, str_App_Arg_Devel_Folder, bool_App_Arg_Devel_Uses_Sync_Folders):

        self.obj_Log_RD = None
        self.obj_Log_DD = None
        
        self.obj_Config_Settings = None
        
        self.str_App_Arg_Working_Base_Path = str_App_Arg_Working_Base_Path
        self.str_App_Run_Path_And_File = str_App_Run_Path_And_File
        self.str_App_Run_Path, self.str_App_Run_File = os__path.split(self.str_App_Run_Path_And_File)
        self.bool_App_Arg_Debug_Logging = bool_App_Arg_Debug_Logging
        self.bool_App_Arg_Devel_Mode = bool_App_Arg_Devel_Mode
        self.str_App_Arg_Devel_Folder = str_App_Arg_Devel_Folder
        self.bool_App_Arg_Devel_Uses_Sync_Folders = bool_App_Arg_Devel_Uses_Sync_Folders
                
        self.obj_SSFEParams = None
        
        return None

    def func_Initialize_Loggers(self):

        ''' Get Default Display Logger '''
        self.obj_Log_Default_Display = None
        if globalsSSFE.Logger_Default_Display.bool_Default_Display:
            obj_Logging = Logging()
            obj_Logging.strLogFile = self.obj_SSFEParams.strUniqueRunID + '__' + globalsSSFE.Logger_Default_Display.static_Logger_File_Name__Default_Display + globalsSSFE.Logger_Default_Display.static_Logger_File_Suffix__Default_Display
            obj_Logging.strLogPath = self.obj_SSFEParams.str_Current_App_Run_Log_Path
            obj_Logging.bool_LogToConsole = globalsSSFE.Logger_Default_Display.static_Logger_bool_LogToConsole
            obj_Logging.bool_LogToFile = globalsSSFE.Logger_Default_Display.static_Logger_bool_LogToFile
            obj_Logging.str_Logger_Name = globalsSSFE.Logger_Default_Display.static_Logger_Name__Default_Display 
            obj_Logging.str_Logger_Level = 'info'
            obj_Logging.func_Initialise_New_Logger()
            self.obj_Log_Default_Display = logging__getLogger(globalsSSFE.Logger_Default_Display.static_Logger_Name__Default_Display)
            self.obj_Log_Default_Display.info('Log initialised: ' + globalsSSFE.Logger_Default_Display.static_Logger_File_Name__Default_Display)
        pass

        ''' Get Debug Display Logger '''
        self.obj_Log_Debug_Display = None
        if globalsSSFE.Logger_Debug_Display.bool_Debug_Display and self.bool_App_Arg_Debug_Logging:
            obj_Logging = Logging()
            obj_Logging.strLogFile = self.obj_SSFEParams.strUniqueRunID + '__' + globalsSSFE.Logger_Debug_Display.static_Logger_File_Name__Debug_Display + globalsSSFE.Logger_Debug_Display.static_Logger_File_Suffix__Debug_Display
            obj_Logging.strLogPath = self.obj_SSFEParams.str_Current_App_Run_Log_Path
            obj_Logging.bool_LogToConsole = globalsSSFE.Logger_Debug_Display.static_Logger_bool_LogToConsole
            obj_Logging.bool_LogToFile = globalsSSFE.Logger_Debug_Display.static_Logger_bool_LogToFile
            obj_Logging.str_Logger_Name = globalsSSFE.Logger_Debug_Display.static_Logger_Name__Debug_Display 
            obj_Logging.str_Logger_Level = 'debug'
            obj_Logging.func_Initialise_New_Logger()
            self.obj_Log_Debug_Display = None
            self.obj_Log_Debug_Display = logging__getLogger(globalsSSFE.Logger_Debug_Display.static_Logger_Name__Debug_Display)
            self.obj_Log_Debug_Display.info('Log initialised: ' + globalsSSFE.Logger_Debug_Display.static_Logger_File_Name__Debug_Display)   

        pass

        return True
      
    def func_Run_Initiation(self):    

        obj_SSFEParams = self.func_Parameter_Initializaton()
        self.func_Run_Processing(obj_SSFEParams)
                  
        return True
    
    def func_Parameter_Initializaton(self):
        
        '''
        Create an SSParameter object - All the run/batch/replicate parameters are contained within the parameters object
        '''
        objSSOperation = None
        obj_SSFEParams = None

        with SSFEParameters() as obj_SSFEParams:
            '''
            Initialise Global Variable General Message DateTime
            '''
            globals_SharkSimFE.global_dateTimeLastGeneralMessage = datetime.now()
            
            obj_SSFEParams.dateSimRunStartTime = datetime.now()
            
        pass
    
        return obj_SSFEParams
            
    def func_Run_Processing(self, obj_SSFEParams):    
        
        self.obj_SSFEParams = obj_SSFEParams   
             
        '''
        -------------------------------------------
        Setup simulation run-wide parameters
        -------------------------------------------
        '''
        self.obj_SSFEParams.str_App_Run_Path = self.str_App_Run_Path
        self.obj_SSFEParams.str_App_Run_File = self.str_App_Run_File
        self.obj_SSFEParams.str_Application_Settings_Path_And_File = self.str_App_Run_Path_And_File
        self.obj_SSFEParams.str_App_Arg_Working_Base_Path = self.str_App_Arg_Working_Base_Path
        self.obj_SSFEParams.bool_App_Arg_Debug_Logging = self.bool_App_Arg_Debug_Logging
        self.obj_SSFEParams.bool_App_Arg_Devel_Mode = self.bool_App_Arg_Devel_Mode
        self.obj_SSFEParams.str_App_Arg_Devel_Folder = self.str_App_Arg_Devel_Folder
        self.obj_SSFEParams.bool_App_Arg_Devel_Uses_Sync_Folders = self.bool_App_Arg_Devel_Uses_Sync_Folders
        
        self.obj_SSFEParams.func_Run_Pre_Processing__Application_Specs()
        self.obj_SSFEParams.func_Run_Pre_Processing__Environment_Specs()
        
        '''
        -------------------------------------------
        Get SIM loggers
        -------------------------------------------
        '''
        self.func_Initialize_Loggers()
        
        '''
        -------------------------------------------
        Construct the settings file name to send to the main form
        -------------------------------------------
        ''' 
        #2017-05-11 - Settings.ini  path and file now passed in as argument 
#         str_Path = self.str_App_Run_Path
#         str_Base_Filename = globalsSSFE.App_File.static_str__App_File_Prefix__Settings #'Settings'
#         str_Extension = globalsSSFE.App_File.static_str__App_File_Extension__Config_File #'ini'
#         self.obj_SSFEParams.str_Application_Settings_Path_And_File = os__path.join(str_Path, ''.join([str_Base_Filename, os__extsep, str_Extension]))
        
        
        '''
        -------------------------------------------
        Start Run Processing - Load GUI
        -------------------------------------------
        '''
        with SSFEGUIOperation(self.obj_SSFEParams) as obj_GUI:
            obj_GUI.func_Main()
        pass
    
        '''
        -------------------------------------------
        Close loggers
        -------------------------------------------
        '''
        if self.obj_Log_Default_Display is not None:
            self.obj_Log_Default_Display.handlers = []
        pass      
        if self.obj_Log_Debug_Display is not None:
            self.obj_Log_Debug_Display.handlers = []
        pass                      
        return True

    def func_Run_Start(self):    

        '''
        Set simulation wide simupop parms
        '''
        #simu_pop.setOptions(numThreads=8, name='mt19937_1999', seed=0)
              
        self.func_Run_Initiation()
        
        return True

      
    def __exit__(self, type, value, traceback): 

#         ''' Close loggers '''
#         if self.obj_Log_RD != None:
#             self.obj_Log_RD.handlers = []
#         pass
#         if self.obj_Log_Debug_Display is not None:
#             self.obj_Log_Debug_Display.handlers = []
#         pass        
        
        return None
        
    '''            
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS FINALIZATION
    '''
