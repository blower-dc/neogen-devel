'''
Created on 20 Jan 2015

@author: Darwin
'''

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
import os
import logging

static_Log_Format_Default_1 = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
static_Log_Format_Default_2 = '%(asctime)s %(name)-12s %(levelname)-6s %(module)-14s : %(message)s'
logging.basicConfig(level=logging.DEBUG,
                    format=static_Log_Format_Default_2,
                    datefmt='%m-%d %H:%M'
                    )

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

class Logging(object):

    obj_Logger = None
    str_Logger_Name = ''
    str_Logger_Level = ''
    bool_ClearLogFileAtStart = True
    bool_LogToConsole = True
    bool_LogToFile = True
    strLogFile = ''
    strLogPath = ''
    
    def __init__(self):

        self.obj_Internal_Logger = None
        
        self.obj_Internal_Logger = logging.getLogger(__name__)
#         if self.obj_Internal_Logger == None:
#             self.obj_Internal_Logger = logging.getLogger(__name__)
#             self.obj_Internal_Logger.setLevel(logging.INFO)

        #self.obj_Logger.setLevel(logging.WARNING)
        #self.obj_Logger.setLevel(logging.ERROR)

# 
#         pass
#     
#     def __call__(self):
#  
    def func_Initialise_Default_Loggers(self):
        list_tuple_Logger_Specs = [('',''),('app_debug', 'debug')]
        for tuple_Logger_Name in list_tuple_Logger_Specs: 
            self.func_Initialise_Default_Loggers_By_List(tuple_Logger_Name)
        pass
    
            
    def func_Initialise_Default_Loggers_By_List(self, tuple_Logger_Name):
        
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
            
        pass

            
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
                self.obj_Internal_Logger.info('Logging to DEFAULT LOG FILE enabled:' + self.strLogPath + self.strLogFile)
            else:
                self.obj_Internal_Logger.info('Logging to LOG FILE enabled:' + self.strLogPath + self.strLogFile)
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

        if self.bool_LogToFile:
            try:
                loggingHandler = logging.StreamHandler()
                if str_Logger_Name == '':
                    
                    loggingHandler.setLevel(logging.INFO)
                else:
                    level = LEVELS.get(str_Logger_Level, logging.NOTSET)
                    loggingHandler.setLevel(level)
                pass
                #loggingFormatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
                #loggingFormatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
                loggingFormatter = logging.Formatter(static_Log_Format_Default_2)
                loggingHandler.setFormatter(loggingFormatter)

                # add the handler to the root logger
                #self.obj_Logger = logging.getLogger('').addHandler(loggingHandler)
                logging.getLogger(str_Logger_Name).addHandler(loggingHandler)
#                 self.obj_Logger = logging.getLogger(self.str_Logger_Name)
#                 self.obj_Logger.addHandler(loggingHandler)
                self.obj_Internal_Logger.info('Logging enabled at level:' + str_Logger_Level + ' for CONSOLE handler: ' + str_Logger_Name + ' enabled : ..%s' % self.strLogPath + '\\' + self.strLogFile)
                boolSuccess = True
            except (SystemExit, KeyboardInterrupt):
            
                raise
            
            except Exception, e:
             
                self.obj_Internal_Logger.error('Failed add logging handler: %s' % str_Logger_Name, exc_info=True)
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
                    loggingHandler = logging.FileHandler(self.strLogPath + '\\' + self.strLogFile, mode='w')
                else:
                    loggingHandler = logging.FileHandler(self.strLogPath + '\\' + self.strLogFile)
                pass
            
                if str_Logger_Name == '':
                    loggingHandler.setLevel(logging.DEBUG)
                else:
                    level = LEVELS.get(str_Logger_Level, logging.NOTSET)
                    loggingHandler.setLevel(level)
                pass
                loggingFormatter = logging.Formatter(static_Log_Format_Default_2)
                loggingHandler.setFormatter(loggingFormatter)
                
                # add the handler to the root logger
                logging.getLogger(self.str_Logger_Name).addHandler(loggingHandler)
                #logging.getLogger(self.str_Logger_Name).addHandler(loggingHandler)
                #logging.getLogger('').addHandler(loggingHandler)
                #self.obj_Logger.addHandler(loggingHandler)                self.obj_Logger.info(' Logging to file enabled - Log file %s' % self.strLogFile )
                #self.obj_Logger = logging.getLogger(self.str_Logger_Name)
                #self.obj_Logger.addHandler(loggingHandler)
                self.obj_Internal_Logger.info('Logging enabled at level:' + str_Logger_Level + ' for FILE handler: ' + str_Logger_Name + ' enabled : ..%s' % self.strLogPath + '\\' + self.strLogFile)
                boolSuccess = True
            except (SystemExit, KeyboardInterrupt):
            
                raise
            
            except Exception, e:
             
                self.obj_Internal_Logger.error('Failed add logging handler: %s' % str_Logger_Name, exc_info=True)
            pass
        
        return boolSuccess    
    
#     def func_Start_Logging(self, str_Logging_Level=''):
#         
#         
#         boolSuccess = False
#         
#         self.func_Initialise_Logging_Levels(str_Logging_Level)
#         
#         return boolSuccess = True   
#     
#     def func_Initialise_Logging_Levels(self, str_Logging_Level):    
#         
#         try:
#             if str_Logging_Level == '':
#                 #set defualt level to INFO
#                 self.obj_Logger.setLevel(logging.INFO)
#             else:
#                 self.obj_Logger.setLevel(str_Logging_Level)
#             
#             self.obj_Logger.info(' Logging level set to %s' % self.obj_Logger )
#             boolSuccess = True
#         except (SystemExit, KeyboardInterrupt):
#         
#             raise
#         
#         except Exception, e:
#          
#             self.obj_Logger.error(' Failed to set logging level to %s' % self.str_Logging_Level , exc_info=True)
#         pass

         
               