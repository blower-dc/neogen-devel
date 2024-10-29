'''
Created on 29 Jan 2015

@author: dblowe
'''
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS
#
#------------------< Import python modules
# DEBUG Imports
# from logging import getLogger as logging__getLogger
# from handler_Debug import Timer2
# from handler_Debug import Debug_Location
#
from collections import OrderedDict
 
#------------------< Import DCB_General modules
# from FileHandler import FileHandler
# from handler_Logging import Logging
#------------------< Import SharkSim modules
#from globals_SharkSim import globalsSS
from object_SSConfigFiles import object_SSConfigFiles
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
class object_SSConfigSamplingStrategy(object_SSConfigFiles):

    '''
    --------------------------------------------------------------------------------------------------------
    # <<<<<<<<<<<<<<<<<< CLASS INIT
    --------------------------------------------------------------------------------------------------------
    '''   

    __slots__ = (
                #PROPERTIES
                #'obj_SSParams'                
                #VARIABLES
                #,'str_Project_Name'
                )

    static_str_Section__INI_File = 'INI_File'
    static_str_Option__INI_Filename = 'INI_Filename'
    static_str_Value__INI_Filename = 'SPECIES'
    static_str_Option__INI_Creation_Run_ID = 'INI_Creation_Run_ID'
    static_str_Option__INI_UID = 'INI_UID'

    static_str_Section__Scenario_Project_Details = 'Project_Details'
    static_str_Option__Scenario_Project_Name = 'Project_Name'
    static_str_Option__Scenario_Project_UID = 'Project_UID'
    static_str_Option__Scenario_Project_Species_Name = 'Project_Species_Name'
    
    static_str_Section__Scenario_Details = 'Scenario_Details'
    static_str_Option__Scenario_Name = 'Scenario_Name'
    static_str_Option__Scenario_UID = 'Scenario_UID'
    
    static_str_Section__Sampling_Strategy_Batch_Scenario = 'Batch_Scenario'
    static_str_Option__Sampling_Strategy_Scenario_File = 'Batch_Scenario_File'
    
    static_str_Section__Sampling_Strategy_Details = 'Sampling_Strategy_Details'
    static_str_Option__Sampling_Strategy_Name = 'Sampling_Strategy_Name'
    static_str_Option__Sampling_Strategy_UID = 'Sampling_Strategy_UID'

    static_str_Section__Sampling_Strategy_Run_Details = 'Sampling_Strategy_Run_Details'
    static_str_Option__Sampling_Strategy_Run_Ne_Estimator_External_Process_Version = 'Sampling_Strategy_Run_Ne_Estimator_External_Process_Version'
    static_str_Option__Sampling_Strategy_Run_Simulation_Working_Base_Path = 'Sampling_Strategy_Run_Simulation_Working_Base_Path'
    static_str_Option__Sampling_Strategy_Run_Simulation_Output_Base_Path = 'Sampling_Strategy_Run_Simulation_Output_Base_Path'
    static_str_Option__Sampling_Strategy_Run_LDNe_External_Process_Run_Time_Max_Seconds = 'Sampling_Strategy_Run_LDNe_External_Process_Run_Time_Max_Seconds'
    static_str_Option__Sampling_Strategy_Run_LDNe_External_Process_Repeat_FAILED_Max_Count = 'Sampling_Strategy_Run_LDNe_External_Process_Repeat_FAILED_Max_Count'
    static_str_Option__Sampling_Strategy_Run_LDNe_External_Process_Number_Of_Concurrent_Processes_Allowed = 'Sampling_Strategy_Run_LDNe_External_Process_Number_Of_Concurrent_Processes_Allowed'
    static_str_Option__Sampling_Strategy_Run_LDNe_External_Process_Zombie_Found_Serially_Count_Allowed = 'Sampling_Strategy_Run_LDNe_External_Process_Zombie_Found_Serially_Count_Allowed'
    static_str_Option__Sampling_Strategy_Run_LDNe_Accuracy_Line_Sampling_Plan_Dict__PLAN_CODE__REPS = 'Sampling_Strategy_Run_LDNe_Accuracy_Line_Sampling_Plan_Dict__PLAN_CODE__REPS'
    static_str_Option__Sampling_Strategy_Run_LDNe_Other_Sampling_Plans_CSV_Dict__PLAN_CODE__REPS = 'Sampling_Strategy_Run_LDNe_Other_Sampling_Plans_CSV_Dict__PLAN_CODE__REPS'
    static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_PSMP = 'PSMP'
    static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FAC = 'FAC'
    static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FEM = 'FEM'
    static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FJV = 'FJV'
    static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FMT = 'FMT'
    static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FUL = 'FUL'
    static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Name_PSMP = 'Scale_By_Max_Prop'
    static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Name_FAC = 'Full_Age_Cohorts'
    static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Name_FEM = 'Full_Embryo'
    static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Name_FJV = 'Full_Juvenile'
    static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Name_FMT = 'Full_Mature'
    static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Name_FUL = 'Full'

    
    static_str_Section__Sampling_Strategy_Last_Run_Details = 'Sampling_Strategy_Last_Run_Details'
    static_str_Option__Sampling_Strategy_Last_Run_UID = 'Last_Sampling_Strategy_Run_UID'
    static_str_Option__Sampling_Strategy_Last_Run_Job_Status = 'Last_Sampling_Strategy_Run_Job_Status'
    static_str_Option__Sampling_Strategy_Last_Run_Job_Status_Terminated_Reason = 'Last_Sampling_Strategy_Run_Job_Status_Terminated_Reason'
    static_str_Option__Sampling_Strategy_Last_Run_Shell_PID = 'Last_Sampling_Strategy_Run_Shell_PID'
    static_str_Option__Sampling_Strategy_Last_Run_Python_PID = 'Last_Sampling_Strategy_Run_Python_PID'
                
    static_str_Section__Sampling_Strategy_Sample_Details = 'Sample_Details'
    static_str_Option__Sampling_Strategy_Sample_Range_Min = 'Sample_Range_Min'
    static_str_Option__Sampling_Strategy_Sample_Range_Max = 'Sample_Range_Max'
    static_str_Option__Sampling_Strategy_Sample_Range_Increment = 'Sample_Range_Increment'
    
    static_str_Section__Sampling_Strategy_Locus_Details = 'Locus_Details'
    static_str_Option__Sampling_Strategy_Locus_Range_Min = 'Locus_Range_Min'
    static_str_Option__Sampling_Strategy_Locus_Range_Max = 'Locus_Range_Max'
    static_str_Option__Sampling_Strategy_Locus_Range_Increment = 'Locus_Range_Increment'

    static_str_Section__Sampling_Strategy_LDNe_Details = 'LDNe_Details'
    static_str_Option__Sampling_Strategy_LDNe_FULL_Estimates__Percentage_Of_Loci_To_Keep = 'LDNe_FULL_Estimates__Percentage_Of_Loci_To_Keep'
    static_str_Option__Sampling_Strategy_LDNe_Replicates = 'LDNe_Random_Sample_Replicates'
    static_str_Option__Sampling_Strategy_LDNe_PCrit_To_Get = 'LDNe_PCrit_To_Get'
    static_str_Value__Sampling_Strategy_LDNe_PCrit_To_Get__0_00 = '0.00'
    static_str_Value__Sampling_Strategy_LDNe_PCrit_To_Get__0_01 = '0.01'
    static_str_Value__Sampling_Strategy_LDNe_PCrit_To_Get__0_02 = '0.02'
    static_str_Value__Sampling_Strategy_LDNe_PCrit_To_Get__0_05 = '0.05'
    #static_str_Value__Sampling_Strategy_LDNe_PCrit_To_Get__NoS = '1'
    static_str_Value__Sampling_Strategy_LDNe_PCrit_To_Get__NoS = 'No_Singletons'
    
    
    static_str_Section__Sampling_Strategy_Sample_Proportion_Details = 'Sample_Proportion_Details'
    static_str_Option__Sampling_Strategy_Sample_Proportions_Source = 'Sample_Proportions_Source'
    static_str_Value__Sampling_Strategy_Sample_Proportions_Source__USER_PROPORTIONS = 'USER_PROPORTIONS' #Phase this out in favour of USER_SAMPLE_PROPORTIONS
    static_str_Value__Sampling_Strategy_Sample_Proportions_Source__USER_SAMPLE_NUMBERS = 'USER_SAMPLE_NUMBERS'
    static_str_Value__Sampling_Strategy_Sample_Proportions_Source__USER_SAMPLE_PROPORTIONS = 'USER_SAMPLE_PROPORTIONS'
    static_str_Value__Sampling_Strategy_Sample_Proportions_Source__USER_AGE_COHORTS = 'USER_AGE_COHORTS'
    
    static_str_Section__Sampling_Strategy_Sample_Proportions_By_Age__Age_And_Sample_Proportion = 'Sample_Proportions_By_Age'
    
    static_str_Section__Sampling_Strategy_Sample_Proportions_By_Age__Age_And_Sample_Number = 'Sample_Size_By_Number'
    
    static_str_Section__Sampling_Strategy_Sample_Proportions_By_Age__Total_Sample_Size_By_Age_Proportion = 'Total_Sample_Size_By_Age_Proportion'
    
    static_str_Section__Sampling_Strategy_Sample_Proportions_By_Age__Age_And_Cohort_Proportion = 'Sample_Cohorts_By_Age'
    

    def __enter__(self):
        
        return self 
    
    def __init__(self):

        return None         

    '''
    --------------------------------------------------------------------------------------------------------
    # <<<<<<<<<<<<<<<<<< CLASS FINALIZATION
    --------------------------------------------------------------------------------------------------------
    '''       
    def __exit__(self, type, value, traceback):
         
        pass
    