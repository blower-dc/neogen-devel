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
from handler_Debug import Debug_Location
#
from collections import OrderedDict
from ConfigParser import ConfigParser
import re
#------------------< Import DCB_General modules
from FileHandler import FileHandler
from handler_Logging import Logging
from ConfigHandler import ConfigOperation
#------------------< Import SharkSim modules
from SSParameterHandler import SSParameterHandler
from globals_SharkSim import globalsSS

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
class object_SSConfigSpecies(object):

    '''
    --------------------------------------------------------------------------------------------------------
    # <<<<<<<<<<<<<<<<<< CLASS INIT
    --------------------------------------------------------------------------------------------------------
    '''   

    __slots__ = (
                #PROPERTIES
#                 'Project_Name'
#                 ,'Project_Name'
#                 ,'Scenarios_File'
#                 ,'Section_To_Read'
#                 ,'Option_To_Read'
#                 ,'Option_Type_To_Read'
                'obj_SSParams'                
                #VARIABLES
                #,'str_Project_Name'
                #,'str_Scenarios_File'
                ,'str_Section_To_Read'
                ,'str_Option_To_Read'
                ,'int_Option_Type_To_Read'
                ,'value_Read'
                #                
                ,'obj_SSParams'
                ,'str_Current_Col_Index'
                ,'obj_Log_Run_Display'
                ,'obj_Log_Default_Display'
                ,'obj_Log_Default'
                ,'obj_Log_Debug_Display'
                ,'obj_Log_Debug_Timing'               
                ,'obj_Config'               
                
                #CONSTANTS
                ,'static_str_Option_Key__Project_Name'
                ,'static_str_Option_Key__Scenarios_File'
                )

    static_str_Section__INI_File = 'INI_File'
    static_str_Option__INI_Filename = 'INI_Filename'
    static_str_Value__INI_Filename = 'SPECIES'
    static_str_Option__INI_Creation_Run_ID = 'INI_Creation_Run_ID'
                    
    static_str_Section__Species_Details = 'Species_Details'
    static_str_Option__Species_Code_Long = 'Species_Code_Long'
    static_str_Option__Species_Code_Short = 'Species_Code_Short'
    static_str_Option__Species_Name = 'Species_Name'

    def __enter__(self):
        
        return self 
         
    def __init__(self, objSSParametersLocal):
        '''
        Constructor
        '''
 
        self.obj_SSParams = objSSParametersLocal
        
        self.str_Current_Col_Index = str(
                                     '0' +
                                     globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                     '0' +
                                     globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                     '0' +
                                     globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                     '0')
                
        ''' Get all the loggers required for monitoring this object '''
        self.func_Initialise_Monitor_Loggers()


#         #Initialize  PROPERTIES
#         self.Project_Name = ''
#         self.Scenarios_File = ''
#         self.Section_To_Read = ''
#         self.Option_To_Read = ''
#         self.Option_Type_To_Read = 0     
        
        #Initialize VARIALBLES
        #self.str_Project_Name = ''
        #self.str_Scenarios_File = ''
        self.str_Section_To_Read = ''
        self.str_Option_To_Read = ''
        self.int_Option_Type_To_Read = 0      
        self.value_Read = None     
        
        return None         

    def func_Initialise(self):
         
#         #PROPERTIES -> VARIABLES
#         self.str_Project_Name = self.Project_Name
#         self.str_Scenarios_File = self.Scenarios_File
#         self.str_Section_To_Read = self.Section_To_Read
#         self.str_Option_To_Read = self.Option_To_Read
#         self.int_Option_Type_To_Read = self.Option_Type_To_Read  
        
        
        self.obj_Config = ConfigOperation(globalsSS)
        self.obj_Config.obj_Log_Run_Display = self.obj_Log_Run_Display
        self.obj_Config.obj_Log_Default_Display = self.obj_Log_Default_Display
        self.obj_Config.obj_Log_Debug_Display = self.obj_Log_Debug_Display
        self.obj_Config.obj_Log_Debug_Timing = self.obj_Log_Debug_Timing           
    
        return True

    def func_Initialise_Config_File(self, str_Config_File_Path_And_Name):
        
        bool_Success = False
        file_Handle = None
        config_parser_Config = None
        bool_Option_Exists = False

        file_Handle = self.obj_Config.func_Open_Config_File(str_Config_File_Path_And_Name)       
             
        if file_Handle != None:
            config_parser_Config = self.obj_Config.func_Create_Config_File_Parser()

            list_Filenames__Config = [str_Config_File_Path_And_Name]
            
            config_parser_Config = self.obj_Config.func_Read_Config_File(config_parser_Config, list_Filenames__Config)
        
            str_Section = self.static_str_Section__INI_File
            key_Option = self.static_str_Option__INI_Creation_Run_ID
            value_Option = self.obj_SSParams.strUniqueRunID
            ''' FIRST Check if OPTION exists - If so the file is already initialised '''
            bool_Option_Exists = self.obj_Config.func_Check_If_Config_File_OPTION_Exists(config_parser_Config, str_Section, key_Option)
            '''SECOND - If it this option does not exist - initialise the file'''
            if not bool_Option_Exists:
                
                ''' Define Sections/Options/Values dict '''
                dict_Section_Key_Option_Value_Tuple = OrderedDict()
                
                value_Option = self.obj_SSParams.strUniqueRunID
                dict_Section_Key_Option_Value_Tuple[self.static_str_Section__INI_File] = [(self.static_str_Option__INI_Creation_Run_ID, self.obj_SSParams.strUniqueRunID)
                                                                                          ,(self.static_str_Option__INI_Filename, self.static_str_Value__INI_Filename)]
                ''' Set the values from the dict '''
                config_parser_Config = self.obj_Config.func_Set_Values_in_Config_File_From_Dict(config_parser_Config, dict_Section_Key_Option_Value_Tuple)
                                               
                bool_Success = self.obj_Config.func_Write_Config_File(config_parser_Config, str_Config_File_Path_And_Name)
            else:
                bool_Success = True
            pass
        else:
            with Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Message = str_Message_Location + ' >> UNEXPECTED ERROR - Config file could not be opened/created & initial values written: ' + str(str_Config_File_Path_And_Name)
            self.obj_Log_Default_Display.error(str_Message)
            raise ValueError(str_Message)
        pass
        pass              
    
        return config_parser_Config
        
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
        ''' NOTE: Name is obj_Log_Default '''
        self.obj_Log_Default = self.obj_Log_Default_Display

        ''' Get Debug Logger '''
        ''' NOTE: Name is obj_Log_Debug_Display '''
        self.obj_Log_Debug_Display = logging__getLogger(globalsSS.Logger_Debug_Display.static_Logger_Name__Debug_Display)

        ''' Get Debug Timer '''
        self.obj_Log_Debug_Timing = None
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            self.obj_Log_Debug_Timing = logging__getLogger(globalsSS.Logger_Debug_Timing.static_Logger_Name__Debug_Timing)
        pass

