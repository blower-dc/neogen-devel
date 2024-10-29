'''
Created on 26/05/2014

@author: Dean
'''
#------------------< Import python modules
from datetime import datetime, timedelta
# DEBUG Imports
#import sys
#------------------< Import simupop modules
# PROD simuPOP
import simuPOP as sim

#------------------< Import DCB_General modules
from handler_Debug import Debug_Location as dcb_Debug_Location
#------------------< Import SharkSim modules
from object_SSRepProperty import object_SSPropertyHandler
from object_SSReportingProperty import object_SSReportingProperty
import globals_SharkSim


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< GLOBALS DEFINITION
global_dateTimeLastGeneralMessage = datetime

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
class globalsSS(object):
        
    class Shared_External_Resources(object):
        
        static_User_Programs_Folder = 'usr'
        static_Win_Binary_Folder_GENEPOP = 'Genepop'
        static_Win_Binary_Exe_GENEPOP = 'Genepop.exe'
        
        static_Win_DOS_Command_Scripts_Ne2Bulk = 'Ne2Bulk_Fresh'
        
        static_Win_DOS_Batch_Program__Ne2Bulk_ReRun_Failed__Path = 'Ne2Bulk_Fresh'
        
        static_Win_DOS_Batch_Program__Ne2Bulk_ReRun_Failed__Filename = "Ne2Bulk_ReRun_Failed_V1"
        static_Win_DOS_Batch_Program__Ne2Bulk_ReRun_Failed__FAILED_Process_File_Flag_Extension = '.FAILED'

        static_Win_Parameter_File__Ne_Estimator_Version_Exe = 'Ne_Estimator_Version_To_Use.param'
        static_Win_Binary_Exe_NE_ESTIMATOR_Version_2_0_0 = 'Ne2_0_0.exe'
        static_Win_Binary_Exe_NE_ESTIMATOR_Version_2_0_1 = 'Ne2_0_1.exe'
        static_Win_Binary_Exe_NE_ESTIMATOR_Version_2_1_0 = 'Ne2_1_0.exe'
        
    class Processing_Path(object):
        
        static_str_Processing_Path__Genepop_PF_Pop_Sample = 'BioP'
        static_str_Processing_Path__Pop_Sim = 'sim'
        static_str_Processing_Path__General_Logs = 'logs'
        static_str_Processing_Path__LDNe_Sampling_Strategy = 'sst'
        static_str_Processing_Path__Plots = 'plots'
        
    class Run_Processing_Step(object):
        
        static_str_Run_Processing_Step__POP_SIM = 'POP_SIM'
        static_str_Run_Processing_Step__SAMP_STRAT = 'SAMP_STRAT'
        
        static_int_Run_Processing_Step__POP_SIM = 0
        static_int_Run_Processing_Step__SAMP_STRAT = 1

    class App_File(object):
        
        static_str__App_File_Prefix__Settings = 'Settings'
        static_str__App_File_Prefix__Projects = 'Projects'
        static_str__App_File_Prefix__Project = 'Project'
        static_str__App_File_Prefix__Batch_Scenario = 'Batch_Scenario'
        static_str__App_File_Prefix__Batch_Settings = 'Batch_Settings'
        static_str__App_File_Prefix__Sampling_Strategy = 'Sampling_Strategy'

        static_str__App_File_Name__Thumbnail = 'thumb'
        
        static_str__App_File_Extension__Config_File = 'ini'
#         static_str__App_File_Extension__Image_File = 'png'

                        
#     class Debug(object):
#         
#         static_global_Debug = False
        
    class Logger_Run_Display(object):
        
        bool_Run_Display = True #You will not want to turn this off.
        
        static_Logger_File_Name__Run_Display = 'Run_Display_Log'
        static_Logger_Name__Run_Display = 'log_Run_Display'
        static_Logger_File_Suffix__Run_Display = '.log_Run_Display_ssim'
        
    class Logger_Default_Display(object):
        
        bool_Default_Display = True #You will not want to turn this off.
        
        static_Logger_File_Name__Default_Display = 'Default_Display_Log'
        static_Logger_Name__Default_Display = 'log_Default_Display'
        static_Logger_File_Suffix__Default_Display = '.log_Default_Display_ssim'
        
        static_Logger_bool_LogToConsole = True
        static_Logger_bool_LogToFile = True #You will not want to turn this off.
        
    class Logger_Error_Display(object):
        
        bool_Error_Display = True #You will not want to turn this off.
        
        static_Logger_File_Name__Error_Display = 'Error_Display_Log'
        static_Logger_Name__Error_Display = 'log_Error_Display'
        static_Logger_File_Suffix__Error_Display = '.log_Error_Display_ssim'

        static_Logger_bool_LogToConsole = False
        static_Logger_bool_LogToFile = False
        
        static_str_Logger_Message_Prefix = '!!ERR!!; '
        
    class Logger_Debug_Display(object):
        
        bool_Debug_Display = True #You will not want to turn this off.
        
        static_Logger_File_Name__Debug_Display = 'Debug_Display_Log'
        static_Logger_Name__Debug_Display = 'log_Debug_Display'
        static_Logger_File_Suffix__Debug_Display = '.log_Debug_Display_ssim'

        static_Logger_bool_LogToConsole = False
        static_Logger_bool_LogToFile = True #You will not want to turn this off.
        
        static_str_Logger_Message_Prefix = '>>; '
        
    class Logger_Debug_AgeNe(object):
        
        bool_Debug_AgeNe = True
        
        static_Logger_File_Name__Debug_AgeNe = 'Debug__AgeNe_Log'
        static_Logger_Name__Debug_AgeNe = 'log_Debug__AgeNe'
        static_Logger_File_Suffix__Debug_AgeNe = '.log_Debug__AgeNe_ssim'

        static_Logger_bool_LogToConsole = False
        static_Logger_bool_LogToFile = True

        static_str_Logger_Message_Prefix = '>>; '

    class Logger_Debug_Timing(object):
        
        bool_Debug_Timing_Override = False #Use this to just create the logger and use manually placed timers in the code
        
        bool_Debug_Timing = False #Use this to display timings on all functions that has this standard debug timer
        
        bool_Debug_Timing__Pause = False
        
        static_Logger_File_Name__Debug_Timing = 'Debug_Timing_Log'
        static_Logger_Name__Debug_Timing = 'log_Debug_Timing'
        static_Logger_File_Suffix__Debug_Timing = '.log_Debug_Timing_ssim'
        
    class Pause_Console(object): 
        
        def __init__(self):
            return None
        
        def __enter__(self):
            return self
                       
        def method_Pause_Console(self, str_Message='', bool_Location=True):
            bool_Kill_Switch_Off = True
            
            if bool_Kill_Switch_Off:
                
                str_Message += '>> '
                
                if bool_Location:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message += obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                pass
                if str_Message == '':
                    str_Message += ' << Pausing for output review -'
                pass
                
                
                raw_input('\n' + str_Message + ' << Press return to close this console window... \n')
            pass
        
            return True

        def __exit__(self, *args):
            return None

        
    class Output_Display_Constants(object):
        
        
        static_str_Does_Not_Compute = 'DNC'        
        
        static_str_Message_Separator = '-------------------------------------------------------------------------------------'        
        static_str_Message_Header = 'MH-------------------------------------------------------------------------------------MH'        
        static_str_Message_Footer = 'MF-------------------------------------------------------------------------------------MF'        

        static_str_Message_Separator_WARNING = '!!!!WARNING!!!!WARNING!!!!WARNING!!!!WARNING!!!!WARNING!!!!WARNING!!!!WARNING!!!!WARNING!!!!'
        
    class StringDelimiters(object):
        
        static_stringDelimiter = ';'
        static_stringDelimiter1 = '_'
        static_stringDelimiter2 = ','
        static_stringDelimiter3 = '|'
        static_stringDelimiterTAB = '\t'
        static_stringDelimiterSPACE = ' '
        static_stringDelimiter_SPACE = ' '
        static_stringDelimiter_RESULTS_START = '<>'
        static_stringDelimiter_DOT = '.'
        static_stringDelimiter_UNDERSCORE = '_'
        static_stringDelimiter_HYPHEN = '-'
        static_stringDelimiter_SEMI_COLON = ';'
        static_stringDelimiter_COMMA = ','
        
    class StringUnexpectedResults(object):
        
        static_stringError_Reporting_IDNotFound = 'ID_NOT_FOUND'
        static_stringNotApplicable = 'NA'
        static_stringSuppressed = 'SUP'
        static_stringError_ReportingPropertyNameNotFound = 'PROP NAME NOT FOUND'
        static_stringError_ReportingPropertyObjectNotFound = 'PROP NOT FOUND'
        static_stringError_ReportingPropertyLabelsNotFound = 'PROP LABELS NOT FOUND'

    class MatingParentSelectionScheme(object):
        
        static_Mating_Parent_Selection_Scheme_Gestating = 10
        static_Mating_Parent_Selection_Scheme_Resting = 11
        
    class MatingSchemeType(object):
    
        static_WF_Diploid_Sexual_Random_Mating = 0
        # - Standard Wright-Fisher diploid sexual random mating (includes a probability of 1/N hermaaphroditic matings)
        
        static_WF_Diploid_Sexual_Random_Mating_RANDOM_PARENT_CHOOSER = 0.1
        # - Standard Wright-Fisher diploid sexual random mating (includes a probability of 1/N hermaaphroditic matings)
        
        static_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_with_REPLACEMENT = 0.2
        # - Wright-Fisher diploid sexual random mating BUT parents can only be MALE/FEMALE unions. Parents can be chosen more than once.
        
        static_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_WITHOUT_REPLACEMENT = 0.3
        # - Wright-Fisher diploid sexual random mating BUT parents can only be MALE/FEMALE unions. Each parent can be chosen only once.
        
        static_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP = 1
        # SP - Uses simupop parent chooser
        # - Distinct sexes (dioecious). Random mating with replacement where one parent
        # This is is RANDOM Mating WITH replacement
        # may be randomly picked more than once to be a parent.
        # Parents of each sex are drawn randomly from sex-specific lists of adults and paired randomly.
        # Both sexes may have multiple mating opportunities with a randomly chosen partner.
        # This may not be biologically realistic if one female gives birth to more than a
        # biologically realistic number of multiple-paternities.  However this may only be a problem at low population sizes.
       
        static_Diploid_Monecious_Random_Mating_SP = 3
        # SP - Uses simupop parent chooser        
        # - NO Distinct sexes (monecious). Random mating with replacement where one parent may be randomly picked more than once to be a parent
        
        static_Diploid_Polygamous_Random_Mating_SP = 4
        # SP - Uses simupop parent chooser        
        # - Distinct sexes (diecious). Polyanderous Random mating with replacement where one parent may be randomly picked more than once to be a parent
        #MUST SPECIFY POLYGAMOUS MATE SEX AND NUM OF MATES
        
        static_Diploid_Dioecious_Polyandrous_Random_Mating_SP = 5
        # SP - Uses simupop parent chooser        
        # - Distinct sexes (diecious). Polyanderous Random mating with replacement where one parent may be randomly picked more than once to be a parent
        #MUST SPECIFY POLYGAMOUS MATE SEX AND NUM OF MATES
        
        static_Diploid_Dioecious_Random_Mating_WITH_Replacement = 10
        #Uses my parent chooser
        # - Distinct sexes (dioecious). Random mating with replacement where one parent
        # This is is RANDOM Mating WITH replacement
        # may be randomly picked more than once to be a parent.
        # Parents of each sex are drawn randomly from sex-specific lists of adults and paired randomly.
        # Both sexes may have multiple mating opportunities with a randomly chosen partner.
        # This may not be biologically realistic if one female gives birth to more than a
        # biologically realistic number of multiple-paternities.  However this may only be a problem at low population sizes.
        #2014-12-15 - Assuming this IS realistic as at larger population sizes this allows for a level of POLYAGAMOUS mating
        
        static_Diploid_Dioecious_Random_Mating_WITHOUT_Replacement = 11
        #Uses my parent chooser
        # - Distinct sexes (dioecious). Random mating WITHOUT replacement where a one parent
        # This is probably MONANDRY which is also SERIAL MONOGAMY
        # may only be be randomly picked only once to be a parent & parent pairs are fixed for that mating event.
        # A list of parent pairs is drawn from sequentially.  
        # If the pool of parent-pairs is exhausted before all offspring are created, the list is restarted.
        
        static_Diploid_Dioecious_Polyandrous_Random_Mating = 12
        #Uses my parent chooser
        # - Distinct sexes (dioecious). POLYANDRY - If more than male parent per female

        static_Diploid_Dioecious_Polygynous_Random_Mating = 13
        #Uses my parent chooser
        # - Distinct sexes (dioecious). POLYGYNY - If more than one female parent per male

        static_WF_Diploid_Sexual_Random_Mating_HARDCODED_1 = 20
        # - Standard Wright-Fisher diploid sexual random mating (includes a probability of 1/N hermaaphroditic matings)
        '''
        HARDCODED for: 
        Offspring Sex = 0.5 Prob of Males
        Num Offspring = 1
        VSP to mate = [(0,2)]
        '''

        ''' Two sexes mendelian random mating with replacement hermaphrodites allowed'''
        static_Diploid_Sexual_Random_Mating_LS_with_SELFING_with_REPLACEMENT = 21 

        ''' Two sexes mendelian random mating with replacement hermaphrodites allowed'''
        static_Diploid_Sexual_Random_Mating_LS_with_SELFING_with_REPLACEMENT_CONTROLLED_ALLELE_FREQS = 22 

        ''' Two sexes mendelian random mating with replacement hermaphrodites NOT allowed'''
        static_Diploid_Sexual_Random_Mating_LS_WITHOUT_SELFING_with_REPLACEMENT = 23

        ''' Two sexes mendelian random mating WITHOUT replacement hermaphrodites NOT allowed'''
        static_Diploid_Sexual_Random_Mating_LS_WITHOUT_SELFING_WITHOUT_REPLACEMENT = 24

        ''' Two sexes mendelian random POLYANDROUS mating (female polygamy) with replacement hermaphrodites NOT allowed'''
        static_Diploid_Sexual_Random_POLYANDROUS_Mating_LS_WITHOUT_SELFING_with_REPLACEMENT = 25
             
    class MatingOffspringSexModeSchemeType(object):
        
        ''' Uses a probability of male offspring to determine the M:F ratio of the embryo cohort '''
        static_int_Mating_Offspring_Sex_Mode_PROB_OF_MALES = 0
        
        ''' Strictly sets each sex to MALE and then FEMALE always resulting in and equal number of each sex in the embryo cohort '''  
        static_int_Mating_Offspring_Sex_Mode_GLOBAL_SEQ_OF_SEX_MF = 1
        
          
    class InitialAgeDistribution:
       
        #Individuals are initialized with ages that are evenly spread across all life stages
        #Each life stage has an approximately even number of individuals
        static_EvenAgeAndNumberSpreadAcrossLifeStages = 0
        #Individuals are initialized with random ages between 0 and maxAge.
        #Each life stage has a random number of individuals
        static_RandomAgeAndNumberSpreadAcrossLifeStages = 1
        #Individuals are initialized with the SAME AGE in each life stage as appropriate for that life stage
        #Each life stage has an approximately even number of individuals
        static_SameAgeAndEvenSpreadAcrossLifeStages_1CohortPerLifeStage = 2 
        
        
        static_SameAgeAndEvenSpreadAcrossLifeStages_1CohortPer12Months = 3
        
        
        static_Embryo_And_Mature_Only_1CohortPer12Months = 4
    
    class Allele_Frequency_Distribution:
        
        static_int_Allele_Frequency_Distribution_Distribution__NON_RANDOM = 0
        static_int_Allele_Frequency_Distribution_Distribution__ALL_ALLELE_FREQUENCIES_FILE = 1
        static_int_Allele_Frequency_Distribution_Distribution__DRICHLET = 2
        static_int_Allele_Frequency_Distribution_Distribution__GENEPOP_FILE = 4
        
    class Allele_Number_Per_Locus_Distribution:
        
        static_int_Allele_Number_Per_Locus_Distribution__UNIFORM = 0
        static_int_Allele_Number_Per_Locus_Distribution__NORMAL = 1
        static_int_Allele_Number_Per_Locus_Distribution__BINOMIAL = 2
        static_int_Allele_Number_Per_Locus_Distribution__ALL_ALLELE_FREQUENCIES_FILE = 3
        static_int_Allele_Number_Per_Locus_Distribution__GENEPOP_FILE = 4
        
        
    class SP_SubPops:
        
        static_intSP_SubPop_Primary = 0

    class VSP_Groups(object):
        
        static_VSP_Group_Age_Class = 'age_class'
        static_VSP_Group_Life_Stage = 'life_stage'
        
        def func_Get_VSP_Cohort_Group_From_VSP_Name(self, str_VSP_Name):
            
            if str_VSP_Name == self.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Juvenile:
                str_VSP_Cohort_Group = self.VSP_Groups.static_VSP_Group_Life_Stage
            elif str_VSP_Name == self.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Sub_adult:
                str_VSP_Cohort_Group = self.VSP_Groups.static_VSP_Group_Life_Stage
            elif str_VSP_Name == self.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult:
                str_VSP_Cohort_Group = self.VSP_Groups.static_VSP_Group_Life_Stage
            elif str_VSP_Name == self.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Gestating_adult_female:
                str_VSP_Cohort_Group = self.VSP_Groups.static_VSP_Group_Life_Stage
            elif str_VSP_Name == self.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Resting_adult_female:
                str_VSP_Cohort_Group = self.VSP_Groups.static_VSP_Group_Life_Stage
            else:
                str_VSP_Cohort_Group = self.VSP_Groups.static_VSP_Group_Age_Class
                
            return str_VSP_Cohort_Group

    class VSP_Life_Stage_Names(object):
        
        def func_Get_VSP_Name_From_VSP_Number(self, int_VSP_Number, int_VSP_Name_Length=1):
            
            if int_VSP_Number == globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo:
                if int_VSP_Name_Length == 0:
                    int_VSP_Name = globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Embryo
                elif int_VSP_Name_Length == 1:
                    int_VSP_Name = globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Embryo
                elif int_VSP_Name_Length == 2:
                    int_VSP_Name = globalsSS.VSP_LifeStage.static_stringLongNameVSP_LifeStage_Embryo
                else:
                    int_VSP_Name = globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo
                pass
#            elif int_VSP_Number == globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Neonate:
#                int_VSP_Name = globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Neonate
            elif int_VSP_Number == globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Juvenile:
                int_VSP_Name = globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Juvenile
