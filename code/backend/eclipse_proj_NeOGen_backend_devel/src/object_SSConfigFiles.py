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
from unicodedata import category as unicodedata__category
#from ConfigParser import ConfigParser
import re

#------------------< Import DCB_General modules
#from FileHandler import FileHandler
#from handler_Logging import Logging
from ConfigHandler import ConfigOperation
#------------------< Import SharkSim modules
#from SSParameterHandler import SSParameterHandler
from globals_SharkSim import globalsSS
from SSErrorHandler import SSErrorOperation
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
class object_SSConfigFiles(object):

    '''
    --------------------------------------------------------------------------------------------------------
    # <<<<<<<<<<<<<<<<<< CLASS INIT
    --------------------------------------------------------------------------------------------------------
    '''   

    __slots__ = (
                #PROPERTIES
                'strUniqueRunID'                
                ,'str_INI_UID_DateTime_Stamp'                
                #VARIABLES
                ,'config_parser_Config'
                ,'obj_Config'               
                )

    static_str_Section__INI_File = 'INI_File'
    static_str_Option__INI_Filename = 'INI_Filename'
    static_str_Value__INI_Filename = 'BATCH_SCENARIO'
    static_str_Option__INI_Creation_Run_ID = 'INI_Creation_Run_ID'
    static_str_Option__INI_UID = 'INI_UID'
                    
    def __enter__(self):
        
        return self 
         
    def __init__(self):
        '''
        Constructor
        '''
        
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
        
        #Initialize VARIALBLES
        self.strUniqueRunID = ''
        self.str_INI_UID_DateTime_Stamp = ''
        self.config_parser_Config = None
        
        return None         

    def func_Initialise(self):
         
#         #PROPERTIES -> VARIABLES
#         self.strUniqueRunID = self.Project_Name
#         self.str_INI_UID_DateTime_Stamp = self.Scenarios_File
#         self.str_Section_To_Read = self.Section_To_Read
#         self.str_Option_To_Read = self.Option_To_Read
#         self.int_Option_Type_To_Read = self.Option_Type_To_Read  
        
        
        self.obj_Config = ConfigOperation(globalsSS)
