#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import SharkSim modules
from FileHandler import FileHandler
from AnalysisHandler import AnalysisHandler
from SSAnalysisHandler import SSAnalysisHandler
from OutputHandler import OutputHandler
from object_SSSimulation import object_SSSimulation
from object_SSBatch import object_SSBatch
from object_SSReplicate import object_SSReplicate
from object_SSPopulation import object_SSPopulation
from object_SSVirtualSubPop import object_SSVirtualSubPop
from object_SSIndividual import object_SSIndividual
from object_SSDemographicNe import object_SSDemographicNe
from AutoVivificationHandler import AutoVivificationHandler
from globals_SharkSim import globalsSS
from object_SSRepProperty import object_SSPropertyHandler
from object_SSReportingObject import object_SSReportingObject
from object_SSReportingCustom_LDNE_1 import object_SSReportingCustom_LDNE_1
from handler_Logging import Logging
from collections import OrderedDict
##!!!!REQUIRED FOR PY2EXE !!!!!!!
import object_SSSimulation_V2
import object_SSBatch_V2
import object_SSReplicate_V2
import object_SSVirtualSubPop_V2
#import FileHandler
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
from simuPOP import *
import simuPOP as simupop
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
# DEBUG Imports
from logging import getLogger as logging__getLogger
from handler_Debug import Timer2
from sys import stdout as sys__stdout
from re import findall as re__findall
from re import compile as re__compile
from ntpath import basename as ntpath__basename
from datetime import datetime, timedelta
#from _ast import TryExcept
import re as regex
import pandas
import operator
import sys, os
# DEBUG Imports
#import objgraph
import pdb
from memory_profiler import profile

class SSOutputHandler:
    """Handle SSOutputOperation objects"""
    def __enter__(self):

        def __init__(self):
            
            pass
                
        class color:
            PURPLE = '\033[95m'
            CYAN = '\033[96m'
            DARKCYAN = '\033[36m'
            BLUE = '\033[94m'
            GREEN = '\033[92m'
            YELLOW = '\033[93m'
            RED = '\033[91m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
            END = '\033[0m' 
           
        class SSOutputOperation: 
            """Explicitly control all fundemental file operations"""

            str_Current_Col_Index = str(
                                         '0' +
                                         globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                         '0' +
                                         globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                         '0' +
                                         globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                         '0')

            def __init__(self):
                
#                 self.obj_Log_Default = logging__getLogger(__name__)
#                 self.obj_Log_Debug = logging__getLogger('app_debug')
#                 
#                 self.obj_Log_SL = logging__getLogger(globalsSS.Logger_LEVEL_Details.static_Logger_Name__SIM_LEVEL)

                ''' Get all the loggers required for monitoring this object '''
                self.method_Initialise_Monitor_Loggers()
                
                pass         