#             elif int_VSP_Number == globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Sub_adult:
#                 int_VSP_Name = globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Sub_adult
            elif int_VSP_Number == globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult:
                int_VSP_Name = globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult
            elif int_VSP_Number == globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Gestating_adult_female:
                int_VSP_Name = globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Gestating_adult_female
            elif int_VSP_Number == globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Resting_adult_female:
                int_VSP_Name = globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Resting_adult_female
            elif int_VSP_Number == globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Senescent_adult:
                int_VSP_Name = globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Senescent_adult
            else:
                int_VSP_Name = globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Died
                
            return int_VSP_Name
        
    class VSP_AgeClass:

        static_intVSP_AgeClass_NumberofVSPs = 5
        
        #Age_class
        static_intVSP_AgeClass_Embryo = 0
        #static_intVSP_AgeClass_Neonate = 1
        static_intVSP_AgeClass_Juvenile = 1
        static_intVSP_AgeClass_Reproductivly_available_adult = 2
        static_intVSP_AgeClass_Senescent_adult = 3
        static_intVSP_AgeClass_Died = 4
        
        static_stringShortNameVSP_AgeClass_Embryo = 'AC00'
        #static_stringShortNameVSP_AgeClass_Neonate = 'AC01'
        static_stringShortNameVSP_AgeClass_Juvenile = 'AC01'
        static_stringShortNameVSP_AgeClass_Reproductivly_available_adult ='AC02'
        static_stringShortNameVSP_AgeClass_Senescent_adult = 'AC03'
        static_stringShortNameVSP_AgeClass_Died = 'AC04'
        
        static_stringMediumNameVSP_AgeClass_Embryo = 'Embryo'
        #static_stringMediumNameVSP_AgeClass_Neonate = 'Neonate'
        static_stringMediumNameVSP_AgeClass_Juvenile = 'Juvenile'
        static_stringMediumNameVSP_AgeClass_Reproductivly_available_adult = 'Mature'
        static_stringMediumNameVSP_AgeClass_Senescent_adult = 'Senescent'
        static_stringMediumNameVSP_AgeClass_Died = 'Died'
        
        static_stringLongNameVSP_AgeClass_Embryo = 'Unborn_Emryo'
        #static_stringLongNameVSP_AgeClass_Neonate = 'Neonate'
        static_stringLongNameVSP_AgeClass_Juvenile = 'Juvenile'
        static_stringLongNameVSP_AgeClass_Reproductivly_available_adult ='Reproductivly_available_adult'
        static_stringLongNameVSP_AgeClass_Senescent_adult = 'Senescent_adult'
        static_stringLongNameVSP_AgeClass_Died = 'Died'
    
        static_string_Age_Class_VSP_Name_Embryo = static_stringMediumNameVSP_AgeClass_Embryo
        #static_string_Age_Class_VSP_Name_Neonate = static_stringMediumNameVSP_AgeClass_Neonate
        static_string_Age_Class_VSP_Name_Juvenile = static_stringMediumNameVSP_AgeClass_Juvenile
        static_string_Age_Class_VSP_Name_Reproductivly_available_adult = static_stringMediumNameVSP_AgeClass_Reproductivly_available_adult
        static_string_Age_Class_VSP_Name_Senescent_adult = static_stringMediumNameVSP_AgeClass_Senescent_adult
        static_string_Age_Class_VSP_Name_Died = static_stringMediumNameVSP_AgeClass_Died

        static_stringSexMale = 'Male'
        static_string_Age_Class_VSP_Name_Embryo_Male = static_stringMediumNameVSP_AgeClass_Embryo + '_' + static_stringSexMale
        #static_string_Age_Class_VSP_Name_Neonate_Male = static_stringMediumNameVSP_AgeClass_Neonate + '_' + static_stringSexMale
        static_string_Age_Class_VSP_Name_Juvenile_Male = static_stringMediumNameVSP_AgeClass_Juvenile + '_' + static_stringSexMale
        static_string_Age_Class_VSP_Name_Reproductivly_available_adult_Male = static_stringMediumNameVSP_AgeClass_Reproductivly_available_adult + '_' + static_stringSexMale
        static_string_Age_Class_VSP_Name_Senescent_adult_Male = static_stringMediumNameVSP_AgeClass_Senescent_adult + '_' + static_stringSexMale
        static_string_Age_Class_VSP_Name_Died_Male = static_stringMediumNameVSP_AgeClass_Died + '_' + static_stringSexMale

        static_stringSexFemale = 'Female'
        static_string_Age_Class_VSP_Name_Embryo_Female = static_stringMediumNameVSP_AgeClass_Embryo + '_' + static_stringSexFemale
        #static_string_Age_Class_VSP_Name_Neonate_Female = static_stringMediumNameVSP_AgeClass_Neonate + '_' + static_stringSexFemale
        static_string_Age_Class_VSP_Name_Juvenile_Female = static_stringMediumNameVSP_AgeClass_Juvenile + '_' + static_stringSexFemale
        static_string_Age_Class_VSP_Name_Reproductivly_available_adult_Female = static_stringMediumNameVSP_AgeClass_Reproductivly_available_adult + '_' + static_stringSexFemale
        static_string_Age_Class_VSP_Name_Senescent_adult_Female = static_stringMediumNameVSP_AgeClass_Senescent_adult + '_' + static_stringSexFemale
        static_string_Age_Class_VSP_Name_Died_Female = static_stringMediumNameVSP_AgeClass_Died + '_' + static_stringSexFemale

    class VSP_LifeStage:

        static_intVSP_LifeStage_NumberofVSPs = 7

#         #Life_stage constants         
#         static_intVSP_LifeStage_Embryo = 0
#         #static_intVSP_LifeStage_Neonate = 1
#         static_intVSP_LifeStage_Juvenile = 2
#         #static_intVSP_LifeStage_Sub_adult = 3
#         static_intVSP_LifeStage_Reproductivly_available_adult = 4
#         static_intVSP_LifeStage_Gestating_adult_female = 5
#         static_intVSP_LifeStage_Resting_adult_female = 6
#         static_intVSP_LifeStage_Senescent_adult = 7
#         static_intVSP_LifeStage_Died = 8
        
        #Life_stage constants         
        static_intVSP_LifeStage_Embryo = 0
        #static_intVSP_LifeStage_Neonate = 1
        static_intVSP_LifeStage_Juvenile = 1
        #static_intVSP_LifeStage_Sub_adult = 3
        static_intVSP_LifeStage_Reproductivly_available_adult = 2
        static_intVSP_LifeStage_Gestating_adult_female = 3
        static_intVSP_LifeStage_Resting_adult_female = 4
        static_intVSP_LifeStage_Senescent_adult = 5
        static_intVSP_LifeStage_Died = 6
        
        static_stringShortNameVSP_LifeStage_Embryo = 'LS0' + str(static_intVSP_LifeStage_Embryo)
        #static_stringShortNameVSP_LifeStage_Neonate = 'LS0' + str(static_intVSP_LifeStage_Embryo)
        static_stringShortNameVSP_LifeStage_Juvenile = 'LS0' + str(static_intVSP_LifeStage_Embryo)
        #static_stringShortNameVSP_LifeStage_Sub_adult = 'LS0' + str(static_intVSP_LifeStage_Embryo)
        static_stringShortNameVSP_LifeStage_Reproductivly_available_adult ='LS0' + str(static_intVSP_LifeStage_Embryo)
        static_stringShortNameVSP_LifeStage_Gestating_adult_female = 'LS0' + str(static_intVSP_LifeStage_Embryo)
        static_stringShortNameVSP_LifeStage_Resting_adult_female = 'LS0' + str(static_intVSP_LifeStage_Embryo)
        static_stringShortNameVSP_LifeStage_Senescent_adult = 'LS0' + str(static_intVSP_LifeStage_Embryo)
        static_stringShortNameVSP_LifeStage_Died = 'LS0' + str(static_intVSP_LifeStage_Embryo)
        
        static_stringMediumNameVSP_LifeStage_Embryo = 'Embryo'
        #static_stringMediumNameVSP_LifeStage_Neonate = 'Neonate'
        static_stringMediumNameVSP_LifeStage_Juvenile = 'Juvenile'
        #static_stringMediumNameVSP_LifeStage_Sub_adult = 'Sub_adult'
        static_stringMediumNameVSP_LifeStage_Reproductivly_available_adult ='Mature'
        static_stringMediumNameVSP_LifeStage_Gestating_adult_female = 'Gestating'
        static_stringMediumNameVSP_LifeStage_Resting_adult_female = 'Resting'
        static_stringMediumNameVSP_LifeStage_Senescent_adult = 'Senescent'
        static_stringMediumNameVSP_LifeStage_Died = 'Died'
        
        static_stringLongNameVSP_LifeStage_Embryo = 'Unborn_Embryo'                
        #static_stringLongNameVSP_LifeStage_Neonate = 'Neonate'
        static_stringLongNameVSP_LifeStage_Juvenile = 'Juvenile'
        #static_stringLongNameVSP_LifeStage_Sub_adult = 'Sub_adult'
        static_stringLongNameVSP_LifeStage_Reproductivly_available_adult ='Reproductivly_available_adult'
        static_stringLongNameVSP_LifeStage_Gestating_adult_female = 'Gestating_adult_female'
        static_stringLongNameVSP_LifeStage_Resting_adult_female = 'Resting_adult_female'
        static_stringLongNameVSP_LifeStage_Senescent_adult = 'Senescent_adult'
        static_stringLongNameVSP_LifeStage_Died = 'Died'

        static_string_Life_Stage_VSP_Name_Embryo = static_stringMediumNameVSP_LifeStage_Embryo
        #static_string_Life_Stage_VSP_Name_Neonate = static_stringMediumNameVSP_LifeStage_Neonate
        static_string_Life_Stage_VSP_Name_Juvenile = static_stringMediumNameVSP_LifeStage_Juvenile
        #static_string_Life_Stage_VSP_Name_Sub_adult = static_stringMediumNameVSP_LifeStage_Sub_adult
        static_string_Life_Stage_VSP_Name_Reproductivly_available_adult = static_stringMediumNameVSP_LifeStage_Reproductivly_available_adult
        static_string_Life_Stage_VSP_Name_Gestating_adult_female = static_stringMediumNameVSP_LifeStage_Gestating_adult_female
        static_string_Life_Stage_VSP_Name_Resting_adult_female = static_stringMediumNameVSP_LifeStage_Resting_adult_female
        static_string_Life_Stage_VSP_Name_Senescent_adult = static_stringMediumNameVSP_LifeStage_Senescent_adult
        static_string_Life_Stage_VSP_Name_Died = static_stringMediumNameVSP_LifeStage_Died

        static_stringSexMale = 'Male'
        static_string_Life_Stage_VSP_Name_Embryo_Male = static_stringMediumNameVSP_LifeStage_Embryo + '_' + static_stringSexMale
        #static_string_Life_Stage_VSP_Name_Neonate_Male = static_stringMediumNameVSP_LifeStage_Neonate + '_' + static_stringSexMale
        static_string_Life_Stage_VSP_Name_Juvenile_Male = static_stringMediumNameVSP_LifeStage_Juvenile + '_' + static_stringSexMale
        #static_string_Life_Stage_VSP_Name_Sub_adult_Male = static_stringMediumNameVSP_LifeStage_Sub_adult + '_' + static_stringSexMale
        static_string_Life_Stage_VSP_Name_Reproductivly_available_adult_Male = static_stringMediumNameVSP_LifeStage_Reproductivly_available_adult + '_' + static_stringSexMale
        static_string_Life_Stage_VSP_Name_Gestating_adult_female_Male = static_stringMediumNameVSP_LifeStage_Gestating_adult_female + '_' + static_stringSexMale
        static_string_Life_Stage_VSP_Name_Resting_adult_female_Male = static_stringMediumNameVSP_LifeStage_Resting_adult_female + '_' + static_stringSexMale
        static_string_Life_Stage_VSP_Name_Senescent_adult_Male = static_stringMediumNameVSP_LifeStage_Senescent_adult + '_' + static_stringSexMale
        static_string_Life_Stage_VSP_Name_Died_Male = static_stringMediumNameVSP_LifeStage_Died + '_' + static_stringSexMale

        static_stringSexFemale = 'Female'
        static_string_Life_Stage_VSP_Name_Embryo_Female = static_stringMediumNameVSP_LifeStage_Embryo + '_' + static_stringSexFemale
        #static_string_Life_Stage_VSP_Name_Neonate_Female = static_stringMediumNameVSP_LifeStage_Neonate + '_' + static_stringSexFemale
        static_string_Life_Stage_VSP_Name_Juvenile_Female = static_stringMediumNameVSP_LifeStage_Juvenile + '_' + static_stringSexFemale
        #static_string_Life_Stage_VSP_Name_Sub_adult_Female = static_stringMediumNameVSP_LifeStage_Sub_adult + '_' + static_stringSexFemale
        static_string_Life_Stage_VSP_Name_Reproductivly_available_adult_Female = static_stringMediumNameVSP_LifeStage_Reproductivly_available_adult + '_' + static_stringSexFemale
        static_string_Life_Stage_VSP_Name_Gestating_adult_female_Female = static_stringMediumNameVSP_LifeStage_Gestating_adult_female + '_' + static_stringSexFemale
        static_string_Life_Stage_VSP_Name_Resting_adult_female_Female = static_stringMediumNameVSP_LifeStage_Resting_adult_female + '_' + static_stringSexFemale
        static_string_Life_Stage_VSP_Name_Senescent_adult_Female = static_stringMediumNameVSP_LifeStage_Senescent_adult + '_' + static_stringSexFemale
        static_string_Life_Stage_VSP_Name_Died_Female = static_stringMediumNameVSP_LifeStage_Died + '_' + static_stringSexFemale

        

    class Offspring_Number_Distribution_At_Mating:
        #(GEOMETRIC_DISTRIBUTION, p) EG [sim.GEOMETRIC_DISTRIBUTION, 0.9] gives a mean of 1.1 and a variance of 0.12
        #(POISSON_DISTRIBUTION, p), p > 0 EG [sim.POISSON_DISTRIBUTION, 1]
        #(BINOMIAL_DISTRIBUTION, p, N), 0 < p <=1, N > 0
        #(UNIFORM_DISTRIBUTION, a, b), 0 <= a <= b.  EG [sim.UNIFORM_DISTRIBUTION, 1, 2]
                    
        static_Offspring_Number_Distribution_At_Mating__ABSOLUTE_DISTRIBUTION = 0
        static_Offspring_Number_Distribution_At_Mating__POISSON_DISTRIBUTION = 1
        static_Offspring_Number_Distribution_At_Mating__BINOMIAL_DISTRIBUTION = 2
        static_Offspring_Number_Distribution_At_Mating__UNIFORM_DISTRIBUTION = 3
        static_Offspring_Number_Distribution_At_Mating__GEOMETRIC_DISTRIBUTION = 4
        
    class OffspringNumberDistributionModel_IndividualSpecific:
        '''
        AGE_FIXED_NUMBER: Number of offpring is fixed for each age from Min mating age to Max mating age
            e.g (AGE=10, #OFFPRING=1), (AGE=11, #OFFPRING=2), (A12, O3), (A13, O4) etc
        AGE_RANDOM: Number of offspring is randomly chosen 
        AGE_RANDOM_WEIGHTED: Number of offspring is randomly chosen but olders ages are weighted towards more offspring    
            e.g. Weight/Age:    10    11    12    14    14    15
                 Random chance of having x,x+1 offspring increase with weight/age
        AGE_FIXED_PROBABILITY: A probablity distribution is provided for each age from min mating age to max mating age.
            The number of offspring is determined by the age-specifc probability dist for the individual in question
            e.g. Age 10
                 #Offspring:        1      2      3      4
                 P(offspring):    0.1    0.4    0.4    0.1
                 Probability of randomly having 2 or 3 offspring is higher than the random probability of having 1 or 4 offsping
        '''
        
        static_OffspringNumberDistributionModel_IndividualSpecific_AGE_FIXED_NUMBER = 0
        static_OffspringNumberDistributionModel_IndividualSpecific_AGE_RANDOM = 1
        static_OffspringNumberDistributionModel_IndividualSpecific_AGE_RANDOM_WEIGHTED = 2
        static_OffspringNumberDistributionModel_IndividualSpecific_AGE_FIXED_PROBABILITY = 3

    class MortalitySource:
        '''
        What type of mortality is it?
        NATRUAL = Ordinary day-to-day sudden death
        UNNATURAL = Anthropogenic mortality e.g Fishing
        '''
        static_intMortalityType_NATURAL = 0
        static_intMortalityType_UnNATURAL = 1
        static_intMortalityType_COMBINED = 2

        static_strMortalityType_NATURAL = 'NATURAL'
        static_strMortalityType_UnNATURAL = 'UnNATURAL'
        static_strMortalityType_COMBINED = 'COMBINED'

    class MortalityApplication:
        
        static_str_Mating_Mortlity_Starts__Nat = 'Mating_Mortality_Starts__Nat'
        static_str_Mating_Mortlity_Starts__UnNat = 'Mating_Mortality_Starts__UnNat'

        '''NOTE: These are currently not implemented '''
        static_str_Mortality_Application_Model__Nat = 'Mortality_Application_Model__Nat' 
        static_str_Mortality_Application_Model__UnNat = 'Mortality_Application_Model__UnNat' 
        
        ''' Abs number of individuals given by (1-Survival rate)*Mortality_Scaling_Total__UnNat '''
        static_str_Mortality_Scaling_Total__Nat = 'Mortality_Scaling_Total__Nat'
        static_str_Mortality_Scaling_Total__UnNat = 'Mortality_Scaling_Total__UnNat'
        
    class MortalityNumberDistributionModel_IndividualSpecific:
        '''
        AGE_FIXED_NUMBER: Number of deaths ar fixed for each age from 0 to MaxAge
            e.g (AGE=10, #DEATHS=1), (AGE=11, #DEATHS=2), (A12, D3), (A13, D4) etc
        AGE_RANDOM: Number of deaths are randomly chosen 
        Not applicable - AGE_RANDOM_WEIGHTED: Number of deaths are randomly chosen but older ages are weighted towards more offspring    
            e.g. Weight/Age:    10    11    12    14    14    15
                 Random chance of having x,x+1 offspring increase with weight/age
        AGE_FIXED_PROBABILITY: A probablity distribution is provided for each age from 0 to MaxAge.
            The number of deaths in each age group is determined by the age-specifc probability dist for the age of each individual in question
            A coin weighted with the probability of death (specifed by age) is flipped for each individual
            e.g. Age 10
                 Age               0      1      2      3  etc
                 P(offspring):    0.1    0.2    0.2    0.1 etc = 1
                 Probabilty of death at age 1 is 20%
        '''
        
        static_MortalityNumberDistributionModel_IndividualSpecific_AGE_FIXED_NUMBER = 0
        static_MortalityNumberDistributionModel_IndividualSpecific_AGE_RANDOM = 1
        static_MortalityNumberDistributionModel_IndividualSpecific_AGE_RANDOM_WEIGHTED = 2
        static_MortalityNumberDistributionModel_IndividualSpecific_AGE_FIXED_PROBABILITY = 3
        static_MortalityNumberDistributionModel_IndividualSpecific_AGE_FIXED_PROBABILITY_SCALED = 4

