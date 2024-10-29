'''
Created on Jan 11, 2015

@author: VB-WIN7PRO64
'''

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS

#------------------< Import python modules
import ctypes
from ctypes import *
from logging import getLogger as logging__getLogger
#------------------< Import DCB_General modules
from FileHandler import FileHandler
from _ctypes import FreeLibrary
from handler_suppress_stdout_stderr import  suppress_stdout_stderr
#from handler_Logging import Logging

# #------------------< Import SharkSim modules
# #from globals_SharkSim import globalsSS
# from SSBatchHandler import SSBatchHandler
# from SSParameterHandler import SSParameterHandler
# from SSOutputHandler import SSOutputHandler
# import globals_SharkSim
# from _ctypes import Structure
# from ctypes import c_char_p, c_int8
# #from SSSamplingTest import SSSamplingTest 
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
gstringModuleName='object_SSNe2_Win_DLL.py'
gstringClassName='object_SSNe2_Win_DLL'

class object_SSNe2_Win_DLL(object):

    '''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Class Properties
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''            
    boolVB_Run = False
    bool_Suppress_ALL_LDNe_Console_Output = False
    libraryObject = None
    strNe2_Win_DLL_Program_Version = ''
    strNe2_Win_DLL_Program_Version = ''
    strNe2_Win_DLL_Name = ''
    strNe2_Win_DLL_Release_Type = ''
    strDLL_Path_And_File = ''

    obj_Ne2_Input_Params = None

    c_struct_Ne2_Input_Params = None
    c_struct_Ne2_Output = None

    
    '''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    DLL Constants
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''                    
          
    static_int_C_Integer_Undefined = -9999
      
#     '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Input File Format |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#     NE2_RUN_FILE_FORMAT__FSTAT = 1
#     NE2_RUN_FILE_FORMAT__GENEPOP = 2
#       
#     '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Output File Append |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#     NE2_RESULTS_FILE_NE__NOT_APPEND = 0
#     NE2_RESULTS_FILE_NE__APPEND = 1
#       
#     '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Output NUmber Indivs |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#     NE2_RUN_ALL_INDIVS = 0
#       
#     '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Output Pop Freq |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#     NE2_RUN_POP_FREQ_OUTPUT_ALL_POPS = -1
#     NE2_RUN_POP_FREQ_OUTPUT_NONE = 0
#       
#     '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Output CIs |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#     NE2_RUN_OUTPUT_PARAMETRIC_CIS__YES = 1
#     NE2_RUN_OUTPUT_PARAMETRIC_CIS__NO = 0
#     NE2_RUN_OUTPUT_JACKKNIFE_CIS__YES = 1
#     NE2_RUN_OUTPUT_JACKKNIFE_CIS__NO = 0 
#       
#       
#     NE2_LDNE_USE_TMP_FILE_OR_RAM__USE_RAM = 0
#     NE2_LDNE_USE_TMP_FILE_OR_RAM__USE_FILE = 1      
#                     
#     '''-------------------------------| Ne2 General Constants |-------------------------------'''    
#     
#     RUN_COMMAND_REPEAT__NO = "N"
#     RUN_COMMAND_REPEAT__YES = "Y"
    
