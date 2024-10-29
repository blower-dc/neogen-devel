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
from object_SSConfigBatchScenario import object_SSConfigBatchScenario
from object_SSConfigSamplingStrategy import object_SSConfigSamplingStrategy
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
class object_SSConfigSettings(object_SSConfigBatchScenario, object_SSConfigSamplingStrategy):

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
    static_str_Value__INI_Filename = 'SETTINGS'
    static_str_Option__INI_Creation_Run_ID = 'INI_Creation_Run_ID'
    static_str_Option__INI_UID = 'INI_UID'
    #    
    #    
    static_str_Section__Settings_Details = 'Settings_Details'
    static_str_Option__Settings_Name = 'Settings_Name'
    #
    #
    static_str_Section__Settings_Run_Details = 'Settings_Run_Details'
    static_str_Option__Settings_Run_App_Version = 'Settings_Run_App_Version'
    static_str_Option__Settings_Run_App_Name = 'Settings_Run_App_Name'
    static_str_Option__Settings_Run_FrontEnd_DEBUG_Show_Settings_Menu = 'Settings_Run_FrontEnd_DEBUG_Show_Settings_Menu'
    static_str_Option__Settings_Run_FrontEnd_DEBUG_Logging = 'Settings_Run_FrontEnd_DEBUG_Logging'
    static_str_Option__Settings_Run_FrontEnd_FirstTime = 'Settings_Run_FrontEnd_FirstTime'
    static_str_Option__Settings_Run_FrontEnd_Job_Run_Monitor_Job_Status_Time_Delay_Secs = 'Settings_Run_FrontEnd_Job_Run_Monitor_Job_Status_Time_Delay_Secs'
    static_str_Option__Settings_Run_FrontEnd_Job_Run_Monitor_Job_Termination_Status_Time_Delay_Secs = 'Settings_Run_FrontEnd_Job_Run_Monitor_Job_Termination_Status_Time_Delay_Secs'
    
    static_str_Option__Settings_Run_Use_Relative_Paths = 'Settings_Use_Relative_Paths'
    
    static_str_Option__Settings_Run_Config_Folder = 'Settings_Run_Config_Folder'
    static_str_Option__Settings_Run_Docs_Folder = 'Settings_Run_Docs_Folder'
    static_str_Option__Settings_Run_Projects_Folder = 'Settings_Run_Projects_Folder'
    
    static_str_Option__Settings_Run_Project_Folder_Prefix = 'Settings_Run_Project_Folder_Prefix'
    static_str_Option__Settings_Run_Batch_Scenario_Folder_Prefix = 'Settings_Run_Batch_Scenario_Folder_Prefix'
    static_str_Option__Settings_Run_Sampling_Strategy_Folder_Prefix = 'Settings_Run_Sampling_Strategy_Folder_Prefix'
    
    static_str_Option__Settings_Run_Results_Folder_Prefix = 'Settings_Run_Results_Folder_Prefix'
    static_str_Option__Settings_Run_Results_Plots_Folder_Prefix = 'Settings_Run_Results_Plots_Folder_Prefix'
    static_str_Option__Settings_Run_Results_Thumbnail_Images_Folder_Prefix = 'Settings_Run_Results_Thumbnail_Images_Folder_Prefix'
    
    static_str_Option__Settings_Run_File_Extension_Config_File = 'Settings_Run_File_Extension_Config_File'
    static_str_Option__Settings_Run_File_Extension_Image_File = 'Settings_Run_File_Extension_Image_File'
    
    static_str_Option__Settings_Run_FrontEnd_Path = 'Settings_Run_FrontEnd_Path'
    static_str_Option__Settings_Run_BackEnd_Path = 'Settings_Run_BackEnd_Path'
    static_str_Option__Settings_Run_BackEnd_Relative_Path = 'Settings_Run_BackEnd_Relative_Path'
    static_str_Option__Settings_Run_BackEnd_Path_Max_Allowable_Length = 'Settings_Run_BackEnd_Path_Max_Allowable_Length' #Allow for a filename in this estimate
    static_str_Option__Settings_Run_BackEnd_Job_CPUs_To_Leave_In_Reserve = 'BackEnd_Job_CPUs_To_Leave_In_Reserve'
    static_str_Option__Settings_Run_BackEnd_ExecutableName = 'Settings_Run_BackEnd_ExecutableName'
    static_str_Option__Settings_Run_BackEnd_Working_Path = 'Settings_Run_BackEnd_Working_Path'
    static_str_Option__Settings_Run_BackEnd_Working_Relative_Path = 'Settings_Run_BackEnd_Working_Relative_Path'
    static_str_Option__Settings_Run_Python_Executable_Path = 'Settings_Run_Python_Executable_Path'
    static_str_Option__Settings_Run_Python_Executable_Name = 'Settings_Run_Python_Executable_Name'
    static_str_Option__Settings_Run_BackEnd_BINARY_Executable_Path = 'Settings_Run_BackEnd_BINARY_Executable_Path '
    static_str_Option__Settings_Run_BackEnd_BINARY_Executable_Relative_Path = 'Settings_Run_BackEnd_BINARY_Executable_Relative_Path '
    static_str_Option__Settings_Run_BackEnd_BINARY_Executable_Name = 'Settings_Run_BackEnd_BINARY_Executable_Name'
    static_str_Option__Settings_Run_BackEnd_BINARY_Executable = 'Settings_Run_BackEnd_BINARY_Executable'
    #
    #
    static_str_Section__Settings_Job_Details = 'Settings_Job_Details'
    static_str_Option__Settings_Job_Run_Scenario_Job__Time_Delay_In_Secs_Before_Monitoring = 'Run_Scenario_Job__Time_Delay_In_Secs_Before_Monitoring'
    #
    #
    static_str_Section__Population_Demographic_Settings = 'Population_Settings'
    static_str_Option__Population_Size__Default_Value = 'Population_Size__Default_Value'    
    static_str_Option__Population_Size__Max = 'Population_Size__Max'    
    static_str_Option__Population_Size__Min = 'Population_Size__Min'    
    #
    #
    static_str_Section__Simulation_Batch_Settings = 'Simulation_Batch_Settings'
    static_str_Option__Simulation_Batch_Replicates__Default_Value = 'Population_Replicates__Default_Value'
    static_str_Option__Simulation_Batch_Replicates__Max = 'Population_Replicates__Max'
    static_str_Option__Simulation_Batch_Replicates__Min = 'Population_Replicates__Min'
    static_str_Option__Simulation_Batch_Replicate_Length_Muliplier__Default_Value = 'Annual_Matings_Muliplier__Default_Value'
    static_str_Option__Simulation_Batch_Replicate_Length_Muliplier__Max = 'Annual_Matings_Muliplier__Max'
    static_str_Option__Simulation_Batch_Replicate_Length_Muliplier__Min = 'Annual_Matings_Muliplier__Min'
    static_str_Option__Simulation_Batch_Replicate_Length_Burn_In__Default_Value = 'Burn_In_Annual_Matings__Default_Value'
    static_str_Option__Simulation_Batch_Replicate_Length_Burn_In__Max = 'Burn_In_Annual_Matings__Max'
    static_str_Option__Simulation_Batch_Replicate_Length_Burn_In__Min = 'Burn_In_Annual_Matings__Min'
    static_str_Option__Simulation_Batch_Replicate_Length_Temporal_Evolution__Default_Value = 'Temporal_Evolution_Annual_Matings__Default_Value'
    static_str_Option__Simulation_Batch_Replicate_Length_Temporal_Evolution__Max = 'Temporal_Evolution_Annual_Matings__Max'
    static_str_Option__Simulation_Batch_Replicate_Length_Temporal_Evolution__Min = 'Temporal_Evolution_Annual_Matings__Min'
    #
    #
    static_str_Section__Genome_Settings = 'Genome_Settings'
    static_str_Option__Genome_Mutation_Allowed__Default_Value = 'Mutation_Allowed__Default_Value'
    static_str_Option__Genome_Mutation_Rate__Default_Value = 'Mutation_Rate__Default_Value'
    # 
    static_str_Section__Genome_Source_List = 'Genome_Source_List'
    #
    static_str_Section__Genome_Source_Settings = 'Genome_Source_Settings'
    static_str_Option__Genome_Source__Default_Value = 'Genome_Source__Default_Value'
    static_str_Option__Genome_Source_File__Default_Value = 'Genome_Source_File__Default_Value'
    #
    static_str_Section__Genome_Locus_Number_Settings = 'Genome_Locus_Number_Settings' 
    static_str_Option__Genome_Locus_Number__Default_Value = 'Genome_Locus_Number__Default_Value' 
    static_str_Option__Genome_Locus_Number__Max = 'Genome_Locus_Number__Max' 
    static_str_Option__Genome_Locus_Number__Min = 'Genome_Locus_Number__Min' 
    #
    static_str_Section__Genome_Alleles_Per_Locus_Distribution_List = 'Genome_Alleles_Per_Locus_Distribution_List' 
    #
    static_str_Section__Genome_Alleles_Per_Locus_Distribution_Settings = 'Genome_Alleles_Per_Locus_Distribution_Settings' 
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_UNIFORM_Number_Alleles_Per_Locus__Default_Value = 'Genome_Number_Alleles_Per_Locus__Default_Value'
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_UNIFORM_Number_Alleles_Per_Locus__Max = 'Genome_Number_Alleles_Per_Locus__Max'
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_UNIFORM_Number_Alleles_Per_Locus__Min = 'Genome_Number_Alleles_Per_Locus__Min'
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_BINOMIAL_Mean_Number_Alleles_Per_Locus__Default_Value = 'Genome_Mean_Number_Alleles_Per_Locus__Default_Value'
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_BINOMIAL_Mean_Number_Alleles_Per_Locus__Max = 'Genome_Mean_Number_Alleles_Per_Locus__Default_Value__Max'
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_BINOMIAL_Mean_Number_Alleles_Per_Locus__Min = 'Genome_Mean_Number_Alleles_Per_Locus__Default_Value__Min'
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_BINOMIAL_Mean_Number_Alleles_Per_Locus__Decimals = 'Genome_Mean_Number_Alleles_Per_Locus__Default_Value__Decimals'
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_BINOMIAL_Mean_Number_Alleles_Per_Locus__Step_Divisor = 'Genome_Mean_Number_Alleles_Per_Locus__Default_Value__Step_Divisor'
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_BINOMIAL_StdDev_Alleles_Per_Locus__Default_Value = 'Genome_Standard_Deviation_Alleles_Per_Locus__Default_Value'
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_BINOMIAL_StdDev_Alleles_Per_Locus__Max = 'Genome_Standard_Deviation_Alleles_Per_Locus__Default_Value__Max'
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_BINOMIAL_StdDev_Alleles_Per_Locus__Min = 'Genome_Standard_Deviation_Alleles_Per_Locus__Default_Value__Min'
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_BINOMIAL_StdDev_Alleles_Per_Locus__Decimals = 'Genome_Standard_Deviation_Alleles_Per_Locus__Default_Value__Decimals'
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_BINOMIAL_StdDev_Alleles_Per_Locus__Step_Divisor = 'Genome_Standard_Deviation_Alleles_Per_Locus__Default_Value__Step_Divisor'
    #
    static_str_Section__Genome_Allele_Frequency_Distribution_List = 'Genome_Allele_Frequency_Distribution_List' 
    #
    static_str_Section__Genome_Allele_Frequency_Distribution_Settings = 'Genome_Allele_Frequency_Distribution_Settings' 
    static_str_Option__Genome_Allele_Frequency_Distribution__Default_Value = 'Genome_Allele_Frequency_Distribution__Default_Value' 
    #
    #
    static_str_Section__Species_Life_History_Settings = 'Life_History_Settings'
    static_str_Option__Species_Life_History_Max_Age__Default_Value = 'Max_Age__Default_Value'
    static_str_Option__Species_Life_History_Max_Age__Max = 'Max_Age__Max'
    static_str_Option__Species_Life_History_Max_Age__Min = 'Max_Age__Min'
    static_str_Option__Species_Life_History_Max_Mating_Age__Default_Value = 'Max_mating_Age__Default_Value'
    static_str_Option__Species_Life_History_Max_Mating_Age__Max = 'Max_mating_Age__Max'
    static_str_Option__Species_Life_History_Max_Mating_Age__Min = 'Max_mating_Age__Min'
    static_str_Option__Species_Life_History_Min_Mating_Age__Default_Value = 'Min_Mating_Age__Default_Value'
    static_str_Option__Species_Life_History_Min_Mating_Age__Max = 'Min_Mating_Age__Max'
    static_str_Option__Species_Life_History_Min_Mating_Age__Min = 'Min_Mating_Age__Min'
    #
    #    
    static_str_Section__Settings_Species_Offspring_Distribution_List = 'Offspring_Distribution_List'
    #
    #
    static_str_Section__Species_Offspring_Distribution_Settings = 'Offspring_Distribution_Settings'
    #
    static_str_Option__Species_Offspring_Distribution_ABSOLUTE_Offspring_Number__Default_Value = 'Offspring_Distribution_ABSOLUTE__Number_Of_Offspring_Per_Mating__Default_Value'
    static_str_Option__Species_Offspring_Distribution_ABSOLUTE_Offspring_Number__Max = 'Offspring_Distribution_ABSOLUTE__Number_Of_Offspring_Per_Mating__Max'
    static_str_Option__Species_Offspring_Distribution_ABSOLUTE_Offspring_Number__Min = 'Offspring_Distribution_ABSOLUTE__Number_Of_Offspring_Per_Mating__Min'
    #
    static_str_Option__Species_Offspring_Distribution_POISSON_Offspring_Mean_Number__Default_Value = 'Offspring_Distribution_POISSON__Mean_Number_Of_Offspring_Per_Mating__Default_Value'
    static_str_Option__Species_Offspring_Distribution_POISSON_Offspring_Mean_Number__Max = 'Offspring_Distribution_POISSON__Mean_Number_Of_Offspring_Per_Mating__Max'
    static_str_Option__Species_Offspring_Distribution_POISSON_Offspring_Mean_Number__Min = 'Offspring_Distribution_POISSON__Mean_Number_Of_Offspring_Per_Mating__Min'
    static_str_Option__Species_Offspring_Distribution_POISSON_Offspring_Mean_Number__Decimals = 'Offspring_Distribution_POISSON__Mean_Number_Of_Offspring_Per_Mating__Decimals'
    static_str_Option__Species_Offspring_Distribution_POISSON_Offspring_Mean_Number__Step_Divisor = 'Offspring_Distribution_POISSON__Mean_Number_Of_Offspring_Per_Mating__Step_Divisor'
    #
    static_str_Option__Species_Offspring_Distribution_BINOMIAL_Offspring_Mean_Number__Default_Value = 'Offspring_Distribution_BINOMIAL__Mean_Number_Of_Offspring_Per_Mating__Default_Value'
    static_str_Option__Species_Offspring_Distribution_BINOMIAL_Offspring_Mean_Number__Max = 'Offspring_Distribution_BINOMIAL__Mean_Number_Of_Offspring_Per_Mating__Max'
    static_str_Option__Species_Offspring_Distribution_BINOMIAL_Offspring_Mean_Number__Min = 'Offspring_Distribution_BINOMIAL__Mean_Number_Of_Offspring_Per_Mating__Min'
    static_str_Option__Species_Offspring_Distribution_BINOMIAL_Offspring_Mean_Number__Decimals = 'Offspring_Distribution_BINOMIAL__Mean_Number_Of_Offspring_Per_Mating__Decimals'
    static_str_Option__Species_Offspring_Distribution_BINOMIAL_Offspring_Mean_Number__Step_Divisor = 'Offspring_Distribution_BINOMIAL__Mean_Number_Of_Offspring_Per_Mating__Step_Divisor'
    static_str_Option__Species_Offspring_Distribution_BINOMIAL_Offspring_StdDev__Default_Value = 'Offspring_Distribution_BINOMIAL__Standard_Deviation_Of_Offspring_Per_Mating__Default_Value'
    static_str_Option__Species_Offspring_Distribution_BINOMIAL_Offspring_StdDev__Max = 'Offspring_Distribution_BINOMIAL__Standard_Deviation_Of_Offspring_Per_Mating__Max'
    static_str_Option__Species_Offspring_Distribution_BINOMIAL_Offspring_StdDev__Min = 'Offspring_Distribution_BINOMIAL__Standard_Deviation_Of_Offspring_Per_Mating__Min'
    static_str_Option__Species_Offspring_Distribution_BINOMIAL_Offspring_StdDev__Decimals = 'Offspring_Distribution_BINOMIAL__Standard_Deviation_Of_Offspring_Per_Mating__Decimals'
    static_str_Option__Species_Offspring_Distribution_BINOMIAL_Offspring_StdDev__Step_Divisor = 'Offspring_Distribution_BINOMIAL__Standard_Deviation_Of_Offspring_Per_Mating__Step_Divisor'
    #
    static_str_Option__Species_Offspring_Distribution_UNIFORM_Offspring_Min__Default_Value = 'Offspring_Distribution_UNIFORM__Min_Number_Of_Offspring_Per_Mating__Default_Value'
    static_str_Option__Species_Offspring_Distribution_UNIFORM_Offspring_Min__Max = 'Offspring_Distribution_UNIFORM__Min_Number_Of_Offspring_Per_Mating__Max'
    static_str_Option__Species_Offspring_Distribution_UNIFORM_Offspring_Min__Min = 'Offspring_Distribution_UNIFORM__Min_Number_Of_Offspring_Per_Mating__Min'
    static_str_Option__Species_Offspring_Distribution_UNIFORM_Offspring_Max__Default_Value = 'Offspring_Distribution_UNIFORM__Max_Number_Of_Offspring_Per_Mating__Default_Value'
    static_str_Option__Species_Offspring_Distribution_UNIFORM_Offspring_Max__Max = 'Offspring_Distribution_UNIFORM__Max_Number_Of_Offspring_Per_Mating__Max'
    static_str_Option__Species_Offspring_Distribution_UNIFORM_Offspring_Max__Min = 'Offspring_Distribution_UNIFORM__Max_Number_Of_Offspring_Per_Mating__Min'
    #
    static_str_Option__Species_Offspring_Distribution_GEOMETRIC_Offspring_Mean__Default_Value = 'Offspring_Distribution_GEOMETRIC__Mean_Offspring_Per_Mating__Default_Value'
    static_str_Option__Species_Offspring_Distribution_GEOMETRIC_Offspring_Mean__Max = 'Offspring_Distribution_GEOMETRIC__Mean_Offspring_Per_Mating__Max'
    static_str_Option__Species_Offspring_Distribution_GEOMETRIC_Offspring_Mean__Min = 'Offspring_Distribution_GEOMETRIC__Mean_Offspring_Per_Mating__Min'
    static_str_Option__Species_Offspring_Distribution_GEOMETRIC_Offspring_Mean__Decimals = 'Offspring_Distribution_GEOMETRIC__Mean_Offspring_Per_Mating__Decimals'
    static_str_Option__Species_Offspring_Distribution_GEOMETRIC_Offspring_Mean__Step_Divisor = 'Offspring_Distribution_GEOMETRIC__Mean_Offspring_Per_Mating__Step_Divisor'
    #
    #
    #
    ''' STAMPLING STRATEGY SETTINGS '''
    #
    #
    static_str_Section__Sampling_Strategy_Run_Settings = 'Sampling_Strategy_Run_Settings'
    static_str_Option__Sampling_Strategy_Run_Settings_Ne_Estimator_External_Process_Version__Default_Value = 'Sampling_Strategy_Run_Settings_Ne_Estimator_External_Process_Version__Default_Value'
    static_str_Option__Sampling_Strategy_Run_Settings_LDNe_External_Process_Run_Time_Max_Seconds__Default_Value = 'Sampling_Strategy_Run_Settings_LDNe_External_Process_Run_Time_Max_Seconds__Default_Value'
    static_str_Option__Sampling_Strategy_Run_Settings_LDNe_External_Process_Repeat_FAILED_Max_Count__Default_Value = 'Sampling_Strategy_Run_Settings_LDNe_External_Process_Repeat_FAILED_Max_Count__Default_Value'
    static_str_Option__Sampling_Strategy_Run_Settings_LDNe_External_Process_Number_Of_Concurrent_Processes_Allowed__Default_Value = 'Sampling_Strategy_Run_Settings_LDNe_External_Process_Number_Of_Concurrent_Processes_Allowed__Default_Value'
    static_str_Option__Sampling_Strategy_Run_Settings_LDNe_External_Process_Zombie_Found_Serially_Count_Allowed__Default_Value = 'Sampling_Strategy_Run_Settings_LDNe_External_Process_Zombie_Found_Serially_Count_Allowed__Default_Value'
    static_str_Option__Sampling_Strategy_Run_Settings_LDNe_Accuracy_Line_Sampling_Plan_Dict__PLAN_CODE__REPS__Default_Value = 'Sampling_Strategy_Run_Settings_LDNe_Accuracy_Line_Sampling_Plan_Dict__PLAN_CODE__REPS__Default_Value'
    static_str_Option__Sampling_Strategy_Run_Settings_LDNe_Other_Sampling_Plans_CSV_Dict__PLAN_CODE__REPS__Default_Value = 'Sampling_Strategy_Run_Settings_LDNe_Other_Sampling_Plans_CSV_Dict__PLAN_CODE__REPS__Default_Value'
    #
    #
    static_str_Section__Sampling_Strategy_Sample_Settings = 'Sample_Stategy__Sample_Settings'
    static_str_Option__Sampling_Strategy_Sample_Range_Min__Default_Value = 'Sample_Range_Min__Default_Value'
    static_str_Option__Sampling_Strategy_Sample_Range_Min__Max = 'Sample_Range_Min__Max'
    static_str_Option__Sampling_Strategy_Sample_Range_Min__Min = 'Sample_Range_Min__Min'
    static_str_Option__Sampling_Strategy_Sample_Range_Max__Default_Value = 'Sample_Range_Max__Default_Value'
    static_str_Option__Sampling_Strategy_Sample_Range_Max__Max = 'Sample_Range_Max__Max'
    static_str_Option__Sampling_Strategy_Sample_Range_Max__Min = 'Sample_Range_Max__Min'
    static_str_Option__Sampling_Strategy_Sample_Range_Increment__Default_Value = 'Sample_Range_Increment__Default_Value'
    static_str_Option__Sampling_Strategy_Sample_Range_Increment__Max = 'Sample_Range_Increment__Max'
    static_str_Option__Sampling_Strategy_Sample_Range_Increment__Min = 'Sample_Range_Increment__Min'
    #
    #
    static_str_Section__Sampling_Strategy_Locus_Settings = 'Sample_Stategy__Locus_Settings'
    static_str_Option__Sampling_Strategy_Locus_Range_Min__Default_Value = 'Locus_Range_Min__Default_Value'
    static_str_Option__Sampling_Strategy_Locus_Range_Min__Max = 'Locus_Range_Min__Max'
    static_str_Option__Sampling_Strategy_Locus_Range_Min__Min = 'Locus_Range_Min__Min'
    static_str_Option__Sampling_Strategy_Locus_Range_Max__Default_Value = 'Locus_Range_Max__Default_Value'
    static_str_Option__Sampling_Strategy_Locus_Range_Max__Max = 'Locus_Range_Max__Max'
    static_str_Option__Sampling_Strategy_Locus_Range_Max__Min = 'Locus_Range_Max__Min'
    static_str_Option__Sampling_Strategy_Locus_Range_Increment__Default_Value = 'Locus_Range_Increment__Default_Value'
    static_str_Option__Sampling_Strategy_Locus_Range_Increment__Max = 'Locus_Range_Increment__Max'
    static_str_Option__Sampling_Strategy_Locus_Range_Increment__Min = 'Locus_Range_Increment__Min'
    #
    #
    static_str_Section__Sampling_Strategy_LDNe_Settings = 'LDNe_Settings'
    static_str_Option__Sampling_Strategy_LDNe_Replicates__Default_Value = 'LDNe_Random_Sample_Replicates__Default_Value'
    static_str_Option__Sampling_Strategy_LDNe_Replicates__Max = 'LDNe_Random_Sample_Replicates__Max'
    static_str_Option__Sampling_Strategy_LDNe_Replicates__Min = 'LDNe_Random_Sample_Replicates__Min'    
    static_str_Option__Sampling_Strategy_LDNe_FULL_Estimates__Percentage_Of_Loci_To_Keep = 'LDNe_FULL_Estimates__Percentage_Of_Loci_To_Keep' 
    #
    #    
    static_str_Section__Sampling_Strategy_LDNe_PCrit_To_Get_List = 'LDNe_PCrit_To_Get_List'
    #
    #
    static_str_Section__Sampling_Strategy_Sample_Proportions_Source_List = 'Sample_Proportions_Source_List'
    #
    #
    static_str_Section__Settings_Context_Help = 'Context_Help'
    static_str_Option__Settings_Context_Help_Display_At_Start = 'Context_Help_Display_At_Start'
    static_str_Option__Settings_Context_Help_Follow_Context = 'Context_Help_Follow_Context'
    static_str_Option__Settings_Context_Help_Zoom_Factor = 'Context_Help_Zoom_Factor'
    #
    static_str_Section__Settings_Context_Help_Files = 'Context_Help_Files'
    static_str_Option__Settings_Context_Help_File_Start_Splash_Screen = 'Context_Help_File_Start_Splash_Screen '
    #static_str_Option__Settings_Context_Help_File = 'Context_Help_File'
        
    
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
        