#         ''' Get Debug AgeNe Logger '''
#         self.obj_Log_Debug_AgeNe = None
#         if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
#             self.obj_Log_Debug_AgeNe = logging__getLogger(globalsSS.Logger_Debug_AgeNe.static_Logger_Name__Debug_AgeNe)
#         pass



        
        return True

    
    '''
    --------------------------------------------------------------------------------------------------------
    # Main Processing
    --------------------------------------------------------------------------------------------------------
    '''
       
    def func_Main(self):

        
        return True
    
    '''
    --------------------------------------------------------------------------------------------------------
    # Sub-Main Processing
    --------------------------------------------------------------------------------------------------------
    '''

    def func_Create_Config_File(self, str_Config_File_Path_And_Name, dict_Section_Key_Option_Value_Tuple):
        
        bool_Success = False
        
        config_parser_Config = self.func_Initialise_Config_File(str_Config_File_Path_And_Name)
        
        list_Filenames__Config = [str_Config_File_Path_And_Name]
        config_parser_Config = self.obj_Config.func_Read_Config_File(config_parser_Config, list_Filenames__Config)

        ''' Set values from dict '''
        config_parser_Config = self.obj_Config.func_Set_Values_in_Config_File_From_Dict(config_parser_Config, dict_Section_Key_Option_Value_Tuple)
    
        bool_Success = self.obj_Config.func_Write_Config_File(config_parser_Config, str_Config_File_Path_And_Name)
        
        return bool_Success
    
    def func_Read_Config_File(self, str_Config_File_Path_And_Name):

        config_parser_Config = self.obj_Config.func_Create_Config_File_Parser()

        list_Filenames__Config = [str_Config_File_Path_And_Name]
        config_parser_Config = self.obj_Config.func_Read_Config_File(config_parser_Config, list_Filenames__Config)

        str_Section = self.str_Section_To_Read
        str_Option = self.str_Option_To_Read
        int_Value_Type = self.int_Option_Type_To_Read 
        #value_Project_Name = obj_Config.func_Get_Config_File_OPTION_Specifying_Option_Type(config_parser_Config, str_Section, str_Option, int_Value_Type)
        self.value_Read = self.obj_Config.func_Get_Config_File_OPTION_Specifying_Option_Type(config_parser_Config, str_Section, str_Option, int_Value_Type)
        
        return self.value_Read
    
    '''
    --------------------------------------------------------------------------------------------------------
    # Utility Processing
    --------------------------------------------------------------------------------------------------------
    '''

    def func_Get_Log_Current_Column_Index(self, bool_Reset, intLevel, bool_Add_Suffix = False, str_Suffix = ''):
        
        if bool_Reset:
            self.str_Current_Col_Index = str(
                                             str(intLevel) +
                                             globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                             '0' +
                                             globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                             '0' +
                                             globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                             '0')
        else:
            list_Delimiters = [str_Suffix, globalsSS.StringDelimiters.static_stringDelimiter_DOT]
            L, h, i, j, _ = re.split('|'.join(re.escape(x) for x in list_Delimiters), self.str_Current_Col_Index)            
            #L, h, i, j = self.str_Current_Col_Index.split(globalsSS.StringDelimiters.static_stringDelimiter_DOT)
            
            h = int(h)
            i = int(i)
            j = int(j)
            
            j += 1
            
            '''Get column numbering'''
            if j == 10:
                j = 0
                i += 1
                if i == 10:
                    i = 0
                    h += 1
                    if h == 10:
                        self.obj_Internal_Logger.warn('Column index number has exceeded its max number 9.9.9. Dataframes will not be in the correct column order')
                pass
            pass
            
            self.str_Current_Col_Index = str(
                                str(intLevel) +
                                globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                str(h) +
                                globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                str(i) +
                                globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                str(j))
            
        pass

        if bool_Add_Suffix:
            self.str_Current_Col_Index = self.str_Current_Col_Index + str(str_Suffix)
        pass
    
        return self.str_Current_Col_Index


    '''
    --------------------------------------------------------------------------------------------------------
    # <<<<<<<<<<<<<<<<<< CLASS FINALIZATION
    --------------------------------------------------------------------------------------------------------
    '''       
    def __exit__(self, type, value, traceback):
         
        pass
    
    
    
    
    