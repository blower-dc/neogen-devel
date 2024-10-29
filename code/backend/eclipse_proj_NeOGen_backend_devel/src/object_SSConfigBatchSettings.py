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
class object_SSConfigBatchSettings(object_SSConfigFiles):

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
    static_str_Value__INI_Filename = 'BATCH_SETTINGS'
    static_str_Option__INI_Creation_Run_ID = 'INI_Creation_Run_ID'
    static_str_Option__INI_UID = 'INI_UID'
    
    static_str_Section__Batch_Setting_Project_Details = 'Project_Details'
    static_str_Option__Batch_Setting_Details__Project_Name = 'Project_Name'
    static_str_Option__Batch_Setting_Details__Project_UID = 'Project_UID'
    static_str_Option__Batch_Setting_Details__Project_Species_Name = 'Project_Species_Name'
    
    static_str_Section__Batch_Setting_Details = 'Batch_Setting_Details'
    static_str_Option__Batch_Setting_Details__Scenario_Name = 'Scenario_Name'
    static_str_Option__Batch_Setting_Details__Scenario_UID = 'Scenario_UID'
#     static_str_Option__Batch_Setting_Details__Scenario_Code_Long = 'Scenario_Code_Long'
#     static_str_Option__Batch_Setting_Details__Scenario_Code_Short = 'Scenario_Code_Short'

    static_str_Section__Batch_Setting_Batch_Scenario = 'Batch_Scenario'
    static_str_Option__Batch_Setting_Scenario_File = 'Batch_Scenario_File'
        
    static_str_Section__Batch_Setting_Last_Batch_Scenario_Run_Details = 'Batch_Setting_Last_Batch_Scenario_Run_Details'
    static_str_Option__Batch_Setting_Last_Batch_Scenario_Run_UID = 'Last_Batch_Scenario_Run_UID'
    static_str_Option__Batch_Setting_Last_Batch_Scenario_Run_Job_Status = 'Last_Batch_Scenario_Run_Job_Status'
    static_str_Option__Batch_Setting_Last_Batch_Scenario_Run_Job_Status_Terminated_Reason = 'Last_Batch_Scenario_Run_Job_Status_Terminated_Reason'
    static_str_Option__Batch_Setting_Last_Batch_Scenario_Run_Shell_PID = 'Last_Batch_Scenario_Run_Shell_PID'
    static_str_Option__Batch_Setting_Last_Batch_Scenario_Run_Python_PID = 'Last_Batch_Scenario_Run_Python_PID'
        
    static_str_Section__Batch_Setting_Last_Sampling_Strategy_Run_Details = 'Batch_Setting_Last_Sampling_Strategy_Run_Details'
    static_str_Option__Batch_Setting_Last_Sampling_Strategy_Run_UID = 'Last_Sampling_Strategy_Run_UID'
    static_str_Option__Batch_Setting_Last_Sampling_Strategy_Run_Job_Status = 'Last_Sampling_Strategy_Run_Job_Status'
    static_str_Option__Batch_Setting_Last_Sampling_Strategy_Run_Job_Status_Terminated_Reason = 'Last_Sampling_Strategy_Run_Job_Status_Terminated_Reason'
    static_str_Option__Batch_Setting_Last_Sampling_Strategy_Run_Shell_PID = 'Last_Sampling_Strategy_Run_Shell_PID'
    static_str_Option__Batch_Setting_Last_Sampling_Strategy_Run_Python_PID = 'Last_Sampling_Strategy_Run_Python_PID'
            
    static_str_Section__Batch_Setting__Pop_Saving = 'Batch_Setting_Pop_Saving'
    static_str_Option__Batch_Setting__Pop_Saving__Replicate_Mating_Count_At_Which_Pop_Saving_Starts = 'Replicate_Mating_Count_At_Which_Pop_Saving_Starts'
    static_str_Option__Batch_Setting__Pop_Saving__Save_Pop_Every_Replicate_Mating_Count = 'Pop_Every_Replicate_Mating_Count'
    
    static_str_Section__Batch_Setting__Pop_Sampling = 'Batch_Setting_Pop_Sampling'
    static_str_Option__Batch_Setting__Pop_Sampling__Sample_Pop_Every_Mating_Count = 'Sample_Pop_Every_Mating_Count'
    static_str_Option__Batch_Setting__Pop_Sampling__Post_Sim_Pop_Sampling_Start_At_Replicate_Mating_Count = 'Post_Sim_Pop_Sampling_Start_At_Replicate_Mating_Count'

    static_str_Section__Batch_Setting__Genepop_Details = 'Batch_Setting_Genepop_Details'
    static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_PF_Files = 'Export_Genepop_PF_Files'
    static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_PF_Files_During_BurnIn = 'Export_Genepop_PF_Files_During_BurnIn'
    static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_PF_Embryo_VSP  = 'Export_Genepop_PF_Embryo_VSP'
    static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_SubSample_Percent_Of_PF_Embryo_VSP  = 'Export_Genepop_SubSample_Percent_Of_PF_Embryo_VSP'
    static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_PF_Mature_VSP  = 'Export_Genepop_PF_Mature_VSP'
    static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_SubSample_Percent_Of_PF_Mature_VSP  = 'Export_Genepop_SubSample_Percent_Of_PF_Mature_VSP'
    static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_PF_Full_VSP  = 'Export_Genepop_PF_Full_VSP'
    static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_SubSample_Percent_Of_PF_Full_VSP  = 'Export_Genepop_SubSample_Percent_Of_PF_Full_VSP'
    static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_PF_Files_Starts_At_Replicate_Mating_Count = 'Export_Genepop_PF_Files_Starts_At_Replicate_Mating_Count'
    static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_PF_Files_Every_Replicate_Mating_Count = 'Export_Genepop_PF_Files_Every_Replicate_Mating_Count'


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
    