#     MAX_OUTPUT_TABULAR_METHODS = 4
#     MAX_OUTPUT_BURROWS_POP = 3
#     MAX_OUTPUT_POPS = 2
#     MAX_OUTPUT_POP_FREQUENCY = 2
#     MAX_OUTPUT_LOCI_OMITTED_COUNT_OR_INCLUDED_RANGE_PAIRS = 100
#     MAX_OUTPUT_LOCI_OMITTED_BY_LOCUS_NUM = 100
       
    '''-------------------------------| Ne2 LDNe Constants |-------------------------------'''
    MAX_INPUT_FLOAT_ARRAY_PCRITS = 10
    
    
    '''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    DLL INPUT data structures
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''
    
    #obj_Ne2_Input_Params = None 
    
    '''~~~~~~~~~~~~| Define ctypes equivalent of C function args |~~~~~~~~~~~~'''
    class object_Ne2_Input_Params(object): 
    
        obj_Ne2_Input_Params__General_Run = None
        obj_Ne2_Input_Params__General_Processing = None
        obj_Ne2_Input_Params__Output_Properties = None
        obj_Ne2_Input_Params__Method_LDNe = None
                                    
        class object_Ne2_Input_Params__General_Run(object):
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run DLL linked      |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Ne2 running is controlled by an external program which supplies the run parameters
            bool_Run_DLL_Linked = True
            
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run DLL with DEBUG_ONLY_CODE |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Ne2 running will run code defined as DEBUG_ONLY_CODE.  IMPORTANT: Requires the DLL to have been compiled with #define DEBUG_ONLY_CODE in the global constants class
            bool_Run_DLL_With_DEBUG_ONLY_CODE = False
            
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run mode            |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #ie same as command line switches to control output processing e.g. "i: o:"
            char_Run_Command_Line_Switch = ''
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Method          |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # Ne estimation methods to run e.g LDNe, Temporal Ne
            int_Run_Methods = 0
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Path            |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #General working location
            char_Run_Path = ''
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Input           |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Input path & file details
            char_Run_InputDataFilePath = ''
            char_Run_InputDataFileName = ''
            int_Run_InputDataFile_Format = 0 #FSTAT or GENEPOP - set with constants
            char_Run_ID = '' # Unique ID identifying a batch of runs            
            int_Run_Count = 0 # Unique sequential number identifying each run #ALWAYS start from 1 NOT 0
            bool_Run_Last_Run = False # Flag to specify the final run. Only sets the finish time in the output #TRUE Indicates that this is the last run ina batch or runs
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output          |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Output path & standard output details            
            char_Run_OutputResultsPath = '' 
            char_Run_Standard_OutputResultsFile_NE = '' # This is the default output file of the Ne2 program
            bool_Run_Prevent_Standard_OutputResultsFile_NE = False; # Prevent this output, AND ASSOCIATED FILES e.g TAB delim, by setting to false
            int_Run_Standard_OutputResultsFile_NE_AppendResults = 0 # Append or overwrite this output
            char_Run_Repeat = ''
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Console Control |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Control console messaging
            bool_Run_Prevent_Console_Output = False  #If TRUE, prevent ALL console messages from displaying, ignoring in SPECIFIC console output permissions specificed by array_bool_Run_Prevent_Specific_Console_Output
            list_array_bool_Run_Prevent_Specific_Console_Output = [] # Each bool prevents specific console display block.
                       
        class object_Ne2_Input_Params__General_Processing(object):
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| General Processing Specifics |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # Specify individuals, populations and loci to be processed
            int_NumberOfIndividualsToBeprocessedPerPop = 0 # 0 = All
            int_NumberOfPopsToBeprocessed = 0 # 0 = All
            int_NumberOfLociToBeprocessed = 0 # 0 = All
            int_PopulationFrequencyOutput = 0 # -1 = Freq not specified
      
        class object_Ne2_Input_Params__Output_Properties(object):
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # Output file specifics

            #char_Output_FileName = ''
            #char_Output_FileName_Delimited_TAB = ''
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output Methods |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # TAB Delimited output method specific
            list_int_Output_Methods_As_TAB_Delimited = []
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output Data CIs |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Output data confidence interval specifics
            int_Output_CIs = 0
            int_Output_Parametric_CIs = 0
            int_Output_Jackknife_CIs = 0
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output Ranges |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Output data ranges
            list_int_Output_Pop_Frequency_Range = []
            list_int_Output_Burrows_Calcs_For_Pop_Range = []
            list_int_Output_Pop_Range = []
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output LOCI Ranges |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            '''
            Include LOCI ranges (by pairs) or Exclude a number or specific LOCI
        
            If only one number is given, it is the number of loci to be omitted, then
            the next line(s) should list omitted loci (ended by a non-digit character).
            If more than one entry are entered on line 8, then they should be entered
            in pairs on the same line, each pair is for a range of loci to be included.
            Examples:    pair 2 5 is for loci from 2 to 5; pair 9 9 is for locus 9.
    
            FURTHUR EXPLANATIION: Number of loci to be omitted (CASE 1) OR pairs of loci, defining ranges, of loci to be INCLUDED (CASE 2) (!)
            CASE 1: ie 2 <-- will omit two loci specified in Output_Loci_Omitted_By_Locus_Number
            CASE 2: ie 3,5,7,9 <-- will include loci 3,4,5, skip 6, and include loci 7,8,9
            For CASE 2 - Output_Loci_Omitted_By_Locus_Number will be ignored
            '''
            list_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs = []
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output SPECIFIC LOCI  |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Exclude SPECIFIC LOCI by their number (not name). Only used if struct_t__int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs is a single number otherwise ignored
            #C Array being passed to c std::vector
            list_int_Output_Loci_Omitted_By_Locus_Number = []                  
      
        class object_Ne2_Input_Params__Method_LDNe(object):
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| LD Method Output          |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Output file details        
            char_Output_FileName_Delimited_TAB = ''
            bool_Allow_Output_FileName_Delimited_TAB = True
            int_Output_FileName_Delimited_TAB_AppendResults = 0
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| LD Method Processing       |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #LDNe processing specifics                            
            int_LD_In_Param__Use_Temp_File_Or_RAM = 0
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~| LD Method Calculation      |~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #LDNe calculation specifics
            list_float_Array_PCrits = []
            int_Mating_Model = 0
    
        def __init__(self):
            
            self.obj_Ne2_Input_Params__General_Run = self.object_Ne2_Input_Params__General_Run()
            self.obj_Ne2_Input_Params__General_Processing = self.object_Ne2_Input_Params__General_Processing()
            self.obj_Ne2_Input_Params__Output_Properties = self.object_Ne2_Input_Params__Output_Properties()
            self.obj_Ne2_Input_Params__Method_LDNe = self.object_Ne2_Input_Params__Method_LDNe()
            pass
    
                                    
    #Complete INPUT object
    class struct_t__Ne2_Input_Params(ctypes.Structure):
          
          
        class struct_t__Ne2_Input_Params__General_Run(ctypes.Structure):
            
            '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Input File Format |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
            NE2_RUN_FILE_FORMAT__FSTAT = 1
            NE2_RUN_FILE_FORMAT__GENEPOP = 2

            '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Output File Append |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
            NE2_RESULTS_FILE_NE__NOT_APPEND = 0
            NE2_RESULTS_FILE_NE__APPEND = 1           
            
            MAX_OUTPUT_CONSOLE_SPECIFIC_OUTPUT = 7;  # This can be increased as console disply demand increase
             
            _fields_ = [
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run DLL linked      |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        #Ne2 running is controlled by an external program which supplies the run parameters
                        ("c_bool_Run_DLL_Linked", ctypes.c_bool),
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run DLL with DEBUG_ONLY_CODE |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        #Ne2 running will run code defined as DEBUG_ONLY_CODE.  IMPORTANT: Requires the DLL to have been compiled with #define DEBUG_ONLY_CODE in the global constants class
                        ("c_bool_Run_DLL_With_DEBUG_ONLY_CODE", ctypes.c_bool),
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run mode            |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        #ie same as command line switches to control output processing e.g. "i: o:"
                        ("c_char_Run_Command_Line_Switch", ctypes.c_char_p),
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Method          |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        # Ne estimation methods to run e.g LDNe, Temporal Ne
                        ("c_int_Run_Methods", ctypes.c_int),
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Path            |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        #General working location
                        ("c_char_Run_Path", ctypes.c_char_p),
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Input           |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        #Input path & file details
                        ("c_char_Run_InputDataFilePath", ctypes.c_char_p),
                        ("c_char_Run_InputDataFileName", ctypes.c_char_p),
                        ("c_int_Run_InputDataFile_Format", ctypes.c_int), #FSTAT or GENEPOP - set with constants
                        ("c_char_Run_ID", ctypes.c_char_p), # Unique ID identifying a batch of runs
                        ("c_int_Run_Count", ctypes.c_int), # Unique sequential number identifying each run
                        ("c_bool_Run_Last_Run", ctypes.c_bool), # Flag to specify the final run. Only sets the finish time in the output
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output          |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        #Output path & standard output details
                        ("c_char_Run_OutputResultsPath", ctypes.c_char_p),
                        ("c_char_Run_Standard_OutputResultsFile_NE", ctypes.c_char_p), # This is the default output file of the Ne2 program
                        ("c_bool_Run_Prevent_Standard_OutputResultsFile_NE", ctypes.c_bool), # Prevent this output, AND ASSOCIATED FILES e.g TAB delim, by setting to false
                        ("c_int_Run_Standard_OutputResultsFile_NE_AppendResults", ctypes.c_int), # Append or overwrite this output
                        ("c_char_Run_Repeat", ctypes.c_char_p),
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Console Control |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        #Control console messaging
                        ("c_bool_Run_Prevent_Console_Output", ctypes.c_bool), #If TRUE, prevent ALL console messages from displaying, ignoring in SPECIFIC console output permissions specificed by array_bool_Run_Prevent_Specific_Console_Output
                        ("c_array_bool_Run_Prevent_Specific_Console_Output", ctypes.c_bool*MAX_OUTPUT_CONSOLE_SPECIFIC_OUTPUT) # Each bool prevents specific console display block.
                        ]
    
      
        class struct_t__Ne2_Input_Params__General_Processing(ctypes.Structure):
            
            '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Output NUmber Indivs |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
            NE2_RUN_ALL_INDIVS = 0

            '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Output Pop Freq |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
            NE2_RUN_POP_FREQ_OUTPUT_ALL_POPS = -1
            NE2_RUN_POP_FREQ_OUTPUT_NONE = 0            
            
            _fields_ = [
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| General Processing Specifics |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        # Specify individuals, populations and loci to be processed
                        ("c_int_NumberOfIndividualsToBeprocessedPerPop", ctypes.c_int), # 0 = All
                        ("c_int_NumberOfPopsToBeprocessed", ctypes.c_int), # 0 = All
                        ("c_int_NumberOfLociToBeprocessed", ctypes.c_int), # 0 = All
                        ("c_int_PopulationFrequencyOutput", ctypes.c_int) # -1 = Freq not specified
                        ]
    
      
        class struct_t__Ne2_Input_Params__Output_Properties(ctypes.Structure):
              
            #Sub-structure of struct_Ne2_Input_Params__Output_Properties
            class struct_t__int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs(ctypes.Structure):
                
                MAX_OUTPUT_LOCI_OMITTED_COUNT_OR_INCLUDED_RANGE_PAIRS = 100
                            
                _fields_ = [
                            ("c_int_Size", ctypes.c_int),
                            ("c_array_int_Values", ctypes.c_int*MAX_OUTPUT_LOCI_OMITTED_COUNT_OR_INCLUDED_RANGE_PAIRS)
                            ]
    
      
            #Sub-structure of struct_Ne2_Input_Params__Output_Properties
            class struct_t__int_Output_Loci_Omitted_By_Locus_Number(ctypes.Structure):
                
                MAX_OUTPUT_LOCI_OMITTED_BY_LOCUS_NUM = 100
                
                _fields_ = [
                            ("c_int_Size", ctypes.c_int),
                            ("c_array_int_Values", ctypes.c_int*MAX_OUTPUT_LOCI_OMITTED_BY_LOCUS_NUM)
                            ]

            '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Output CIs |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
                
            MAX_OUTPUT_TABULAR_METHODS = 4
            MAX_OUTPUT_BURROWS_POP = 3
            MAX_OUTPUT_POPS = 2
            MAX_OUTPUT_POP_FREQUENCY = 2

            NE2_RUN_OUTPUT_PARAMETRIC_CIS__YES = 1
            NE2_RUN_OUTPUT_PARAMETRIC_CIS__NO = 0
            NE2_RUN_OUTPUT_JACKKNIFE_CIS__YES = 1
            NE2_RUN_OUTPUT_JACKKNIFE_CIS__NO = 0  
             
            RUN_COMMAND_REPEAT__NO = "N"
            RUN_COMMAND_REPEAT__YES = "Y" 
                                                                           
            _fields_ = [
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        # Output file specifics

                        #("c_char_Output_FileName", ctypes.c_char_p),
                        #("c_char_Output_FileName_Delimited_TAB", ctypes.c_char_p),
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output Methods |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        # TAB Delimited output method specific
                        #C array being passed to std:array 
                        ("c_array_int_Output_Methods_As_TAB_Delimited", ctypes.c_int*MAX_OUTPUT_TABULAR_METHODS),
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output Data CIs |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        #Output data confidence interval specifics
                        ("c_int_Output_CIs", ctypes.c_int),
                        ("c_int_Output_Parametric_CIs", ctypes.c_int),
                        ("c_int_Output_Jackknife_CIs", ctypes.c_int),
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output Ranges |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        #Output data ranges
                        #C array being passed to std:array
                        ("c_array_int_Output_Pop_Frequency_Range", ctypes.c_int*MAX_OUTPUT_POP_FREQUENCY),
                        #C array being passed to std:array
                        ("c_array_int_Output_Burrows_Calcs_For_Pop_Range", ctypes.c_int*MAX_OUTPUT_BURROWS_POP),
                        #C array being passed to std:array
                        ("c_array_int_Output_Pop_Range", ctypes.c_int*MAX_OUTPUT_POPS),
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output LOCI Ranges |~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                         '''
#                         Include LOCI ranges (by pairs) or Exclude a number or specific LOCI
#                     
#                         If only one number is given, it is the number of loci to be omitted, then
#                         the next line(s) should list omitted loci (ended by a non-digit character).
#                         If more than one entry are entered on line 8, then they should be entered
#                         in pairs on the same line, each pair is for a range of loci to be included.
#                         Examples:    pair 2 5 is for loci from 2 to 5; pair 9 9 is for locus 9.
#                 
#                         FURTHUR EXPLANATIION: Number of loci to be omitted (CASE 1) OR pairs of loci, defining ranges, of loci to be INCLUDED (CASE 2) (!)
#                         CASE 1: ie 2 <-- will omit two loci specified in Output_Loci_Omitted_By_Locus_Number
#                         CASE 2: ie 3,5,7,9 <-- will include loci 3,4,5, skip 6, and include loci 7,8,9
#                         For CASE 2 - Output_Loci_Omitted_By_Locus_Number will be ignored
#                         '''
                        #C Array being passed to c std::vector 
                        ("c_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs", struct_t__int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs),
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output SPECIFIC LOCI  |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        #Exclude SPECIFIC LOCI by their number (not name). Only used if struct_t__int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs is a single number otherwise ignored
                        #C Array being passed to c std::vector
                        ("c_struct_int_Output_Loci_Omitted_By_Locus_Number", struct_t__int_Output_Loci_Omitted_By_Locus_Number)
                        ]
      
      
        class struct_t__Ne2_Input_Params__Method_LDNe(ctypes.Structure):
              
            #Sub-structure of struct_t__Ne2_Input_Params__Method_LDNe
            class struct_t__float_Array_PCrits(ctypes.Structure):
                
                MAX_INPUT_FLOAT_ARRAY_PCRITS = 10
                
                _fields_ = [
                            ("c_int_Size", ctypes.c_int), # Number of PCrit values to analyse
                            ("c_array_float_Values", ctypes.c_float*MAX_INPUT_FLOAT_ARRAY_PCRITS) # PCrit values to analyse. Must have as many entries as specfied by int_Size
                            ]

            NE2_LDNE_USE_TMP_FILE_OR_RAM__USE_RAM = 0
            NE2_LDNE_USE_TMP_FILE_OR_RAM__USE_FILE = 1      
                              
            _fields_ = [
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| LD Method Output          |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        #Output file details
                        ("c_char_Output_FileName_Delimited_TAB", ctypes.c_char_p), # This is the LD method specifc TAB delimited output file
                        ("c_bool_Allow_Output_FileName_Delimited_TAB", ctypes.c_bool), # Prevent this output by setting to false
                        ("c_int_Output_FileName_Delimited_TAB_AppendResults", ctypes.c_int), # Append or overwrite this output
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| LD Method Processing       |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        #LDNe processing specifics
                        ("c_int_LD_In_Param__Use_Temp_File_Or_RAM", ctypes.c_int), # Use a temp file or keep variable is memory 
                        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| LD Method Calculation      |~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        #LDNe calculation specifics
                        ("c_struct_float_Array_PCrits", struct_t__float_Array_PCrits),
                        ("c_int_Mating_Model", ctypes.c_int) # RANDOM or MONOGAMY
                        ]
                              
      
        _fields_ = [
                    ("c_struct_Ne2_Input_Params__General_Run", struct_t__Ne2_Input_Params__General_Run),
                    ("c_struct_Ne2_Input_Params__General_Processing", struct_t__Ne2_Input_Params__General_Processing),
                    ("c_struct_Ne2_Input_Params__Output_Properties", struct_t__Ne2_Input_Params__Output_Properties),
                    ("c_struct_Ne2_Input_Params__Method_LDNe", struct_t__Ne2_Input_Params__Method_LDNe)
                    ]
              
    '''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    DLL OUTPUT data structures
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''
       
    class c_struct_t__Ne2_Output_LDNe(ctypes.Structure):
          
          
        '''~~~~~~~~~~~~| Define ctypes equivalent of C function return value |~~~~~~~~~~~~'''      
        class c_struct_t__Ne2_Output_LDNe_Procesing_Info(ctypes.Structure):
            _fields_ = [
                        ("c_intProcessingCount", ctypes.c_int),
                        ("c_strProcessingFileName", ctypes.c_char_p),
                        ("c_intProcesssingFileLoci", ctypes.c_int)
                        ]
      
        class c_struct_t__Ne2_Output_LDNe_Pop_Info(ctypes.Structure):
            _fields_ = [
                        ("c_intNeLoci", ctypes.c_int),
                        ("c_intNeSamples", ctypes.c_int),
                        ("c_strPopID", ctypes.c_char_p)
                        ]
      
        class c_struct_t__Ne2_Output_LDNe_Locus_Info(ctypes.Structure):
            _fields_ = [
                        ("c_intNeLoci", ctypes.c_int)
                        ]
      
        class c_struct_t__Ne2_Output_LDNe_Burrows_Info(ctypes.Structure):
            _fields_ = [
                        ("c_intMatingScheme", ctypes.c_int),
                        ("c_intIndependentAlleles", ctypes.c_int),
                        ("c_floatWeightedMeanSampleSize", ctypes.c_float),
                        ("c_floatPCrit", ctypes.c_float),
                        ("c_floatRSquared_Observed", ctypes.c_float),
                        ("c_floatRSquared_Expected", ctypes.c_float)
                        ]
      
        class c_struct_t__Ne2_Output_LDNe_Ne_Info(ctypes.Structure):
            _fields_ = [
                        ("c_floatLDNe", ctypes.c_float),
                        ("c_floatLDNeParametric_Lwr_CI", ctypes.c_float),
                        ("c_floatLDNeParametric_Upr_CI", ctypes.c_float),
                        ("c_floatLDNeJackknife_Lwr_CI", ctypes.c_float),
                        ("c_floatLDNeJackknife_Upr_CI", ctypes.c_float)
                        ]       
                          
      
        _fields_ = [
                    ("c_struct_Ne2_Output_LDNe_Procesing_Info", c_struct_t__Ne2_Output_LDNe_Procesing_Info),
                    ("c_struct_Ne2_Output_LDNe_Pop_Info", c_struct_t__Ne2_Output_LDNe_Pop_Info),
                    ("c_struct_Ne2_Output_LDNe_Locus_Info", c_struct_t__Ne2_Output_LDNe_Locus_Info),
                    ("c_struct_Ne2_Output_LDNe_Burrows_Info", c_struct_t__Ne2_Output_LDNe_Burrows_Info),
                    ("c_struct_Ne2_Output_LDNe_Ne_Info", c_struct_t__Ne2_Output_LDNe_Ne_Info)
                    ]
        
     
    
    def __init__(self, params):
        '''
        Constructor
        '''
        self.obj_Log_Default = logging__getLogger(__name__)
        self.obj_Log_Debug = logging__getLogger('app_debug')
        '''Prevent debug log output '''        
        self.bool_Allow_Log_Debug_Console_Output = False
        self.obj_Log_Debug.propagate = self.bool_Allow_Log_Debug_Console_Output 
        
        self.objSSParametersLocal = params[0]
        
        self.boolVB_Run = False
        self.bool_Suppress_ALL_LDNe_Console_Output = False #Suppresses everything irrelevant of all other settings
        self.libraryObject = None
        self.strNe2_Win_DLL_Program_Version = ''
        self.strNe2_Win_DLL_Name = ''
        self.strNe2_Win_DLL_Release_Type = ''
        self.strDLL_Path_And_File = ''
        
        self.obj_Ne2_Input_Params = object_SSNe2_Win_DLL.object_Ne2_Input_Params()
        
        self.c_struct_Ne2_Input_Params = None
        self.c_struct_Ne2_Output = None
        
        boolSuccess = False
        boolSuccess = self.func_Initialise()
        #boolSuccess = self.func_Initialise_Interface_Data_Structures()
        
        pass   


    def func_Initialise(self):
        
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        DLL Release
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        
        self.boolVB_Run = False
        self.strNe2_Win_DLL_Program_Version = 'v_1_9'
        self.strNe2_Win_DLL_Name = 'Ne2_Win_DLL.dll'

        bool_Run_DLL_With_DEBUG_ONLY_CODE = False
        self.obj_Ne2_Input_Params.bool_Run_DLL_With_DEBUG_ONLY_CODE = bool_Run_DLL_With_DEBUG_ONLY_CODE
        
        boolNe2_Win_DLL_Debug = False
        if boolNe2_Win_DLL_Debug:
            self.strNe2_Win_DLL_Release_Type = 'Debug'
        else:
            self.strNe2_Win_DLL_Release_Type = 'Release'
        pass
        
        self.strDLL_Path_And_File = ''    
                        
        '''
        VB or Non-VB DLL
        '''
        if self.boolVB_Run:
            self.strDLL_Path_And_File = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_VirtualBox\\MUI_A_VirtualBox_Shared\\MUI_A_VirtualBox_Shared_VB_Sync\\VS Projects\\Ne2_Win_DLL\\Ne2_Win_DLL_'+ self.strNe2_Win_DLL_Program_Version +'\\Ne2_Win_DLL\\x64\\' + self.strNe2_Win_DLL_Release_Type + '\\' + self.strNe2_Win_DLL_Name
        else:
            #self.strDLL_Path_And_File = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_VirtualBox\\MUI_A_VirtualBox_Shared\\MUI_A_VirtualBox_Shared_VB_Sync\\VS Projects\\Ne2_Win_DLL\\Ne2_Win_DLL_' + self.strNe2_Win_DLL_Program_Version + '\\Ne2_Win_DLL\\x64\\' + self.strNe2_Win_DLL_Release_Type + '\\' + self.strNe2_Win_DLL_Name
            self.strDLL_Path_And_File = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\Shared_Data\\Bin\\Ne2_Win_DLL\\Ne2_Win_DLL_' + self.strNe2_Win_DLL_Program_Version + '\\Ne2_Win_DLL\\x64\\' + self.strNe2_Win_DLL_Release_Type + '\\' + self.strNe2_Win_DLL_Name
            #self.strDLL_Path_And_File = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\Shared_Data\\Bin\\Ne2_Win_DLL\\Ne2_Win_DLL_' + strNe2_Win_DLL_Program_Version + '\\Ne2_Win_DLL\\x64\\' + strNe2_Win_DLL_Release_Type + '\\' + strNe2_Win_DLL_Name
        pass
    
        return True

    
    def func_Load_Library__Ne2_Win_DLL(self, strDLL_Path_And_File):
        
        
        '''~~~~~~~~~~~~| load DLL Library |~~~~~~~~~~~~'''
        self.obj_Log_Debug.debug('PYTHON DEBUG - !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        self.obj_Log_Debug.debug('PYTHON DEBUG - Attempting to load DLL : ' + strDLL_Path_And_File)
        self.obj_Log_Debug.debug('PYTHON DEBUG - NOTE - If this fails, check: ')
        self.obj_Log_Debug.debug('PYTHON DEBUG - (1) - The path to the DLL specified above is correct')
        self.obj_Log_Debug.debug('PYTHON DEBUG - (2) - All dependencies of the DLL are present in the source folder of the python project')
        self.obj_Log_Debug.debug('PYTHON DEBUG -       E.G. Ne2_Win_DLL requires msvcp120.dll & msvcr120 to be in the project source folder (or other PATH location)')
        self.obj_Log_Debug.debug('PYTHON DEBUG -       For Ne2_Win_DLL msvcp120.dll & msvcr120 can be found in the Depends sub-folder and can be copied to destination')
        self.obj_Log_Debug.debug('PYTHON DEBUG - !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        #Load it
        libraryReturnObject = ctypes.cdll.LoadLibrary(strDLL_Path_And_File)
        #libraryReturnObject = CDLL(strDLL_Path_And_File)
        
        if libraryReturnObject:
            self.obj_Log_Debug.debug("\n")
            self.obj_Log_Debug.debug('PYTHON DEBUG - Loaded DLL SUCCSSFULLY : ' + strDLL_Path_And_File)
            self.obj_Log_Debug.debug("\n")
        else:
            self.obj_Log_Debug.debug('!!!ERROR - DLL Failed to load - ERROR!!!')
            self.obj_Log_Debug.debug('!!!ERROR - DLL : ' + strDLL_Path_And_File + ' - !!!ERROR')
        pass
        
        return libraryReturnObject
        

    def func_Ne2_Win_DLL_Output_Processing(self, libraryObject, c_struct_Ne2_Input_Params):


        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Call DLL
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''


    
        '''~~~~~~~~~~~~| Get DLL function instance |~~~~~~~~~~~~'''
        libraryObject_Function_Ref = libraryObject.func_DLL_Export
          
        '''~~~~~~~~~~~~| Assign ctype to function object |~~~~~~~~~~~~''' #Assign a ctypes type to specify the result type of the foreign function
        #libraryObject_Function_Ref.restype = object_SSNe2_Win_DLL.c_struct_t__Ne2_Output_LDNe 
        libraryObject_Function_Ref.restype = self.c_struct_t__Ne2_Output_LDNe 
        
        c_struct_Ne2_Output_LDNe = libraryObject.func_DLL_Export(c_struct_Ne2_Input_Params)
            
        '''~~~~~~~~~~~~| Use DLL function results |~~~~~~~~~~~~'''
        strFunc = "func_DLL_Export_Output_Test_1"
        strReturnObject = "c_struct_Ne2_Output_LDNe"
        #
        strSubObject_1 = "c_struct_Ne2_Output_LDNe_Procesing_Info"
        self.obj_Log_Debug.debug("\n")
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Displaying Return Object - " + strReturnObject + " - START")
        
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Sub-object: " + strSubObject_1 + "...")
        self.obj_Log_Debug.debug("\n")
        self.obj_Log_Debug.debug("c_intProcessingCount        : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Procesing_Info.c_intProcessingCount))
        self.obj_Log_Debug.debug("c_strProcessingFileName     : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Procesing_Info.c_strProcessingFileName))
        self.obj_Log_Debug.debug("c_intProcesssingFileLoci    : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Procesing_Info.c_intProcesssingFileLoci))

        strSubObject_1 = "c_struct_Ne2_Output_LDNe_Pop_Info"
        self.obj_Log_Debug.debug("\n")
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Sub-object: " + strSubObject_1 + "...")
        self.obj_Log_Debug.debug("c_intNeLoci        : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Pop_Info.c_intNeLoci))
        self.obj_Log_Debug.debug("c_intNeSamples     : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Pop_Info.c_intNeSamples))
        self.obj_Log_Debug.debug("c_strPopID         : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Pop_Info.c_strPopID))
        
        strSubObject_1 = "c_struct_Ne2_Output_LDNe_Locus_Info"
        self.obj_Log_Debug.debug("\n")
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Sub-object: " + strSubObject_1 + "...")
        self.obj_Log_Debug.debug("c_intNeLoci        : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Locus_Info.c_intNeLoci))
        
        strSubObject_1 = "c_struct_Ne2_Output_LDNe_Burrows_Info"
        self.obj_Log_Debug.debug("\n")
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Sub-object: " + strSubObject_1 + "...")
        self.obj_Log_Debug.debug("c_intMatingScheme                : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Burrows_Info.c_intMatingScheme))
        self.obj_Log_Debug.debug("c_intIndependentAlleles          : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Burrows_Info.c_intIndependentAlleles))
        self.obj_Log_Debug.debug("c_floatWeightedMeanSampleSize    : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Burrows_Info.c_floatWeightedMeanSampleSize))
        self.obj_Log_Debug.debug("c_floatPCrit                     : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Burrows_Info.c_floatPCrit))
        self.obj_Log_Debug.debug("c_floatRSquared_Observed         : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Burrows_Info.c_floatRSquared_Observed))
        self.obj_Log_Debug.debug("c_floatRSquared_Expected         : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Burrows_Info.c_floatRSquared_Expected))
        
        strSubObject_1 = "c_struct_Ne2_Output_LDNe_Ne_Info"
        self.obj_Log_Debug.debug("\n")
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Sub-object: " + strSubObject_1 + "...")
        self.obj_Log_Debug.debug("c_floatLDNe                      : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Ne_Info.c_floatLDNe))
        self.obj_Log_Debug.debug("c_floatLDNeParametric_Lwr_CI     : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Ne_Info.c_floatLDNeParametric_Lwr_CI))
        self.obj_Log_Debug.debug("c_floatLDNeParametric_Upr_CI     : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Ne_Info.c_floatLDNeParametric_Upr_CI))
        self.obj_Log_Debug.debug("c_floatLDNeJackknife_Lwr_CI      : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Ne_Info.c_floatLDNeJackknife_Lwr_CI))
        self.obj_Log_Debug.debug("c_floatLDNeJackknife_Upr_CI      : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Ne_Info.c_floatLDNeJackknife_Upr_CI))
        
        strSubObject_1 = "c_struct_Ne2_Output_LDNe"
        self.obj_Log_Debug.debug("\n")
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Sub-object: " + strSubObject_1 + "...")
        self.obj_Log_Debug.debug("c_struct_Ne2_Output_LDNe_Procesing_Info  : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Procesing_Info))
        self.obj_Log_Debug.debug("c_struct_Ne2_Output_LDNe_Pop_Info        : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Pop_Info))
        self.obj_Log_Debug.debug("c_struct_Ne2_Output_LDNe_Locus_Info      : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Locus_Info))
        self.obj_Log_Debug.debug("c_struct_Ne2_Output_LDNe_Burrows_Info    : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Burrows_Info))
        self.obj_Log_Debug.debug("c_struct_Ne2_Output_LDNe_Ne_Info         : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Ne_Info))
        
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Displaying Return Object - " + strReturnObject + " - END")
        #DEBUG_OFF
        
        return c_struct_Ne2_Output_LDNe;


    def func_Ne2_Win_DLL_Input_Processing(self, boolTest):

        boolVB_Run = boolTest
                    
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        DLL INPUT variables
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''' 
         
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run DLL linked      |~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Ne2 running is controlled by an external program which supplies the run parameters 
        bool_Run_DLL_Linked = True
 
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run DLL with DEBUG_ONLY_CODE |~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Ne2 running will run code defined as DEBUG_ONLY_CODE.  IMPORTANT: Requires the DLL to have been compiled with #define DEBUG_ONLY_CODE in the global constants class
        bool_Run_DLL_With_DEBUG_ONLY_CODE = self.obj_Ne2_Input_Params.bool_Run_DLL_With_DEBUG_ONLY_CODE
         
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run mode            |~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #ie same as command line switches to control output processing e.g. "i: o:"
        char_Run_Command_Line_Switch = 'o:'

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Method          |~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Ne estimation methods to run e.g LDNe, Temporal Ne
        int_Run_Methods = 1
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Path            |~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #General working location        
        char_Run_Path = ""
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Input           |~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Input path & file details        
        '''
        VB or Non-VB DLL Run
        '''

        
        if boolVB_Run:
            strNe2_Win_DLL__Input_Data_Path = 'C:\\Users\\VB-WIN7PRO64\\Downloads\\VS Projects\\Ne2_Win_DLL\\Ne2_Win_DLL_'+ self.strNe2_Win_DLL_Program_Version +'\\Ne2_Win_DLL\\Ne2_Data\\In\\'
            strNe2_Win_DLL__Output_Data_Path = 'C:\\Users\\VB-WIN7PRO64\\Downloads\\VS Projects\\Ne2_Win_DLL\\Ne2_Win_DLL_'+ self.strNe2_Win_DLL_Program_Version +'\\Ne2_Win_DLL\\Ne2_Data\\Out\\'
            strNe2_Win_DLL__Input_Data_File = "CAOBWA_1.txt"
            strNe2_Win_DLL__Output_Data_File = "CAOBWA_LD_Out_TAB_V2.txt"

        else:
            boolTest = False
            intFolderCount = 0
            strWorkingFolder = str(intFolderCount) + '\\' + 'Ne2_DLL\\'
            #strFilePath_WorkingFolder = self.objSSParametersLocal.outfilePath + strWorkingFolder
            strFilePath_WorkingFolder = self.obj_Ne2_Input_Params.obj_Ne2_Input_Params__General_Run.char_Run_OutputResultsPath + strWorkingFolder
            if boolTest:
                #strFilePath_SharedFolder = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\Shared_Data\\'
                strFilePath_SharedFolder = "C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_VirtualBox\\MUI_A_VirtualBox_Shared\\MUI_A_VirtualBox_Shared_VB_Sync\\VS Projects\\Ne2_Win_DLL\\Ne2_Win_DLL_"+ self.strNe2_Win_DLL_Program_Version +"\\Ne2_Win_DLL\\Ne2_Data\\";
                strNe2_Win_DLL__Input_Data_Path = strFilePath_SharedFolder + "In\\"
                strNe2_Win_DLL__Output_Data_Path = strFilePath_SharedFolder + 'Out\\'
                #strNe2_Win_DLL__Output_Data_Path = strFilePath_WorkingFolder + 'Out\\'
                
                #strNe2_Win_DLL__Input_Data_File = "GsPy_GP_2014_11_08_17_14_AGL_B2_CAOB_X_14_43_49_Clean_V1_No_Pops_X_WA.gp_gspy"
                strNe2_Win_DLL__Input_Data_File = "CAOBWA_1.txt"
                strNe2_Win_DLL__Output_Data_File = "CAOBWA_LD_Out_TAB_V2.txt"
            else:
#                         strNe2_Win_DLL__Input_Data_Path = strFilePath_WorkingFolder + 'In\\'
#                         strNe2_Win_DLL__Output_Data_Path = strFilePath_WorkingFolder + 'Out\\'
                strNe2_Win_DLL__Input_Data_Path = self.obj_Ne2_Input_Params.obj_Ne2_Input_Params__General_Run.char_Run_InputDataFilePath
                strNe2_Win_DLL__Output_Data_Path = strFilePath_WorkingFolder + 'Out\\'
                
                strNe2_Win_DLL__Input_Data_File = self.obj_Ne2_Input_Params.obj_Ne2_Input_Params__General_Run.char_Run_InputDataFileName
                strNe2_Win_DLL__Output_Data_File = "Ne2_Std_Out.txt"
        pass

        #Create the OUTPUT folder if it doesnt exist
        with FileHandler() as objFileOperation:
            if objFileOperation.method_Path_Exists(strNe2_Win_DLL__Output_Data_Path) == False:
                objFileOperation.method_Create_Path(strNe2_Win_DLL__Output_Data_Path)
            pass
        pass
    

        int_Len_strNe2_Win_DLL__Input_Data_Path = len(strNe2_Win_DLL__Input_Data_Path)
        int_Len_strNe2_Win_DLL__Input_Data_Path_And_FileName = len(strNe2_Win_DLL__Input_Data_File) + int_Len_strNe2_Win_DLL__Input_Data_Path
        int_MaxLength = 258
        if int_Len_strNe2_Win_DLL__Input_Data_Path_And_FileName > int_MaxLength:
            self.obj_Log_Default.error('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            self.obj_Log_Default.error('strNe2_Win_DLL__Input_Data_Path &  strNe2_Win_DLL__Input_Data_File : ' + strNe2_Win_DLL__Input_Data_Path + '\\' + strNe2_Win_DLL__Input_Data_File)
            self.obj_Log_Default.error('IS TOO LONG: ' + str(int_Len_strNe2_Win_DLL__Input_Data_Path_And_FileName))
            self.obj_Log_Default.error('BY: ' + str(int_Len_strNe2_Win_DLL__Input_Data_Path_And_FileName - int_MaxLength) + ' CHARACTERS')
            self.obj_Log_Default.error('Ne2_Win_DLL will fail')
            self.obj_Log_Default.error('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            return False
        pass
        char_Run_InputDataFilePath = strNe2_Win_DLL__Input_Data_Path
        char_Run_InputDataFileName = strNe2_Win_DLL__Input_Data_File
    
        int_Run_InputDataFile_Format = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__General_Run.NE2_RUN_FILE_FORMAT__GENEPOP # FSTAT or GENEPOP - set with constants
        #char_Run_ID = self.objSSParametersLocal.strUniqueRunID + "_" # Unique ID identifying a batch of runs
        char_Run_ID = self.obj_Ne2_Input_Params.obj_Ne2_Input_Params__General_Run.char_Run_ID + "_" # Unique ID identifying a batch of runs
        #char_Run_ID = "Test_BATCH_RUn_ID_" # Unique ID identifying a batch of runs
        int_Run_Count = int(self.obj_Ne2_Input_Params.obj_Ne2_Input_Params__General_Run.int_Run_Count) # Unique sequential number identifying each run
        bool_Run_Last_Run = self.obj_Ne2_Input_Params.obj_Ne2_Input_Params__General_Run.bool_Run_Last_Run # Flag to specify the final run. Only sets the finish time in the output
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Output          |~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Output path & standard output details
        '''Validate length of path '''
        int_Len_char_Run_OutputResultsPath = len(strNe2_Win_DLL__Output_Data_Path)
        int_Len_char_Run_OutputStandardResultsPath_And_FileName = int_Len_char_Run_OutputResultsPath + len(strNe2_Win_DLL__Output_Data_File)
        int_MaxLength = 225
        if int_Len_char_Run_OutputStandardResultsPath_And_FileName > int_MaxLength:
            self.obj_Log_Default.error('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            self.obj_Log_Default.error('strNe2_Win_DLL__Output_Data_Path & strNe2_Win_DLL__Output_Data_File: ' + strNe2_Win_DLL__Output_Data_Path + '\\' + strNe2_Win_DLL__Output_Data_File)
            self.obj_Log_Default.error('IS TOO LONG: ' + str(int_Len_char_Run_OutputStandardResultsPath_And_FileName))
            self.obj_Log_Default.error('BY: ' + str(int_Len_char_Run_OutputStandardResultsPath_And_FileName - int_MaxLength) + ' CHARACTERS')
            self.obj_Log_Default.error('Ne2_Win_DLL will fail')
            self.obj_Log_Default.error('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            return False
        pass
        char_Run_OutputResultsPath = strNe2_Win_DLL__Output_Data_Path
        char_Run_Standard_OutputResultsFile_NE = strNe2_Win_DLL__Output_Data_File # This is the default output file of the Ne2 program
        
        #bool_Run_Prevent_Standard_OutputResultsFile_NE = self.obj_Ne2_Input_Params.obj_Ne2_Input_Params__General_Run.bool_Run_Prevent_Standard_OutputResultsFile_NE # Prevent this output, AND ASSOCIATED FILES e.g TAB delim, by setting to false
        bool_Run_Prevent_Standard_OutputResultsFile_NE = True # Prevent this output, AND ASSOCIATED FILES e.g TAB delim, by setting to false
        #bool_Run_Prevent_Standard_OutputResultsFile_NE = False # Prevent this output, AND ASSOCIATED FILES e.g TAB delim, by setting to false
        #int_Run_Standard_OutputResultsFile_NE_AppendResults = self.obj_Ne2_Input_Params.obj_Ne2_Input_Params__General_Run.int_Run_OutputResultsFile_NE_AppendResults # Append or overwrite this output
        if self.obj_Ne2_Input_Params.obj_Ne2_Input_Params__General_Run.int_Run_Count == 1:
            int_Run_Standard_OutputResultsFile_NE_AppendResults = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__General_Run.NE2_RESULTS_FILE_NE__NOT_APPEND
        else:
            int_Run_Standard_OutputResultsFile_NE_AppendResults = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__General_Run.NE2_RESULTS_FILE_NE__APPEND
        pass        
        #int_Run_Standard_OutputResultsFile_NE_AppendResults = 0
        char_Run_Repeat = "Y"
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~| Run Console Control |~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Control console messaging                
        #bool_Run_Prevent_Console_Output = False # If TRUE, prevent ALL console messages from displaying, ignoring in SPECIFIC console output permissions specificed by array_bool_Run_Prevent_Specific_Console_Output
        if self.bool_Suppress_ALL_LDNe_Console_Output: #Suppresses everything irrelevant of settings below
            bool_Run_Prevent_Console_Output = True # If TRUE, prevent ALL console messages from displaying, ignoring in SPECIFIC console output permissions specificed by array_bool_Run_Prevent_Specific_Console_Output
            list_array_bool_Run_Prevent_Specific_Console_Output = [True,True,True,True,True,True,True]  # Each bool prevents specific console display block.
        else:
            bool_Run_Prevent_Console_Output = False # If TRUE, prevent ALL console messages from displaying, ignoring in SPECIFIC console output permissions specificed by array_bool_Run_Prevent_Specific_Console_Output
            list_array_bool_Run_Prevent_Specific_Console_Output = [False,True,True,True,True,True,True]  # Each bool prevents specific console display block.
            #list_array_bool_Run_Prevent_Specific_Console_Output = [False,False,False,False,False,False,False]  # Each bool prevents specific console display block.
        pass
    
        #Initialise list with the correct number of array elements expected by DLL
        int_List_Max_Length = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__General_Run.MAX_OUTPUT_CONSOLE_SPECIFIC_OUTPUT
        int_List_Start_Length = len(list_array_bool_Run_Prevent_Specific_Console_Output)
        list_Extend = [False] * (int_List_Max_Length - int_List_Start_Length)
        list_array_bool_Run_Prevent_Specific_Console_Output.extend(list_Extend)
      
        struct_Ne2_Input_Params__General_Run = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__General_Run(
                                                     c_bool_Run_DLL_Linked = ctypes.c_bool(bool_Run_DLL_Linked)
                                                    ,c_bool_Run_DLL_With_DEBUG_ONLY_CODE = ctypes.c_bool(bool_Run_DLL_With_DEBUG_ONLY_CODE)
                                                    ,c_char_Run_Command_Line_Switch = ctypes.c_char_p(char_Run_Command_Line_Switch)
                                                    ,c_int_Run_Methods = ctypes.c_int(int_Run_Methods)
                                                    ,c_char_Run_Path = ctypes.c_char_p(char_Run_Path)
                                                    ,c_char_Run_InputDataFilePath = ctypes.c_char_p(char_Run_InputDataFilePath)
                                                    ,c_char_Run_InputDataFileName = ctypes.c_char_p(char_Run_InputDataFileName)
                                                    ,c_int_Run_InputDataFile_Format = ctypes.c_int(int_Run_InputDataFile_Format)
                                                    ,c_char_Run_ID = ctypes.c_char_p(char_Run_ID)
                                                    ,c_int_Run_Count = ctypes.c_int(int_Run_Count)
                                                    ,c_bool_Run_Last_Run = ctypes.c_bool(bool_Run_Last_Run)
                                                    ,c_char_Run_OutputResultsPath = ctypes.c_char_p(char_Run_OutputResultsPath)
                                                    ,c_char_Run_Standard_OutputResultsFile_NE = ctypes.c_char_p(char_Run_Standard_OutputResultsFile_NE)
                                                    ,c_bool_Run_Prevent_Standard_OutputResultsFile_NE = ctypes.c_bool(bool_Run_Prevent_Standard_OutputResultsFile_NE)
                                                    ,c_int_Run_Standard_OutputResultsFile_NE_AppendResults = ctypes.c_int(int_Run_Standard_OutputResultsFile_NE_AppendResults)
                                                    ,c_char_Run_Repeat = ctypes.c_char_p(char_Run_Repeat)
                                                    ,c_bool_Run_Prevent_Console_Output = ctypes.c_bool(bool_Run_Prevent_Console_Output)
                                                    ,c_array_bool_Run_Prevent_Specific_Console_Output = (ctypes.c_bool*len(list_array_bool_Run_Prevent_Specific_Console_Output))(*list_array_bool_Run_Prevent_Specific_Console_Output)
                                                    )
                                                                                       
                                                
        int_NumberOfIndividualsToBeprocessedPerPop = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__General_Processing.NE2_RUN_ALL_INDIVS # 0 = All
        int_NumberOfPopsToBeprocessed = 0
        int_NumberOfLociToBeprocessed = 0
        int_PopulationFrequencyOutput = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__General_Processing.NE2_RUN_POP_FREQ_OUTPUT_ALL_POPS

        struct_Ne2_Input_Params__General_Processing = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__General_Processing(
                                                             c_int_NumberOfIndividualsToBeprocessedPerPop = ctypes.c_int(int_NumberOfIndividualsToBeprocessedPerPop)
                                                            ,c_int_NumberOfPopsToBeprocessed = ctypes.c_int(int_NumberOfPopsToBeprocessed)
                                                            ,c_int_NumberOfLociToBeprocessed = ctypes.c_int(int_NumberOfLociToBeprocessed)
                                                            ,c_int_PopulationFrequencyOutput = ctypes.c_int(int_PopulationFrequencyOutput)
                                                            )
                        
        #char_Output_FileName = ""
        #char_Output_FileName_Delimited_TAB = ""
                         
        list_int_Output_Methods_As_TAB_Delimited = [1,0,1,1] #First number = sum of method(s) to have extra output : LD(= 1), Het(= 2), Coan(= 4), Temporal(= 8)
        #int_Output_Methods_As_TAB_Delimited[1] = 0 #First number = sum of method(s) to have extra output : LD(= 1), Het(= 2), Coan(= 4), Temporal(= 8)
        #int_Output_Methods_As_TAB_Delimited[2] = 1 #First number = sum of method(s) to have extra output : LD(= 1), Het(= 2), Coan(= 4), Temporal(= 8)
        #int_Output_Methods_As_TAB_Delimited[3] = 1 #First number = sum of method(s) to have extra output : LD(= 1), Het(= 2), Coan(= 4), Temporal(= 8)

        int_Output_CIs = 1
        int_Output_Parametric_CIs = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Output_Properties.NE2_RUN_OUTPUT_PARAMETRIC_CIS__YES #Parameter CI : 1 for Yes, 0 for No
        int_Output_Jackknife_CIs = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Output_Properties.NE2_RUN_OUTPUT_JACKKNIFE_CIS__YES #Jackknife CI : 1 for Yes, 0 for No

        list_int_Output_Pop_Frequency_Range = [-1,0] # First entry n1 = 0: No Freq output. If n1 = -1: Freq. output up to population 50. Two entries n1, n2 with n1 <= n2: Freq output for populations from n1 to n2. Max. populations to have Freq output is set at 50
        #int_Output_Pop_Frequency_Range[0] = -1 # First entry n1 = 0: No Freq output. If n1 = -1: Freq. output up to population 50. Two entries n1, n2 with n1 <= n2: Freq output for populations from n1 to n2. Max. populations to have Freq output is set at 50
        #int_Output_Pop_Frequency_Range[1] = 0 # First entry n1 = 0: No Freq output. If n1 = -1: Freq. output up to population 50. Two entries n1, n2 with n1 <= n2: Freq output for populations from n1 to n2. Max. populations to have Freq output is set at 50

        list_int_Output_Burrows_Calcs_For_Pop_Range = [-1,1,0] #For Burrow output file (up to 50 populations can have output). See remark below
        #int_Output_Burrows_Calcs_For_Pop_Range[0] = -1 #For Burrow output file (up to 50 populations can have output). See remark below
        #int_Output_Burrows_Calcs_For_Pop_Range[1] = 1 #For Burrow output file (up to 50 populations can have output). See remark below
        #int_Output_Burrows_Calcs_For_Pop_Range[2] = 0 #For Burrow output file (up to 50 populations can have output). See remark below

        list_int_Output_Pop_Range = [0,0] #Up to population, or range of populations to run(if 2 entries).If first entry = 0 : no restriction
        #int_Output_Pop_Range[0] = 0 #Up to population, or range of populations to run(if 2 entries).If first entry = 0 : no restriction
        #int_Output_Pop_Range[1] = 0 #Up to population, or range of populations to run(if 2 entries).If first entry = 0 : no restriction
        #int  Output_Loci_Omitted_Count # Number of loci to be omitted


        '''If only one number is given, it is the number of loci to be omitted, then
        the next line(s) should list omitted loci (ended by a non-digit character).
        If more than one entry are entered on line 8, then they should be entered
        in pairs on the same line, each pair is for a range of loci to be included.
        Examples:    pair 2 5 is for loci from 2 to 5 pair 9 9 is for locus 9.
        '''

        '''
        FURTHUR EXPLANATIION: Number of loci to be omitted (CASE 1) OR pairs of loci, defining ranges, of loci to be INCLUDED (CASE 2) (!)
        CASE 1: ie 2 <-- will omit two loci specified in Output_Loci_Omitted_By_Locus_Number
        CASE 2: ie 3,5,7,9 <-- will include loci 3,4,5, skip 6, and include loci 7,8,9
        For CASE 2 - Output_Loci_Omitted_By_Locus_Number will be ignored
        '''

        #KEEP_WHEN_COMMENTED
        # CASE 1 - # of loci to be OMITTED
        int_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Size = 1
        list_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Values = [0] # CASE 1 - 2 loci to be OMITTED
        #int_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Size = 1
        #list_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Values = [2] # CASE 1 - 2 loci to be OMITTED
        #KEEP_WHEN_COMMENTED

        #KEEP_WHEN_COMMENTED
        #CASE 2 - Pair range of loci to be INCLUDED
#                 int_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Size = 4
#                 list_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Values = [3,5,7,9] #CASE 2 - Pair range of loci to be INCLUDED
        #struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs.int_Values[0] = 3 CASE 2 - Pair range of loci to be INCLUDED
        #struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs.int_Values[1] = 5
        #struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs.int_Values[2] = 7
        #struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs.int_Values[3] = 9
        #KEEP_WHEN_COMMENTED

        #Initialise list with the correct number of array elements expected by DLL
        int_List_Max_Length = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Output_Properties.struct_t__int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs.MAX_OUTPUT_LOCI_OMITTED_COUNT_OR_INCLUDED_RANGE_PAIRS
        int_List_Start_Length = len(list_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Values)
        list_Extend = [self.static_int_C_Integer_Undefined] * (int_List_Max_Length - int_List_Start_Length)
        list_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Values.extend(list_Extend)
        
        
        struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Output_Properties.struct_t__int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs(
                                                                            c_int_Size = ctypes.c_int(int_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Size)
                                                                            ,c_array_int_Values = (ctypes.c_int*len(list_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Values))(*list_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Values)
                                                                            )




        int_struct_int_Output_Loci_Omitted_By_Locus_Number_int_Size = 2
        list_struct_int_Output_Loci_Omitted_By_Locus_Number_int_Values = [3,4] #Loci omitted
        #struct_int_Output_Loci_Omitted_By_Locus_Number.int_Values[0] = 3 #Loci omitted
        #struct_int_Output_Loci_Omitted_By_Locus_Number.int_Values[1] = 4 #Loci omitted
                        
        #Initialise list with the correct number of array elements expected by DLL
        int_List_Max_Length = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Output_Properties.struct_t__int_Output_Loci_Omitted_By_Locus_Number.MAX_OUTPUT_LOCI_OMITTED_BY_LOCUS_NUM
        int_List_Start_Length = len(list_struct_int_Output_Loci_Omitted_By_Locus_Number_int_Values)
        list_Extend = [self.static_int_C_Integer_Undefined] * (int_List_Max_Length - int_List_Start_Length)
        list_struct_int_Output_Loci_Omitted_By_Locus_Number_int_Values.extend(list_Extend)


        #DEBUG_OFF

        struct_int_Output_Loci_Omitted_By_Locus_Number = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Output_Properties.struct_t__int_Output_Loci_Omitted_By_Locus_Number(
                                                            c_int_Size = ctypes.c_int(int_struct_int_Output_Loci_Omitted_By_Locus_Number_int_Size)
                                                            ,c_array_int_Values = (ctypes.c_int*len(list_struct_int_Output_Loci_Omitted_By_Locus_Number_int_Values))(*list_struct_int_Output_Loci_Omitted_By_Locus_Number_int_Values)
                                                            )
                        
        #Initialise lists with the correct number of array elements expected by DLL
        int_List_Max_Length = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Output_Properties.MAX_OUTPUT_TABULAR_METHODS
        int_List_Start_Length = len(list_int_Output_Methods_As_TAB_Delimited)
        list_Extend = [self.static_int_C_Integer_Undefined] * (int_List_Max_Length - int_List_Start_Length)
        list_int_Output_Methods_As_TAB_Delimited.extend(list_Extend)

        int_List_Max_Length = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Output_Properties.MAX_OUTPUT_POP_FREQUENCY
        int_List_Start_Length = len(list_int_Output_Pop_Frequency_Range)
        list_Extend = [self.static_int_C_Integer_Undefined] * (int_List_Max_Length - int_List_Start_Length)
        list_int_Output_Pop_Frequency_Range.extend(list_Extend)
        
        int_List_Max_Length = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Output_Properties.MAX_OUTPUT_BURROWS_POP
        int_List_Start_Length = len(list_int_Output_Burrows_Calcs_For_Pop_Range)
        list_Extend = [self.static_int_C_Integer_Undefined] * (int_List_Max_Length - int_List_Start_Length)
        list_int_Output_Burrows_Calcs_For_Pop_Range.extend(list_Extend)
        
        int_List_Max_Length = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Output_Properties.MAX_OUTPUT_POPS
        int_List_Start_Length = len(list_int_Output_Pop_Range)
        list_Extend = [self.static_int_C_Integer_Undefined] * (int_List_Max_Length - int_List_Start_Length)
        list_int_Output_Pop_Range.extend(list_Extend)
                                        
        #Complete Output Properties object
        struct_Ne2_Input_Params__Output_Properties = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Output_Properties(
                                                         c_array_int_Output_Methods_As_TAB_Delimited = (ctypes.c_int*len(list_int_Output_Methods_As_TAB_Delimited))(*list_int_Output_Methods_As_TAB_Delimited)
                                                        ,c_int_Output_CIs = ctypes.c_int(int_Output_CIs)                                                        
                                                        ,c_int_Output_Parametric_CIs = ctypes.c_int(int_Output_Parametric_CIs)
                                                        ,c_int_Output_Jackknife_CIs = ctypes.c_int(int_Output_Jackknife_CIs)
                                                        ,c_array_int_Output_Pop_Frequency_Range = (ctypes.c_int*len(list_int_Output_Pop_Frequency_Range))(*list_int_Output_Pop_Frequency_Range)
                                                        ,c_array_int_Output_Burrows_Calcs_For_Pop_Range = (ctypes.c_int*len(list_int_Output_Burrows_Calcs_For_Pop_Range))(*list_int_Output_Burrows_Calcs_For_Pop_Range)
                                                        ,c_array_int_Output_Pop_Range = (ctypes.c_int*len(list_int_Output_Pop_Range))(*list_int_Output_Pop_Range)
                                                        #C Arrays being passed to c std::vector 
                                                        ,c_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs = struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs
                                                        ,c_struct_int_Output_Loci_Omitted_By_Locus_Number = struct_int_Output_Loci_Omitted_By_Locus_Number
                                                        ) 


        '''Validate length of path '''
        char_Output_FileName_Delimited_TAB = 'LDNe_TAB_Delim.txt'
        int_Len_char_Run_OutputResultsPath_And_FileName = int_Len_char_Run_OutputResultsPath + len(char_Output_FileName_Delimited_TAB)
        int_MaxLength = 225
        if int_Len_char_Run_OutputResultsPath_And_FileName > int_MaxLength:
            self.obj_Log_Default.error('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            self.obj_Log_Default.error('char_Run_OutputResultsPath & char_Output_FileName_Delimited_TAB: ' + strNe2_Win_DLL__Output_Data_Path + '\\' + char_Output_FileName_Delimited_TAB)
            self.obj_Log_Default.error('IS TOO LONG: ' + str(int_Len_char_Run_OutputResultsPath_And_FileName))
            self.obj_Log_Default.error('BY: ' + str(int_Len_char_Run_OutputResultsPath_And_FileName - int_MaxLength) + ' CHARACTERS')
            self.obj_Log_Default.error('Ne2_Win_DLL will fail')
            self.obj_Log_Default.error('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            return False
        else:
            char_Run_OutputResultsPath = strNe2_Win_DLL__Output_Data_Path
        pass     

        bool_Allow_Output_FileName_Delimited_TAB = True
        if self.obj_Ne2_Input_Params.obj_Ne2_Input_Params__General_Run.int_Run_Count == 1:
            int_Output_FileName_Delimited_TAB_AppendResults = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__General_Run.NE2_RESULTS_FILE_NE__NOT_APPEND
        else:
            int_Output_FileName_Delimited_TAB_AppendResults = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__General_Run.NE2_RESULTS_FILE_NE__APPEND
        pass
#         bool_Allow_Output_FileName_Delimited_TAB = False
#         int_Output_FileName_Delimited_TAB_AppendResults = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__General_Run.NE2_RESULTS_FILE_NE__NOT_APPEND
        
        int_LD_In_Param__Use_Temp_File_Or_RAM = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Method_LDNe.NE2_LDNE_USE_TMP_FILE_OR_RAM__USE_RAM
        int_struct_float_Array_PCrits_int_Size = 1
        #list_struct_float_Array_PCrits_int_Values = [0.02]
        list_struct_float_Array_PCrits_int_Values = self.obj_Ne2_Input_Params.obj_Ne2_Input_Params__Method_LDNe.list_float_Array_PCrits
        int_Mating_Model = 0

        #Initialise lists with the correct number of array elements expected by DLL
        int_List_Max_Length = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Method_LDNe.struct_t__float_Array_PCrits.MAX_INPUT_FLOAT_ARRAY_PCRITS
        int_List_Start_Length = len(list_struct_float_Array_PCrits_int_Values)
        list_Extend = [self.static_int_C_Integer_Undefined] * (int_List_Max_Length - int_List_Start_Length)
        list_struct_float_Array_PCrits_int_Values.extend(list_Extend)

        struct_float_Array_PCrits = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Method_LDNe.struct_t__float_Array_PCrits(
                                        c_int_Size = ctypes.c_int(int_struct_float_Array_PCrits_int_Size)
                                        ,c_array_float_Values = (ctypes.c_float*len(list_struct_float_Array_PCrits_int_Values))(*list_struct_float_Array_PCrits_int_Values)
                                        )

        struct_Ne2_Input_Params__Method_LDNe = self.struct_t__Ne2_Input_Params.struct_t__Ne2_Input_Params__Method_LDNe(
                                                     c_char_Output_FileName_Delimited_TAB = ctypes.c_char_p(char_Output_FileName_Delimited_TAB)
                                                    ,c_bool_Allow_Output_FileName_Delimited_TAB = ctypes.c_bool(bool_Allow_Output_FileName_Delimited_TAB)
                                                    ,c_int_Output_FileName_Delimited_TAB_AppendResults = ctypes.c_int(int_Output_FileName_Delimited_TAB_AppendResults)
                                                    ,c_int_LD_In_Param__Use_Temp_File_Or_RAM = ctypes.c_int(int_LD_In_Param__Use_Temp_File_Or_RAM)
                                                    ,c_struct_float_Array_PCrits = struct_float_Array_PCrits
                                                    ,c_int_Mating_Model = ctypes.c_int(int_Mating_Model)
                                                    )
                                                                                                               
        #Complete INPUT object
        struct_Ne2_Input_Params = self.struct_t__Ne2_Input_Params(
                                    c_struct_Ne2_Input_Params__General_Run = struct_Ne2_Input_Params__General_Run
                                    ,c_struct_Ne2_Input_Params__General_Processing = struct_Ne2_Input_Params__General_Processing
                                    ,c_struct_Ne2_Input_Params__Output_Properties = struct_Ne2_Input_Params__Output_Properties
                                    ,c_struct_Ne2_Input_Params__Method_LDNe = struct_Ne2_Input_Params__Method_LDNe
                                    ) 
                                

        return struct_Ne2_Input_Params
 
  
    def func_Test_Ne2_DLL_Test(self):

        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        DLL Release
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        boolVB_Run = False
        strNe2_Win_DLL_Program_Version = 'v_1_6'
        strNe2_Win_DLL_Name = 'Ne2_Win_DLL.dll'
        boolNe2_Win_DLL_Debug = True
        if boolNe2_Win_DLL_Debug:
            strNe2_Win_DLL_Release_Type = 'Debug'
        else:
            strNe2_Win_DLL_Release_Type = 'Release'

        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        DLL Constants
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''                    
            
        static_int_C_Integer_Undefined = -9999

        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Input File Format |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        NE2_RUN_FILE_FORMAT__FSTAT = 1
        NE2_RUN_FILE_FORMAT__GENEPOP = 2
    
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Output File Append |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        NE2_RESULTS_FILE_NE__NOT_APPEND = 0
        NE2_RESULTS_FILE_NE__APPEND = 1
        
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Output NUmber Indivs |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        NE2_RUN_ALL_INDIVS = 0
    
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Output Pop Freq |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        NE2_RUN_POP_FREQ_OUTPUT_ALL_POPS = -1
        NE2_RUN_POP_FREQ_OUTPUT_NONE = 0
    
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Ne2 Output CIs |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        NE2_RUN_OUTPUT_PARAMETRIC_CIS__YES = 1
        NE2_RUN_OUTPUT_PARAMETRIC_CIS__NO = 0
        NE2_RUN_OUTPUT_JACKKNIFE_CIS__YES = 1
        NE2_RUN_OUTPUT_JACKKNIFE_CIS__NO = 0 


        NE2_LDNE_USE_TMP_FILE_OR_RAM__USE_RAM = 0
        NE2_LDNE_USE_TMP_FILE_OR_RAM__USE_FILE = 1      
                      
        '''-------------------------------| Ne2 General Constants |-------------------------------'''    
        MAX_OUTPUT_TABULAR_METHODS = 4
        RUN_COMMAND_REPEAT__NO = "N"
        RUN_COMMAND_REPEAT__YES = "Y"
        MAX_OUTPUT_BURROWS_POP = 3
        MAX_OUTPUT_POPS = 2
        MAX_OUTPUT_POP_FREQUENCY = 2
        MAX_OUTPUT_LOCI_OMITTED_COUNT_OR_INCLUDED_RANGE_PAIRS = 100
        MAX_OUTPUT_LOCI_OMITTED_BY_LOCUS_NUM = 100

        '''-------------------------------| Ne2 LDNe Constants |-------------------------------'''
        MAX_INPUT_FLOAT_ARRAY_PCRITS = 10

        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        DLL INPUT variables
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
            
        '''~~~~~~~~~~~~| Define ctypes equivalent of C function args |~~~~~~~~~~~~'''
        class struct_t__Ne2_Input_Params__General_Run(Structure):
            _fields_ = [
                        ("c_char_Run_Command_Line_Switch", ctypes.c_char_p),
                        ("c_char_Run_Path", ctypes.c_char_p),
                        ("c_char_Run_InputDataFilePath", ctypes.c_char_p),
                        ("c_char_Run_InputDataFileName", ctypes.c_char_p),
                        ("c_char_Run_OutputResultsPath", ctypes.c_char_p),
                        ("c_char_Run_OutputResultsFile_NE", ctypes.c_char_p),
                        ("c_int_Run_InputDataFile_Format", ctypes.c_int),
                        ("c_int_Run_OutputResultsFile_NE_AppendResults", ctypes.c_int),
                        ("c_int_Run_Methods", ctypes.c_int),
                        ("c_char_Run_Repeat", ctypes.c_char_p),
                        ("c_bool_Run_Allow_Console_Output", ctypes.c_bool)
                        ]

        class struct_t__Ne2_Input_Params__General_Processing(Structure):
            _fields_ = [
                        ("c_int_NumberOfIndividualsToBeprocessedPerPop", ctypes.c_int),
                        ("c_int_NumberOfPopsToBeprocessed", ctypes.c_int),
                        ("c_int_NumberOfLociToBeprocessed", ctypes.c_int),
                        ("c_int_PopulationFrequencyOutput", ctypes.c_int)
                        ]

        #Sub-structure of struct_Ne2_Input_Params__Output_Properties
        class struct_t__int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs(Structure):
            _fields_ = [
                        ("c_int_Size", ctypes.c_int),
                        ("c_int_Values", ctypes.c_int*MAX_OUTPUT_LOCI_OMITTED_COUNT_OR_INCLUDED_RANGE_PAIRS)
                        ]
            
        #Sub-structure of struct_Ne2_Input_Params__Output_Properties
        class struct_t__int_Output_Loci_Omitted_By_Locus_Number(Structure):
            _fields_ = [
                        ("c_int_Size", ctypes.c_int),
                        ("c_int_Values", ctypes.c_int*MAX_OUTPUT_LOCI_OMITTED_BY_LOCUS_NUM)
                        ]
                                
        class struct_t__Ne2_Input_Params__Output_Properties(Structure):
            _fields_ = [
                        ("c_int_Output_CIs", ctypes.c_int),
                        ("c_char_Output_FileName", ctypes.c_char_p),
                        ("c_char_Output_FileName_Delimited_TAB", ctypes.c_char_p),
                        #C arrays being passed to std:array
                        ("c_int_Output_Methods_As_TAB_Delimited", ctypes.c_int*MAX_OUTPUT_TABULAR_METHODS),
                        ("c_int_Output_Pop_Frequency_Range", ctypes.c_int*MAX_OUTPUT_POP_FREQUENCY),
                        ("c_int_Output_Burrows_Calcs_For_Pop_Range", ctypes.c_int*MAX_OUTPUT_BURROWS_POP),
                        ("c_int_Output_Parametric_CIs", ctypes.c_int),
                        ("c_int_Output_Jackknife_CIs", ctypes.c_int),
                        ("c_int_Output_Pop_Range", ctypes.c_int*MAX_OUTPUT_POPS),
                        #C Arrays being passed to c std::vector 
                        ("c_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs", struct_t__int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs),
                        ("c_struct_int_Output_Loci_Omitted_By_Locus_Number", struct_t__int_Output_Loci_Omitted_By_Locus_Number)
                        ]

        #Sub-structure of struct_t__Ne2_Input_Params__Method_LDNe
        class struct_t__float_Array_PCrits(Structure):
            _fields_ = [
                        ("c_int_Size", ctypes.c_int),
                        ("c_int_Values", ctypes.c_int*MAX_INPUT_FLOAT_ARRAY_PCRITS)
                        ]

        class struct_t__Ne2_Input_Params__Method_LDNe(Structure):
            _fields_ = [
                        ("c_int_LD_In_Param__Use_Temp_File_Or_RAM", ctypes.c_int),
                        ("c_struct_float_Array_PCrits", struct_t__float_Array_PCrits),
                        ("c_int_Mating_Model", ctypes.c_int)
                        ]
                                
        #Complete INPUT object
        class struct_t__Ne2_Input_Params(Structure):
            _fields_ = [
                        ("c_struct_Ne2_Input_Params__General_Run", struct_t__Ne2_Input_Params__General_Run),
                        ("c_struct_Ne2_Input_Params__General_Processing", struct_t__Ne2_Input_Params__General_Processing),
                        ("c_struct_Ne2_Input_Params__Output_Properties", struct_t__Ne2_Input_Params__Output_Properties),
                        ("c_struct_Ne2_Input_Params__Method_LDNe", struct_t__Ne2_Input_Params__Method_LDNe)
                        ]
            
        #DEBUG_ON
        char_Run_Command_Line_Switch = 'o:'
        char_Run_Path = ""
        '''
        VB or Non-VB DLL Run
        '''

        if boolVB_Run:
            strNe2_Win_DLL__Input_Data_Path = 'C:\\Users\\VB-WIN7PRO64\\Downloads\\VS Projects\\Ne2_Win_DLL\\Ne2_Win_DLL_'+ strNe2_Win_DLL_Program_Version +'\\Ne2_Win_DLL\\Ne2_Data\\In\\'
            strNe2_Win_DLL__Output_Data_Path = 'C:\\Users\\VB-WIN7PRO64\\Downloads\\VS Projects\\Ne2_Win_DLL\\Ne2_Win_DLL_'+ strNe2_Win_DLL_Program_Version +'\\Ne2_Win_DLL\\Ne2_Data\\Out\\'
            strNe2_Win_DLL__Input_Data_File = "CAOBWA_1.txt"
            strNe2_Win_DLL__Output_Data_File = "CAOBWA_LD_Out_TAB_V2.txt"

        else:
            boolTest = True
            intFolderCount = 0
            strWorkingFolder = str(intFolderCount) + '\\' + 'Ne2_DLL\\'
            #strFilePath_WorkingFolder = self.objSSParametersLocal.outfilePath + strWorkingFolder
            strFilePath_WorkingFolder = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_VirtualBox\\MUI_A_VirtualBox_Shared\\VS Projects\\Projects\\Ne2_Win_DLL\\Ne2_Win_DLL_v_1_4\\Ne2_Win_DLL\Ne2_Data\\'
            if boolTest:
                strFilePath_SharedFolder = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\Shared_Data\\'
                strNe2_Win_DLL__Input_Data_Path = strFilePath_SharedFolder
                strNe2_Win_DLL__Output_Data_Path = strFilePath_WorkingFolder + 'Out\\'
                
                strNe2_Win_DLL__Input_Data_File = "GsPy_GP_2014_11_08_17_14_AGL_B2_CAOB_X_14_43_49_Clean_V1_No_Pops_X_WA.gp_gspy"
                #strNe2_Win_DLL__Input_Data_File = "CAOBWA_1.txt"
                strNe2_Win_DLL__Output_Data_File = "CAOBWA_LD_Out_TAB_V2.txt"
            else:
                
                strNe2_Win_DLL__Input_Data_Path = strFilePath_WorkingFolder + 'In\\'
                strNe2_Win_DLL__Output_Data_Path = strFilePath_WorkingFolder + 'Out\\'
        pass

        #Create the OUTPUT folder if it doesnt exist
        with FileHandler() as objFileOperation:
            if objFileOperation.method_Path_Exists(strNe2_Win_DLL__Output_Data_Path) == False:
                objFileOperation.method_Create_Path(strNe2_Win_DLL__Output_Data_Path)
            pass
        pass
    
        char_Run_InputDataFilePath = strNe2_Win_DLL__Input_Data_Path 
        char_Run_InputDataFileName = strNe2_Win_DLL__Input_Data_File
        char_Run_OutputResultsPath = strNe2_Win_DLL__Output_Data_Path
        char_Run_OutputResultsFile_NE = strNe2_Win_DLL__Output_Data_File
        int_Run_InputDataFile_Format = NE2_RUN_FILE_FORMAT__GENEPOP
        int_Run_OutputResultsFile_NE_AppendResults = NE2_RESULTS_FILE_NE__NOT_APPEND
        int_Run_Methods = 1
        char_Run_Repeat = "Y"
        bool_Run_Allow_Console_Output = False
        
        struct_Ne2_Input_Params__General_Run = struct_t__Ne2_Input_Params__General_Run(
                                                     c_char_Run_Command_Line_Switch = ctypes.c_char_p(char_Run_Command_Line_Switch)
                                                    ,c_char_Run_Path = ctypes.c_char_p(char_Run_Path)
                                                    ,c_char_Run_InputDataFilePath = ctypes.c_char_p(char_Run_InputDataFilePath)
                                                    ,c_char_Run_InputDataFileName = ctypes.c_char_p(char_Run_InputDataFileName)
                                                    ,c_char_Run_OutputResultsPath = ctypes.c_char_p(char_Run_OutputResultsPath)
                                                    ,c_char_Run_OutputResultsFile_NE = ctypes.c_char_p(char_Run_OutputResultsFile_NE)
                                                    ,c_int_Run_InputDataFile_Format = ctypes.c_int(int_Run_InputDataFile_Format)
                                                    ,c_int_Run_OutputResultsFile_NE_AppendResults = ctypes.c_int(int_Run_OutputResultsFile_NE_AppendResults)
                                                    ,c_int_Run_Methods = ctypes.c_int(int_Run_Methods)
                                                    ,c_char_Run_Repeat = ctypes.c_char_p(char_Run_Repeat)
                                                    ,c_bool_Run_Allow_Console_Output = ctypes.c_bool(bool_Run_Allow_Console_Output)
                                                    )
                                                                                       
                                                
        int_NumberOfIndividualsToBeprocessedPerPop = NE2_RUN_ALL_INDIVS # 0 = All
        int_NumberOfPopsToBeprocessed = 0
        int_NumberOfLociToBeprocessed = 0
        int_PopulationFrequencyOutput = NE2_RUN_POP_FREQ_OUTPUT_ALL_POPS

        struct_Ne2_Input_Params__General_Processing = struct_t__Ne2_Input_Params__General_Processing(
                                                             c_int_NumberOfIndividualsToBeprocessedPerPop = ctypes.c_int(int_NumberOfIndividualsToBeprocessedPerPop)
                                                            ,c_int_NumberOfPopsToBeprocessed = ctypes.c_int(int_NumberOfPopsToBeprocessed)
                                                            ,c_int_NumberOfLociToBeprocessed = ctypes.c_int(int_NumberOfLociToBeprocessed)
                                                            ,c_int_PopulationFrequencyOutput = ctypes.c_int(int_PopulationFrequencyOutput)
                                                            )
                        
        int_Output_CIs = 1
        char_Output_FileName = ""
        char_Output_FileName_Delimited_TAB = ""


                         
        list_int_Output_Methods_As_TAB_Delimited = [1,0,1,1] #First number = sum of method(s) to have extra output : LD(= 1), Het(= 2), Coan(= 4), Temporal(= 8)
        #int_Output_Methods_As_TAB_Delimited[1] = 0 #First number = sum of method(s) to have extra output : LD(= 1), Het(= 2), Coan(= 4), Temporal(= 8)
        #int_Output_Methods_As_TAB_Delimited[2] = 1 #First number = sum of method(s) to have extra output : LD(= 1), Het(= 2), Coan(= 4), Temporal(= 8)
        #int_Output_Methods_As_TAB_Delimited[3] = 1 #First number = sum of method(s) to have extra output : LD(= 1), Het(= 2), Coan(= 4), Temporal(= 8)

        list_int_Output_Pop_Frequency_Range = [-1,0] # First entry n1 = 0: No Freq output. If n1 = -1: Freq. output up to population 50. Two entries n1, n2 with n1 <= n2: Freq output for populations from n1 to n2. Max. populations to have Freq output is set at 50
        #int_Output_Pop_Frequency_Range[0] = -1 # First entry n1 = 0: No Freq output. If n1 = -1: Freq. output up to population 50. Two entries n1, n2 with n1 <= n2: Freq output for populations from n1 to n2. Max. populations to have Freq output is set at 50
        #int_Output_Pop_Frequency_Range[1] = 0 # First entry n1 = 0: No Freq output. If n1 = -1: Freq. output up to population 50. Two entries n1, n2 with n1 <= n2: Freq output for populations from n1 to n2. Max. populations to have Freq output is set at 50

        list_int_Output_Burrows_Calcs_For_Pop_Range = [-1,1,0] #For Burrow output file (up to 50 populations can have output). See remark below
        #int_Output_Burrows_Calcs_For_Pop_Range[0] = -1 #For Burrow output file (up to 50 populations can have output). See remark below
        #int_Output_Burrows_Calcs_For_Pop_Range[1] = 1 #For Burrow output file (up to 50 populations can have output). See remark below
        #int_Output_Burrows_Calcs_For_Pop_Range[2] = 0 #For Burrow output file (up to 50 populations can have output). See remark below

        int_Output_Parametric_CIs = NE2_RUN_OUTPUT_PARAMETRIC_CIS__YES #Parameter CI : 1 for Yes, 0 for No
        int_Output_Jackknife_CIs = NE2_RUN_OUTPUT_JACKKNIFE_CIS__YES #Jackknife CI : 1 for Yes, 0 for No

        list_int_Output_Pop_Range = [0,0] #Up to population, or range of populations to run(if 2 entries).If first entry = 0 : no restriction
        #int_Output_Pop_Range[0] = 0 #Up to population, or range of populations to run(if 2 entries).If first entry = 0 : no restriction
        #int_Output_Pop_Range[1] = 0 #Up to population, or range of populations to run(if 2 entries).If first entry = 0 : no restriction
        #int  Output_Loci_Omitted_Count # Number of loci to be omitted


        '''If only one number is given, it is the number of loci to be omitted, then
        the next line(s) should list omitted loci (ended by a non-digit character).
        If more than one entry are entered on line 8, then they should be entered
        in pairs on the same line, each pair is for a range of loci to be included.
        Examples:    pair 2 5 is for loci from 2 to 5 pair 9 9 is for locus 9.
        '''

        '''
        FURTHUR EXPLANATIION: Number of loci to be omitted (CASE 1) OR pairs of loci, defining ranges, of loci to be INCLUDED (CASE 2) (!)
        CASE 1: ie 2 <-- will omit two loci specified in Output_Loci_Omitted_By_Locus_Number
        CASE 2: ie 3,5,7,9 <-- will include loci 3,4,5, skip 6, and include loci 7,8,9
        For CASE 2 - Output_Loci_Omitted_By_Locus_Number will be ignored
        '''

        #KEEP_WHEN_COMMENTED
        # CASE 1 - # of loci to be OMITTED
        int_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Size = 1
        list_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Values = [2] # CASE 1 - 2 loci to be OMITTED
        #KEEP_WHEN_COMMENTED

        #KEEP_WHEN_COMMENTED
        #CASE 2 - Pair range of loci to be INCLUDED
        #int_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Size = 4
        #list_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Values = [3,5,7,9] #CASE 2 - Pair range of loci to be INCLUDED
        #struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs.int_Values[0] = 3 CASE 2 - Pair range of loci to be INCLUDED
        #struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs.int_Values[1] = 5
        #struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs.int_Values[2] = 7
        #struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs.int_Values[3] = 9
        #KEEP_WHEN_COMMENTED

        #Initialise list with the correct number of array elements expected by DLL
        int_List_Max_Length = MAX_OUTPUT_LOCI_OMITTED_COUNT_OR_INCLUDED_RANGE_PAIRS
        int_List_Start_Length = len(list_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Values)
        list_Extend = [static_int_C_Integer_Undefined] * (int_List_Max_Length - int_List_Start_Length)
        list_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Values.extend(list_Extend)
        
        
        struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs = struct_t__int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs(
                                                                            c_int_Size = ctypes.c_int(int_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Size)
                                                                            ,c_int_Values = (ctypes.c_int*len(list_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Values))(*list_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs_int_Values)
                                                                            #,c_int_Values = (ctypes.c_int*len(temp))(temp)
                                                                            )




        int_struct_int_Output_Loci_Omitted_By_Locus_Number_int_Size = 2
        list_struct_int_Output_Loci_Omitted_By_Locus_Number_int_Values = [3,4] #Loci omitted
        #struct_int_Output_Loci_Omitted_By_Locus_Number.int_Values[0] = 3 #Loci omitted
        #struct_int_Output_Loci_Omitted_By_Locus_Number.int_Values[1] = 4 #Loci omitted
                        
        #Initialise list with the correct number of array elements expected by DLL
        int_List_Max_Length = MAX_OUTPUT_LOCI_OMITTED_BY_LOCUS_NUM
        int_List_Start_Length = len(list_struct_int_Output_Loci_Omitted_By_Locus_Number_int_Values)
        list_Extend = [static_int_C_Integer_Undefined] * (int_List_Max_Length - int_List_Start_Length)
        list_struct_int_Output_Loci_Omitted_By_Locus_Number_int_Values.extend(list_Extend)


        #DEBUG_OFF

        struct_int_Output_Loci_Omitted_By_Locus_Number = struct_t__int_Output_Loci_Omitted_By_Locus_Number(
                                                            c_int_Size = ctypes.c_int(int_struct_int_Output_Loci_Omitted_By_Locus_Number_int_Size)
                                                            ,c_int_Values = (ctypes.c_int*len(list_struct_int_Output_Loci_Omitted_By_Locus_Number_int_Values))(*list_struct_int_Output_Loci_Omitted_By_Locus_Number_int_Values)
                                                            )
                        
        #Initialise lists with the correct number of array elements expected by DLL
        int_List_Max_Length = MAX_OUTPUT_TABULAR_METHODS
        int_List_Start_Length = len(list_int_Output_Methods_As_TAB_Delimited)
        list_Extend = [static_int_C_Integer_Undefined] * (int_List_Max_Length - int_List_Start_Length)
        list_int_Output_Methods_As_TAB_Delimited.extend(list_Extend)

        int_List_Max_Length = MAX_OUTPUT_POP_FREQUENCY
        int_List_Start_Length = len(list_int_Output_Pop_Frequency_Range)
        list_Extend = [static_int_C_Integer_Undefined] * (int_List_Max_Length - int_List_Start_Length)
        list_int_Output_Pop_Frequency_Range.extend(list_Extend)
        
        int_List_Max_Length = MAX_OUTPUT_BURROWS_POP
        int_List_Start_Length = len(list_int_Output_Burrows_Calcs_For_Pop_Range)
        list_Extend = [static_int_C_Integer_Undefined] * (int_List_Max_Length - int_List_Start_Length)
        list_int_Output_Burrows_Calcs_For_Pop_Range.extend(list_Extend)
        
        int_List_Max_Length = MAX_OUTPUT_POPS
        int_List_Start_Length = len(list_int_Output_Pop_Range)
        list_Extend = [static_int_C_Integer_Undefined] * (int_List_Max_Length - int_List_Start_Length)
        list_int_Output_Pop_Range.extend(list_Extend)
                                        
        #Complete Output Properties object
        struct_Ne2_Input_Params__Output_Properties = struct_t__Ne2_Input_Params__Output_Properties(
                                                        c_int_Output_CIs = ctypes.c_int(int_Output_CIs)
                                                        ,c_char_Output_FileName = ctypes.c_char_p(char_Output_FileName)
                                                        ,c_char_Output_FileName_Delimited_TAB = ctypes.c_char_p(char_Output_FileName_Delimited_TAB)
                                                        #C arrays being passed to std:array
                                                        #,c_int_Output_Methods_As_TAB_Delimited = ctypes.c_int*len(list_int_Output_Methods_As_TAB_Delimited)
                                                        ,c_int_Output_Methods_As_TAB_Delimited = (ctypes.c_int*len(list_int_Output_Methods_As_TAB_Delimited))(*list_int_Output_Methods_As_TAB_Delimited)
                                                        #,c_int_Output_Pop_Frequency_Range = ctypes.c_int*len(list_int_Output_Pop_Frequency_Range)
                                                        ,c_int_Output_Pop_Frequency_Range = (ctypes.c_int*len(list_int_Output_Pop_Frequency_Range))(*list_int_Output_Pop_Frequency_Range)
                                                        #,c_int_Output_Burrows_Calcs_For_Pop_Range = ctypes.c_int*len(list_int_Output_Burrows_Calcs_For_Pop_Range)
                                                        ,c_int_Output_Burrows_Calcs_For_Pop_Range = (ctypes.c_int*len(list_int_Output_Burrows_Calcs_For_Pop_Range))(*list_int_Output_Burrows_Calcs_For_Pop_Range)
                                                        ,c_int_Output_Parametric_CIs = ctypes.c_int(int_Output_Parametric_CIs)
                                                        ,c_int_Output_Jackknife_CIs = ctypes.c_int(int_Output_Jackknife_CIs)
                                                        #,c_int_Output_Pop_Range = ctypes.c_int*len(list_int_Output_Pop_Range)
                                                        ,c_int_Output_Pop_Range = (ctypes.c_int*len(list_int_Output_Pop_Range))(*list_int_Output_Pop_Range)
                                                        #C Arrays being passed to c std::vector 
                                                        ,c_struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs = struct_int_Output_Loci_OMITTED_Count_or_INCLUDED_Range_Pairs
                                                        ,c_struct_int_Output_Loci_Omitted_By_Locus_Number = struct_int_Output_Loci_Omitted_By_Locus_Number
                                                        ) 

        int_LD_In_Param__Use_Temp_File_Or_RAM = NE2_LDNE_USE_TMP_FILE_OR_RAM__USE_RAM
        int_struct_float_Array_PCrits_int_Size = 1
        list_struct_float_Array_PCrits_int_Values = [0.05]
        int_Mating_Model = 0

        #Initialise lists with the correct number of array elements expected by DLL
        int_List_Max_Length = MAX_INPUT_FLOAT_ARRAY_PCRITS
        int_List_Start_Length = len(list_struct_float_Array_PCrits_int_Values)
        list_Extend = [static_int_C_Integer_Undefined] * (int_List_Max_Length - int_List_Start_Length)
        list_struct_float_Array_PCrits_int_Values.extend(list_Extend)

        struct_float_Array_PCrits = struct_t__float_Array_PCrits(
                                        c_int_Size = ctypes.c_int(int_struct_float_Array_PCrits_int_Size)
                                        ,c_float_Values = (ctypes.c_float*len(list_struct_float_Array_PCrits_int_Values))(*list_struct_float_Array_PCrits_int_Values)
                                        )

        struct_Ne2_Input_Params__Method_LDNe = struct_t__Ne2_Input_Params__Method_LDNe(
                                                    c_int_LD_In_Param__Use_Temp_File_Or_RAM = ctypes.c_int(int_LD_In_Param__Use_Temp_File_Or_RAM)
                                                    ,c_struct_float_Array_PCrits = struct_float_Array_PCrits
                                                    ,c_int_Mating_Model = ctypes.c_int(int_Mating_Model)
                                                    )
                                                                                                               
        #Complete INPUT object
        struct_Ne2_Input_Params = struct_t__Ne2_Input_Params(
                                    c_struct_Ne2_Input_Params__General_Run = struct_Ne2_Input_Params__General_Run
                                    ,c_struct_Ne2_Input_Params__General_Processing = struct_Ne2_Input_Params__General_Processing
                                    ,c_struct_Ne2_Input_Params__Output_Properties = struct_Ne2_Input_Params__Output_Properties
                                    ,c_struct_Ne2_Input_Params__Method_LDNe = struct_Ne2_Input_Params__Method_LDNe
                                    ) 
                                

        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        DLL OUTPUT variables
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''

        '''~~~~~~~~~~~~| Define ctypes equivalent of C function return value |~~~~~~~~~~~~'''      
        class c_struct_t__Ne2_Output_LDNe_Procesing_Info(Structure):
            _fields_ = [
                        ("c_intProcessingCount", ctypes.c_int),
                        ("c_strProcessingFileName", ctypes.c_char_p),
                        ("c_intProcesssingFileLoci", ctypes.c_int)
                        ]

        class c_struct_t__Ne2_Output_LDNe_Pop_Info(Structure):
            _fields_ = [
                        ("c_intNeLoci", ctypes.c_int),
                        ("c_intNeSamples", ctypes.c_int),
                        ("c_strPopID", ctypes.c_char_p)
                        ]

        class c_struct_t__Ne2_Output_LDNe_Locus_Info(Structure):
            _fields_ = [
                        ("c_intNeLoci", ctypes.c_int)
                        ]

        class c_struct_t__Ne2_Output_LDNe_Burrows_Info(Structure):
            _fields_ = [
                        ("c_intMatingScheme", ctypes.c_int),
                        ("c_intIndependentAlleles", ctypes.c_int),
                        ("c_floatWeightedMeanSampleSize", ctypes.c_float),
                        ("c_floatPCrit", ctypes.c_float),
                        ("c_floatRSquared_Observed", ctypes.c_float),
                        ("c_floatRSquared_Expected", ctypes.c_float)
                        ]

        class c_struct_t__Ne2_Output_LDNe_Ne_Info(Structure):
            _fields_ = [
                        ("c_floatLDNe", ctypes.c_float),
                        ("c_floatLDNeParametric_Lwr_CI", ctypes.c_float),
                        ("c_floatLDNeParametric_Upr_CI", ctypes.c_float),
                        ("c_floatLDNeJackknife_Lwr_CI", ctypes.c_float),
                        ("c_floatLDNeJackknife_Upr_CI", ctypes.c_float)
                        ]       
                        
        class c_struct_t__Ne2_Output_LDNe(Structure):
            _fields_ = [
                        ("c_struct_Ne2_Output_LDNe_Procesing_Info", c_struct_t__Ne2_Output_LDNe_Procesing_Info),
                        ("c_struct_Ne2_Output_LDNe_Pop_Info", c_struct_t__Ne2_Output_LDNe_Pop_Info),
                        ("c_struct_Ne2_Output_LDNe_Locus_Info", c_struct_t__Ne2_Output_LDNe_Locus_Info),
                        ("c_struct_Ne2_Output_LDNe_Burrows_Info", c_struct_t__Ne2_Output_LDNe_Burrows_Info),
                        ("c_struct_Ne2_Output_LDNe_Ne_Info", c_struct_t__Ne2_Output_LDNe_Ne_Info)
                        ]

#                 '''
#                 !!!!!!!!!!!!!!!!!!!!
#                 DEBUG - INPUT Interface testing
#                 !!!!!!!!!!!!!!!!!!!!
#                 '''
#                 #DEBUG_ON
#                 '''~~~~~~~~~~~~| load DLL Library |~~~~~~~~~~~~'''
#                 dllNe2 = ctypes.cdll.LoadLibrary('C:\\Users\\VB-WIN7PRO64\\Downloads\\VS Projects\\Ne2_Win_DLL\\Ne2_Win_DLL_v_1_3\\Ne2_Win_DLL\\x64\\Debug\\Ne2_Win_DLL.dll')
# 
#                 '''~~~~~~~~~~~~| Get DLL function instance |~~~~~~~~~~~~'''
#                 dllNe2_new = dllNe2.func_DLL_Export_Test_1
#                 
#                 '''~~~~~~~~~~~~| Assign ctype to function object |~~~~~~~~~~~~''' #Assign a ctypes type to specify the result type of the foreign function
#                 dllNe2_new.restype = c_struct_t__Ne2_Output_LDNe 
# 
#                 c_struct_Ne2_Output_LDNe_Procesing_Info = dllNe2.c_struct_Ne2_Output_LDNe = dllNe2.func_DLL_Export_Input_Test_1(struct_Ne2_Input_Params__General_Run) 
#                 #DEBUG_OFF

        '''
        !!!!!!!!!!!!!!!!!!!!
        DEBUG - OUTPUT Interface testing
        !!!!!!!!!!!!!!!!!!!!
        '''
        #DEBUG_ON
#                 '''
#                 ---------------------------------
#                 Interface - c_struct_t__Ne2_Output_LDNe_Procesing_Info
#                 ---------------------------------
#                 '''
# 
#                 '''~~~~~~~~~~~~| load DLL Library |~~~~~~~~~~~~'''
#                 dllNe2 = ctypes.cdll.LoadLibrary('C:\\Users\\VB-WIN7PRO64\\Downloads\\VS Projects\\Ne2_Win_DLL\\Ne2_Win_DLL_v_1_3\\Ne2_Win_DLL\\x64\\Debug\\Ne2_Win_DLL.dll')
#  
#                 '''~~~~~~~~~~~~| Get DLL function instance |~~~~~~~~~~~~'''
#                 dllNe2_new = dllNe2.func_DLL_Export_Output_Test_1
#                  
#                 '''~~~~~~~~~~~~| Assign ctype to function object |~~~~~~~~~~~~''' #Assign a ctypes type to specify the result type of the foreign function
#                 dllNe2_new.restype = c_struct_t__Ne2_Output_LDNe_Procesing_Info 
#  
#                 c_struct_Ne2_Output_LDNe_Procesing_Info = dllNe2.func_DLL_Export_Output_Test_1(struct_Ne2_Input_Params) 
# 
#                 strFunc = "func_DLL_Export_Output_Test_1"
#                 strReturnObject = "c_struct_Ne2_Output_LDNe"
#                 strSubObject_1 = "c_struct_Ne2_Output_LDNe_Procesing_Info"
#                 print("PYTHON DEBUG - " + strFunc + " - Displaying Return Object - " + strReturnObject + " - START")
#                 print("PYTHON DEBUG - " + strFunc + " - Sub-object: " + strSubObject_1 + "...")
#                 print("c_intProcessingCount        : " + str(c_struct_Ne2_Output_LDNe_Procesing_Info.c_intProcessingCount))
#                 print("c_strProcessingFileName     : " + str(c_struct_Ne2_Output_LDNe_Procesing_Info.c_strProcessingFileName))
#                 print("c_intProcesssingFileLoci    : " + str(c_struct_Ne2_Output_LDNe_Procesing_Info.c_intProcesssingFileLoci))
#                 print("PYTHON DEBUG - " + strFunc + " - Displaying Return Object - " + strReturnObject + " - END")
        #DEBUG_OFF
        
        '''
        ---------------------------------
        Interface - c_struct_t__Ne2_Output_LDNe_Pop_Info
        ---------------------------------
        '''
        #DEBUG_ON
#                 '''~~~~~~~~~~~~| load DLL Library |~~~~~~~~~~~~'''
#                 dllNe2 = ctypes.cdll.LoadLibrary('C:\\Users\\VB-WIN7PRO64\\Downloads\\VS Projects\\Ne2_Win_DLL\\Ne2_Win_DLL_v_1_3\\Ne2_Win_DLL\\x64\\Debug\\Ne2_Win_DLL.dll')
#  
#                 '''~~~~~~~~~~~~| Get DLL function instance |~~~~~~~~~~~~'''
#                 dllNe2_new = dllNe2.func_DLL_Export_Output_Test_2
#                  
#                 '''~~~~~~~~~~~~| Assign ctype to function object |~~~~~~~~~~~~''' #Assign a ctypes type to specify the result type of the foreign function
#                 dllNe2_new.restype = c_struct_t__Ne2_Output_LDNe_Pop_Info 
#  
#                 c_struct_Ne2_Output_LDNe_Pop_Info = dllNe2.func_DLL_Export_Output_Test_2(struct_Ne2_Input_Params) 
#                 
#                 strFunc = "func_DLL_Export_Output_Test_2"
#                 strReturnObject = "c_struct_Ne2_Output_LDNe"
#                 strSubObject_1 = "c_struct_Ne2_Output_LDNe_Pop_Info"
#                 print("PYTHON DEBUG - " + strFunc + " - Displaying Return Object - " + strReturnObject + " - START")
#                 print("PYTHON DEBUG - " + strFunc + " - Sub-object: " + strSubObject_1 + "...")
#                 print("c_intNeLoci        : " + str(c_struct_Ne2_Output_LDNe_Pop_Info.c_intNeLoci))
#                 print("c_intNeSamples     : " + str(c_struct_Ne2_Output_LDNe_Pop_Info.c_intNeSamples))
#                 print("c_strPopID         : " + str(c_struct_Ne2_Output_LDNe_Pop_Info.c_strPopID))
#                 print("PYTHON DEBUG - " + strFunc + " - Displaying Return Object - " + strReturnObject + " - END")
        #DEBUG_OFF
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Call DLL
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''

        '''~~~~~~~~~~~~| load DLL Library |~~~~~~~~~~~~'''

            
        '''
        VB or Non-VB DLL
        '''
        if boolVB_Run:
            strDLL_Path_And_File = 'C:\\Users\\VB-WIN7PRO64\\Downloads\\VS Projects\\Ne2_Win_DLL\\Ne2_Win_DLL_'+ strNe2_Win_DLL_Program_Version +'\\Ne2_Win_DLL\\x64\\' + strNe2_Win_DLL_Release_Type + '\\' + strNe2_Win_DLL_Name
        else:
            #strDLL_Path_And_File = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_VirtualBox\\MUI_A_VirtualBox_Shared\\VS Projects\\Projects\\Ne2_Win_DLL\\Ne2_Win_DLL_' + strNe2_Win_DLL_Program_Version + '\\Ne2_Win_DLL\\x64\\' + strNe2_Win_DLL_Release_Type + '\\' + strNe2_Win_DLL_Name
            strDLL_Path_And_File = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\Shared_Data\\Bin\\Ne2_Win_DLL\\Ne2_Win_DLL_' + strNe2_Win_DLL_Program_Version + '\\Ne2_Win_DLL\\x64\\' + strNe2_Win_DLL_Release_Type + '\\' + strNe2_Win_DLL_Name
        pass
    
#         print("\n")
#         print('PYTHON DEBUG - Loading DLL : ' + strDLL_Path_And_File)
#         print("\n")
        self.obj_Log_Debug.debug('PYTHON DEBUG - Loading DLL : ' + strDLL_Path_And_File)

        #Load it
        #dllNe2 = ctypes.cdll.LoadLibrary('C:\\Users\\VB-WIN7PRO64\\Downloads\\VS Projects\\Ne2_Win_DLL\\Ne2_Win_DLL_v_1_3\\Ne2_Win_DLL\\x64\\Debug\\Ne2_Win_DLL.dll')
        dllNe2 = ctypes.cdll.LoadLibrary(strDLL_Path_And_File)
        
        if dllNe2:
            self.obj_Log_Debug.debug("\n")
            self.obj_Log_Debug.debug('PYTHON DEBUG - Loaded DLL : ' + strDLL_Path_And_File)
            self.obj_Log_Debug.debug("\n")
        else:
            self.obj_Log_Debug.debug('!!!ERROR - DLL Failed to load - ERROR!!!')
            self.obj_Log_Debug.debug('!!!ERROR - DLL : ' + strDLL_Path_And_File + ' - !!!ERROR')
        pass
    
        '''~~~~~~~~~~~~| Get DLL function instance |~~~~~~~~~~~~'''
        dllNe2_new = dllNe2.func_DLL_Export
          
        '''~~~~~~~~~~~~| Assign ctype to function object |~~~~~~~~~~~~''' #Assign a ctypes type to specify the result type of the foreign function
        dllNe2_new.restype = c_struct_t__Ne2_Output_LDNe 
          
        c_struct_Ne2_Output_LDNe = dllNe2.func_DLL_Export(struct_Ne2_Input_Params)
        
        '''~~~~~~~~~~~~| Use DLL function results |~~~~~~~~~~~~'''
        strFunc = "func_DLL_Export_Output_Test_1"
        strReturnObject = "c_struct_Ne2_Output_LDNe"
        #
        strSubObject_1 = "c_struct_Ne2_Output_LDNe_Procesing_Info"
        self.obj_Log_Debug.debug("\n")
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Displaying Return Object - " + strReturnObject + " - START")
        
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Sub-object: " + strSubObject_1 + "...")
        self.obj_Log_Debug.debug("\n")
        self.obj_Log_Debug.debug("c_intProcessingCount        : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Procesing_Info.c_intProcessingCount))
        self.obj_Log_Debug.debug("c_strProcessingFileName     : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Procesing_Info.c_strProcessingFileName))
        self.obj_Log_Debug.debug("c_intProcesssingFileLoci    : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Procesing_Info.c_intProcesssingFileLoci))

        strSubObject_1 = "c_struct_Ne2_Output_LDNe_Pop_Info"
        self.obj_Log_Debug.debug("\n")
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Sub-object: " + strSubObject_1 + "...")
        self.obj_Log_Debug.debug("c_intNeLoci        : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Pop_Info.c_intNeLoci))
        self.obj_Log_Debug.debug("c_intNeSamples     : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Pop_Info.c_intNeSamples))
        self.obj_Log_Debug.debug("c_strPopID         : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Pop_Info.c_strPopID))
        
        strSubObject_1 = "c_struct_Ne2_Output_LDNe_Locus_Info"
        self.obj_Log_Debug.debug("\n")
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Sub-object: " + strSubObject_1 + "...")
        self.obj_Log_Debug.debug("c_intNeLoci        : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Locus_Info.c_intNeLoci))
        
        strSubObject_1 = "c_struct_Ne2_Output_LDNe_Burrows_Info"
        self.obj_Log_Debug.debug("\n")
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Sub-object: " + strSubObject_1 + "...")
        self.obj_Log_Debug.debug("c_intMatingScheme                : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Burrows_Info.c_intMatingScheme))
        self.obj_Log_Debug.debug("c_intIndependentAlleles          : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Burrows_Info.c_intIndependentAlleles))
        self.obj_Log_Debug.debug("c_floatWeightedMeanSampleSize    : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Burrows_Info.c_floatWeightedMeanSampleSize))
        self.obj_Log_Debug.debug("c_floatPCrit                     : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Burrows_Info.c_floatPCrit))
        self.obj_Log_Debug.debug("c_floatRSquared_Observed         : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Burrows_Info.c_floatRSquared_Observed))
        self.obj_Log_Debug.debug("c_floatRSquared_Expected         : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Burrows_Info.c_floatRSquared_Expected))
        
        strSubObject_1 = "c_struct_Ne2_Output_LDNe_Ne_Info"
        self.obj_Log_Debug.debug("\n")
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Sub-object: " + strSubObject_1 + "...")
        self.obj_Log_Debug.debug("c_floatLDNe                      : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Ne_Info.c_floatLDNe))
        self.obj_Log_Debug.debug("c_floatLDNeParametric_Lwr_CI     : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Ne_Info.c_floatLDNeParametric_Lwr_CI))
        self.obj_Log_Debug.debug("c_floatLDNeParametric_Upr_CI     : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Ne_Info.c_floatLDNeParametric_Upr_CI))
        self.obj_Log_Debug.debug("c_floatLDNeJackknife_Lwr_CI      : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Ne_Info.c_floatLDNeJackknife_Lwr_CI))
        self.obj_Log_Debug.debug("c_floatLDNeJackknife_Upr_CI      : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Ne_Info.c_floatLDNeJackknife_Upr_CI))
        
        strSubObject_1 = "c_struct_Ne2_Output_LDNe"
        self.obj_Log_Debug.debug("\n")
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Sub-object: " + strSubObject_1 + "...")
        self.obj_Log_Debug.debug("c_struct_Ne2_Output_LDNe_Procesing_Info  : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Procesing_Info))
        self.obj_Log_Debug.debug("c_struct_Ne2_Output_LDNe_Pop_Info        : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Pop_Info))
        self.obj_Log_Debug.debug("c_struct_Ne2_Output_LDNe_Locus_Info      : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Locus_Info))
        self.obj_Log_Debug.debug("c_struct_Ne2_Output_LDNe_Burrows_Info    : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Burrows_Info))
        self.obj_Log_Debug.debug("c_struct_Ne2_Output_LDNe_Ne_Info         : " + str(c_struct_Ne2_Output_LDNe.c_struct_Ne2_Output_LDNe_Ne_Info))
        
        self.obj_Log_Debug.debug("PYTHON DEBUG - " + strFunc + " - Displaying Return Object - " + strReturnObject + " - END")
        #DEBUG_OFF
        
        return True;

    '''
    --------------------------------------------------------------------------------------------------------
    # Sub-Main Processing
    --------------------------------------------------------------------------------------------------------
    ''' 

    
    def func_Get_Ne2_Results(self):
        
        boolTest = False
        if boolTest:
            self.func_Test_Ne2_DLL_Test()
        else:
            self.c_struct_Ne2_Input_Params = self.func_Ne2_Win_DLL_Input_Processing(self.boolVB_Run)
            
            self.obj_Log_Debug.debug("\n")
            self.obj_Log_Debug.debug('PYTHON DEBUG - Loading DLL : ' + self.strDLL_Path_And_File)
            self.obj_Log_Debug.debug("\n")
    
            #self.libraryObject = self.func_Load_Library__Ne2_Win_DLL(self.strDLL_Path_And_File)
            
            self.c_struct_Ne2_Output = self.func_Ne2_Win_DLL_Output_Processing(self.libraryObject, self.c_struct_Ne2_Input_Params)
            
            #handle = self.libraryObject._handle # obtain the DLL handle

            #windll.kernel32.FreeLibrary(handle)
            #windll.kernel32.FreeLibrary.argtypes = [handle]
            #FreeLibrary(self.libraryObject)
            #self.obj_Log_Debug.debug("c_floatLDNe                      : " + str(self.c_struct_Ne2_Output.c_struct_Ne2_Output_LDNe_Ne_Info.c_floatLDNe))

        return True

 
    '''
    --------------------------------------------------------------------------------------------------------
    # Main Processing
    --------------------------------------------------------------------------------------------------------
    '''
               
    def method_Main(self):    
        
        
        bool_Test_Ne2_DLL = True
        if bool_Test_Ne2_DLL == True:
            
            boolSuccess = self.func_Test_Ne2_DLL_Test()

            pass
        pass 
        
        return True

