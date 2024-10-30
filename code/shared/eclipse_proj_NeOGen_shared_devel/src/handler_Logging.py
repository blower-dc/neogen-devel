'''
Created on 20 Jan 2015

@author: Darwin
'''

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
import os
import logging
import re

static_Log_Format_Default_1 = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
static_Log_Format_Default_2 = '%(asctime)s %(name)-12s %(levelname)-6s %(module)-14s : %(message)s'
# logging.basicConfig(level=logging.DEBUG,
#                     format=static_Log_Format_Default_2,
#                     datefmt='%m-%d %H:%M'
#                     )

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

static_stringDelimiter_DOT = '.'
static_stringDelimiter_RESULTS_START = '<>' 
static_stringDelimiter_SEMI_COLON = ';'
static_stringDelimiter_SPACE = ' '
static_stringDelimiter_UNDERSCORE = '_'

class Logging(object):

    obj_Logger = None
    str_Logger_Name = ''
    str_Logger_Level = ''
    bool_ClearLogFileAtStart = True
    bool_LogToConsole = True
    bool_LogToFile = True
    strLogFile = ''
    strLogPath = ''
    dict_Default_Logger_Specs = {}
    
    def __init__(self):


        logging.basicConfig(level=logging.DEBUG,
                            format=static_Log_Format_Default_2,
                            datefmt='%m-%d %H:%M'
                            )

        self.obj_Internal_Logger = None
        
        self.obj_Internal_Logger = logging.getLogger(__name__)

        str_Current_Col_Index = str(
                                     '0' +
                                     static_stringDelimiter_DOT +
                                     '0' +
                                     static_stringDelimiter_DOT +
                                     '0' +
                                     static_stringDelimiter_DOT +
                                     '0')
        self.dict_Default_Logger_Specs = {}
        
    def func_Initialise_Default_Loggers(self):
        #list_tuple_Logger_Specs = [('',''),('app_debug', 'debug'),(True,False), (True,True)]
        #list_tuple_Logger_Specs = [('',''),('app_debug', 'debug'),(True,False), (True,True)]
        
        if self.dict_Default_Logger_Specs == {}:
            self.dict_Default_Logger_Specs = {'':{'Level':'','LogToConsole':True,'LogToFile':True}
                                         ,'app_debug':{'Level':'debug','LogToConsole':True,'LogToFile':True}}
            
        pass
    