#         self.obj_Config.obj_Log_Run_Display = self.obj_Log_Run_Display
#         self.obj_Config.obj_Log_Default_Display = self.obj_Log_Default_Display
#         self.obj_Config.obj_Log_Debug_Display = self.obj_Log_Debug_Display
#         self.obj_Config.obj_Log_Debug_Timing = self.obj_Log_Debug_Timing           
    
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
            
            config_parser_Config = self.obj_Config.func_Read_Config_File_From_Config_Parser(config_parser_Config, list_Filenames__Config)
        
            str_Section = self.static_str_Section__INI_File
            key_Option = self.static_str_Option__INI_Creation_Run_ID
            ''' FIRST Check if OPTION exists - If so the file is already initialised '''
            bool_Option_Exists = self.obj_Config.func_Check_If_Config_File_OPTION_Exists(config_parser_Config, str_Section, key_Option)
            '''SECOND - If it this option does not exist - initialise the file'''
            if not bool_Option_Exists:
                
                ''' Define Sections/Options/Values dict '''
                dict_Section_Key_Option_Value_Tuple = OrderedDict()
                
                dict_Section_Key_Option_Value_Tuple[self.static_str_Section__INI_File] = [(self.static_str_Option__INI_Creation_Run_ID, self.strUniqueRunID)
                                                                                          ,(self.static_str_Option__INI_Filename, self.static_str_Value__INI_Filename)
                                                                                          ,(self.static_str_Option__INI_UID, self.str_INI_UID_DateTime_Stamp)
                                                                                          ]
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
            bool_Success = False
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
        config_parser_Config = self.obj_Config.func_Read_Config_File_From_Config_Parser(config_parser_Config, list_Filenames__Config)

        ''' Set values from dict '''
        config_parser_Config = self.obj_Config.func_Set_Values_in_Config_File_From_Dict(config_parser_Config, dict_Section_Key_Option_Value_Tuple)
    
        bool_Success = self.obj_Config.func_Write_Config_File(config_parser_Config, str_Config_File_Path_And_Name)
        
        return bool_Success
    
    def func_Read_Config_File(self, str_Config_File_Path_And_Name):

        config_parser_Config = self.obj_Config.func_Create_Config_File_Parser()

        list_Filenames__Config = [str_Config_File_Path_And_Name]
        self.config_parser_Config = self.obj_Config.func_Read_Config_File_From_Config_Parser(config_parser_Config, list_Filenames__Config)

        return self.config_parser_Config

        
    def func_Set_Values_in_Config_File_From_Dict(self, config_parser_Config, dict_Section_Key_Option_Value_Tuple):

        self.config_parser_Config = self.obj_Config.func_Set_Values_in_Config_File_From_Dict(config_parser_Config, dict_Section_Key_Option_Value_Tuple)

        return self.config_parser_Config

    def func_Set_Values_in_Config_File_Section(self, config_parser_Config, str_Section, str_Option, value_Option):

        self.config_parser_Config = self.obj_Config.func_Set_Values_in_Config_File_Section(config_parser_Config, str_Section, str_Option, value_Option)

        return self.config_parser_Config

    def func_Remove_OPTIONS_in_Config_File_From_Dict(self, config_parser_Config, dict_Section_Key_Option_Value):

        bool_Success = False
        
        bool_Success, self.config_parser_Config = self.obj_Config.func_Remove_OPTIONS_in_Config_File_From_Dict(config_parser_Config, dict_Section_Key_Option_Value)

        return bool_Success, self.config_parser_Config

    def func_Remove_SECTION_From_Config_File_Section(self, config_parser_Config, str_Section):

        bool_Success = False
        
        bool_Success, self.config_parser_Config = self.obj_Config.func_Remove_SECTION_From_Config_File_Section(config_parser_Config, str_Section)

        return bool_Success, self.config_parser_Config

    def func_Remove_OPTION_From_Config_File_Section(self, config_parser_Config, str_Section, str_Option):

        bool_Success = False
        
        bool_Success, self.config_parser_Config = self.obj_Config.func_Remove_OPTION_From_Config_File_Section(config_parser_Config, str_Section, str_Option)

        return bool_Success, self.config_parser_Config

    def func_Write_Config_File(self, config_parser_Config, str_Config_File_Path_And_Name):

        
        bool_Success = self.obj_Config.func_Write_Config_File(config_parser_Config, str_Config_File_Path_And_Name)
        
        return bool_Success
    
    def func_Read_Config_File_OPTION_RETIRE(self, str_Section, str_Option, int_Value_Type, config_parser_Config=None):

        bool_Success = False
        
        if config_parser_Config == None:
            if self.config_parser_Config != None:
                config_parser_Config = self.config_parser_Config
                bool_Success = True
            else:
                bool_Success = False
            pass
        pass
        
        value_Read = None
        if bool_Success:
            value_Read = self.obj_Config.func_Get_Config_File_OPTION_Specifying_Option_Type(config_parser_Config, str_Section, str_Option, int_Value_Type)
        pass
    
        return value_Read
    
    def func_Read_OPTION(self, bool_OPTION_is_expected, bool_OPTION_is_List, obj_Config, str_Section, str_Option, value_Type):
        ''' Check if OPTION exists in config file '''
        value_Option = None
        bool_Option_Exists = False
        ''' Remove any whitespaces, CRLF, TAB etc '''
        if isinstance(str_Section, str):
            str_Section = str_Section.join(str_Section.split())
        pass
        if isinstance(str_Section, str):
            str_Option = str_Option.join(str_Option.split())
        pass        
        bool_Option_Exists = self.func_Check_If_Config_File_OPTION_Exists(obj_Config.config_parser_Config, str_Section, str_Option)
        if bool_OPTION_is_expected:
            if not bool_Option_Exists:
                str_Section_Err, str_Option_Err, value_Type_Err = obj_Config.static_str_Section__INI_File, obj_Config.static_str_Option__INI_UID, 0
                value_Opton_Err = self.func_Read_Config_File_OPTION(str_Section_Err, str_Option_Err, value_Type_Err)
                str_Message_Text = 'Non-existent OPTION error READING config_parser (' + obj_Config.static_str_Value__INI_Filename + '_' + str(value_Opton_Err) + ') ; SECTION:' + str_Section + '; OPTION :' + str_Option
                int_Stack_Trace_Level = 3
                with SSErrorOperation([]) as obj_SSErrorOp:
                    obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text)
                pass
            pass
        pass
        if bool_Option_Exists:
            if bool_OPTION_is_List:
                value_Option = OrderedDict(obj_Config.config_parser_Config.items(str_Section))
            else:
                value_Option = self.func_Read_Config_File_OPTION(str_Section, str_Option, value_Type)
            pass
        pass
        ''' Remove any whitespaces, CRLF, TAB etc '''
        if isinstance(value_Option, str):
            value_Option = self.func_Clean_String__Of_Control_Characters(value_Option)
        pass
        return bool_Option_Exists, value_Option  

    def func_Clean_String__Of_Control_Characters(self, str_UnClean):
        
        '''
        Examples of unicode categories:
        >>> from unicodedata import category
        >>> category('\r')      # carriage return --> Cc : control character
        'Cc'
        >>> category('\0')      # null character ---> Cc : control character
        'Cc'
        >>> category('\t')      # tab --------------> Cc : control character
        'Cc'
        >>> category(' ')       # space ------------> Zs : separator, space
        'Zs'
        >>> category(u'\u200A') # hair space -------> Zs : separator, space
        'Zs'
        >>> category(u'\u200b') # zero width space -> Cf : control character, formatting
        'Cf'
        >>> category('A')       # letter "A" -------> Lu : letter, uppercase
        'Lu'
        >>> category(u'\u4e21') #  ---------------> Lo : letter, other
        'Lo'
        >>> category(',')       # comma  -----------> Po : punctuation
        'Po'
        >>>        
        '''
        
        str_Clean = ''
        
        if isinstance(str_UnClean, str): 
            
            ''' Convert to unicode to detect categories '''
            str_UnClean = unicode(str_UnClean)
            str_Clean = "".join(ch for ch in str_UnClean if unicodedata__category(ch)[0]!="C")
            ''' Convert to back to str '''
            str_Clean = str(str_Clean)
        pass
    
        return str_Clean
    

    def func_Read_Config_File_OPTION(self, str_Section, str_Option, value_Type, config_parser_Config=None):

        bool_Success = False
        
        if config_parser_Config == None:
            if self.config_parser_Config != None:
                config_parser_Config = self.config_parser_Config
                bool_Success = True
            else:
                bool_Success = False
            pass
        pass
        
        value_Read = None
        if bool_Success:
            value_Read = self.obj_Config.func_Get_Config_File_OPTION_Specifying_Option_Type(config_parser_Config, str_Section, str_Option, value_Type)
        pass
    
        return value_Read

    def func_Check_If_Config_File_SECTION_Exists(self, config_parser_Config, str_Section):
        
        bool_Success = self.obj_Config.func_Check_If_Config_File_SECTION_Exists(config_parser_Config, str_Section)

        return bool_Success
    
    
    def func_Check_If_Config_File_SECTION_Is_Expected(self, obj_Config, str_Section, bool_SECTION_is_expected):
        
        bool_Success = self.func_Check_If_Config_File_SECTION_Exists(obj_Config.config_parser_Config, str_Section)

        ''' Trigger Error if the SECTION is expected but missing'''
        if bool_SECTION_is_expected:
            if not bool_Success:
                str_Section_Err, str_Option_Err, value_Type_Err = obj_Config.static_str_Section__INI_File, obj_Config.static_str_Option__INI_UID, 0
                value_Opton_Err = obj_Config.func_Read_Config_File_OPTION(str_Section_Err, str_Option_Err, value_Type_Err)
                str_Message_Text = 'Non-existent SECTION error READING config_parser (' + obj_Config.static_str_Value__INI_Filename + '_' + str(value_Opton_Err) + ') ; SECTION:' + str_Section
                int_Stack_Trace_Level = 3
                with SSErrorOperation([]) as obj_SSErrorOp:
                    obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text)
                pass
            pass
        pass                    
        return bool_Success
        
    def func_Check_If_Config_File_OPTION_Exists(self, config_parser_Config, str_Section, str_Option):
        
        bool_Success = self.obj_Config.func_Check_If_Config_File_OPTION_Exists(config_parser_Config, str_Section, str_Option)
        
        return bool_Success    

    def func_Check_If_Config_File_SECTION_And_OPTION_Exists(self, str_Section, str_Option, config_parser_Config=None):
        
        bool_Success = False
        
        if config_parser_Config == None:
            
            if self.config_parser_Config != None:
                config_parser_Config = self.config_parser_Config
                bool_Success = True
            else:
                bool_Success = False
            pass
        else:
            bool_Success = True
        pass
    
        if bool_Success:        
            bool_Success = self.func_Check_If_Config_File_SECTION_Exists(config_parser_Config, str_Section)
            if bool_Success:
                bool_Success = self.func_Check_If_Config_File_OPTION_Exists(config_parser_Config, str_Section, str_Option)
            pass
        pass
    
        return bool_Success    
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
    
    
    
    
    