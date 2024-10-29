'''
Created on 21 Jan 2015

@author: Alia
'''
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS
#
#------------------< Import python modules
# DEBUG Imports
from logging import getLogger as logging__getLogger
from handler_Debug import Timer
from handler_Debug import Timer2
from handler_Debug import Debug_Location
#from Bio.PopGen.GenePop.EasyController import EasyController as biopython__Easy_Controller
from BioPython.EasyController import EasyController as biopython__Easy_Controller
from collections import OrderedDict
from itertools import compress as itertools__compress
from os import path as os__path
from os import getcwd as os__getcwd
#------------------< Import SharkSim modules
from handler_Logging import Logging
from SSParameterHandler import SSParameterHandler
from SSOutputHandler import SSOutputHandler
from globals_SharkSim import globalsSS
from FileHandler import FileHandler
from SSAnalysisHandler import SSAnalysisHandler

class Biopython(object):
    '''
    classdocs
    '''
    
    str_GP_Data_File = ''
    str_GP_Data_Path = ''
    str_Current_Col_Index = str(
                                 '0' +
                                 globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                 '0' +
                                 globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                 '0' +
                                 globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                 '0')
    str_Log_Output_Path = ''
    
    def __init__(self, objSSParameters, str_Log_Output_Path, str_GP_Data_Path, str_GP_Data_File, str_GP_EXE_Path=''):
        '''
        Constructor
        '''
        #self.obj_Log_Default = logging__getLogger(__name__)
        #self.obj_Log_Debug = logging__getLogger('app_debug')

        ''' Get Default Logger '''
        self.obj_Log_Default_Display = None
        if globalsSS.Logger_Default_Display.bool_Default_Display:
            ''' NOTE: Name is obj_Log_Default '''
            self.obj_Log_Default = logging__getLogger(globalsSS.Logger_Default_Display.static_Logger_Name__Default_Display)
        pass

#         self.obj_Log_Debug = None
#         if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
        self.obj_Log_Debug = logging__getLogger('app_debug')           
        pass
            
        self.objSSParametersLocal = objSSParameters
        
        self.str_ID_Suf = globalsSS.StringDelimiters.static_stringDelimiter_SPACE
        
        self.str_Log_Output_Path = str_Log_Output_Path
        
        self.str_GP_Data_File = str_GP_Data_File
        self.str_GP_Data_Path = str_GP_Data_Path
        
        str_GP_Data_Path_And_File = str_GP_Data_Path + '\\' + str_GP_Data_File
        
        
        boolSuccess = False
        ''' Ensure Genepop.exe exists in the analysis path '''
        
        boolSuccess = self.Put_Genepop_Binary_Into_Analysis_Path(str_GP_EXE_Path)
        
        ''' Create Biopython EasyController '''
        if boolSuccess:
            self.GP_EC = biopython__Easy_Controller(str_GP_Data_Path_And_File, str_GP_EXE_Path)
            #self.GP_EC = biopython__Easy_Controller(str_GP_Data_Path_And_File)
        pass
    
        return None
    
    def Put_Genepop_Binary_Into_Analysis_Path(self, str_GP_EXE_Path):
    
        boolSuccess = False
        
        strFilePath_ProcessUser = globalsSS.Shared_External_Resources.static_User_Programs_Folder
        strFilePath_ProcessSource = globalsSS.Shared_External_Resources.static_Win_Binary_Folder_GENEPOP
        strFilePath_Working = str_GP_EXE_Path
        
        with FileHandler() as objFileOperation:
#             strFolderPath_Copy_Source = strFilePath_ProcessSource
#             strFolderPath_Copy_Destination = strFilePath_Working
            strFolderPath_Copy_Source = os__path.join(self.objSSParametersLocal.str_App_Run_Path, strFilePath_ProcessUser, strFilePath_ProcessSource)
            strFolderPath_Copy_Destination = strFilePath_Working
        
            #Check if it exists first
            boolFileExistsAtDestination = objFileOperation.fileExists(strFilePath_Working + '\\' + globalsSS.Shared_External_Resources.static_Win_Binary_Exe_GENEPOP)
            if boolFileExistsAtDestination == False:
                #If not then copy it
                boolSuccess = objFileOperation.method_Copy_Folder_Or_All_Files(strFolderPath_Copy_Source, strFolderPath_Copy_Destination)
            else:
                boolSuccess = True
            pass
        
            if boolSuccess:
                self.obj_Log_Debug.debug('Success - Put_Genepop_Binary_Into_Analysis_Path:' + 'strFolderPath_Copy_Source:' + strFolderPath_Copy_Source + ' to strFolderPath_Copy_Source:' + strFolderPath_Copy_Destination)
            else:
                self.obj_Log_Default.error('ERROR - Put_Genepop_Binary_Into_Analysis_Path:' + 'strFolderPath_Copy_Source:' + strFolderPath_Copy_Source + ' to strFolderPath_Copy_Source:' + strFolderPath_Copy_Destination)
            pass
        
        return boolSuccess
            
            
        return True
    
    def Get_Basic_Info(self):

        boolSuccess = False
         
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()        
            
        pop_names, loci_names = self.GP_EC.get_basic_info()
        
        self.obj_Log_Debug.debug('Basic Info - pop_names:' + str(pop_names) + '; loci_names:' + str(loci_names))
        
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
            #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            #    t2 = Timer2(True)
            #    t2.Start()
            #pass                    
        pass    

        boolSuccess = True
        
        return boolSuccess
    
    
    def Get_Alleles(self):

        boolSuccess = False
         
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()        
            
        allele_list = self.GP_EC.get_alleles_all_pops('07COBS')
        
        self.obj_Log_Debug.debug('get_alleles - allele_list:' + str(allele_list) )
        
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
            #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            #    t2 = Timer2(True)
            #    t2.Start()
            #pass                    
        pass       
        
        boolSuccess = True
        
        return boolSuccess
    
    def Get_Genotype_Frequency(self):

        boolSuccess = False
         
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()        
            
        genotype_list  = self.GP_EC.get_genotype_frequency(0,'07COBS')
        
        self.obj_Log_Debug.debug('get_genotype_frequency - genes_total: ' + str(genotype_list ))
        
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
            #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            #    t2 = Timer2(True)
            #    t2.Start()
            #pass                    
        pass             
        
        boolSuccess = True
        
        return boolSuccess
    
    def Get_Allele_Frequency(self):

        boolSuccess = False
         
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()        
            
        genes_total, allele_freq = self.GP_EC.get_allele_frequency(0,'07COBS')
        
        self.obj_Log_Debug.debug('get_allele_frequency - genes_total: ' + str(genes_total) + '; allele_freq: ' + str(allele_freq))
        
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
            #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            #    t2 = Timer2(True)
            #    t2.Start()
            #pass                    
        pass            
        
        boolSuccess = True
        
        return boolSuccess
    
    def Get_Allele_Frequency_All_Loci(self, dict_Results):

        boolSuccess = False
         
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()        
        
        ''' Get logger to record results '''
        str_Logger_Name = globalsSS.Logger_Details.static_Logger_Name__Genepop_Allele_Freq
        obj_Logging = self.func_Get_Func_Specific_Logger_Name(str_Logger_Name)

        ''' Check if logger already exists - i.e. Genepop data file already processed for this function'''
        with FileHandler() as objFileOperation:
            boolFileExistsAtDestination = objFileOperation.fileExists(obj_Logging.strLogPath + '\\' + obj_Logging.strLogFile)
            
        ''' Run BioP function '''
        if boolFileExistsAtDestination == False:
            int_Pop_Index = 0
            dictAlleleFreq = self.GP_EC.get_allele_frequency_all_loci(int_Pop_Index)
    
            '''Log results'''
            self.Allele_Frequency_All_Loci_By_Allele__Log_Results(dict_Results, dictAlleleFreq)
            self.Log_Allele_Frequency_All_Loci(obj_Logging, dictAlleleFreq, [int_Pop_Index])
                    
            if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