#         for tuple_Logger_Name in list_tuple_Logger_Specs: 
#             self.func_Initialise_Default_Loggers_By_List(tuple_Logger_Name)
#         pass
        for key_Logger_Name, value_Dict_Specs in self.dict_Default_Logger_Specs.iteritems(): 
            self.func_Initialise_Default_Loggers_By_Dict(key_Logger_Name, value_Dict_Specs)
        pass
    
            
    def func_Initialise_Default_Loggers_By_Dict(self, str_Logger_Name, dict_Logger_Specs):
        
        self.str_Logger_Name = str_Logger_Name
        str_Logger_Name = str_Logger_Name
        self.str_Logger_Level = dict_Logger_Specs['Level']
        str_Logger_Level = dict_Logger_Specs['Level']
        bool_LogToConsole = dict_Logger_Specs['LogToConsole']
        bool_LogToFile = dict_Logger_Specs['LogToFile']

        if str_Logger_Name == '':
            self.obj_Internal_Logger.info('Initialising default logger')
            self.bool_LogToConsole = bool_LogToConsole
            self.bool_LogToFile = bool_LogToFile
            self.func_Initialise_Class_Properties(str_Logger_Name, str_Logger_Level)
            #No console config as that is set by default in logging.basicConfig() above

            #Config the file handler for the default logger
            if self.bool_LogToFile:
                self.func_Initialise_File_Logging_Handler(str_Logger_Name, str_Logger_Level)
            pass
        pass
        
        if str_Logger_Name == 'app_debug':
            self.obj_Internal_Logger.info('Initialising DEBUG only logger: %s ' % self.str_Logger_Name)
            self.bool_LogToConsole = bool_LogToConsole
            self.bool_LogToFile = bool_LogToFile
            self.func_Initialise_Class_Properties(str_Logger_Name, str_Logger_Level)
            #Config the console handler for this logger
            if self.bool_LogToConsole:
                self.func_Initialise_Console_Logging_Handler(str_Logger_Name, str_Logger_Level)
            pass            
            #Config the file handler for this logger
            if self.bool_LogToFile:
                self.func_Initialise_File_Logging_Handler(str_Logger_Name, str_Logger_Level)
            pass
            obj_Logger = logging.getLogger(str_Logger_Name)
            obj_Logger.propagate = False
            
        pass
            
    def func_Initialise_Default_Loggers_By_List_RETIRED(self, tuple_Logger_Name):
        
        self.str_Logger_Name, self.str_Logger_Level = tuple_Logger_Name
        str_Logger_Name, str_Logger_Level = tuple_Logger_Name

        if str_Logger_Name == '':
            self.obj_Internal_Logger.info('Initialising default logger')
            self.bool_LogToConsole = True
            self.bool_LogToFile = True
            self.func_Initialise_Class_Properties(str_Logger_Name, str_Logger_Level)
            #No console config as that is set by default in logging.basicConfig() above
            
            #Config the file handler for the default logger
            if self.bool_LogToFile:
                self.func_Initialise_File_Logging_Handler(str_Logger_Name, str_Logger_Level)
            pass
        pass
        
        if str_Logger_Name == 'app_debug':
            self.obj_Internal_Logger.info('Initialising DEBUG only logger: %s ' % self.str_Logger_Name)
            self.bool_LogToConsole = True
            self.bool_LogToFile = True
            self.func_Initialise_Class_Properties(str_Logger_Name, str_Logger_Level)
            #Config the console handler for this logger
            if self.bool_LogToConsole:
                self.func_Initialise_Console_Logging_Handler(str_Logger_Name, str_Logger_Level)
            pass            
            #Config the file handler for this logger
            if self.bool_LogToFile:
                self.func_Initialise_File_Logging_Handler(str_Logger_Name, str_Logger_Level)
            pass
            obj_Logger = logging.getLogger(str_Logger_Name)
            obj_Logger.propagate = False
            
        pass
    
    def func_Initialise_New_Logger(self):
        
       
        if self.str_Logger_Name == '':
            self.obj_Internal_Logger.error('No Logger Name Supplied. Logger was not created.')
        else:
            self.obj_Internal_Logger.info('Initialising' + self.str_Logger_Level + ' logger: %s ' % self.str_Logger_Name)
            self.func_Initialise_Class_Properties(self.str_Logger_Name, self.str_Logger_Level)
            #Config the console handler for this logger
            if self.bool_LogToConsole:
                self.func_Initialise_Console_Logging_Handler(self.str_Logger_Name, self.str_Logger_Level)
            pass            
            #Config the file handler for this logger
            if self.bool_LogToFile:
                self.func_Initialise_File_Logging_Handler(self.str_Logger_Name, self.str_Logger_Level)
            pass
            obj_Logger = logging.getLogger(self.str_Logger_Name)
            obj_Logger.propagate = False
            
        return obj_Logger

            
    def func_Initialise_Class_Properties(self, str_Logger_Name, str_Logger_Level):

        boolSuccess = False

