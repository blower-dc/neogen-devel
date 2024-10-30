'''
Created on 29 Jan 2015

@author: dblowe
'''
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS
#
#------------------< Import python modules
from collections import OrderedDict
import ConfigParser
from os import path as os__path
#------------------< Import DCB_General modules
# DEBUG Imports
from logging import getLogger as logging__getLogger
from handler_Debug import Timer2
from handler_Debug import Debug_Location
#
from FileHandler import FileHandler
from handler_Logging import Logging


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
class ConfigOperation(object):

    '''
    --------------------------------------------------------------------------------------------------------
    # <<<<<<<<<<<<<<<<<< CLASS INIT
    --------------------------------------------------------------------------------------------------------
    '''   

    #str_Results_Base_Path = ''
    ''' Get Run Display Logger '''
    obj_Log_Run_Display = None
               
    ''' Get Default Logger '''
    obj_Log_Default_Display = None

    ''' Get Debug Logger '''
    obj_Log_Debug_Display = None

    ''' Get Debug Timer '''
    obj_Log_Debug_Timing = None
    

    def __enter__(self):
        
        return self 
         
    def __init__(self, obj_Globals_From_Parent_Object):
        '''
        Constructor
        '''
        
        self.globals_From_Parent_Object = obj_Globals_From_Parent_Object
        
        self.str_Current_Col_Index = str(
                                     '0' +
                                     self.globals_From_Parent_Object.StringDelimiters.static_stringDelimiter_DOT +
                                     '0' +
                                     self.globals_From_Parent_Object.StringDelimiters.static_stringDelimiter_DOT +
                                     '0' +
                                     self.globals_From_Parent_Object.StringDelimiters.static_stringDelimiter_DOT +
                                     '0')
                
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
        self.obj_Log_Run_Display = logging__getLogger(self.globals_From_Parent_Object.Logger_Run_Display.static_Logger_Name__Run_Display)
                   
        ''' Get Default Logger '''
        self.obj_Log_Default_Display = logging__getLogger(self.globals_From_Parent_Object.Logger_Default_Display.static_Logger_Name__Default_Display)
        ''' NOTE: Name is obj_Log_Default '''
        self.obj_Log_Default = self.obj_Log_Default_Display

        ''' Get Debug Logger '''
        ''' NOTE: Name is obj_Log_Debug_Display '''
        self.obj_Log_Debug_Display = logging__getLogger(self.globals_From_Parent_Object.Logger_Debug_Display.static_Logger_Name__Debug_Display)

        ''' Get Debug Timer '''
        self.obj_Log_Debug_Timing = None
        if self.globals_From_Parent_Object.Logger_Debug_Timing.bool_Debug_Timing:
            self.obj_Log_Debug_Timing = logging__getLogger(self.globals_From_Parent_Object.Logger_Debug_Timing.static_Logger_Name__Debug_Timing)
        pass
                                
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

    '''
    --------------------------------------------------------------------------------------------------------
    # Utility Processing
    --------------------------------------------------------------------------------------------------------
    '''

    def func_Create_Config_File_Parser(self):
        
        bool_Success = False
        
        config_parser_Config = ConfigParser.ConfigParser()
        
        return config_parser_Config

    def func_Open_Config_File(self, str_Config_File_Path_And_Name):
        
        bool_Success = False
        fileHandle = None
        
        with FileHandler() as obj_FileOp:
            fileHandle = obj_FileOp.fileOpen(str_Config_File_Path_And_Name, 'write')
            
            if fileHandle != None:
                bool_Success = True
            else:
                with Debug_Location() as obj_DebugLoc:
                    str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                pass
                str_Message = str_Message_Location + ' >> UNEXPECTED ERROR - Config file could not be created/opened: ' + str(str_Config_File_Path_And_Name)
                self.obj_Log_Default_Display.error(str_Message)
                raise ValueError(str_Message)
            pass               
        pass
    
        return fileHandle
    
    def func_Read_Config_File_From_Config_Parser(self, config_parser_Config, list_Filenames__Config):

        bool_Success = False
        
        list_Filenames__Config_Successfully_Read = config_parser_Config.read(list_Filenames__Config)

        int_Files_To_Read = len(list_Filenames__Config)
        int_Files_Read = len(list_Filenames__Config_Successfully_Read)
        list_Files_Not_Read = set(list_Filenames__Config) - set(list_Filenames__Config_Successfully_Read)
        int_Files_Not_Read = len(list_Files_Not_Read)
        
        if int_Files_Not_Read == 0 :
            bool_Success = True
        else:
            with Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Message = str_Message_Location + ' >> UNEXPECTED ERROR - Not all of the requested list of Config files could be read; #Files to read: ' + str(int_Files_To_Read) + '; #Files read: ' + str(int_Files_Read) + '; #Files NOT read: ' + str(int_Files_Not_Read) + '\n\t; List files to read: ' + str(list_Filenames__Config) + '\n\t; list files read' + str(list_Filenames__Config_Successfully_Read) + '\n\t; list files NOT read: ' + str(list_Files_Not_Read)
            self.obj_Log_Default_Display.error(str_Message)
            raise ValueError(str_Message)
            bool_Success = False
            config_parser_Config = None
        pass
            
        return config_parser_Config

    def func_Write_Config_File(self, config_parser_Config, str_Config_File_Path_And_Name):
        
        bool_Success = False
        file_Handle = None

        ''' Check if path exists - If not create it '''
        with FileHandler() as obj_FileHandler:
            str_Config_File_Path, _ = os__path.split(str_Config_File_Path_And_Name)
            obj_FileHandler.method_Create_Path(str_Config_File_Path)
        pass        
        
        with FileHandler() as obj_FileOp:
            file_Handle = obj_FileOp.fileOpen(str_Config_File_Path_And_Name, 'write')
            
            if file_Handle != None:
                config_parser_Config.write(file_Handle)
                bool_Success = True
            else:
                with Debug_Location() as obj_DebugLoc:
                    str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                pass
                str_Message = str_Message_Location + ' >> UNEXPECTED ERROR - Config file could not be opened/written: ' + str(str_Config_File_Path_And_Name)
                self.obj_Log_Default_Display.error(str_Message)
                raise ValueError(str_Message)
            pass               
        pass
    
        return bool_Success

    def func_Set_Values_in_Config_File_From_Dict(self, config_parser_Config, dict_Section_Key_Option_Value_Tuple):
        
        bool_Success = False
        
        '''
        -------------------------
        Add Keys and Values to section
        -------------------------
        '''
        for str_Section, list_Options in dict_Section_Key_Option_Value_Tuple.items():

            for (str_Option, value_Option) in list_Options:
                
                if isinstance(value_Option, (str,bool,int,float)):
                     config_parser_Config = self.func_Set_Values_in_Config_File_Section(config_parser_Config, str_Section, str_Option, value_Option)
                else:
                    with Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                        pass
                        str_Message = str_Message_Location + ' >> UNEXPECTED ERROR - value_Option is not a valid type ; SECTION: ' + str_Section + ' ; OPTION: ' + str(str_Option) + ' ; VALUE: ' + str(value_Option) + ' ; VALUE_TYPE: ' + str(type(value_Option))
                        self.obj_Log_Default_Display.error(str_Message)
                        raise ValueError(str_Message)
                        bool_Success = False
                        config_parser_Config = None
                    pass
                pass
            pass
        pass   
        
        return config_parser_Config
    
    