#     class ObjectSSSimulationPropertyLabels:
#         
#         '''
#         E.g.         lisPropertyLabels =['Property_Name','Property_Label_Long','Property_Label_Short''Property_Label_Abreviation','Property_Label_Units',Property_Label_Default_Label_Key'}
#         '''
#         
#         with object_SSPropertyHandler() as objSSPropertyOperation:
#             static_listProperties_Data_Section_Note = ['Data_Section_Note', 'Data Section Note','Section','Sect','', objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Long]
#             static_SSSimulation_listProperties_1 = ['dict_SimPopulationSize', 'Sim_Population_size','Sim Pop Size','Pop_size','individuals',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]

    class ObjectCustom1ReportingPropertyLabels:
        
        '''
        E.g.         lisPropertyLabels =['Property_Name','Property_Label_Long','Property_Label_Short''Property_Label_Abreviation','Property_Label_Units',Property_Label_Default_Label_Key'}
        '''
        
        with object_SSPropertyHandler() as objSSPropertyOperation:
            static_listProperties_Data_Section_Note = ['Data_Section_Note', 'Data Section Note','Section','Sect','', objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Long]
            static_listProperties_Sub_Pop_VSP = ['Sub_Pop_VSP', 'Sub_Pop_VSP','Sub Pop VSP','VSP','VSP',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Sub_Pop_Size_VSP = ['Sub_Pop_Size_VSP', 'Sub_Pop_Size_VSP','VSP Size','VSP Size','Indivs',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_demographic_ne_loci_1_VSP = ['demographic_ne_loci_1_VSP', 'VSP DemographicNe Locus 1','Demo Ne','NeDemo','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_temporal_JR_P1_ne_VSP = ['temporal_JR_P1_ne_VSP', 'Temporal Ne JR P1','Temporal NE JS P1','NeTempJSP1','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_temporal_JR_P1_ne_2_5_CI_VSP = ['temporal_JR_P1_ne_2.5_CI_VSP', 'Temporal Ne JR P1 Lower 2.5 CI','Temporal NE JS P1 Lwr CI','NeTempJSP1_2.5CI','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_temporal_JR_P1_ne_97_5_CI_VSP = ['temporal_JR_P1_ne_97.5_CI_VSP', 'Temporal Ne JR P1 Upper 97.5 CI','Temporal NE JS P1 Uppr CI','NeTempJSP1_97.5CI','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_temporal_JR_P2_ne_VSP = ['temporal_JR_P2_ne_VSP', 'VSP Temporal Ne JR P2','Temporal NE JS P2','NeTempJSP2','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_temporal_JR_P2_ne_2_5_CI_VSP = ['temporal_JR_P2_ne_2.5_CI_VSP', 'VSP Temporal Ne JR P2 Lower 2.5 CI','Temporal NE JS P2 Lwr CI','NeTempJSP2_2.5CI','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_temporal_JR_P2_ne_97_5_CI_VSP = ['temporal_JR_P2_ne_97.5_CI_VSP', 'VSP Temporal Ne JR P2 Upper 97.5 CI','Temporal NE JS P2 Uppr CI','NeTempJSP2_97.5CI','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_ld_ne_pcrit_0_VSP = ['ld_ne_pcrit_0_VSP', 'VSP LD Ne PCrit 0','LD Ne PCrit 0','NeLD_Pc_0','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_ld_ne_pcrit_0_lwr_ci_VSP = ['ld_ne_pcrit_0_lwr_ci_VSP', 'VSP LD Ne PCrit 0 Lower CI','LD Ne PCrit 0 Lwr CI','NeLD_Pc_0_lwr_ci','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_ld_ne_pcrit_0_upr_ci_VSP = ['ld_ne_pcrit_0_upr_ci_VSP', 'VSP LD Ne PCrit 0 Upper CI','LD Ne PCrit 0 Upr CI','NeLD_Pc_0_upr_ci','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_ld_ne_pcrit_0_05_VSP = ['ld_ne_pcrit_0.05_VSP', 'VSP LD Ne PCrit 0.05','LD Ne PCrit 0.05','NeLD_Pc_0.05','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_ld_ne_pcrit_0_05_lwr_ci_VSP = ['ld_ne_pcrit_0.05_lwr_ci_VSP', 'VSP LD Ne PCrit 0.05 Lower CI','LD Ne PCrit 0.05 Lwr CI','NeLD_Pc_0.05_lwr_ci','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_ld_ne_pcrit_0_05_upr_ci_VSP = ['ld_ne_pcrit_0.05_upr_ci_VSP', 'VSP LD Ne PCrit 0.05 Upper CI','LD Ne PCrit 0.05 Upr CI','NeLD_Pc_0.05_upr_ci','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_ld_ne_pcrit_0_02_VSP = ['ld_ne_pcrit_0.02_VSP', 'VSP LD Ne PCrit 0.02','LD Ne PCrit 0.02','NeLD_Pc_0.02','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_ld_ne_pcrit_0_02_lwr_ci_VSP = ['ld_ne_pcrit_0.02_lwr_ci_VSP', 'VSP LD Ne PCrit 0.02 Lower CI','LD Ne PCrit 0.02 Lwr CI','NeLD_Pc_0.02_lwr_ci','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_ld_ne_pcrit_0_02_upr_ci_VSP = ['ld_ne_pcrit_0.02_upr_ci_VSP', 'VSP LD Ne PCrit 0.02 Upper CI','LD Ne PCrit 0.02 Upr CI','NeLD_Pc_0.02_upr_ci','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_ld_ne_pcrit_0_01_VSP = ['ld_ne_pcrit_0.01_VSP', 'VSP LD Ne PCrit 0.01','LD Ne PCrit 0.01','NeLD_Pc_0.01','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_ld_ne_pcrit_0_01_lwr_ci_VSP = ['ld_ne_pcrit_0.01_lwr_ci_VSP', 'VSP LD Ne PCrit 0.01 Lower CI','LD Ne PCrit 0.01 Lwr CI','NeLD_Pc_0.01_lwr_ci','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_ld_ne_pcrit_0_01_upr_ci_VSP = ['ld_ne_pcrit_0.01_upr_ci_VSP', 'VSP LD Ne PCrit 0.01 Upper CI','LD Ne PCrit 0.01 Upr CI','NeLD_Pc_0.01_upr_ci','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
                              
            #With Prefix                          
            static_listProperties_Loci_Allele_Totals_Per_Locus_List_VSP = ['Loci_Allele_Totals_Per_Locus_List_VSP', 'VSP ' +  ' Allele Totals Per Locus List','Total Alleles Per Locus','Tot_Allele_Per_Locus','Alleles',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Loci_Allele_Instance_Count_List_VSP = ['Loci_Allele_Instance_Count_List_VSP', 'VSP ' +  ' Locus Allele Instance Count List','Allele Instance Count Per Locus','Allele_Instances','Alleles',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Loci_Allele_Frequencies_List_VSP = ['Loci_Allele_Frequencies_List_VSP', 'VSP ' +  ' Locus Allele Frequencies List','Allele Freqs Per Locus','Allele_Freqs','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Num_Sire_Parent = ['Num_Sire_Parent', 'VSP ' +  ' Number of Sires','Num Sires','n_Sires','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Mean_Offspring_Per_Sire_Parent = ['Mean_Offspring_Per_Sire_Parent', 'VSP ' +  ' Mean Offspring Per Sire','Mean Sire Offspring','Mean(Embr)_Sire','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Mean_Variance_Offspring_Per_Sire_Parent = ['Mean_Variance_Offspring_Per_Sire_Parent', 'VSP ' +  ' Variance in Offspring per Sire','Variance Sire Embr','Var(Embr)_Sire','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Num_Male_Potential_Parent = ['Num_Male_Potential_Parent', 'VSP ' +  ' Number of Male Potential Parents','Num Male Potential Parents','n_P_Parent_Male','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Mean_Offspring_Per_Male_Potential_Parent = [' Mean_Offspring_Per_Male_Potential_Parent', 'VSP ', 'Mean Offspring Per Male Potential Parent','Mean(Embr)_Male','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Variance_Offspring_Per_Male_Potential_Parent = ['Variance_Offspring_Per_Male_Potential_Parent', 'VSP ' +  ' Variance Offspring Per Male Potential Parent','Var Offspring Per Male Potential Parent','Var(Embr)_Male','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents = ['Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents', 'VSP ' +  ' Ne Demographic From Known Offspring Given Male Potential Parents','Offspring Ne Demographic Given Male Potential Parents','NeDemo_Male','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
    
            static_listProperties_Loci_Allele_Totals_Per_Locus_List_VSP = ['Loci_Allele_Totals_Per_Locus_List_VSP', 'VSP ' +  ' Allele Totals Per Locus List','Total Alleles Per Locus','Tot_Allele_Per_Locus','Alleles',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Loci_Allele_Instance_Count_List_VSP = ['Loci_Allele_Instance_Count_List_VSP', 'VSP ' +  ' Locus Allele Instance Count List','Allele Instance Count Per Locus','Allele_Instances','Alleles',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Loci_Allele_Frequencies_List_VSP = ['Loci_Allele_Frequencies_List_VSP', 'VSP ' +  ' Locus Allele Frequencies List','Allele Freqs Per Locus','Allele_Freqs','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Num_Dame_Parent = ['Num_Dame_Parent', 'VSP ' +  ' Number of Dames','Num Dames','n_Dames','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Mean_Offspring_Per_Dame_Parent = ['Mean_Offspring_Per_Dame_Parent', 'VSP ' +  ' Mean Offspring Per Dame','Mean Dame Offspring','Mean(Embr)_Dame','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Mean_Variance_Offspring_Per_Dame_Parent = ['Mean_Variance_Offspring_Per_Dame_Parent', 'VSP ' +  ' Variance in Offspring per Dame','Variance Dame Offspring','Var(Embr)_Dame','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Num_Female_Potential_Parent = ['Num_Female_Potential_Parent', 'VSP ' +  ' Number of Female Potential Parents','Num Female Potential Parents','n_P_Parent_Fema','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Mean_Offspring_Per_Female_Potential_Parent = [' Mean_Offspring_Per_Female_Potential_Parent', 'VSP ', 'Mean Offspring Per Female Potential Parent','Mean(Embr)_Fema','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Variance_Offspring_Per_Female_Potential_Parent = ['Variance_Offspring_Per_Female_Potential_Parent', 'VSP ' +  ' Variance Offspring Per Female Potential Parent','Var Offspring Per Female Potential Parent','Var(Embr)_Fema','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents = ['Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents', 'VSP ' +  ' Ne Demographic From Known Offspring Given Female Potential Parents','Offspring Ne Demographic Given Female Potential Parents','NeDemo_Fema','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            
            static_listProperties_Num_Actual_Parent = ['Num_Actual_Parent', 'VSP ' +  ' Number of Actuals','Num Actuals','n_Parent','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Mean_Offspring_Per_Actual_Parent = ['Mean_Offspring_Per_Actual_Parent', 'VSP ' +  ' Mean Offspring Per Actual','Mean Actual Offspring','Mean(Embr)','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Mean_Variance_Offspring_Per_Actual_Parent = ['Mean_Variance_Offspring_Per_Actual_Parent', 'VSP ' +  ' Variance in Offspring per Actual','Variance Actual Offspring','Var(Embr)','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Num_Actual_Potential_Parent = ['Num_Actual_Potential_Parent', 'VSP ' +  ' Number of Actual Potential Parents','Num Actual Potential Parents','n_PPare','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Mean_Offspring_Per_Actual_Potential_Parent = ['Mean_Offspring_Per_Actual_Potential_Parent', 'VSP ' +  ' Mean Offspring Per Actual Potential Parent','Mean Offspring Per Actual Potential Parent','Mean(Embr)_PPare','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Variance_Offspring_Per_Actual_Potential_Parent = ['Variance_Offspring_Per_Actual_Potential_Parent', 'VSP ' +  ' Variance Offspring Per Actual Potential Parent','Var Offspring Per Actual Potential Parent','Var(Embr)_PPare','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Ne_Demographic_From_Known_Offspring_Given_Actual_Potential_Parents = ['Ne_Demographic_From_Known_Offspring_Given_Actual_Potential_Parents', 'VSP ' +  ' Ne Demographic From Known Offspring Given Actual Potential Parents','Offspring Ne Demographic Given Actual Potential Parents','NeDemo_PPare','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]
            static_listProperties_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents = ['Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents', 'VSP ' +  ' Ne Demographic From Known Offspring Given Both Sexes Potential Parents Ne Rato Nc Potential Parents','NeDemo/Nc from known Offspring Given Both Sexes Potential Parents','NeDemo/Nc_Both_Sexes','',objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation]

            '''
            AgeNe_CalculatedTotals
            '''
            #For Sim
            static_AgeNe_Sim_CalculatedTotals_Label_Prefix1 = 'Sim_'
            static_AgeNe_Sim_CalculatedTotals_Label_Prefix2 = 'Sim_'
            static_AgeNe_Sim_CalculatedTotals_listProperties_1 = [static_AgeNe_Sim_CalculatedTotals_Label_Prefix1 + 'L_Overall', '','',static_AgeNe_Sim_CalculatedTotals_Label_Prefix2 + 'L_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Sim_CalculatedTotals_listProperties_2 = [static_AgeNe_Sim_CalculatedTotals_Label_Prefix1 + 'N_Adults_Overall', '','',static_AgeNe_Sim_CalculatedTotals_Label_Prefix2 + 'N_Adults_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Sim_CalculatedTotals_listProperties_3 = [static_AgeNe_Sim_CalculatedTotals_Label_Prefix1 + 'N_Overall', '','',static_AgeNe_Sim_CalculatedTotals_Label_Prefix2 + 'N_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Sim_CalculatedTotals_listProperties_4 = [static_AgeNe_Sim_CalculatedTotals_Label_Prefix1 + 'NbDemo', '','',static_AgeNe_Sim_CalculatedTotals_Label_Prefix2 + 'NbDemo','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Sim_CalculatedTotals_listProperties_5 = [static_AgeNe_Sim_CalculatedTotals_Label_Prefix1 + 'Nb_Vx_All_Sexes_Overall', '','',static_AgeNe_Sim_CalculatedTotals_Label_Prefix2 + 'Nb_Vx_All_Sexes_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Sim_CalculatedTotals_listProperties_6 = [static_AgeNe_Sim_CalculatedTotals_Label_Prefix1 + 'NeDemo', '','',static_AgeNe_Sim_CalculatedTotals_Label_Prefix2 + 'NeDemo','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            #static_AgeNe_Sim_CalculatedTotals_listProperties_7 = [static_AgeNe_Sim_CalculatedTotals_Label_Prefix1 + 'NeDemoDivNAdultsOverall', '','',static_AgeNe_Sim_CalculatedTotals_Label_Prefix2 + 'NeDemoDivNAdultsOverall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Sim_CalculatedTotals_listProperties_7 = [static_AgeNe_Sim_CalculatedTotals_Label_Prefix1 + 'NeDemoDivNcAdultsOverall', '','',static_AgeNe_Sim_CalculatedTotals_Label_Prefix2 + 'NeDemoDivNcAdultsOverall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Sim_CalculatedTotals_listProperties_8 = [static_AgeNe_Sim_CalculatedTotals_Label_Prefix1 + 'NeDemoDivNOverall', '','',static_AgeNe_Sim_CalculatedTotals_Label_Prefix2 + 'NeDemoDivNOverall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Sim_CalculatedTotals_listProperties_9 = [static_AgeNe_Sim_CalculatedTotals_Label_Prefix1 + 'Vk_Overall', '','',static_AgeNe_Sim_CalculatedTotals_Label_Prefix2 + 'Vk_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Sim_CalculatedTotals_listProperties_10 = [static_AgeNe_Sim_CalculatedTotals_Label_Prefix1 + 'kbar_Overall', '','',static_AgeNe_Sim_CalculatedTotals_Label_Prefix2 + 'kbar_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            #For Manual
            static_AgeNe_Manual_CalculatedTotals_Label_Prefix1 = 'Manual_'
            static_AgeNe_Manual_CalculatedTotals_Label_Prefix2 = 'Man_'
            static_AgeNe_Manual_CalculatedTotals_listProperties_1 = [static_AgeNe_Manual_CalculatedTotals_Label_Prefix1 + 'L_Overall', '','',static_AgeNe_Manual_CalculatedTotals_Label_Prefix2 + 'L_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Manual_CalculatedTotals_listProperties_2 = [static_AgeNe_Manual_CalculatedTotals_Label_Prefix1 + 'N_Adults_Overall', '','',static_AgeNe_Manual_CalculatedTotals_Label_Prefix2 + 'N_Adults_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Manual_CalculatedTotals_listProperties_3 = [static_AgeNe_Manual_CalculatedTotals_Label_Prefix1 + 'N_Overall', '','',static_AgeNe_Manual_CalculatedTotals_Label_Prefix2 + 'N_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Manual_CalculatedTotals_listProperties_4 = [static_AgeNe_Manual_CalculatedTotals_Label_Prefix1 + 'NbDemo', '','',static_AgeNe_Manual_CalculatedTotals_Label_Prefix2 + 'NbDemo','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Manual_CalculatedTotals_listProperties_5 = [static_AgeNe_Manual_CalculatedTotals_Label_Prefix1 + 'Nb_Vx_All_Sexes_Overall', '','',static_AgeNe_Manual_CalculatedTotals_Label_Prefix2 + 'Nb_Vx_All_Sexes_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Manual_CalculatedTotals_listProperties_6 = [static_AgeNe_Manual_CalculatedTotals_Label_Prefix1 + 'NeDemo', '','',static_AgeNe_Manual_CalculatedTotals_Label_Prefix2 + 'NeDemo','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            #static_AgeNe_Manual_CalculatedTotals_listProperties_7 = [static_AgeNe_Manual_CalculatedTotals_Label_Prefix1 + 'NeDemoDivNAdultsOverall', '','',static_AgeNe_Manual_CalculatedTotals_Label_Prefix2 + 'NeDemoDivNAdultsOverall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Manual_CalculatedTotals_listProperties_7 = [static_AgeNe_Manual_CalculatedTotals_Label_Prefix1 + 'NeDemoDivNcAdultsOverall', '','',static_AgeNe_Manual_CalculatedTotals_Label_Prefix2 + 'NeDemoDivNcAdultsOverall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Manual_CalculatedTotals_listProperties_8 = [static_AgeNe_Manual_CalculatedTotals_Label_Prefix1 + 'NeDemoDivNOverall', '','',static_AgeNe_Manual_CalculatedTotals_Label_Prefix2 + 'NeDemoDivNOverall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Manual_CalculatedTotals_listProperties_9 = [static_AgeNe_Manual_CalculatedTotals_Label_Prefix1 + 'Vk_Overall', '','',static_AgeNe_Manual_CalculatedTotals_Label_Prefix2 + 'Vk_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
            static_AgeNe_Manual_CalculatedTotals_listProperties_10 = [static_AgeNe_Manual_CalculatedTotals_Label_Prefix1 + 'kbar_Overall', '','',static_AgeNe_Manual_CalculatedTotals_Label_Prefix2 + 'kbar_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
    

    class ObjectReportingPropertyLabels:
        
        '''
        E.g.         lisPropertyLabels =['Property_Name','Property_Label_Long','Property_Label_Short''Property_Label_Abreviation','Property_Label_Units',Property_Label_Default_Label_Key', Optional_Single_Value_Dict_Key}
        
        Optional: If a 6th Property Label value is present then the property is a dict with only one value where the 6th label is the dict key
        '''

        '''
        AgeNeLifeTables
        '''        
        static_Property_Label_Short_Prefix_LT = 'LT__'
        static_AgeNeLifeTable_listProperties_1 = ['N1_Odict', '','',static_Property_Label_Short_Prefix_LT + 'N1','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTable_listProperties_2 = ['odictSexAgeInMonths', '','',static_Property_Label_Short_Prefix_LT + 'Age','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTable_listProperties_3 = ['odictSexAgeInYears', '','',static_Property_Label_Short_Prefix_LT + 'Age','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTable_listProperties_4 = ['sx_Odict', '','',static_Property_Label_Short_Prefix_LT + 'sx','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTable_listProperties_5 = ['bx_Odict', '','',static_Property_Label_Short_Prefix_LT + 'bx.','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTable_listProperties_6 = ['lx_Odict', '','',static_Property_Label_Short_Prefix_LT + 'lx','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTable_listProperties_7 = ['bxlx_Odict', '','',static_Property_Label_Short_Prefix_LT + 'bxlx','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTable_listProperties_8 = ['b_x_Odict', '','',static_Property_Label_Short_Prefix_LT + 'b_x','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTable_listProperties_9 = ['bxNx_Odict', '','',static_Property_Label_Short_Prefix_LT + 'bxNx','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTable_listProperties_10 = ['Nx_Odict', '','',static_Property_Label_Short_Prefix_LT + 'Nx','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTable_listProperties_11 = ['Bx_Odict', '','',static_Property_Label_Short_Prefix_LT + 'Bx','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTable_listProperties_12 = ['xBx_Div_N1_Odict', '','',static_Property_Label_Short_Prefix_LT + 'xBx/N1','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTable_listProperties_13 = ['Calculated_Totals', '','',static_Property_Label_Short_Prefix_LT + 'L-Totals','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        '''
        AgeNeLifeTables_CalculatedTotals
        '''
        static_Property_Label_Short_Prefix_LTT = 'LTT__'
        static_AgeNeLifeTables_CalculatedTotals_listProperties_1 = ['L_All', '','',static_Property_Label_Short_Prefix_LTT + 'L_All','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTables_CalculatedTotals_listProperties_2 = ['Nx_N_Adults', '','',static_Property_Label_Short_Prefix_LTT + 'Nx_N_Adults','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTables_CalculatedTotals_listProperties_3 = ['Nx_Nc_Adults', '','',static_Property_Label_Short_Prefix_LTT + 'Nx_Nc_Adults','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTables_CalculatedTotals_listProperties_4 = ['Nx_All', '','',static_Property_Label_Short_Prefix_LTT + 'Nx_All','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeLifeTables_CalculatedTotals_listProperties_5 = ['bxNx_Sum_All', '','',static_Property_Label_Short_Prefix_LTT + 'bxNx_Sum_All','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        
        '''
        AgeNeDemographicTable
        '''
        static_Property_Label_Short_Prefix_DT = 'DT__' 
        static_AgeNeDemographicTable_listProperties_1 = ['kbarx_Odict', '','',static_Property_Label_Short_Prefix_DT + 'kbarx','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTable_listProperties_2 = ['Vx_Odict', '','',static_Property_Label_Short_Prefix_DT + 'Vx','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTable_listProperties_3 = ['Dx_Odict', '','',static_Property_Label_Short_Prefix_DT + 'Dx','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTable_listProperties_4 = ['kbarDx_Odict', '','',static_Property_Label_Short_Prefix_DT + 'kbarDx','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTable_listProperties_5 = ['kbarAll_Odict', '','',static_Property_Label_Short_Prefix_DT + 'kbarAll','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTable_listProperties_6 = ['delta_kbar_Odict', '','',static_Property_Label_Short_Prefix_DT + 'delta_kbar','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTable_listProperties_7 = ['SSDIx_Odict', '','',static_Property_Label_Short_Prefix_DT + 'SSDIx','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTable_listProperties_8 = ['SSDGx_Odict', '','',static_Property_Label_Short_Prefix_DT + 'SSDGx','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTable_listProperties_9 = ['SSDx_Odict', '','',static_Property_Label_Short_Prefix_DT + 'SSDx','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTable_listProperties_10 = ['Yx_Odict', '','',static_Property_Label_Short_Prefix_DT + 'Yx','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTable_listProperties_11= ['Nb_Vx_All_Odict', '','',static_Property_Label_Short_Prefix_DT + 'Nb_Vx_All','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTable_listProperties_12= ['Nb_Vx_All_Sexes_Odict', '','',static_Property_Label_Short_Prefix_DT + 'Nb_Vx_All_Sexes','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTable_listProperties_13 = ['Calculated_Totals', '','',static_Property_Label_Short_Prefix_DT + 'D-Totals','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        '''
        AgeNeDemographicTables_CalculatedTotals
        '''
        static_Property_Label_Short_Prefix_DTT = 'DTT__'
        static_AgeNeDemographicTables_CalculatedTotals_listProperties_1 = ['SSD_T', '','',static_Property_Label_Short_Prefix_DTT + 'SSD_T','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTables_CalculatedTotals_listProperties_2 = ['Vk_All', '','',static_Property_Label_Short_Prefix_DTT + 'Vk_All','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTables_CalculatedTotals_listProperties_3 = ['kbar_All', '','',static_Property_Label_Short_Prefix_DTT + 'kbar_All','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTables_CalculatedTotals_listProperties_4 = ['kbarx_Dx_All', '','',static_Property_Label_Short_Prefix_DTT + 'kbarx_Dx_All','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        '''
        AgeNeDemographicTables_CalculatedTotals_AllSexes
        '''
        static_Property_Label_Short_Prefix_DTFT = 'FTT__' 
        static_AgeNeDemographicTables_CalculatedTotals_AllSexes_listProperties_1 = ['Nb_Vx_All_Sexes', '','',static_Property_Label_Short_Prefix_DTFT + 'Nb_Vx_All_sexes','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNeDemographicTables_CalculatedTotals_AllSexes_listProperties_2 = ['Nb_kbar_All_Sexes', '','',static_Property_Label_Short_Prefix_DTFT + 'Nb_kbar_All_sexes','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        '''
        AgeNe
        '''        
        
        static_AgeNe_listProperties_1 = ['N1_Newborns_Per_Age', '','','N1','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNe_listProperties_2 = ['List_Sexes', '','','Sexes','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNe_listProperties_3 = ['Initial_Male_Sex_Ratio', '','','Sex_Ratio','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNe_listProperties_4 = ['Calculated_Totals', '','','AN-Totals','',object_SSReportingProperty.static_stringProperty_Label_Abreviation]

        '''
        AgeNe_CalculatedTotals
        '''
        static_Property_Label_Short_Prefix_FTT = 'FTT__' 
        static_AgeNe_CalculatedTotals_listProperties_1 = ['L_Overall', '','',static_Property_Label_Short_Prefix_FTT + 'L_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNe_CalculatedTotals_listProperties_2 = ['N_Adults_Overall', '','',static_Property_Label_Short_Prefix_FTT + 'N_Adults_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNe_CalculatedTotals_listProperties_3 = ['Nc_Adults_Overall', '','',static_Property_Label_Short_Prefix_FTT + 'Nc_Adults_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNe_CalculatedTotals_listProperties_4 = ['N_Overall', '','',static_Property_Label_Short_Prefix_FTT + 'N_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNe_CalculatedTotals_listProperties_5 = ['NbDemo', '','',static_Property_Label_Short_Prefix_FTT + 'NbDemo','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNe_CalculatedTotals_listProperties_6 = ['Nb_Vx_All_Sexes_Overall', '','',static_Property_Label_Short_Prefix_FTT + 'Nb_Vx_all_sexes_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNe_CalculatedTotals_listProperties_7 = ['NeDemo', '','',static_Property_Label_Short_Prefix_FTT + 'NeDemo.','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        #static_AgeNe_CalculatedTotals_listProperties_8 = ['NeDemoDivNAdultsOverall', '','',static_Property_Label_Short_Prefix_FTT + 'NeDemoDivNAdultsOverall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNe_CalculatedTotals_listProperties_8 = ['NeDemoDivNcAdultsOverall', '','',static_Property_Label_Short_Prefix_FTT + 'NeDemoDivNcAdultsOverall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNe_CalculatedTotals_listProperties_9 = ['NeDemoDivNOverall', '','',static_Property_Label_Short_Prefix_FTT + 'NeDemoDivNOverall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNe_CalculatedTotals_listProperties_10 = ['Vk_Overall', '','',static_Property_Label_Short_Prefix_FTT + 'Vk_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNe_CalculatedTotals_listProperties_11 = ['kbar_Overall', '','',static_Property_Label_Short_Prefix_FTT + 'kbar_Overall','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]
        static_AgeNe_CalculatedTotals_listProperties_12 = ['Male_N1_Ratio', '','',static_Property_Label_Short_Prefix_FTT + 'Male_N1_Ratio','', object_SSReportingProperty.static_stringProperty_Label_Abreviation]

        '''
        SSSSimulation
        '''
        static_SSSimulation_listProperties_1 = ['dictDataSectionNotesLevels', 'Data Section Note','Section','Sect','', object_SSReportingProperty.static_stringProperty_Label_Long, 'Data_Section_Note_1', ]
        static_SSSimulation_listProperties_2 = ['dictFilenameEmbeddedFields', 'Filename_Embedded_Fields','Filename Embedded Fields','Run_Specs','',object_SSReportingProperty.static_stringProperty_Label_Abreviation, 'Filename_Embedded_Fields']
        static_SSSimulation_listProperties_3 = ['dict_SimPopulationSize', 'Sim_Population_size','Sim Pop Size','Pop_size','individuals',object_SSReportingProperty.static_stringProperty_Label_Abreviation, 'Sim_Population_size']
        static_SSSimulation_listProperties_4 = ['dict_SimCurrentBatch', 'Sim_Current_Batch','Current Batch','Batch','batchs',object_SSReportingProperty.static_stringProperty_Label_Abreviation, 'Sim_Current_Batch']
        static_SSSimulation_listProperties_5 = ['dict_SimCurrentReplicate', 'Sim_Current_Replicate','Current Replicate','Replicate','replicates',object_SSReportingProperty.static_stringProperty_Label_Abreviation, 'Sim_Current_Replicate']
        static_SSSimulation_listProperties_6 = ['dict_InitialLociAlleleFreqList', 'Loci_initial_allele_frequencies_list','Loci initial allele frequencies list','Initial_Allele_Freqs','',object_SSReportingProperty.static_stringProperty_Label_Abreviation, 'Loci_initial_allele_frequencies_list']
        static_SSSimulation_listProperties_7 = ['dict_dictSimImportedLocusNames', 'Sim_Imported_Locus_Names','Imported locus locus names','Locus_Names','',object_SSReportingProperty.static_stringProperty_Label_Abreviation, 'Sim_Imported_Locus_Names']
        static_SSSimulation_listProperties_8 = ['dict_dictSimImportedLocusAlleleNames', 'Sim_Imported_Locus_Allele_Names','Imported locus allele names','Allele_Names','',object_SSReportingProperty.static_stringProperty_Label_Abreviation, 'Sim_Imported_Locus_Allele_Names']
        static_SSSimulation_listProperties_9 = ['dict_CurrentIteration', 'Current_Month','Sim Current Month','Sim_Month','',object_SSReportingProperty.static_stringProperty_Label_Abreviation, 'Current_Month']
        '''
        SSSPopulation
        '''
        static_SSPopulation_listProperties_1 = ['dictDataSectionNotesLevels', 'Data Section Note','Section','Sect','', object_SSReportingProperty.static_stringProperty_Label_Long, 'Data_Section_Note_2', ]
        static_SSPopulation_listProperties_2 = ['dict_dictAlleleFreqs', 'Loci_Allele_Frequencies_List','Loci Allele Frequencies List','Allele_Freqs','',object_SSReportingProperty.static_stringProperty_Label_Abreviation, 'Loci_Allele_Frequencies_List']
        static_SSPopulation_listProperties_3 = ['dict_dictAlleleFreqsAtPopulationInitialization', 'Loci_Allele_Frequencies_List_At_Pop_Init','Loci Allele Frequencies List At Pop Init','Allele_Freqs_Initial','',object_SSReportingProperty.static_stringProperty_Label_Abreviation, 'Loci_Allele_Frequencies_List_At_Pop_Init']
   
    class ILFOutputSuppressionFlags:
        
        static_stringNotSuppressed = 'NSUP'
        static_stringSuppressed = 'SUP'
        static_stringNotSpecified = 'NSP'
        static_stringSuppressedAndNotOutput = 'SUPNOUT'

    class SexConstants(object):
        
        static_stringSexAll = 'All'
        static_stringSexMale = 'Male'
        static_stringSexFemale = 'Female'
        
        static_simupop_Sex_MALE = sim.MALE
        static_simupop_Sex_FEMALE = sim.FEMALE

        def method_Get_Simupop_Sex_Constant(self, strSex):
            
            static_simupop_Sex = -1
            
            if strSex == globalsSS.SexConstants.static_stringSexMale:
                static_simupop_Sex = globalsSS.SexConstants.static_simupop_Sex_MALE
            elif strSex == globalsSS.SexConstants.static_stringSexFemale: 
                static_simupop_Sex = globalsSS.SexConstants.static_simupop_Sex_FEMALE
                
            return static_simupop_Sex
    
    class StatisticsConstants(object):
        
        static_stringSampleSizeLabel = 'n'
        static_stringMeanLabel = 'Mean'
        static_stringVarianceLabel = 'Variance'
 
    class DateTimeVariables(object):
        
        dateTimeSinceLastGeneralMessage = timedelta
        
        def method_Get_DateTime_General_Message(self):
            
            dateTimeLastGeneralMessage = globals_SharkSim.global_dateTimeLastGeneralMessage
            
            globals_SharkSim.global_dateTimeLastGeneralMessage = datetime.now()
            
            return dateTimeLastGeneralMessage
        
        def method_Get_Time_Since_Last_General_Message(self):
            
            dateTimeLastGeneralMessage = self.method_Get_DateTime_General_Message()
            
            dateTimeNow = datetime.now()
            
            dateTimeSinceLastGeneralMessage = dateTimeNow - dateTimeLastGeneralMessage
            
            return dateTimeSinceLastGeneralMessage
    
    class LDNe_PCrit__Float(object):
        
        #individual PCrits
        static_float_LDNe_PCrit_0_05 = 0.05
        static_float_LDNe_PCrit_0_02 = 0.02
        static_float_LDNe_PCrit_0_01 = 0.01
        static_float_LDNe_PCrit_0_00 = 0
        static_float_LDNe_PCrit_NoS = 1
        
    class Ne2Bulk_Processing(object):
        
        #individual PCrits
        static_stringNe2Bulk_PCrit_To_Process_PCrit_0_05 = 'PCRIT_0_05'
        static_stringNe2Bulk_PCrit_To_Process_PCrit_0_02 = 'PCRIT_0_02'
        static_stringNe2Bulk_PCrit_To_Process_PCrit_0_01 = 'PCRIT_0_01'
        static_stringNe2Bulk_PCrit_To_Process_PCrit_0_00 = 'PCRIT_0_00'
        static_stringNe2Bulk_PCrit_To_Process_PCrit_NoS = 'PCRIT_NOS'
        
        #Combinations
        static_stringNe2Bulk_PCrit_To_Process_PCrit_0_02_PCrit_0_00 = 'PCRIT_0_02_PCRIT_0_00'
        static_stringNe2Bulk_PCrit_To_Process_PCrit_0_05_PCrit_0_02 = 'PCRIT_0_05_PCRIT_0_02'
        static_stringNe2Bulk_PCrit_To_Process_PCrit_0_05_PCrit_0_00 = 'PCRIT_0_05_PCRIT_0_00'
        static_stringNe2Bulk_PCrit_To_Process_PCrit_0_05_PCrit_0_02_PCrit_0_00 = 'PCRIT_0_05_PCRIT_0_02_PCRIT_0_00'
        static_stringNe2Bulk_PCrit_To_Process_PCrit_0_05_PCrit_0_02_PCrit_0_01_PCrit_0_00 = 'PCRIT_0_05_PCRIT_0_02_PCRIT_0_01_PCRIT_0_00'
        static_stringNe2Bulk_PCrit_To_Process_PCrit_0_10_PCrit_0_05_PCrit_0_02_PCrit_0_01_PCrit_0_00 = 'PCRIT_0_10_PCRIT_0_05_PCRIT_0_02_PCRIT_0_01_PCRIT_0_00'
        
    class Sampling_SamplingMethod(object):
        
        #Cohort Dependent Sample
        static_SamplingMethod_VSPSplit_AgeInMonths = 50
        static_SamplingMethod_SampleSizeIsCohortAbsoluteRate = 1
        static_SamplingMethod_SampleSizeIsCohortAbsoluteNumber = 2
        static_SamplingMethod_SampleSizeIsCohortRateDist_CAPL_FISHED_cohort_proportions = 3
        static_SamplingMethod_SampleSizeIsCohortRateDist_CAPL_random_sampling_MATURE_cohort_proportions  = 4
        static_SamplingMethod_SampleSizeIsCohortRateDist_CAPL_random_sampling_ALL_cohort_proportions = 5
        static_SamplingMethod_SampleSizeIsCohortRateDist_CAPL_random_sampling_ALL_cohort_proportions_X_NEONATE = 6
        static_SamplingMethod_SampleSizeIsCohortRateDist_CAPL_random_sampling_NEONATE = 7
        static_SamplingMethod_SampleSizeIsProportionPerVSPCohort = 8
        static_SamplingMethod_SampleSizeIsProportionScaledByMaxAbsPerVSPCohort = 9
        static_SamplingMethod_SampleSizeIsAbsScaledByMaxAbsPerVSPCohort = 10
        static_SamplingMethod_SampleSizeIsProportionPerVSPCohortOfTotalSamples = 11
        static_SamplingMethod_SampleSizeIs_A_Cohort_Size_Dependent_ProportionPerVSPCohortOfTotalSamples = 12
        static_SamplingMethod_SampleSizeIs_100_Percent_Of_User_Specified_Age_Cohorts = 13
        static_SamplingMethod_SampleSizeIsProportionScaledByTotalSampleSize = 15
        static_SamplingMethod_SampleSizeIsProportionScaledByMaxPropPerVSPCohort = 16
        
        #Non-Cohort Dependent Sample
        static_SamplingMethod_VSPSplit_AgeClass = 51
        static_SamplingMethod_SampleSizeIsNonCohortRandom = 20
        static_SamplingMethod_SampleSizeIsNonCohortRandomAbsolute = 21
        
        pass

    class Sampling_SamplingParameters(object):
        
        static_VSPSplitMethod = 'VSP_Split_Method'
        
        static_AbsoluteNumberOfIndividuals = 'Absolute_Number_Of_Individuals'
        static_PercentageOfTotalPopulation = 'Percentage_Of_Total_Population'
        static_SampleSizeIsProportionPerVSPCohort = 'Sample_Size_Is_Proportion_Per_VSP_Cohort'
        #static_SampleSizeIsProportionPerVSPCohortOfTotalSamples = 'Sample_Size_Is_Proportion_Per_VSP_Cohort_Of_Total_Samples'
        static_SampleSizeIsAbsoluteNumberPerVSPCohort = 'Sample_Size_Is_Absolute_Number_Per_VSP_Cohort'
        static_SampleSizeIsProportionScaledByMaxAbsPerVSPCohort = 'Sample_Size_Is_Proportion_Scaled_By_Max_Absolute_Number_Per_VSP_Cohort'
        static_SampleSizeIsProportionScaledByMaxAbsPerVSPCohort = 'Sample_Size_Is_Proportion_Scaled_By_Max_Absolute_Number_Per_VSP_Cohort'
        static_SampleSizeIsProportionScaledByMaxAbsPerVSPCohort_MaxProportion = 'Sample_Size_Is_Proportion_Scaled_By_Max_Absolute_Number_Per_VSP_Cohort_Max_Proportion'
        static_SampleSizeIsAbsScaledByMaxAbsPerVSPCohort = 'Sample_Size_Is_Abs_Num_Scaled_By_Max_Absolute_Number_Per_VSP_Cohort'
        static_SampleSizeIsAbsScaledByMaxAbsPerVSPCohort_MaxProportion = 'Sample_Size_Is_Abs_Num_Scaled_By_Max_Absolute_Number_Per_VSP_Cohort_Max_Proportion'
        static_SampleSizeIsProportionScaledByTotalSampleSize = 'Sample_Size_Is_Proportion_Scaled_By_Total_Sample_Size'
        
        static_TotalSampleSize = 'Total_Sample_Size'
        
        static_tup_VSP_To_Sample = 'tup_VSP_To_Sample'
        pass

    class Sampling_Locus_ExclusionLDNe_Deltas_Method(object):
        
        static_Sampling_LocusExclusionLDNeDeltas_Method_MinimumDelta = 1
        static_Sampling_LocusExclusionLDNeDeltas_Method_MaximumDelta = 2
        
        pass

    class LDNe_Estimate(object):
    
        static_LDNe_Estimate_Point = 0    
        static_LDNe_Estimate_Lwr_JackKnife_CI = 1    
        static_LDNe_Estimate_Upr_JackKnife_CI = 2
        
        pass
    
    class Genepop_Stats(object):
        
        '''General'''
        static_Label_Gen_UniqueID = 'Unique_Run_ID'
        static_Label_Gen_File = 'GP_Data_File'
        static_Label_Gen_Logger = 'Logger'
        static_Label_Gen_Headings = 'Headings'
        static_Label_Gen_Results = 'Results'
        static_Label_Gen_Locus = 'Locus'
        static_Label_Gen_Sig = 'Sig'
        static_Label_Gen_Pop = 'Pop'
        static_Interpret_Gen_Sig_P_Value_0_05 = 0.05
        static_Interpret_Gen_Sig_P_Value_0_01 = 0.01
        static_Interpret_Gen_Sig_P_Value_0_001 = 0.001
        static_Interpret_Gen_Sig_P_Value_0_0001 = 0.0001
        static_Interpret_Gen_Sig_P_Value_0_00001 = 0.00001
                
        '''HWE'''
        static_Label_HWE_Test = 'Test'
        static_Label_HWE_P = 'P-value'
        static_Label_HWE_SE = 'S.E.'
        static_Label_HWE_RH = 'R&H'
        static_Label_HWE_WC = 'W&C'
        static_Label_HWE_Steps = 'Steps'

        '''HWE Interpretation'''
        #static_Interpret_HWE_Sig_P_Value_0_05 = 0.05
        #static_Interpret_HWE_Sig_P_Value_0_01 = 0.01
    
        '''LD'''
        static_Label_LD_Test = 'Test'
        static_Label_LD_Pair = 'Pair'
        static_Label_LD_Locus_Pair_1 = 'Locus 1'
        static_Label_LD_Locus_Pair_2 = 'Locus 2'
        static_Label_LD_P = 'P-value'
        static_Label_LD_SE = 'S.E.'
        static_Label_LD_Switches = 'Switches'
        static_Label_LD_Demoritization = 'Demoritization'
        static_Label_LD_Batches = 'Batches'
        static_Label_LD_Iterations = 'Iterations'
       
        '''Heterozygosity'''
        #static_Label_He_All_Loci_Test = 'Test'
        static_Label_He_All_Loci_HoExp = 'HoExp'
        static_Label_He_All_Loci_HoObs = 'HoObs'
        static_Label_He_All_Loci_HeExp = 'HeExp'
        static_Label_He_All_Loci_HeObs = 'HeObs'
       
        '''Allele Freqs'''
        static_Label_Allele_Freq_Genes = 'Genes'
        static_Label_Allele_Freq_Allele = ' Allele'
        static_Label_Allele_Freq_Freq = ' Freq' 
        
        pass
    
    class Logger_Details(object):
        
        static_Logger_Field_Heading_When_delim_RESULTS_START = '0 Logger_Info'
        
        static_Logger_Name__Genepop_HWE = 'Stats_HWE'
        static_Logger_File_Suffix__Genepop_HWE = '.gp_hwe_ssim'
        
        static_Logger_Name__Genepop_Allele_Freq = 'Stats_AF'
        static_Logger_File_Suffix__Genepop_Allele_Freq = '.gp_af_ssim'
        
        static_Logger_Name__Genepop_LD = 'Stats_LD'
        static_Logger_File_Suffix__Genepop_LD = '.gp_ld_ssim'
        
        static_Logger_Name__Genepop_He_All_Loci = 'Stats_He'
        static_Logger_File_Suffix__Genepop_He_All_Loci = '.gp_heal_ssim'
        
    class SS_Level_Details(object):
        
        static_Output_File_Suffix__Level_SIM = '.r_slf_ssim'
        static_Output_File_Suffix__Level_BATCH = '.r_blf_ssim'
        
        static_Output_File_Suffix__Level_REPLICATE_EOR = '.r_rlf_eor_ssim'
        static_Reporting_Interval__Level_REPLICATE_End_Of_Replicate = 'EOR'
        static_Output_File_Suffix__Level_REPLICATE_PF = '.r_rlf_pf_ssim'
        static_Reporting_Interval__Level_REPLICATE_Post_Fertilization = 'PF'
        
        static_Output_File_Suffix__Level_Age_Class_VSP_EOR = '.r_vlf_ac_eor_ssim'
        static_Reporting_Interval__Level_Age_Class_VSP_End_Of_Replicate = 'EOR'
        static_Output_File_Suffix__Level_Age_Class_VSP_PF = '.r_vlf_ac_pf_ssim'
        static_Reporting_Interval__Level_Age_Class_VSP_Post_Fertilization = 'PF'
        
        static_Output_File_Suffix__Level_Life_Stage_VSP_EOR = '.r_vlf_ls_eor_ssim'
        static_Reporting_Interval__Level_Life_Stage_VSP_End_Of_Replicate = 'EOR'
        static_Output_File_Suffix__Level_Life_Stage_VSP_PF = '.r_vlf_ls_pf_ssim'
        static_Reporting_Interval__Level_Life_Stage_VSP_Post_Fertilization = 'PF'


    class SS_Replicate_Details(object):
        
        static_Output_File_Suffix__SimuPOP_Pop_EOR = '.r_eor_ssim.pop'
        
    class SS_Per_Fert_PF_File_Output_Details(object):
        
        static_Output_Path_Folder__SimuPOP_Pop_PF = 'SPOP_PF\\'
        static_Output_File_Suffix__SimuPOP_Pop_PF = '.pop_pf_ssim'
        static_Output_File_Prefix__SimuPOP_Pop_PF = '_SPOP_PF'
        
    class Logger_Details_Sampling(object):
        
        static_Logger_Field_Heading_When_delim_RESULTS_START = '0 Logger_Info'
        
        static_Logger_Name__Genepop_Ne2_Samples = 'Ne2_Samps'
        static_Logger_File_Suffix__Genepop_Ne2_Samples = '.gp_Ne2S_ssim'

    class Logger_LEVEL_Details(object):
        
        static_Logger_File_Name__SIM_LEVEL = 'Sim_Log'
        static_Logger_Name__SIM_LEVEL = 'log_SL'
        static_Logger_File_Suffix__SIM_LEVEL = '.log_SL_ssim'
        
        static_Logger_File_Name__BATCH_LEVEL = 'Sim_Batch_Log'
        static_Logger_Name__BATCH_LEVEL = 'log_BL'
        static_Logger_File_Suffix__BATCH_LEVEL = '.log_BL_ssim'
        
        static_Logger_File_Name__REPLICATE_LEVEL = 'Sim_Replicate_Log'
        static_Logger_Name__REPLICATE_LEVEL = 'log_RL'
        static_Logger_File_Suffix__REPLICATE_LEVEL = '.log_RL_ssim'

    class Sim_Status(object):
        
        static_str_Sim_Status__BurnIn = 'BIN' 
        static_str_Sim_Status__InSim = 'SIM'
        
    class Genepop_Results_File_Details(object):
        
        static_Genepop_File_Name__Embryo_VSP_Post_Fertilization = 'GPOP_VSP_Emb_PF_'
        static_Genepop_File_Suffix__Embryo_VSP_Post_Fertilization = '.gp_vsp_Emb_pf_ssim'
        
        static_Genepop_File_Name__Mature_VSP_Post_Fertilization = 'GPOP_VSP_Mat_PF_'
        static_Genepop_File_Suffix__Mature_VSP_Post_Fertilization = '.gp_vsp_Mat_pf_ssim'
        
        static_Genepop_File_Name__Full_SP_Post_Fertilization = 'GPOP_SP_0_Full'
        static_Genepop_File_Suffix__Full_SP_Post_Fertilization = '.gp_sp_0_Full_pf_ssim'
        
        #static_Genepop_File_Name__PF_Pop_SubSample = 'GPOP_SUBS_PF'
        static_Genepop_File_Name__PF_Pop_SubSample = 'GpExp2Pf'
        static_Genepop_File_Suffix__PF_Pop_SubSample = '.a'

        static_Genepop_File_Name__Locus_Jackknifing = 'EESL'
        static_Genepop_File_Suffix__Locus_Jackknifing = '.l'

    class Genepop_Details(object):
         
        static_Output_File_Suffix__Genepop_Pop_Data_EOR_POP = '.gp_eor_pop_ssim'
        static_Output_File_Suffix__Genepop_Pop_Data_EOR_VSP = '.gp_eor_vsp_ssim'
                 
                
    class Logger_Results_File_Details(object):
        
        static_Logger_Field_Heading_When_delim_RESULTS_START = '0 Logger_Info'
        
        static_Logger_Label_Gen_UniqueID = 'Unique_Run_ID'
        
        static_Label_Gen_Source_Unique_Run_Batch_Rep_VSP_ID = 'Unique_Run_Batch_Rep_VSP_ID'
        
        static_Logger_Label_Col_Key_Experiment_Label = 'Experiment_Label'
        static_Label_Log_Col_Key_Batch = 'Sim_Current_Batch'
        static_Label_Log_Col_Key_Replicate = 'Sim_Current_Replicate'

        static_Logger_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results = 'EXP1_CAT_NE2_'        
        static_Logger_Name__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results = 'EXP1_CAT_NE2_eor_Stats'
        static_Logger_File_Suffix__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results = '.dl_EXP1_CAT_NE2_eor_ssim'
 
        static_Logger_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results = 'EXP2_CAT_NE2_'
        static_Logger_Name__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results = 'EXP2_CAT_NE2_pf_Stats'
        static_Logger_File_Suffix__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results = '.dl_EXP2_CAT_NE2_pf_ssim'
        
        static_Logger_Name__Embryo_Parent_Ne_Stats_Post_Fertilization = 'EPNS_PF_Stats'
        static_Logger_File_Suffix__Embryo_Parent_Ne_Stats_Post_Fertilization = '.dl_EPNS_pf_ssim'
 
        static_Logger_Name__Effective_Parents_Stats_Post_Fertilization = 'EPS_PF_Stats'
        static_Logger_File_Suffix__Effective_Parents_Stats_Post_Fertilization = '.dl_EPS_pf_ssim'

        static_Logger_Colname__Prefix__Mortality_PF_Results = 'MORT_'
        static_Logger_Name__Mortality_PF_Results = 'MORT_pf_Stats'
        static_Logger_File_Suffix__Mortality_PF_Results = '.dl_MORT_pf_ssim'

        static_Logger_Colname__Prefix__Sampling_Strategy_Results = 'S_STRAT_'
        static_Logger_Name__Sampling_Strategy_Results = 'S_STRAT_Stats'
        static_Logger_File_Suffix__Sampling_Strategy_Results = '.dl_SAMPLES_ssim'

        static_Logger_Colname__Prefix__Sampling_Exp_2_2_Results = 'EXP_2_2_'
        static_Logger_Name__Sampling_Exp_2_2_Results = 'EXP_2_2_Stats'
        static_Logger_File_Suffix__Sampling_Exp_2_2_Results = static_Logger_File_Suffix__Sampling_Strategy_Results
        
        static_Logger_Colname__Prefix__Sampling_100P_A_COHORTS_Results = '100P_AC_'
        static_Logger_Name__Sampling_100P_A_COHORTS_Results = '100P_AC_Stats'
        static_Logger_File_Suffix__Sampling_100P_A_COHORTS_Results = static_Logger_File_Suffix__Sampling_Strategy_Results
        
        static_Logger_Colname__Prefix__Sampling_FULL_EMBRYO_COHORT_Results = 'FEM_'
        static_Logger_Name__Sampling_FULL_EMBRYO_COHORT_Results = 'FEM_EMBRYOS'
        static_Logger_File_Suffix__Sampling_FULL_EMBRYO_COHORT_Results = static_Logger_File_Suffix__Sampling_Strategy_Results
        
        static_Logger_Colname__Prefix__Sampling_FULL_JUVENILE_COHORTS_Results = 'FJV_'
        static_Logger_Name__Sampling_FULL_JUVENILE_COHORTS_Results = 'FJV_JUVENILES'
        static_Logger_File_Suffix__Sampling_FULL_JUVENILE_COHORTS_Results = static_Logger_File_Suffix__Sampling_Strategy_Results
        
        static_Logger_Colname__Prefix__Sampling_FULL_ADULT_COHORTS_Results = 'FMT_'
        static_Logger_Name__Sampling_FULL_ADULT_COHORTS_Results = 'FMT_ADULTS'
        static_Logger_File_Suffix__Sampling_FULL_ADULT_COHORTS_Results = static_Logger_File_Suffix__Sampling_Strategy_Results
        
        static_Logger_Colname__Prefix__Sampling_FULL_SAMPLING_OF_COHORTS_Results = 'FUL_'
        static_Logger_Name__Sampling_FULL_SAMPLING_OF_COHORTS_Results = 'FUL_COHORTS'
        static_Logger_File_Suffix__Sampling_FULL_SAMPLING_OF_COHORTS_Results = static_Logger_File_Suffix__Sampling_Strategy_Results
        
        static_Logger_Colname__Prefix__Sampling_SAMPLING_PROPORTIONS_SCALED_BY_MAX_PROPORTION_Results = 'PSMP_'
        static_Logger_Name__Sampling_SAMPLING_PROPORTIONS_SCALED_BY_MAX_PROPORTION_Results = 'SCALED_MAX_PROP'
        static_Logger_File_Suffix__Sampling_SAMPLING_PROPORTIONS_SCALED_BY_MAX_PROPORTION_Results = static_Logger_File_Suffix__Sampling_Strategy_Results
        
        '''
        ~~~~~~~~~~~~~~~~~~
        AgeNe EOR Loggers
        ~~~~~~~~~~~~~~~~~~
        ''' 
        static_Logger_Colname__AgeNe_Man_Details_EOR_Results = 'M_AGENE_D_EOR_'
        static_Logger_Name__AgeNe_Man_Details_EOR_Results = 'M_AGENE_D_EOR_Stats'
        static_Logger_File_Suffix__AgeNe_Man_Details_EOR_Results = '.dl_M_AGENE_D_eor_ssim'
 
        static_Logger_Colname__AgeNe_Man_LifeTables_Total_EOR_Results = 'M_AGENE_LT_EOR_'
        static_Logger_Name__AgeNe_Man_LifeTables_Total_EOR_Results = 'M_AGENE_LT_EOR_Stats'
        static_Logger_File_Suffix__AgeNe_Man_LifeTables_Total_EOR_Results = '.dl_M_AGENE_LT_eor_ssim'
 
        static_Logger_Colname__AgeNe_Man_DemographicTables_Total_EOR_Results = 'M_AGENE_DT_EOR_'
        static_Logger_Name__AgeNe_Man_DemographicTables_Total_EOR_Results = 'M_AGENE_DT_EOR_Stats'
        static_Logger_File_Suffix__AgeNe_Man_DemographicTables_Total_EOR_Results = '.dl_M_AGENE_DT_eor_ssim'
 
        static_Logger_Colname__AgeNe_Man_Final_Totals_EOR_Results = 'M_AGENE_FT_EOR_'
        static_Logger_Name__AgeNe_Man_Final_Totals_EOR_Results = 'M_AGENE_FT_EOR_Stats'
        static_Logger_File_Suffix__AgeNe_Man_Final_Totals_EOR_Results = '.dl_M_AGENE_FT_eor_ssim'
 
        static_Logger_Colname__AgeNe_Sim_Details_EOR_Results = 'S_AGENE_D_EOR_'
        static_Logger_Name__AgeNe_Sim_Details_EOR_Results = 'S_AGENE_D_EOR_Stats'
        static_Logger_File_Suffix__AgeNe_Sim_Details_EOR_Results = '.dl_S_AGENE_D_eor_ssim'
 
        static_Logger_Colname__AgeNe_Sim_LifeTables_Total_EOR_Results = 'S_AGENE_LT_EOR_'
        static_Logger_Name__AgeNe_Sim_LifeTables_Total_EOR_Results = 'S_AGENE_LT_EOR_Stats'
        static_Logger_File_Suffix__AgeNe_Sim_LifeTables_Total_EOR_Results = '.dl_S_AGENE_LT_eor_ssim'
 
        static_Logger_Colname__AgeNe_Sim_DemographicTables_Total_EOR_Results = 'S_AGENE_DT_EOR_'
        static_Logger_Name__AgeNe_Sim_DemographicTables_Total_EOR_Results = 'S_AGENE_DT_EOR_Stats'
        static_Logger_File_Suffix__AgeNe_Sim_DemographicTables_Total_EOR_Results = '.dl_S_AGENE_DT_eor_ssim'
 
        static_Logger_Colname__AgeNe_Sim_Final_Totals_EOR_Results = 'S_AGENE_FT_EOR_'
        static_Logger_Name__AgeNe_Sim_Final_Totals_EOR_Results = 'S_AGENE_FT_EOR_Stats'
        static_Logger_File_Suffix__AgeNe_Sim_Final_Totals_EOR_Results = '.dl_S_AGENE_FT_eor_ssim'
        
        '''
        ~~~~~~~~~~~~~~~~~~
        AgeNe PF Loggers
        ~~~~~~~~~~~~~~~~~~
        '''        
        static_Logger_Colname__AgeNe_Sim_Details_PF_Results = 'S_AGENE_D_PF_'
        static_Logger_Name__AgeNe_Sim_Details_PF_Results = 'S_AGENE_D_PF_Stats'
        static_Logger_File_Suffix__AgeNe_Sim_Details_PF_Results = '.dl_S_AGENE_D_pf_ssim'
 
        static_Logger_Colname__AgeNe_Sim_LifeTables_Total_PF_Results = 'S_AGENE_LT_PF_'
        static_Logger_Name__AgeNe_Sim_LifeTables_Total_PF_Results = 'S_AGENE_LT_PF_Stats'
        static_Logger_File_Suffix__AgeNe_Sim_LifeTables_Total_PF_Results = '.dl_S_AGENE_LT_pf_ssim'
 
        static_Logger_Colname__AgeNe_Sim_DemographicTables_Total_PF_Results = 'S_AGENE_DT_PF_'
        static_Logger_Name__AgeNe_Sim_DemographicTables_Total_PF_Results = 'S_AGENE_DT_PF_Stats'
        static_Logger_File_Suffix__AgeNe_Sim_DemographicTables_Total_PF_Results = '.dl_S_AGENE_DT_pf_ssim'
 
        static_Logger_Colname__AgeNe_Sim_Final_Totals_PF_Results = 'S_AGENE_FT_PF_'
        static_Logger_Name__AgeNe_Sim_Final_Totals_PF_Results = 'S_AGENE_FT_PF_Stats'
        static_Logger_File_Suffix__AgeNe_Sim_Final_Totals_PF_Results = '.dl_S_AGENE_FT_pf_ssim'

        static_Logger_Colname__Genepop_Allele_Freq_By_Allele_PF_Results = 'AFBA'
        static_Logger_File_Heading__Prefix_1__Genepop_Allele_Freq_By_Allele_PF_Results = 'AFBA_'
        static_Logger_File_Suffix__Genepop_Allele_Freq_By_Allele_PF_Results = '.AFBA_'

        static_Logger_Colname_Prefix__Ne2_LDNe_Pcrit_Exp1 = 'NPC1'        
        static_Logger_Name__Ne2_LDNe_Pcrit_Exp1 = 'LDNe_Pcrit_Sampling_Stats_1'
        static_Logger_File_Suffix__Ne2_LDNe_Pcrit_Exp1 = '.dl_NPC1_ssim'
        
    class Ne2_LDNe_Results_Details(object): 
        
        static_File_Suffix__Ne2_LDNe_TAB_File_Results = 'xLD.txt'
           
    class Excel_Results_File_Details(object):

        static_Excel_Colname_Prefix__Embryo_Parent_Ne_Stats_Post_Fertilization = 'PO_PF_R_MCST'
        static_Excel_FileName__Embryo_Parent_Ne_Stats_Post_Fertilization = '_Parent_Off_PF_Group_By_Run_By_MateCountSimTot_'
        static_Excel_SheetName__Embryo_Parent_Ne_Stats_Post_Fertilization = static_Excel_Colname_Prefix__Embryo_Parent_Ne_Stats_Post_Fertilization

        
        '''
        ---------------------
        SIM/BATCH/REPLICATE LEVEL Reporting Results
        ---------------------
        '''
        static_Excel_Colname_Prefix__SS_LEVEL_Results = ''
        static_Excel_FileName__SS_LEVEL_Results = 'SS_LEVEL_Results'
        static_Excel_SheetName__SS_LEVEL_SIM_Results = 'SIM'
        static_Excel_SheetName__SS_LEVEL_BATCH_Results = 'BATCH'
        static_Excel_SheetName__SS_LEVEL_REPLICATE_EOR_Results = 'REPLICATE_EOR'
        static_Excel_SheetName__SS_LEVEL_REPLICATE_PF_Results = 'REPLICATE_PF'
        static_Excel_SheetName__SS_LEVEL_VSP_AgeCohort_EOR_Results = 'VSP_AC_EOR'
        static_Excel_SheetName__SS_LEVEL_VSP_AgeCohort_PF_Results = 'VSP_AC_PF'
        static_Excel_SheetName__SS_LEVEL_VSP_LifeStage_EOR_Results = 'VSP_LS_EOR'
        static_Excel_SheetName__SS_LEVEL_VSP_LifeStage_PF_Results = 'VSP_LS_PF'
        
        '''
        ---------------------
        EXPERIMENT_Parent_Offspring_Ne_1
        ---------------------
        '''
        static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results = 'EXP1_PO_PF_SUMM'
        static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results = '_EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results_'
        static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results = static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results

        static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results = 'EXP1_CAT_NE2'
        static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results = '_EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results_'
        static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results = static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results

        static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results = 'EXP1_COMP'
        static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results = '_EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results_'
        static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results = static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results
        
        static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results = 'EXP1_SUMM'
        static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results = '_EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results_'
        static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results = static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results
        
        '''
        ---------------------
        EXPERIMENT_Parent_Offspring_Ne_2_PostSim_Results
        ---------------------
        '''
#         static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PS_PF_Results = 'EXP2_PS_CAT_NE2'
#         #static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PS_PF_Results = '_EXP2_Parent_Offsp_Ne_2__Cat_Ne2_PS_PF_Results_'
#         static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PS_PF_Results = '_EXP_Cat_Ne2_PS_PF_Results_'
#         static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PS_PF_Results = static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PS_PF_Results
        #static_Excel_Colname_Prefix__Ne2_LDNe__Raw_EOR_Results = 'NE2_LDNE__RAW_EOR_PS'
        static_Excel_Colname_Prefix__Ne2_LDNe__Raw_EOR_Results = 'LDNE2_RAW'
        static_Excel_FileName__Ne2_LDNe__Raw_EOR_Results = '_Ne2_LDNe__Raw_EOR_PS_Results' #+ '_'
        static_Excel_SheetName__Ne2_LDNe__Raw_EOR_Results = static_Excel_Colname_Prefix__Ne2_LDNe__Raw_EOR_Results

        #static_Excel_Colname_Prefix__Ne2_LDNe__Categorised_EOR_Results = 'NE2_LDNE__CAT_EOR_PS'
        static_Excel_Colname_Prefix__Ne2_LDNe__Categorised_EOR_Results = 'LDNE2_CAT'
        static_Excel_FileName__Ne2_LDNe__Categorised_EOR_Results = '_Ne2_LDNe__Categorised_EOR_Results' #+ '_'
        static_Excel_SheetName__Ne2_LDNe__Categorised_EOR_Results = static_Excel_Colname_Prefix__Ne2_LDNe__Categorised_EOR_Results

        #static_Excel_Colname_Prefix__Ne2_LDNe__Composite_EOR_Results = 'NE2_LDNE__COMP_EOR_PS'
        static_Excel_Colname_Prefix__Ne2_LDNe__Composite_EOR_Results = 'LDNE2_COMP'
        static_Excel_FileName__Ne2_LDNe__Composite_EOR_Results = '_Ne2_LDNe__Composite_EOR_Results' #+ '_'
        static_Excel_SheetName__Ne2_LDNe__Composite_EOR_Results = static_Excel_Colname_Prefix__Ne2_LDNe__Composite_EOR_Results

#         static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results = 'EXP2_PS_COMP'
#         #static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results = '_EXP2_Parent_Offsp_Ne_2__PS_Composite_Results_'
#         static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results = '_EXP_Cat_Ne2_PS_Composite_'
#         static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results = static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results
        
        #static_Excel_Colname_Prefix__Ne2_LDNe__Summary_EOR_Results = 'NE2_LDNE__SUMM_EOR_PS' 
        static_Excel_Colname_Prefix__Ne2_LDNe__Summary_EOR_Results = 'LDNE2_SUMM'
        static_Excel_FileName__Ne2_LDNe__Summary_EOR_Results = '_Ne2_LDNe__Summary_EOR_Results' #+ '_'
        static_Excel_SheetName__Ne2_LDNe__Summary_EOR_Results = static_Excel_Colname_Prefix__Ne2_LDNe__Summary_EOR_Results

#         static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results = 'EXP2_PS_SUMM'
#         #static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results = '_EXP2_Parent_Offsp_Ne_2__PS_Summary_Results_'
#         static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results = '_EXP_Cat_Ne2_PS_Summary_'
#         static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results = static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results
                
        '''
        ---------------------
        SAMPLING_INDIVS_Results
        ---------------------
        '''
        static_Excel_Colname_Prefix__SAMPLING_INDIVS__Aggregate_Results = 'INDIV_SAMPLES'
        static_Excel_FileName__SAMPLING_INDIVS__Aggregate_Results = '_INDIV_SAMPLES__Aggregate_Results'
        static_Excel_SheetName__SAMPLING_INDIVS__Aggregate_Results = static_Excel_Colname_Prefix__SAMPLING_INDIVS__Aggregate_Results
        
        static_Excel_Colname_Prefix__SAMPLING_INDIVS_Summary__Aggregate_Results = 'INDIV_SAMP_SUMM'
        static_Excel_FileName__SAMPLING_INDIVS_Summary__Aggregate_Results = '_INDIV_SAMPLES_SUMMARY__Aggregate_Results'
        static_Excel_SheetName__SAMPLING_INDIVS_Summary__Aggregate_Results = static_Excel_Colname_Prefix__SAMPLING_INDIVS_Summary__Aggregate_Results
        
        '''
        ---------------------
        EXPERIMENT_Parent_Offspring_Ne_2
        ---------------------
        '''
        static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results = 'EXP2_RAW_NE2'
        static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results = '_EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results_'
        static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results = static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results
        
        static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results = 'EXP2_CAT_NE2'
        static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results = '_EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results_'
        static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results = static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results
        
        static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results = 'EXP2_COMP'
        static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results = '_EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results_'
        static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results = static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results
        
        static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results = 'EXP2_SUMM'
        static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results = '_EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results_'
        static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results = static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results
        
        '''
        ---------------------
        AgeNe Sim - EOR Aggregate Results
        ---------------------
        '''        
        ''' AgeNe Manual Results '''
        static_Excel_Colname_Prefix__AgeNe_Man_Details_EOR_Results = 'M_AGENE_D_EOR'
        static_Excel_SheetName__AgeNe_Man_Details_EOR_Results = 'M_AGENE_D_EOR_Stats'
 
        static_Excel_Colname_Prefix__AgeNe_Man_LifeTables_Total_EOR_Results = 'M_AGENE_LT_EOR'
        static_Excel_SheetName__AgeNe_Man_LifeTables_Total_EOR_Results = 'M_AGENE_LT_EOR_Stats'
 
        static_Excel_Colname_Prefix__AgeNe_Man_DemographicTables_Total_EOR_Results = 'M_AGENE_DT_EOR'
        static_Excel_SheetName__AgeNe_Man_DemographicTables_Total_EOR_Results = 'M_AGENE_DT_EOR_Stats'
 
        static_Excel_Colname_Prefix__AgeNe_Man_Final_Totals_EOR_Results = 'M_AGENE_FT_EOR'
        static_Excel_SheetName__AgeNe_Man_Final_Totals_EOR_Results = 'M_AGENE_FT_EOR_Stats'
 
        ''' AgeNe Sim Results '''
        static_Excel_Colname_Prefix__AgeNe_Sim_Details_EOR_Results = 'S_AGENE_D_EOR'
        static_Excel_SheetName__AgeNe_Sim_Details_EOR_Results = 'S_AGENE_D_EOR_Stats'
 
        static_Excel_Colname_Prefix__AgeNe_Sim_LifeTables_Total_EOR_Results = 'S_AGENE_LT_EOR'
        static_Excel_SheetName__AgeNe_Sim_LifeTables_Total_EOR_Results = 'S_AGENE_LT_EOR_Stats'
 
        static_Excel_Colname_Prefix__AgeNe_Sim_DemographicTables_Total_EOR_Results = 'S_AGENE_DT_EOR'
        static_Excel_SheetName__AgeNe_Sim_DemographicTables_Total_EOR_Results = 'S_AGENE_DT_EOR_Stats'
 
        static_Excel_Colname_Prefix__AgeNe_Sim_Final_Totals_EOR_Results = 'S_AGENE_FT_EOR'
        static_Excel_SheetName__AgeNe_Sim_Final_Totals_EOR_Results = 'S_AGENE_FT_EOR_Stats'

        static_Excel_FileName__AgeNe_Sim_Aggregate_ALL_EOR__Summary_Results_Short_Name = 'S_AGENE_EOR_SUMM'        
        static_Excel_FileName__AgeNe_Sim_Aggregate_ALL_EOR__Summary_Results = '_AgeNe_Sim_Aggregate_ALL_EOR__Summary_Results_'        

        static_Excel_FileName__AgeNe_Man_Aggregate_ALL_EOR__Summary_Results_Short_Name = 'M_AGENE_EOR_SUMM'        
        static_Excel_FileName__AgeNe_Man_Aggregate_ALL_EOR__Summary_Results = '_AgeNe_Man_Aggregate_ALL_EOR__Summary_Results_'        
        
        static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results = 'S_AGENE_EOR_MERGE'
        static_Excel_FileName__AgeNe_Sim_Merge_ALL_EOR__Summary_Results = '_AgeNe_Sim_Merge_ALL_EOR__Summary_Results_'
        static_Excel_SheetName__AgeNe_Sim_Merge_ALL_EOR__Summary_Results = static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results

        static_Excel_Colname_Prefix__AgeNe_Man_Merge_ALL_EOR__Summary_Results = 'M_AGENE_EOR_MERGE'
        static_Excel_FileName__AgeNe_Man_Merge_ALL_EOR__Summary_Results = '_AgeNe_Man_Merge_ALL_EOR__Summary_Results_'
        static_Excel_SheetName__AgeNe_Man_Merge_ALL_EOR__Summary_Results = static_Excel_Colname_Prefix__AgeNe_Man_Merge_ALL_EOR__Summary_Results
   
        
        '''
        ---------------------
        AgeNe Sim EOR - Merge All Results
        ---------------------
        '''        
        static_Excel_Colname_Prefix__AgeNe_Sim_Summarise_ALL_EOR__Summary_Results = 'S_AGENE_EOR_SUMM'
        static_Excel_FileName__AgeNe_Sim_Summarise_ALL_EOR__Summary_Results = '_AgeNe_Summarise_ALL_EOR__Summary_Results_'
        static_Excel_SheetName__AgeNe_Sim_Summarise_ALL_EOR__Summary_Results = static_Excel_Colname_Prefix__AgeNe_Sim_Summarise_ALL_EOR__Summary_Results
                
        static_Excel_Colname_Prefix__AgeNe_Man_Summarise_ALL_EOR__Summary_Results = 'M_AGENE_EOR_SUMM'
        static_Excel_FileName__AgeNe_Man_Summarise_ALL_EOR__Summary_Results = '_AgeNe_Summarise_ALL_EOR__Summary_Results_'
        static_Excel_SheetName__AgeNe_Man_Summarise_ALL_EOR__Summary_Results = static_Excel_Colname_Prefix__AgeNe_Man_Summarise_ALL_EOR__Summary_Results


        '''
        ---------------------
        AgeNe Sim - PF Aggregate Results
        ---------------------
        '''     
        ''' AgeNe Sim Results '''
        static_Excel_Colname_Prefix__AgeNe_Sim_Details_PF_Results = 'S_AGENE_D_PF'
        static_Excel_SheetName__AgeNe_Sim_Details_PF_Results = 'S_AGENE_D_PF_Stats'
 
        static_Excel_Colname_Prefix__AgeNe_Sim_LifeTables_Total_PF_Results = 'S_AGENE_LT_PF'
        static_Excel_SheetName__AgeNe_Sim_LifeTables_Total_PF_Results = 'S_AGENE_LT_PF_Stats'
 
        static_Excel_Colname_Prefix__AgeNe_Sim_DemographicTables_Total_PF_Results = 'S_AGENE_DT_PF'
        static_Excel_SheetName__AgeNe_Sim_DemographicTables_Total_PF_Results = 'S_AGENE_DT_PF_Stats'
 
        static_Excel_Colname_Prefix__AgeNe_Sim_Final_Totals_PF_Results = 'S_AGENE_FT_PF'
        static_Excel_SheetName__AgeNe_Sim_Final_Totals_PF_Results = 'S_AGENE_FT_PF_Stats'

        static_Excel_FileName__AgeNe_Sim_Aggregate_ALL_PF__Summary_Results_Short_Name = 'S_AGENE_PF_SUMM'        
        static_Excel_FileName__AgeNe_Sim_Aggregate_ALL_PF__Summary_Results = '_AgeNe_Sim_Aggregate_ALL_PF__Summary_Results_'        

        static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results = 'S_AGENE_PF_MERGE'
        static_Excel_FileName__AgeNe_Sim_Merge_ALL_PF__Summary_Results = '_AgeNe_Sim_Merge_ALL_PF__Summary_Results_'
        static_Excel_SheetName__AgeNe_Sim_Merge_ALL_PF__Summary_Results = static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results


        '''
        ---------------------
        AgeNe Sim PF - Merge All Results
        ---------------------
        '''        
        static_Excel_Colname_Prefix__AgeNe_Sim_Summarise_ALL_PF__Summary_Results = 'S_AGENE_PF_SUMM'
        static_Excel_FileName__AgeNe_Sim_Summarise_ALL_PF__Summary_Results = '_AgeNe_Summarise_ALL_PF__Summary_Results_'
        static_Excel_SheetName__AgeNe_Sim_Summarise_ALL_PF__Summary_Results = static_Excel_Colname_Prefix__AgeNe_Sim_Summarise_ALL_PF__Summary_Results
                
        static_Excel_Colname_Prefix__AgeNe_Man_Summarise_ALL_PF__Summary_Results = 'M_AGENE_PF_SUMM'
        static_Excel_FileName__AgeNe_Man_Summarise_ALL_PF__Summary_Results = '_AgeNe_Summarise_ALL_PF__Summary_Results_'
        static_Excel_SheetName__AgeNe_Man_Summarise_ALL_PF__Summary_Results = static_Excel_Colname_Prefix__AgeNe_Man_Summarise_ALL_PF__Summary_Results

        '''
        ---------------------
        Genepop Allele Freq By Allele - Summarise All Results
        ---------------------
        '''        
        static_Excel_FileName__Genepop_Allele_Freqs_By_Allele__Embryo_PF__Aggregate_ALL__Summary_Results_Sheet_Name = 'AFBA_Embryo_PF'        
        static_Excel_FileName__Genepop_Allele_Freqs_By_Allele__Mature_PF__Aggregate_ALL__Summary_Results_Sheet_Name = 'AFBA_Mature_PF'        
        static_Excel_FileName__Genepop_Allele_Freqs_By_Allele__SP_0_Full_PF__Aggregate_ALL__Summary_Results_Sheet_Name = 'AFBA_SP_0_Full_PF'        
        static_Excel_FileName__Genepop_Allele_Freqs_By_Allele__SP_0_Full_PF__Aggregate_ALL__Summary_Results_Short_Name = 'AFBA_PF'        
        
        static_Excel_Colname_Prefix__Genepop_Allele_Freqs_By_Allele__Aggregate_ALL__Summary_Results = 'AFBA_PF'
        static_Excel_FileName__Genepop_Allele_Freqs_By_Allele__Aggregate_ALL__Summary_Results = '_Genepop_Allele_Freq_By_Allele__Aggregate_Results_'        

        '''
        ---------------------
        LOCUS_JACKNIFING_Ne2Bulk_Results
        ---------------------
        '''
        static_Excel_Colname_Prefix__func_LOCUS_JACKNIFING_Ne2Bulk_Results__Aggregate_Results = 'LOCUS_JK_NE2B'
        static_Excel_FileName__func_LOCUS_JACKNIFING_Ne2Bulk_Results__Aggregate_Results = '_LOCUS_JACKNIFE__Aggregate_Ne2Bulk_Results_'
        static_Excel_SheetName__func_LOCUS_JACKNIFING_Ne2Bulk_Results__Aggregate_Results = static_Excel_Colname_Prefix__func_LOCUS_JACKNIFING_Ne2Bulk_Results__Aggregate_Results



    class Figure_Colour_Schemes(object):
        
        static_str_Figure_Colour_Scheme__Dark_Blue = 'Dark_Blue'
        
    class Experment_Groups(object):
        
        static_int_Experiment_2_Ver_0 = 0
        static_str_Experiment_2_Ver_0_Label = 'EXP2_0'
        static_int_Experiment_2_Ver_1 = 1
        static_str_Experiment_2_Ver_1_Label = 'EXP2_1'
        static_int_Experiment_2_Ver_2 = 2
        static_str_Experiment_2_Ver_2_Label = 'EXP2_2'
        static_int_Experiment_2_Ver_3 = 9
        static_str_Experiment_2_Ver_3_Label = 'EXP2_3'
        
        static_int_Experiment_2_CAPL_FISHED_PROPORTIONS_v1_0 = 2
        static_int_Experiment_2_CAOB_FISHED_PROPORTIONS_v1_0 = 3
                       
        static_int_Experiment_2_CAPL_FISHED_ABSOLUTE_v1_0 = 4
        static_int_Experiment_2_CAOB_FISHED_ABSOLUTE_v1_0 = 5
        
        static_int_Experiment_2_CAPL_FISHED_PROPORTIONS_SCALED_BY_MAX_ABSOLUTE_v1_0 = 6
        static_int_Experiment_2_CAPL_FISHED_ABS_SCALED_BY_MAX_ABSOLUTE_v1_0 = 7
        static_int_Experiment_2_CAOB_FISHED_ABS_SCALED_BY_MAX_ABSOLUTE_v1_0 = 8
        
        static_int_Experiment_Sampling_Strategy_v1_0 = 10
        static_str_Experiment_Sampling_Strategy_v1_0_Label = 'S_STRAT_1_0'

        static_int_Experiment_Sampling_Strategy_v1_1__USER_AGE_COHORTS = 11
        static_str_Experiment_Sampling_Strategy_v1_1__USER_AGE_COHORTS_Label = 'S_STRAT_1_1_UAC'
                
        static_int_Experiment_Sampling_Strategy_v1_1__USER_PROPORTIONS = 12
        static_str_Experiment_Sampling_Strategy_v1_1__USER_PROPORTIONS_Label = 'S_STRAT_1_1_UP'   
                            
        static_int_Experiment_100_PERCENT_USER_SPECIFIED_AGE_COHORTS_v1_0 = 13
        static_str_Experiment_100_PERCENT_USER_SPECIFIED_AGE_COHORTS_v1_0_Label = '100P_A_COHORTS'   

        static_int_Experiment_Sampling_Strategy_v1_1__USER_SAMPLE_NUMBERS = 14
        static_str_Experiment_Sampling_Strategy_v1_1__USER_SAMPLE_NUMBERS_Label = 'S_STRAT_1_1_USN'   
        
        static_int_Experiment_Sampling_Strategy_v1_1__USER_SAMPLE_PROPORTIONS = 15
        static_int_Experiment_Sampling_Strategy_v1_1__USER_SAMPLE_PROPORTIONS_Label = 'S_STRAT_1_1_USP'   

        static_int_Experiment_FULL_EMBRYO_COHORT = 16
        static_str_Experiment_FULL_EMBRYO_COHORT_Label = 'FEM_EMBRYOS'   

        static_int_Experiment_FULL_JUVENILE_COHORTS = 17
        static_str_Experiment_FULL_JUVENILE_COHORTS_Label = 'FJV_JUVENILES'   

        static_int_Experiment_FULL_ADULT_COHORTS = 18
        static_str_Experiment_FULL_ADULT_COHORTS_Label = 'FMT_ADULTS'   

        static_int_Experiment_FULL_SAMPLING_OF_COHORTS = 19
        static_str_Experiment_FULL_SAMPLING_OF_COHORTS_Label = 'FUL_COHORTS'   
        
        static_int_Experiment_SAMPLING_PROPORTIONS_SCALED_BY_MAX_PROPORTION = 20
        static_str_Experiment_SAMPLING_PROPORTIONS_SCALED_BY_MAX_PROPORTION_Label = 'SCALED_MAX_PROP'   
        
    class Categorised_Ne2_Sampling_Stats(object):
    
        '''General'''
        static_Label_Gen_UniqueID = 'Unique_Run_ID'
        static_Label_Gen_File = 'CAT_NE2_'
        static_Label_Gen_Source_UniqueID = static_Label_Gen_File + 'Source_UID'
        static_Label_Gen_Source_Unique_Run_Batch_Rep_VSP_ID = 'Unique_Run_Batch_Rep_VSP_ID'
        
    class Ne2_Sampling_Stats(object):
    
        '''General'''
        static_Label_Gen_UniqueID = 'Unique_Run_ID'
        static_Label_Gen_File = 'GP_Ne2_'
        static_Label_Gen_Source_UniqueID = static_Label_Gen_File + 'Source_UID'
        static_Label_Gen_Source_Unique_Run_Batch_Rep_VSP_ID = 'Unique_Run_Batch_Rep_VSP_ID'
        
        
        static_Label_Colname_c_floatRSquared_Observed = 'c_floatRSquared_Observed'
        static_Label_Colname_c_floatRSquared_Expected = 'c_floatRSquared_Expected'
        static_Label_Colname_float_Burrows_r_Squared_Diff = 'float_Burrows_r_Squared_Diff'
        static_Label_Colname_float_Burrows_r_Sqrd_LDNe = 'float_Burrows_r_Sqrd_LDNe'

    class Colnames_Genepop_Allele_Freqs_By_Allele_Results(object):
        
        '''
        ----------------
        Genepop_Allele_Freqs_By_Allele Details
        ----------------
        '''
        static_Colname_Prefix_AFBA = ''
        static_str_Colname_Pop_Name = static_Colname_Prefix_AFBA + 'Pop_Name'
        static_str_Colname_Pop_Gene_Count = static_Colname_Prefix_AFBA + 'Pop_Gene_Count'
        static_str_Colname_Locus_Allele_Freqs = static_Colname_Prefix_AFBA + 'Locus_Allele_Freqs'
        static_str_Colname_Locus_Name = static_Colname_Prefix_AFBA + 'Locus_Name'
        static_str_Colname_Allele_Name = static_Colname_Prefix_AFBA + 'Allele_Name'
        static_str_Colname_Allele_Freq = static_Colname_Prefix_AFBA + 'Allele_Freq'
        
        
    class Colnames_AgeNe_Results(object):
        
        '''
        ----------------
        AgeNe Life Table Details
        ----------------
        '''
        static_Colname_Prefix_LT = 'LT__'
        static_str_Colname_N1 = static_Colname_Prefix_LT + 'N1'
        static_str_Colname_Age = static_Colname_Prefix_LT + 'Age'
        static_str_Colname_sx = static_Colname_Prefix_LT + 'sx'
        static_str_Colname_bx = static_Colname_Prefix_LT + 'bx.'
        static_str_Colname_lx = static_Colname_Prefix_LT + 'lx'
        static_str_Colname_bxlx = static_Colname_Prefix_LT + 'bxlx'
        static_str_Colname_b_x = static_Colname_Prefix_LT + 'b_x'
        static_str_Colname_bxNx = static_Colname_Prefix_LT + 'bxNx'
        static_str_Colname_Nx = static_Colname_Prefix_LT + 'Nx'
        static_str_Colname_Bx = static_Colname_Prefix_LT + 'Bx'
        static_str_Colname_xBx_Div_N1 = static_Colname_Prefix_LT + 'xBx/N1'
        
        '''
        ----------------
        AgeNe LifeTable Totals
        ----------------
        '''
        static_Colname_Prefix_LTT = 'LTT__'
        static_str_Colname_L_All = static_Colname_Prefix_LTT + 'L_All'
        static_str_Colname_Nx_N_Adults = static_Colname_Prefix_LTT + 'Nx_N_Adults'
        static_str_Colname_Nx_Nc_Adults = static_Colname_Prefix_LTT + 'Nx_Nc_Adults'
        static_str_Colname_Nx_All = static_Colname_Prefix_LTT + 'Nx_All'
        static_str_Colname_bxNx_Sum_All = static_Colname_Prefix_LTT + 'bxNx_Sum_All'
                
        '''
        ----------------
        AgeNe DemographicTable 
        ----------------
        '''
        static_Colname_Prefix_DT = 'DT__'
        static_str_Colname_kbarx = static_Colname_Prefix_DT + 'kbarx'
        static_str_Colname_Vx = static_Colname_Prefix_DT + 'Vx'
        static_str_Colname_Dx = static_Colname_Prefix_DT + 'Dx'
        static_str_Colname_kbarDx = static_Colname_Prefix_DT + 'kbarDx'
        static_str_Colname_kbarAll = static_Colname_Prefix_DT + 'kbarAll'
        static_str_Colname_delta_kbar = static_Colname_Prefix_DT + 'delta_kbar'
        static_str_Colname_SSDIx = static_Colname_Prefix_DT + 'SSDIx'
        static_str_Colname_SSDGx = static_Colname_Prefix_DT + 'SSDGx'
        static_str_Colname_SSDx = static_Colname_Prefix_DT + 'SSDx'
        static_str_Colname_Yx = static_Colname_Prefix_DT + 'Yx'
        static_str_Colname_Nb_Vx_All = static_Colname_Prefix_DT + 'Nb_Vx_All'
        
        '''
        ----------------
        AgeNe DemographicTable Totals
        ----------------
        '''
        static_Colname_Prefix_DTT = 'DTT__'
        #static_Colname_Prefix_DTFT = 'FTT__'
        static_str_Colname_SSD_T = static_Colname_Prefix_DTT + 'SSD_T'
        static_str_Colname_Vk_All = static_Colname_Prefix_DTT + 'Vk_All'
        static_str_Colname_kbar_All = static_Colname_Prefix_DTT + 'kbar_All'
        static_str_Colname_kbarx_Dx_All = static_Colname_Prefix_DTT + 'kbarx_Dx_All'
        ''' For ALL sexes catgorical lines'''
#         static_Colname_Prefix_DTT_Replacement = 'DTTAS__'
#         static_str_Colname_SSD_T_ForAllSex = static_Colname_Prefix_DTT_Replacement + 'SSD_T'
#         static_str_Colname_Vk_All_ForAllSex = static_Colname_Prefix_DTT_Replacement + 'Vk_All'
#         static_str_Colname_kbar_All_ForAllSex = static_Colname_Prefix_DTT_Replacement + 'kbar_All'
#         static_str_Colname_kbarx_Dx_All_ForAllSex = static_Colname_Prefix_DTT_Replacement + 'kbarx_Dx_All'
                
        '''
        ----------------
        AgeNe FinalOverall Totals
        ----------------
        '''
        static_Colname_Prefix_FTT = 'FTT__'
        static_str_Colname_L_Overall = static_Colname_Prefix_FTT + 'L_Overall'
        static_str_Colname_N_Adults_Overall = static_Colname_Prefix_FTT + 'N_Adults_Overall'
        static_str_Colname_Nc_Adults_Overall = static_Colname_Prefix_FTT + 'Nc_Adults_Overall'
        static_str_Colname_N_Overall = static_Colname_Prefix_FTT + 'N_Overall'
        static_str_Colname_NbDemo = static_Colname_Prefix_FTT + 'NbDemo'
        static_str_Colname_Nb_Vx_All_Sexes_Overall = static_Colname_Prefix_FTT + 'Nb_Vx_all_sexes_Overall'
        static_str_Colname_NeDemo = static_Colname_Prefix_FTT + 'NeDemo.'
        #static_str_Colname_NeDemoDivNAdultsOverall = static_Colname_Prefix_FTT + 'NeDemoDivNAdultsOverall'
        static_str_Colname_NeDemoDivNcAdultsOverall = static_Colname_Prefix_FTT + 'NeDemoDivNcAdultsOverall'
        static_str_Colname_NeDemoDivNOverall = static_Colname_Prefix_FTT + 'NeDemoDivNOverall'
        static_str_Colname_Vk_Overall = static_Colname_Prefix_FTT + 'Vk_Overall'
        static_str_Colname_kbar_Overall = static_Colname_Prefix_FTT + 'kbar_Overall'
        static_str_Colname_Nb_Vx_All_Sexes = static_Colname_Prefix_FTT + 'Nb_Vx_All_sexes'
        static_str_Colname_Nb_kbar_All_Sexes = static_Colname_Prefix_FTT + 'Nb_kbar_All_sexes'               
        static_str_Colname_Male_N1_Ratio = static_Colname_Prefix_FTT + 'Male_N1_Ratio'               
    
    class Colnames_Parent_Offspring_Stats_METHOD_1(object):    
        '''
        --------------------------------------
        Parent Offspring Counts by Sex & Demographic Ne (DCB C&D 1988) - METHOD 1
        --------------------------------------
        '''
        static_Colname_Prefix = 'M1_'
        static_Str_Colname_int_NonUnique_Female_Effective_Gametes = static_Colname_Prefix + 'int_NonUnique_Female_Effective_Gametes'
        static_Str_Colname_int_NonUnique_Male_Effective_Gametes = static_Colname_Prefix + 'int_NonUnique_Male_Effective_Gametes'
        static_Str_Colname_int_NonUnique_Effective_Dame_Sire_Gamete_Pair_Count = static_Colname_Prefix + 'int_NonUnique_Effective_Dame_Sire_Gamete_Pair_Count'
        static_Str_Colname_int_Unique_Female_Effective_Gametes = static_Colname_Prefix + 'int_Unique_Female_Effective_Gametes'
        static_Str_Colname_int_Unique_Male_Effective_Gametes = static_Colname_Prefix + 'int_Unique_Male_Effective_Gametes'
        static_Str_Colname_int_Unique_Effective_Dame_Sire_Gamete_Pair_Count = static_Colname_Prefix + 'int_Unique_Effective_Dame_Sire_Gamete_Pair_Count'
        static_Str_Colname_int_Total_NonUnique_Gametes = static_Colname_Prefix + 'int_Total_NonUnique_Gametes'
        static_Str_Colname_int_Total_Unique_Gametes = static_Colname_Prefix + 'int_Total_Unique_Gametes'
        static_Str_Colname_Demo_Ne_By_Sex = static_Colname_Prefix + 'Demo_Ne_By_Sex_=_4(Nf.Nm)/(Nf+Nm)'
        static_Str_Colname_float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating = static_Colname_Prefix + 'float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating'
        static_Str_Colname_float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn = static_Colname_Prefix + 'float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn'
        static_Str_Colname_float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn = static_Colname_Prefix + 'float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn'
        static_Str_Colname_float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate = static_Colname_Prefix + 'float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate'

    class Pandas_Aggregate_Function_Keyword(object):
        
        static_str_Pandas_Aggregate_Function_Keyword__first = 'first'
        static_str_Pandas_Aggregate_Function_Keyword__last = 'last'
        static_str_Pandas_Aggregate_Function_Keyword__sum = 'sum'
        static_str_Pandas_Aggregate_Function_Keyword__mean = 'mean'
        static_str_Pandas_Aggregate_Function_Keyword__median = 'median'

    class Colnames_Parent_Offspring_Stats_METHOD_2(object):        
        '''
        --------------------------------------
        Parent Offspring Counts by Sex, Reproductive Means & Variances by Sex, & Demographic Ne (DCB C&D 1988) - METHOD 2
        --------------------------------------
        '''
        static_Colname_Prefix = 'M2_'
        static_Str_Colname_Male_Potential_Parent = static_Colname_Prefix + 'Num_Male_Potential_Parent'
        static_Str_Colname_Mean_Offspring_Per_Male_Potential_Parent = static_Colname_Prefix + 'Mean_Offspring_Per_Male_Potential_Parent'
        static_Str_Colname_Mean_Variance_Offspring_Per_Male_Potential_Parent = static_Colname_Prefix + 'Mean_Variance_Offspring_Per_Male_Potential_Parent'
        static_Str_Colname_Demo_NeMale_Potential_Parents_NeM = static_Colname_Prefix + 'Demo_NeMale_Potential_Parents_NeM_=_((Nm.Mean(Km))-1)/((Mean(Km)-1)+(Var(Km)/mean(Km))'
        static_Str_Colname_Sires = static_Colname_Prefix + 'Num_Sires'
        static_Str_Colname_Mean_Offspring_Per_Sire = static_Colname_Prefix + 'Mean_Offspring_Per_Sire'
        static_Str_Colname_Mean_Variance_Offspring_Per_Sire = static_Colname_Prefix + 'Mean_Variance_Offspring_Per_Sire'
        static_Str_Colname_Demo_NeSires_NeS = static_Colname_Prefix + 'Demo_NeSires_NeS_=_((Ns.Mean(Ks))-1)/((Mean(Ks)-1)+(Var(Ks)/mean(Ks))'
        static_Str_Colname_Female_Potential_Parent = static_Colname_Prefix + 'Num_Female_Potential_Parent'
        static_Str_Colname_Mean_Offspring_Per_Female_Potential_Parent = static_Colname_Prefix + 'Mean_Offspring_Per_Female_Potential_Parent'
        static_Str_Colname_Mean_Variance_Offspring_Per_Female_Potential_Parent = static_Colname_Prefix + 'Mean_Variance_Offspring_Per_Female_Potential_Parent'
        static_Str_Colname_Ne_DemoFemale_Potential_Parents_NeF = static_Colname_Prefix + 'Ne_DemoFemale_Potential_Parents_NeF_=_((Nf.Mean(Kf))-1)/((Mean(Kf)-1)+(Var(Kf)/mean(Kf))'
        static_Str_Colname_Dames = static_Colname_Prefix + 'Num_Dames'
        static_Str_Colname_Mean_Offspring_Per_Dame = static_Colname_Prefix + 'Mean_Offspring_Per_Dame'
        static_Str_Colname_Mean_Variance_Offspring_Per_Dame = static_Colname_Prefix + 'Mean_Variance_Offspring_Per_Dame'
        static_Str_Colname_Demo_NeDames_NeD = static_Colname_Prefix + 'Demo_NeDames_NeD_=_((Nd.Mean(Kd))-1)/((Mean(Kd)-1)+(Var(Kd)/mean(Kd))'
        static_Str_Colname_Potential_Parents_PP = static_Colname_Prefix + 'Potential_Parents_PP'
        static_Str_Colname_Mean_Offspring_Per_PP = static_Colname_Prefix + 'Mean_Offspring_Per_PP'
        static_Str_Colname_Mean_Variance_Offspring_Per_PP = static_Colname_Prefix + 'Mean_Variance_Offspring_Per_PP'
        static_Str_Colname_Demo_NePP = static_Colname_Prefix + 'Demo_NePP_=_(4.NeF.NeM)/(NeF+NeM)'
        static_Str_Colname_Demo_NePP_Rato_Nc = static_Colname_Prefix + 'Demo_NePP_Rato_Nc'
        static_Str_Colname_Effective_Parents_EP = static_Colname_Prefix + 'Effective_Parents_EP'
        static_Str_Colname_Mean_Offspring_Per_EP = static_Colname_Prefix + 'Mean_Offspring_Per_EP'
        static_Str_Colname_Mean_Variance_Offspring_Per_EP = static_Colname_Prefix + 'Mean_Variance_Offspring_Per_EP'
        static_Str_Colname_Demo_NeEP = static_Colname_Prefix + 'Demo_NeEP_=_(4.NeD.NeS)/(NeD+NeS)'
        static_Str_Colname_Demo_NeEP_Rato_Nc = static_Colname_Prefix + 'Demo_NeEP_Rato_Nc'
        
    class Colnames_MEAN_Parent_Offspring_Stats(object):
        '''
        --------------------------------------
        Parent Offspring MEANS by Sex
        --------------------------------------
        '''        
        static_Str_Colname_Mean_NonUnique_Female_Effective_Parents = 'Mean_NonUnique_Female_Effective_Parents'
        static_Str_Colname_Mean_NonUnique_Male_Effective_Parents = 'Mean_NonUnique_Male_Effective_Parents'
        static_Str_Colname_Mean_Unique_Female_Effective_Parents = 'Mean_Unique_Female_Effective_Parents'
        static_Str_Colname_Mean_Unique_Male_Effective_Parents = 'Mean_Unique_Male_Effective_Parents'
        static_Str_Colname_Mean_Total_Unique_Effective_Parents = 'Mean_Total_Unique_Effective_Parents'
        
        static_Str_Colname_float_Grand_Mean_DCB_CD_Dem_Ne_By_Sex = 'float_Grand_Mean_DCB_CD_Dem_Ne_By_Sex'

    class Colnames_Pop_Sampling(object):
        
        static_Colname_Prefix = ''
        static_Str_Colname_Sampling_Params = static_Colname_Prefix + 'Sampling_Params'        
        static_Str_Colname_Sample_Replicates = static_Colname_Prefix + 'Sample_Replicates'        
        static_Str_Colname_Sample_Loci_To_Remove = static_Colname_Prefix + 'Loci_To_Remove'
        static_Str_Colname_Sampling_Method = static_Colname_Prefix + 'Sampling_Method'
        
    
    
    class Colnames_COMMON_STATS(object):
        '''
        --------------------------------------
        Colnames - COMMON to STATS
        --------------------------------------
        '''               
        static_str_Colname_Stats_Category__Full = 'Full'
        static_str_Colname_Stats_Category__Full_Mature = 'Full_Mature'
        static_str_Colname_Stats_Category__Full_Juvenile = 'Full_Juvenile'
        static_str_Colname_Stats_Category__Full_Embryo = 'Full_Embryo'
        static_str_Colname_Stats_Category__Full_Age_Cohorts = 'Full_Age_Cohorts'
        static_str_Colname_Stats_Category__Sampling_Proportions_Scaled_By_Max_Proportion = 'Scale_By_Max_Prop'
        
#         static_str_Colname_Stats_Category_Code__Full = 'FUL'
#         static_str_Colname_Stats_Category_Code__Full_Mature = 'FMT'
#         static_str_Colname_Stats_Category_Code__Full_Juvenile = 'FJV'
#         static_str_Colname_Stats_Category_Code__Full_Embryo = 'FEM'
#         static_str_Colname_Stats_Category_Code__Full_Age_Cohorts = 'FAC'
#         static_str_Colname_Stats_Category_Code__Sampling_Proportions_Scaled_By_Max_Proportion = 'PSMP'
    
    
    class Colnames_BATCH_PARAMETERS(object):
        '''
        --------------------------------------
        Colnames - common to BATCHes
        --------------------------------------
        '''               
        static_str_Colname_Max_age = 'Max_age'
        static_str_Colname_Max_mating_age = 'Max_mating_age'
        static_str_Colname_Min_mating_age = 'Min_mating_age'


    class Colnames_COMMON_EXPERIMENT(object):
        '''
        --------------------------------------
        Colnames - COMMON to EXPERIMENTs
        --------------------------------------
        '''               
        static_Str_Colname_Run_User_Defined_Folder = 'Run_User_Defined_Folder'
        static_Str_Colname_Experiment_Count = 'Experiment_Count'
        static_Str_Colname_Experiment_Label = 'Experiment_Label'
        static_Str_Colname_Unique_Run_ID = 'Unique_Run_ID'
        static_Str_Colname_Source_Data_Unique_Run_ID = 'Source_Unique_Run_ID'
        static_Str_Colname_Sim_Batches = 'Sim_Batches'
        static_Str_Colname_Sim_Replicates = 'Sim_Replicates'
        static_Str_Colname_Sim_MatingsToSimulatePerReplicate = 'Sim_MatingsToSimulatePerReplicate'
        static_Str_Colname_Sim_MatingsToSimulate = 'Sim_MatingsTotalToSimulate'
        static_Str_Colname_Sim_Last_Mating_In_Replicate = 'Sim_Last_Mating_In_Replicate'
        static_Str_Colname_Sim_Current_Batch = 'Sim_Current_Batch'
        static_Str_Colname_Sim_Current_Replicate = 'Sim_Current_Replicate'
        static_Str_Colname_Source_Data_Sim_Current_Batch = 'Sim_Source_Current_Batch'
        static_Str_Colname_Source_Data_Sim_Current_File = 'Sim_Source_Current_File'
        static_Str_Colname_Source_Data_Sim_Current_Replicate = 'Sim_Source_Current_Replicate'
        static_Str_Colname_Source_Data_Sim_Current_Replicate_Mating = 'Sim_Source_Current_Rep_Mating'
        static_Str_Colname_Replicate_Current_Year = 'Replicate_Current_Year'
        static_Str_Colname_Replicate_Current_Month = 'Replicate_Current_Month'
        static_Str_Colname_Burn_In = 'In_BurnIn'
        static_Str_Colname_Gens_Overlapp = 'Gens_Overlap'
        
        static_Str_Colname_int_MatingCount_Replicate_Total = 'int_MatingCount_Replicate_Total'
        static_Str_Colname_Pop_Size = 'Pop_Size'
        static_Str_Colname_Mating_Count_Sim_Total = 'Mating_Count_Sim_Total'
        static_Str_Colname_Mating_Count_Replicate_Total = 'Mating_Count_Replicate_Total'
        static_Str_Colname_Loci = 'Sim_Loci'
        static_Str_Colname_Alleles_Per_Locus = 'Alleles_Per_Locus'
        static_Str_Colname_Allow_Mutation = 'Allow_Mutation'
        static_Str_Colname_Mutation_Rate = 'Mutation_Rate'
        static_Str_Colname_str_Experiment_Category = 'str_Experiment_Category'
        static_Str_Colname_intSubSample_Size = 'intSubSample_Size'
        static_Str_Colname_Population_Sampled = 'Pop_Sampled'
        static_Str_Colname_Result_MultiLine_Count = 'Result_MultiLine_Count'
        static_Str_Colname_Stats_Categories = 'Stats_Categories'
        static_Str_Colname_Stats_Category = 'Stats_Category'
        static_Str_Colname_Stats_Category_Code = 'Stats_Cat_Code' #'Stats_Category_Code'
        static_Str_Colname_list_Stats_Categories = 'list_Stats_Categories'
        static_Str_Colname_Sex = 'Sex'
        static_Str_Colname_Mortality_Type = 'Mortality_Type'
        
        static_Str_Colname_Search_Path = 'Search_Path'
        
        static_Str_Colname_Random_SubSamples = 'Random_SubSamples'
        static_Str_Colname_Sample_Each_Mating_Count_Divisible_By = 'Sample_Each_Mating_Count_Divisible_By'
        static_Str_Colname_Pop_Starts_When_Mating_Count_Is = 'Pop_Starts_When_Mating_Count_Is' 
        
        static_Str_Colname_Sampling_Replicates = 'Random_SubSamples' #'Sampling_Replicates' 
        static_Str_Colname_Sampling_Replicate = 'Sampling_Replicate' 
        static_Str_Colname_Sampling_Replicate_Filename = 'Sampling_Rep_Filename' 
        static_Str_Colname_Sampling_Indiv_Number = 'SamplingIndiv_Number' 
        static_Str_Colname_Sampling_Loci_Number = 'SamplingLoci_Number' 
        static_Str_Colname_Sampling_Replicate = 'Sampling_Replicate' 
        static_Str_Colname_Age_In_Months = 'Age_In_Months' 
        static_Str_Colname_Source_VSP_Ages_And_Sizes = 'Source_VSP_Ages_And_Sizes' 
        static_Str_Colname_Source_VSP_Ages_And_Sizes__Ages = 'Source_VSP_Ages' 
        static_Str_Colname_Source_VSP_Ages_And_Sizes__Sizes = 'Source_VSP_Sizes' 
        static_Str_Colname_Sample_VSP_Ages_And_Sizes = 'Sample_VSP_Ages_And_Sizes'    
        static_Str_Colname_Sample_VSP_Ages_And_Sizes__Ages = 'Sample_VSP_Age'    
        static_Str_Colname_Sample_VSP_Ages_And_Sizes__Sizes = 'Sample_Size'    
        static_Str_Colname_Sample_Percent_VSP_Ages_And_Sizes = 'Sample_Percent_VSP_Ages_And_Sizes'    
        static_Str_Colname_Sample_Percent_VSP_Ages_And_Sizes__Ages = 'Sample_Percent_VSP_Age'    
        static_Str_Colname_Sample_Percent_VSP_Ages_And_Sizes__Sizes = 'Sample_Percent_Size'    

    class Colnames_EXPERIMENT_Parent_Offspring_Ne_1(object):
        '''
        --------------------------------------
        Colnames - EXPERIMENT_Parent_Offspring_Ne_1
        --------------------------------------
        '''               

        static_Str_Colname_SubSample_Sizes_By_Category = 'SubSample_Sizes_By_Category'
        static_Str_Colname_SubSample_Replicates_By_Category = 'SubSample_Replicates_By_Category'
        static_Str_Colname_VSPs_To_SubSample_By_Category = 'VSPs_To_SubSample_By_Category'
        static_Str_Colname_list_LDNe_PCrits_To_Get = 'list_LDNe_PCrits_To_Get'
        static_Str_Colname_strPCritsToProcess = 'PCrits_To_Process'
        
        static_Str_Colname_LDNe_PCrit = 'LDNe_PCrit'
        
#         static_Str_Colname_Ne2_Replicate_Current_Month = 'Ne2_Replicate_Current_Month'
#         static_Str_Colname_Ne2_Genepop_Source_File = 'Ne2_Genepop_Source_File'
#         static_Str_Colname_Ne2_Burn_In = 'Ne2_Burn_In'
#         static_Str_Colname_Ne2_list_Stats_Categories = 'Ne2_list_Stats_Categories'
#         static_Str_Colname_Ne2_SubSample_Replicates_By_Category = 'Ne2_SubSample_Replicates_By_Category'
#         static_Str_Colname_Ne2_int_MatingCount_Replicate_Total = 'Ne2_int_MatingCount_Replicate_Total'
        static_Str_Colname_Ne2_Experiment_Label = 'Ne2_Experiment_Label'
#         static_Str_Colname_Ne2_str_Stats_Category = 'Ne2_str_Stats_Category'
#         static_Str_Colname_Ne2_Genepop_Source_Path = 'Ne2_Genepop_Source_Path'
#         static_Str_Colname_Ne2_list_LDNe_PCrits_To_Get = 'Ne2_list_LDNe_PCrits_To_Get'
#         static_Str_Colname_Ne2_Genepop_Source_Path = 'Ne2_Genepop_Sorce_Path'
#         static_Str_Colname_Ne2_Unique_Run_Batch_Rep_VSP_ID = 'Ne2_Unique_Run_Batch_Rep_VSP_ID'
        static_Str_Colname_File = 'File'

        #static_Str_Colname_Ne2_Replicate_Current_Year = 'Ne2_Replicate_Current_Year'

    class Colnames_Ne2_LDNe_TAB_File_Output__Locus_Jackknifing:
        
        static_str_Colname_Ne2_TAB_Out__GPFileCount = 'GP_File_Count'
        static_str_Colname_Ne2_TAB_Out__Locus_Combo_Integer = 'Locus_Combo_Int'

    class Colnames_Emprical_Ne2_Processing:
        
        static_str_FilePath_Working_Ne2 = 'FilePath_Working_Ne2'
        static_str_Filename_Genepop = 'Filename_Genepop'
        static_str_OutputResultsPath = 'OutputResultsPath'
                     
    class Colnames_Ne2_Output(object):
        '''
        --------------------------------------
        Colnames - Ne2 Output Results
        --------------------------------------
        '''              
        
        static_Str_Colname_Genepop_Source_File = 'Sampling_Rep_Filename' #'Genepop_Source_File'
        
        static_Str_Colname_Ne2_intNeLoci = 'Ne2_intNeLoci'
        static_Str_Colname_Ne2_strPopID = 'Ne2_strPopID'
        static_Str_Colname_Ne2_intNeSamples = 'Ne2_intNeSamples'
        static_Str_Colname_Ne2_floatWeightedMeanSampleSize = 'Ne2_floatWeightedMeanSampleSize'
        static_Str_Colname_Ne2_intIndependentAlleles = 'Ne2_intIndependentAlleles'

        static_Str_Colname_Ne2_floatRSquared_Observed = 'Ne2_floatRSquared_Observed'
        static_Str_Colname_Ne2_floatRSquared_Expected = 'Ne2_floatRSquared_Expected'

        static_Str_Colname_Ne2_floatLDNe = 'Ne2_floatLDNe_Estimate'
        static_Str_Colname_Ne2_floatLDNe_Harmonic_Mean = 'Ne2_floatLDNe_Harmonic_Mean'
        static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI = 'Ne2_floatLDNeParametric_Lwr_CI'
        static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI = 'Ne2_floatLDNeParametric_Upr_CI'
        static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI = 'Ne2_floatLDNeJackknife_Lwr_CI'
        static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI = 'Ne2_floatLDNeJackknife_Upr_CI'
        static_Str_Colname_Ne2_floatLDNeJackknife_CI_Eff_DF = 'Ne2_floatLDNeJackknife_CI_Eff_DF'
                                        
        static_Str_Colname_Ne2_intMatingScheme = 'Ne2_intMatingScheme'
        static_Str_Colname_Ne2_floatPCrit = 'Ne2_floatPCrit'
       
        static_Str_Colname_Genepop_Source_Path = 'Genepop_Source_Path'

    class Colnames_Ne2_Aggregation(object):        
        '''Colnames - Ne2 Summary Stats'''

        static_Str_Colname_float_Ne2_Burrows_r_Squared__Observed = 'float_Ne2_Burrows_r_Squared__Observed'
        static_Str_Colname_float_Ne2_Burrows_r_Squared__Expected = 'float_Ne2_Burrows_r_Squared__Expected'

        static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff = 'float_Ne2_Burrows_r_Squared_Diff'
        static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe = 'float_Ne2_Burrows_r_Sqrd_LDNe'

        static_Str_Colname_Ne2_floatLDNe_Harmonic_Mean = 'Ne2_floatLDNe_Harmonic_Mean'
                
        static_Str_Colname_Ne2_Inf_Count_floatLDNe = 'Ne2_Inf_Count_floatLDNe_Estimate'
        static_Str_Colname_Ne2_Inf_Count_floatLDNeParametric_Lwr_CI = 'Ne2_Inf_Count_floatLDNeParametric_Lwr_CI'
        static_Str_Colname_Ne2_Inf_Count_floatLDNeParametric_Upr_CI = 'Ne2_Inf_Count_floatLDNeParametric_Upr_CI'
        static_Str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Lwr_CI = 'Ne2_Inf_Count_floatLDNeJackknife_Lwr_CI'
        static_Str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Upr_CI = 'Ne2_Inf_Count_floatLDNeJackknife_Upr_CI'
        
        static_Str_Colname_float_Mean_Ne2_Burrows_r_Squared__Observed = 'float_Mean_Ne2_Burrows_r_Squared__Observed'
        static_Str_Colname_float_Mean_Ne2_Burrows_r_Squared__Expected = 'float_Mean_Ne2_Burrows_r_Squared__Expected'
        static_Str_Colname_float_Mean_Ne2_Burrows_r_Squared_Diff = 'float_Mean_Ne2_Burrows_r_Squared_Diff'
        static_Str_Colname_float_Total_Ne2_r_Sqrd_LDNe = 'float_Total_Ne2_r_Sqrd_LDNe'

        static_Str_Colname_float_Grand_Mean_Ne2_Burrows_r_Squared__Observed = 'float_Grand_Mean_Ne2_Burrows_r_Squared__Observed'
        static_Str_Colname_float_Grand_Mean_Ne2_Burrows_r_Squared__Expected = 'float_Grand_Mean_Ne2_Burrows_r_Squared__Expected'
        static_Str_Colname_float_Grand_Mean_Ne2_r_Sqrd_LDNe = 'float_Grand_Mean_Ne2_r_Sqrd_LDNe'

        static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc = 'float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc'
        static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_DemoNe = 'float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_DemoNe'
        static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents = 'float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents'

#         static_Str_Colname_float_Ratio_Grand_Mean_Ne2_r_Sqrd_LDNe_To_Nc = 'float_Ratio_Grand_Mean_Ne2_r_Sqrd_LDNe_To_Nc'
#         static_Str_Colname_float_Ratio_Grand_Mean_Ne2_r_Sqrd_LDNe_To_DemoNe = 'float_Ratio_Grand_Mean_Ne2_r_Sqrd_LDNe_To_DemoNe'
#         static_Str_Colname_float_Ratio_Grand_Mean_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents = 'float_Ratio_Grand_Mean_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents'
        
    class Embryo_Offspring_Parent_Ne_Stats(object):
    
        '''General'''
        static_Label_Gen_File = 'EPNS_'
        static_Logger_Label_Gen_Source_UID = 'Source_UID'
        static_Label_Gen_Source_UniqueID = static_Label_Gen_File + static_Logger_Label_Gen_Source_UID

    class Effective_Parents_Stats(object):
    
        '''General'''
        static_Label_Gen_File = 'EPS_'
        static_Logger_Label_Gen_Source_UID = 'Source_UID'
        static_Label_Gen_Source_UniqueID = static_Label_Gen_File + static_Logger_Label_Gen_Source_UID
  
    class SS_LEVEL_Replicate_Details(object):
    
        '''General'''
        static_Label_Gen_UniqueID = 'Unique_Run_ID'
        static_Label_Gen_Unique_Run_Batch_Rep_ID = 'Unique_Run_Batch_Rep_ID'
        
    class SS_LEVEL_VSP_Details(object):
    
        '''General'''
        static_Label_Gen_UniqueID = 'Unique_Run_ID'
        static_Label_Gen_Unique_Run_Batch_Rep_ID = 'Unique_Run_Batch_Rep_ID'
        static_Label_Gen_Unique_Run_Batch_Rep_VSP_ID = 'Unique_Run_Batch_Rep_VSP_ID'