#         if self.str_Logger_Name == '':
#             self.str_Logger_Name = 'app_log'
#         pass
    
        if self.bool_LogToConsole:
            self.obj_Internal_Logger.info('Logging to CONSOLE enabled')
        else:
            self.obj_Internal_Logger.info('Logging to CONSOLE DISABLED for handler: %s' % str_Logger_Name)
        pass
    
    
        if self.bool_LogToFile:
            if self.strLogFile == '':
                #Use default file path & name
                
                self.strLogPath = os.getcwd() + "\\log"
                self.strLogFile = "dcb_logging.log"
                self.obj_Internal_Logger.info('Logging to DEFAULT LOG FILE enabled:' + os.path.join(self.strLogPath, self.strLogFile))
            else:
                self.obj_Internal_Logger.info('Logging to LOG FILE enabled:' + os.path.join(self.strLogPath, self.strLogFile))
            pass
        else:
            self.obj_Internal_Logger.warn('WARNING - Logging to file DISABLED for handler: %s' % str_Logger_Name)
        pass
    
        if self.bool_LogToConsole == False and self.bool_LogToFile == False:

            self.obj_Internal_Logger.warn('WARNING WARNING WARNING - Logging to both console AND file is DISABLED - WARNING WARNING WARNING')
        pass
    
        boolSuccess = True
        
        return boolSuccess

    def func_Initialise_Console_Logging_Handler(self, str_Logger_Name, str_Logger_Level):

        boolSuccess = False

        if self.bool_LogToConsole:
            try:
                loggingHandler = logging.StreamHandler()
                if str_Logger_Name == '':
                    loggingHandler.setLevel(logging.INFO)
                else:
                    level = LEVELS.get(str_Logger_Level, logging.NOTSET)
                    loggingHandler.setLevel(level)
                pass
                loggingFormatter = logging.Formatter(static_Log_Format_Default_2)
                loggingHandler.setFormatter(loggingFormatter)
                loggingHandler.name = 'log_handler_CONSOLE_' + str_Logger_Name
                
                # add the handler to the root logger
                logging.getLogger(str_Logger_Name).addHandler(loggingHandler)
                self.obj_Internal_Logger.info('Logging enabled at level:' + str_Logger_Level + ' for CONSOLE handler: ' + str_Logger_Name + ' enabled : ' + self.strLogPath + '\\' + self.strLogFile)
                boolSuccess = True
            except Exception as exception:
                self.obj_Internal_Logger.error('Failed add logging handler: %s' % str_Logger_Name, exc_info=True)
                self.obj_Internal_Logger.error(exception.message, exception.args)
                raise
            pass
        pass
        
        return boolSuccess 
       
    def func_Initialise_File_Logging_Handler(self, str_Logger_Name, str_Logger_Level):

        boolSuccess = False

        if self.bool_LogToFile:
            try:
                if os.path.exists(self.strLogPath):
                    pass
                else:
                    os.makedirs(self.strLogPath)
                pass
                if self.bool_ClearLogFileAtStart:
                    #loggingHandler = logging.FileHandler(os.path.join(self.strLogPath, self.strLogFile), mode='w')
                    try:
                        loggingHandler = logging.FileHandler(os.path.join(self.strLogPath, self.strLogFile), mode='w')
                    except Exception as exception:
                        self.obj_Internal_Logger.error('Failed to create logging handler: %s' % str_Logger_Name, exc_info=True)
                        self.obj_Internal_Logger.error(exception.message, exception.args)
                        raise
                    pass
                else:
                    #loggingHandler = logging.FileHandler(os.path.join(self.strLogPath, self.strLogFile))
                    try:
                        loggingHandler = logging.FileHandler(os.path.join(self.strLogPath, self.strLogFile))
                    except Exception as exception:
                        self.obj_Internal_Logger.error('Failed to create logging handler: %s' % str_Logger_Name, exc_info=True)
                        self.obj_Internal_Logger.error(exception.message, exception.args)
                        raise
                    pass                        
                pass
            
                if str_Logger_Name == '':
                    loggingHandler.setLevel(logging.DEBUG)
                else:
                    level = LEVELS.get(str_Logger_Level, logging.NOTSET)
                    loggingHandler.setLevel(level)
                pass
                loggingFormatter = logging.Formatter(static_Log_Format_Default_2)
                loggingHandler.setFormatter(loggingFormatter)
                loggingHandler.name = 'log_handler_FILE_' + str_Logger_Name
                
                # add the handler to the root logger
                logging.getLogger(self.str_Logger_Name).addHandler(loggingHandler)
                self.obj_Internal_Logger.info('Logging enabled at level:' + str_Logger_Level + ' for FILE handler: ' + str_Logger_Name + ' enabled : ' + self.strLogPath + '\\' + self.strLogFile)
                boolSuccess = True

            except Exception as exception:
                self.obj_Internal_Logger.error('Failed add logging handler: %s' % str_Logger_Name, exc_info=True)
                self.obj_Internal_Logger.error(exception.message, exception.args)
                raise
            pass
        
        return boolSuccess    
    
    '''
    -------------------------
    Results Loggers
    -------------------------
    '''
    def func_Log_Results_Header(self, obj_Log_Results, str_Heading_1, str_Heading_Prefix_1, dict_Results):

        str_ID_Suf = static_stringDelimiter_UNDERSCORE
        #str_ID_Suf = static_stringDelimiter_SPACE
        int_Level = 1

        ''' Log header '''
        str_Log_Line = str(static_stringDelimiter_RESULTS_START
                           + static_stringDelimiter_SEMI_COLON
                           + self.func_Get_Log_Current_Column_Index(True, int_Level, True, str_ID_Suf)
                           + str_Heading_1)
        
        for key in dict_Results.keys():
            str_Log_Line += str(static_stringDelimiter_SEMI_COLON
                                + self.func_Get_Log_Current_Column_Index(False, int_Level, True, str_ID_Suf)
                                + str_Heading_Prefix_1
                                + str(key))
           
        pass
        obj_Log_Results.info(str_Log_Line)
        
        return True

    def func_Log_Results_Detail(self, str_Results_1, obj_Log_Results, dict_Results):

        str_ID_Suf = static_stringDelimiter_SPACE
        int_Level = 1
        
        ''' Log results '''

        str_Log_Line = str(static_stringDelimiter_RESULTS_START
                           + static_stringDelimiter_SEMI_COLON
                           + str_Results_1)
        
        for value in dict_Results.values():
            str_Log_Line += str(static_stringDelimiter_SEMI_COLON
                                + str(value))
            
        pass
        
        obj_Log_Results.info(str_Log_Line)
        
        return True

    def func_Log_MultiLine_Results_Header(self, obj_Log_Results, str_Heading_1, str_Heading_Prefix_1, dict_MultiLine_Results):

        str_ID_Suf = static_stringDelimiter_UNDERSCORE
        #str_ID_Suf = static_stringDelimiter_SPACE
        int_Level = 1

        ''' Log header '''

        str_Log_Line = str(static_stringDelimiter_RESULTS_START
                            + static_stringDelimiter_SEMI_COLON
                            + self.func_Get_Log_Current_Column_Index(True, int_Level, True, str_ID_Suf)
                            + 'Result_MultiLine_Count'
                            + static_stringDelimiter_SEMI_COLON
                            + self.func_Get_Log_Current_Column_Index(False, int_Level, True, str_ID_Suf)
                            + str_Heading_1)
        
        dict_Results = dict_MultiLine_Results[0]
        
        for key in dict_Results.keys():
            str_Log_Line += str(static_stringDelimiter_SEMI_COLON
                                + self.func_Get_Log_Current_Column_Index(False, int_Level, True, str_ID_Suf)
                                + str_Heading_Prefix_1
                                + key)
           
        pass
        obj_Log_Results.info(str_Log_Line)
        
        return True

    def func_Log_MultiLine_Results_Detail(self, str_Results_1, obj_Log_Results, dict_MultiLine_Results):

        ''' Log results '''

        int_Result_MultiLine_Total = len(dict_MultiLine_Results)
        
        for int_Result_MultiLine_Count in range(0, int_Result_MultiLine_Total):
            
            dict_Results = dict_MultiLine_Results[int_Result_MultiLine_Count]
            str_Log_Line = ''
            str_Log_Line = str(static_stringDelimiter_RESULTS_START
                                + static_stringDelimiter_SEMI_COLON
                                + str(int_Result_MultiLine_Count)
                                + static_stringDelimiter_SEMI_COLON
                                + str_Results_1
                                + static_stringDelimiter_SEMI_COLON)
            