#     
#     def func_Set_Values_in_Config_File_Section(self, config_parser_Config, str_Section, str_Option, value_Option):
#         
#         bool_Success = False
#         
#         '''
#         -------------------------
#         Check if Section exists, if not create it
#         -------------------------
#         '''
#         bool_Success = self.func_Add_Config_File_SECTION(config_parser_Config, str_Section)
# 
#         '''
#         -------------------------
#         Add Keys and Values to section
#         -------------------------
#         '''
#         try:
#             config_parser_Config.set(str(str_Section), str(str_Option), value_Option)
#         except:
#             with Debug_Location() as obj_DebugLoc:
#                 str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
#             pass
#             str_Message = str_Message_Location + ' >> UNEXPECTED ERROR - SECTION: ' + str_Section + ' cant set OPTION: ' + str(str_Option) + ' and VALUE: ' + str(value_Option)
#             self.obj_Log_Default_Display.error(str_Message)
#             raise ValueError(str_Message)
#             bool_Success = False
#             config_parser_Config = None
#         pass
#     
#         return config_parser_Config
#     
    def func_Set_Values_in_Config_File_Section(self, config_parser_Config, str_Section, str_Option, value_Option):
        
        bool_Success = False
        
        '''
        -------------------------
        Check if Section exists, if not create it
        -------------------------
        '''
        bool_Success = self.func_Add_Config_File_SECTION(config_parser_Config, str_Section)

        '''
        -------------------------
        Add Keys and Values to section
        -------------------------
        '''
        try:
            config_parser_Config.set(str(str_Section), str(str_Option), value_Option)
        except:
            with Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Message = str_Message_Location + ' >> UNEXPECTED ERROR - SECTION: ' + str_Section + ' cant set OPTION: ' + str(str_Option) + ' and VALUE: ' + str(value_Option)
            self.obj_Log_Default_Display.error(str_Message)
            raise ValueError(str_Message)
            bool_Success = False
            config_parser_Config = None
        pass
    
        return config_parser_Config

    def func_Remove_OPTIONS_in_Config_File_From_Dict(self, config_parser_Config, dict_Section_Key_Option_Value):
        
        bool_Success = False
        
        '''
        -------------------------
        Removed Keys and Values from a section
        -------------------------
        '''
        for str_Section, list_Options in dict_Section_Key_Option_Value.items():

            for str_Option in list_Options:
                
                bool_Success, config_parser_Config = self.func_Remove_OPTION_From_Config_File_Section(config_parser_Config, str_Section, str_Option)
            pass   
        pass   
        
        return bool_Success, config_parser_Config
    
    def func_Remove_SECTION_From_Config_File_Section(self, config_parser_Config, str_Section):
        
        bool_Success = False
        
        '''
        -------------------------
        Check if Section exists, if not create it
        -------------------------
        '''
        #bool_Success = self.func_Check_If_Config_File_SECTION_Exists(config_parser_Config, str_Section)

        '''
        -------------------------
        Add Keys and Values to section
        -------------------------
        '''
        try:
            bool_Section_Exists = False
            bool_Section_Exists = config_parser_Config.remove_section(str(str_Section))
            bool_Success = True
        except  Exception, error:
            with Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Message = str_Message_Location + ' >> UNEXPECTED ERROR - SECTION: ' + str_Section + ' cant set OPTION: ' + str(str_Option) + ' and VALUE: ' + str(value_Option)
            self.obj_Log_Default_Display.error(str_Message)
            raise ValueError(str_Message)
            bool_Success = False
            config_parser_Config = None
        pass
    
        return bool_Success, config_parser_Config
    
    def func_Remove_OPTION_From_Config_File_Section(self, config_parser_Config, str_Section, str_Option):
        
        bool_Success = False
        
        '''
        -------------------------
        Check if Section exists, if not create it
        -------------------------
        '''
        #bool_Success = self.func_Check_If_Config_File_SECTION_Exists(config_parser_Config, str_Section)

        '''
        -------------------------
        Add Keys and Values to section
        -------------------------
        '''
        try:
            bool_Option_Exists = False
            bool_Option_Exists = config_parser_Config.remove_option(str(str_Section), str(str_Option))
            bool_Success = True
        except  ConfigParser.NoSectionError:
            bool_Success = True
        except  Exception, error:
            with Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Message = str_Message_Location + ' >> UNEXPECTED ERROR - SECTION: ' + str_Section + ' cant set OPTION: ' + str(str_Option) + ' and VALUE: ' + str(value_Option)
            self.obj_Log_Default_Display.error(str_Message)
            raise ValueError(str_Message)
            bool_Success = False
            config_parser_Config = None
        pass
    
        return bool_Success, config_parser_Config
    
    def func_Get_Config_File_OPTION_Specifying_Option_Type_RETIRE(self, config_parser_Config, str_Section, str_Option, int_Value_Type):

        if self.globals_From_Parent_Object.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()
        pass   
                    
        value = None
        bool_Success = False
        
        try:
            if int_Value_Type == 0: #STRING
                value = config_parser_Config.get(str_Section, str_Option)
                bool_Success = True
            elif int_Value_Type == 1: #BOOL
                value = config_parser_Config.getboolean(str_Section, str_Option)
                bool_Success = True                
            elif int_Value_Type == 2: #INT
                value = config_parser_Config.getint(str_Section, str_Option)
                bool_Success = True                
            elif int_Value_Type == 3: #FLOAT
                value = config_parser_Config.getfloat(str_Section, str_Option)
                bool_Success = True
            else:
                with Debug_Location() as obj_DebugLoc:
                    str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                pass
                str_Message = str_Message_Location + ' >> OPTION value type is not valid ; int_Value_Type: ' + str(str_Section) + ' ; OPTION:' + str(str_Option) + ' ; Type:' + str(int_Value_Type) 
                self.obj_Log_Default_Display.error(str_Message)
                raise ValueError(str_Message)
            pass
        except ConfigParser.NoSectionError:
            with Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Message = str_Message_Location + ' >> SECTION could not be found when getting OPTION of specific type ;SECTION: ' + str(str_Section) + ' ; OPTION:' + str(str_Option) + ' ; Type:' + str(int_Value_Type)
            self.obj_Log_Default_Display.error(str_Message)
            raise ValueError(str_Message)
        except ConfigParser.NoOptionError:
            with Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Message = str_Message_Location + ' >> OPTION of specific type could not be found ;SECTION: ' + str(str_Section) + ' ; OPTION:' + str(str_Option) + ' ; Type:' + str(int_Value_Type)
            self.obj_Log_Default_Display.error(str_Message)
            raise ValueError(str_Message)
        except:
            with Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Message = str_Message_Location + ' >> UNEXPECTED ERROR - OPTION of specific type could not be retrieved ; SECTION: ' + str(str_Section) + ' ; OPTION:' + str(str_Option) + ' ; Type:' + str(int_Value_Type)
            self.obj_Log_Default_Display.error(str_Message)
            raise ValueError(str_Message)
        pass

        #DEBUG_ON
        if self.globals_From_Parent_Object.Logger_Debug_Display.bool_Debug_Display:
            with Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Msg_Prefix = self.globals_From_Parent_Object.Logger_Debug_Display.static_str_Logger_Message_Prefix
            self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
        pass
        bool_Display_Option_Values = True
        if bool_Success and bool_Display_Option_Values:
            self.obj_Log_Debug_Display.debug('OPTION Read \n\t; SECTION: ' + str(str_Section) + '\n\t; OPTION Type: ' + str(int_Value_Type) + '\n\t; OPTION: ' + str(str_Option) + '\n\t; VALUE: ' + str(value))
            #self.obj_Log_Debug_Display.debug(globalsSS.Output_Display_Constants.static_str_Message_Separator)
        pass
                    
        if self.globals_From_Parent_Object.Logger_Debug_Timing.bool_Debug_Timing:
            t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
            #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            #    t2 = Timer2(True)
            #    t2.Start()
            #pass                    
        pass
                
        return value
    
    def func_Get_Config_File_OPTION_Specifying_Option_Type(self, config_parser_Config, str_Section, str_Option, value_Type):

        if self.globals_From_Parent_Object.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()
        pass   
                    
        value = None
        bool_Success = False
        
        try:
            if isinstance(value_Type, str): #STRING
                value = config_parser_Config.get(str_Section, str_Option)
                bool_Success = True
            elif isinstance(value_Type, bool): #BOOL
                value = config_parser_Config.getboolean(str_Section, str_Option)
                bool_Success = True                
            elif isinstance(value_Type, int): #INT
                value = config_parser_Config.getint(str_Section, str_Option)
                bool_Success = True                
            elif isinstance(value_Type, float): #FLOAT
                value = config_parser_Config.getfloat(str_Section, str_Option)
                bool_Success = True
            else:
                with Debug_Location() as obj_DebugLoc:
                    str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                pass
                str_Message = str_Message_Location + ' >> OPTION value type is not valid ; int_Value_Type: ' + str(str_Section) + ' ; OPTION:' + str(str_Option) + ' ; Type:' + str(type(value_Type))
                self.obj_Log_Default_Display.error(str_Message)
                raise ValueError(str_Message)
            pass
        except ConfigParser.NoSectionError:
            with Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Message = str_Message_Location + ' >> SECTION could not be found when getting OPTION of specific type ;SECTION: ' + str(str_Section) + ' ; OPTION:' + str(str_Option) + ' ; Type:' + str(type(value_Type))
            self.obj_Log_Default_Display.error(str_Message)
            raise ValueError(str_Message)
        except ConfigParser.NoOptionError:
            with Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Message = str_Message_Location + ' >> OPTION of specific type could not be found ;SECTION: ' + str(str_Section) + ' ; OPTION:' + str(str_Option) + ' ; Type:' + str(type(value_Type))
            self.obj_Log_Default_Display.error(str_Message)
            raise ValueError(str_Message)
        except:
            with Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Message = str_Message_Location + ' >> UNEXPECTED ERROR - OPTION of specific type could not be retrieved ; SECTION: ' + str(str_Section) + ' ; OPTION:' + str(str_Option) + ' ; Type:' + str(type(value_Type))
            self.obj_Log_Default_Display.error(str_Message)
            raise ValueError(str_Message)
        pass

        #DEBUG_ON
        if self.globals_From_Parent_Object.Logger_Debug_Display.bool_Debug_Display:
            with Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Msg_Prefix = self.globals_From_Parent_Object.Logger_Debug_Display.static_str_Logger_Message_Prefix
            self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
        pass
        bool_Display_Option_Values = True
        if bool_Success and bool_Display_Option_Values:
            self.obj_Log_Debug_Display.debug('OPTION Read \n\t; SECTION: ' + str(str_Section) + '\n\t; OPTION Type: ' + str(type(value_Type)) + '\n\t; OPTION: ' + str(str_Option) + '\n\t; VALUE: ' + str(value))
            #self.obj_Log_Debug_Display.debug(globalsSS.Output_Display_Constants.static_str_Message_Separator)
        pass
                    
        if self.globals_From_Parent_Object.Logger_Debug_Timing.bool_Debug_Timing:
            t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=False)
            #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            #    t2 = Timer2(True)
            #    t2.Start()
            #pass                    
        pass
                
        return value
    
    def func_Add_Config_File_SECTION(self, config_parser_Config, str_Section):
        
        bool_Success = False
        bool_Section_Exists = False
        '''
        -------------------------
        Check if Section exists, if not create it
        -------------------------
        '''
        bool_Section_Exists = self.func_Check_If_Config_File_SECTION_Exists(config_parser_Config, str_Section)

        '''
        -------------------------
        Create Section exists
        -------------------------
        '''        
        if not bool_Section_Exists:
            try:
                config_parser_Config.add_section(str_Section)
                bool_Success = True
            except config_parser_Config.DuplicateSectionError:
                with Debug_Location() as obj_DebugLoc:
                    str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                pass
                str_Message = str_Message_Location + ' >> SECTION to be added is duplicate: ' + str_Section
                self.obj_Log_Default_Display.info(str_Message)
                #raise ValueError(str_Message)
                bool_Success = False
            except:
                with Debug_Location() as obj_DebugLoc:
                    str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                pass
                str_Message = str_Message_Location + ' >> UNEXPECTED ERROR - SECTION could not be added: ' + str_Section
                self.obj_Log_Default_Display.error(str_Message)
                raise ValueError(str_Message)
                bool_Success = False
            pass
        pass
    
        return bool_Success

    def func_Check_If_Config_File_SECTION_Exists(self, config_parser_Config, str_Section):
        
        bool_Success = config_parser_Config.has_section(str_Section)
        
        return bool_Success
        
    def func_Check_If_Config_File_OPTION_Exists(self, config_parser_Config, str_Section, str_Option):
        
        bool_Success = config_parser_Config.has_option(str_Section, str_Option)
        
        return bool_Success

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
    
    
    
    
    