# ----- General routines

            def method_Initialise_Monitor_Loggers(self):
                
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
                #Retire once all classes are converted to new logger
                self.obj_Log_Debug_Display = self.obj_Log_Debug_Display
        
                ''' Get Debug Timer '''
                self.obj_Log_Debug_Timing = None
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    self.obj_Log_Debug_Timing = logging__getLogger(globalsSS.Logger_Debug_Timing.static_Logger_Name__Debug_Timing)
                pass
        
                ''' Get Debug AgeNe Logger '''
                self.obj_Log_Debug_AgeNe = None
                if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                    self.obj_Log_Debug_AgeNe = logging__getLogger(globalsSS.Logger_Debug_AgeNe.static_Logger_Name__Debug_AgeNe)
                pass
                                        
                return True
    
            def method_Pause_Console(self):
                
                raw_input('\n Pausing for output review - Press return to continue... \n')

            def AutomaticLociNamesList(self, nLoci):

                listLociNames = []

                for i in range(1, nLoci+1):
                    strLociName = listLociNames.append('Locus-' + str(i))
        
                return listLociNames

            def methodOutput_SimGeneralMessageWithoutHeaderAndFooter(self, listOutputDestinations, strMessage, boolNewline):
                '''
                Output general log message
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_SimGeneralMessageWithoutHeaderAndFooter(objOutput, strMessage, boolNewline)
                        
                    else:
                        #write output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            objOutput=outputFileHandle
                            self.methodFileOutput_SimGeneralMessageWithoutHeaderAndFooter(objOutput, strMessage, boolNewline)
                            
                            #Close the file
                            #boolSuccessful = objectFileHandler.fileClose(outputFileHandle, stringOutputDestination)
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)

            def methodConsoleOutput_SimGeneralMessageWithoutHeaderAndFooter(self, objOutput, strMessage, boolNewline):
                
                if boolNewline:
                    objOutput.write('\n')

                objOutput.write(strMessage)
                #objOutput.write('\n')
           
            def methodFileOutput_SimGeneralMessageWithoutHeaderAndFooter(self, objOutput, strMessage, boolNewline):
                
                if boolNewline:
                    objOutput.write('\n')
                    
                objOutput.write(strMessage)
                #objOutput.write('\n')

            def method_Output_Sim_General_Message_With_Time(self, listOutputDestinations, strMessage, boolIsHeader, boolReportDateTime=False, boolTimeSinceLastGeneralMessage=False):
                '''
                Output general log message
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.method_Output_Write_Sim_General_Message_With_Time(objOutput, strMessage, boolIsHeader, boolReportDateTime, boolTimeSinceLastGeneralMessage)
                        
                    else:
                        #write output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            objOutput=outputFileHandle
                            self.method_Output_Write_Sim_General_Message_With_Time(objOutput, strMessage, boolIsHeader, boolReportDateTime, boolTimeSinceLastGeneralMessage)
                                
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)


            def method_Output_Write_Sim_General_Message_With_Time(self, objOutput, strMessage, boolIsHeader, boolReportDateTime, boolTimeSinceLastGeneralMessage):
                
                strMessageSuffix1 = ''
                strMessageSuffix2 = ''
                
                if boolReportDateTime:
                    dateTimeNow = datetime.now()
                    strMessageSuffixDT = ' > DTN:' + dateTimeNow.strftime("%Y-%m-%d %H:%M:%S")
                    strMessageSuffix2 += strMessageSuffixDT
                
                if boolTimeSinceLastGeneralMessage:
                    
                    objGlobal_DateTimeVariables = globalsSS.DateTimeVariables()
                    dateTimeSinceLastGeneralMessage = objGlobal_DateTimeVariables.method_Get_Time_Since_Last_General_Message()

                    strMessageSuffixTSLM = ' > TSLM:' + str(dateTimeSinceLastGeneralMessage)
                    strMessageSuffix2 += strMessageSuffixTSLM
                    
                if boolIsHeader:
                    strMessageSuffix1 =  ' - BEGIN - '
                    if strMessage == '':
                        strMessageFinal = 'SharkSim GeneralMessage' + strMessageSuffix1 + strMessageSuffix2 
                    else:
                        strMessageFinal = strMessage + strMessageSuffix1 + strMessageSuffix2
                        
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine(strMessageFinal, 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    strMessageSuffix1 =  ' - END - '
                    if strMessage == '':
                        strMessageFinal = 'SharkSim GeneralMessage'  + strMessageSuffix1 + strMessageSuffix2
                    else:
                        strMessageFinal = strMessage  + strMessageSuffix1 + strMessageSuffix2 
                    
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine(strMessageFinal, 120)
                    objOutput.write(strMessageDelineationText)
            
                    
            def methodOutput_Output_Sampling_Locus_Combo_Info(self, listOutputDestinations, strPrefixMessage, boolHeader, boolFooter, listData):
                '''
                Output log message
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_Output_Sampling_Locus_Combo_Info(objOutput, strPrefixMessage, boolHeader, boolFooter, listData)
                        
                    else:
                        #write output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            objOutput=outputFileHandle
                            self.methodFileOutput_Output_Sampling_Locus_Combo_Info(objOutput, strPrefixMessage, boolHeader, boolFooter, listData)
                            
                            #Close the file
                            #boolSuccessful = objectFileHandler.fileClose(outputFileHandle, stringOutputDestination)
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                
                return boolSuccessful

            def methodConsoleOutput_Output_Sampling_Locus_Combo_Info(self, objOutput, strPrefixMessage, boolHeader, boolFooter, listData):

                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('Sampling Locus Combo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
#                 else:
#                     objOutput.write('\n')

                objOutput.write(strPrefixMessage)
                objOutput.write(str(listData))
                
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('Sampling Locus Combo - END ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                
                return True

            def methodFileOutput_Output_Sampling_Locus_Combo_Info(self, objOutput, strPrefixMessage, boolHeader, boolFooter, listData):

                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('Sampling Locus Combo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
#                 else:
#                     objOutput.write('\n')

                objOutput.write(strPrefixMessage)
                objOutput.write(str(listData))
                
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('Sampling Locus Combo - END ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                
                return True

            def methodOutput_Output_LDNE_Info(self, listOutputDestinations, strPrefixMessage, boolHeader, boolFooter, dictNeLD, listLDNePCritOutput):
                '''
                Output general log message
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_Output_LDNE_Info(objOutput, strPrefixMessage, boolHeader, boolFooter, dictNeLD, listLDNePCritOutput)
                        
                    else:
                        #write output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            objOutput=outputFileHandle
                            self.methodFileOutput_Output_LDNE_Info(objOutput, strPrefixMessage, boolHeader, boolFooter, dictNeLD, listLDNePCritOutput)
                            
                            #Close the file
                            #boolSuccessful = objectFileHandler.fileClose(outputFileHandle, stringOutputDestination)
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)

            def methodConsoleOutput_Output_LDNE_Info(self, objOutput, strPrefixMessage, boolHeader, boolFooter, dictNeLD, listLDNePCritOutput):

                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('LDNe Info - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
#                 else:
#                     objOutput.write('\n')

                dictRounded = OrderedDict()
                for listItem in listLDNePCritOutput:
                    listRounded = []
                    for i in range(0,3):
                        listRounded.append(round(dictNeLD[listItem][i],2))
                    pass
                    dictRounded[listItem] = listRounded

                objOutput.write(strPrefixMessage)
                objOutput.write('LDNe: ' + str(dictRounded))
                #objOutput.write('\n')
                
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('LDNe Info - END ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                
                return True

            def methodFileOutput_Output_LDNE_Info(self, objOutput, strPrefixMessage, boolHeader, boolFooter, dictNeLD, listLDNePCritOutput):

                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('LDNe Info - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
#                 else:
#                     objOutput.write('\n')

                dictRounded = OrderedDict()
                for listItem in listLDNePCritOutput:
                    listRounded = []
                    for i in range(0,3):
                        listRounded.append(round(dictNeLD[listItem][i],2))
                    pass
                    dictRounded[listItem] = listRounded

                objOutput.write(strPrefixMessage)
                objOutput.write('LDNe: ' + str(dictRounded))
                #objOutput.write('\n')
                
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('LDNe Info - END ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                
                return True

            def methodOutput_SimGeneralMessageHeader(self, listOutputDestinations, strMessage, boolReportDateTime=False, boolTimeSinceLastGeneralMessage=False):
                '''
                Output general log message
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_SimGeneralMessageHeader(objOutput, strMessage)
                        
                    else:
                        #write output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            objOutput=outputFileHandle
                            self.methodFileOutput_SimGeneralMessageHeader(objOutput, strMessage)
                            
                            #Close the file
                            #boolSuccessful = objectFileHandler.fileClose(outputFileHandle, stringOutputDestination)
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)


            def methodConsoleOutput_SimGeneralMessageHeader(self, objOutput, strMessage):
                
                strMessageSuffix =  '- BEGIN'
                if strMessage == '':
                    strMessageFinal = 'SharkSim GeneralMessage' + strMessageSuffix 
                else:
                    strMessageFinal = strMessage + strMessageSuffix
                    
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine(strMessageFinal, 120)
                objOutput.write(strMessageDelineationText)

            def methodFileOutput_SimGeneralMessageHeader(self, objOutput, strMessage):

                strMessageSuffix =  '- BEGIN'
                if strMessage == '':
                    strMessageFinal = 'SharkSim GeneralMessage' + strMessageSuffix 
                else:
                    strMessageFinal = strMessage + strMessageSuffix
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine(strMessageFinal, 120)
                objOutput.write(strMessageDelineationText)

            def methodOutput_SimGeneralMessageFooter(self, listOutputDestinations, strMessage):
                '''
                Output general log message
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_SimGeneralMessageFooter(objOutput, strMessage)
                        
                    else:
                        #write output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            objOutput=outputFileHandle
                            self.methodFileOutput_SimGeneralMessageFooter(objOutput, strMessage)
                            
                            #Close the file
                            #boolSuccessful = objectFileHandler.fileClose(outputFileHandle, stringOutputDestination)
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
            
            def methodConsoleOutput_SimGeneralMessageFooter(self, objOutput, strMessage):

                strMessageSuffix =  ' - END   '
                if strMessage == '':
                    strMessageFinal = 'SharkSim GeneralMessage' + strMessageSuffix 
                else:
                    strMessageFinal = strMessage + strMessageSuffix
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine(strMessageFinal, 120)
                objOutput.write(strMessageDelineationText)

            def methodFileOutput_SimGeneralMessageFooter(self, objOutput, strMessage):

                strMessageSuffix =  ' - END   '
                if strMessage == '':
                    strMessageFinal = 'SharkSim GeneralMessage' + strMessageSuffix 
                else:
                    strMessageFinal = strMessage + strMessageSuffix
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine(strMessageFinal, 120)
                objOutput.write(strMessageDelineationText)
                
            def methodOutput_SimGeneralMessage(self, boolHeader, boolFooter, listOutputDestinations, strMessage):
                '''
                Output general log message
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_SimGeneralMessage(objOutput, boolHeader, boolFooter, strMessage)
                        
                    else:
                        #write output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            objOutput=outputFileHandle
                            self.methodFileOutput_SimGeneralMessage(objOutput, boolHeader, boolFooter, strMessage)
                            
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)

            def methodConsoleOutput_SimGeneralMessage(self, objOutput, boolHeader, boolFooter, strMessage):
                
                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimGeneralMessage - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                
                objOutput.write(strMessage)
                
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimGeneralMessage - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                        
            def methodFileOutput_SimGeneralMessage(self, objOutput, boolHeader, boolFooter, strMessage):
                
                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimGeneralMessage - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                
                objOutput.write(strMessage)
                
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimGeneralMessage - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')

            def methodConstruct_MessageDelineationLine(self, strMessageHeadingText, intMessageDelineationTotalLength):
                
                #strMessageStart = '----------------------------------- '
                strMessageStart = '----------------- '
                strMessageHeadingMiddle = strMessageHeadingText
                
                intMessageStartPlusMiddleLength = len(strMessageStart + strMessageHeadingMiddle)
                intMessageEndLength = intMessageDelineationTotalLength - intMessageStartPlusMiddleLength

                strMessageHeadingEnd = ' '
                for intMessageLength in range(0, intMessageEndLength):
                    strMessageHeadingEnd = strMessageHeadingEnd + '-'    
                
                strMessageDelineationText = '\n' + strMessageStart + strMessageHeadingMiddle + strMessageHeadingEnd + '\n'
                
                return strMessageDelineationText
            
            def method_Construct__MessageDelineationLine(self, strMessageHeadingText, intMessageDelineationTotalLength):
                
                strMessageStart = '----------------- '
                strMessageHeadingMiddle = strMessageHeadingText
                
                intMessageStartPlusMiddleLength = len(strMessageStart + strMessageHeadingMiddle)
                intMessageEndLength = intMessageDelineationTotalLength - intMessageStartPlusMiddleLength

                strMessageHeadingEnd = ' '
                for intMessageLength in range(0, intMessageEndLength):
                    strMessageHeadingEnd = strMessageHeadingEnd + '-'    
                
                strMessageDelineationText = strMessageStart + strMessageHeadingMiddle + strMessageHeadingEnd
                
                return strMessageDelineationText


# ----- Summary and Debug information output

            '''
            AgeNe Final TOTALS output
            '''
            def methodOutput_Sim_AgeNe_Final_Total_Info_Reporting(self, objSharkSimOperation, pop, boolHeader, boolFooter, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes):
                '''
                Output simulation summary details
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_Sim_AgeNe_Final_Total_Info_Reporting(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes)
                        
                    else:
                        #write output to file
                        
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                objOutput=outputFileHandle
                                self.methodFileOutput_Sim_AgeNe_Final_Total_Info_Reporting(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes)
                                
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                objOutput=outputFileHandle
                                self.methodFileOutput_Sim_AgeNe_Final_Total_Info_Reporting(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes)
                                
                            
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)

            def methodConsoleOutput_Sim_AgeNe_Final_Total_Info_Reporting(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes):
                
                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeNeLifeTableTotalsInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')

                '''
                Output AgeNe details
                '''
                    
                '''
                For each Sex produce lists of Headers and Values
                Combine these and output them
                '''
                #Prime reporting objects with their properties from the raw data
                strSex = globalsSS.SexConstants.static_stringSexAll
                #TESTING_ON
                boolUseAgeNeSimParameters = objSharkSimOperation.objSSParametersLocal.boolUseAgeNeSimParameters
                if boolUseAgeNeSimParameters:
                    listOfAgeNeObjects = objSharkSimOperation.objSSParametersLocal.listOfAgeNeSimObjects
                else:
                    listOfAgeNeObjects = objSharkSimOperation.objSSParametersLocal.listOfAgeNeManualObjects

                objSSReporting = self.method_AgeNe_Final_Totals_Reporting(listOfAgeNeObjects, strSex)
                #TESTING_OFF

                listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)

                #Now header have been written...write the details
                listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                
                #Format and send output to console
                dictHeaderAndValues = self.methodFormat_AgeNeTotals_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                boolOutputHeader = True
                objOutput.write('Sex: ' + strSex + '\n')
                self.methodOutput_AgeNeDetail_HeaderAndValues(objOutput, dictHeaderAndValues, boolOutputHeader)
                objOutput.write('\n')
                pass
                    
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeNeLifeTableTotalsInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                    
            def methodFileOutput_Sim_AgeNe_Final_Total_Info_Reporting(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes):

                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeNeLifeTableTotalsInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')

                '''
                Output AgeNe details
                '''
                    
                '''
                For each Sex produce lists of Headers and Values
                Combine these and output them
                '''
                #Prime reporting objects with their properties from the raw data
                strSex = globalsSS.SexConstants.static_stringSexAll
                #TESTING_ON
                boolUseAgeNeSimParameters = objSharkSimOperation.objSSParametersLocal.boolUseAgeNeSimParameters
                if boolUseAgeNeSimParameters:
                    listOfAgeNeObjects = objSharkSimOperation.objSSParametersLocal.listOfAgeNeSimObjects
                else:
                    listOfAgeNeObjects = objSharkSimOperation.objSSParametersLocal.listOfAgeNeManualObjects

                objSSReporting = self.method_AgeNe_Final_Totals_Reporting(listOfAgeNeObjects, strSex)
                #TESTING_OFF

                listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)

                #Now header have been written...write the details
                listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                
                #Format and send output to console
                dictHeaderAndValues = self.methodFormat_AgeNeTotals_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                boolOutputHeader = True
                objOutput.write('Sex: ' + strSex + '\n')
                self.methodOutput_AgeNeDetail_HeaderAndValues(objOutput, dictHeaderAndValues, boolOutputHeader)
                objOutput.write('\n')
                pass
                    
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeNeLifeTableTotalsInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')

            def method_LogOutput_Sim_AgeNe_Final_Total_Info_Reporting(self, obj_Logging, obj_Results_Log, str_Heading_Prefix_1, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes, dict_Results):

                '''
                Output AgeNe details
                '''
                    
                '''
                For each Sex produce lists of Headers and Values
                Combine these and output them
                '''
                #Prime reporting objects with their properties from the raw data
                strSex = globalsSS.SexConstants.static_stringSexAll
                #TESTING_ON
                boolUseAgeNeSimParameters = objSharkSimOperation.objSSParametersLocal.boolUseAgeNeSimParameters
                if boolUseAgeNeSimParameters:
                    listOfAgeNeObjects = objSharkSimOperation.objSSParametersLocal.listOfAgeNeSimObjects
                else:
                    listOfAgeNeObjects = objSharkSimOperation.objSSParametersLocal.listOfAgeNeManualObjects

                objSSReporting = self.method_AgeNe_Final_Totals_Reporting(listOfAgeNeObjects, strSex)
                #TESTING_OFF

                listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)

                #Now header have been written...write the details
                listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                
                #Format and send output to console
                dictHeaderAndValues = self.methodFormat_AgeNeTotals_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                boolOutputHeader = True
                dict_MultiLine_Results = OrderedDict()
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = strSex
                int_MultiLine_Count = 0
                dict_MultiLine_Results = self.methodOutput_AgeNeDetail_HeaderAndValues_To_Multiline_Dict(dict_Results, dictHeaderAndValues, boolOutputHeader, dict_MultiLine_Results, int_MultiLine_Count)
                pass

                #Prime reporting objects with their properties from the raw data
                #TESTING_ON
                objSSReporting = self.method_AgeNe_DemographicTable_Totals_All_Sexes_Reporting(objSharkSimOperation.objSSParametersLocal, strSex)
                #TESTING_OFF

                listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)

                #Now header have been written...write the details
                listDetailValues = []
                listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                
                #Format and send output to console
                dictHeaderAndValues = self.methodFormat_AgeNeTotals_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                boolOutputHeader = True
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = strSex
                int_MultiLine_Count = 0 #This so these extra totals go onto the same line as the the other totals
                dict_MultiLine_Results = self.methodOutput_AgeNeDetail_HeaderAndValues_To_Multiline_Dict(dict_Results, dictHeaderAndValues, boolOutputHeader, dict_MultiLine_Results, int_MultiLine_Count)

                '''
                --------------------------
                Log the results
                --------------------------
                '''
                str_Results_1 = objSharkSimOperation.objSSParametersLocal.strUniqueRunID
                str_Heading_1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
                if boolHeader:
                    obj_Logging.func_Log_MultiLine_Results_Header(obj_Results_Log, str_Heading_1, str_Heading_Prefix_1, dict_MultiLine_Results)
                pass
                obj_Logging.func_Log_MultiLine_Results_Detail(str_Results_1, obj_Results_Log, dict_MultiLine_Results)
                    
                return True
            
            '''
            AgeNe life table TOTALS output
            '''
            def methodOutput_Sim_AgeNe_LifeTables_Total_Info_Reporting(self, objSharkSimOperation, pop, boolHeader, boolFooter, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes):
                '''
                Output simulation summary details
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_Sim_AgeNe_LifeTables_Total_Info_Reporting(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes)
                        
                    else:
                        #write output to file
                        
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                objOutput=outputFileHandle
                                self.methodFileOutput_Sim_AgeNe_LifeTables_Total_Info_Reporting(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes)
                                
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                objOutput=outputFileHandle
                                self.methodFileOutput_Sim_AgeNe_LifeTables_Total_Info_Reporting(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes)
                                
                            
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)

            def methodConsoleOutput_Sim_AgeNe_LifeTables_Total_Info_Reporting(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes):
                
                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeNeLifeTableTotalsInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')

                '''
                Output AgeNe details
                '''
                    
                listHeaderValues = []
                '''
                For each Sex produce lists of Headers and Values
                Combine these and output them
                '''
                for strSex in listSexes:
                    #Prime reporting objects with their properties from the raw data
                    #TESTING_ON
                    objSSReporting = self.method_AgeNe_LifeTable_Totals_Reporting(objSharkSimOperation.objSSParametersLocal, strSex)
                    #TESTING_OFF

                    listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)
    
                    #Now header have been written...write the details
                    listDetailValues = []
                    listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                    
                    #Format and send output to console
                    dictHeaderAndValues = self.methodFormat_AgeNeTotals_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                    boolOutputHeader = True
                    objOutput.write('Sex: ' + strSex + '\n')
                    self.methodOutput_AgeNeDetail_HeaderAndValues(objOutput, dictHeaderAndValues, boolOutputHeader)
                    objOutput.write('\n')
                    pass
                    
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeNeLifeTableTotalsInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                    
            def methodFileOutput_Sim_AgeNe_LifeTables_Total_Info_Reporting(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes):

                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeNeLifeTableTotalsInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')

                '''
                Output AgeNe details
                '''
                    
                listHeaderValues = []
                '''
                For each Sex produce lists of Headers and Values
                Combine these and output them
                '''
                for strSex in listSexes:
                    #Prime reporting objects with their properties from the raw data
                    #TESTING_ON
                    objSSReporting = self.method_AgeNe_LifeTable_Totals_Reporting(objSharkSimOperation.objSSParametersLocal, strSex)
                    #TESTING_OFF

                    listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)
    
                    #Now header have been written...write the details
                    listDetailValues = []
                    listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                    
                    #Format and send output to console
                    dictHeaderAndValues = self.methodFormat_AgeNeTotals_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                    boolOutputHeader = True
                    objOutput.write('Sex: ' + strSex + '\n')
                    self.methodOutput_AgeNeDetail_HeaderAndValues(objOutput, dictHeaderAndValues, boolOutputHeader)
                    objOutput.write('\n')
                    pass
                    
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeNeLifeTableTotalsInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')

            def method_LogOutput_Sim_AgeNe_LifeTables_Total_Info_Reporting(self, obj_Logging, obj_Results_Log, str_Heading_Prefix_1, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes, dict_Results):

                '''
                Output AgeNe details
                '''
                    
                listHeaderValues = []
                '''
                For each Sex produce lists of Headers and Values
                Combine these and output them
                '''
                dict_MultiLine_Results = OrderedDict()
                for strSex in listSexes:
                    #Prime reporting objects with their properties from the raw data
                    #TESTING_ON
                    objSSReporting = self.method_AgeNe_LifeTable_Totals_Reporting(objSharkSimOperation.objSSParametersLocal, strSex)
                    #TESTING_OFF

                    listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)
    
                    #Now header have been written...write the details
                    listDetailValues = []
                    listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                    
                    #Format and send output to console
                    dictHeaderAndValues = self.methodFormat_AgeNeTotals_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                    boolOutputHeader = True
                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = strSex
                    int_MultiLine_Count = len(dict_MultiLine_Results)
                    dict_MultiLine_Results = self.methodOutput_AgeNeDetail_HeaderAndValues_To_Multiline_Dict(dict_Results, dictHeaderAndValues, boolOutputHeader, dict_MultiLine_Results, int_MultiLine_Count)
                pass

                '''
                --------------------------
                Log the results
                --------------------------
                '''
                str_Results_1 = objSharkSimOperation.objSSParametersLocal.strUniqueRunID
                str_Heading_1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
                if boolHeader:
                    obj_Logging.func_Log_MultiLine_Results_Header(obj_Results_Log, str_Heading_1, str_Heading_Prefix_1, dict_MultiLine_Results)
                pass
                obj_Logging.func_Log_MultiLine_Results_Detail(str_Results_1, obj_Results_Log, dict_MultiLine_Results)
           
                return True
            '''
            AgeNe Demographic table TOTALS output
            '''
            def methodOutput_Sim_AgeNe_DemographicTables_Total_Info_Reporting(self, objSharkSimOperation, pop, boolHeader, boolFooter, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes):
                '''
                Output simulation summary details
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_Sim_AgeNe_DemographicTables_Total_Info_Reporting(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes)
                        
                    else:
                        #write output to file
                        
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                objOutput=outputFileHandle
                                self.methodFileOutput_Sim_AgeNe_DemographicTables_Total_Info_Reporting(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes)
                                
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                objOutput=outputFileHandle
                                self.methodFileOutput_Sim_AgeNe_DemographicTables_Total_Info_Reporting(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes)
                                
                            
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)

            def methodConsoleOutput_Sim_AgeNe_DemographicTables_Total_Info_Reporting(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes):
                
                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeNeDemographicTableTotalsInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')

                '''
                Output AgeNe details
                '''
                    
                listHeaderValues = []
                '''
                For each Sex produce lists of Headers and Values
                Combine these and output them
                '''
                #Add "All" sex to get those totals
                #objSharkSimOperation.objSSParametersLocal.listSexes.append(globalsSS.SexConstants.static_stringSexAll)
                
                for strSex in listSexes:
                    #Prime reporting objects with their properties from the raw data
                    #TESTING_ON
                    objSSReporting = self.method_AgeNe_DemographicTable_Totals_Reporting(objSharkSimOperation.objSSParametersLocal, strSex)
                    #TESTING_OFF

                    listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)
    
                    #Now header have been written...write the details
                    listDetailValues = []
                    listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                    
                    #Format and send output to console
                    dictHeaderAndValues = self.methodFormat_AgeNeTotals_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                    boolOutputHeader = True
                    objOutput.write('Sex: ' + strSex + '\n')
                    self.methodOutput_AgeNeDetail_HeaderAndValues(objOutput, dictHeaderAndValues, boolOutputHeader)
                    objOutput.write('\n')
                    pass
                
                #Also Report for All sexes
                strSex = globalsSS.SexConstants.static_stringSexAll

                #Prime reporting objects with their properties from the raw data
                #TESTING_ON
                objSSReporting = self.method_AgeNe_DemographicTable_Totals_All_Sexes_Reporting(objSharkSimOperation.objSSParametersLocal, strSex)
                #TESTING_OFF

                listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)

                #Now header have been written...write the details
                listDetailValues = []
                listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                
                #Format and send output to console
                dictHeaderAndValues = self.methodFormat_AgeNeTotals_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                boolOutputHeader = True
                objOutput.write('Sex: ' + strSex + '\n')
                self.methodOutput_AgeNeDetail_HeaderAndValues(objOutput, dictHeaderAndValues, boolOutputHeader)
                objOutput.write('\n')
                pass
                    
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeNeDemographicTableTotalsInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                    
            def methodFileOutput_Sim_AgeNe_DemographicTables_Total_Info_Reporting(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes):

                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeNeDemographicTableTotalsInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')

                '''
                Output AgeNe details
                '''
                    
                listHeaderValues = []
                '''
                For each Sex produce lists of Headers and Values
                Combine these and output them
                '''
                #Add "All" sex to get those totals
                #objSharkSimOperation.objSSParametersLocal.listSexes.append(globalsSS.SexConstants.static_stringSexAll)
                
                for strSex in listSexes:
                    #Prime reporting objects with their properties from the raw data
                    #TESTING_ON
                    objSSReporting = self.method_AgeNe_DemographicTable_Totals_Reporting(objSharkSimOperation.objSSParametersLocal, strSex)
                    #TESTING_OFF

                    listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)
    
                    #Now header have been written...write the details
                    listDetailValues = []
                    listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                    
                    #Format and send output to console
                    dictHeaderAndValues = self.methodFormat_AgeNeTotals_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                    boolOutputHeader = True
                    objOutput.write('Sex: ' + strSex + '\n')
                    self.methodOutput_AgeNeDetail_HeaderAndValues(objOutput, dictHeaderAndValues, boolOutputHeader)
                    objOutput.write('\n')
                    pass
                
                #Also Report for All sexes
                strSex = globalsSS.SexConstants.static_stringSexAll

                #Prime reporting objects with their properties from the raw data
                #TESTING_ON
                objSSReporting = self.method_AgeNe_DemographicTable_Totals_All_Sexes_Reporting(objSharkSimOperation.objSSParametersLocal, strSex)
                #TESTING_OFF

                listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)

                #Now header have been written...write the details
                listDetailValues = []
                listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                
                #Format and send output to console
                dictHeaderAndValues = self.methodFormat_AgeNeTotals_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                boolOutputHeader = True
                objOutput.write('Sex: ' + strSex + '\n')
                self.methodOutput_AgeNeDetail_HeaderAndValues(objOutput, dictHeaderAndValues, boolOutputHeader)
                objOutput.write('\n')
                pass
                    
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeNeDemographicTableTotalsInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
            
            def method_LogOutput_Sim_AgeNe_DemographicTables_Total_Info_Reporting(self, obj_Logging, obj_Results_Log, str_Heading_Prefix_1, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes, dict_Results):

                '''
                Output AgeNe details
                '''
                    
                listHeaderValues = []
                '''
                For each Sex produce lists of Headers and Values
                Combine these and output them
                '''
                #Add "All" sex to get those totals
                #objSharkSimOperation.objSSParametersLocal.listSexes.append(globalsSS.SexConstants.static_stringSexAll)
                dict_MultiLine_Results = OrderedDict()
                for strSex in listSexes:
                    #Prime reporting objects with their properties from the raw data
                    #TESTING_ON
                    objSSReporting = self.method_AgeNe_DemographicTable_Totals_Reporting(objSharkSimOperation.objSSParametersLocal, strSex)
                    #TESTING_OFF

                    listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)
    
                    #Now header have been written...write the details
                    listDetailValues = []
                    listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                    
                    #Format and send output to console
                    dictHeaderAndValues = self.methodFormat_AgeNeTotals_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                    boolOutputHeader = True
                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = strSex
                    int_MultiLine_Count = len(dict_MultiLine_Results)
                    dict_MultiLine_Results = self.methodOutput_AgeNeDetail_HeaderAndValues_To_Multiline_Dict(dict_Results, dictHeaderAndValues, boolOutputHeader, dict_MultiLine_Results, int_MultiLine_Count)
                pass

                '''
                --------------------------
                Log the results
                --------------------------
                '''
                str_Results_1 = objSharkSimOperation.objSSParametersLocal.strUniqueRunID
                str_Heading_1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
                if boolHeader:
                    obj_Logging.func_Log_MultiLine_Results_Header(obj_Results_Log, str_Heading_1, str_Heading_Prefix_1, dict_MultiLine_Results)
                pass
                obj_Logging.func_Log_MultiLine_Results_Detail(str_Results_1, obj_Results_Log, dict_MultiLine_Results)
                
                return True
            
            def method_LogOutput_Sim_AgeNe_DemographicTables_All_Sexes_Total_Info_Reporting(self, obj_Logging, obj_Results_Log, str_Heading_Prefix_1, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes, dict_Results):

                '''
                Output AgeNe details
                '''
                    
                listHeaderValues = []
                
                #Also Report for All sexes
                strSex = globalsSS.SexConstants.static_stringSexAll

                #Prime reporting objects with their properties from the raw data
                #TESTING_ON
                objSSReporting = self.method_AgeNe_DemographicTable_Totals_All_Sexes_Reporting(objSharkSimOperation.objSSParametersLocal, strSex)
                #TESTING_OFF

                listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)

                #Now header have been written...write the details
                listDetailValues = []
                listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                
                #Format and send output to console
                dictHeaderAndValues = self.methodFormat_AgeNeTotals_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                boolOutputHeader = True
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = strSex
                int_MultiLine_Count = 0 #This so these extra totals go onto the same line as the the other totals
                #dict_MultiLine_Results = self.methodOutput_AgeNeDetail_HeaderAndValues_To_Multiline_Dict(dict_Results, dictHeaderAndValues, boolOutputHeader, dict_MultiLine_Results, int_MultiLine_Count)
                dict_MultiLine_Results = None
                pass

                '''
                --------------------------
                Log the results
                --------------------------
                '''
                str_Results_1 = objSharkSimOperation.objSSParametersLocal.strUniqueRunID
                str_Heading_1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
                if boolHeader:
                    obj_Logging.func_Log_MultiLine_Results_Header(obj_Results_Log, str_Heading_1, str_Heading_Prefix_1, dict_MultiLine_Results)
                pass
                obj_Logging.func_Log_MultiLine_Results_Detail(str_Results_1, obj_Results_Log, dict_MultiLine_Results)
                    
                return True
            
            '''
            AgeNe sex-specific age-specific detail output
            '''
            def methodOutput_Sim_AgeNe_Detail_Info_Reporting(self, objSharkSimOperation, pop, boolHeader, boolFooter, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes):
                '''
                Output simulation summary details
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_Sim_AgeNe_Detail_Info_Reporting(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes)
                        
                    else:
                        #write output to file
                        
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                objOutput=outputFileHandle
                                self.methodFileOutput_Sim_AgeNe_Detail_Info_Reporting(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes)
                                
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                objOutput=outputFileHandle
                                self.methodFileOutput_Sim_AgeNe_Detail_Info_Reporting(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes)
                                
                            
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)

            def methodConsoleOutput_Sim_AgeNe_Detail_Info_Reporting(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes):
                
                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeNeProcessingSummaryInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')

                '''
                Output AgeNe details
                '''
 
                #TESTING_ON
                objSSReporting = self.method_AgeNeReporting_Age_Specific_Details(objSharkSimOperation.objSSParametersLocal)
                #TESTING_OFF
 
                '''
                Prime reporting objects with their properties from the raw data
                '''
                
                listHeaderValues = []
                
                dictObj_SSParams = AutoVivificationHandler()
                
                ''' 
                Write out keys and values to destination media
                '''
                        
                '''
                Prime objects with their properties from the raw data
                Data is being written for the first time so....
                Write the reporting objects keys as header labels
                '''
                for strSex in listSexes:
                    listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)
    
                    #Now header have been written...write the details
                    listDetailValues = []
                    listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                    
                    #Format and send output to console
                    if objSharkSimOperation.objSSParametersLocal.boolUseAgeNeSimParameters:
                        #intLines = objSharkSimOperation.objSSParametersLocal.maxAge + 1#+2
                        intLines = objSharkSimOperation.objSSParametersLocal.intAgeNe_Sim_Max_Age+1
                    else:  
                        #intLines = objSharkSimOperation.objSSParametersLocal.maxAge + 1 #+2
                        intLines = objSharkSimOperation.objSSParametersLocal.intAgeNe_Manual_Max_Age+1
                           
                    dictHeaderAndValues = self.methodFormat_AgeNeDetail_CombineHeaderAndValuesForOrderedDicts(listHeaderValues, listDetailValues, intLines, strSex)
                    boolOutputHeader = True
                    objOutput.write('Sex: ' + strSex + '\n')
                    self.methodOutput_AgeNeDetail_HeaderAndValues(objOutput, dictHeaderAndValues, boolOutputHeader)
                    objOutput.write('\n')
                    pass

                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimTemporalAgeNeSummaryInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                    
            def methodFileOutput_Sim_AgeNe_Detail_Info_Reporting(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes):
                
                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeNeProcessingSummaryInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')

                '''
                Output AgeNe details
                '''
 
                #TESTING_ON
                objSSReporting = self.method_AgeNeReporting_Age_Specific_Details(objSharkSimOperation.objSSParametersLocal)
                #TESTING_OFF
 
                '''
                Prime reporting objects with their properties from the raw data
                '''
                
                listHeaderValues = []
                
                dictObj_SSParams = AutoVivificationHandler()
                
                ''' 
                Write out keys and values to destination media
                '''
                        
                '''
                Prime objects with their properties from the raw data
                Data is being written for the first time so....
                Write the reporting objects keys as header labels
                '''
                for strSex in listSexes:
                    listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)
    
                    #Now header have been written...write the details
                    listDetailValues = []
                    listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                    
                    #Format and send output to console
                    if objSharkSimOperation.objSSParametersLocal.boolUseAgeNeSimParameters:
                        #intLines = objSharkSimOperation.objSSParametersLocal.maxAge+1 #+2
                        intLines = objSharkSimOperation.objSSParametersLocal.intAgeNe_Sim_Max_Age+1
                    else:  
                        #intLines = objSharkSimOperation.objSSParametersLocal.maxAge+1 #+2
                        intLines = objSharkSimOperation.objSSParametersLocal.intAgeNe_Manual_Max_Age+1
                           
                    dictHeaderAndValues = self.methodFormat_AgeNeDetail_CombineHeaderAndValuesForOrderedDicts(listHeaderValues, listDetailValues, intLines, strSex)
                    boolOutputHeader = True
                    objOutput.write('Sex: ' + strSex + '\n')
                    self.methodOutput_AgeNeDetail_HeaderAndValues(objOutput, dictHeaderAndValues, boolOutputHeader)
                    objOutput.write('\n')
                    pass

                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimTemporalAgeNeSummaryInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                    
            def method_LogOutput_Sim_AgeNe_Detail_Info_Reporting(self, obj_Logging, obj_Results_Log, str_Heading_Prefix_1, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn, objSSReporting, listSexes, dict_Results):
                
                '''
                Output AgeNe details
                '''
 
                #TESTING_ON
                objSSReporting = self.method_AgeNeReporting_Age_Specific_Details(objSharkSimOperation.objSSParametersLocal)
                #TESTING_OFF
 
                '''
                Prime reporting objects with their properties from the raw data
                '''
                
                listHeaderValues = []
                
                dictObj_SSParams = AutoVivificationHandler()
                
                ''' 
                Write out keys and values to destination media
                '''
                        
                '''
                Prime objects with their properties from the raw data
                Data is being written for the first time so....
                Write the reporting objects keys as header labels
                '''
                dict_MultiLine_Results = OrderedDict()
                for strSex in listSexes:
                    listHeaderValues = self.methodOutput_AgeNeDetail_Header_Reporting(objSSReporting)
    
                    #Now header have been written...write the details
                    listDetailValues = []
                    listDetailValues = self.methodOutput_AgeNeDetail_Value_Reporting(objSSReporting)
                    
                    #Format and send output to console
                    if objSharkSimOperation.objSSParametersLocal.boolUseAgeNeSimParameters:
                        #intLines = objSharkSimOperation.objSSParametersLocal.maxAge+1#+2
                        intLines = objSharkSimOperation.objSSParametersLocal.intAgeNe_Sim_Max_Age+1
                    else:  
                        #intLines = objSharkSimOperation.objSSParametersLocal.maxAge+1#+2
                        intLines = objSharkSimOperation.objSSParametersLocal.intAgeNe_Manual_Max_Age+1
                           
                    dictHeaderAndValues = self.methodFormat_AgeNeDetail_CombineHeaderAndValuesForOrderedDicts(listHeaderValues, listDetailValues, intLines, strSex)
                    boolOutputHeader = True
                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = strSex
                    int_MultiLine_Count = len(dict_MultiLine_Results)
                    dict_MultiLine_Results = self.methodOutput_AgeNeDetail_HeaderAndValues_To_Multiline_Dict(dict_Results, dictHeaderAndValues, boolOutputHeader, dict_MultiLine_Results, int_MultiLine_Count)
                pass
            
                '''
                --------------------------
                Log the results
                --------------------------
                '''
                str_Results_1 = objSharkSimOperation.objSSParametersLocal.strUniqueRunID
                str_Heading_1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
                if boolHeader:
                    obj_Logging.func_Log_MultiLine_Results_Header(obj_Results_Log, str_Heading_1, str_Heading_Prefix_1, dict_MultiLine_Results)
                pass
                obj_Logging.func_Log_MultiLine_Results_Detail(str_Results_1, obj_Results_Log, dict_MultiLine_Results)
           
                return True
            
            '''
            AgeNe output processing
            '''
            def method_AgeNeReporting_Age_Specific_Details(self, objSSParametersLocal):
                
                dictOfObjectsToReport = AutoVivificationHandler()
                
                if objSSParametersLocal.boolUseAgeNeSimParameters:
                    listOfAgeObjects = objSSParametersLocal.listOfAgeNeSimObjects
                else:
                    listOfAgeObjects = objSSParametersLocal.listOfAgeNeManualObjects
                    
                strObjectNameToReport = 'objAgeNeLifeTable'
                dictOfObjectsToReport[strObjectNameToReport] = listOfAgeObjects[0]
                strObjectNameToReport = 'objAgeNeDemographicTable'
                dictOfObjectsToReport[strObjectNameToReport] = listOfAgeObjects[1]
                
                oDictOfObjectPropertiesToReport = OrderedDict([])
                listReportingProperties = []
                
                listReportingProperties = [
                                            globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTable_listProperties_1[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTable_listProperties_2[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTable_listProperties_3[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTable_listProperties_4[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTable_listProperties_5[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTable_listProperties_6[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTable_listProperties_7[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTable_listProperties_8[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTable_listProperties_9[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTable_listProperties_10[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTable_listProperties_11[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTable_listProperties_12[0]
                                            ]
                oDictOfObjectPropertiesToReport[0] = {'objAgeNeLifeTable':listReportingProperties}
                
#                 listReportingProperties = [
#                                             globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_1[0]
#                                             ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_2[0]
#                                             ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_3[0]
#                                             ]                  
                listReportingProperties = [
                                            globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_1[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_2[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_3[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_4[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_5[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_6[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_7[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_8[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_9[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_10[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_11[0]
                                            #,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTable_listProperties_12[0]
                                            ]                  
                oDictOfObjectPropertiesToReport[1] = {'objAgeNeDemographicTable':listReportingProperties}
                
                objSSReporting = object_SSReportingObject()
                objSSReporting.method_Initialse(dictOfObjectsToReport, {}, oDictOfObjectPropertiesToReport)
                objSSReporting.method_GetListOfReportingPropertys_From_OrderedDict()                
                
                return objSSReporting   

            def method_AgeNe_Final_Totals_Reporting(self, listOfAgeNeObjects, strSex):
                
                dictOfObjectsToReport = AutoVivificationHandler()
                
#                 if boolUseAgeNeSimParameters:
#                     listOfAgeNeObjects = listOfAgeNeSimObjects
#                 else:
#                     listOfAgeNeObjects = objSSParametersLocal.listOfAgeNeManualObjects
                
                strObjectNameToReport = 'objAgeNe_CalculatedTotals'
                dictOfObjectsToReport[strObjectNameToReport] = listOfAgeNeObjects[2].Calculated_Totals
                
                oDictOfObjectPropertiesToReport = OrderedDict([])
                listReportingProperties = []
                listReportingProperties = [
                                            globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_1[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_2[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_3[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_4[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_5[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_6[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_7[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_8[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_9[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_10[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_11[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_12[0]
                                            ]
                oDictOfObjectPropertiesToReport[0] = {strObjectNameToReport:listReportingProperties}
                
                objSSReporting = object_SSReportingObject()
                objSSReporting.method_Initialse(dictOfObjectsToReport, {}, oDictOfObjectPropertiesToReport)
                objSSReporting.method_GetListOfReportingPropertysFromAProperty()                
                
                return objSSReporting   
            
            def method_AgeNe_Final_Totals_Reporting_RETIRED(self, boolUseAgeNeSimParameters, listOfAgeNeObjects, strSex):
                
                dictOfObjectsToReport = AutoVivificationHandler()
                
#                 if boolUseAgeNeSimParameters:
#                     listOfAgeNeObjects = listOfAgeNeSimObjects
#                 else:
#                     listOfAgeNeObjects = objSSParametersLocal.listOfAgeNeManualObjects
                
                strObjectNameToReport = 'objAgeNe_CalculatedTotals'
                dictOfObjectsToReport[strObjectNameToReport] = listOfAgeNeObjects[2].Calculated_Totals
                
                oDictOfObjectPropertiesToReport = OrderedDict([])
                listReportingProperties = []
                listReportingProperties = [
                                            globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_1[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_2[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_3[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_4[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_5[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_6[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_7[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_8[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_9[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_10[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_11[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNe_CalculatedTotals_listProperties_12[0]
                                            ]
                oDictOfObjectPropertiesToReport[0] = {strObjectNameToReport:listReportingProperties}
                
                objSSReporting = object_SSReportingObject()
                objSSReporting.method_Initialse(dictOfObjectsToReport, {}, oDictOfObjectPropertiesToReport)
                objSSReporting.method_GetListOfReportingPropertysFromAProperty()                
                
                return objSSReporting   

            def method_AgeNe_LifeTable_Totals_Reporting(self, objSSParametersLocal, strSex):
                
                dictOfObjectsToReport = AutoVivificationHandler()
                
                if objSSParametersLocal.boolUseAgeNeSimParameters:
                    listOfAgeObjects = objSSParametersLocal.listOfAgeNeSimObjects
                else:
                    listOfAgeObjects = objSSParametersLocal.listOfAgeNeManualObjects
                
                strObjectNameToReport = 'objAgeNeLifeTables_CalculatedTotals'
                dictOfObjectsToReport[strObjectNameToReport] = listOfAgeObjects[0].Calculated_Totals[strSex]
                
                oDictOfObjectPropertiesToReport = OrderedDict([])
                listReportingProperties = []
                listReportingProperties = [
                                            globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTables_CalculatedTotals_listProperties_1[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTables_CalculatedTotals_listProperties_2[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTables_CalculatedTotals_listProperties_3[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTables_CalculatedTotals_listProperties_4[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeLifeTables_CalculatedTotals_listProperties_5[0]
                                            ]
                oDictOfObjectPropertiesToReport[0] = {strObjectNameToReport:listReportingProperties}
                
                objSSReporting = object_SSReportingObject()
                objSSReporting.method_Initialse(dictOfObjectsToReport, {}, oDictOfObjectPropertiesToReport)
                objSSReporting.method_GetListOfReportingPropertysFromAProperty()                
                
                return objSSReporting   

            def method_AgeNe_DemographicTable_Totals_Reporting(self, objSSParametersLocal, strSex):
                
                dictOfObjectsToReport = AutoVivificationHandler()
                
                if objSSParametersLocal.boolUseAgeNeSimParameters:
                    listOfAgeObjects = objSSParametersLocal.listOfAgeNeSimObjects
                else:
                    listOfAgeObjects = objSSParametersLocal.listOfAgeNeManualObjects
                
                strObjectNameToReport = 'objAgeNeDemographicTables_CalculatedTotals'
                dictOfObjectsToReport[strObjectNameToReport] = listOfAgeObjects[1].Calculated_Totals[strSex]
                
                oDictOfObjectPropertiesToReport = OrderedDict([])
                listReportingProperties = []
                listReportingProperties = [
                                            globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTables_CalculatedTotals_listProperties_1[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTables_CalculatedTotals_listProperties_2[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTables_CalculatedTotals_listProperties_3[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTables_CalculatedTotals_listProperties_4[0]
                                            ]
                oDictOfObjectPropertiesToReport[0] = {strObjectNameToReport:listReportingProperties}
                
                objSSReporting = object_SSReportingObject()
                objSSReporting.method_Initialse(dictOfObjectsToReport, {}, oDictOfObjectPropertiesToReport)
                objSSReporting.method_GetListOfReportingPropertysFromAProperty()                
                
                return objSSReporting   

            def method_AgeNe_DemographicTable_Totals_All_Sexes_Reporting(self, objSSParametersLocal, strSex):
                
                dictOfObjectsToReport = AutoVivificationHandler()
                
                if objSSParametersLocal.boolUseAgeNeSimParameters:
                    listOfAgeObjects = objSSParametersLocal.listOfAgeNeSimObjects
                else:
                    listOfAgeObjects = objSSParametersLocal.listOfAgeNeManualObjects
                
                strObjectNameToReport = 'objAgeNeDemographicTables_CalculatedTotals_AllSexes'
                dictOfObjectsToReport[strObjectNameToReport] = listOfAgeObjects[1].Calculated_Totals[strSex]
                
                oDictOfObjectPropertiesToReport = OrderedDict([])
                listReportingProperties = []
                listReportingProperties = [
                                            globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTables_CalculatedTotals_AllSexes_listProperties_1[0]
                                            ,globalsSS.ObjectReportingPropertyLabels.static_AgeNeDemographicTables_CalculatedTotals_AllSexes_listProperties_1[0]
                                            ]
                oDictOfObjectPropertiesToReport[0] = {strObjectNameToReport:listReportingProperties}
                
                objSSReporting = object_SSReportingObject()
                objSSReporting.method_Initialse(dictOfObjectsToReport, {}, oDictOfObjectPropertiesToReport)
                objSSReporting.method_GetListOfReportingPropertysFromAProperty()                
                
                return objSSReporting   

            def methodOutput_AgeNeDetail_Header_Reporting(self, objSSReporting):

                listValues = []
                
                #with OutputHandler() as obj_OutputOperation:
                    #This only requires one pass to set up headings
                                        
                for objReportingProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                    
                    strSuppressOutput = objReportingProperty.Property_Value_Suppressed
                    if strSuppressOutput == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressedAndNotOutput:
                        #Dont write detail
                        pass
                    else:
                        strDefaultLabelKey = objReportingProperty.Property_Label_Default_Label_Key
                        strKey = getattr(objReportingProperty,strDefaultLabelKey)
                        listValues.append(strKey)
                    
                return listValues

            def methodOutput_AgeNeDetail_Value_Reporting(self, objSSReporting):

                listValues = []
                
               # with OutputHandler() as obj_OutputOperation:

                for objReportingProperty in objSSReporting.List_Of_Object_Properties_To_Output:

                    strSuppressOutput = objReportingProperty.Property_Value_Suppressed
                    if strSuppressOutput == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressedAndNotOutput:
                        #Dont write detail
                        pass
                    else:
                        value = objReportingProperty.Property_Value
                        listValues.append(value)
                    
                pass
                return listValues

            def methodFormat_AgeNeTotals_CombineHeaderAndValues(self, listHeaderValues, listDetailValues):
                
                intFloatRounding = 3
                dictHeaderAndValues = AutoVivificationHandler()
                
                intListLength = len(listHeaderValues)
                
                for intListItem in range(0, intListLength):
                    strHeader = listHeaderValues[intListItem]
                    value = listDetailValues[intListItem]
                    
                    #Determi which is larger
                    intHeaderSize = len(strHeader)
                    #intValueSize = len(strValue)
                    if isinstance(value, float):
                        strValue = str(round(value, intFloatRounding))
                    else:
                        strValue = str(value)
                        
                    intValueSize = len(str(value))
                        
                    if intHeaderSize >= intValueSize:
                        intLargestSize = intHeaderSize
                    else:
                        intLargestSize = intValueSize
                    
                    dictHeaderAndValues[intListItem]['header'] = strHeader
                    dictHeaderAndValues[intListItem]['display_header'] = True
                    dictHeaderAndValues[intListItem]['value'] = strValue
                    dictHeaderAndValues[intListItem]['largest_size'] = intLargestSize
                    dictHeaderAndValues[intListItem]['EOL'] = ''
                    
                dictHeaderAndValues[intListItem]['EOL'] = '\n'  
                return dictHeaderAndValues

            def methodFormat_AgeNeDetail_CombineHeaderAndValuesForOrderedDicts(self, listHeaderValues, listDetailValues, intOdictIndexMax, strSex):
                
                dictHeaderAndValues = OrderedDict()
                #dictHeaderAndValues = AutoVivificationHandler()
                
                intListLength = len(listHeaderValues)
                listNewHeaderValues = []
                listNewDetailValues = []
                for intListItem in range(0, intListLength):
                    valueOdict = listDetailValues[intListItem]
                    if isinstance(valueOdict, OrderedDict):
                        listNewHeaderValues.append(listHeaderValues[intListItem]) 
                        listNewDetailValues.append(listDetailValues[intListItem]) 
                    pass
                pass
                
                intDictHeaderAndValuesItemCount = 0
                intIndex = intDictHeaderAndValuesItemCount
                    
                for intOdictIndexCount in range(1, intOdictIndexMax):
                    
                    intListLength = len(listNewHeaderValues)
                    for intListItem in range(0, intListLength):
                        
                        strHeader = listNewHeaderValues[intListItem]
                        valueOdict = listNewDetailValues[intListItem][strSex]
                        
                        #Determine which is larger
                        intHeaderSize = len(strHeader)
                        
                        intLargestSize = 0
                        intFloatRounding = 3
                        #Go through the whole dict to look for the largest lenght value
                        for key, value in valueOdict.items():
                            if isinstance(value, float):
                                intValueSize = len(str(round(value, intFloatRounding)))
                            else:
                                intValueSize = len(str(value))
                            pass
                        
                            if intValueSize >= intLargestSize:
                                intLargestSize = intValueSize
                            pass
                        pass
                    
                        if intHeaderSize >= intLargestSize:
                            intLargestSize = intHeaderSize
                        pass
                        #Format the SELCTED value
                        valueOdictValue = valueOdict[intOdictIndexCount]
                        if isinstance(valueOdictValue, float):
                            strValue = str(round(valueOdictValue, intFloatRounding))
                        else:
                            strValue = str(valueOdictValue)
                        pass
                    
                        intIndex = intDictHeaderAndValuesItemCount    
                        dictHeaderAndValues[intIndex] = OrderedDict([('header',strHeader)])
                        if intDictHeaderAndValuesItemCount < intListLength:
                            dictHeaderAndValues[intIndex].update(OrderedDict([('display_header',True)]))
                        else:
                            dictHeaderAndValues[intIndex].update(OrderedDict([('display_header',False)]))
                        pass
                        dictHeaderAndValues[intIndex].update(OrderedDict([('value',strValue)]))
                        dictHeaderAndValues[intIndex].update(OrderedDict([('largest_size',intLargestSize)]))
                        if (intListItem == intListLength-1):
                            dictHeaderAndValues[intIndex].update(OrderedDict([('EOL','\n')]))
                        else:
                            dictHeaderAndValues[intIndex].update(OrderedDict([('EOL','')]))
                        pass
                    
                        intDictHeaderAndValuesItemCount += 1
                    pass
                #Write EOL when sex changes
                dictHeaderAndValues[intIndex].update(OrderedDict([('EOL',dictHeaderAndValues[intIndex]['EOL'] + '\n')]))
                pass
              
                return dictHeaderAndValues

            def methodFormat_AgeNeDetail_CombineHeaderAndValuesForOrderedDicts_OLD(self, listHeaderValues, listDetailValues, intOdictIndexMax, strSex):
                
                dictHeaderAndValues = OrderedDict()
                #dictHeaderAndValues = AutoVivificationHandler()
                
                intListLength = len(listHeaderValues)
                listNewHeaderValues = []
                listNewDetailValues = []
                for intListItem in range(0, intListLength):
                    valueOdict = listDetailValues[intListItem]
                    if isinstance(valueOdict, OrderedDict):
                        listNewHeaderValues.append(listHeaderValues[intListItem]) 
                        listNewDetailValues.append(listDetailValues[intListItem]) 
                        
                #listSexes = [globalsSS.SexConstants.static_stringSexMale, globalsSS.SexConstants.static_stringSexFemale]        
                
                intDictHeaderAndValuesItemCount = 0
                intIndex = intDictHeaderAndValuesItemCount
                #for strSex in listSexes:
                    
                for intOdictIndexCount in range(1, intOdictIndexMax):
                    
                    intListLength = len(listNewHeaderValues)
                    for intListItem in range(0, intListLength):
                        
                        strHeader = listNewHeaderValues[intListItem]
                        valueOdict = listNewDetailValues[intListItem][strSex]
                        
                        #Determine which is larger
                        intHeaderSize = len(strHeader)
                        
                        intLargestSize = 0
                        intFloatRounding = 3
                        #Go through the whole dict to look for the largest lenght value
                        for key, value in valueOdict.items():
                            if isinstance(value, float):
                                intValueSize = len(str(round(value, intFloatRounding)))
                            else:
                                intValueSize = len(str(value))
                        
                            if intValueSize >= intLargestSize:
                                intLargestSize = intValueSize
                        pass
                        if intHeaderSize >= intLargestSize:
                            intLargestSize = intHeaderSize
                        
                        #Format the SELCTED value
                        valueOdictValue = valueOdict[intOdictIndexCount]
                        if isinstance(valueOdictValue, float):
                            strValue = str(round(valueOdictValue, intFloatRounding))
                        else:
                            strValue = str(valueOdictValue)
                            
                        #Add header and values to reporting dict
                        intIndex = intDictHeaderAndValuesItemCount    
                        dictHeaderAndValues[intIndex]['header'] = strHeader
                        if intDictHeaderAndValuesItemCount < intListLength:
                            dictHeaderAndValues[intIndex]['display_header'] = True
                        else:
                            dictHeaderAndValues[intIndex]['display_header'] = False
                        dictHeaderAndValues[intIndex]['value'] = strValue
                        dictHeaderAndValues[intIndex]['largest_size'] = intLargestSize
                        if (intListItem == intListLength-1):
                            dictHeaderAndValues[intIndex]['EOL'] = '\n'
                        else:
                            dictHeaderAndValues[intIndex]['EOL'] = ''
                        
                        intDictHeaderAndValuesItemCount += 1
                        pass
                    pass
                #Write EOL when sex changes
                dictHeaderAndValues[intIndex]['EOL'] = dictHeaderAndValues[intIndex]['EOL'] + '\n'
                pass
              
                return dictHeaderAndValues

            def methodOutput_AgeNeDetail_HeaderAndValues(self, objOutput, dictHeaderAndValues, boolOutputHeader):
                
                stringPadChar = ' '
                stringPadString = ' '
                intJustifyOdd = 3
                intJustifyEven = 4
                #Get the Max Reporting Order Key
                intLastOutputOrderKey = int(max(dictHeaderAndValues.iterkeys(), key=int))
                
                if boolOutputHeader:
                    #Output the header values
                    for intOutputOrderKey in range(0, intLastOutputOrderKey+1):
                        
                        strHeader = dictHeaderAndValues[intOutputOrderKey]['header']
                        boolDisplayHeader = dictHeaderAndValues[intOutputOrderKey]['display_header']
                        intLargestSize = dictHeaderAndValues[intOutputOrderKey]['largest_size']
                        strEOL = dictHeaderAndValues[intOutputOrderKey]['EOL']
                        
                        #Is even or odd
                        intOdd = intLargestSize & 0x1
                        if intOdd == 1:
                            intLargestSize += intJustifyOdd
                        else:
                            intLargestSize += intJustifyEven
                                
    #                     if len(strHeader) == intLargestSize:
    #                         intCalculatedJustify = intLargestSize + intJustify
    #                     else:
    #                         intCalculatedJustify = ((intLargestSize - len(strHeader))/2) + intJustify
                        
                        stringFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                        
                        if boolDisplayHeader:
                            objOutput.write(stringFormat.format(strHeader) + stringPadString + strEOL)
                        
                    #objOutput.write('\n')
                
                #Now outoput the detail values    
                for intOutputOrderKey in range(0, intLastOutputOrderKey+1):
                    
                    strValue = dictHeaderAndValues[intOutputOrderKey]['value']
                    intLargestSize = dictHeaderAndValues[intOutputOrderKey]['largest_size']
                    strEOL = dictHeaderAndValues[intOutputOrderKey]['EOL']
                    
                    #Is even or odd
                    intOdd = intLargestSize & 0x1
                    if intOdd == 1:
                        intLargestSize += intJustifyOdd
                    else:
                        intLargestSize += intJustifyEven
                    
#                     if len(strValue) == intLargestSize:
#                         intCalculatedJustify = intJustify
#                     else:
#                         intCalculatedJustify = ((intLargestSize - len(strValue))/2) + intJustify
                    
                    if strValue.isdigit():
                        stringFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                    else:
                        stringFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                
                    objOutput.write(stringFormat.format(strValue) + stringPadString  + strEOL)
                
                #objOutput.write('\n')
                pass

            def methodOutput_AgeNeDetail_HeaderAndValues_To_Multiline_Dict(self, dict_Results, dictHeaderAndValues, boolOutputHeader, dict_Multiline_Results, int_MultiLine_Count):
                
                stringPadChar = ' '
                stringPadString = ' '
                intJustifyOdd = 3
                intJustifyEven = 4
                #Get the Max Reporting Order Key
                intLastOutputOrderKey = int(max(dictHeaderAndValues.iterkeys(), key=int))
                
                int_Line_Count = int_MultiLine_Count
#                 int_Line_Count = 0
#                 int_MultiLine_Count = len(dict_Multiline_Results)
#                 if int_MultiLine_Count > 0:
#                     int_Line_Count = int_MultiLine_Count
#                 pass

            
                for intOutputOrderKey in range(0, intLastOutputOrderKey+1):
                    
                    strHeader = dictHeaderAndValues[intOutputOrderKey]['header']
                    strValue = dictHeaderAndValues[intOutputOrderKey]['value']
                    intLargestSize = dictHeaderAndValues[intOutputOrderKey]['largest_size']
                    strEOL = dictHeaderAndValues[intOutputOrderKey]['EOL']
                    
                    #Is even or odd
                    intOdd = intLargestSize & 0x1
                    if intOdd == 1:
                        intLargestSize += intJustifyOdd
                    else:
                        intLargestSize += intJustifyEven
                    
#                     if len(strValue) == intLargestSize:
#                         intCalculatedJustify = intJustify
#                     else:
#                         intCalculatedJustify = ((intLargestSize - len(strValue))/2) + intJustify
                    
                    if strValue.isdigit():
                        stringFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                    else:
                        stringFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                    pass
                    #objOutput.write(stringFormat.format(strValue) + stringPadString  + strEOL)

                    if int_Line_Count not in dict_Multiline_Results:
                        bool_New_Line = True
                        for key, value in dict_Results.items():
                            if bool_New_Line:
                                dict_Multiline_Results[int_Line_Count] = OrderedDict([(key,value)])
                                bool_New_Line = False
                            else:
                                dict_Multiline_Results[int_Line_Count].update(OrderedDict([(key,value)]))
                            pass
                        pass
                    pass
                    dict_Multiline_Results[int_Line_Count].update(OrderedDict([(strHeader,stringFormat.format(strValue))]))
                    
                    if strEOL:
                        int_Line_Count += 1
                    pass
                #objOutput.write('\n')
                pass
          
                return dict_Multiline_Results
            '''
            Temporal output
            '''
            def methodOutput_SimTemporalProcessingSummaryInfo(self, objSharkSimOperation, pop, boolHeader, boolFooter, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, boolBurnIn):
                '''
                Output simulation summary details
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_SimTemporalProcessingSummaryInfo(objOutput, boolHeader, boolFooter, listOutputDestinations, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn)
                        
                    else:
                        #write output to file
                        
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                objOutput=outputFileHandle
                                self.methodFileOutput_SimTemporalProcessingSummaryInfo(objOutput, boolHeader, boolFooter, listOutputDestinations, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn)
                                
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                objOutput=outputFileHandle
                                self.methodFileOutput_SimTemporalProcessingSummaryInfo(objOutput, boolHeader, boolFooter, listOutputDestinations, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn)
                                
                            
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)

            def methodConsoleOutput_SimTemporalProcessingSummaryInfo(self, objOutput, boolHeader, boolFooter, listOutputDestinations, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn):
                
                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimTemporalProcessingSummaryInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                    
                intLeftJustify = 38
                stringPadChar = '-'
                stringPadString = '> '
                stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
                objOutput.write('\n')
                objOutput.write(stringLeftJustifyFormat.format('Replicate:') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intCurrentReplicate))
                objOutput.write('\n')
                objOutput.write(stringLeftJustifyFormat.format('Population Size: ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.popnSize))
                objOutput.write('\n')
                
                if boolBurnIn:
                    objOutput.write(color.BOLD + color.GREEN + stringLeftJustifyFormat.format('Burn-in length (months): ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intReplicateBurnInLengthInMonths) + color.END)
                    objOutput.write('\n')
                    objOutput.write(color.BOLD + color.YELLOW + stringLeftJustifyFormat.format('Burn-in current month  : ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intSimulationCurrentMonth) + color.END)
                    objOutput.write('\n')
                    
                objOutput.write(stringLeftJustifyFormat.format('Simulation potential fertilisations: ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intOffspringPotentialFertilisationsToSimulate))
                objOutput.write('\n')
                objOutput.write(stringLeftJustifyFormat.format('Simulation current fertilisation: ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intCurrentTemporalFertilisation))
                objOutput.write('\n')
                objOutput.write(stringLeftJustifyFormat.format('Reproductive cycle month: ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intYearReproductiveCycleCurrentMonth))
                objOutput.write('\n')
                objOutput.write(stringLeftJustifyFormat.format('Simulation Month: ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intSimulationCurrentMonth))
                objOutput.write('\n')
                objOutput.write(color.BOLD + color.GREEN + stringLeftJustifyFormat.format('Simulation Length (years, months): ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intTotalYearsToSimulate) + ', ' + str(objSharkSimOperation.objSSParametersLocal.intTotalMonthsToSimulate) + color.END)
                objOutput.write('\n\n')
                objOutput.write(color.BOLD + color.YELLOW + stringLeftJustifyFormat.format('Year: ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intSimulationCurrentMonth//12) + color.END)
                objOutput.write('\n')
                objOutput.write(color.BOLD + color.YELLOW + stringLeftJustifyFormat.format('Year Month: ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intYearCurrentMonth) + color.END)
                objOutput.write('\n\n')
                objOutput.write(stringLeftJustifyFormat.format('Event Message:') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.stringEventMessage))
                objOutput.write('\n')
                
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimTemporalProcessingSummaryInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                    
            def methodFileOutput_SimTemporalProcessingSummaryInfo(self, objOutput, boolHeader, boolFooter, listOutputDestinations, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation, boolBurnIn):

                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimTemporalProcessingSummaryInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                    
                intLeftJustify = 38
                stringPadChar = '-'
                stringPadString = '> '
                stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
                objOutput.write('\n')
                objOutput.write(stringLeftJustifyFormat.format('Replicate:') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intCurrentReplicate))
                objOutput.write('\n')
                objOutput.write(stringLeftJustifyFormat.format('Population Size: ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.popnSize))
                objOutput.write('\n')
                
                if boolBurnIn:
                    objOutput.write(stringLeftJustifyFormat.format('Burn-in length (months): ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intReplicateBurnInLengthInMonths))
                    objOutput.write('\n')
                    objOutput.write(stringLeftJustifyFormat.format('Burn-in current month  : ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intSimulationCurrentMonth))
                    objOutput.write('\n')
                    
                objOutput.write(stringLeftJustifyFormat.format('Simulation potential fertilisations: ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intOffspringPotentialFertilisationsToSimulate))
                objOutput.write('\n')
                objOutput.write(stringLeftJustifyFormat.format('Simulation current fertilisation: ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intCurrentTemporalFertilisation))
                objOutput.write('\n')
                objOutput.write(stringLeftJustifyFormat.format('Reproductive cycle month: ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intYearReproductiveCycleCurrentMonth))
                objOutput.write('\n')
                objOutput.write(stringLeftJustifyFormat.format('Simulation Month: ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intSimulationCurrentMonth))
                objOutput.write('\n')
                objOutput.write(stringLeftJustifyFormat.format('Simulation Length (years, months): ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intTotalYearsToSimulate) + ', ' + str(objSharkSimOperation.objSSParametersLocal.intTotalMonthsToSimulate))
                objOutput.write('\n\n')
                objOutput.write(stringLeftJustifyFormat.format('Year: ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intSimulationCurrentMonth//12))
                objOutput.write('\n')
                objOutput.write(stringLeftJustifyFormat.format('Year Month: ') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.intYearCurrentMonth))
                objOutput.write('\n\n')
                objOutput.write(stringLeftJustifyFormat.format('Event Message:') + stringPadString + str(objSharkSimOperation.objSSParametersLocal.stringEventMessage))
                objOutput.write('\n')
                
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimTemporalProcessingSummaryInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                    
            def methodOutput_SimLifeStageSummaryInfo(self, objSharkSimOperation, pop, boolHeader, boolFooter,listOutputDestinations, intSubPop, intCurrentTemporalFertilisation):
                '''
                Output simulation summary details
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_SimLifeStageSummaryInfo(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation)
                        
                    else:
                        #write output to file
                        
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                objOutput=outputFileHandle
                                self.methodFileOutput_SimLifeStageSummaryInfo(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation)
                                
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                objOutput=outputFileHandle
                                self.methodFileOutput_SimLifeStageSummaryInfo(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation)
                                
                            
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)

            def methodConsoleOutput_SimLifeStageSummaryInfo_OLD(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation):
                
                intNumberVirtualSubPops = pop.numVirtualSubPop()
                
                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimLifeStageSummaryInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                
                stringVSPPopSizeTotals=''
                stringVSPHeadings=''
                stringIndividual1AgeForVSP=''
                for intVirtualSubPop in range(intSubPop, intNumberVirtualSubPops):
                    stringHeading = pop.subPopName([intSubPop, intVirtualSubPop]).ljust(10)
                    intHeadingLength = len(stringHeading)
                    intHeadingPadding = 3
                    stringVSPHeadings = stringVSPHeadings + stringHeading.ljust(intHeadingLength + intHeadingPadding)
                    stringVSPPopSize = str(pop.subPopSize([intSubPop, intVirtualSubPop]))
                    if int(stringVSPPopSize) > 0:
                        stringVSPPopSizeTotals = stringVSPPopSizeTotals + color.BOLD + color.CYAN + stringVSPPopSize.ljust(intHeadingLength + intHeadingPadding) + color.END
                    else:
                        stringVSPPopSizeTotals = stringVSPPopSizeTotals + stringVSPPopSize.ljust(intHeadingLength + intHeadingPadding)
                    if stringVSPPopSize == '0':
                        stringIndividual1AgeForVSP = stringIndividual1AgeForVSP + 'NA'.ljust(intHeadingLength + intHeadingPadding)
                    else:
                        for individual in pop.individuals([intSubPop, intVirtualSubPop]):
                            intIndividualAge = int(individual.age_in_months)
                            if intIndividualAge > 0:
                                stringIndividual1AgeForVSP = stringIndividual1AgeForVSP + color.BOLD + color.CYAN + str(intIndividualAge).ljust(intHeadingLength + intHeadingPadding) + color.END
                            else:
                                stringIndividual1AgeForVSP = stringIndividual1AgeForVSP + str(intIndividualAge).ljust(intHeadingLength + intHeadingPadding)
                            break
                        
                objOutput.write('Life stage:'.ljust(30) + stringVSPHeadings)
                objOutput.write('\n')
                objOutput.write('Size of life stages:'.ljust(30) + stringVSPPopSizeTotals)
                objOutput.write('\n')
                objOutput.write('Age of life stages:'.ljust(30) + stringIndividual1AgeForVSP)
                objOutput.write('\n')
                
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimLifeStageSummaryInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                    
            def methodConsoleOutput_SimLifeStageSummaryInfo(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation):
                
                intNumberVirtualSubPops = pop.numVirtualSubPop()
                
                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimLifeStageSummaryInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                
                stringVSPPopSizeTotals=''
                stringVSPHeadings=''
                stringIndividual1AgeForVSP=''
                strMin_Mean_Max_String = ''
                for intVirtualSubPop in range(intSubPop, intNumberVirtualSubPops):
                    stringHeading = pop.subPopName([intSubPop, intVirtualSubPop]).ljust(10)
                    intHeadingLength = len(stringHeading)
                    intHeadingPadding = 3
                    stringVSPHeadings = stringVSPHeadings + stringHeading.ljust(intHeadingLength + intHeadingPadding)
                    stringVSPPopSize = str(pop.subPopSize([intSubPop, intVirtualSubPop]))

                    strSS_InfoField = 'age_in_months'
                    if int(stringVSPPopSize) > 0:
                        strMin_Mean_Max = self.method_Display_String_Min_Mean_Max(pop, intSubPop, intVirtualSubPop, strSS_InfoField)
                    else:
                        strMin_Mean_Max = ''
                        
                    strMin_Mean_Max_String += strMin_Mean_Max.ljust(intHeadingLength + intHeadingPadding)
                    
                    if int(stringVSPPopSize) > 0:
                        stringVSPPopSizeTotals = stringVSPPopSizeTotals + color.BOLD + color.CYAN + stringVSPPopSize.ljust(intHeadingLength + intHeadingPadding) + color.END

                    else:
                        stringVSPPopSizeTotals = stringVSPPopSizeTotals + stringVSPPopSize.ljust(intHeadingLength + intHeadingPadding)
                    if stringVSPPopSize == '0':
                        stringIndividual1AgeForVSP = stringIndividual1AgeForVSP + 'NA'.ljust(intHeadingLength + intHeadingPadding)
                    else:
                        for individual in pop.individuals([intSubPop, intVirtualSubPop]):
                            intIndividualAge = int(individual.age_in_months)
                            if intIndividualAge > 0:
                                stringIndividual1AgeForVSP = stringIndividual1AgeForVSP + color.BOLD + color.CYAN + str(intIndividualAge).ljust(intHeadingLength + intHeadingPadding) + color.END
                            else:
                                stringIndividual1AgeForVSP = stringIndividual1AgeForVSP + str(intIndividualAge).ljust(intHeadingLength + intHeadingPadding)
                            break
                
                
                objOutput.write('Life stage:'.ljust(30) + stringVSPHeadings)
                objOutput.write('\n')
                objOutput.write('Size:'.ljust(30) + stringVSPPopSizeTotals)
                objOutput.write('\n')
                objOutput.write('Ages (Min-Mean-Max):'.ljust(30) + strMin_Mean_Max_String)
                objOutput.write('\n')
                
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimLifeStageSummaryInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')

            def method_Display_String_Min_Mean_Max(self, pop, intSubPop, intVirtualSubPop, strSS_InfoField):

                strMin_Mean_Max = ''
                
                dictMin = pop.dvars([intSubPop, intVirtualSubPop]).minOfInfo
                if dictMin[strSS_InfoField] == None:
                    #strMin = globalsSS.StringUnexpectedResults.static_stringNotApplicable
                    strMin = ''
                else:
                    strMin = str(int(dictMin[strSS_InfoField]))
                    
                dictMean = pop.dvars([intSubPop, intVirtualSubPop]).meanOfInfo
                if dictMean[strSS_InfoField] == None:
                    #strMean = globalsSS.StringUnexpectedResults.static_stringNotApplicable
                    strMean = ''
                else:
                    strMean = str(int(dictMean[strSS_InfoField]))
                    
                dictMax = pop.dvars([intSubPop, intVirtualSubPop]).maxOfInfo
                if dictMax[strSS_InfoField] == None:
                    #strMax = globalsSS.StringUnexpectedResults.static_stringNotApplicable
                    strMax = ''
                else:
                    strMax = str(int(dictMax[strSS_InfoField]))
                
                strMin_Mean_Max = strMin + '-' + strMean + '-' + strMax
                    
                return strMin_Mean_Max
                                
            def methodFileOutput_SimLifeStageSummaryInfo(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation):
                
                intNumberVirtualSubPops = pop.numVirtualSubPop()
                
                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimLifeStageSummaryInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                
                stringVSPPopSizeTotals=''
                stringVSPHeadings=''
                stringIndividual1AgeForVSP=''
                strMin_Mean_Max_String = ''
                for intVirtualSubPop in range(intSubPop, intNumberVirtualSubPops):
                    stringHeading = pop.subPopName([intSubPop, intVirtualSubPop]).ljust(10)
                    intHeadingLength = len(stringHeading)
                    intHeadingPadding = 3
                    stringVSPHeadings = stringVSPHeadings + stringHeading.ljust(intHeadingLength + intHeadingPadding)
                    stringVSPPopSize = str(pop.subPopSize([intSubPop, intVirtualSubPop]))

                    strSS_InfoField = 'age_in_months'
                    if int(stringVSPPopSize) > 0:
                        strMin_Mean_Max = self.method_Display_String_Min_Mean_Max(pop, intSubPop, intVirtualSubPop, strSS_InfoField)
                    else:
                        strMin_Mean_Max = ''
                        
                    strMin_Mean_Max_String += strMin_Mean_Max.ljust(intHeadingLength + intHeadingPadding)
                    
                    if int(stringVSPPopSize) > 0:
                        stringVSPPopSizeTotals = stringVSPPopSizeTotals + stringVSPPopSize.ljust(intHeadingLength + intHeadingPadding)

                    else:
                        stringVSPPopSizeTotals = stringVSPPopSizeTotals + stringVSPPopSize.ljust(intHeadingLength + intHeadingPadding)
                    if stringVSPPopSize == '0':
                        stringIndividual1AgeForVSP = stringIndividual1AgeForVSP + 'NA'.ljust(intHeadingLength + intHeadingPadding)
                    else:
                        for individual in pop.individuals([intSubPop, intVirtualSubPop]):
                            intIndividualAge = int(individual.age_in_months)
                            if intIndividualAge > 0:
                                stringIndividual1AgeForVSP = stringIndividual1AgeForVSP + str(intIndividualAge).ljust(intHeadingLength + intHeadingPadding)
                            else:
                                stringIndividual1AgeForVSP = stringIndividual1AgeForVSP + str(intIndividualAge).ljust(intHeadingLength + intHeadingPadding)
                            break
                
                
                objOutput.write('Life stage:'.ljust(30) + stringVSPHeadings)
                objOutput.write('\n')
                objOutput.write('Size:'.ljust(30) + stringVSPPopSizeTotals)
                objOutput.write('\n')
                objOutput.write('Ages (Min-Mean-Max):'.ljust(30) + strMin_Mean_Max_String)
                objOutput.write('\n')
                
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimLifeStageSummaryInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
      
            def methodOutput_SimAgeClassSummaryInfo(self, objSharkSimOperation, pop, boolHeader, boolFooter, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation):
                '''
                Output simulation summary details
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_SimAgeClassSummaryInfo(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation)
                        
                    else:
                        #write output to file
                        
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                objOutput=outputFileHandle
                                self.methodFileOutput_SimAgeClassSummaryInfo(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation)
                                
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                objOutput=outputFileHandle
                                self.methodFileOutput_SimAgeClassSummaryInfo(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation)
                                
                            
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)

            def methodConsoleOutput_SimAgeClassSummaryInfo(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation):
                
                intNumberVirtualSubPops = pop.numVirtualSubPop()
                
                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeClassSummaryInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                    
                stringVSPPopSizeTotals=''
                stringVSPHeadings=''
                stringIndividual1AgeForVSP=''
                strMin_Mean_Max_String = ''
                for intVirtualSubPop in range(intSubPop, intNumberVirtualSubPops):
                    stringHeading = pop.subPopName([intSubPop, intVirtualSubPop]).ljust(10)
                    intHeadingLength = len(stringHeading)
                    intHeadingPadding = 3
                    stringVSPHeadings = stringVSPHeadings + stringHeading.ljust(intHeadingLength + intHeadingPadding)
                    stringVSPPopSize = str(pop.subPopSize([intSubPop, intVirtualSubPop]))
                    stringVSPPopSizeTotals = stringVSPPopSizeTotals + stringVSPPopSize.ljust(intHeadingLength + intHeadingPadding)
                    
                    strSS_InfoField = 'age_in_months'
                    if int(stringVSPPopSize) > 0:
                        strMin_Mean_Max = self.method_Display_String_Min_Mean_Max(pop, intSubPop, intVirtualSubPop, strSS_InfoField)
                    else:
                        strMin_Mean_Max = ''
                        
                    strMin_Mean_Max_String += strMin_Mean_Max.ljust(intHeadingLength + intHeadingPadding)

                    if stringVSPPopSize == '0':
                        stringIndividual1AgeForVSP = stringIndividual1AgeForVSP + 'NA'.ljust(intHeadingLength + intHeadingPadding)
                    else:
                        for individual in pop.individuals([intSubPop, intVirtualSubPop]):
                            stringIndividual1AgeForVSP = stringIndividual1AgeForVSP + str(int(individual.age_in_months)).ljust(intHeadingLength + intHeadingPadding)
                            break
                        
                objOutput.write('Age class:'.ljust(30) + stringVSPHeadings)
                objOutput.write('\n')
                objOutput.write('Size:'.ljust(30) + stringVSPPopSizeTotals)
                objOutput.write('\n')
                objOutput.write('Ages (Min-Mean-Max):'.ljust(30) + strMin_Mean_Max_String)
                objOutput.write('\n')
                
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeClassSummaryInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                    
            def methodFileOutput_SimAgeClassSummaryInfo(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, intSubPop, intCurrentTemporalFertilisation):
                
                intNumberVirtualSubPops = pop.numVirtualSubPop()
                
                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeClassSummaryInfo - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                    
                stringVSPPopSizeTotals=''
                stringVSPHeadings=''
                stringIndividual1AgeForVSP=''
                strMin_Mean_Max_String = ''
                for intVirtualSubPop in range(intSubPop, intNumberVirtualSubPops):
                    stringHeading = pop.subPopName([intSubPop, intVirtualSubPop]).ljust(10)
                    intHeadingLength = len(stringHeading)
                    intHeadingPadding = 3
                    stringVSPHeadings = stringVSPHeadings + stringHeading.ljust(intHeadingLength + intHeadingPadding)
                    stringVSPPopSize = str(pop.subPopSize([intSubPop, intVirtualSubPop]))
                    stringVSPPopSizeTotals = stringVSPPopSizeTotals + stringVSPPopSize.ljust(intHeadingLength + intHeadingPadding)
                    
                    strSS_InfoField = 'age_in_months'
                    if int(stringVSPPopSize) > 0:
                        strMin_Mean_Max = self.method_Display_String_Min_Mean_Max(pop, intSubPop, intVirtualSubPop, strSS_InfoField)
                    else:
                        strMin_Mean_Max = ''
                        
                    strMin_Mean_Max_String += strMin_Mean_Max.ljust(intHeadingLength + intHeadingPadding)

                    if stringVSPPopSize == '0':
                        stringIndividual1AgeForVSP = stringIndividual1AgeForVSP + 'NA'.ljust(intHeadingLength + intHeadingPadding)
                    else:
                        for individual in pop.individuals([intSubPop, intVirtualSubPop]):
                            stringIndividual1AgeForVSP = stringIndividual1AgeForVSP + str(int(individual.age_in_months)).ljust(intHeadingLength + intHeadingPadding)
                            break
                        
                objOutput.write('Age class:'.ljust(30) + stringVSPHeadings)
                objOutput.write('\n')
                objOutput.write('Size:'.ljust(30) + stringVSPPopSizeTotals)
                objOutput.write('\n')
                objOutput.write('Ages (Min-Mean-Max):'.ljust(30) + strMin_Mean_Max_String)
                objOutput.write('\n')
                
                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimAgeClassSummaryInfo - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    objOutput.write('\n')
                    
            def methodOutput_SimPopDump(self, pop, listOutputDestinations, listDumpParameters):
                '''
                Output simulation population dump
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        self.methodConsoleOutput_DumpOfAllAgeClasses(pop, listDumpParameters[0], listDumpParameters[1], listDumpParameters[2], listDumpParameters[3], listDumpParameters[4], listDumpParameters[5], listDumpParameters[6])
                        
                        pass
                    else:
                        #write output to file
                        self.methodWriteFileOutput_DumpOfAllAgeClasses(stringOutputDestination, pop, listDumpParameters[0], listDumpParameters[1], listDumpParameters[2], listDumpParameters[3], listDumpParameters[4], listDumpParameters[5], listDumpParameters[6])

            def methodConsoleOutput_DumpOfAllAgeClasses(self, pop, intSubPop, intWidth, intMaxIndivsToDisplayPerSubPop, boolOutputStructure, boolOutputGenotype, listInfoFields, strMethod_Call_Origin):
              
                intNumberVirtualSubPops = pop.numVirtualSubPop()
                    
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('Sim Dump - ' + strMethod_Call_Origin + ' - BEGIN ', 120)
                sys__stdout.write(strMessageDelineationText)
                sys__stdout.write('\n')
                sys__stdout.write('pop.numVirtualSubPop:' + str(intNumberVirtualSubPops))
                sys__stdout.write('\n')

                for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                    sys__stdout.write('++++ Sim Dump Virtual Sub-population [' + str(intSubPop) + ', ' + str(intVirtualSubPop) + '] ++++')
                    sys__stdout.write('\n')
                    sys__stdout.write('------------------------------------------------------------------')
                    sys__stdout.write('\n')
                    
                    simupop.dump(pop, width=intWidth, subPops=[(intSubPop,intVirtualSubPop)], max=intMaxIndivsToDisplayPerSubPop, structure=boolOutputStructure, genotype=boolOutputGenotype, infoFields=listInfoFields)

                    sys__stdout.write('\n')
                    sys__stdout.write('------------------------------------------------------------------')
                    sys__stdout.write('\n')
                    sys__stdout.write('pop.subPopName([' + str(intSubPop) + ', ' + str(intVirtualSubPop) + ']):' + pop.subPopName([intSubPop, intVirtualSubPop]))
                    sys__stdout.write('\n')
                    sys__stdout.write('pop.subPopSize([' + str(intSubPop) + ', ' + str(intVirtualSubPop) + ']):' + str(pop.subPopSize([intSubPop, intVirtualSubPop])))
                    sys__stdout.write('\n')
                    
                    with SSAnalysisHandler() as SSAnalysisOperation:
                        listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop, intSubPop, intVirtualSubPop)
                    
                    sys__stdout.write('Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))   
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('Sim Dump - ' + strMethod_Call_Origin + ' - END ', 120)
                    sys__stdout.write(strMessageDelineationText)
    
            def methodWriteFileOutput_DumpOfAllAgeClasses(self, stringOutputDestination, pop, intSubPop, intWidth, intMaxIndivsToDisplayPerSubPop, boolOutputStructure, boolOutputGenotype, listInfoFields, strMethod_Call_Origin):

                intNumberVirtualSubPops = pop.numVirtualSubPop()

                with FileHandler() as objectFileHandler:
                    #Open the file for APPEND
                    outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                    
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('Sim Dump - ' + strMethod_Call_Origin + ' - BEGIN ', 120)
                    outputFileHandle.write(strMessageDelineationText)
                    outputFileHandle.write('\n')
                    outputFileHandle.write('pop.numVirtualSubPop:' + str(intNumberVirtualSubPops))
                    outputFileHandle.write('\n')

                    for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                        outputFileHandle.write('++++ Sim Dump Virtual Sub-population [' + str(intSubPop) + ', ' + str(intVirtualSubPop) + '] ++++')
                        outputFileHandle.write('\n')
                        outputFileHandle.write('------------------------------------------------------------------')
                        outputFileHandle.write('\n')
                        #Close the file
                        boolSuccessful = objectFileHandler.fileClose(outputFileHandle)

                        simupop.dump(pop, width=intWidth, subPops=[(intSubPop,intVirtualSubPop)], max=intMaxIndivsToDisplayPerSubPop, structure=boolOutputStructure, genotype=boolOutputGenotype, infoFields=listInfoFields, output='>>>' + stringOutputDestination)

                        #Ooen the file for APPEND
                        outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')

                        outputFileHandle.write('\n')
                        outputFileHandle.write('------------------------------------------------------------------')
                        outputFileHandle.write('\n')
                        outputFileHandle.write('pop.subPopName([' + str(intSubPop) + ', ' + str(intVirtualSubPop) + ']):' + pop.subPopName([intSubPop, intVirtualSubPop]))
                        outputFileHandle.write('\n')
                        outputFileHandle.write('pop.subPopSize([' + str(intSubPop) + ', ' + str(intVirtualSubPop) + ']):' + str(pop.subPopSize([intSubPop, intVirtualSubPop])))
                        outputFileHandle.write('\n')
                    
                        with SSAnalysisHandler() as SSAnalysisOperation:
                            listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop, intSubPop, intVirtualSubPop)
                    
                        outputFileHandle.write('Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))   
                        strMessageDelineationText = self.methodConstruct_MessageDelineationLine('Sim Dump - ' + strMethod_Call_Origin + ' - END ', 120)
                        outputFileHandle.write(strMessageDelineationText)
                    
                    #Perform FINAL close of the file
                    boolSuccessful = objectFileHandler.fileClose(outputFileHandle)

            def methodOutput_SimSummaryInfo(self, objSharkSimOperation, listOutputDestinations, boolPauseOutput):
                '''
                Output simulation summary details
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_SimStartingProperties(objOutput, objSharkSimOperation, boolPauseOutput)
                        self.methodConsoleOutput_LifeStageDefinitions(objOutput, objSharkSimOperation)
                        pass
                    else:
                        #write output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                objOutput=outputFileHandle
                                self.methodWriteFileOutput_SimStartingProperties(objOutput, objSharkSimOperation)
                                self.methodWriteFileOutput_LifeStageDefinitions(objOutput, objSharkSimOperation)
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                objOutput=outputFileHandle
                                self.methodWriteFileOutput_SimStartingProperties(objOutput, objSharkSimOperation)
                                self.methodWriteFileOutput_LifeStageDefinitions(objOutput, objSharkSimOperation)
                            
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)

            def method_Log_Output__SimStartingProperties(self, obj_Logger, obj_SSParams, boolPauseOutput):
                
                strMessageDelineationText = self.method_Construct__MessageDelineationLine('SharkSimOperation properties - BEGIN ', 120)
                obj_Logger.info(strMessageDelineationText)
                obj_Logger.info(' Project Run Path                    : ' + str(obj_SSParams.str_Current_Run_Path))
                obj_Logger.info(' User-Specified Path                 : ' + str(obj_SSParams.strRunSpecificUserDefinedFolder))
                obj_Logger.info(' Run UID                             : ' + str(obj_SSParams.strUniqueRunID))
                obj_Logger.info('-----------------------------------------')
                obj_Logger.info(' Suppress Burn-in output             : ' + str(obj_SSParams.boolSuppressBurnInOutput))
                obj_Logger.info(' Loci to report Ne for (if enabled)  : ' + str(obj_SSParams.listLociToReportNE))
                obj_Logger.info(' Suppress Demographic Ne reporting   : ' + str(obj_SSParams.boolReportDemographicNe))
                obj_Logger.info(' Suppress LDNe reporting             : ' + str(obj_SSParams.boolReportLDNe))
                obj_Logger.info(' Suppress Temporal FS_P1_Ne reporting: ' + str(obj_SSParams.boolReportTemporalFS_P1_Ne))
                obj_Logger.info(' Suppress Temporal FS_P2_Ne reporting: ' + str(obj_SSParams.boolReportTemporalFS_P2_Ne))
                obj_Logger.info('-----------------------------------------')
                obj_Logger.info(' Burn-in length (years)              : '+ str(obj_SSParams.intReplicateBurnInLengthInYears))
                obj_Logger.info(' Simulation Length (years, months)   : ' + str(obj_SSParams.intTotalYearsToSimulate) + ', ' + str(obj_SSParams.intTotalMonthsToSimulate))
                obj_Logger.info(' Simulated potential fertilisations  : ' + str(obj_SSParams.intOffspringPotentialFertilisationsToSimulate))
                obj_Logger.info(' Initial population age scheme       : ' + str(obj_SSParams.intPopulationInitialAges))
                obj_Logger.info(' Predicted Breeding Population Size  : '+ str(obj_SSParams.intPredictedBreedingPopulationSize))
                obj_Logger.info('-----------------------------------------')
                obj_Logger.info(' Species Run Specification           : ' + str(obj_SSParams.str_Species_Code))
                obj_Logger.info(' Population size                     : ' + str(obj_SSParams.popnSize))
                obj_Logger.info(' Maximum age (months)                : '+ str(obj_SSParams.maxAge))
                obj_Logger.info(' Minimal mating age (months)         : '+ str(obj_SSParams.minMatingAge))
                obj_Logger.info(' Maximal mating age (months)         : '+ str(obj_SSParams.maxMatingAge))
                obj_Logger.info('-----------------------------------------')
                obj_Logger.info(' Male sex ratio (initial & ongoing)  : ' + str(obj_SSParams.floatSexRatioOfMales))
                obj_Logger.info(' Mating scheme                       : ' + str(obj_SSParams.intMatingSchemeType))
                obj_Logger.info(' Polygamyous mates (if appropriate)  : ' + str(obj_SSParams.intPolygamousMateNumber))
                obj_Logger.info(' Mean number of offspring per individual & Offspring generatio probability distribution...')
                obj_Logger.info(' List mating distribution:           : '+ str(obj_SSParams.listOffspringNumberParameters))
                obj_Logger.info(' Mating month                        : ' + str(obj_SSParams.intMatingCalenderMonth))
                obj_Logger.info(' Parturition month                   : ' + str(obj_SSParams.intParturitionCalenderMonth))
                obj_Logger.info(' Gestation length                    : ' + str(obj_SSParams.intGestationLengthInMonths))
                obj_Logger.info(' Reproductive Resting length         : ' + str(obj_SSParams.intReproductiveRestLengthInMonths))
                obj_Logger.info('-----------------------------------------')
                obj_Logger.info(' Number of loci                      : '+ str(obj_SSParams.nLoci))
                obj_Logger.info(' Loci alleles per locus distribution : '+ str(obj_SSParams.str_Genome_Alleles_Per_Locus_Distribution))
                if obj_SSParams.int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__UNIFORM:
                    obj_Logger.info(' Number of alleles per locus         : '+ str(obj_SSParams.int_Alleles_Per_Locus))
                pass
                if obj_SSParams.int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__BINOMIAL:
                    obj_Logger.info(' Mean alleles per locus          : '+ str(obj_SSParams.float_Genome_BINOMIAL_Mean_Number_Alleles_Per_Locus))
                    obj_Logger.info(' Stddev alleles per locus        : '+ str(obj_SSParams.float_Genome_BINOMIAL_StdDev_Alleles_Per_Locus))
                pass
                obj_Logger.info(' Loci allele frequencies scheme      : '+ str(obj_SSParams.str_Genome_Allele_Frequency_Distribution))
                if obj_SSParams.intAlleleFrequencyScheme == globalsSS.Allele_Frequency_Distribution.static_int_Allele_Frequency_Distribution_Distribution__ALL_ALLELE_FREQUENCIES_FILE:
                    intLocusCount = 0
                    for listLocusAlleleFreqs in obj_SSParams.listAlleleFreqs:
                        intLeftJustify = 3
                        stringPadChar = '-'
                        stringPadString = '> '
                        stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
                        obj_Logger.info(' ' + stringLeftJustifyFormat.format(str(intLocusCount)) + stringPadString)
                        
    #                     intLeftJustify = 10
    #                     stringPadChar = ' '
    #                     stringPadString = '> '
    #                     stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
    #                     obj_Logger.info(stringLeftJustifyFormat.format(pop.locusName(intLocus)))
                        
                        intLeftJustify = 18
                        stringPadChar = ' '
                        stringPadString = '> '
                        stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
                        obj_Logger.info(stringLeftJustifyFormat.format('Allele Count : ' + str(len(listLocusAlleleFreqs))))
                        
                        obj_Logger.info('Allele Frequencies : ' + str(listLocusAlleleFreqs))
                        intLocusCount += 1
                else:
                    obj_Logger.info(' Loci allele frequencies             : NOT AVIALABLE UNTIL SIMULATION STARTS') #+ str(obj_SSParams.listAlleleFreqs))
                pass        
                obj_Logger.info('-----------------------------------------')
                obj_Logger.info(' Output file                         : '+ obj_SSParams.outfilePath + obj_SSParams.strFileNameProgramPrefix + obj_SSParams.strFilenameEmbeddedFields + '.ped.txt')
                obj_Logger.info(' Number of Replicates                : '+ str(obj_SSParams.intReplicates))
                obj_Logger.info(' Current Replicate                   : '+ str(obj_SSParams.intCurrentReplicate))
                
                strMessageDelineationText = self.method_Construct__MessageDelineationLine('SharkSimOperation properties - END   ', 120)
                obj_Logger.info(strMessageDelineationText)

                if boolPauseOutput:
                    self.method_Pause_Console()
                    
                return True
            
            def methodConsoleOutput_SimStartingProperties(self, objOutput, objSharkSimOperation, boolPauseOutput):
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation properties - BEGIN ', 120)
                objOutput.write(strMessageDelineationText)
                objOutput.write('\n')
                objOutput.write(' Suppress Burn-in output             : ' + str(objSharkSimOperation.boolSuppressBurnInOutput))
                objOutput.write('\n')
                objOutput.write(' Loci to report Ne for (if enabled)  : ' + str(objSharkSimOperation.listLociToReportNE))
                objOutput.write('\n')
                objOutput.write(' Suppress Demographic Ne reporting   : ' + str(objSharkSimOperation.boolReportDemographicNe))
                objOutput.write('\n')
                objOutput.write(' Suppress LDNe reporting             : ' + str(objSharkSimOperation.boolReportLDNe))
                objOutput.write('\n')
                objOutput.write(' Suppress Temporal FS_P1_Ne reporting: ' + str(objSharkSimOperation.boolReportTemporalFS_P1_Ne))
                objOutput.write('\n')
                objOutput.write(' Suppress Temporal FS_P2_Ne reporting: ' + str(objSharkSimOperation.boolReportTemporalFS_P2_Ne))
                objOutput.write('\n')
                
                objOutput.write('\n')
                objOutput.write(' Population size                     : ' + str(objSharkSimOperation.popnSize))
                objOutput.write('\n')
                objOutput.write(' Burn-in length (years)              : '+ str(objSharkSimOperation.intReplicateBurnInLengthInYears))
                objOutput.write('\n')
                objOutput.write(' Simulation Length (years, months)   : ' + str(objSharkSimOperation.intTotalYearsToSimulate) + ', ' + str(objSharkSimOperation.intTotalMonthsToSimulate))
                objOutput.write('\n')
                objOutput.write(' Simulated potential fertilisations  : ' + str(objSharkSimOperation.intOffspringPotentialFertilisationsToSimulate))
                objOutput.write('\n')
                
                objOutput.write('\n')   
                objOutput.write(' Initial population age scheme       : ' + str(objSharkSimOperation.intPopulationInitialAges))
                objOutput.write('\n')   
                objOutput.write(' Male sex ratio (initial & ongoing)  : ' + str(objSharkSimOperation.floatSexRatioOfMales))
                objOutput.write('\n')
                objOutput.write(' Mating scheme                       : ' + str(objSharkSimOperation.intMatingSchemeType))
                objOutput.write('\n')
                objOutput.write(' Parturition month (Gestation length): ' + str(objSharkSimOperation.intGestationLengthInMonths))
                objOutput.write('\n')
                
                objOutput.write('\n')
                objOutput.write(' Maximum age (months)                : '+ str(objSharkSimOperation.maxAge))
                objOutput.write('\n')
                objOutput.write(' Minimal mating age (months)         : '+ str(objSharkSimOperation.minMatingAge))
                objOutput.write('\n')
                objOutput.write(' Maximal mating age (months)         : '+ str(objSharkSimOperation.maxMatingAge))
                objOutput.write('\n')
                objOutput.write('\n')
                objOutput.write(' Predicted Breeding Population Size  : '+ str(objSharkSimOperation.intPredictedBreedingPopulationSize))
                objOutput.write('\n')
                objOutput.write(' Mean number of offspring per individual (Poisson distribution)')
                objOutput.write('\n')
                objOutput.write('                                     : '+ str(objSharkSimOperation.meanvarnumOffspring))
                objOutput.write('\n')
                objOutput.write(' List mating distribution:           : '+ str(objSharkSimOperation.listOffspringNumberParameters))
                objOutput.write('\n')
                objOutput.write(' Number of loci                      : '+ str(objSharkSimOperation.nLoci))
                objOutput.write('\n')
                objOutput.write(' Loci alleles per locus distribution : '+ str(objSharkSimOperation.str_Genome_Alleles_Per_Locus_Distribution))
                objOutput.write('\n')
                if objSharkSimOperation.int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__UNIFORM:
                    objOutput.write(' Number of alleles per locus         : '+ str(objSharkSimOperation.int_Alleles_Per_Locus))
                    objOutput.write('\n')
                pass
                if objSharkSimOperation.int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__BINOMIAL:
                    objOutput.write(' Mean alleles per locus              : '+ str(objSharkSimOperation.float_Genome_BINOMIAL_Mean_Number_Alleles_Per_Locus))
                    objOutput.write('\n')
                    objOutput.write(' Stddev alleles per locus            : '+ str(objSharkSimOperation.float_Genome_BINOMIAL_StdDev_Alleles_Per_Locus))
                    objOutput.write('\n')
                pass
                objOutput.write(' Loci allele frequencies scheme      : '+ str(objSharkSimOperation.str_Genome_Allele_Frequency_Distribution))
                objOutput.write('\n')
                
                #if objSharkSimOperation.intAlleleFrequencyScheme == globalsSS.Allele_Frequency_Distribution.static_int_Allele_Frequency_Distribution_Distribution__ALL_ALLELE_FREQUENCIES_FILE:
                if objSharkSimOperation.int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__ALL_ALLELE_FREQUENCIES_FILE:
                    intLocusCount = 0
                    for listLocusAlleleFreqs in objSharkSimOperation.listAlleleFreqs:
                        intLeftJustify = 3
                        stringPadChar = '-'
                        stringPadString = '> '
                        stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
                        objOutput.write(' ' + stringLeftJustifyFormat.format(str(intLocusCount)) + stringPadString)
                        
    #                     intLeftJustify = 10
    #                     stringPadChar = ' '
    #                     stringPadString = '> '
    #                     stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
    #                     objOutput.write(stringLeftJustifyFormat.format(pop.locusName(intLocus)))
                        
                        intLeftJustify = 18
                        stringPadChar = ' '
                        stringPadString = '> '
                        stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
                        objOutput.write(stringLeftJustifyFormat.format('Allele Count : ' + str(len(listLocusAlleleFreqs))))
                        
                        objOutput.write('Allele Frequencies : ' + str(listLocusAlleleFreqs))
                        objOutput.write('\n')
                        intLocusCount += 1
                else:
                    objOutput.write(' Loci allele frequencies             : '+ str(objSharkSimOperation.listAlleleFreqs))
                pass       
                objOutput.write('\n')
                
                objOutput.write('\n')
                objOutput.write(' Output file                         : '+ objSharkSimOperation.outfilePath + objSharkSimOperation.strFileNameProgramPrefix + objSharkSimOperation.strFilenameEmbeddedFields + '.ped.txt')
                objOutput.write('\n')
                objOutput.write(' Number of Replicates                : '+ str(objSharkSimOperation.intReplicates))
                objOutput.write('\n')
                objOutput.write(' Current Replicate                   : '+ str(objSharkSimOperation.intCurrentReplicate))
                objOutput.write('\n')
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation properties - END   ', 120)
                objOutput.write(strMessageDelineationText)

                if boolPauseOutput:
                    self.method_Pause_Console(objOutput)
                    
            def methodWriteFileOutput_SimStartingProperties(self, objOutput, objSharkSimOperation):
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation properties - BEGIN ', 120)
                objOutput.write(strMessageDelineationText)
                objOutput.write('\n')
                objOutput.write(' Suppress Burn-in output             : ' + str(objSharkSimOperation.boolSuppressBurnInOutput))
                objOutput.write('\n')
                objOutput.write(' Loci to report Ne for (if enabled)  : ' + str(objSharkSimOperation.listLociToReportNE))
                objOutput.write('\n')
                objOutput.write(' Suppress Demographic Ne reporting   : ' + str(objSharkSimOperation.boolReportDemographicNe))
                objOutput.write('\n')
                objOutput.write(' Suppress LDNe reporting             : ' + str(objSharkSimOperation.boolReportLDNe))
                objOutput.write('\n')
                objOutput.write(' Suppress Temporal FS_P1_Ne reporting: ' + str(objSharkSimOperation.boolReportTemporalFS_P1_Ne))
                objOutput.write('\n')
                objOutput.write(' Suppress Temporal FS_P2_Ne reporting: ' + str(objSharkSimOperation.boolReportTemporalFS_P2_Ne))
                objOutput.write('\n')
                
                objOutput.write('\n')
                objOutput.write(' Population size                     : ' + str(objSharkSimOperation.popnSize))
                objOutput.write('\n')
                objOutput.write(' Burn-in length (years)              : '+ str(objSharkSimOperation.intReplicateBurnInLengthInYears))
                objOutput.write('\n')
                objOutput.write(' Simulation Length (years, months)   : ' + str(objSharkSimOperation.intTotalYearsToSimulate) + ', ' + str(objSharkSimOperation.intTotalMonthsToSimulate))
                objOutput.write('\n')
                objOutput.write(' Simulated potential fertilisations  : ' + str(objSharkSimOperation.intOffspringPotentialFertilisationsToSimulate))
                objOutput.write('\n')
                
                objOutput.write('\n')   
                objOutput.write(' Initial population age scheme       : ' + str(objSharkSimOperation.intPopulationInitialAges))
                objOutput.write('\n')   
                objOutput.write(' Male sex ratio (initial & ongoing)  : ' + str(objSharkSimOperation.floatSexRatioOfMales))
                objOutput.write('\n')
                objOutput.write(' Mating scheme                       : ' + str(objSharkSimOperation.intMatingSchemeType))
                objOutput.write('\n')
                objOutput.write(' Parturition month (Gestation length): ' + str(objSharkSimOperation.intGestationLengthInMonths))
                objOutput.write('\n')
                
                objOutput.write('\n')
                objOutput.write(' Maximum age (truly Max Age-0.1)     : '+ str(objSharkSimOperation.maxAge))
                objOutput.write('\n')
                objOutput.write(' Minimal mating age                  : '+ str(objSharkSimOperation.minMatingAge))
                objOutput.write('\n')
                objOutput.write(' Maximal mating age                  : '+ str(objSharkSimOperation.maxMatingAge))
                objOutput.write('\n')
                objOutput.write(' Predicted Breeding Population Size  : '+ str(objSharkSimOperation.intPredictedBreedingPopulationSize))
                objOutput.write('\n')
                objOutput.write(' Mean number of offspring per individual (Poisson distribution)')
                objOutput.write('\n')
                objOutput.write('                                     : '+ str(objSharkSimOperation.meanvarnumOffspring))
                objOutput.write('\n')
                objOutput.write(' List mating distribution:           : '+ str(objSharkSimOperation.listOffspringNumberParameters))
                objOutput.write('\n')
                objOutput.write(' Number of loci                      : '+ str(objSharkSimOperation.nLoci))
                objOutput.write('\n')
                objOutput.write(' Number of alleles per loci          : '+ str(objSharkSimOperation.nAllelesPerLoci))
                objOutput.write('\n')
                objOutput.write(' Loci allele frequencies scheme      : '+ str(objSharkSimOperation.intAlleleFrequencyScheme))
                objOutput.write('\n')
                objOutput.write(' Loci allele frequencies             : '+ str(objSharkSimOperation.listAlleleFreqs))
                objOutput.write('\n')
                
                objOutput.write('\n')
                objOutput.write(' Output file                         : '+ objSharkSimOperation.outfilePath + objSharkSimOperation.strFileNameProgramPrefix + objSharkSimOperation.strFilenameEmbeddedFields + '.ped.txt')
                objOutput.write('\n')
                objOutput.write(' Number of Replicates                : '+ str(objSharkSimOperation.intReplicates))
                objOutput.write('\n')
                objOutput.write(' Current Replicate                   : '+ str(objSharkSimOperation.intCurrentReplicate))
                objOutput.write('\n')
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation properties - END   ', 120)
                objOutput.write(strMessageDelineationText)

            def method_Log_Output__LifeStageDefinitions(self, obj_Logger, obj_SSParams):
                
                strMessageDelineationText = self.method_Construct__MessageDelineationLine('SharkSimOperation Life Stage Definitions - BEGIN', 120)
                obj_Logger.info(strMessageDelineationText)
                obj_Logger.info('Total the individuals in each life stage per year')
                obj_Logger.info(' Sub-adult               - L0: age <  ' + str(obj_SSParams.minMatingAge))
                obj_Logger.info(' Reproductive adult      - L1: age >= ' + str(obj_SSParams.minMatingAge) + ' and age =< ' + str(obj_SSParams.maxMatingAge - 0.1) + '       [age < maxMatingAge]')
                obj_Logger.info(' Post-reproductive adult - L2: age >= ' + str(obj_SSParams.maxMatingAge) + ' and age =< ' + str(obj_SSParams.maxAge - 0.1) + '       [maxMatingAge < age < maxAge]')
                obj_Logger.info(' Mort!                   - L3: age >= ' + str(obj_SSParams.maxAge) + '                      [age > maxAge] DEAD but only zeroed at Parturition')
                strMessageDelineationText = self.method_Construct__MessageDelineationLine('SharkSimOperation Life Stage Definitions - END   ', 120)
                obj_Logger.info(strMessageDelineationText)
                
            def methodConsoleOutput_LifeStageDefinitions(self, objOutput, objSharkSimOperation):
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation Life Stage Definitions - BEGIN', 120)
                objOutput.write(strMessageDelineationText)
                objOutput.write('\n')
                objOutput.write('Total the individuals in each life stage per year')
                objOutput.write('\n')
                objOutput.write('\n')
                objOutput.write(' Sub-adult               - L0: age <  ' + str(objSharkSimOperation.minMatingAge))
                objOutput.write('\n')
                objOutput.write(' Reproductive adult      - L1: age >= ' + str(objSharkSimOperation.minMatingAge) + ' and age =< ' + str(objSharkSimOperation.maxMatingAge - 0.1) + '       [age < maxMatingAge]')
                objOutput.write('\n')
                objOutput.write(' Post-reproductive adult - L2: age >= ' + str(objSharkSimOperation.maxMatingAge) + ' and age =< ' + str(objSharkSimOperation.maxAge - 0.1) + '       [maxMatingAge < age < maxAge]')
                objOutput.write('\n')
                objOutput.write(' Mort!                   - L3: age >= ' + str(objSharkSimOperation.maxAge) + '                      [age > maxAge] DEAD but only zeroed at Parturition \n')
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation Life Stage Definitions - END   ', 120)
                objOutput.write(strMessageDelineationText)

            def methodWriteFileOutput_LifeStageDefinitions(self, objOutput, objSharkSimOperation):
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation Life Stage Definitions - BEGIN', 120)
                objOutput.write(strMessageDelineationText)
                objOutput.write('\n')
                objOutput.write('Total the individuals in each life stage per year')
                objOutput.write('\n')
                objOutput.write('\n')
                objOutput.write(' Sub-adult               - L0: age <  ' + str(objSharkSimOperation.minMatingAge))
                objOutput.write('\n')
                objOutput.write(' Reproductive adult      - L1: age >= ' + str(objSharkSimOperation.minMatingAge) + ' and age =< ' + str(objSharkSimOperation.maxMatingAge - 0.1) + '       [age < maxMatingAge]')
                objOutput.write('\n')
                objOutput.write(' Post-reproductive adult - L2: age >= ' + str(objSharkSimOperation.maxMatingAge) + ' and age =< ' + str(objSharkSimOperation.maxAge - 0.1) + '       [maxMatingAge < age < maxAge]')
                objOutput.write('\n')
                objOutput.write(' Mort!                   - L3: age >= ' + str(objSharkSimOperation.maxAge) + '                      [age > maxAge] DEAD but only zeroed at Parturition \n')
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation Life Stage Definitions - END   ', 120)
                objOutput.write(strMessageDelineationText)

            def method_Output_Population_Offspring_Totals_By_Parent(self, pop, listOutputDestinations, listOffspringNumberParameters,  intSubPop, intVirtualSubPop):
                '''
                Output population offspring totals for each parent
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.method_Console_Output_Population_Offspring_Totals_By_Parent(objOutput, pop, listOffspringNumberParameters,  intSubPop, intVirtualSubPop)
                        
                        pass
                    else:
                         #write output to file
                        
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                objOutput=outputFileHandle
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                objOutput=outputFileHandle
                            
                            self.method_File_Output_Population_Offspring_Totals_By_Parent(objOutput, pop, listOffspringNumberParameters,  intSubPop, intVirtualSubPop)

                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
            
            def method_Console_Output_Population_Offspring_Totals_By_Parent(self, objOutput, pop, listOffspringNumberParameters,  intSubPop, intVirtualSubPop):
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation VSP[' + str(intSubPop) + ',' + str(intVirtualSubPop) + '] ' +  'Offspring Totals By Parent - BEGIN', 120)
                objOutput.write(strMessageDelineationText)
                objOutput.write('\n')
                
                #Check if any offspring exist in the Embyro life stage
                intVSPPopSize = pop.subPopSize([intSubPop, intVirtualSubPop])
                
                if intVSPPopSize > 0:
                    with SSAnalysisHandler() as objSSAnalysisOperation:
                        listPopulationOffspringTotalsByParentPair = objSSAnalysisOperation.method_Count_Offspring_Per_Sorted_ParentPair_For_VirtualSubPop(pop, intSubPop, intVirtualSubPop)
                        
                        dictPopulationOffspringTotalsBySire = AutoVivificationHandler()
                        dictPopulationOffspringTotalsBySire = objSSAnalysisOperation.method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(pop, intSubPop, intVirtualSubPop)
                        dictPopulationOffspringTotalsByDame = AutoVivificationHandler()
                        dictPopulationOffspringTotalsByDame = objSSAnalysisOperation.method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(pop, intSubPop, intVirtualSubPop)

                        list_Offspring_Count_Sires_Sorted = sorted(dictPopulationOffspringTotalsBySire[1].items(), key=operator.itemgetter(0))
                        list_Offspring_Count_Dames_Sorted = sorted(dictPopulationOffspringTotalsByDame[2].items(), key=operator.itemgetter(0))
    
                        #listPotentialParents = objSSAnalysisOperation.method_List_IndividualID_For_VirtualSubPop(pop, intSubPop, intVirtualSubPop+1, 'ind_id', True)
                        listPotentialParents = objSSAnalysisOperation.method_List_IndividualID_For_VirtualSubPop(pop, intSubPop, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult, 'ind_id', True)
                        listPotentialParents = [int(i) for i in listPotentialParents]
                        listPotentialParentsSex = objSSAnalysisOperation.method_List_Sexes_For_VirtualSubPop(pop, intSubPop, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult, 'ind_id', True)
                        
                        dictOffspringCount = objSSAnalysisOperation.method_Count_Offspring_PerParent_For_VirtualSubPop(pop, dictPopulationOffspringTotalsBySire, dictPopulationOffspringTotalsByDame, intSubPop, intVirtualSubPop)
                        
                        list_Offspring_Count_Putative_Parent_Male_Sorted = sorted(dictOffspringCount[1].items(), key=operator.itemgetter(0))
                        list_Offspring_Count_Putative_Parent_Female_Sorted = sorted(dictOffspringCount[2].items(), key=operator.itemgetter(0))
                        
                        objOutput.write('\n')
                        objOutput.write('Potential Parents Count: ')
                        objOutput.write(str(len(listPotentialParents)))
                        objOutput.write('\n')
                        objOutput.write('Potential Parent Individual ID List (sorted ascending): ')
                        objOutput.write('\n')
                        objOutput.write(str(listPotentialParents))
                        objOutput.write('\n')
                        objOutput.write('Potential Parent Sex List (sorted ascending): ')
                        objOutput.write('\n')
                        objOutput.write(str(listPotentialParentsSex))
                        objOutput.write('\n')
                        objOutput.write('Potential Parents MALE Count  : ')
                        objOutput.write(str(listPotentialParentsSex.count('M')))
                        objOutput.write('\n')
                        objOutput.write('Potential Parents FEMALE Count: ')
                        objOutput.write(str(listPotentialParentsSex.count('F')))
                        objOutput.write('\n')
                        objOutput.write('Offspring Per Parent Count [(PARENT_ID, OFFSPING_COUNT)]: ')
                        objOutput.write('\n')
                        objOutput.write('Male  : ' + str(list_Offspring_Count_Putative_Parent_Male_Sorted))
                        objOutput.write('\n')
                        objOutput.write('Female: ' + str(list_Offspring_Count_Putative_Parent_Female_Sorted))
                        objOutput.write('\n')
    
                        with AnalysisHandler() as objAnalysisOperation:
                            #Construct a list of MALE offspring counts
                            listMaleOffspringCount = []
                            for i in dictOffspringCount[simupop.MALE]:
                                listMaleOffspringCount.append(dictOffspringCount[simupop.MALE][i])
    
                            floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listMaleOffspringCount)
                            floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listMaleOffspringCount)
                        
                            objOutput.write('Mean and Variance in Offspring Per MALE Parent: ')
                            objOutput.write('\n')
                            objOutput.write(str(floatMean) +', ' + str(round(floatVariance,4)))
                            objOutput.write('\n')
    
                            #Construct a list of FEMALE offspring counts
                            listFemaleOffspringCount = []
                            for i in dictOffspringCount[simupop.FEMALE]:
                                listFemaleOffspringCount.append(dictOffspringCount[simupop.FEMALE][i])
    
                            floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listFemaleOffspringCount)
                            floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listFemaleOffspringCount)
    
                            objOutput.write('Mean and Variance in Offspring Per FEMALE Parent: ')
                            objOutput.write('\n')
                            objOutput.write(str(floatMean) +', ' + str(round(floatVariance,4)))
                            objOutput.write('\n')
    
                            listBothSexesOffspringCount = []
                            for intCount in listMaleOffspringCount:
                                listBothSexesOffspringCount.append(intCount)
                            for intCount in listFemaleOffspringCount:
                                listBothSexesOffspringCount.append(intCount)
    
                            floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listBothSexesOffspringCount)
                            floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listBothSexesOffspringCount)
    
                            objOutput.write('Mean and Variance in Offspring Per Parent of BOTH SEXES: ')
                            objOutput.write('\n')
                            objOutput.write(str(floatMean) +', ' + str(round(floatVariance,4)))
                            objOutput.write('\n')
    
                        objOutput.write('\n')
                        objOutput.write('Offspring Generation Distribution Parameters: ' + str(listOffspringNumberParameters))
                        objOutput.write('\n')
    
                        listSires = objSSAnalysisOperation.method_List_ParentID_Per_Offspring_For_VirtualSubPop(pop, intSubPop, intVirtualSubPop, 'father_id', True)
                        objOutput.write('\n')
                        objOutput.write('Sire Count: ')
                        objOutput.write(str(len(listSires)))
                        objOutput.write('\n')
                        objOutput.write('Sire ID List (sorted ascending): ')
                        objOutput.write('\n')
                        objOutput.write(str(listSires))
                        objOutput.write('\n')
                        objOutput.write('Sire (sorted ascending) Offspring Count List: ')
                        objOutput.write('\n')
                        objOutput.write(str(list_Offspring_Count_Sires_Sorted))
                        objOutput.write('\n')
    
                        listDames = objSSAnalysisOperation.method_List_ParentID_Per_Offspring_For_VirtualSubPop(pop, intSubPop, intVirtualSubPop, 'mother_id', True)
                        objOutput.write('\n')
                        objOutput.write('Dame Count : ')
                        objOutput.write(str(len(listDames)))
                        objOutput.write('\n')
                        objOutput.write('Dame ID List (sorted ascending) : ')
                        objOutput.write('\n')
                        objOutput.write(str(listDames))
                        objOutput.write('\n')
                        objOutput.write('Dame (sorted ascending) Offspring Count List: ')
                        objOutput.write('\n')
                        objOutput.write(str(list_Offspring_Count_Dames_Sorted))
                        objOutput.write('\n')
    
                        listParentPairs = objSSAnalysisOperation.method_List_ParentID_Per_Sorted_ParentPair_For_VirtualSubPop(pop, intSubPop, intVirtualSubPop)
                        objOutput.write('\n')
                        objOutput.write('Parent Pair Count : ')
                        objOutput.write(str(len(listParentPairs)))
                        objOutput.write('\n')
                        objOutput.write('Parent Pair ID List : ')
                        objOutput.write('\n')
                        objOutput.write(str(listParentPairs))
                        objOutput.write('\n')
                        objOutput.write('Parent Pair Offspring Count List: ')
                        objOutput.write('\n')
                        objOutput.write(str(listPopulationOffspringTotalsByParentPair))
                        objOutput.write('\n')
                else:
                    objOutput.write(color.RED + 'No offspring were produced' + color.END)
                    objOutput.write('\n')
                    
                objOutput.write('\n')
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation VSP[' + str(intSubPop) + ',' + str(intVirtualSubPop) + '] ' +  'Offspring Totals By Parent - END  ', 120)
                objOutput.write(strMessageDelineationText)

            def method_File_Output_Population_Offspring_Totals_By_Parent(self, objOutput, pop, listOffspringNumberParameters,  intSubPop, intVirtualSubPop):
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation VSP[' + str(intSubPop) + ',' + str(intVirtualSubPop) + '] ' +  'Offspring Totals By Parent - BEGIN', 120)
                objOutput.write(strMessageDelineationText)
                objOutput.write('\n')
                
                #Check if any offspring exist in the Embyro life stage
                intVSPPopSize = pop.subPopSize([intSubPop, intVirtualSubPop])
                
                if intVSPPopSize > 0:
                    with SSAnalysisHandler() as objSSAnalysisOperation:
                        listPopulationOffspringTotalsByParentPair = objSSAnalysisOperation.method_Count_Offspring_Per_Sorted_ParentPair_For_VirtualSubPop(pop, intSubPop, intVirtualSubPop)
                        
                        dictPopulationOffspringTotalsBySire = AutoVivificationHandler()
                        dictPopulationOffspringTotalsBySire = objSSAnalysisOperation.method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(pop, intSubPop, intVirtualSubPop)
                        dictPopulationOffspringTotalsByDame = AutoVivificationHandler()
                        dictPopulationOffspringTotalsByDame = objSSAnalysisOperation.method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(pop, intSubPop, intVirtualSubPop)

                        list_Offspring_Count_Sires_Sorted = sorted(dictPopulationOffspringTotalsBySire[1].items(), key=operator.itemgetter(0))
                        list_Offspring_Count_Dames_Sorted = sorted(dictPopulationOffspringTotalsByDame[2].items(), key=operator.itemgetter(0))
    
                        #listPotentialParents = objSSAnalysisOperation.method_List_IndividualID_For_VirtualSubPop(pop, intSubPop, intVirtualSubPop+1, 'ind_id', True)
                        listPotentialParents = objSSAnalysisOperation.method_List_IndividualID_For_VirtualSubPop(pop, intSubPop, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult, 'ind_id', True)
                        listPotentialParents = [int(i) for i in listPotentialParents]
                        listPotentialParentsSex = objSSAnalysisOperation.method_List_Sexes_For_VirtualSubPop(pop, intSubPop, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult, 'ind_id', True)
                        
                        dictOffspringCount = objSSAnalysisOperation.method_Count_Offspring_PerParent_For_VirtualSubPop(pop, dictPopulationOffspringTotalsBySire, dictPopulationOffspringTotalsByDame, intSubPop, intVirtualSubPop)
                        
                        list_Offspring_Count_Putative_Parent_Male_Sorted = sorted(dictOffspringCount[1].items(), key=operator.itemgetter(0))
                        list_Offspring_Count_Putative_Parent_Female_Sorted = sorted(dictOffspringCount[2].items(), key=operator.itemgetter(0))
                        
                        objOutput.write('\n')
                        objOutput.write('Potential Parents Count: ')
                        objOutput.write(str(len(listPotentialParents)))
                        objOutput.write('\n')
                        objOutput.write('Potential Parent Individual ID List (sorted ascending): ')
                        objOutput.write('\n')
                        objOutput.write(str(listPotentialParents))
                        objOutput.write('\n')
                        objOutput.write('Potential Parent Sex List (sorted ascending): ')
                        objOutput.write('\n')
                        objOutput.write(str(listPotentialParentsSex))
                        objOutput.write('\n')
                        objOutput.write('Potential Parents MALE Count  : ')
                        objOutput.write(str(listPotentialParentsSex.count('M')))
                        objOutput.write('\n')
                        objOutput.write('Potential Parents FEMALE Count: ')
                        objOutput.write(str(listPotentialParentsSex.count('F')))
                        objOutput.write('\n')
                        objOutput.write('Offspring Per Parent Count [(PARENT_ID, OFFSPING_COUNT)]: ')
                        objOutput.write('\n')
                        objOutput.write('Male  : ' + str(list_Offspring_Count_Putative_Parent_Male_Sorted))
                        objOutput.write('\n')
                        objOutput.write('Female: ' + str(list_Offspring_Count_Putative_Parent_Female_Sorted))
                        objOutput.write('\n')
    
                        with AnalysisHandler() as objAnalysisOperation:
                            #Construct a list of MALE offspring counts
                            listMaleOffspringCount = []
                            for i in dictOffspringCount[simupop.MALE]:
                                listMaleOffspringCount.append(dictOffspringCount[simupop.MALE][i])
    
                            floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listMaleOffspringCount)
                            floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listMaleOffspringCount)
                        
                            objOutput.write('Mean and Variance in Offspring Per MALE Parent: ')
                            objOutput.write('\n')
                            objOutput.write(str(floatMean) +', ' + str(round(floatVariance,4)))
                            objOutput.write('\n')
    
                            #Construct a list of FEMALE offspring counts
                            listFemaleOffspringCount = []
                            for i in dictOffspringCount[simupop.FEMALE]:
                                listFemaleOffspringCount.append(dictOffspringCount[simupop.FEMALE][i])
    
                            floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listFemaleOffspringCount)
                            floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listFemaleOffspringCount)
    
                            objOutput.write('Mean and Variance in Offspring Per FEMALE Parent: ')
                            objOutput.write('\n')
                            objOutput.write(str(floatMean) +', ' + str(round(floatVariance,4)))
                            objOutput.write('\n')
    
                            listBothSexesOffspringCount = []
                            for intCount in listMaleOffspringCount:
                                listBothSexesOffspringCount.append(intCount)
                            for intCount in listFemaleOffspringCount:
                                listBothSexesOffspringCount.append(intCount)
    
                            floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listBothSexesOffspringCount)
                            floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listBothSexesOffspringCount)
    
                            objOutput.write('Mean and Variance in Offspring Per Parent of BOTH SEXES: ')
                            objOutput.write('\n')
                            objOutput.write(str(floatMean) +', ' + str(round(floatVariance,4)))
                            objOutput.write('\n')
    
                        objOutput.write('\n')
                        objOutput.write('Offspring Generation Distribution Parameters: ' + str(listOffspringNumberParameters))
                        objOutput.write('\n')
    
                        listSires = objSSAnalysisOperation.method_List_ParentID_Per_Offspring_For_VirtualSubPop(pop, intSubPop, intVirtualSubPop, 'father_id', True)
                        objOutput.write('\n')
                        objOutput.write('Sire Count: ')
                        objOutput.write(str(len(listSires)))
                        objOutput.write('\n')
                        objOutput.write('Sire ID List (sorted ascending): ')
                        objOutput.write('\n')
                        objOutput.write(str(listSires))
                        objOutput.write('\n')
                        objOutput.write('Sire (sorted ascending) Offspring Count List: ')
                        objOutput.write('\n')
                        objOutput.write(str(list_Offspring_Count_Sires_Sorted))
                        objOutput.write('\n')
    
                        listDames = objSSAnalysisOperation.method_List_ParentID_Per_Offspring_For_VirtualSubPop(pop, intSubPop, intVirtualSubPop, 'mother_id', True)
                        objOutput.write('\n')
                        objOutput.write('Dame Count : ')
                        objOutput.write(str(len(listDames)))
                        objOutput.write('\n')
                        objOutput.write('Dame ID List (sorted ascending) : ')
                        objOutput.write('\n')
                        objOutput.write(str(listDames))
                        objOutput.write('\n')
                        objOutput.write('Dame (sorted ascending) Offspring Count List: ')
                        objOutput.write('\n')
                        objOutput.write(str(list_Offspring_Count_Dames_Sorted))
                        objOutput.write('\n')
    
                        listParentPairs = objSSAnalysisOperation.method_List_ParentID_Per_Sorted_ParentPair_For_VirtualSubPop(pop, intSubPop, intVirtualSubPop)
                        objOutput.write('\n')
                        objOutput.write('Parent Pair Count : ')
                        objOutput.write(str(len(listParentPairs)))
                        objOutput.write('\n')
                        objOutput.write('Parent Pair ID List : ')
                        objOutput.write('\n')
                        objOutput.write(str(listParentPairs))
                        objOutput.write('\n')
                        objOutput.write('Parent Pair Offspring Count List: ')
                        objOutput.write('\n')
                        objOutput.write(str(listPopulationOffspringTotalsByParentPair))
                        objOutput.write('\n')
                else:
                    objOutput.write('No offspring were produced')
                    objOutput.write('\n')
                    
                objOutput.write('\n')
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation VSP[' + str(intSubPop) + ',' + str(intVirtualSubPop) + '] ' +  'Offspring Totals By Parent - END  ', 120)
                objOutput.write(strMessageDelineationText)
                
                return True
            
            def method_Output_Population_Allele_Frequencies(self, pop, listOutputDestinations, listVirtualSubPop):
                '''
                Output population allele frequencies
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.method_Console_Output_Population_Allele_Frequencies(objOutput, pop, listVirtualSubPop)
                        
                        pass
                    else:
                         #write output to file
                        
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                objOutput=outputFileHandle
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                objOutput=outputFileHandle
                            
                            self.method_File_Output_Population_Allele_Frequencies(objOutput, pop, listVirtualSubPop)

                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)

            def method_Console_Output_Population_Allele_Frequencies(self, objOutput, pop, listVirtualSubPop):
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation Allele Frequencies Summary - BEGIN', 120)
                objOutput.write(strMessageDelineationText)
                objOutput.write('\n')
                
                intTotalLoci = pop.totNumLoci()

                with SSAnalysisHandler() as objSSAnalysisOperation:
                    
                    objOutput.write('\n')
                    objOutput.write('Number of loci: ' + str(intTotalLoci))
                    objOutput.write('\n')
                    
                    for listSingleVSP in listVirtualSubPop:
                        objOutput.write('VSP : ' + str(listSingleVSP))
                        objOutput.write('\n')
                    
                        listVSPAlleleFreqs = objSSAnalysisOperation.method_Statistics_On_Allele_Frequencies_For_VirtualSubPop(pop, listSingleVSP)
                        for intLocus in range (0, intTotalLoci):
                            intLeftJustify = 3
                            stringPadChar = '-'
                            stringPadString = '> '
                            stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
                            objOutput.write(stringLeftJustifyFormat.format(str(intLocus)) + stringPadString)
                            
                            intLeftJustify = 10
                            stringPadChar = ' '
                            stringPadString = '> '
                            stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
                            objOutput.write(stringLeftJustifyFormat.format(pop.locusName(intLocus)))
                            
                            intLeftJustify = 18
                            stringPadChar = ' '
                            stringPadString = '> '
                            stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
                            objOutput.write(stringLeftJustifyFormat.format('Allele Count : ' + str(len(listVSPAlleleFreqs[intLocus]))))
                            
                            objOutput.write('Allele Frequencies : ' + str(listVSPAlleleFreqs[intLocus]))
                            objOutput.write('\n')
                    
                objOutput.write('\n')
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation Allele Frequencies Summary - END  ', 120)
                objOutput.write(strMessageDelineationText)

            def method_File_Output_Population_Allele_Frequencies(self, objOutput, pop, listVirtualSubPop):
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation Allele Frequencies Summary - BEGIN', 120)
                objOutput.write(strMessageDelineationText)
                objOutput.write('\n')
                
                intTotalLoci = pop.totNumLoci()

                with SSAnalysisHandler() as objSSAnalysisOperation:
                    
                    objOutput.write('\n')
                    objOutput.write('Number of loci: ' + str(intTotalLoci))
                    objOutput.write('\n')
                    
                    for listSingleVSP in listVirtualSubPop:
                        objOutput.write('VSP : ' + str(listSingleVSP))
                        objOutput.write('\n')
                    
                        listVSPAlleleFreqs = objSSAnalysisOperation.method_Statistics_On_Allele_Frequencies_For_VirtualSubPop(pop, listSingleVSP)
                        for intLocus in range (0, intTotalLoci):
                            intLeftJustify = 3
                            stringPadChar = '-'
                            stringPadString = '> '
                            stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
                            objOutput.write(stringLeftJustifyFormat.format(str(intLocus)) + stringPadString)
                            
                            intLeftJustify = 10
                            stringPadChar = ' '
                            stringPadString = '> '
                            stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
                            objOutput.write(stringLeftJustifyFormat.format(pop.locusName(intLocus)))
                            
                            intLeftJustify = 18
                            stringPadChar = ' '
                            stringPadString = '> '
                            stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
                            objOutput.write(stringLeftJustifyFormat.format('Allele Count : ' + str(len(listVSPAlleleFreqs[intLocus]))))
                            
                            objOutput.write('Allele Frequencies : ' + str(listVSPAlleleFreqs[intLocus]))
                            objOutput.write('\n')
                    
                objOutput.write('\n')
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SharkSimOperation Allele Frequencies Summary - END  ', 120)
                objOutput.write(strMessageDelineationText)
                                            
            def methodOutput_SimuPopEnvironmentInfo(self, listOutputDestinations):
                '''
                Output simuPop run environment details
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.methodConsoleOutput_SimuPopEnvironmentInfo(objOutput)
                        pass
                    else:
                        #write output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                objOutput=outputFileHandle
                                self.methodWriteFileOutput_SimuPopEnvironmentInfo(objOutput)
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                objOutput=outputFileHandle
                                self.methodWriteFileOutput_SimuPopEnvironmentInfo(objOutput)
                            
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle, stringOutputDestination)
                           
            def method_Log_Output__SimuPopEnvironmentInfo(self, obj_Logger):
                
                
                strMessageDelineationText = self.method_Construct__MessageDelineationLine('SimSimuPopEnvironmentInfo - BEGIN ', 120)
                obj_Logger.info(strMessageDelineationText)
                dictEnvironOptions = simupop.moduleInfo()['version']
                obj_Logger.info(' Environmental Options - version: ' + str(dictEnvironOptions))
                dictEnvironOptions = simupop.moduleInfo()['revision']
                obj_Logger.info(' Environmental Options - revision: ' + str(dictEnvironOptions))
                dictEnvironOptions = simupop.moduleInfo()['optimized']
                obj_Logger.info(' Environmental Options - optimized: ' + str(dictEnvironOptions))
                dictEnvironOptions = simupop.moduleInfo()['threads']
                obj_Logger.info(' Environmental Options - threads: ' + str(dictEnvironOptions))
                dictEnvironOptions = simupop.moduleInfo()['alleleType']
                obj_Logger.info(' Environmental Options - alleleType: ' + str(dictEnvironOptions))
                dictEnvironOptions = simupop.moduleInfo()['maxAllele']
                obj_Logger.info(' Environmental Options - maxAllele: ' + str(dictEnvironOptions))
                dictEnvironOptions = simupop.moduleInfo()['compiler']
                obj_Logger.info(' Environmental Options - compiler: ' + str(dictEnvironOptions))
                dictEnvironOptions = simupop.moduleInfo()['date']
                obj_Logger.info(' Environmental Options - date: ' + str(dictEnvironOptions))
                dictEnvironOptions = simupop.moduleInfo()['python']
                obj_Logger.info(' Environmental Options - python: ' + str(dictEnvironOptions))
                dictEnvironOptions = simupop.moduleInfo()['platform']
                obj_Logger.info(' Environmental Options - platform: ' + str(dictEnvironOptions))
                dictEnvironOptions = simupop.moduleInfo()['wordsize']
                obj_Logger.info(' Environmental Options - wordsize: ' + str(dictEnvironOptions))
                dictEnvironOptions = simupop.moduleInfo()['alleleBits']
                obj_Logger.info(' Environmental Options - alleleBits: ' + str(dictEnvironOptions))
                dictEnvironOptions = simupop.moduleInfo()['maxIndex']
                obj_Logger.info(' Environmental Options - maxIndex: ' + str(dictEnvironOptions))
                dictEnvironOptions = simupop.moduleInfo()['availableRNGs']
                obj_Logger.info(' Environmental Options - availableRNGs: ')
                #obj_Logger.info(str(dictEnvironOptions))
                for value in dictEnvironOptions:
                    obj_Logger.info('       ' + str(value))
                dictEnvironOptions = simupop.moduleInfo()['debug']
                obj_Logger.info(' Environmental Options - debug: ')
                #obj_Logger.info(str(dictEnvironOptions))
                for key, value in dictEnvironOptions.items():
                    obj_Logger.info('       ' + str(key) + ' = ' + str(value))
                
                strMessageDelineationText = self.method_Construct__MessageDelineationLine('SimSimuPopEnvironmentInfo properties - END   ', 120)
                obj_Logger.info(strMessageDelineationText)

                return True
            
            def methodConsoleOutput_SimuPopEnvironmentInfo(self, objOutput):
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimSimuPopEnvironmentInfo - BEGIN ', 120)
                objOutput.write(strMessageDelineationText)
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['version']
                objOutput.write(' Environmental Options - version: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['revision']
                objOutput.write(' Environmental Options - revision: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['optimized']
                objOutput.write(' Environmental Options - optimized: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['threads']
                objOutput.write(' Environmental Options - threads: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['alleleType']
                objOutput.write(' Environmental Options - alleleType: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['maxAllele']
                objOutput.write(' Environmental Options - maxAllele: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['compiler']
                objOutput.write(' Environmental Options - compiler: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['date']
                objOutput.write(' Environmental Options - date: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['python']
                objOutput.write(' Environmental Options - python: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['platform']
                objOutput.write(' Environmental Options - platform: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['wordsize']
                objOutput.write(' Environmental Options - wordsize: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['alleleBits']
                objOutput.write(' Environmental Options - alleleBits: ' + str(dictEnvironOptions))
                #objOutput.write('\n')
                #dictEnvironOptions = simupop.moduleInfo()['maxNumSubPop']
                #objOutput.write(' Environmental Options - maxNumSubPop: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['maxIndex']
                objOutput.write(' Environmental Options - maxIndex: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['availableRNGs']
                objOutput.write(' Environmental Options - availableRNGs: ')
                #objOutput.write(str(dictEnvironOptions))
                for value in dictEnvironOptions:
                    objOutput.write('\n')
                    objOutput.write('       ' + str(value))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['debug']
                objOutput.write(' Environmental Options - debug: ')
                objOutput.write('\n')
                #objOutput.write(str(dictEnvironOptions))
                for key, value in dictEnvironOptions.items():
                    objOutput.write('\n')
                    objOutput.write('       ' + str(key) + ' = ' + str(value))
                
                objOutput.write('\n')
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimSimuPopEnvironmentInfo properties - END   ', 120)
                objOutput.write(strMessageDelineationText)

            def methodWriteFileOutput_SimuPopEnvironmentInfo(self, objOutput):
                
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimSimuPopEnvironmentInfo - BEGIN ', 120)
                objOutput.write(strMessageDelineationText)
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['version']
                objOutput.write(' Environmental Options - version: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['revision']
                objOutput.write(' Environmental Options - revision: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['optimized']
                objOutput.write(' Environmental Options - optimized: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['threads']
                objOutput.write(' Environmental Options - threads: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['alleleType']
                objOutput.write(' Environmental Options - alleleType: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['maxAllele']
                objOutput.write(' Environmental Options - maxAllele: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['compiler']
                objOutput.write(' Environmental Options - compiler: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['date']
                objOutput.write(' Environmental Options - date: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['python']
                objOutput.write(' Environmental Options - python: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['platform']
                objOutput.write(' Environmental Options - platform: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['wordsize']
                objOutput.write(' Environmental Options - wordsize: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['alleleBits']
                objOutput.write(' Environmental Options - alleleBits: ' + str(dictEnvironOptions))
                #objOutput.write('\n')
                #dictEnvironOptions = simupop.moduleInfo()['maxNumSubPop']
                #objOutput.write(' Environmental Options - maxNumSubPop: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['maxIndex']
                objOutput.write(' Environmental Options - maxIndex: ' + str(dictEnvironOptions))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['availableRNGs']
                objOutput.write(' Environmental Options - availableRNGs: ')
                #objOutput.write(str(dictEnvironOptions))
                for value in dictEnvironOptions:
                    objOutput.write('\n')
                    objOutput.write('       ' + str(value))
                objOutput.write('\n')
                dictEnvironOptions = simupop.moduleInfo()['debug']
                objOutput.write(' Environmental Options - debug: ')
                objOutput.write('\n')
                #objOutput.write(str(dictEnvironOptions))
                for key, value in dictEnvironOptions.items():
                    objOutput.write('\n')
                    objOutput.write('       ' + str(key) + ' = ' + str(value))
                
                objOutput.write('\n')
                strMessageDelineationText = self.methodConstruct_MessageDelineationLine('SimSimuPopEnvironmentInfo properties - END   ', 120)
                objOutput.write(strMessageDelineationText)
            
# ----- Ne output

            def method_Output_Sim_NE_Summary_Info(self, objSharkSimOperation, pop, boolHeader, boolFooter, listOutputDestinations, listVirtualSubPop, listLDNePCritOutput):
                '''
                Output simulation summary details
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        self.method_Console_Output_Sim_NE_Summary_Info(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, listVirtualSubPop, listLDNePCritOutput)
                        
                    else:
                        #write output to file
                        
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                objOutput=outputFileHandle
                                self.method_File_Output_Sim_NE_Summary_Info(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, listVirtualSubPop, listLDNePCritOutput)
                                
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                objOutput=outputFileHandle
                                self.method_File_Output_Sim_NE_Summary_Info(objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, listVirtualSubPop, listLDNePCritOutput)
                                
                            
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
            
            def method_Console_Output_Sim_NE_Summary_Info(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, listVirtualSubPop, listLDNePCritOutput):
                
                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('Sim Effective Population Size (NE) Summary Info - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                    objOutput.write('\n')
                else:
                    objOutput.write('\n')
                
#                intNumberVirtualSubPops = pop.numVirtualSubPop()
                
                objOutput.write('Population Size: ' + str(objSharkSimOperation.objSSParametersLocal.popnSize))
                objOutput.write('\n')
                for listSingleVSP in listVirtualSubPop:
                    objOutput.write('VSP : ' + str(listSingleVSP) + ' of size: ' + str(pop.subPopSize(listSingleVSP)))
                    #objOutput.write('\n')
                    
                    with SSAnalysisHandler() as objSSAnalysisOperation:
                        if objSharkSimOperation.objSSParametersLocal.boolReportDemographicNe:
                            listNeDemographic = objSSAnalysisOperation.method_Statistics_On_NE_Demographic_Population_Size_For_VirtualSubPop(pop, listSingleVSP)
                            listNeDemographicRounded = []
                            for intElement in listNeDemographic:
                                #listNeDemographicRounded.append(round(listNeDemographic[intElement],2))
                                listNeDemographicRounded.append(listNeDemographic[intElement])
    
                            objOutput.write('Demographic (Inbreeding) Effective Population Size (NeDI; Ne = KN-1/k-1+Vk/k only valid for isogamous monecious diploids,')
                            objOutput.write('\n')
                            objOutput.write('    self-fertilization permitted; Per Locus, Both Sexes, Crow & Denniston 1998)')
                            objOutput.write('\n')
                            objOutput.write('    NeDI: ' + str(listNeDemographicRounded))
                            objOutput.write('\n')
#                         else:
#                             objOutput.write('Demographic (Inbreeding) Effective Population Size (NeDI; Ne = KN-1/k-1+Vk/k only valid for isogamous monecious diploids,')
#                             objOutput.write('\n')
#                             objOutput.write('    self-fertilization permitted; Per Locus, Both Sexes, Crow & Denniston 1998)')
#                             objOutput.write('\n')
#                             objOutput.write('    NeDI: ' + 'OUTPUT SUPPRESSED see SSParameter.boolReportDemographicNe; ' + str(objSharkSimOperation.objSSParametersLocal.boolReportDemographicNe))
#                             objOutput.write('\n')

                        #Dont process subpop 3 as it has 0 popsize and will case an eror with Temporal NE and LDNE (for LDNE See below)
                        intSingleVSP = 0
                        if listSingleVSP !=0:
                            intSingleVSP = listSingleVSP[1]

                        if objSharkSimOperation.objSSParametersLocal.boolReportLDNe:
                            dictNeLD = objSSAnalysisOperation.method_Statistics_On_NE_LD_Population_Size_For_VirtualSubPop(pop, listSingleVSP)
                            #listLDNePCritOutput=[0.0,0.05,0.02,0.01]
                            dictRounded = OrderedDict()
                            for listItem in listLDNePCritOutput:
                                listRounded = []
                                for i in range(0,3):
                                    listRounded.append(round(dictNeLD[listItem][i],2))
                                pass
                                dictRounded[listItem] = listRounded
    
                            #for listItem in listLDNePCritOutput:
                            #    objOutput.write('LD Ne PCrit ' + str(listItem) + ' Value:' + str(round(dictNeLD[listItem][0],2)))
                            #    objOutput.write('\n')
                            #    objOutput.write('LD Ne PCrit ' + str(listItem) + ' JK Lower CI:' + str(round(dictNeLD[listItem][1],2)))
                            #    objOutput.write('\n')
                            #    objOutput.write('LD Ne PCrit ' + str(listItem) + ' JK Upper CI:' + str(round(dictNeLD[listItem][2],2)))
                            #    objOutput.write('\n')
    
                            #objOutput.write('LD Ne (LDNe; Both Sexes): ')
                            #objOutput.write('\n')
                            objOutput.write('    LDNe: ' + str(dictRounded))
                            objOutput.write('\n')
#                         else:
#                             objOutput.write('LD Ne (LDNe; Both Sexes): ')
#                             objOutput.write('\n')
#                             objOutput.write('    LDNe: ' + 'OUTPUT SUPPRESSED see SSParameter.boolReportLDNe; ' + str(objSharkSimOperation.objSSParametersLocal.boolReportLDNe))
#                             objOutput.write('\n')
                            
                        # VSP 3 give an error here
                        if intSingleVSP !=3:
                            
                            if objSharkSimOperation.objSSParametersLocal.boolReportTemporalFS_P1_Ne:
                                
                                listTemporalJROutput=['2.5% CI', 'Est.', '97.5% CI']
    
                                listNeTemporal_JR_P1 = objSSAnalysisOperation.method_Statistics_On_NE_Temporal_JordeRyman_P1_Population_Size_For_VirtualSubPop(pop, listSingleVSP)
                                orderedDictRounded = ([])
                                listDisplay = [1,0,2]
                                intCount = 0 
                                for listItem in listTemporalJROutput:
                                    orderedDictRounded.append((listItem,round(listNeTemporal_JR_P1[listDisplay[intCount]],2)))
                                    intCount += 1
                            
                                objOutput.write('Temporal JR P1 Ne (tempoFS Plan 1; Both Sexes): ' + str(orderedDictRounded))
                                objOutput.write('\n')
#                             else:
#                                 objOutput.write('Temporal JR P1 Ne (tempoFS Plan 1; Both Sexes): ' + 'OUTPUT SUPPRESSED see SSParameter.boolReportTemporalFS_P1_Ne; ' + str(objSharkSimOperation.objSSParametersLocal.boolReportTemporalFS_P1_Ne))
#                                 objOutput.write('\n')
                            
                            if objSharkSimOperation.objSSParametersLocal.boolReportTemporalFS_P2_Ne:
                                
                                listTemporalJROutput=['2.5% CI', 'Est.', '97.5% CI']
                                    
                                listNeTemporal_JR_P2 = objSSAnalysisOperation.method_Statistics_On_NE_Temporal_JordeRyman_P2_Population_Size_For_VirtualSubPop(pop, listSingleVSP)
                                orderedDictRounded = ([])
                                listDisplay = [1,0,2]
                                intCount = 0 
                                for listItem in listTemporalJROutput:
                                    orderedDictRounded.append((listItem,round(listNeTemporal_JR_P2[listDisplay[intCount]],2)))
                                    intCount += 1
                            
                                objOutput.write('Temporal JR P2 Ne (tempoFS Plan 2; Both Sexes): ' + str(orderedDictRounded))
                                objOutput.write('\n')
#                             else:
#                                 objOutput.write('Temporal JR P2 Ne (tempoFS Plan 2; Both Sexes): ' + 'OUTPUT SUPPRESSED see SSParameter.boolReportTemporalFS_P2_Ne; ' + str(objSharkSimOperation.objSSParametersLocal.boolReportTemporalFS_P2_Ne))
#                                 objOutput.write('\n')
                                                
                    #objOutput.write('\n')

                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('Sim Effective Population Size (NE) Summary Info - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    pass
                    #objOutput.write('\n')
                                
            def method_File_Output_Sim_NE_Summary_Info(self, objOutput, boolHeader, boolFooter, objSharkSimOperation, pop, listVirtualSubPop, listLDNePCritOutput):

                if boolHeader:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('Sim Effective Population Size (NE) Summary Info - BEGIN ', 120)
                    objOutput.write(strMessageDelineationText)
                    objOutput.write('\n')
                else:
                    objOutput.write('\n')
                
#                intNumberVirtualSubPops = pop.numVirtualSubPop()
                
                objOutput.write('Population Size: ' + str(objSharkSimOperation.objSSParametersLocal.popnSize))
                objOutput.write('\n')
                for listSingleVSP in listVirtualSubPop:
                    objOutput.write('VSP : ' + str(listSingleVSP))
                    objOutput.write('\n')
                    
                    with SSAnalysisHandler() as objSSAnalysisOperation:
                        if objSharkSimOperation.objSSParametersLocal.boolReportDemographicNe:
                            listNeDemographic = objSSAnalysisOperation.method_Statistics_On_NE_Demographic_Population_Size_For_VirtualSubPop(pop, listSingleVSP)
                            listRounded = []
                            for intElement in listNeDemographic:
                                listRounded.append(round(listNeDemographic[intElement],2))
                                #listRounded.append(listNeDemographic[intElement])
    
                            objOutput.write('Demographic (Inbreeding) Effective Population Size (NeDI; Ne = KN-1/k-1+Vk/k only valid for isogamous monecious diploids,')
                            objOutput.write('\n')
                            objOutput.write('    self-fertilzation permitted; Per Locus, Both Sexes)')
                            objOutput.write('\n')
                            objOutput.write('    NeDI: ' + str(listRounded))
                            objOutput.write('\n')
#                         else:
#                             objOutput.write('Demographic (Inbreeding) Effective Population Size (NeDI; Ne = KN-1/k-1+Vk/k only valid for isogamous monecious diploids,')
#                             objOutput.write('\n')
#                             objOutput.write('    self-fertilization permitted; Per Locus, Both Sexes, Crow & Denniston 1998)')
#                             objOutput.write('\n')
#                             objOutput.write('    NeDI: ' + 'OUTPUT SUPPRESSED see SSParameter.boolReportDemographicNE_Ne; ' + str(objSharkSimOperation.objSSParametersLocal.boolReportDemographicNe))
#                             objOutput.write('\n')

                        if objSharkSimOperation.objSSParametersLocal.boolReportLDNe:
                            dictNeLD = objSSAnalysisOperation.method_Statistics_On_NE_LD_Population_Size_For_VirtualSubPop(pop, listSingleVSP)
                            #listLDNePCritOutput=[0.0,0.05,0.02,0.01]
                            dictRounded = OrderedDict()
                            for listItem in listLDNePCritOutput:
                                listRounded = []
                                for i in range(0,3):
                                    listRounded.append(round(dictNeLD[listItem][i],2))
                                pass
                                dictRounded[listItem] = listRounded
    
                            #for listItem in listLDNePCritOutput:
                            #    objOutput.write('LD Ne PCrit ' + str(listItem) + ' Value:' + str(round(dictNeLD[listItem][0],2)))
                            #    objOutput.write('\n')
                            #    objOutput.write('LD Ne PCrit ' + str(listItem) + ' JK Lower CI:' + str(round(dictNeLD[listItem][1],2)))
                            #    objOutput.write('\n')
                            #    objOutput.write('LD Ne PCrit ' + str(listItem) + ' JK Upper CI:' + str(round(dictNeLD[listItem][2],2)))
                            #    objOutput.write('\n')
    
                            objOutput.write('LD Ne (LDNe; Both Sexes): ')
                            objOutput.write('\n')
                            objOutput.write('    LDNe: ' + str(dictRounded))
                            objOutput.write('\n')
#                         else:
#                             objOutput.write('LD Ne (LDNe; Both Sexes): ')
#                             objOutput.write('\n')
#                             objOutput.write('    LDNe: ' + 'OUTPUT SUPPRESSED see SSParameter.boolReportLDNe; ' + str(objSharkSimOperation.objSSParametersLocal.boolReportLDNe))
#                             objOutput.write('\n')
                            
                        #Dont process subpop 3 as it has 0 popsize and will case an eror with Temporal NE
                        intSingleVSP = 0
                        if listSingleVSP !=0:
                            intSingleVSP = listSingleVSP[1]

                        if intSingleVSP !=3:
                            if objSharkSimOperation.objSSParametersLocal.boolReportTemporalFS_P1_Ne:
                                
                                listTemporalJROutput=['2.5% CI', 'Est.', '97.5% CI']
    
                                listNeTemporal_JR_P1 = objSSAnalysisOperation.method_Statistics_On_NE_Temporal_JordeRyman_P1_Population_Size_For_VirtualSubPop(pop, listSingleVSP)
                                orderedDictRounded = ([])
                                listDisplay = [1,0,2]
                                intCount = 0 
                                for listItem in listTemporalJROutput:
                                    orderedDictRounded.append((listItem,round(listNeTemporal_JR_P1[listDisplay[intCount]],2)))
                                    intCount += 1
                            
                                objOutput.write('Temporal JR P1 Ne (tempoFS Plan 1; Both Sexes): ' + str(orderedDictRounded))
                                objOutput.write('\n')
#                             else:
#                                 objOutput.write('Temporal JR P1 Ne (tempoFS Plan 1; Both Sexes): ' + 'OUTPUT SUPPRESSED see SSParameter.boolReportTemporalFS_P1_Ne; ' + str(objSharkSimOperation.objSSParametersLocal.boolReportTemporalFS_P1_Ne))
#                                 objOutput.write('\n')
                                
                            if objSharkSimOperation.objSSParametersLocal.boolReportTemporalFS_P2_Ne:
                                    
                                listTemporalJROutput=['2.5% CI', 'Est.', '97.5% CI']
                                
                                listNeTemporal_JR_P2 = objSSAnalysisOperation.method_Statistics_On_NE_Temporal_JordeRyman_P2_Population_Size_For_VirtualSubPop(pop, listSingleVSP)
                                orderedDictRounded = ([])
                                listDisplay = [1,0,2]
                                intCount = 0 
                                for listItem in listTemporalJROutput:
                                    orderedDictRounded.append((listItem,round(listNeTemporal_JR_P2[listDisplay[intCount]],2)))
                                    intCount += 1
                            
                                objOutput.write('Temporal JR P2 Ne (tempoFS Plan 2; Both Sexes): ' + str(orderedDictRounded))
                                objOutput.write('\n')
#                             else:
#                                 objOutput.write('Temporal JR P2 Ne (tempoFS Plan 2; Both Sexes): ' + 'OUTPUT SUPPRESSED see SSParameter.boolReportTemporalFS_P2_Ne; ' + str(objSharkSimOperation.objSSParametersLocal.boolReportTemporalFS_P2_Ne))
#                                 objOutput.write('\n')
                                
                        #objOutput.write('\n')

                if boolFooter:
                    strMessageDelineationText = self.methodConstruct_MessageDelineationLine('Sim Effective Population Size (NE) Summary Info - END   ', 120)
                    objOutput.write(strMessageDelineationText)
                else:
                    pass
                    #objOutput.write('\n')
 
# ----- Specific Data File Output & Input

            def methodSaveFile_GENEPOP_FSTAT_By_Pop(self, pop, boolGenepopFormat, boolOutputVSPs, listVirtSubPopsToOutput, boolSaveAsOnePop, intAlleleLengthFormat ,output='', maxAllele=0, loci=[]):
                '''
                '''
                if output != '':
                    file = output
                else:
                    raise ValueError("Please specify output")
                # open file
                try:
                    f = open(file, "w")
                except IOError:
                    raise IOError("Can not open file " + file + " to write.")
                #
                # file is opened.
                #np = pop.numSubPop()
                np = len(listVirtSubPopsToOutput)
                if np > 200:
                    print("Warning: Current version (2.93) of FSTAT can not handle more than 200 samples")
                if loci == []:
                    loci = list(range(pop.totNumLoci()))
                nl = len(loci)
                if nl > 100:
                    print("Warning: Current version (2.93) of FSTAT can not handle more than 100 loci")
                if maxAllele != 0:
                    nu = maxAllele
                else:
                    nu = max(pop.genotype()) + 1
                if nu > 999:
                    print("Warning: Current version (2.93) of FSTAT can not handle more than 999 alleles at each locus")
                    print("If you used simuPOP_la library, you can specify maxAllele in population constructure")
                if nu < 10:
                    nd = 1
                elif nu < 100:
        
                    nd = 2
                elif nu < 1000:
                    nd = 3
                else: # FSTAT can not handle this now. how many digits?
                    nd = len(str(nu))

                ## DCB - Force to 3 orders of magnitude (i.e max 999 alleles per locus
                nd = 3

                # write the first line
                f.write('SharkSim generated GENEPOP file - ' + str(ntpath__basename(file)) + '\n')

                # following lines with loci name.
                for loc in loci:
                    #
                    f.write( pop.locusName(loc) +"\n");
                gs = pop.totNumLoci()
                #for sp in range(0, intSubPopIndex):

                objOutput = f
                listLoci = loci

                if boolOutputVSPs:
                    self.method_Output_All_VSPs_In_GENEPOP_FSTAT_Format(f, pop, boolGenepopFormat, listVirtSubPopsToOutput, boolSaveAsOnePop, listLoci, intAlleleLengthFormat)
                else:
                    self.method_Output_Population_In_GENEPOP_FSTAT_Format (f, pop, listLoci, boolGenepopFormat, intAlleleLengthFormat)  

                f.close()

            def method_Output_Population_In_GENEPOP_FSTAT_Format(self, objOutput, pop, listLoci, boolGenepopFormat, intAlleleLengthFormat):
                
                if boolGenepopFormat:
                    objOutput.write('POP\n') 
                else:
                    pass
                                
                for intIndividual in pop.individuals():
                    self.method_Output_An_Individuals_Alleles_By_Loci_GENEPOP_FSTAT_Format(objOutput, intIndividual, listLoci, boolGenepopFormat, intAlleleLengthFormat)
                
            def method_Output_All_VSPs_In_GENEPOP_FSTAT_Format(self, objOutput, pop, boolGenepopFormat, listVirtSubPopsToOutput, boolSaveAsOnePop, listLoci, intAlleleLengthFormat):
                
                if boolGenepopFormat:
                    objOutput.write('POP\n') 
                else:
                    pass

                for intVirtSubPopToOutput in listVirtSubPopsToOutput:
                   
                    if boolGenepopFormat: 
                        if boolSaveAsOnePop:
                            pass
                        else:
                            #Write 'POP'
                            objOutput.write('POP\n')   

                    for intIndividual in pop.individuals([0,intVirtSubPopToOutput]):

                        
                        self.method_Output_An_Individuals_Alleles_By_Loci_GENEPOP_FSTAT_Format(objOutput, intIndividual, listLoci, boolGenepopFormat, intAlleleLengthFormat)
             
            def method_Output_An_Individuals_Alleles_By_Loci_GENEPOP_FSTAT_Format(self, objOutput, intIndividual, listLoci, boolGenepopFormat, intAlleleLengthFormat):
                   
                if boolGenepopFormat:
                    objOutput.write("%d, " % (1))
                else:
                    objOutput.write("%d " % (1))

                #DEBUG ON
                #intIndividualID = intIndividual.ind_id
                #listIndividulsGenotype = list(intIndividual.genotype())
                #listIndividulsGenotype0 = list(intIndividual.genotype(0))
                #listIndividulsGenotype1 = list(intIndividual.genotype(1))
                #DEBUG OFF
                
                intShift = 1
                   
                for intLocus in listLoci:

                    '''
                    Simupops Allele object for an individuals is:
                    
                    pop.individual.allele(locus-index, ploidy, chromosome),
                                        
                    where for a diplod ploidy is either AlleleA or AlleleB.
                    For two alleles per locus AlleleA= 0 or 1 and AlleleB= 1 or 0
                      
                    e.g. for allele A at locus 1 pop.individual.allele(1,0).
                    Where locus-index=1, & ploidy=0 (equvalent to saying AlleleA),
                    and chromosome is not required as we put each locus on a separate chromosome
                    
                    '''
                                            
                    intPloidy0 = 0
                    intPloidy1 = 1

                    intAllele1 = intIndividual.allele(intLocus, intPloidy0) + intShift
                    intAllele2 = intIndividual.allele(intLocus, intPloidy1) + intShift

                    objOutput.write('%%0%dd' % intAlleleLengthFormat % intAllele1)
                    objOutput.write('%%0%dd' % intAlleleLengthFormat % intAllele2)

                    objOutput.write(' ')

                objOutput.write( "\n")

### Determine ILF output

#             def method_Output_Population_Individuals_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):
# 
#                 #Check if file is required.  No filenames listed assumes that it is NOT required.
#                 if listOutputDestinations != []:
# 
#                     self.method_Output_Population_Individuals_checked_REPLICATES_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
# 
# 
#                 else:
#                     #Output is NOT Required
#                     pass
# 
#                 pass

#             def method_Output_Population_Individuals_checked_REPLICATES_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):
#                 
#                 #Check if only specific REPLICATES are required.  None assumes that ALL ARE REQUIRED.
#                 if objSSParametersLocal.listOutputReplicates_ILF_PopulationIndividualsDump != []:
# 
#                     self.method_Output_Population_Individuals_SPECIFIC_REPLICATES_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
# 
#                 else:
#                     #Write specified VSPs for ALL GENERATIONS for ALL REPLICATES to central ILF file
#                     #SSOutputOperation.methodOutput_SimPopIndividulsDump(self.objSSParametersLocal, pop, listOutputDestinations, intSubPop, self.objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
#                         
#                     self.method_Output_Population_Individuals_ALL_REPLICATES_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
# 
#                     pass
# 
#                 pass
# 
#             def method_Output_Population_Individuals_SPECIFIC_REPLICATES_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):
# 
#                 #Process a required REPLICATE if it is the CURRENT REPLICATE
#                 for intOutputReplicate in objSSParametersLocal.listOutputReplicates_ILF_PopulationIndividualsDump:
#                     if intOutputReplicate == objSSParametersLocal.intCurrentReplicate: 
# 
#                         self.method_Output_Population_Individuals_checked_GENERATIONS_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
# 
#                         pass
#                     else:
#                         #CURRENT REPLICATE is NOT required.
#                         pass
#                 
#                 #End of REPLICATE FOR Loop
#                 pass
# 
#             def method_Output_Population_Individuals_ALL_REPLICATES_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):
# 
#                 self.method_Output_Population_Individuals_checked_GENERATIONS_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
# 
#                 pass
# 
#             def method_Output_Population_Individuals_checked_GENERATIONS_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):
# 
#                 #Check if only specific GENERATIONS are required.  None assumes that ALL ARE REQUIRED. 
#                 if objSSParametersLocal.listOutputGenerations_ILF_PopulationIndividualsDump !=[]:
#                     
#                     self.method_Output_Population_Individuals_SPECIFIC_GENERATIONS_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
#                     pass
#                 else:
#                     #Write specified VSPs for ALL GENERATIONS for specified/all REPLICATE(s) to central ILF file
#                     self.methodOutput_SimPopIndividulsDump(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
#                     
#                     pass
# 
#                 pass
# 
#             def method_Output_Population_Individuals_SPECIFIC_GENERATIONS_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):
# 
#                 #Process a required GENERATION if it is the CURRENT GENERATION
#                 for intOutputFertilisation in objSSParametersLocal.listOutputGenerations_ILF_PopulationIndividualsDump:
#                     if intOutputFertilisation == objSSParametersLocal.intCurrentTemporalFertilisation: 
#                     
#                         self.method_Output_Population_Individuals_checked_VSPs_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
# 
#                         pass
#                     else:
#                         #CURRENT GENERATION is NOT required.
#                         pass
#                 
#                 #End of GENERATION FOR Loop
#                 pass
# 
#             def method_Output_Population_Individuals_ALL_GENERATIONS_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):
# 
#                 #Write specified VSPs for ALL GENERATIONS for specified/all REPLICATE(s) to central ILF file
#                 self.methodOutput_SimPopIndividulsDump(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
# 
#                 pass
# 
#             def method_Output_Population_Individuals_checked_VSPs_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):
# 
#                 #Check if only specific VSPs are required.  None assumes that ALL ARE REQUIRED. 
#                 if objSSParametersLocal.listOutputVSPs_ILF_PopulationIndividualsDump !=[]:
#                     #Write out only the specified VSPs
# 
#                     self.method_Output_Population_Individuals_SPECIFIC_VSPs_To_Specific_ILF_Gen_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
# 
#                     pass
#                 else:
# 
#                     self.method_Output_Population_Individuals_ALL_VSPs_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
# 
#                     pass
#                                              
#                 pass
# 
#             def method_Output_Population_Individuals_SPECIFIC_VSPs_To_Specific_ILF_Gen_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):
# 
#                 listOutputDestinationsPerGen = []
#                 intCount = len(listOutputDestinations)
#                 if (listOutputDestinations[0] == 'console') & (intCount == 1):
#                         # If the list length is <= 1 then only console output is required and the filenames should not be added to the list
#                         pass
#                 else:
#                     #Add output files for specified VSPS for a specified GENERATION for a specified REPLICATE
#                     outputFileName = objSSParametersLocal.outfilePath + objSSParametersLocal.strFileNameProgramPrefix + 'ILF_individ_log_GEN_' + str(objSSParametersLocal.intCurrentTemporalFertilisation) + '_' + objSSParametersLocal.strFilenameEmbeddedFields + '_rep_' + str(objSSParametersLocal.intCurrentReplicate).zfill(3) + '.ilfg_ssim'
#                     list.append(listOutputDestinationsPerGen, outputFileName) #NOTE: Special output destinations list, not the general output generations list
# 
#                     #Write ALL VSPs for specified GENERATIONS for a specified REPLICATE to....
#                     #SPECIAL CASE: Writes to a separate file for each GENERATION and no output is written to central ILF file   
#                     self.methodOutput_SimPopIndividulsDump(objSSParametersLocal, pop, listOutputDestinationsPerGen, intSubPop, objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
#                     pass
# 
#                 pass
# 
#             def method_Output_Population_Individuals_ALL_VSPs_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):
# 
#                 intCount = len(listOutputDestinations)
#                 if (listOutputDestinations[0] == 'console') & (intCount == 1):
#                         # If the list lenght is <= 1 then only console output is required and the filenames should not be added to the list
#                         pass
#                 else:
#                     #Write ALL VSPs for a specified GENERATION for a specified REPLICATE to central ILF file    
#                     self.methodOutput_SimPopIndividulsDump(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
#                     pass
# 
#                 pass

#             '''
#             Start to output the data
#             '''
#                
#             def methodOutput_SimPopIndividulsDump(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):
#                 '''
#                 Output simulation summary details
#                 '''
#                 
#                 for stringOutputDestination in listOutputDestinations:
#                     if stringOutputDestination == 'console':
#                         #print output to screen
#                         #self.methodConsoleOutput_SimPopIndividulsDump(objSSParametersLocal, pop, intSubPop, intCurrentTemporalFertilisation)
#                         pass
#                     else:
#                         #write output to file
#                         with FileHandler() as objectFileHandler:
#                             boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
#                             if boolFileExists:
#                                 outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
# 
#                                 obj_SSSimulation = self.methodFileOutput_SimPopIndividulsDump_Prime_Sim_Level(objSSParametersLocal)
#                                 obj_SSBatch = self.methodFileOutput_SimPopIndividulsDump_Prime_Batch_Level(objSSParametersLocal)
#                                 obj_SSReplicate = self.methodFileOutput_SimPopIndividulsDump_Prime_Replicate_Level(objSSParametersLocal)
#                                 obj_SSPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_Population_Level(objSSParametersLocal, pop)
#                                 boolIncludeParentOffspringProperties = True
#                                 obj_SSVirtualSubPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Level(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties)
# 
#                                 with object_SSIndividual() as obj_SSIndividual:
#                                     obj_SSIndividual.objSSParametersLocal = objSSParametersLocal
#                                     obj_SSIndividual.pop = pop
#                                     intIndivCount = 1
#                                     obj_SSIndividual.intIndivCount = intIndivCount
#                                     for simupopIndividual in pop.individuals([0,1]):
#                                         obj_SSIndividual.method_PopulateProperties(simupopIndividual)
#                                         #Only need 1 individual for headings
#                                         break
# 
#                             else:
#                                 outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
# 
#                                 #File is being written to for the first time so write the header record
#                                 obj_SSSimulation = self.methodFileOutput_SimPopIndividulsDump_Prime_Sim_Level(objSSParametersLocal)
#                                 self.methodFileOutput_SimPopIndividulsDump_Write_Sim_Level(outputFileHandle, obj_SSSimulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
#                                 obj_SSBatch = self.methodFileOutput_SimPopIndividulsDump_Prime_Batch_Level(objSSParametersLocal)
#                                 self.methodFileOutput_SimPopIndividulsDump_Write_Batch_Level(outputFileHandle, obj_SSBatch, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
#                                 obj_SSReplicate = self.methodFileOutput_SimPopIndividulsDump_Prime_Replicate_Level(objSSParametersLocal)
#                                 self.methodFileOutput_SimPopIndividulsDump_Write_Replicate_Level(outputFileHandle, obj_SSReplicate, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
#                                 obj_SSPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_Population_Level(objSSParametersLocal, pop)
#                                 self.methodFileOutput_SimPopIndividulsDump_Write_Population_Level(outputFileHandle, obj_SSPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
#                                 boolIncludeParentOffspringProperties = True
#                                 obj_SSVirtualSubPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Level(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties)
#                                 self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Level(outputFileHandle, obj_SSVirtualSubPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, listVirtSubPopsToOutput)
# 
#                                 with object_SSIndividual() as obj_SSIndividual:
#                                     obj_SSIndividual.objSSParametersLocal = objSSParametersLocal
#                                     obj_SSIndividual.pop = pop
#                                     intIndivCount = 1
#                                     obj_SSIndividual.intIndivCount = intIndivCount
#                                     for simupopIndividual in pop.individuals([0,0]):
#                                         obj_SSIndividual.method_PopulateProperties(simupopIndividual)
#                                         #Only need 1 individual for headings
#                                         break
# 
#                                 #obj_SSIndividual = self.methodFileOutput_SimPopIndividulsDump_Prime_Individual_Level(objSSParametersLocal, pop, simupopIndividual)
#                                 self.methodFileOutput_SimPopIndividulsDump_Write_Individual_Level(outputFileHandle, obj_SSIndividual, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
# 
#                             #Write header EOL
#                             outputFileHandle.write('\n')
#                             
#                             #Now header have been written...write the details
#                             self.methodFileOutput_SimPopIndividulsDump_Write_Detail(outputFileHandle, objSSParametersLocal, obj_SSSimulation, obj_SSBatch, obj_SSReplicate, obj_SSPopulation, obj_SSVirtualSubPopulation, obj_SSIndividual, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput)
# 
# 
#                             #self.methodFileOutput_SimPopIndividulsDump(outputFileHandle, objSSParametersLocal, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
#                             #self.methodFileOutput_SimPopIndividulsPedigreeCompatibleDump(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
# 
#                             #Close the file
#                             boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
#                             pass

            def method_Output_Population_Individuals_To_ILF_Files_With_NE_Experiments(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput, listPopSubSamples, listSubSampleVSPsToOutput):
                '''
                Output simulation summary details + NE experiments consisting of sub sampled pops
                '''
 
                '''
                Prime reporting objects with their properties from the raw data
                '''
                obj_SSSimulation = self.methodFileOutput_SimPopIndividulsDump_Prime_Sim_Level(objSSParametersLocal)
                obj_SSBatch = self.methodFileOutput_SimPopIndividulsDump_Prime_Batch_Level(objSSParametersLocal)
                obj_SSReplicate = self.methodFileOutput_SimPopIndividulsDump_Prime_Replicate_Level(objSSParametersLocal)
                obj_SSPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_Population_Level(objSSParametersLocal, pop)
                boolIncludeParentOffspringProperties = True
                obj_SSVirtualSubPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Level(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties)

                #For every population sample/experiment supplied produce a VSP level object
                listExperiments = []
                for pop_sample in listPopSubSamples:
                    boolIncludeParentOffspringProperties = False
                    obj_SSVirtualSubPopulation_Experiment = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Level(objSSParametersLocal, pop_sample, listSubSampleVSPsToOutput, boolIncludeParentOffspringProperties)
                    listExperiments.append(obj_SSVirtualSubPopulation_Experiment)
                
                ''' 
                Write out keys and values to destination media
                '''
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        #self.methodConsoleOutput_SimPopIndividulsDump(objSSParametersLocal, pop, intSubPop, intCurrentTemporalFertilisation)
                        pass
                    else:
                        #write header output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                ''' No header required so set file write to append and write the data further down '''
                                pass
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                '''
                                Prime objects with their properties from the raw data
                                File is being written to for the first time so....
                                Write the reporting objects keys as header labels
                                '''
                                self.methodFileOutput_SimPopIndividulsDump_Write_Sim_Level(outputFileHandle, obj_SSSimulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                                self.methodFileOutput_SimPopIndividulsDump_Write_Batch_Level(outputFileHandle, obj_SSBatch, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                                self.methodFileOutput_SimPopIndividulsDump_Write_Replicate_Level(outputFileHandle, obj_SSReplicate, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                                self.methodFileOutput_SimPopIndividulsDump_Write_Population_Level(outputFileHandle, obj_SSPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                                
                                boolIncludeParentOffspringProperties = True
                                self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Level(outputFileHandle, obj_SSVirtualSubPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties)

                                #For every population sample/experiment supplied produce a VSP level object
                                for objExperimentData in listExperiments:
                                    boolIncludeParentOffspringProperties = False
                                    self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Level(outputFileHandle, obj_SSVirtualSubPopulation_Experiment, pop_sample, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties)

                            #Write EOL
                            outputFileHandle.write('\n')
                            
                            #Now header have been written...write the details
                            self.methodFileOutput_SimPopIndividulsDump_Write_NE_Experiment_Detail(outputFileHandle, objSSParametersLocal, obj_SSSimulation, obj_SSBatch, obj_SSReplicate, obj_SSPopulation, obj_SSVirtualSubPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput, listExperiments, listSubSampleVSPsToOutput)

                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                            pass

            def method_Output_Population_Individuals_To_ILF_Files_With_Custom_1_Reporting(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput, listPopSubSamples, listSubSampleVSPsToOutput, dictPropertiesNotSuppressed, dictOfObjectPropertiesToReport, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport):
                '''
                Output simulation summary details + NE experiments consisting of sub sampled pops
                '''
 
                '''
                Prime reporting objects with their properties from the raw data
                '''
                listHeaderValues = []
                
                strObjectName = 'objCustom_1_Reporting'
                dictObj_SSParams = AutoVivificationHandler()
                
                
                strClassNameOfReportingObjectToCreate = 'object_SSReportingCustom_2'
                dictPropertiesNotSuppressedForThisObject = {}
                dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                if boolReusePrimedTopLevelOutputObject:
                    obj_SSParams = objSSParametersLocal.objCustom_1_PrimedTopLevelOutputObject
                else:
                    obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                    objSSParametersLocal.objCustom_1_PrimedTopLevelOutputObject = obj_SSParams
                
                
                dictObj_SSParams[strObjectName] = obj_SSParams
                
                #For every population sample/experiment supplied produce a VSP level object
                listExperiments = []
                intNumberOfSubSamplesToReport = len(listPopSubSamples)
                for intSubSamplesToReport in range(0, intNumberOfSubSamplesToReport):
                    pop_sample = listPopSubSamples[intSubSamplesToReport]
                    strObjectNameToReport = 'objCustom_1_Reporting_Experiment_' + str(intSubSamplesToReport)
                    
                    dictPropertiesNotSuppressedForThisObject = {}
                    if intSubSamplesToReport > 0 and boolReuseObjectPropertiesToReport:
                        strBASEObjectNameToReport = 'objCustom_1_Reporting_Experiment_0'
                        dictPropertiesNotSuppressedToReuse = dictPropertiesNotSuppressed[strBASEObjectNameToReport]
                        dictPropertiesNotSuppressed[strObjectNameToReport] = dictPropertiesNotSuppressedToReuse
                        dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectNameToReport]
                        
                        strBASEObjectPropertiesNameToReport = '1'
                        dictOfObjectPropertiesToReportToReuse = dictOfObjectPropertiesToReport[strBASEObjectPropertiesNameToReport][strBASEObjectNameToReport]
                        dictOfObjectPropertiesToReport[str(intSubSamplesToReport+1)] = {strObjectNameToReport: dictOfObjectPropertiesToReportToReuse}
                        pass
                    else:
                        dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectNameToReport]
                    
                    #dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strBASEObjectNameToReport]
                    #strClassNameOfReportingObjectToCreate = 'object_SSReportingCustom_1'
                    boolIncludeParentOffspringProperties = False
                    obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop_sample, listSubSampleVSPsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                    #listExperiments.append(obj_SSVSP_Custom_1_Reporting_Experiment)
                    dictObj_SSParams[strObjectNameToReport] = obj_SSParams
                
                ''' 
                Write out keys and values to destination media
                '''
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        
                        '''
                        Prime objects with their properties from the raw data
                        Data is being written for the first time so....
                        Write the reporting objects keys as header labels
                        '''
                        objSSReporting = object_SSReportingObject()
                        objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                        objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
#                         #TESTING_ON
#                         self.test_method_AgeNeReporting(objSSParametersLocal)
#                         #TESTING_OFF
                        
                        listHeaderValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting)

                        #Now header have been written...write the details
                        listDetailValues = []
                        listDetailValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting)
                        
                        #Format and send output to console
                        dictHeaderAndValues = self.method_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                        self.methodConsoleOutput_Header(objOutput, dictHeaderAndValues, boolOutputHeader)
                        pass
                    else:
                        #write header output to file
                        with FileHandler() as objectFileHandler:
                            outputFileHandle = ''
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            if boolOutputHeader == False:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                ''' No header required so set file write to append and write the data further down '''
                                objSSReporting = object_SSReportingObject()
                                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                                objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
                                pass
                            else:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                
                                '''
                                Prime objects with their properties from the raw data
                                File is being written to for the first time so....
                                Write the reporting objects keys as header labels
                                '''
                                if boolFileExists:
                                    #Write EOL
                                    outputFileHandle.write('\n\n')
                                
                                objSSReporting = object_SSReportingObject()
                                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                                objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
                                self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting)

                            #Write EOL
                            outputFileHandle.write('\n')
                            
                            #Now header have been written...write the details
                            self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting)

                            #Write EOL
                            #outputFileHandle.write('\n')
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                            pass
                        
            def method_Output_Population_Individuals_To_ILF_Files_With_Custom_2_Reporting(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput, listPopSubSamples, listSubSampleVSPsToOutput, dictPropertiesNotSuppressed, dictOfObjectPropertiesToReport, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport):
                '''
                Output simulation summary details + NE experiments consisting of sub sampled pops
                '''
 
                '''
                Prime reporting objects with their properties from the raw data
                '''
                listHeaderValues = []
                dictObj_SSParams = AutoVivificationHandler()
                
                strObjectName = 'objSSSimulation'
                strClassNameOfReportingObjectToCreate = 'object_SSSimulation'
                dictPropertiesNotSuppressedForThisObject = {}
                dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                
                dictObj_SSParams[strObjectName] = obj_SSParams
                  
                objSSReporting = object_SSReportingObject()
                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                objSSReporting.method_GetListOfReportingPropertys_From_Dict()
                
#                 for listObjectPropertyToReport in dictOfObjectPropertiesToReport[strClassNameOfReportingObjectToCreate]:
#                     intCount = 0
#                     for strPropertyName in listObjectPropertyToReport:
#                         objReportingProperty =  objSSReporting.List_Of_Object_Properties_To_Output[intCount]
                        
                for objReportingProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                    strPropertyName = objReportingProperty.Property_Name
                    obj_SSParams.dictReportingPropertyObjects[strPropertyName] = objReportingProperty
                 
                
                
                
                strObjectName = 'objCustom_2_Reporting'
                strClassNameOfReportingObjectToCreate = 'object_SSReportingCustom_2'
                dictPropertiesNotSuppressedForThisObject = {}
                dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                if boolReusePrimedTopLevelOutputObject:
                    obj_SSParams = objSSParametersLocal.objCustom_2_PrimedTopLevelOutputObject
                else:
                    obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                    objSSParametersLocal.objCustom_2_PrimedTopLevelOutputObject = obj_SSParams
                dictObj_SSParams[strObjectName] = obj_SSParams
                
                #For every population sample/experiment supplied produce a VSP level object
                listExperiments = []
                intNumberOfSubSamplesToReport = len(listPopSubSamples)
                for intSubSamplesToReport in range(0, intNumberOfSubSamplesToReport):
                    pop_sample = listPopSubSamples[intSubSamplesToReport]
                    strObjectNameToReport = 'objCustom_2_Reporting_Experiment_' + str(intSubSamplesToReport)
                    
                    dictPropertiesNotSuppressedForThisObject = {}
                    if intSubSamplesToReport > 0 and boolReuseObjectPropertiesToReport:
                        strBASEObjectNameToReport = 'objCustom_2_Reporting_Experiment_0'
                        dictPropertiesNotSuppressedToReuse = dictPropertiesNotSuppressed[strBASEObjectNameToReport]
                        dictPropertiesNotSuppressed[strObjectNameToReport] = dictPropertiesNotSuppressedToReuse
                        dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectNameToReport]
                        
                        strBASEObjectPropertiesNameToReport = '1'
                        dictOfObjectPropertiesToReportToReuse = dictOfObjectPropertiesToReport[strBASEObjectPropertiesNameToReport][strBASEObjectNameToReport]
                        dictOfObjectPropertiesToReport[str(intSubSamplesToReport+1)] = {strObjectNameToReport: dictOfObjectPropertiesToReportToReuse}
                        pass
                    else:
                        dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectNameToReport]
                    
                    #dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strBASEObjectNameToReport]
                    #strClassNameOfReportingObjectToCreate = 'object_SSReportingCustom_1'
                    boolIncludeParentOffspringProperties = False
                    obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop_sample, listSubSampleVSPsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                    #listExperiments.append(obj_SSVSP_Custom_1_Reporting_Experiment)
                    dictObj_SSParams[strObjectNameToReport] = obj_SSParams
                
                ''' 
                Write out keys and values to destination media
                '''
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        
                        '''
                        Prime objects with their properties from the raw data
                        Data is being written for the first time so....
                        Write the reporting objects keys as header labels
                        '''
                        objSSReporting = object_SSReportingObject()
                        objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                        objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
#                         #TESTING_ON
#                         self.test_method_AgeNeReporting(objSSParametersLocal)
#                         #TESTING_OFF
                        
                        listHeaderValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting)

                        #Now header have been written...write the details
                        listDetailValues = []
                        listDetailValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting)
                        
                        #Format and send output to console
                        dictHeaderAndValues = self.method_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                        self.methodConsoleOutput_Header(objOutput, dictHeaderAndValues, boolOutputHeader)
                        pass
                    else:
                        #write header output to file
                        with FileHandler() as objectFileHandler:
                            outputFileHandle = ''
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                boolOutputHeader = False
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            if boolOutputHeader == False:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                ''' No header required so set file write to append and write the data further down '''
                                objSSReporting = object_SSReportingObject()
                                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                                objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
                                pass
                            else:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                
                                '''
                                Prime objects with their properties from the raw data
                                File is being written to for the first time so....
                                Write the reporting objects keys as header labels
                                '''
                                if boolFileExists:
                                    #Write EOL
                                    outputFileHandle.write('\n\n')
                                
                                objSSReporting = object_SSReportingObject()
                                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                                objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
                                self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting)

                            #Write EOL
                            outputFileHandle.write('\n')
                            
                            #Now header have been written...write the details
                            self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting)

                            #Write EOL
                            #outputFileHandle.write('\n')
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                            pass
            
            def method_Output_Population_Individuals_To_ILF_Files_With_Custom_3_Reporting(self, objSSParametersLocal, pop, listOutputDestinations, intCurrentTemporalFertilisation, listSubPopsToOutput, dictPropertiesNotSuppressed, dictOfObjectPropertiesToReport, boolOutputHeader):
                '''
                Output simulation summary details
                '''
 
                '''
                Prime reporting objects with their properties from the raw data
                '''
                listHeaderValues = []
                dictObj_SSParams = AutoVivificationHandler()
                intSubPop = listSubPopsToOutput[0]
                
                strObjectName = 'objSSSimulation'
                strClassNameOfReportingObjectToCreate = 'object_SSSimulation'
                dictPropertiesNotSuppressedForThisObject = {}
                dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop, listSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                obj_SSParams.boolReportLDNe = False
                
                dictObj_SSParams[strObjectName] = obj_SSParams
                  
                objSSReporting = object_SSReportingObject()
                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                objSSReporting.method_GetListOfReportingPropertys_From_Dict()
                        
                for objReportingProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                    strPropertyName = objReportingProperty.Property_Name
                    obj_SSParams.dictReportingPropertyObjects[strPropertyName] = objReportingProperty
                
                
                strObjectName = 'objSSPopulation'
                strClassNameOfReportingObjectToCreate = 'object_SSPopulation'
                dictPropertiesNotSuppressedForThisObject = {}
                dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop, listSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                
                dictObj_SSParams[strObjectName] = obj_SSParams
                  
                objSSReporting = object_SSReportingObject()
                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                objSSReporting.method_GetListOfReportingPropertys_From_Dict()
                
                for objReportingProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                    strPropertyName = objReportingProperty.Property_Name
                    obj_SSParams.dictReportingPropertyObjects[strPropertyName] = objReportingProperty
                 
                
                ''' 
                Write out keys and values to destination media
                '''
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        
                        '''
                        Prime objects with their properties from the raw data
                        Data is being written for the first time so....
                        Write the reporting objects keys as header labels
                        '''
                        objSSReporting = object_SSReportingObject()
                        objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                        objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
                        
                        listHeaderValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting)

                        #Now header have been written...write the details
                        listDetailValues = []
                        listDetailValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting)
                        
                        #Format and send output to console
                        dictHeaderAndValues = self.method_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                        self.methodConsoleOutput_Header(objOutput, dictHeaderAndValues, boolOutputHeader)
                        pass
                    else:
                        #write header output to file
                        with FileHandler() as objectFileHandler:
                            outputFileHandle = ''
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                boolOutputHeader = False
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            if boolOutputHeader == False:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                ''' No header required so set file write to append and write the data further down '''
                                objSSReporting = object_SSReportingObject()
                                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                                objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
                                pass
                            else:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                
                                '''
                                Prime objects with their properties from the raw data
                                File is being written to for the first time so....
                                Write the reporting objects keys as header labels
                                '''
                                if boolFileExists:
                                    #Write EOL
                                    outputFileHandle.write('\n\n')
                                
                                objSSReporting = object_SSReportingObject()
                                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                                objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
                                self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting)

                            #Write EOL
                            outputFileHandle.write('\n')
                            
                            #Now header have been written...write the details
                            self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting)

                            #Write EOL
                            #outputFileHandle.write('\n')
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                            pass

            def method_Output_Population_Individuals_To_ILF_Files_With_Custom_4_Reporting(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput, listPopSubSamples, listSubSampleVSPsToOutput, dictPropertiesNotSuppressed, dictOfObjectPropertiesToReport, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport):
                '''
                Output simulation summary details + NE experiments consisting of sub sampled pops
                '''
 
                '''
                Prime reporting objects with their properties from the raw data
                '''
                listHeaderValues = []
                dictObj_SSParams = AutoVivificationHandler()
                
                strObjectName = 'objSSSimulation'
                strClassNameOfReportingObjectToCreate = 'object_SSSimulation'
                dictPropertiesNotSuppressedForThisObject = {}
                dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                
                dictObj_SSParams[strObjectName] = obj_SSParams
                  
                objSSReporting = object_SSReportingObject()
                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                objSSReporting.method_GetListOfReportingPropertys_From_Dict()
                
#                 for listObjectPropertyToReport in dictOfObjectPropertiesToReport[strClassNameOfReportingObjectToCreate]:
#                     intCount = 0
#                     for strPropertyName in listObjectPropertyToReport:
#                         objReportingProperty =  objSSReporting.List_Of_Object_Properties_To_Output[intCount]
                        
                for objReportingProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                    strPropertyName = objReportingProperty.Property_Name
                    obj_SSParams.dictReportingPropertyObjects[strPropertyName] = objReportingProperty
                
                listSubPopsToOutput = [globalsSS.SP_SubPops.static_intSP_SubPop_Primary] #TEMP FIX - But makes no difference for the Population object anyway
                objSSParametersLocal.boolReportLDNe = False #TEMP_FIX
                strObjectName = 'objSSPopulation'
                strClassNameOfReportingObjectToCreate = 'object_SSPopulation'
                dictPropertiesNotSuppressedForThisObject = {}
                dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop, listSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                
                
                dictObj_SSParams[strObjectName] = obj_SSParams
                  
                objSSReporting = object_SSReportingObject()
                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                objSSReporting.method_GetListOfReportingPropertys_From_Dict()
                
                for objReportingProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                    strPropertyName = objReportingProperty.Property_Name
                    obj_SSParams.dictReportingPropertyObjects[strPropertyName] = objReportingProperty
                 
                
                
                strObjectName = 'objCustom_4_Reporting'
                strClassNameOfReportingObjectToCreate = 'object_SSReportingCustom_2'
                dictPropertiesNotSuppressedForThisObject = {}
                dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                if boolReusePrimedTopLevelOutputObject:
                    obj_SSParams = objSSParametersLocal.objCustom_4_PrimedTopLevelOutputObject
                else:
                    obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                    objSSParametersLocal.objCustom_4_PrimedTopLevelOutputObject = obj_SSParams
                dictObj_SSParams[strObjectName] = obj_SSParams
                
                #For every population sample/experiment supplied produce a VSP level object
                objSSParametersLocal.boolReportLDNe = True #TEMP FIX
                listExperiments = []
                intNumberOfSubSamplesToReport = len(listPopSubSamples)
                for intSubSamplesToReport in range(0, intNumberOfSubSamplesToReport):
                    pop_sample = listPopSubSamples[intSubSamplesToReport]
                    strObjectNameToReport = 'objCustom_4_Reporting_Experiment_' + str(intSubSamplesToReport)
                    
                    dictPropertiesNotSuppressedForThisObject = {}
                    if intSubSamplesToReport > 0 and boolReuseObjectPropertiesToReport:
                        strBASEObjectNameToReport = 'objCustom_4_Reporting_Experiment_0'
                        dictPropertiesNotSuppressedToReuse = dictPropertiesNotSuppressed[strBASEObjectNameToReport]
                        dictPropertiesNotSuppressed[strObjectNameToReport] = dictPropertiesNotSuppressedToReuse
                        dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectNameToReport]
                        
                        strBASEObjectPropertiesNameToReport = '1'
                        dictOfObjectPropertiesToReportToReuse = dictOfObjectPropertiesToReport[strBASEObjectPropertiesNameToReport][strBASEObjectNameToReport]
                        dictOfObjectPropertiesToReport[str(intSubSamplesToReport+1)] = {strObjectNameToReport: dictOfObjectPropertiesToReportToReuse}
                        pass
                    else:
                        dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectNameToReport]
                    
                    #dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strBASEObjectNameToReport]
                    #strClassNameOfReportingObjectToCreate = 'object_SSReportingCustom_1'
                    boolIncludeParentOffspringProperties = False
                    obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop_sample, listSubSampleVSPsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                    #listExperiments.append(obj_SSVSP_Custom_1_Reporting_Experiment)
                    dictObj_SSParams[strObjectNameToReport] = obj_SSParams
                
                ''' 
                Write out keys and values to destination media
                '''
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        
                        '''
                        Prime objects with their properties from the raw data
                        Data is being written for the first time so....
                        Write the reporting objects keys as header labels
                        '''
                        objSSReporting = object_SSReportingObject()
                        objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                        objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
#                         #TESTING_ON
#                         self.test_method_AgeNeReporting(objSSParametersLocal)
#                         #TESTING_OFF
                        
                        listHeaderValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting)

                        #Now header have been written...write the details
                        listDetailValues = []
                        listDetailValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting)
                        
                        #Format and send output to console
                        dictHeaderAndValues = self.method_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                        self.methodConsoleOutput_Header(objOutput, dictHeaderAndValues, boolOutputHeader)
                        pass
                    else:
                        #write header output to file
                        with FileHandler() as objectFileHandler:
                            outputFileHandle = ''
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                boolOutputHeader = False
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            if boolOutputHeader == False:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                ''' No header required so set file write to append and write the data further down '''
                                objSSReporting = object_SSReportingObject()
                                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                                objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
                                pass
                            else:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                
                                '''
                                Prime objects with their properties from the raw data
                                File is being written to for the first time so....
                                Write the reporting objects keys as header labels
                                '''
                                if boolFileExists:
                                    #Write EOL
                                    outputFileHandle.write('\n\n')
                                
                                objSSReporting = object_SSReportingObject()
                                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                                objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
                                self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting)

                            #Write EOL
                            outputFileHandle.write('\n')
                            
                            #Now header have been written...write the details
                            self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting)

                            #Write EOL
                            #outputFileHandle.write('\n')
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                            pass
            
            
            def method_Output_Population_Individuals_To_ILF_Files_With_Custom_LDNE_1_Reporting(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput,  dictPropertiesNotSuppressed, dictOfObjectPropertiesToReport, boolOutputHeader):
                '''
                Output simulation summary details + NE experiments consisting of sub sampled pops
                '''
 
                '''
                Prime reporting objects with their properties from the raw data
                '''
                listHeaderValues = []
                dictObj_SSParams = AutoVivificationHandler()
                
                strObjectName = 'objSSSimulation'
                strClassNameOfReportingObjectToCreate = 'object_SSSimulation'
                dictPropertiesNotSuppressedForThisObject = {}
                dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                
                dictObj_SSParams[strObjectName] = obj_SSParams
                  
                objSSReporting = object_SSReportingObject()
                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                objSSReporting.method_GetListOfReportingPropertys_From_Dict()
                
                for objReportingProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                    strPropertyName = objReportingProperty.Property_Name
                    obj_SSParams.dictReportingPropertyObjects[strPropertyName] = objReportingProperty
                        
                
                strObjectName = 'objCustom_LDNE_Reporting_1'
                strClassNameOfReportingObjectToCreate = 'object_SSReportingCustom_LDNE_1'
                dictPropertiesNotSuppressedForThisObject = {}
                dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                dictObj_SSParams[strObjectName] = obj_SSParams
                
                ''' 
                Write out keys and values to destination media
                '''
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        
                        '''
                        Prime objects with their properties from the raw data
                        Data is being written for the first time so....
                        Write the reporting objects keys as header labels
                        '''
                        objSSReporting = object_SSReportingObject()
                        objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                        objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
#                         #TESTING_ON
#                         self.test_method_AgeNeReporting(objSSParametersLocal)
#                         #TESTING_OFF
                        
                        listHeaderValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting)

                        #Now header have been written...write the details
                        listDetailValues = []
                        listDetailValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting)
                        
                        #Format and send output to console
                        dictHeaderAndValues = self.method_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                        self.methodConsoleOutput_Header(objOutput, dictHeaderAndValues, boolOutputHeader)
                        pass
                    else:
                        #write header output to file
                        with FileHandler() as objectFileHandler:
                            outputFileHandle = ''
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                boolOutputHeader = False
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            if boolOutputHeader == False:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                ''' No header required so set file write to append and write the data further down '''
                                objSSReporting = object_SSReportingObject()
                                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                                objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
                                pass
                            else:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                
                                '''
                                Prime objects with their properties from the raw data
                                File is being written to for the first time so....
                                Write the reporting objects keys as header labels
                                '''
                                if boolFileExists:
                                    #Write EOL
                                    outputFileHandle.write('\n\n')
                                
                                objSSReporting = object_SSReportingObject()
                                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                                objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
                                self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting)

                            #Write EOL
                            outputFileHandle.write('\n')
                            
                            #Now header have been written...write the details
                            self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting)

                            #Write EOL
                            #outputFileHandle.write('\n')
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                            pass
            
            def method_Output_Population_Individuals_To_ILF_Files_With_Custom_5_Reporting(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput, listPopSubSamples, listSubSampleVSPsToOutput, dictPropertiesNotSuppressed, dictOfObjectPropertiesToReport, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport):
                '''
                Output simulation summary details + NE experiments consisting of sub sampled pops
                '''
 
                '''
                Prime reporting objects with their properties from the raw data
                '''
                listHeaderValues = []
                dictObj_SSParams = AutoVivificationHandler()
                
                strObjectName = 'objSSSimulation'
                strClassNameOfReportingObjectToCreate = 'object_SSSimulation'
                dictPropertiesNotSuppressedForThisObject = {}
                dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                
                dictObj_SSParams[strObjectName] = obj_SSParams
                  
                objSSReporting = object_SSReportingObject()
                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                objSSReporting.method_GetListOfReportingPropertys_From_Dict()
                
#                 for listObjectPropertyToReport in dictOfObjectPropertiesToReport[strClassNameOfReportingObjectToCreate]:
#                     intCount = 0
#                     for strPropertyName in listObjectPropertyToReport:
#                         objReportingProperty =  objSSReporting.List_Of_Object_Properties_To_Output[intCount]
                        
                for objReportingProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                    strPropertyName = objReportingProperty.Property_Name
                    obj_SSParams.dictReportingPropertyObjects[strPropertyName] = objReportingProperty
                
                listSubPopsToOutput = [globalsSS.SP_SubPops.static_intSP_SubPop_Primary] #TEMP FIX
                objSSParametersLocal.boolReportLDNe = False #TEMP_FIX
                strObjectName = 'objSSPopulation'
                strClassNameOfReportingObjectToCreate = 'object_SSPopulation'
                dictPropertiesNotSuppressedForThisObject = {}
                dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop, listSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                
                
                dictObj_SSParams[strObjectName] = obj_SSParams
                  
                objSSReporting = object_SSReportingObject()
                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                objSSReporting.method_GetListOfReportingPropertys_From_Dict()
                
                for objReportingProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                    strPropertyName = objReportingProperty.Property_Name
                    obj_SSParams.dictReportingPropertyObjects[strPropertyName] = objReportingProperty
                 
                
                
                strObjectName = 'objCustom_5_Reporting'
                strClassNameOfReportingObjectToCreate = 'object_SSReportingCustom_2'
                dictPropertiesNotSuppressedForThisObject = {}
                dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                if boolReusePrimedTopLevelOutputObject:
                    obj_SSParams = objSSParametersLocal.objCustom_4_PrimedTopLevelOutputObject
                else:
                    obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                    objSSParametersLocal.objCustom_4_PrimedTopLevelOutputObject = obj_SSParams
                dictObj_SSParams[strObjectName] = obj_SSParams
                
                #For every population sample/experiment supplied produce a VSP level object
                objSSParametersLocal.boolReportLDNe = True #TEMP FIX
                listExperiments = []
                intNumberOfSubSamplesToReport = len(listPopSubSamples)
                for intSubSamplesToReport in range(0, intNumberOfSubSamplesToReport):
                    pop_sample = listPopSubSamples[intSubSamplesToReport]
                    strObjectNameToReport = 'objCustom_5_Reporting_Experiment_' + str(intSubSamplesToReport)
                    
                    dictPropertiesNotSuppressedForThisObject = {}
                    if intSubSamplesToReport > 0 and boolReuseObjectPropertiesToReport:
                        strBASEObjectNameToReport = 'objCustom_5_Reporting_Experiment_0'
                        dictPropertiesNotSuppressedToReuse = dictPropertiesNotSuppressed[strBASEObjectNameToReport]
                        dictPropertiesNotSuppressed[strObjectNameToReport] = dictPropertiesNotSuppressedToReuse
                        dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectNameToReport]
                        
                        strBASEObjectPropertiesNameToReport = '1'
                        dictOfObjectPropertiesToReportToReuse = dictOfObjectPropertiesToReport[strBASEObjectPropertiesNameToReport][strBASEObjectNameToReport]
                        dictOfObjectPropertiesToReport[str(intSubSamplesToReport+1)] = {strObjectNameToReport: dictOfObjectPropertiesToReportToReuse}
                        pass
                    else:
                        dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectNameToReport]
                    
                    #dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strBASEObjectNameToReport]
                    #strClassNameOfReportingObjectToCreate = 'object_SSReportingCustom_1'
                    boolIncludeParentOffspringProperties = False
                    obj_SSParams = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(objSSParametersLocal, pop_sample, listSubSampleVSPsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject)
                    #listExperiments.append(obj_SSVSP_Custom_1_Reporting_Experiment)
                    dictObj_SSParams[strObjectNameToReport] = obj_SSParams
                
                ''' 
                Write out keys and values to destination media
                '''
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        
                        '''
                        Prime objects with their properties from the raw data
                        Data is being written for the first time so....
                        Write the reporting objects keys as header labels
                        '''
                        objSSReporting = object_SSReportingObject()
                        objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                        objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
#                         #TESTING_ON
#                         self.test_method_AgeNeReporting(objSSParametersLocal)
#                         #TESTING_OFF
                        
                        listHeaderValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting)

                        #Now header have been written...write the details
                        listDetailValues = []
                        listDetailValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting)
                        
                        #Format and send output to console
                        dictHeaderAndValues = self.method_CombineHeaderAndValues(listHeaderValues, listDetailValues)
                        self.methodConsoleOutput_Header(objOutput, dictHeaderAndValues, boolOutputHeader)
                        pass
                    else:
                        #write header output to file
                        with FileHandler() as objectFileHandler:
                            outputFileHandle = ''
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                boolOutputHeader = False
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            if boolOutputHeader == False:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                ''' No header required so set file write to append and write the data further down '''
                                objSSReporting = object_SSReportingObject()
                                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                                objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
                                pass
                            else:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                
                                '''
                                Prime objects with their properties from the raw data
                                File is being written to for the first time so....
                                Write the reporting objects keys as header labels
                                '''
                                if boolFileExists:
                                    #Write EOL
                                    outputFileHandle.write('\n\n')
                                
                                objSSReporting = object_SSReportingObject()
                                objSSReporting.method_Initialse(dictObj_SSParams, dictOfObjectPropertiesToReport, OrderedDict([]))
                                objSSReporting.method_GetListOfReportingPropertys_Using_ExistingReportingPropertys()
                                self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting)

                            #Write EOL
                            outputFileHandle.write('\n')
                            
                            #Now header have been written...write the details
                            self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting)

                            #Write EOL
                            #outputFileHandle.write('\n')
                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                            pass
            
            
            def method_Console_Output_AgeNe_Reporting(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput, listPopSubSamples, listSubSampleVSPsToOutput, dictPropertiesNotSuppressed, dictOfObjectPropertiesToReport, boolOutputHeader):
                '''
                Output AgeNe details
                '''
 
                #TESTING_ON
                objSSReporting_Details = self.method_AgeNeReporting_Age_Specific_Details(objSSParametersLocal)
                objSSReporting_Totals = self.test_method_AgeNeReporting_Totals(objSSParametersLocal)
                #TESTING_OFF
 
                '''
                Prime reporting objects with their properties from the raw data
                '''
                
                listHeaderValues = []
                
                dictObj_SSParams = AutoVivificationHandler()
                
                ''' 
                Write out keys and values to destination media
                '''
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        
                        '''
                        Prime objects with their properties from the raw data
                        Data is being written for the first time so....
                        Write the reporting objects keys as header labels
                        '''
                        listHeaderValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_AgeNe_Reporting_Level(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, False, objSSReporting_Details)

                        #Now header have been written...write the details
                        listDetailValues = []
                        listDetailValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_AgeNe_Reporting_Level_Detail(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, False, objSSReporting_Details)
                        
                        #Format and send output to console
                        dictHeaderAndValues = self.method_CombineHeaderAndValuesForOrderedDicts(listHeaderValues, listDetailValues, 6)
                        self.methodConsoleOutput_HeaderAndValues_ForAgeNe(objOutput, dictHeaderAndValues, boolOutputHeader)
                        pass


            def method_Output_Population_Individuals_To_ILF_Files_With_AgeNe_Reporting(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation,  boolOutputHeader):
                '''
                Output AgeNe details
                '''
 
                #TESTING_ON
                objSSReporting_Details = self.method_AgeNeReporting_Age_Specific_Details(objSSParametersLocal)
                #objSSReporting_Totals = self.test_method_AgeNeReporting_Totals(objSSParametersLocal)
                #TESTING_OFF
 
                '''
                Prime reporting objects with their properties from the raw data
                '''
                
                listHeaderValues = []
                
                dictObj_SSParams = AutoVivificationHandler()
                
                ''' 
                Write out keys and values to destination media
                '''
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        
                        '''
                        Prime objects with their properties from the raw data
                        Data is being written for the first time so....
                        Write the reporting objects keys as header labels
                        '''
                        listHeaderValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_AgeNe_Reporting_Level(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, False, objSSReporting_Details)

                        #Now header have been written...write the details
                        listDetailValues = []
                        listDetailValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_AgeNe_Reporting_Level_Detail(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, False, objSSReporting_Details)
                        
                        #Format and send output to console
                        dictHeaderAndValues = self.method_CombineHeaderAndValuesForOrderedDicts(listHeaderValues, listDetailValues, 6)
                        self.methodConsoleOutput_HeaderAndValues_ForAgeNe(objOutput, dictHeaderAndValues, boolOutputHeader)
                        pass
                    else:
                        #write header output to file
                        with FileHandler() as objectFileHandler:
                            outputFileHandle = ''
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            if boolOutputHeader == False:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                ''' No header required so set file write to append and write the data further down '''
                                pass
                            else:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                
                                '''
                                Prime objects with their properties from the raw data
                                File is being written to for the first time so....
                                Write the reporting objects keys as header labels
                                '''
                                if boolFileExists:
                                    #Write EOL
                                    outputFileHandle.write('\n\n')
                                
                                self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_AgeNE_Reporting_Level(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, False, objSSReporting_Details)

                            #Write EOL
                            outputFileHandle.write('\n')
                            
                            #Now header have been written...write the details
                            self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_AgeNe_Reporting_Level_Detail(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, False, objSSReporting_Details)

                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                            pass
            
            def method_Output_Population_Individuals_To_ILF_Files_With_AgeNe_Reporting_OLD(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput, listPopSubSamples, listSubSampleVSPsToOutput, dictPropertiesNotSuppressed, dictOfObjectPropertiesToReport, boolOutputHeader):
                '''
                Output AgeNe details
                '''
 
                #TESTING_ON
                objSSReporting_Details = self.method_AgeNeReporting_Age_Specific_Details(objSSParametersLocal)
                objSSReporting_Totals = self.test_method_AgeNeReporting_Totals(objSSParametersLocal)
                #TESTING_OFF
 
                '''
                Prime reporting objects with their properties from the raw data
                '''
                
                listHeaderValues = []
                
                dictObj_SSParams = AutoVivificationHandler()
                
                ''' 
                Write out keys and values to destination media
                '''
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        objOutput=sys__stdout
                        
                        '''
                        Prime objects with their properties from the raw data
                        Data is being written for the first time so....
                        Write the reporting objects keys as header labels
                        '''
                        listHeaderValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_AgeNe_Reporting_Level(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, False, objSSReporting_Details)

                        #Now header have been written...write the details
                        listDetailValues = []
                        listDetailValues = self.methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_AgeNe_Reporting_Level_Detail(objOutput, pop, intSubPop, intCurrentTemporalFertilisation, False, objSSReporting_Details)
                        
                        #Format and send output to console
                        dictHeaderAndValues = self.method_CombineHeaderAndValuesForOrderedDicts(listHeaderValues, listDetailValues, 6)
                        self.methodConsoleOutput_HeaderAndValues_ForAgeNe(objOutput, dictHeaderAndValues, boolOutputHeader)
                        pass
                    else:
                        #write header output to file
                        with FileHandler() as objectFileHandler:
                            outputFileHandle = ''
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                            if boolOutputHeader == False:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                ''' No header required so set file write to append and write the data further down '''
                                pass
                            else:
                                #outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
                                
                                '''
                                Prime objects with their properties from the raw data
                                File is being written to for the first time so....
                                Write the reporting objects keys as header labels
                                '''
                                if boolFileExists:
                                    #Write EOL
                                    outputFileHandle.write('\n\n')
                                
                                self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_AgeNE_Reporting_Level(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, False, objSSReporting_Details)

                            #Write EOL
                            outputFileHandle.write('\n')
                            
                            #Now header have been written...write the details
                            self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_AgeNe_Reporting_Level_Detail(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, False, objSSReporting_Details)

                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                            pass
            
            '''
            Prime objects with their properties from the raw data
            '''

            def methodFileOutput_SimPopIndividulsDump_Prime_Sim_Level(self, objSSParametersLocal):

                #intLevel = 1

                with object_SSSimulation() as obj_SSSimulation:
                    obj_SSSimulation.objSSParametersLocal = objSSParametersLocal
                    obj_SSSimulation.method_PopulateProperties()

                    return obj_SSSimulation
                pass

            def methodFileOutput_SimPopIndividulsDump_Prime_Batch_Level(self, objSSParametersLocal):

                #intLevel = 2

                with object_SSBatch() as obj_SSParams:
                    obj_SSParams.objSSParametersLocal = objSSParametersLocal
                    obj_SSParams.method_PopulateProperties()

                    return obj_SSParams
                pass

            def methodFileOutput_SimPopIndividulsDump_Prime_Replicate_Level(self, objSSParametersLocal):

                with object_SSReplicate() as obj_SSParams:
                    obj_SSParams.objSSParametersLocal = objSSParametersLocal
                    obj_SSParams.method_PopulateProperties()

                    return obj_SSParams
                pass

            def methodFileOutput_SimPopIndividulsDump_Prime_Population_Level(self, objSSParametersLocal, pop):

                with object_SSPopulation() as obj_SSParams:
                    obj_SSParams.objSSParametersLocal = objSSParametersLocal
                    obj_SSParams.pop = pop
                    obj_SSParams.method_PopulateProperties()

                    return obj_SSParams
                pass

            def methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Level(self, objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties):

                with object_SSVirtualSubPop() as obj_SSParams:
                    obj_SSParams.objSSParametersLocal = objSSParametersLocal
                    obj_SSParams.pop = pop
                    obj_SSParams.listVirtSubPopsToOutput = listVirtSubPopsToOutput
                    #for intVirtualSubPop in listVirtSubPopsToOutput:
                    obj_SSParams.method_PopulateProperties(boolIncludeParentOffspringProperties)

                    return obj_SSParams
                pass

            def methodFileOutput_SimPopIndividulsDump_Prime_Individual_Level(self, objSSParametersLocal, pop, simupopIndividual, intIndivCount):
                
                with object_SSIndividual() as obj_SSParams:
                    obj_SSParams.objSSParametersLocal = objSSParametersLocal
                    obj_SSParams.pop = pop
                    obj_SSParams.intIndivCount = intIndivCount

                    obj_SSParams.method_PopulateProperties(simupopIndividual)


                    return obj_SSParams
                pass

            def methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Custom_1_Reporting_Level(self, objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject):

                #Get the Type for the passed class name so the it can be created as an object
                typeFromClassName = self.method_getClassTypeFromClassName(strClassNameOfReportingObjectToCreate)
                
                with typeFromClassName() as obj_SSParams:
                    obj_SSParams.objSSParametersLocal = objSSParametersLocal
                    obj_SSParams.pop = pop
                    obj_SSParams.listVirtSubPopsToOutput = listVirtSubPopsToOutput
                    obj_SSParams.dictPropertiesNotSuppressed = dictPropertiesNotSuppressedForThisObject

                    #for intVirtualSubPop in listVirtSubPopsToOutput:
                    if strClassNameOfReportingObjectToCreate == 'object_SSReportingCustom_2': 
                        obj_SSParams.method_PopulateProperties(boolIncludeParentOffspringProperties)
                    else:
                        obj_SSParams.method_PopulateProperties()
    
                return obj_SSParams


            def method_getClassTypeFromClassName(self, strClassName):
                
                objectModule = __import__(strClassName)
                typeFromClassName = getattr(objectModule, strClassName)        
                #objectFromClassName = typeFromClassName()
                
                return typeFromClassName 
  
            '''
            Write the labels (keys) for each object
            '''
           
            def methodFileOutput_SimPopIndividulsDump_Write_Sim_Level(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists):

                with OutputHandler() as obj_OutputOperation:

                    listKeys = list(obj_SSParams.dictDataSectionNotesLevels[obj_SSParams.intLevel].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, '')

                    listKeys = list(obj_SSParams.dictFilenameEmbeddedFields.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_SingleRun.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_BatchRunStart.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ReplicateRunStart.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_SimCurrentBatch.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_SimCurrentReplicate.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_SimPopulationSize.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_IterationsToSimulate.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_CurrentIteration.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_InitialAgesRandom.keys())
                    strKey = listKeys[0]
                            
                    listKeys = list(obj_SSParams.dict_InitialMaleSexRatio.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_MatingScheme.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_MaxAge.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_MinMatinAee.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_MaxMatingAge.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
                    
                    listKeys = list(obj_SSParams.dictPredictedBreedingPopulationSize.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
                    
                    listKeys = list(obj_SSParams.dict_MeanOffspringPerIndiv.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_MatingDistType.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_MatingDistParamList.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_NumLoci.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_NumAllelesPerLoci.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_LociAlleleFreqScheme.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_InitialLociAlleleFreqList.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    #Write EOL
                    #outputFileHandle.write('\n')
                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_Batch_Level(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists):

                with OutputHandler() as obj_OutputOperation:

                    listKeys = list(obj_SSParams.dictDataSectionNotesLevels[obj_SSParams.intLevel].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ReplicateBatches.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_CurrentReplicateBatch.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    #Write EOL
                    #outputFileHandle.write('\n')
                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_Replicate_Level(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists):

                with OutputHandler() as obj_OutputOperation:

                    listKeys = list(obj_SSParams.dictDataSectionNotesLevels[obj_SSParams.intLevel].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_Replicates.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_CurrentReplicate.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    #Write EOL
                    #outputFileHandle.write('\n')
                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_Population_Level(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists):

                with OutputHandler() as obj_OutputOperation:

                    listKeys = list(obj_SSParams.dictDataSectionNotesLevels[obj_SSParams.intLevel].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_SubPop.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_SubPopSize.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_NeDemographic.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_temporal_JR_P1_ne.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
                    
                    listKeys = list(obj_SSParams.dict_temporal_JR_P1_ne_2_5_CI.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
                    
                    listKeys = list(obj_SSParams.dict_temporal_JR_P1_ne_97_5_CI.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_temporal_JR_P2_ne.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_temporal_JR_P2_ne_2_5_CI.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_temporal_JR_P2_ne_97_5_CI.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_lwr_ci.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_upr_ci.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_05.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_05_lwr_ci.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_05_upr_ci.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_02.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_02_lwr_ci.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_02_upr_ci.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_01.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_01_lwr_ci.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_01_upr_ci.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_AlleleTotalPerLocus.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_dictAlleleInstanceCountPerLocus.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_dictAlleleFreqs.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    #Write EOL
                    #outputFileHandle.write('\n')
                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Level(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, listVirtSubPopsToOutput):

                with OutputHandler() as obj_OutputOperation:
                    #This only requires one pass to set up headings
                    #so use the heading for VSP (0,1)

                    #Prime VSP number to process
                    intVirtualSubPop = 0
                    #listValues = obj_SSParams.dict_SubPop_VSP[intVirtualSubPop].values()
                    
                    listSingleVirtualSubPop = listVirtSubPopsToOutput[0]
                    strValue = listSingleVirtualSubPop
                    intVirtualSubPop = int(re__findall( r'\,(.*?)\)', str(strValue))[0])  

                    listCurrentVSP = listSingleVirtualSubPop
                    #listSingleVirtualSubPop = listCurrentVSP[0]

                    listKeys = list(obj_SSParams.dictDataSectionNotesLevels[obj_SSParams.intLevel].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_SubPop_VSP[intVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_SubPopSize_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_NeDemographic_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_temporal_JR_P1_ne_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_temporal_JR_P1_ne_2_5_CI_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_temporal_JR_P1_ne_97_5_CI_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_temporal_JR_P2_ne_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_temporal_JR_P2_ne_2_5_CI_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_temporal_JR_P2_ne_97_5_CI_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_lwr_ci_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_upr_ci_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_05_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_05_lwr_ci_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_05_upr_ci_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_02_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_02_lwr_ci_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_02_upr_ci_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_01_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_01_lwr_ci_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_ld_ne_pcrit_0_01_upr_ci_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_AlleleTotalPerLocus_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_dictAlleleInstanceCountPerLocus_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_dictAlleleFreqs_VSP[listSingleVirtualSubPop].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    if boolIncludeParentOffspringProperties:
                        listKeys = list(obj_SSParams.dict_Num_Sire_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Mean_Offspring_Per_Sire_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Mean_Variance_Per_Sire_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
    
                        listKeys = list(obj_SSParams.dict_Num_Male_Potential_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Mean_Offspring_Per_Male_Potential_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Mean_Variance_Per_Male_Potential_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
    
    
                        listKeys = list(obj_SSParams.dict_Num_Dame_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Mean_Offspring_Per_Dame_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Mean_Variance_Per_Dame_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
    
                        listKeys = list(obj_SSParams.dict_Num_Female_Potential_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Mean_Offspring_Per_Female_Potential_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Mean_Variance_Per_Female_Potential_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
    
    
                        listKeys = list(obj_SSParams.dict_Num_Actual_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Mean_Offspring_Per_Actual_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Mean_Variance_Per_Actual_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
    
                        listKeys = list(obj_SSParams.dict_Num_Potential_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Mean_Offspring_Per_Potential_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Mean_Variance_Per_Potential_Parent[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)
    
                        listKeys = list(obj_SSParams.dict_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents[listSingleVirtualSubPop].keys())
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)


                    #Write EOL
                    #outputFileHandle.write('\n')
                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_Individual_Level(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists):

                with OutputHandler() as obj_OutputOperation:

                    listKeys = list(obj_SSParams.dictDataSectionNotesLevels[obj_SSParams.intLevel].keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_LevelIndivKey.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_Individual_ID.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_Father_ID.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_Mother_ID.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_Sex.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_Affection_not_working.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_Age.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_Birth_Generation.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    boolFirstValue=False
                    listNumLoci = list(obj_SSParams.dict_NumLoci.values())
                    for intLoci in range(0, listNumLoci[0]):
                        strKey = list(obj_SSParams.dict_Genotype[intLoci].keys())
                        strKeyAlleleA = strKey[0] + '_Allele_A'
                        strKeyAlleleB = strKey[0] + '_Allele_B'
                        #strKey = listKeys[0]
                        if boolFirstValue == False:
                            boolFirstValue = True
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKeyAlleleA,  obj_SSParams.stringDelimiter)
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKeyAlleleB,  obj_SSParams.stringDelimiter)
                        else:
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKeyAlleleA,  obj_SSParams.stringDelimiter)
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKeyAlleleB,  obj_SSParams.stringDelimiter)
 
                    #Write EOL
                    #outputFileHandle.write('\n')
                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level(self, outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting):

                with OutputHandler() as obj_OutputOperation:
                    #This only requires one pass to set up headings
                                        
                    for dictProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                    #for dictProperty in obj_SSParams.listPropertyDicts:
                        
                        if isinstance(dictProperty, dict):
                            with object_SSPropertyHandler() as objSSPropertyOperation:
                                strSuppressOutput = dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Value_Suppressed]
                                
                            if strSuppressOutput == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressedAndNotOutput:
                                #Dont write header or detail
                                pass
                            else:
                                with object_SSPropertyHandler() as objSSPropertyOperation:
                                    strDefaultLabelKey = dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Default_Label_Key]
                                    
                                strKey = dictProperty[strDefaultLabelKey]
                                obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, globalsSS.StringDelimiters.static_stringDelimiter)
                        else:
                            strSuppressOutput = dictProperty.Property_Value_Suppressed
                            if strSuppressOutput == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressedAndNotOutput:
                                #Dont write detail
                                pass
                            else:
                                strDefaultLabelKey = dictProperty.Property_Label_Default_Label_Key
                                strKey = getattr(dictProperty,strDefaultLabelKey)
                                obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, globalsSS.StringDelimiters.static_stringDelimiter)

                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_AgeNE_Reporting_Level(self, outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting):

                with OutputHandler() as obj_OutputOperation:
                    #This only requires one pass to set up headings
                                        
                    for dictProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                    #for dictProperty in obj_SSParams.listPropertyDicts:
                        
                        if isinstance(dictProperty, dict):
                            with object_SSPropertyHandler() as objSSPropertyOperation:
                                strSuppressOutput = dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Value_Suppressed]
                                
                            if strSuppressOutput == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressedAndNotOutput:
                                #Dont write header or detail
                                pass
                            else:
                                with object_SSPropertyHandler() as objSSPropertyOperation:
                                    strDefaultLabelKey = dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Default_Label_Key]
                                    
                                strKey = dictProperty[strDefaultLabelKey]
                                obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, globalsSS.StringDelimiters.static_stringDelimiter)
                        else:
                            strSuppressOutput = dictProperty.Property_Value_Suppressed
                            if strSuppressOutput == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressedAndNotOutput:
                                #Dont write detail
                                pass
                            else:
                                strDefaultLabelKey = dictProperty.Property_Label_Default_Label_Key
                                strKey = getattr(dictProperty,strDefaultLabelKey)
                                obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, globalsSS.StringDelimiters.static_stringDelimiter)

                    pass
            
            '''
            CONSOLE Header output
            '''
            def methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level(self, objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting):

                listValues = []
                
                with OutputHandler() as obj_OutputOperation:
                    #This only requires one pass to set up headings
                                        
                    for dictProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                    #for dictProperty in obj_SSParams.listPropertyDicts:
                        
                        strSuppressOutput = dictProperty.Property_Value_Suppressed
                        if strSuppressOutput == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressedAndNotOutput:
                            #Dont write detail
                            pass
                        else:
                            strDefaultLabelKey = dictProperty.Property_Label_Default_Label_Key
                            strKey = getattr(dictProperty,strDefaultLabelKey)
                            #obj_OutputOperation.method_ConsoleOutput_WriteDelimitedValue(objOutput, strKey, globalsSS.StringDelimiters.static_stringDelimiterTAB)
                            listValues.append(strKey)
                    
                
                #self.method_FormatHeader(listValues)    
                return listValues

            def methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_AgeNe_Reporting_Level(self, objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting):

                listValues = []
                
                with OutputHandler() as obj_OutputOperation:
                    #This only requires one pass to set up headings
                                        
                    for dictProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                    #for dictProperty in obj_SSParams.listPropertyDicts:
                        
                        strSuppressOutput = dictProperty.Property_Value_Suppressed
                        if strSuppressOutput == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressedAndNotOutput:
                            #Dont write detail
                            pass
                        else:
                            strDefaultLabelKey = dictProperty.Property_Label_Default_Label_Key
                            strKey = getattr(dictProperty,strDefaultLabelKey)
                            #obj_OutputOperation.method_ConsoleOutput_WriteDelimitedValue(objOutput, strKey, globalsSS.StringDelimiters.static_stringDelimiterTAB)
                            listValues.append(strKey)
                    
                
                #self.method_FormatHeader(listValues)    
                return listValues
            
            '''
            Write the objects property values
            '''


#             def methodFileOutput_SimPopIndividulsDump_Write_Detail(self, outputFileHandle, objSSParametersLocal, obj_SSSimulation, obj_SSBatch, obj_SSReplicate, obj_SSPopulation, obj_SSVirtualSubPopulation, obj_SSIndividual, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput):
# 
#                 boolPastFirstWrite = False
# 
#                 intNumberVirtualSubPops = pop.numVirtualSubPop() ### Pass as list instead
#                 
#                 #for intVirtualSubPop in range(0, intNumberVirtualSubPops): #Process from list
#                 for listCurrentVSP in listVirtSubPopsToOutput:
#                     
#                     listSingleVirtualSubPop = listCurrentVSP
# 
#                     if boolPastFirstWrite == False:
#                         intIndivCount = 1
#                         boolPastFirstWrite = True
#                     else:
#                         obj_SSVirtualSubPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Level(objSSParametersLocal, pop)
#                     
#                     intIndivCount = 0
#                     
#                     #for simupopIndividual in pop.individuals([intSubPop,intVirtualSubPop]):
#                     for simupopIndividual in pop.individuals(listSingleVirtualSubPop):
#                             
#                         intIndivCount = intIndivCount + 1
# 
#                         self.methodFileOutput_SimPopIndividulsDump_Write_Sim_Level_Detail(outputFileHandle, obj_SSSimulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
#                         self.methodFileOutput_SimPopIndividulsDump_Write_Batch_Level_Detail(outputFileHandle, obj_SSBatch, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
#                         self.methodFileOutput_SimPopIndividulsDump_Write_Replicate_Level_Detail(outputFileHandle, obj_SSReplicate, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
#                         self.methodFileOutput_SimPopIndividulsDump_Write_Population_Level_Detail(outputFileHandle, obj_SSPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
#                         boolIncludeParentOffspringProperties = True
#                         self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Level_Detail(outputFileHandle, obj_SSVirtualSubPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listSingleVirtualSubPop[1], boolIncludeParentOffspringProperties)
# 
#                         obj_SSIndividual = self.methodFileOutput_SimPopIndividulsDump_Prime_Individual_Level(objSSParametersLocal, pop, simupopIndividual, intIndivCount)
#                         self.methodFileOutput_SimPopIndividulsDump_Write_Individual_Level_Detail(outputFileHandle, obj_SSIndividual, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
# 
#                         #Write EOL
#                         outputFileHandle.write('\n')
#                     pass

            def methodFileOutput_SimPopIndividulsDump_Write_Sim_Level_Detail(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists):

                with OutputHandler() as obj_OutputOperation:

                    listValues = list(obj_SSParams.dictDataSectionNotesLevels[obj_SSParams.intLevel].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, '')

                    listValues = list(obj_SSParams.dictFilenameEmbeddedFields.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_SingleRun.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_BatchRunStart.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ReplicateRunStart.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_SimCurrentBatch.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_SimCurrentReplicate.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_SimPopulationSize.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_IterationsToSimulate.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_CurrentIteration.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_InitialAgesRandom.values())
                    strValue = str(listValues[0])
                            
                    listValues = list(obj_SSParams.dict_InitialMaleSexRatio.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_MatingScheme.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_MaxAge.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_MinMatinAee.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_MaxMatingAge.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
                    
                    listValues = list(obj_SSParams.dictPredictedBreedingPopulationSize.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
                    
                    listValues = list(obj_SSParams.dict_MeanOffspringPerIndiv.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_MatingDistType.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_MatingDistParamList.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_NumLoci.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_NumAllelesPerLoci.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_LociAlleleFreqScheme.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_InitialLociAlleleFreqList.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    #Write EOL
                    #outputFileHandle.write('\n')
                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_Batch_Level_Detail(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists):

                with OutputHandler() as obj_OutputOperation:

                    listValues = list(obj_SSParams.dictDataSectionNotesLevels[obj_SSParams.intLevel].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ReplicateBatches.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_CurrentReplicateBatch.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    #Write EOL
                    #outputFileHandle.write('\n')
                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_Replicate_Level_Detail(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists):

                with OutputHandler() as obj_OutputOperation:

                    listValues = list(obj_SSParams.dictDataSectionNotesLevels[obj_SSParams.intLevel].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_Replicates.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_CurrentReplicate.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    #Write EOL
                    #outputFileHandle.write('\n')
                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_Population_Level_Detail(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists):

                with OutputHandler() as obj_OutputOperation:

                    listValues = list(obj_SSParams.dictDataSectionNotesLevels[obj_SSParams.intLevel].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_SubPop.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_SubPopSize.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_NeDemographic.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_temporal_JR_P1_ne.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_temporal_JR_P1_ne_2_5_CI.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_temporal_JR_P1_ne_97_5_CI.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_temporal_JR_P2_ne.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_temporal_JR_P2_ne_2_5_CI.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_temporal_JR_P2_ne_97_5_CI.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_lwr_ci.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_upr_ci.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_05.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_05_lwr_ci.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_05_upr_ci.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_02.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_02_lwr_ci.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_02_upr_ci.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_01.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_01_lwr_ci.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_01_upr_ci.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_AlleleTotalPerLocus.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_dictAlleleInstanceCountPerLocus.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_dictAlleleFreqs.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    #Write EOL
                    #outputFileHandle.write('\n')
                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Level_Detail(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, intVirtualSubPop, boolIncludeParentOffspringProperties):

                with OutputHandler() as obj_OutputOperation:

                    #Prime VSP number to process
                    listCurrentVSP =[(intSubPop, intVirtualSubPop)]
                    listSingleVirtualSubPop = listCurrentVSP[0]

                    listValues = list(obj_SSParams.dictDataSectionNotesLevels[obj_SSParams.intLevel].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_SubPop_VSP[intVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_SubPopSize_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_NeDemographic_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_temporal_JR_P1_ne_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_temporal_JR_P1_ne_2_5_CI_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_temporal_JR_P1_ne_97_5_CI_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_temporal_JR_P2_ne_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_temporal_JR_P2_ne_2_5_CI_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_temporal_JR_P2_ne_97_5_CI_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_lwr_ci_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_upr_ci_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_05_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_05_lwr_ci_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_05_upr_ci_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_02_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_02_lwr_ci_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_02_upr_ci_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_01_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_01_lwr_ci_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_ld_ne_pcrit_0_01_upr_ci_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_AlleleTotalPerLocus_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_dictAlleleInstanceCountPerLocus_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_dictAlleleFreqs_VSP[listSingleVirtualSubPop].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    if boolIncludeParentOffspringProperties:
                        listValues = list(obj_SSParams.dict_Num_Sire_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Mean_Offspring_Per_Sire_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
                        
                        listValues = list(obj_SSParams.dict_Mean_Variance_Per_Sire_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
    
                        listValues = list(obj_SSParams.dict_Num_Male_Potential_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Mean_Offspring_Per_Male_Potential_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Mean_Variance_Per_Male_Potential_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
    
    
                        listValues = list(obj_SSParams.dict_Num_Dame_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Mean_Offspring_Per_Dame_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Mean_Variance_Per_Dame_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
    
                        listValues = list(obj_SSParams.dict_Num_Female_Potential_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Mean_Offspring_Per_Female_Potential_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Mean_Variance_Per_Female_Potential_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
    
    
                        listValues = list(obj_SSParams.dict_Num_Actual_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Mean_Offspring_Per_Actual_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Mean_Variance_Per_Actual_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
    
                        listValues = list(obj_SSParams.dict_Num_Potential_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Mean_Offspring_Per_Potential_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Mean_Variance_Per_Potential_Parent[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
    
                        listValues = list(obj_SSParams.dict_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents[listSingleVirtualSubPop].values())
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    #Write EOL
                    #outputFileHandle.write('\n')
                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_Individual_Level_Detail(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists):

                with OutputHandler() as obj_OutputOperation:

                    listValues = list(obj_SSParams.dictDataSectionNotesLevels[obj_SSParams.intLevel].values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_LevelIndivKey.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_Individual_ID.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_Father_ID.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_Mother_ID.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_Sex.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_Affection_not_working.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_Age.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_Birth_Generation.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    boolFirstValue=False
                    listNumLoci = list(obj_SSParams.dict_NumLoci.values())
                    for intLoci in range(0, listNumLoci[0]):
                        strAlleleA = str(list(obj_SSParams.dict_Genotype[intLoci].values())[0][0])
                        strAlleleB = str(list(obj_SSParams.dict_Genotype[intLoci].values())[0][1])
                        if boolFirstValue == False:
                            boolFirstValue = True
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strAlleleA, obj_SSParams.stringDelimiter)
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strAlleleB, obj_SSParams.stringDelimiter)
                        else:
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strAlleleA, obj_SSParams.stringDelimiter)
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strAlleleB, obj_SSParams.stringDelimiter)

                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(self, outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting):

                with OutputHandler() as obj_OutputOperation:

                    #Prime VSP number to process
                    #listCurrentVSP =[(intSubPop, intVirtualSubPop)]
                    #listSingleVirtualSubPop = listCurrentVSP[0]

                    for dictProperty in objSSReporting.List_Of_Object_Properties_To_Output:

                        if isinstance(dictProperty, dict):
                            with object_SSPropertyHandler() as objSSPropertyOperation:
                                strSuppressOutput = dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Value_Suppressed]
                                
                            if strSuppressOutput == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressedAndNotOutput:
                                #Dont write detail
                                pass
                            else:
                                with object_SSPropertyHandler() as objSSPropertyOperation:
                                    strValue = str(dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Value])
                                    
                                obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, globalsSS.StringDelimiters.static_stringDelimiter)
                        else:
                            strSuppressOutput = dictProperty.Property_Value_Suppressed
                            if strSuppressOutput == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressedAndNotOutput:
                                #Dont write detail
                                pass
                            else:
                                strValue = str(dictProperty.Property_Value)
                                obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, globalsSS.StringDelimiters.static_stringDelimiter)
                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_AgeNe_Reporting_Level_Detail(self, outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, objSSReporting):

                with OutputHandler() as obj_OutputOperation:

                    #Prime VSP number to process
                    #listCurrentVSP =[(intSubPop, intVirtualSubPop)]
                    #listSingleVirtualSubPop = listCurrentVSP[0]

                    for dictProperty in objSSReporting.List_Of_Object_Properties_To_Output:

                        if isinstance(dictProperty, dict):
                            with object_SSPropertyHandler() as objSSPropertyOperation:
                                strSuppressOutput = dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Value_Suppressed]
                                
                            if strSuppressOutput == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressedAndNotOutput:
                                #Dont write detail
                                pass
                            else:
                                with object_SSPropertyHandler() as objSSPropertyOperation:
                                    strValue = str(dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Value])
                                    
                                obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, globalsSS.StringDelimiters.static_stringDelimiter)
                        else:
                            strSuppressOutput = dictProperty.Property_Value_Suppressed
                            if strSuppressOutput == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressedAndNotOutput:
                                #Dont write detail
                                pass
                            else:
                                strValue = str(dictProperty.Property_Value)
                                obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, globalsSS.StringDelimiters.static_stringDelimiter)
                    pass



            '''
            ILF CONSOLE output
            '''
            def methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(self, objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting):

                listValues = []
                
                with OutputHandler() as obj_OutputOperation:

                    #Prime VSP number to process
                    #listCurrentVSP =[(intSubPop, intVirtualSubPop)]
                    #listSingleVirtualSubPop = listCurrentVSP[0]

                    for dictProperty in objSSReporting.List_Of_Object_Properties_To_Output:

                        strSuppressOutput = dictProperty.Property_Value_Suppressed
                        if strSuppressOutput == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressedAndNotOutput:
                            #Dont write detail
                            pass
                        else:
                            strValue = str(dictProperty.Property_Value)
                            #obj_OutputOperation.method_ConsoleOutput_WriteDelimitedValue(objOutput, strValue, globalsSS.StringDelimiters.static_stringDelimiterTAB)
                            listValues.append(strValue)
                    
                pass
                return listValues
            


            def methodConsoleOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_AgeNe_Reporting_Level_Detail(self, objOutput, pop, intSubPop, intCurrentTemporalFertilisation, boolIncludeParentOffspringProperties, objSSReporting):

                listValues = []
                
                with OutputHandler() as obj_OutputOperation:

                    #Prime VSP number to process
                    #listCurrentVSP =[(intSubPop, intVirtualSubPop)]
                    #listSingleVirtualSubPop = listCurrentVSP[0]

                    for dictProperty in objSSReporting.List_Of_Object_Properties_To_Output:

                        strSuppressOutput = dictProperty.Property_Value_Suppressed
                        if strSuppressOutput == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressedAndNotOutput:
                            #Dont write detail
                            pass
                        else:
                            #strValue = str(dictProperty.Property_Value)
                            value = dictProperty.Property_Value
                            #obj_OutputOperation.method_ConsoleOutput_WriteDelimitedValue(objOutput, strValue, globalsSS.StringDelimiters.static_stringDelimiterTAB)
                            listValues.append(value)
                    
                pass
                return listValues

            '''
            Entry point for ILF FILE output detail
            '''
            
            def methodFileOutput_SimPopIndividulsDump_Write_NE_Experiment_Detail(self, outputFileHandle, objSSParametersLocal, obj_SSSimulation, obj_SSBatch, obj_SSReplicate, obj_SSPopulation, obj_SSVirtualSubPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput, listExperiments, listSubSampleVSPsToOutput):

                boolPastFirstWrite = False

                intNumberVirtualSubPops = pop.numVirtualSubPop() ### Pass as list instead
                
                #for intVirtualSubPop in range(0, intNumberVirtualSubPops): #Process from list
                for listCurrentVSP in listVirtSubPopsToOutput:
                    
                    listSingleVirtualSubPop = listCurrentVSP

                    if boolPastFirstWrite == False:
                        intIndivCount = 1
                        boolPastFirstWrite = True
                    else:
                        obj_SSVirtualSubPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Level(objSSParametersLocal, pop)
                    
                    intIndivCount = 0
                    
                    #for simupopIndividual in pop.individuals([intSubPop,intVirtualSubPop]):
                    #Only need one record written so break after the first individual
                    for simupopIndividual in pop.individuals(listSingleVirtualSubPop):
                            
                        intIndivCount = intIndivCount + 1

                        self.methodFileOutput_SimPopIndividulsDump_Write_Sim_Level_Detail(outputFileHandle, obj_SSSimulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                        self.methodFileOutput_SimPopIndividulsDump_Write_Batch_Level_Detail(outputFileHandle, obj_SSBatch, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                        self.methodFileOutput_SimPopIndividulsDump_Write_Replicate_Level_Detail(outputFileHandle, obj_SSReplicate, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                        self.methodFileOutput_SimPopIndividulsDump_Write_Population_Level_Detail(outputFileHandle, obj_SSPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                        boolIncludeParentOffspringProperties = True
                        self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Level_Detail(outputFileHandle, obj_SSVirtualSubPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listSingleVirtualSubPop[1], boolIncludeParentOffspringProperties)

                        #obj_SSIndividual = self.methodFileOutput_SimPopIndividulsDump_Prime_Individual_Level(objSSParametersLocal, pop, simupopIndividual, intIndivCount)
                        #self.methodFileOutput_SimPopIndividulsDump_Write_Individual_Level_Detail(outputFileHandle, obj_SSIndividual, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                        
                        
                        for obj_SSVirtualSubPopulation_Experiment in listExperiments:
                            boolIncludeParentOffspringProperties = False
                            self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Level_Detail(outputFileHandle, obj_SSVirtualSubPopulation_Experiment, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listSingleVirtualSubPop[1], boolIncludeParentOffspringProperties)
                            
                        #Write EOL
                        outputFileHandle.write('\n')
                        if intIndivCount == 1:
                            break
                    pass

            def methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Detail(self, outputFileHandle, objSSParametersLocal, obj_SSVSP_Custom_1_Reporting, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput, listExperiments, listSubSampleVSPsToOutput):

                boolPastFirstWrite = False

                intNumberVirtualSubPops = pop.numVirtualSubPop() ### Pass as list instead
                
                #for intVirtualSubPop in range(0, intNumberVirtualSubPops): #Process from list
                for listCurrentVSP in listVirtSubPopsToOutput:
                    
                    listSingleVirtualSubPop = listCurrentVSP

                    if boolPastFirstWrite == False:
                        intIndivCount = 1
                        boolPastFirstWrite = True
                    else:
                        obj_SSVirtualSubPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Level(objSSParametersLocal, pop)
                    
                    intIndivCount = 0
                    
                    #for simupopIndividual in pop.individuals([intSubPop,intVirtualSubPop]):
                    #Only need one record written so break after the first individual
                    for simupopIndividual in pop.individuals(listSingleVirtualSubPop):
                            
                        intIndivCount = intIndivCount + 1

                        #self.methodFileOutput_SimPopIndividulsDump_Write_Sim_Level_Detail(outputFileHandle, obj_SSSimulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                        #self.methodFileOutput_SimPopIndividulsDump_Write_Batch_Level_Detail(outputFileHandle, obj_SSBatch, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                        #self.methodFileOutput_SimPopIndividulsDump_Write_Replicate_Level_Detail(outputFileHandle, obj_SSReplicate, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                        #self.methodFileOutput_SimPopIndividulsDump_Write_Population_Level_Detail(outputFileHandle, obj_SSPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                        boolIncludeParentOffspringProperties = True
                        self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(outputFileHandle, obj_SSVSP_Custom_1_Reporting, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listSingleVirtualSubPop[1], boolIncludeParentOffspringProperties)

                        #obj_SSIndividual = self.methodFileOutput_SimPopIndividulsDump_Prime_Individual_Level(objSSParametersLocal, pop, simupopIndividual, intIndivCount)
                        #self.methodFileOutput_SimPopIndividulsDump_Write_Individual_Level_Detail(outputFileHandle, obj_SSIndividual, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                        
                        
                        for obj_SSVSP_Custom_1_Reporting_Experiment in listExperiments:
                            boolIncludeParentOffspringProperties = False
                            self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Custom_1_Reporting_Level_Detail(outputFileHandle, obj_SSVSP_Custom_1_Reporting_Experiment, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listSingleVirtualSubPop[1], boolIncludeParentOffspringProperties)
                            
                        #Write EOL
                        outputFileHandle.write('\n')
                        if intIndivCount == 1:
                            break
                    pass

            '''
            CONSOLE Output FORMATTING
            '''
            def method_CombineHeaderAndValues(self, listHeaderValues, listDetailValues):
                
                intFloatRounding = 3
                dictHeaderAndValues = AutoVivificationHandler()
                
                intListLength = len(listHeaderValues)
                
                for intListItem in range(0, intListLength):
                    strHeader = listHeaderValues[intListItem]
                    value = listDetailValues[intListItem]
                    
                    #Determi which is larger
                    intHeaderSize = len(strHeader)
                    #intValueSize = len(strValue)
                    if isinstance(value, float):
                        intValueSize = len(str(round(value, intFloatRounding)))
                    else:
                        intValueSize = len(str(value))
                        
                    if intHeaderSize >= intValueSize:
                        intLargestSize = intHeaderSize
                    else:
                        intLargestSize = intValueSize
                    
                    dictHeaderAndValues[intListItem]['header'] = strHeader
                    dictHeaderAndValues[intListItem]['value'] = str(value)
                    dictHeaderAndValues[intListItem]['largest_size'] = intLargestSize
                
                  
                return dictHeaderAndValues

               
            def method_CombineHeaderAndValuesForOrderedDicts(self, listHeaderValues, listDetailValues, intOdictIndexMax):
                
                dictHeaderAndValues = AutoVivificationHandler()
                
                intListLength = len(listHeaderValues)
                listNewHeaderValues = []
                listNewDetailValues = []
                for intListItem in range(0, intListLength):
                    valueOdict = listDetailValues[intListItem]
                    if isinstance(valueOdict, OrderedDict):
                        listNewHeaderValues.append(listHeaderValues[intListItem]) 
                        listNewDetailValues.append(listDetailValues[intListItem]) 
                        
                listSexes = [globalsSS.SexConstants.static_stringSexMale, globalsSS.SexConstants.static_stringSexFemale]        
                
                intDictHeaderAndValuesItemCount = 0
                for strSex in listSexes:
                    
                    for intOdictIndexCount in range(1, intOdictIndexMax):
                        
                        intListLength = len(listNewHeaderValues)
                        for intListItem in range(0, intListLength):
                            
                            strHeader = listNewHeaderValues[intListItem]
                            valueOdict = listNewDetailValues[intListItem][strSex]
                            
                            #Determine which is larger
                            intHeaderSize = len(strHeader)
                            
                            intLargestSize = 0
                            intFloatRounding = 3
                            #Go through the whole dict to look for the largest lenght value
                            for key, value in valueOdict.items():
                                if isinstance(value, float):
                                    intValueSize = len(str(round(value, intFloatRounding)))
                                else:
                                    intValueSize = len(str(value))
                            
                                if intValueSize >= intLargestSize:
                                    intLargestSize = intValueSize
                            pass
                            if intHeaderSize >= intLargestSize:
                                intLargestSize = intHeaderSize
                            
                            #Format the SELCTED value
                            valueOdictValue = valueOdict[intOdictIndexCount]
                            if isinstance(valueOdictValue, float):
                                strValue = str(round(valueOdictValue, intFloatRounding))
                            else:
                                strValue = str(valueOdictValue)
                                
                            #Add header and values to reporting dict
                            intIndex = intDictHeaderAndValuesItemCount    
                            dictHeaderAndValues[intIndex]['header'] = strHeader
                            if intDictHeaderAndValuesItemCount < intListLength:
                                dictHeaderAndValues[intIndex]['display_header'] = True
                            else:
                                dictHeaderAndValues[intIndex]['display_header'] = False
                            dictHeaderAndValues[intIndex]['value'] = strValue
                            dictHeaderAndValues[intIndex]['largest_size'] = intLargestSize
                            if (intListItem == intListLength-1):
                                dictHeaderAndValues[intIndex]['EOL'] = '\n'
                            else:
                                dictHeaderAndValues[intIndex]['EOL'] = ''
                            
                            intDictHeaderAndValuesItemCount += 1
                            pass
                        pass
                    #Write EOL when sex changes
                    dictHeaderAndValues[intIndex]['EOL'] = dictHeaderAndValues[intIndex]['EOL'] + '\n'
                    pass
                pass
              
                return dictHeaderAndValues

            def methodConsoleOutput_HeaderAndValues_ForAgeNe(self, objOutput, dictHeaderAndValues, boolOutputHeader):
                
                stringPadChar = ' '
                stringPadString = ' '
                intJustifyOdd = 3
                intJustifyEven = 4
                #Get the Max Reporting Order Key
                intLastOutputOrderKey = int(max(dictHeaderAndValues.iterkeys(), key=int))
                
                if boolOutputHeader:
                    #Output the header values
                    for intOutputOrderKey in range(0, intLastOutputOrderKey+1):
                        
                        strHeader = dictHeaderAndValues[intOutputOrderKey]['header']
                        boolDisplayHeader = dictHeaderAndValues[intOutputOrderKey]['display_header']
                        intLargestSize = dictHeaderAndValues[intOutputOrderKey]['largest_size']
                        strEOL = dictHeaderAndValues[intOutputOrderKey]['EOL']
                        
                        #Is even or odd
                        intOdd = intLargestSize & 0x1
                        if intOdd == 1:
                            intLargestSize += intJustifyOdd
                        else:
                            intLargestSize += intJustifyEven
                                
    #                     if len(strHeader) == intLargestSize:
    #                         intCalculatedJustify = intLargestSize + intJustify
    #                     else:
    #                         intCalculatedJustify = ((intLargestSize - len(strHeader))/2) + intJustify
                        
                        stringFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                        
                        if boolDisplayHeader:
                            objOutput.write(stringFormat.format(strHeader) + stringPadString + strEOL)
                        
                    #objOutput.write('\n')
                
                #Now outoput the detail values    
                for intOutputOrderKey in range(0, intLastOutputOrderKey+1):
                    
                    strValue = dictHeaderAndValues[intOutputOrderKey]['value']
                    intLargestSize = dictHeaderAndValues[intOutputOrderKey]['largest_size']
                    strEOL = dictHeaderAndValues[intOutputOrderKey]['EOL']
                    
                    #Is even or odd
                    intOdd = intLargestSize & 0x1
                    if intOdd == 1:
                        intLargestSize += intJustifyOdd
                    else:
                        intLargestSize += intJustifyEven
                    
#                     if len(strValue) == intLargestSize:
#                         intCalculatedJustify = intJustify
#                     else:
#                         intCalculatedJustify = ((intLargestSize - len(strValue))/2) + intJustify
                    
                    if strValue.isdigit():
                        stringFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                    else:
                        stringFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                
                    objOutput.write(stringFormat.format(strValue) + stringPadString  + strEOL)
                
                #objOutput.write('\n')
                pass
            
            def methodConsoleOutput_Header(self, objOutput, dictHeaderAndValues, boolOutputHeader):
                
                stringPadChar = ' '
                stringPadString = ' '
                intJustifyOdd = 3
                intJustifyEven = 4
                #Get the Max Reporting Order Key
                intLastOutputOrderKey = int(max(dictHeaderAndValues.iterkeys(), key=int))
                
                if boolOutputHeader:
                    #Output the header values
                    for intOutputOrderKey in range(0, intLastOutputOrderKey+1):
                        
                        strHeader = dictHeaderAndValues[intOutputOrderKey]['header']
                        intLargestSize = dictHeaderAndValues[intOutputOrderKey]['largest_size']
                        
                        #Is even or odd
                        intOdd = intLargestSize & 0x1
                        if intOdd == 1:
                            intLargestSize += intJustifyOdd
                        else:
                            intLargestSize += intJustifyEven
                                
    #                     if len(strHeader) == intLargestSize:
    #                         intCalculatedJustify = intLargestSize + intJustify
    #                     else:
    #                         intCalculatedJustify = ((intLargestSize - len(strHeader))/2) + intJustify
                        
                        stringFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                    
                        objOutput.write(stringFormat.format(strHeader) + stringPadString)
                        
                    objOutput.write('\n')
                
                #Now outoput the detail values    
                for intOutputOrderKey in range(0, intLastOutputOrderKey+1):
                    
                    strValue = dictHeaderAndValues[intOutputOrderKey]['value']
                    intLargestSize = dictHeaderAndValues[intOutputOrderKey]['largest_size']

                    #Is even or odd
                    intOdd = intLargestSize & 0x1
                    if intOdd == 1:
                        intLargestSize += intJustifyOdd
                    else:
                        intLargestSize += intJustifyEven
                    
#                     if len(strValue) == intLargestSize:
#                         intCalculatedJustify = intJustify
#                     else:
#                         intCalculatedJustify = ((intLargestSize - len(strValue))/2) + intJustify
                    
                    if strValue.isdigit():
                        stringFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                    else:
                        stringFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                
                    objOutput.write(stringFormat.format(strValue) + stringPadString)
                
                objOutput.write('\n')
                pass

### Process Pedigree file output

            '''
            Pedigree output processing
            '''
            def methodOutput_Population_Individuals_For_Pedigree(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):
                '''
                Output simulation summary details
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        #self.methodConsoleOutput_SimPopIndividulsDump(objSSParametersLocal, pop, intSubPop, intCurrentTemporalFertilisation)
                        pass
                    else:
                        #write output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')

                                with object_SSIndividual() as obj_SSIndividual:
                                    obj_SSIndividual.objSSParametersLocal = objSSParametersLocal
                                    obj_SSIndividual.pop = pop
                                    intIndivCount = 1
                                    obj_SSIndividual.intIndivCount = intIndivCount
                                    for simupopIndividual in pop.individuals([0,1]):
                                        obj_SSIndividual.method_PopulateProperties(simupopIndividual)
                                        #Only need 1 individual for headings
                                        break

                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                                #File is being written to for the first time so write the header record
                                with object_SSIndividual() as obj_SSIndividual:
                                    obj_SSIndividual.objSSParametersLocal = objSSParametersLocal
                                    obj_SSIndividual.pop = pop
                                    intIndivCount = 1
                                    obj_SSIndividual.intIndivCount = intIndivCount
                                    for simupopIndividual in pop.individuals([0,0]):
                                        obj_SSIndividual.method_PopulateProperties(simupopIndividual)
                                        #Only need 1 individual for headings
                                        break

                                self.methodFileOutput_SimPopIndividulsDump_Write_Pedigree_Individual_Level(outputFileHandle, obj_SSIndividual, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)

                            self.methodFileOutput_Population_Individuals_For_Pedigree_Write_Detail(outputFileHandle, objSSParametersLocal, obj_SSIndividual, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput)

                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                            pass
### Write Pedigree headers

            def methodFileOutput_SimPopIndividulsDump_Write_Pedigree_Individual_Level(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists):

                #NOTE: Changing deliniter used
                obj_SSParams.stringDelimiter = ','

                with OutputHandler() as obj_OutputOperation:

                    #listKeys = obj_SSParams.dictDataSectionNotesLevels[obj_SSParams.intLevel].keys()
                    #strKey = listKeys[0]
                    #obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_Individual_ID.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, '')

                    listKeys = list(obj_SSParams.dict_Father_ID.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_Mother_ID.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_LevelIndivKey.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_Sex.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_Affection_not_working.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_Age.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    listKeys = list(obj_SSParams.dict_Age_in_months.keys())
                    strKey = listKeys[0]
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    #listKeys = obj_SSParams.dict_Birth_Generation.keys()
                    #strKey = listKeys[0]
                    strKey = 'TierInfo'
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, obj_SSParams.stringDelimiter)

                    boolFirstValue=False
                    listNumLoci = list(obj_SSParams.dict_NumLoci.values())
                    for intLoci in range(0, listNumLoci[0]):
                        strKey = list(obj_SSParams.dict_Genotype[intLoci].keys())
                        strKeyAlleleA = strKey[0] + '_Allele_A'
                        strKeyAlleleB = strKey[0] + '_Allele_B'
                        #strKey = listKeys[0]
                        if boolFirstValue == False:
                            boolFirstValue = True
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKeyAlleleA,  obj_SSParams.stringDelimiter)
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKeyAlleleB,  obj_SSParams.stringDelimiter)
                        else:
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKeyAlleleA,  obj_SSParams.stringDelimiter)
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKeyAlleleB,  obj_SSParams.stringDelimiter)
 
                    #Write EOL
                    outputFileHandle.write('\n')
                    pass

### Write Pedigree Detail

            def methodFileOutput_Population_Individuals_For_Pedigree_Write_Detail(self, outputFileHandle, objSSParametersLocal, obj_SSIndividual, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput):

                #boolPastFirstWrite = False

                #intNumberVirtualSubPops = pop.numVirtualSubPop() ### Pass as list instead
                
                ##for intVirtualSubPop in range(0, intNumberVirtualSubPops): #Process from list
                for listCurrentVSP in listVirtSubPopsToOutput:
                    
                    listSingleVirtualSubPop = listCurrentVSP

                #    if boolPastFirstWrite == False:
                #        intIndivCount = 1
                #        boolPastFirstWrite = True
                #    else:
                #        obj_SSVirtualSubPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Level(objSSParametersLocal, pop)
                    
                    intIndivCount = 0
                    
                #    #for simupopIndividual in pop.individuals([intSubPop,intVirtualSubPop]):
                    for simupopIndividual in pop.individuals(listSingleVirtualSubPop):
                    #for simupopIndividual in pop.individuals():
                            
                        intIndivCount = intIndivCount + 1

                        obj_SSIndividual = self.methodFileOutput_SimPopIndividulsDump_Prime_Individual_Level(objSSParametersLocal, pop, simupopIndividual, intIndivCount)
                        self.methodFileOutput_SimPopIndividulsDump_Write_Pedigree_Individual_Level_Detail(outputFileHandle, obj_SSIndividual, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                    pass
            
            def methodFileOutput_SimPopIndividulsDump_Write_Pedigree_Individual_Level_Detail(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists):

                #NOTE: Changing deliniter used
                obj_SSParams.stringDelimiter = ','

                with OutputHandler() as obj_OutputOperation:

                    #listValues = obj_SSParams.dictDataSectionNotesLevels[obj_SSParams.intLevel].values()
                    #strValue = str(listValues[0])
                    #obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_Individual_ID.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, '')

                    listValues = list(obj_SSParams.dict_Father_ID.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_Mother_ID.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_LevelIndivKey.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_Sex.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_Affection_not_working.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_Age.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    listValues = list(obj_SSParams.dict_Age_in_months.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)
                    
                    listValues = list(obj_SSParams.dict_Birth_Generation.values())
                    strValue = str(listValues[0])
                    obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, obj_SSParams.stringDelimiter)

                    boolFirstValue=False
                    listNumLoci = list(obj_SSParams.dict_NumLoci.values())
                    for intLoci in range(0, listNumLoci[0]):
                        strAlleleA = str(list(obj_SSParams.dict_Genotype[intLoci].values())[0][0])
                        strAlleleB = str(list(obj_SSParams.dict_Genotype[intLoci].values())[0][1])
                        if boolFirstValue == False:
                            boolFirstValue = True
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strAlleleA, obj_SSParams.stringDelimiter)
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strAlleleB, obj_SSParams.stringDelimiter)
                        else:
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strAlleleA, obj_SSParams.stringDelimiter)
                            obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strAlleleB, obj_SSParams.stringDelimiter)

                    #Write EOL
                    outputFileHandle.write('\n')
                    pass

            def loadFStat(self, file, loci=[]):
                '''load Population from fStat file 'file'
                since fStat does not have chromosome structure
                an additional parameter can be given
                '''
                try:
                    f = open(file, "r")
                except IOError:
                    raise IOError("Can not open file " + file + " to read.")
                #
                # file is opened. get basic parameters
                try:
                    # get numSubPop(), totNumLoci(), maxAllele(), digit
                    [np, nl, nu, nd] = list(map(int, f.readline().split()))
                except ValueError:
                    raise ValueError("The first line does not have 4 numbers. Are you sure this is a FSTAT file?")

                # now, ignore nl lines, if loci is empty try to see if we have info here
                # following lines with loci name.
                numLoci = loci
                lociNames = []
                if loci != []: # ignore allele name lines
                    if nl != sum(loci):
                        raise ValueError("Given number of loci does not add up to number of loci in the file")
                    for al in range(0, nl):
                        lociNames.append(f.readline().strip() )
                else:
                    scan = re__compile(r'\D*(\d+)\D*(\d+)')
                    for al in range(0, nl):
                        lociNames.append( f.readline().strip())
                        # try to parse the name ...
                        try:
                            #print "mating ", lociNames[-1]
                            ch,loc = list(map(int, scan.match(lociNames[-1]).groups()))
                            # get numbers?
                            #print ch, loc
                            if len(numLoci)+1 == ch:
                                numLoci.append( loc )
                            else:
                                numLoci[ ch-1 ] = loc
                        except Exception:
                            pass
                    # if we can not get numbers correct, put all loci in one chromosome
                    if sum(numLoci) != nl:
                        numLoci = [nl]
                #
                # now, numLoci should be valid, we need number of population
                # and subpopulations
                maxAllele = 0
                gt = []
                for line in f.readlines():
                    gt.append( line.split() )
                f.close()
                # subpop size?
                subPopIndex = [int(x[0]) for x in gt]
                # count subpop.
                subPopSize = [0]*subPopIndex[-1]
                for i in range(0, subPopIndex[-1]):
                    subPopSize[i] = subPopIndex.count(i+1)
                if len(subPopSize) != np:
                    raise ValueError("Number of subpop does not match")
                if sum(subPopSize) != len(gt):
                    raise ValueError("population size does not match")
                # we have all the information, create a population
                pop = Population(size=subPopSize, loci=numLoci, lociNames=lociNames)
                for idx, ind in enumerate(pop.individuals()):
                    for locus in range(pop.totNumLoci()):
                        for ploidy in [0,1]:
                            ind.setAllele(int(gt[idx][locus+1][ploidy])-1, idx=locus, ploidy=ploidy)
                return pop


# -------------- Class specific routines

            '''
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ILF Control Routines - Separated by role
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            '''
           
            '''
            ++++++++++++++++++++++++++++
            ORIGINAL Sim Pop Individuals Dump
            ++++++++++++++++++++++++++++
            '''
            
            ''' ENTRY POINT  - Start to define how the requested data will be grouped '''
            def method_Output_Population_Individuals_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                #Check if file is required.  No filenames listed assumes that it is NOT required.
                if listOutputDestinations != []:

                    self.method_Output_Population_Individuals_checked_REPLICATES_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)


                else:
                    #Output is NOT Required
                    pass

                pass
            
            ''' Group the requested data '''
           
            def method_Output_Population_Individuals_checked_REPLICATES_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):
                
                #Check if only specific REPLICATES are required.  None assumes that ALL ARE REQUIRED.
                if objSSParametersLocal.listOutputReplicates_ILF_PopulationIndividualsDump != []:

                    self.method_Output_Population_Individuals_SPECIFIC_REPLICATES_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)

                else:
                    #Write specified VSPs for ALL GENERATIONS for ALL REPLICATES to central ILF file
                    #SSOutputOperation.methodOutput_SimPopIndividulsDump(self.objSSParametersLocal, pop, listOutputDestinations, intSubPop, self.objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
                        
                    self.method_Output_Population_Individuals_ALL_REPLICATES_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)

                    pass

                pass

            def method_Output_Population_Individuals_SPECIFIC_REPLICATES_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                #Process a required REPLICATE if it is the CURRENT REPLICATE
                for intOutputReplicate in objSSParametersLocal.listOutputReplicates_ILF_PopulationIndividualsDump:
                    if intOutputReplicate == objSSParametersLocal.intCurrentReplicate: 

                        self.method_Output_Population_Individuals_checked_GENERATIONS_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)

                        pass
                    else:
                        #CURRENT REPLICATE is NOT required.
                        pass
                
                #End of REPLICATE FOR Loop
                pass

            def method_Output_Population_Individuals_ALL_REPLICATES_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                self.method_Output_Population_Individuals_checked_GENERATIONS_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)

                pass

            def method_Output_Population_Individuals_checked_GENERATIONS_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                #Check if only specific GENERATIONS are required.  None assumes that ALL ARE REQUIRED. 
                if objSSParametersLocal.listOutputGenerations_ILF_PopulationIndividualsDump !=[]:
                    
                    self.method_Output_Population_Individuals_SPECIFIC_GENERATIONS_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
                    pass
                else:
                    #Write specified VSPs for ALL GENERATIONS for specified/all REPLICATE(s) to central ILF file
                    self.methodOutput_SimPopIndividulsDump(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
                    
                    pass

                pass

            def method_Output_Population_Individuals_SPECIFIC_GENERATIONS_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                #Process a required GENERATION if it is the CURRENT GENERATION
                for intOutputFertilisation in objSSParametersLocal.listOutputGenerations_ILF_PopulationIndividualsDump:
                    if intOutputFertilisation == objSSParametersLocal.intCurrentTemporalFertilisation: 
                    
                        self.method_Output_Population_Individuals_checked_VSPs_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)

                        pass
                    else:
                        #CURRENT GENERATION is NOT required.
                        pass
                
                #End of GENERATION FOR Loop
                pass

            def method_Output_Population_Individuals_ALL_GENERATIONS_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                #Write specified VSPs for ALL GENERATIONS for specified/all REPLICATE(s) to central ILF file
                self.methodOutput_SimPopIndividulsDump(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)

                pass

            def method_Output_Population_Individuals_checked_VSPs_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                #Check if only specific VSPs are required.  None assumes that ALL ARE REQUIRED. 
                if objSSParametersLocal.listOutputVSPs_ILF_PopulationIndividualsDump !=[]:
                    #Write out only the specified VSPs

                    self.method_Output_Population_Individuals_SPECIFIC_VSPs_To_Specific_ILF_Gen_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)

                    pass
                else:

                    self.method_Output_Population_Individuals_ALL_VSPs_To_ILF_Files(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)

                    pass
                                             
                pass

            def method_Output_Population_Individuals_SPECIFIC_VSPs_To_Specific_ILF_Gen_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                listOutputDestinationsPerGen = []
                intCount = len(listOutputDestinations)
                if (listOutputDestinations[0] == 'console') & (intCount == 1):
                        # If the list length is <= 1 then only console output is required and the filenames should not be added to the list
                        pass
                else:
                    #Add output files for specified VSPS for a specified GENERATION for a specified REPLICATE
                    outputFileName = objSSParametersLocal.outfilePath + objSSParametersLocal.strFileNameProgramPrefix + 'ILF_individ_log_GEN_' + str(objSSParametersLocal.intCurrentTemporalFertilisation) + '_' + objSSParametersLocal.strFilenameEmbeddedFields + '_rep_' + str(objSSParametersLocal.intCurrentReplicate).zfill(3) + '.ilfg_ssim'
                    list.append(listOutputDestinationsPerGen, outputFileName) #NOTE: Special output destinations list, not the general output generations list

                    #Write ALL VSPs for specified GENERATIONS for a specified REPLICATE to....
                    #SPECIAL CASE: Writes to a separate file for each GENERATION and no output is written to central ILF file   
                    self.methodOutput_SimPopIndividulsDump(objSSParametersLocal, pop, listOutputDestinationsPerGen, intSubPop, objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
                    pass

                pass

            def method_Output_Population_Individuals_ALL_VSPs_To_ILF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                intCount = len(listOutputDestinations)
                if (listOutputDestinations[0] == 'console') & (intCount == 1):
                        # If the list lenght is <= 1 then only console output is required and the filenames should not be added to the list
                        pass
                else:
                    #Write ALL VSPs for a specified GENERATION for a specified REPLICATE to central ILF file    
                    self.methodOutput_SimPopIndividulsDump(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
                    pass

                pass                        

            ''' Start to output the data '''
               
            def methodOutput_SimPopIndividulsDump(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):
                '''
                Output simulation summary details
                '''
                
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        #self.methodConsoleOutput_SimPopIndividulsDump(objSSParametersLocal, pop, intSubPop, intCurrentTemporalFertilisation)
                        pass
                    else:
                        #write output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')

                                obj_SSSimulation = self.methodFileOutput_SimPopIndividulsDump_Prime_Sim_Level(objSSParametersLocal)
                                obj_SSBatch = self.methodFileOutput_SimPopIndividulsDump_Prime_Batch_Level(objSSParametersLocal)
                                obj_SSReplicate = self.methodFileOutput_SimPopIndividulsDump_Prime_Replicate_Level(objSSParametersLocal)
                                obj_SSPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_Population_Level(objSSParametersLocal, pop)
                                boolIncludeParentOffspringProperties = True
                                obj_SSVirtualSubPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Level(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties)

                                with object_SSIndividual() as obj_SSIndividual:
                                    obj_SSIndividual.objSSParametersLocal = objSSParametersLocal
                                    obj_SSIndividual.pop = pop
                                    intIndivCount = 1
                                    obj_SSIndividual.intIndivCount = intIndivCount
                                    for simupopIndividual in pop.individuals([0,1]):
                                        obj_SSIndividual.method_PopulateProperties(simupopIndividual)
                                        #Only need 1 individual for headings
                                        break

                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                                #File is being written to for the first time so write the header record
                                obj_SSSimulation = self.methodFileOutput_SimPopIndividulsDump_Prime_Sim_Level(objSSParametersLocal)
                                self.methodFileOutput_SimPopIndividulsDump_Write_Sim_Level(outputFileHandle, obj_SSSimulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                                obj_SSBatch = self.methodFileOutput_SimPopIndividulsDump_Prime_Batch_Level(objSSParametersLocal)
                                self.methodFileOutput_SimPopIndividulsDump_Write_Batch_Level(outputFileHandle, obj_SSBatch, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                                obj_SSReplicate = self.methodFileOutput_SimPopIndividulsDump_Prime_Replicate_Level(objSSParametersLocal)
                                self.methodFileOutput_SimPopIndividulsDump_Write_Replicate_Level(outputFileHandle, obj_SSReplicate, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                                obj_SSPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_Population_Level(objSSParametersLocal, pop)
                                self.methodFileOutput_SimPopIndividulsDump_Write_Population_Level(outputFileHandle, obj_SSPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                                boolIncludeParentOffspringProperties = True
                                obj_SSVirtualSubPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Level(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties)
                                self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Level(outputFileHandle, obj_SSVirtualSubPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, boolIncludeParentOffspringProperties, listVirtSubPopsToOutput)

                                with object_SSIndividual() as obj_SSIndividual:
                                    obj_SSIndividual.objSSParametersLocal = objSSParametersLocal
                                    obj_SSIndividual.pop = pop
                                    intIndivCount = 1
                                    obj_SSIndividual.intIndivCount = intIndivCount
                                    for simupopIndividual in pop.individuals([0,0]):
                                        obj_SSIndividual.method_PopulateProperties(simupopIndividual)
                                        #Only need 1 individual for headings
                                        break

                                #obj_SSIndividual = self.methodFileOutput_SimPopIndividulsDump_Prime_Individual_Level(objSSParametersLocal, pop, simupopIndividual)
                                self.methodFileOutput_SimPopIndividulsDump_Write_Individual_Level(outputFileHandle, obj_SSIndividual, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                            pass
                        
                            #Write header EOL
                            outputFileHandle.write('\n')
                            
                            #Now header have been written...write the details
                            self.methodFileOutput_SimPopIndividulsDump_Write_Detail(outputFileHandle, objSSParametersLocal, obj_SSSimulation, obj_SSBatch, obj_SSReplicate, obj_SSPopulation, obj_SSVirtualSubPopulation, obj_SSIndividual, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput)


                            #self.methodFileOutput_SimPopIndividulsDump(outputFileHandle, objSSParametersLocal, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                            #self.methodFileOutput_SimPopIndividulsPedigreeCompatibleDump(outputFileHandle, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)

                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                        pass
                    pass
                return boolSuccessful
                
            ''' Start to write the objects property values '''

            def methodFileOutput_SimPopIndividulsDump_Write_Detail(self, outputFileHandle, objSSParametersLocal, obj_SSSimulation, obj_SSBatch, obj_SSReplicate, obj_SSPopulation, obj_SSVirtualSubPopulation, obj_SSIndividual, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput):

                boolPastFirstWrite = False

                intNumberVirtualSubPops = pop.numVirtualSubPop() ### Pass as list instead
                
                #for intVirtualSubPop in range(0, intNumberVirtualSubPops): #Process from list
                for listCurrentVSP in listVirtSubPopsToOutput:
                    
                    listSingleVirtualSubPop = listCurrentVSP

                    if boolPastFirstWrite == False:
                        intIndivCount = 1
                        boolPastFirstWrite = True
                    else:
                        obj_SSVirtualSubPopulation = self.methodFileOutput_SimPopIndividulsDump_Prime_VirtualSubPopulation_Level(objSSParametersLocal, pop)
                    pass
                
                    intIndivCount = 0
                    
                    #for simupopIndividual in pop.individuals([intSubPop,intVirtualSubPop]):
                    for simupopIndividual in pop.individuals(listSingleVirtualSubPop):
                            
                        intIndivCount = intIndivCount + 1

                        self.methodFileOutput_SimPopIndividulsDump_Write_Sim_Level_Detail(outputFileHandle, obj_SSSimulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                        self.methodFileOutput_SimPopIndividulsDump_Write_Batch_Level_Detail(outputFileHandle, obj_SSBatch, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                        self.methodFileOutput_SimPopIndividulsDump_Write_Replicate_Level_Detail(outputFileHandle, obj_SSReplicate, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                        self.methodFileOutput_SimPopIndividulsDump_Write_Population_Level_Detail(outputFileHandle, obj_SSPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                        boolIncludeParentOffspringProperties = True
                        self.methodFileOutput_SimPopIndividulsDump_Write_VirtualSubPopulation_Level_Detail(outputFileHandle, obj_SSVirtualSubPopulation, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listSingleVirtualSubPop[1], boolIncludeParentOffspringProperties)

                        obj_SSIndividual = self.methodFileOutput_SimPopIndividulsDump_Prime_Individual_Level(objSSParametersLocal, pop, simupopIndividual, intIndivCount)
                        self.methodFileOutput_SimPopIndividulsDump_Write_Individual_Level_Detail(outputFileHandle, obj_SSIndividual, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)

                        #Write EOL
                        outputFileHandle.write('\n')
                    pass
                pass

            ''' END OF SPECIFIC CONTROL STRUCTURE '''
                       
            '''
            ++++++++++++++++++++++++++++
            SIM REPORT - SLF - Sim Level File - Sim Level Reporting ONLY
            ++++++++++++++++++++++++++++
            '''

            ''' ENTRY POINT  - Start to define how the requested data will be grouped '''
            def method_Output_SIM_LEVEL_To_SLF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                #Check if file is required.  No filenames listed assumes that it is NOT required.
                if listOutputDestinations != []:

                    self.method_Output_SIM_LEVEL_To_SLF_Files_OUTPUT_HEADER_and_PRIME_DETAIL(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)

                else:
                    #Output is NOT Required
                    pass

                pass
            
            ''' Start to output the data '''
               
            def method_Output_SIM_LEVEL_To_SLF_Files_OUTPUT_HEADER_and_PRIME_DETAIL(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()     
                            

                '''
                Prime reporting objects with their properties from the raw data
                '''
                listHeaderValues = []
                
                strObjectName = 'obj_SIM_LEVEL_Reporting'
                dictObj_SSParams = AutoVivificationHandler()
                
                
                strClassNameOfReportingObjectToCreate = 'object_SSSimulation_V2'
                dictPropertiesNotSuppressedForThisObject = {}
                #dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                #Temp
                boolReusePrimedTopLevelOutputObject = False
                
                if boolReusePrimedTopLevelOutputObject:
                    pass
                else:
                    str_VSP_Group = ''
                    obj_SSParams = self.method_Output_Prime_LEVEL_Reporting_Object(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject, str_VSP_Group)
                    objSSParametersLocal.obj_SIM_LEVEL_Reporting_PrimedTopLevelOutputObject = obj_SSParams
               
                                
                ''' Process to console or file '''                                    
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                         pass
                    else:
                        #write output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                str_VSP_Group = ''
                                obj_SSParams = self.method_Output_Prime_LEVEL_Reporting_Object(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject, str_VSP_Group)
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                                #File is being written to for the first time so write the header record

                                self.method_File_Output_To_LF_Files_OUTPUT_DETAIL_HEADER_KEYS(outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                            pass
                        
                            #Write header EOL
                            outputFileHandle.write('\n')
                            
                            #Now header have been written...write the details
                            self.method_Output_SIM_LEVEL_To_SLF_Files_OUTPUT_DETAIL(outputFileHandle, objSSParametersLocal, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput)

                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                        pass
                    pass

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass  

                return boolSuccessful

            ''' Start to write the objects property values '''

            def method_Output_SIM_LEVEL_To_SLF_Files_OUTPUT_DETAIL(self, outputFileHandle, objSSParametersLocal, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput):

                self.method_File_Output_To_LF_Files_OUTPUT_DETAIL_VALUES(outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                boolIncludeParentOffspringProperties = True

                #Write EOL
                #outputFileHandle.write('\n')

                return True
            
            '''
            ++++++++++++++++++++++++++++
            BATCH REPORT - BLF - Batch Level File - Batch Level Reporting ONLY
            ++++++++++++++++++++++++++++
            '''

            ''' ENTRY POINT  - Start to define how the requested data will be grouped '''
            def method_Output_BATCH_LEVEL_To_BLF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                #Check if file is required.  No filenames listed assumes that it is NOT required.
                if listOutputDestinations != []:

                    self.method_Output_BATCH_LEVEL_To_BLF_Files_OUTPUT_HEADER_and_PRIME_DETAIL(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)

                else:
                    #Output is NOT Required
                    pass

                pass
            
            ''' Start to output the data '''
               
            def method_Output_BATCH_LEVEL_To_BLF_Files_OUTPUT_HEADER_and_PRIME_DETAIL(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                '''
                Prime reporting objects with their properties from the raw data
                '''
                
                strObjectName = 'obj_BATCH_LEVEL_Reporting'
                dictObj_SSParams = AutoVivificationHandler()
                
                
                strClassNameOfReportingObjectToCreate = 'object_SSBatch_V2'
                dictPropertiesNotSuppressedForThisObject = {}
                #dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                #Temp
                boolReusePrimedTopLevelOutputObject = False
                
                if boolReusePrimedTopLevelOutputObject:
                    pass
                else:
                    str_VSP_Group = ''
                    obj_SSParams = self.method_Output_Prime_LEVEL_Reporting_Object(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject, str_VSP_Group)
                    objSSParametersLocal.obj_BATCH_LEVEL_Reporting_PrimedTopLevelOutputObject = obj_SSParams

                                
                ''' Process to console or file '''                                    
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        #self.methodConsoleOutput_SimPopIndividulsDump(objSSParametersLocal, pop, intSubPop, intCurrentTemporalFertilisation)
                        pass
                    else:
                        #write output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                str_VSP_Group = ''
                                obj_SSParams = self.method_Output_Prime_LEVEL_Reporting_Object(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject, str_VSP_Group)
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                                #File is being written to for the first time so write the header record
                                
                                self.method_File_Output_To_LF_Files_OUTPUT_DETAIL_HEADER_KEYS(outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                            pass
                        
                            #Write header EOL
                            outputFileHandle.write('\n')
                            
                            #Now header have been written...write the details
                            self.method_Output_BATCH_LEVEL_To_BLF_Files_OUTPUT_DETAIL(outputFileHandle, objSSParametersLocal, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput)

                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                        pass
                    pass
                return boolSuccessful

            ''' Start to write the objects property values '''

            def method_Output_BATCH_LEVEL_To_BLF_Files_OUTPUT_DETAIL(self, outputFileHandle, objSSParametersLocal, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput):

                self.method_File_Output_To_LF_Files_OUTPUT_DETAIL_VALUES(outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                boolIncludeParentOffspringProperties = True

                #Write EOL
                #outputFileHandle.write('\n')

                return True

            '''
            ++++++++++++++++++++++++++++
            REPLICATE REPORT - RLF - Replicate Level File - Batch Level Reporting ONLY
            ++++++++++++++++++++++++++++
            '''

            ''' ENTRY POINT  - Start to define how the requested data will be grouped '''
            def method_Output_REPLICATE_LEVEL_To_RLF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                #Check if file is required.  No filenames listed assumes that it is NOT required.
                if listOutputDestinations != []:

                    self.method_Output_REPLICATE_LEVEL_To_RLF_Files_OUTPUT_HEADER_and_PRIME_DETAIL(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput)

                else:
                    #Output is NOT Required
                    pass

                pass
            
            ''' Start to output the data '''
               
            def method_Output_REPLICATE_LEVEL_To_RLF_Files_OUTPUT_HEADER_and_PRIME_DETAIL(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput):

                '''
                Prime reporting objects with their properties from the raw data
                '''
                
                strObjectName = 'obj_REPLICATE_LEVEL_Reporting'
                dictObj_SSParams = AutoVivificationHandler()
                
                
                strClassNameOfReportingObjectToCreate = 'object_SSReplicate_V2'
                dictPropertiesNotSuppressedForThisObject = {}
                #dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                boolIncludeParentOffspringProperties = True
                #Temp
                boolReusePrimedTopLevelOutputObject = False
                
                if boolReusePrimedTopLevelOutputObject:
                    pass
                else:
                    str_VSP_Group = ''
                    obj_SSParams = self.method_Output_Prime_LEVEL_Reporting_Object(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject, str_VSP_Group)
                    objSSParametersLocal.obj_REPLICATE_LEVEL_Reporting_PrimedTopLevelOutputObject = obj_SSParams

                                
                ''' Process to console or file '''                                    
                for stringOutputDestination in listOutputDestinations:
                    if stringOutputDestination == 'console':
                        #print output to screen
                        #self.methodConsoleOutput_SimPopIndividulsDump(objSSParametersLocal, pop, intSubPop, intCurrentTemporalFertilisation)
                        pass
                    else:
                        #write output to file
                        with FileHandler() as objectFileHandler:
                            boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                            if boolFileExists:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
                                str_VSP_Group = ''
                                obj_SSParams = self.method_Output_Prime_LEVEL_Reporting_Object(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject, str_VSP_Group)
                            else:
                                outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')

                                #File is being written to for the first time so write the header record
                                
                                self.method_File_Output_To_LF_Files_OUTPUT_DETAIL_HEADER_KEYS(outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                            pass
                        
                            #Write header EOL
                            outputFileHandle.write('\n')
                            
                            #Now header have been written...write the details
                            self.method_Output_REPLICATE_LEVEL_To_RLF_Files_OUTPUT_DETAIL(outputFileHandle, objSSParametersLocal, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput)

                            #Close the file
                            boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                        pass
                    pass
                return boolSuccessful

            ''' Start to write the objects property values '''

            def method_Output_REPLICATE_LEVEL_To_RLF_Files_OUTPUT_DETAIL(self, outputFileHandle, objSSParametersLocal, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput):

                self.method_File_Output_To_LF_Files_OUTPUT_DETAIL_VALUES(outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                boolIncludeParentOffspringProperties = True

                #Write EOL
                #outputFileHandle.write('\n')

                return True

            '''
            ++++++++++++++++++++++++++++
            VSP REPORT - VLF - VSP Level File - Batch Level Reporting ONLY
            ++++++++++++++++++++++++++++
            '''

            ''' ENTRY POINT  - Start to define how the requested data will be grouped '''
            def method_Output_VSP_LEVEL_To_VLF_Files(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput, str_VSP_Group):

                #Check if file is required.  No filenames listed assumes that it is NOT required.
                if listOutputDestinations != []:

                    self.method_Output_VSP_LEVEL_To_VLF_Files_OUTPUT_HEADER_and_PRIME_DETAIL(objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput, str_VSP_Group)

                else:
                    #Output is NOT Required
                    pass

                pass
            
                return True
            
            ''' Start to output the data '''
               
            def method_Output_VSP_LEVEL_To_VLF_Files_OUTPUT_HEADER_and_PRIME_DETAIL(self, objSSParametersLocal, pop, listOutputDestinations, intSubPop, intCurrentTemporalFertilisation, listVirtSubPopsToOutput, str_VSP_Group):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()     
                    
                listVSPsTpReport = [x for x in listVirtSubPopsToOutput]
                for tupVSP in listVSPsTpReport:
                    listVirtSubPopsToOutput = []
                    listVirtSubPopsToOutput.append(tupVSP)
                    
                    '''
                    Prime reporting objects with their properties from the raw data
                    '''
                    
                    strObjectName = 'obj_VSP_LEVEL_Reporting'
                    dictObj_SSParams = AutoVivificationHandler()
                    
                    
                    strClassNameOfReportingObjectToCreate = 'object_SSVirtualSubPop_V2'
                    dictPropertiesNotSuppressedForThisObject = {}
                    #dictPropertiesNotSuppressedForThisObject = dictPropertiesNotSuppressed[strObjectName]
                    boolIncludeParentOffspringProperties = True
                    #Temp
                    boolReusePrimedTopLevelOutputObject = False
                    
                    if boolReusePrimedTopLevelOutputObject:
                        pass
                    else:
                        obj_SSParams = self.method_Output_Prime_LEVEL_Reporting_Object(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject, str_VSP_Group)
                        objSSParametersLocal.obj_VSP_LEVEL_Reporting_PrimedTopLevelOutputObject = obj_SSParams
    
                                    
                    ''' Process to console or file '''                                    
                    for stringOutputDestination in listOutputDestinations:
                        if stringOutputDestination == 'console':
                            #print output to screen
                            #self.methodConsoleOutput_SimPopIndividulsDump(objSSParametersLocal, pop, intSubPop, intCurrentTemporalFertilisation)
                            pass
                        else:
                            #write output to file
                            with FileHandler() as objectFileHandler:
                                boolFileExists = objectFileHandler.fileExists(stringOutputDestination)
                                if boolFileExists:
                                    outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'append')
    
                                    obj_SSParams = self.method_Output_Prime_LEVEL_Reporting_Object(objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject, str_VSP_Group)
                                else:
                                    outputFileHandle = objectFileHandler.fileOpen(stringOutputDestination, 'write')
    
                                    #File is being written to for the first time so write the header record
                                    
                                    self.method_File_Output_To_LF_Files_OUTPUT_DETAIL_HEADER_KEYS(outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                                pass
                            
                                #Write header EOL
                                outputFileHandle.write('\n')
                                
                                #Now header have been written...write the details
                                self.method_Output_VSP_LEVEL_To_VLF_Files_OUTPUT_DETAIL(outputFileHandle, objSSParametersLocal, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput)
    
                                #Close the file
                                boolSuccessful = objectFileHandler.fileClose(outputFileHandle)
                            pass
                        pass
                    pass
                pass

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass  
                                    
                return boolSuccessful

            ''' Start to write the objects property values '''

            def method_Output_VSP_LEVEL_To_VLF_Files_OUTPUT_DETAIL(self, outputFileHandle, objSSParametersLocal, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists, listVirtSubPopsToOutput):

                self.method_File_Output_To_LF_Files_OUTPUT_DETAIL_VALUES(outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists)
                boolIncludeParentOffspringProperties = True

                #Write EOL
                #outputFileHandle.write('\n')

                return True


            '''
            ++++++++++++++++++++++++++++
            LEVEL REPORT - Level reporting general routines
            ++++++++++++++++++++++++++++
            '''

            ''' prime LEVEL object with its properties '''
            
            def method_Output_Prime_LEVEL_Reporting_Object(self, objSSParametersLocal, pop, listVirtSubPopsToOutput, boolIncludeParentOffspringProperties, strClassNameOfReportingObjectToCreate, dictPropertiesNotSuppressedForThisObject, str_VSP_Group):

                #Get the Type for the passed class name so the it can be created as an object
                typeFromClassName = self.method_getClassTypeFromClassName(strClassNameOfReportingObjectToCreate)
                
                with typeFromClassName() as obj_SSParams:
                    obj_SSParams.objSSParametersLocal = objSSParametersLocal
                    obj_SSParams.pop = pop
                    obj_SSParams.listVirtSubPopsToOutput = listVirtSubPopsToOutput
                    obj_SSParams.dictPropertiesNotSuppressed = dictPropertiesNotSuppressedForThisObject

                    if strClassNameOfReportingObjectToCreate == 'object_SSVirtualSubPop_V2': 
                        obj_SSParams.method_PopulateProperties(boolIncludeParentOffspringProperties, str_VSP_Group)
                    elif strClassNameOfReportingObjectToCreate == 'object_SSReplicate_V2': 
                        obj_SSParams.method_PopulateProperties(boolIncludeParentOffspringProperties)
                    else:
                        obj_SSParams.method_PopulateProperties()
    
                return obj_SSParams
                            

            ''' Write object property keys as header values '''
           
            def method_File_Output_To_LF_Files_OUTPUT_DETAIL_HEADER_KEYS(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists):

                with OutputHandler() as obj_OutputOperation:
                    
                    ''' Get only properties marked for reporting in their property name '''
                    list_Obj_Properties = list(obj_SSParams.__dict__.keys())
                    list_Rep_Properties = [s for s in list_Obj_Properties if '_Rep_' in s]
                    
                    ''' Get the property reporting order and sort the reporting property list  ascending '''
                    def get_Property_Reporting_Order( str_Prop_Name ):
                        int_Index = int(regex.findall('_Rep_(\d+)', str_Prop_Name)[0])
                        return int_Index
                    list_Rep_Properties.sort(key = get_Property_Reporting_Order)
                    
                    ''' Output each property key as a header col name '''
                    for str_Instance_Variable_Name in list_Rep_Properties:
                        
                        obj_attrib_Instance_Valuable_Value = getattr(obj_SSParams, str_Instance_Variable_Name)
                        
                        int_Reporting_Index = get_Property_Reporting_Order(str_Instance_Variable_Name)
                        if int_Reporting_Index == 1:
                            ''' If this is a Data Section Leverl Note - treat it differently '''
                            strDelim = ''
                        else:
                            strDelim = globalsSS.StringDelimiters.static_stringDelimiter_SEMI_COLON
                        pass

                        listKeys = list(obj_attrib_Instance_Valuable_Value.keys())
                        
                        #self.obj_Log_Debug.debug('str_Instance_Variable_Name: ' + str_Instance_Variable_Name + 'listKeys: ' + str(listKeys))
                    
                        ''' output the key '''   
                        strKey = listKeys[0]
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strKey, strDelim)
                    pass

            ''' Write object property values '''
           
            def method_File_Output_To_LF_Files_OUTPUT_DETAIL_VALUES(self, outputFileHandle, obj_SSParams, pop, intSubPop, intCurrentTemporalFertilisation, boolFileExists):

                with OutputHandler() as obj_OutputOperation:

                    ''' Get only properties marked for reporting in their property name '''
                    list_Obj_Properties = list(obj_SSParams.__dict__.keys())
                    list_Rep_Properties = [s for s in list_Obj_Properties if '_Rep_' in s]
                    
                    ''' Get the property reporting order and sort the reporting property list ascending '''
                    def get_Property_Reporting_Order( str_Prop_Name ):
                        int_Index = int(regex.findall('_Rep_(\d+)', str_Prop_Name)[0])
                        return int_Index
                    list_Rep_Properties.sort(key = get_Property_Reporting_Order)
                    
                    ''' Output each property VALUE '''
                    for str_Instance_Variable_Name in list_Rep_Properties:
                        
                        obj_attrib_Instance_Valuable_Value = getattr(obj_SSParams, str_Instance_Variable_Name)
                        
                        int_Reporting_Index = get_Property_Reporting_Order(str_Instance_Variable_Name)
                        if int_Reporting_Index == 1:
                            ''' If this is a Data Section Leverl Note - treat it differently '''
                            strDelim = ''
                        else:
                            strDelim = globalsSS.StringDelimiters.static_stringDelimiter_SEMI_COLON
                        pass

                        listValues = list(obj_attrib_Instance_Valuable_Value.values())

                        #self.obj_Log_Debug.debug('str_Instance_Variable_Name: ' + str_Instance_Variable_Name + 'listValues: ' + str(listValues))
                    
                        ''' output the key '''   
                        strValue = str(listValues[0])
                        obj_OutputOperation.method_FileOutput_WriteDelimitedValue(outputFileHandle, strValue, strDelim)
                    pass

                                
            ''' END OF SPECIFIC CONTROL STRUCTURE '''
            
            '''
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Excel Control Routines
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            '''
            
            def func_Get_Excel_Writer(self, str_Excel_Output_Path, str_Excel_Output_File_WO_Suffix):
    
                str_Excel_Output_File_Suffix = '.xlsx' 
                str_Excel_Output_File = str_Excel_Output_File_WO_Suffix + str_Excel_Output_File_Suffix
                str_Excel_Output_Path_And_File = str_Excel_Output_Path + '\\' + str_Excel_Output_File
        
                writer = pandas.ExcelWriter(str_Excel_Output_Path_And_File)    
            
                return writer

            def func_Save_Excel_Writer(self, writer):
                
                writer.save()
                 
                return True

            '''
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Generic Logging Operations
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            '''
           
            def Get_Log_Current_Column_Index(self, bool_Reset, intLevel, bool_Add_Suffix = False, str_Suffix = ''):
                
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
                    L, h, i, j = self.str_Current_Col_Index.split(globalsSS.StringDelimiters.static_stringDelimiter_DOT)
                    
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
                                self.obj_Log_Default.warn('Column index number has exceeded its max number 9.9.9. Dataframes will not be in the correct column order')
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
            
            def func_Get_Func_Specific_Logger_Name(self, str_Log_Output_Path, str_Logger_Name): 
                
                obj_Logging = Logging()
                obj_Logging.str_Logger_Name = str_Logger_Name
                obj_Logging.str_Logger_Level = 'info'
                obj_Logging.bool_ClearLogFileAtStart = True
                obj_Logging.bool_LogToConsole = True
                obj_Logging.bool_LogToFile = True
                obj_Logging.strLogPath = str_Log_Output_Path
                obj_Logging.strLogFile = str_Logger_Name
        
                return obj_Logging
                        
            '''            
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS FINALIZATION
            '''                        
            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.SSOutputOperation_obj = SSOutputOperation() 
        return self.SSOutputOperation_obj
 
    def __exit__(self, type, value, traceback): 
        self.SSOutputOperation_obj.classCleanUp()