#             for value in dict_Results.values():
#                 str_Log_Line += str(static_stringDelimiter_SEMI_COLON
#                                     + str(value))
            str_Log_Line += static_stringDelimiter_SEMI_COLON.join(str(value) for value in dict_Results.values())

                
            pass
            obj_Log_Results.info(str_Log_Line)
            
        pass
        
        return True

    '''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Generic Logging Operations
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''
   
    def func_Get_Log_Current_Column_Index(self, bool_Reset, intLevel, bool_Add_Suffix = False, str_Suffix = ''):
        
        if bool_Reset:
            self.str_Current_Col_Index = str(
                                             str(intLevel) +
                                             static_stringDelimiter_DOT +
                                             '0' +
                                             static_stringDelimiter_DOT +
                                             '0' +
                                             static_stringDelimiter_DOT +
                                             '0')
        else:
            list_Delimiters = [str_Suffix, static_stringDelimiter_DOT]
            L, h, i, j, _ = re.split('|'.join(re.escape(x) for x in list_Delimiters), self.str_Current_Col_Index)            
            #L, h, i, j = self.str_Current_Col_Index.split(static_stringDelimiter_DOT)
            
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
                                static_stringDelimiter_DOT +
                                str(h) +
                                static_stringDelimiter_DOT +
                                str(i) +
                                static_stringDelimiter_DOT +
                                str(j))
            
        pass

        if bool_Add_Suffix:
            self.str_Current_Col_Index = self.str_Current_Col_Index + str(str_Suffix)
        pass
    
        return self.str_Current_Col_Index
 
               