#                 for key, value in dictAlleleFreq.items():
#                     pop_name, freqs, genes_total = value
#                     self.obj_Log_Debug.debug('get_allele_frequency_all_loci - locus: ' + str(key) + '; pop_name: ' + str(pop_name) + '; genes_total: ' + str(genes_total) + '; freqs: ' + str(freqs))
#                 pass
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
        
        boolSuccess = True
        
        return boolSuccess

    def Allele_Frequency_All_Loci_By_Allele__Log_Results(self, dict_Results_Prev, dict_Results_New):
        
        dict_Results_Conv = OrderedDict()
        
        ''' Convert Allele Freqs Dict, which contains a tuple, to a nested dict '''
        for key, value in dict_Results_New.iteritems():
            
            pop_name, freqs, genes_total = value

            
            dict_Results_Conv[key] = OrderedDict([(globalsSS.Colnames_Genepop_Allele_Freqs_By_Allele_Results.static_str_Colname_Pop_Name, pop_name)])
            dict_Results_Conv[key].update(OrderedDict([(globalsSS.Colnames_Genepop_Allele_Freqs_By_Allele_Results.static_str_Colname_Pop_Gene_Count, genes_total)]))
            dict_Results_Conv[key].update(OrderedDict([(globalsSS.Colnames_Genepop_Allele_Freqs_By_Allele_Results.static_str_Colname_Locus_Allele_Freqs, OrderedDict())]))
            dict_Results_Conv[key].update(OrderedDict([(globalsSS.Colnames_Genepop_Allele_Freqs_By_Allele_Results.static_str_Colname_Locus_Name, key)]))
            
            for key_Allele, value_Allele in freqs.iteritems():
                dict_Results_Conv[key][globalsSS.Colnames_Genepop_Allele_Freqs_By_Allele_Results.static_str_Colname_Locus_Allele_Freqs].update(OrderedDict([(key_Allele, value_Allele)]))
            pass        
        pass

        '''
        --------------------------
        Flatten the dict for logging
        --------------------------
        '''
        dict_To_Flatten = dict_Results_Conv

        with SSAnalysisHandler() as obj_SSAnalysis:
            dict_Non_Dict_Key_Count_Per_Level = OrderedDict()
            dict_Non_Dict_Key_Count_Per_Level = obj_SSAnalysis.method_Get_Nested_Dict__Non_Dict_Key_Count_Per_Nested_Level(dict_To_Flatten, 0, dict_Non_Dict_Key_Count_Per_Level)
            #int_Lowest_Level = max(dict_Non_Dict_Key_Count_Per_Level, key=dict_Non_Dict_Key_Count_Per_Level.get) - 1
            int_Lowest_Level = max(dict_Non_Dict_Key_Count_Per_Level.keys(), key=int) - 1
            
            dict_Final = OrderedDict()
            #dict_MultiLine_Results = OrderedDict()
            int_Line_Initial = 0
            int_Line = 0
            int_Level = 0
            int_Lowest_Level_Dict_Num_Keys = 0            
            dict_MultiLine_Results = obj_SSAnalysis.method_Flatten_Nested_Dict_Into_Multiline_Dict__BioP_Allele_Freqs(True, int_Line_Initial, int_Line, int_Level, int_Lowest_Level, int_Lowest_Level_Dict_Num_Keys, dict_To_Flatten, dict_Final)
        pass
        
        ''' Add the run details '''
        int_MultiLine_Count = 0
        for key_New, value_New in dict_MultiLine_Results.items():
            dict_MultiLine_Results[int_MultiLine_Count].update(OrderedDict([(key_Prev, Value_Prev) for key_Prev, Value_Prev in dict_Results_Prev.items()]))
            int_MultiLine_Count += 1
        pass

        '''
        --------------------------
        Log the results
        --------------------------
        '''
   
        ''' Get logger'''
        bool_LogToConsole = False
        str_Logger_Path = self.str_Log_Output_Path
        with FileHandler() as obj_FileOp:
            tupFilePathNameAndExt = obj_FileOp.method_Get_FileNameAndExtension_From_FileName(self.str_GP_Data_File)
        str_Input_File_Suffix = tupFilePathNameAndExt[1]
        str_Input_File_Suffix = str_Input_File_Suffix.replace('.','')
        str_Logger_Name = tupFilePathNameAndExt[0] 
        str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__Genepop_Allele_Freq_By_Allele_PF_Results + str_Input_File_Suffix
        strFileName_Experiment_Label = ''
        str_Experiment = ''
        obj_Logging__AFBA, obj_Results_Log__AFBA = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)
   
        ''' Write output with logger '''
        str_Results_1 = self.objSSParametersLocal.strUniqueRunID
        str_Heading_1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
        str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_File_Heading__Prefix_1__Genepop_Allele_Freq_By_Allele_PF_Results
        obj_Logging__AFBA.func_Log_MultiLine_Results_Header(obj_Results_Log__AFBA, str_Heading_1, str_Heading_Prefix_1, dict_MultiLine_Results)
        obj_Logging__AFBA.func_Log_MultiLine_Results_Detail(str_Results_1, obj_Results_Log__AFBA, dict_MultiLine_Results)
        
        ''' Close the logger '''
        obj_Results_Log__AFBA.handlers = []
                 
        return dict_MultiLine_Results
    
    def Log_Allele_Frequency_All_Loci(self, obj_Logging, dict_Results, list_Params):


        ''' Get the most number of alleles for a locus to allow reporting '''
        intMaxAlleles = 0
        for key, value in dict_Results.iteritems():
            pop_name, freqs, genes_total = value
            
            intAlleles = len(freqs)
            if intAlleles > intMaxAlleles:
                intMaxAlleles = intAlleles
            pass
        pass
        
        ''' Create logger to record results '''
        int_Level = 1
        #str_Logger_Name = list_Params[0] #'Stats_HWE'
        str_Logger_Name = obj_Logging.strLogFile
        obj_Log_Results = self.func_Get_Func_Specific_Python_Logger(obj_Logging)
        ''' Log header '''
        
        str_Log_Line_Part_1 = str(globalsSS.StringDelimiters.static_stringDelimiter_RESULTS_START +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(True, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_UniqueID +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_File +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Logger +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Headings +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Locus +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Pop +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Allele_Freq_Genes)

        str_Log_Line_Part_2 = ''
#         h = 0
#         i = 0
#         j = 0
        
        for intAllele in range(0, intMaxAlleles):
            
#             '''Get column numbering'''
#             if j == 10:
#                 j = 0
#                 i += 1
#                 if i == 10:
#                     i = 0
#                     h += 1
#                     if h == 10:
#                         self.obj_Log_Default.warn('Index dot number has exceeded it max number 9.9.9.' + str_Logger_Name + ' Dataframe will not be in the correct column order')
#                 pass
#             pass
#            str_Col_Index = str(h) + '.' + str(i) + '.' + str(j)
            
            str_Line = str(globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Allele_Freq_Allele +
                           #str_Col_Index + globalsSS.Genepop_Stats.static_Label_Allele_Freq_Allele +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Allele_Freq_Freq)
                           #str_Col_Index + globalsSS.Genepop_Stats.static_Label_Allele_Freq_Freq)
            str_Log_Line_Part_2 += str_Line
            #j += 1
        pass
    
        str_Log_Line = str_Log_Line_Part_1 + str_Log_Line_Part_2 
                
        obj_Log_Results.info(str_Log_Line)
        
        ''' Log results '''
        for key, value in dict_Results.iteritems():
            pop_name, freqs, genes_total = value
            str_Log_Line_Part_1 = str(globalsSS.StringDelimiters.static_stringDelimiter_RESULTS_START +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               self.objSSParametersLocal.strUniqueRunID +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               self.str_GP_Data_File +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str_Logger_Name +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               globalsSS.Genepop_Stats.static_Label_Gen_Results +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(key)  +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(pop_name) +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(genes_total))
            
            str_Log_Line_Part_2 = ''
            for allele, freq in freqs.items():
                str_Line = str(globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                           str(allele) +
                           globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                           str(freq))
                str_Log_Line_Part_2 += str_Line
            pass
        
            str_Log_Line = str_Log_Line_Part_1 + str_Log_Line_Part_2  
            obj_Log_Results.info(str_Log_Line)
        pass
        
        ''' Clear the log handlers'''
        obj_Log_Results.handlers = []
                
        
        return True
    def Get_Allele_Frequency_All_Loci_OLD(self):

        boolSuccess = False
         
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()        
        
        ''' Get logger to record results '''
        str_Logger_Name = globalsSS.Logger_Details.static_Logger_Name__Genepop_Allele_Freq
        obj_Logging = self.func_Get_Func_Specific_Logger_Name(str_Logger_Name)

        ''' Check if logger already exists - i.e. Genepop data file already processed for this function'''
        with FileHandler() as objFileOperation:
            boolFileExistsAtDestination = objFileOperation.fileExists(obj_Logging.strLogPath + '\\' + obj_Logging.strLogFile)
            
        ''' Run BioP function '''
        if boolFileExistsAtDestination == False:
            int_Pop_Index = 0
            dictAlleleFreq = self.GP_EC.get_allele_frequency_all_loci(int_Pop_Index)
    
            '''Log results'''
            self.Log_Allele_Frequency_All_Loci_OLD(obj_Logging, dictAlleleFreq, [int_Pop_Index])
            
                    
            if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
#                 for key, value in dictAlleleFreq.items():
#                     pop_name, freqs, genes_total = value
#                     self.obj_Log_Debug.debug('get_allele_frequency_all_loci - locus: ' + str(key) + '; pop_name: ' + str(pop_name) + '; genes_total: ' + str(genes_total) + '; freqs: ' + str(freqs))
#                 pass
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
        
        boolSuccess = True
        
        return boolSuccess

    def Log_Allele_Frequency_All_Loci_OLD(self, obj_Logging, dict_Results, list_Params):


        ''' Get the most number of alleles for a locus to allow reporting '''
        intMaxAlleles = 0
        for key, value in dict_Results.iteritems():
            pop_name, freqs, genes_total = value
            
            intAlleles = len(freqs)
            if intAlleles > intMaxAlleles:
                intMaxAlleles = intAlleles
            pass
        pass
        
        ''' Create logger to record results '''
        int_Level = 1
        #str_Logger_Name = list_Params[0] #'Stats_HWE'
        str_Logger_Name = obj_Logging.strLogFile
        obj_Log_Results = self.func_Get_Func_Specific_Python_Logger(obj_Logging)
        ''' Log header '''
        
        str_Log_Line_Part_1 = str(globalsSS.StringDelimiters.static_stringDelimiter_RESULTS_START +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(True, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_UniqueID +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_File +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Logger +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Headings +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Locus +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Pop +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Allele_Freq_Genes)

        str_Log_Line_Part_2 = ''
#         h = 0
#         i = 0
#         j = 0
        
        for intAllele in range(0, intMaxAlleles):
            
#             '''Get column numbering'''
#             if j == 10:
#                 j = 0
#                 i += 1
#                 if i == 10:
#                     i = 0
#                     h += 1
#                     if h == 10:
#                         self.obj_Log_Default.warn('Index dot number has exceeded it max number 9.9.9.' + str_Logger_Name + ' Dataframe will not be in the correct column order')
#                 pass
#             pass
#            str_Col_Index = str(h) + '.' + str(i) + '.' + str(j)
            
            str_Line = str(globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Allele_Freq_Allele +
                           #str_Col_Index + globalsSS.Genepop_Stats.static_Label_Allele_Freq_Allele +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Allele_Freq_Freq)
                           #str_Col_Index + globalsSS.Genepop_Stats.static_Label_Allele_Freq_Freq)
            str_Log_Line_Part_2 += str_Line
            #j += 1
        pass
    
        str_Log_Line = str_Log_Line_Part_1 + str_Log_Line_Part_2 
                
        obj_Log_Results.info(str_Log_Line)
        
        ''' Log results '''
        for key, value in dict_Results.iteritems():
            pop_name, freqs, genes_total = value
            str_Log_Line_Part_1 = str(globalsSS.StringDelimiters.static_stringDelimiter_RESULTS_START +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               self.objSSParametersLocal.strUniqueRunID +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               self.str_GP_Data_File +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str_Logger_Name +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               globalsSS.Genepop_Stats.static_Label_Gen_Results +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(key)  +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(pop_name) +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(genes_total))
            
            str_Log_Line_Part_2 = ''
            for allele, freq in freqs.items():
                str_Line = str(globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                           str(allele) +
                           globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                           str(freq))
                str_Log_Line_Part_2 += str_Line
            pass
        
            str_Log_Line = str_Log_Line_Part_1 + str_Log_Line_Part_2  
            obj_Log_Results.info(str_Log_Line)
        pass
        
        ''' Clear the log handlers'''
        obj_Log_Results.handlers = []
                
        
        return True
    
    def Get_Heterozygosity(self):

        boolSuccess = False
         
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()        

        
        (exp_homo, obs_homo, exp_hetero, obs_hetero) = self.GP_EC.get_heterozygosity_info(0,'07COBS')
        
        self.obj_Log_Debug.debug('get_heterozygosity_info - exp_homo: ' + str(exp_homo) + '; obs_homo: ' + str(obs_homo) + '; exp_hetero: ' + str(exp_hetero) + '; obs_hetero: ' + str(obs_hetero))
        
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
            #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            #    t2 = Timer2(True)
            #    t2.Start()
            #pass                    
        pass           
        
        boolSuccess = True
        
        return boolSuccess
    
    def Get_Heterozygosity_All_Loci(self):

        boolSuccess = False
         
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()        

        ''' Get logger to record results '''
        str_Logger_Name = globalsSS.Logger_Details.static_Logger_Name__Genepop_He_All_Loci
        obj_Logging = self.func_Get_Func_Specific_Logger_Name(str_Logger_Name)

        ''' Check if logger already exists - i.e. Genepop data file already processed for this function'''
        with FileHandler() as objFileOperation:
            boolFileExistsAtDestination = objFileOperation.fileExists(obj_Logging.strLogPath + '\\' + obj_Logging.strLogFile)
            
        ''' Run BioP function '''
        if boolFileExistsAtDestination == False:
            dictHE = self.GP_EC.get_heterozygosity_info_all_loci(0)
           
            '''Log results'''
            self.Log_Heterozygosity_All_Loci(obj_Logging, dictHE, [str_Logger_Name])
                 
            if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                #for key, value in dictHE.items():
                    #(exp_homo, obs_homo, exp_hetero, obs_hetero) = value[1]
                    #self.obj_Log_Debug.debug('get_heterozygosity_info_all_loci - locus: ' + str(key) + '; exp_homo: ' + str(exp_homo) + '; obs_homo: ' + str(obs_homo) + '; exp_hetero: ' + str(exp_hetero) + '; obs_hetero: ' + str(obs_hetero))
                #pass
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
        
        boolSuccess = True
        
        return boolSuccess

    def Log_Heterozygosity_All_Loci(self, obj_Logging, dict_Results, list_Params):
        
        ''' Create logger to record results '''
        int_Level = 1
        str_Logger_Name = obj_Logging.strLogFile
        obj_Log_Results = self.func_Get_Func_Specific_Python_Logger(obj_Logging)
        ''' Log header '''
        str_Log_Line = str(globalsSS.StringDelimiters.static_stringDelimiter_RESULTS_START +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(True, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_UniqueID +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_File +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Logger +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Headings +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Locus +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_He_All_Loci_HoExp +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_He_All_Loci_HoObs +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_He_All_Loci_HeExp +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_He_All_Loci_HeObs)
        obj_Log_Results.info(str_Log_Line)
        
        ''' Log results '''
        for key, value in dict_Results.iteritems():
            (exp_homo, obs_homo, exp_hetero, obs_hetero) = value[1]
            str_Log_Line = str(globalsSS.StringDelimiters.static_stringDelimiter_RESULTS_START +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               self.objSSParametersLocal.strUniqueRunID +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               self.str_GP_Data_File +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str_Logger_Name +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               globalsSS.Genepop_Stats.static_Label_Gen_Results +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(key)  +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(exp_homo) +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(obs_homo) +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(exp_hetero) +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(obs_hetero))
            obj_Log_Results.info(str_Log_Line)
        pass
        
        ''' Clear the log handlers'''
        obj_Log_Results.handlers = []
                
        
        return True
    
    def Get_HWE_Pop(self, str_Param):

        boolSuccess = False
         
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()        

        ''' Get logger to record results '''
        str_Logger_Name = globalsSS.Logger_Details.static_Logger_Name__Genepop_HWE
        obj_Logging = self.func_Get_Func_Specific_Logger_Name(str_Logger_Name)

        ''' Check if logger already exists - i.e. Genepop data file already processed for this function'''
        with FileHandler() as objFileOperation:
            boolFileExistsAtDestination = objFileOperation.fileExists(obj_Logging.strLogPath + '\\' + obj_Logging.strLogFile)
            
        ''' Run BioP function '''
        if boolFileExistsAtDestination == False:
#             #Biopython defaults
            dememorization=10000
            batches=20
            iterations=5000     
            enum_test=False       
            #GP on the Web defaults
#             dememorization =1000
#             batches=100
#             iterations=1000
#             enum_test=False

#             #My opts V1 --- NOTE: When n=4000 S.E > 0.010 - When Best Quality, Slow - 
#             dememorization =10000
#             batches=400
#             iterations=10000
#             enum_test=False
# 
#             #My opts V2 --- NOTE: When n=4000 S.E > 0.013 - Mode Quality, Slowish
#             dememorization =10000
#             batches=200
#             iterations=10000
#             enum_test=False
# 
#             '''
#             My opts V3 --- NOTE:
#             When n=4000 S.E > 0.015 - Mode Quality, Slowish
#             '''
#             dememorization =10000
#             batches=150
#             iterations=10000
#             enum_test=False

#             '''
#             My opts V4 --- NOTE:
#             When n = 1000 S.E > 0.013 - Mode Quality, Slowish
#               '''
#             dememorization =10000
#             batches=100
#             iterations=7000
#             enum_test=False

            loci_map = self.GP_EC.test_hw_pop(1, str_Param, enum_test, dememorization , batches, iterations)
    
            '''Log results'''
            self.Log_HWE_Pop(obj_Logging, loci_map, [str_Logger_Name, str_Param])
                
                
            if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                #self.obj_Log_Debug.debug('test_hw_pop(1, '+ str_Param +') - loci_map:' + str(loci_map))
                #for key, value in loci_map.items():
                    #self.obj_Log_Debug.debug('locus :  ' + str(key) + '( P-val, S.E., W&C, R&H, Steps ) = ' + str(value))
                #pass
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
        
        boolSuccess = True
        
        return boolSuccess
    
    def Log_HWE_Pop(self, obj_Logging, dict_Results, list_Params):
        
        ''' Create logger to record results '''
        int_Level = 1
        str_Logger_Name = obj_Logging.strLogFile
        obj_Log_Results = self.func_Get_Func_Specific_Python_Logger(obj_Logging)
        ''' Log header '''
        str_Log_Line = str(globalsSS.StringDelimiters.static_stringDelimiter_RESULTS_START +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(True, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_UniqueID +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_File +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Logger +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Headings +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Locus +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_HWE_Test +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_HWE_P +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_HWE_SE +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_HWE_WC +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_HWE_RH +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_HWE_Steps)
        obj_Log_Results.info(str_Log_Line)
        
        ''' Log results '''
        for key, value in dict_Results.iteritems():
            p, se, wc, rh, steps = value
            str_Log_Line = str(globalsSS.StringDelimiters.static_stringDelimiter_RESULTS_START +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               self.objSSParametersLocal.strUniqueRunID +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               self.str_GP_Data_File +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str_Logger_Name +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               globalsSS.Genepop_Stats.static_Label_Gen_Results +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(key)  +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               list_Params[1] +                               
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(p) +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(se) +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(wc) +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(rh) +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(steps))
            obj_Log_Results.info(str_Log_Line)
        pass
        
        ''' Clear the log handlers'''
        obj_Log_Results.handlers = []
                
        
        return True
        
    def Get_HWE_Global(self, str_Param):

        boolSuccess = False
         
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()        

        ''' Get logger to record results '''
        str_Logger_Name = globalsSS.Logger_Details.static_Logger_Name__Genepop_HWE
        obj_Logging = self.func_Get_Func_Specific_Logger_Name(str_Logger_Name)

        ''' Check if logger already exists - i.e. Genepop data file already processed for this function'''
        with FileHandler() as objFileOperation:
            boolFileExistsAtDestination = objFileOperation.fileExists(obj_Logging.strLogPath + '\\' + obj_Logging.strLogFile)
            
        ''' Run BioP function '''
        if boolFileExistsAtDestination == False:
            
            pop_test, loc_test, all_test = self.GP_EC.test_hw_global(str_Param)
        
            self.obj_Log_Debug.debug('test_hw_pop(1, "probability") - pop_test:' + str(pop_test) + '; loc_test:' + str(loc_test) + '; all_test' + str(all_test))
        
            '''Log results'''
            loci_map = None
            self.Log_HWE_Global(obj_Logging, loci_map, [str_Logger_Name, str_Param])
                
                
            if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                #self.obj_Log_Debug.debug('test_hw_pop(1, '+ str_Param +') - loci_map:' + str(loci_map))
                #for key, value in loci_map.items():
                    #self.obj_Log_Debug.debug('locus :  ' + str(key) + '( P-val, S.E., W&C, R&H, Steps ) = ' + str(value))
                #pass
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
        
        boolSuccess = True
        
        return boolSuccess
    

    def Get_HWE_Global_OLD(self, str_Param):

        boolSuccess = False
         
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()        
            
        pop_test, loc_test, all_test = self.GP_EC.test_hw_global(str_Param)
        
        self.obj_Log_Debug.debug('test_hw_pop(1, "probability") - pop_test:' + str(pop_test) + '; loc_test:' + str(loc_test) + '; all_test' + str(all_test))
        
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
            #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            #    t2 = Timer2(True)
            #    t2.Start()
            #pass                    
        pass             
        
        boolSuccess = True
        
        return boolSuccess

    
    def Get_Test_LD_All_Pair(self):

        boolSuccess = False
         
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()        
        
        
        
        #GP defaults
        #dememorization=10000
        #batches=100
        #iterations=5000

        #BioP defaults
        #dememorization=10000
        #batches=20
        #iterations=5000
        
        dememorization=10000
        batches=100
        iterations=5000
                
        boolAllLocusPairs = True
        if boolAllLocusPairs:
            ''' Get logger to record results '''
            str_Logger_Name = globalsSS.Logger_Details.static_Logger_Name__Genepop_LD
            obj_Logging = self.func_Get_Func_Specific_Logger_Name(str_Logger_Name)
    
            ''' Check if logger already exists - i.e. Genepop data file already processed for this function'''
            with FileHandler() as objFileOperation:
                boolFileExistsAtDestination = objFileOperation.fileExists(obj_Logging.strLogPath + '\\' + obj_Logging.strLogFile)
                
            ''' Run BioP function '''
            if boolFileExistsAtDestination == False:
                dictLD = self.GP_EC.test_ld_all_pair('','',dememorization, batches, iterations)
    
                '''Log results'''
                
                self.Log_Test_LD_All_Pairs(obj_Logging, dictLD, [str_Logger_Name, dememorization, batches, iterations])

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
        #             if boolAllLocusPairs:
        #                 dictLD = self.GP_EC.test_ld_all_pair('','',dememorization, batches, iterations)
        #                 self.obj_Log_Debug.debug('test_ld_all_pair - boolAllLocusPairs: ' + str(boolAllLocusPairs) + '; dictLD: ')
        #                 for key, value in dictLD.items():
        #                     self.obj_Log_Debug.debug('locus pair :  ' + str(key) + '; loci : ' + str(value[0]) + '; p: ' + str(value[1][0]) + '; se: ' + str(value[1][1]) + '; swirches: ' + str(value[1][2]))
        #                 pass
        #             else:
        #                 self.obj_Log_Debug.debug('test_ld_all_pair - boolAllLocusPairs: ' + str(boolAllLocusPairs) + '; locus1: ' + str_Locus_1 + '; locus2: ' + str_Locus_2 + '; p: ' + str(p) + '; se: ' + str(se) + '; switches: ' + str(switches))
        #             pass
                    pass
                pass
            pass
        else:
            str_Locus_1 = "07COBS"
            str_Locus_2 = "11COBS"
            #DEBUG_ON
            #for inc in range(10, 100, 10):
                #iterations = inc
                #batches = inc

                #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                #    t3 = Timer2(True)
                #    t3.Start()        
            #DEBUG_OFF
            
            p, se, switches = self.GP_EC.test_ld_all_pair(str_Locus_1, str_Locus_2, dememorization, batches, iterations)

            #DEBUG_ON
                #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                #    t3.Stop(self.obj_Log_Debug)
                #self.obj_Log_Debug.debug('inc: ' + str(inc))
            #DEBUG_OFF

            self.obj_Log_Debug.debug('test_ld_all_pair - boolAllLocusPairs: ' + str(boolAllLocusPairs) + '; locus1: ' + str_Locus_1 + '; locus2: ' + str_Locus_2 + '; p: ' + str(p) + '; se: ' + str(se) + '; switches: ' + str(switches))
        
        
#         ''' Clear the log handlers'''
#         obj_Log_Results.handlers = []
               
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
            #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            #    t2 = Timer2(True)
            #    t2.Start()
            #pass                    
        pass        
        
        boolSuccess = True
        
        return boolSuccess

    def Log_Test_LD_All_Pairs(self, obj_Logging, dict_Results, list_Params):
        
        ''' Create logger to record results '''
        int_Level = 1
        str_Logger_Name = obj_Logging.strLogFile
        obj_Log_Results = self.func_Get_Func_Specific_Python_Logger(obj_Logging)
        ''' Log header '''
        str_Log_Line = str(globalsSS.StringDelimiters.static_stringDelimiter_RESULTS_START +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(True, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_UniqueID +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_File +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Logger +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_Gen_Headings +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_LD_Test +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_LD_Locus_Pair_1 +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_LD_Locus_Pair_2 +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_LD_Demoritization +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_LD_Batches +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_LD_Iterations +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_LD_P +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_LD_SE +
                           globalsSS.StringDelimiters.static_stringDelimiter +
                           self.Get_Log_Current_Column_Index(False, int_Level, True, self.str_ID_Suf) +
                           globalsSS.Genepop_Stats.static_Label_LD_Switches)
        obj_Log_Results.info(str_Log_Line)
        
        ''' Log results '''
        for key, value in dict_Results.iteritems():
            ((locus_pair), (p, se, switches)) = value
            str_Log_Line = str(globalsSS.StringDelimiters.static_stringDelimiter_RESULTS_START +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               self.objSSParametersLocal.strUniqueRunID +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               self.str_GP_Data_File +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str_Logger_Name +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               globalsSS.Genepop_Stats.static_Label_Gen_Results +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(key)  +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               locus_pair[0] +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               locus_pair[1] +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(list_Params[1]) +                               
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(list_Params[2]) +                               
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(list_Params[3]) +                               
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(p) +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(se) +
                               globalsSS.StringDelimiters.static_stringDelimiter + globalsSS.StringDelimiters.static_stringDelimiterSPACE +
                               str(switches))
            obj_Log_Results.info(str_Log_Line)
        pass
        
        ''' Clear the log handlers'''
        obj_Log_Results.handlers = []
                
        
        return True

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
    
    def Get_Log_Current_Column_Index_OLD(self, bool_Reset):
        
        if bool_Reset:
            self.str_Current_Col_Index = str('0' +
                                             globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                             '0' +
                                             globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                             '0')
        else:
            h, i, j = self.str_Current_Col_Index.split(globalsSS.StringDelimiters.static_stringDelimiter_DOT)
            
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
            
            self.str_Current_Col_Index = str(str(h) +
                                globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                str(i) +
                                globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                str(j))
        pass
    
        return self.str_Current_Col_Index

    '''
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Logger initilisation
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    '''
    def method_Get_Results_Logger(self, bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment):
    
        with FileHandler() as obj_File_Op:
            obj_File_Op.method_Create_Path(str_Logger_Path)
            
#         str_Logger_Name = self.objSSParametersLocal.strUniqueRunID + '_' + str_Logger_Name + str_Logger_FileName_Suffix
        str_Logger_Name = str_Logger_Name + str_Logger_FileName_Suffix
                        
        obj_Logging = Logging()
        obj_Logging.str_Logger_Name = str_Logger_Name
        obj_Logging.str_Logger_Level = 'info'
        obj_Logging.bool_ClearLogFileAtStart = True
        obj_Logging.bool_LogToConsole = bool_LogToConsole
        obj_Logging.bool_LogToFile = True
        obj_Logging.strLogPath = str_Logger_Path
        obj_Logging.strLogFile = str_Logger_Name
        #obj_Logging = self.func_Get_Func_Specific_Logger_Name(str_Logger_Path, str_Logger_Name)
    
        ''' Create logger to record results '''
        int_Level = 1
        str_Logger_Name = obj_Logging.strLogFile
        obj_Logging.func_Initialise_New_Logger()
        obj_Log_Results = logging__getLogger(obj_Logging.str_Logger_Name)
            
        ''' Check if logger already exists'''
        with FileHandler() as objFileOperation:
            boolFileExistsAtDestination = objFileOperation.fileExists(obj_Logging.strLogPath + '\\' + obj_Logging.strLogFile)
    
        return obj_Logging, obj_Log_Results
        
    def func_Get_Func_Specific_Logger_Name(self, str_Logger_Name): 
        
        obj_Logging = Logging()
        obj_Logging.str_Logger_Name = str_Logger_Name
        obj_Logging.str_Logger_Level = 'info'
        obj_Logging.bool_ClearLogFileAtStart = True
        obj_Logging.bool_LogToConsole = True
        obj_Logging.bool_LogToFile = True
        #obj_Logging.strLogPath = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\Shared_Data\\GP_Test\\BioP_Stats'
        obj_Logging.strLogPath = self.str_Log_Output_Path
        
        bool_Logger_Name_Found = False
        if bool_Logger_Name_Found == False:
            if str_Logger_Name == globalsSS.Logger_Details.static_Logger_Name__Genepop_HWE:
                bool_Logger_Name_Found = True
                str_File_Suffix = globalsSS.Logger_Details.static_Logger_File_Suffix__Genepop_HWE
            pass
        pass

        if bool_Logger_Name_Found == False:
            if str_Logger_Name == globalsSS.Logger_Details.static_Logger_Name__Genepop_Allele_Freq:
                bool_Logger_Name_Found = True
                str_File_Suffix = globalsSS.Logger_Details.static_Logger_File_Suffix__Genepop_Allele_Freq
            pass
        pass
    
        if bool_Logger_Name_Found == False:
            if str_Logger_Name == globalsSS.Logger_Details.static_Logger_Name__Genepop_He_All_Loci:
                bool_Logger_Name_Found = True
                str_File_Suffix = globalsSS.Logger_Details.static_Logger_File_Suffix__Genepop_He_All_Loci
            pass
        pass
    
        if bool_Logger_Name_Found == False:
            if str_Logger_Name == globalsSS.Logger_Details.static_Logger_Name__Genepop_LD:
                bool_Logger_Name_Found = True
                str_File_Suffix = globalsSS.Logger_Details.static_Logger_File_Suffix__Genepop_LD
            pass
        pass
    
        if bool_Logger_Name_Found == False:
            str_File_Suffix = '.txt'
            obj_Logging.strLogFile = self.objSSParametersLocal.strUniqueRunID + '_BioP_' + str_Logger_Name + str_File_Suffix
        pass

        str_Batch = str(self.objSSParametersLocal.intCurrentBatch)
        int_Batches = self.objSSParametersLocal.intBatches
        str_Rep = str(self.objSSParametersLocal.intCurrentReplicate)
        int_Reps = self.objSSParametersLocal.intBatches                       
        #+ str(str_Batch).zfill(int_Batches) + str(str_Rep).zfill(int_Reps)
    
        #obj_Logging.strLogFile = self.objSSParametersLocal.strUniqueRunID + '_BioP_' + str_Logger_Name + str_File_Suffix
        #obj_Logging.strLogFile = self.str_GP_Data_File + str_Logger_Name + '_' + str(str_Batch).zfill(int_Batches) + str(str_Rep).zfill(int_Reps) + str_File_Suffix
        str_GP_Filename = os__path.splitext(self.str_GP_Data_File)[0]
        #obj_Logging.strLogFile = str_GP_Filename + str_Logger_Name + '_' + str(str_Batch).zfill(int_Batches) + str(str_Rep).zfill(int_Reps) + str_File_Suffix
        obj_Logging.strLogFile = str_GP_Filename + str_Logger_Name + str_File_Suffix

        return obj_Logging
       
       
    def func_Get_Func_Specific_Python_Logger(self, obj_Logging): 
        
        obj_Logging.func_Initialise_New_Logger()
        obj_Log = logging__getLogger(obj_Logging.str_Logger_Name)
        
        return obj_Log
       
    