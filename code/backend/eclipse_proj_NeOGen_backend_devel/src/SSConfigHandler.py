'''
Created on 29 Jan 2015

@author: dblowe
'''
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS
#
#------------------< Import python modules
# DEBUG Imports
from logging import getLogger as logging__getLogger
from handler_Debug import Timer2
from handler_Debug import Debug_Location
#
import re
#
import os, fnmatch
from os import path as os__path
import csv
#
import pandas
#from openpyxl import load_workbook as openpyxl__load_workbook
from collections import OrderedDict
import numpy
#import openpyxl
from ConfigParser import ConfigParser

#------------------< Import DCB_General modules
from FileHandler import FileHandler
#from Bio.PopGen.GenePop.EasyController import EasyController as biopython__Easy_Controller
from handler_Logging import Logging
from ConfigHandler import ConfigOperation
#------------------< Import SharkSim modules
from SSParameterHandler import SSParameterHandler
from SSOutputHandler import SSOutputHandler
from globals_SharkSim import globalsSS
from SSAnalysisHandler import SSAnalysisHandler
from SSErrorHandler import SSErrorOperation
from object_SSConfigSettings import object_SSConfigSettings
from object_SSConfigProjects import object_SSConfigProjects
from object_SSConfigProject import object_SSConfigProject
from object_SSConfigScenarios import object_SSConfigScenarios
from object_SSConfigBatchScenario import object_SSConfigBatchScenario
from object_SSConfigBatchSettings import object_SSConfigBatchSettings
from object_SSConfigSamplingStrategy import object_SSConfigSamplingStrategy
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
class SSConfigOperation(object):

    '''
    --------------------------------------------------------------------------------------------------------
    # <<<<<<<<<<<<<<<<<< CLASS INIT
    --------------------------------------------------------------------------------------------------------
    '''   

    #str_Results_Base_Path = ''
    

    def __enter__(self):
        
        return self 
         
    def __init__(self, objSSParametersLocal=None):
        '''
        Constructor
        '''
 
        self.obj_SSParams = objSSParametersLocal
        
        self.str_Current_Col_Index = str(
                                     '0' +
                                     globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                     '0' +
                                     globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                     '0' +
                                     globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                     '0')
                
        ''' Get all the loggers required for monitoring this object '''
        self.method_Initialise_Monitor_Loggers()

        return None         
    
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

    def func_Parse__Project(self, config_parser):
        
        
        return True

    def func_Create_Config_File_PROJECTS(self, str_Config_File_Path_And_Name, list_Existing_Files):
         
        bool_Success = False
        
        obj_SSConfig = object_SSConfigProjects()
        obj_SSConfig.strUniqueRunID = self.obj_SSParams.strUniqueRunID
        obj_SSConfig.str_INI_UID_DateTime_Stamp = self.obj_SSParams.str_INI_UID_DateTime_Stamp
        obj_SSConfig.func_Initialise()
        
        '''
        --------------------------------
        Define Sections/Options/Values dict
        --------------------------------
        '''

        if len(list_Existing_Files) > 0:
            dict_Section_Key_Option_Value_Tuple = OrderedDict()
            
            ''' >>>>>>>>> Projects '''
            str_Section = obj_SSConfig.static_str_Section__Projects
            list_tup_Option_Value = []
    
            ''' Get UID from filename '''
            for str_Existing_Config_Path_And_File in list_Existing_Files:
                str_Path, str_Filename = os__path.split(str_Existing_Config_Path_And_File)
                
                str_Filename_UID = str.split(str_Filename.split('_')[2],'.')[0]
                
                str_Option = obj_SSConfig.static_str_Option__Projects_File  + '_' + str_Filename_UID
                value_Option = str_Existing_Config_Path_And_File
                list_tup_Option_Value.append((str_Option, value_Option))
            pass
        
            dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        else:
            dict_Section_Key_Option_Value_Tuple = OrderedDict()
            
            ''' >>>>>>>>> Projects '''
            str_Section = obj_SSConfig.static_str_Section__Projects
            list_tup_Option_Value = []
    
            str_Option = obj_SSConfig.static_str_Option__Projects_File  + '_' + self.obj_SSParams.str_INI_UID_DateTime_Stamp
            value_Option = self.obj_SSParams.str_PROJECT_Config_File_Path_And_Name
            list_tup_Option_Value.append((str_Option, value_Option))
            
            dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        pass
        
        '''
        ---------------------------------
        Create the config file from the dict values 
        ---------------------------------
        '''
        bool_Success = obj_SSConfig.func_Create_Config_File(str_Config_File_Path_And_Name, dict_Section_Key_Option_Value_Tuple)
     
        return bool_Success

    def func_Create_Config_File_PROJECT(self, str_Config_File_Path, list_Existing_Files):
         
        bool_Success = False
        
        obj_SSConfig = object_SSConfigProject()
        obj_SSConfig.strUniqueRunID = self.obj_SSParams.strUniqueRunID
        obj_SSConfig.str_INI_UID_DateTime_Stamp = self.obj_SSParams.str_INI_UID_DateTime_Stamp
        obj_SSConfig.func_Initialise()
        
        '''
        --------------------------------
        Define Sections/Options/Values dict
        --------------------------------
        '''
        if len(list_Existing_Files) > 0:
            dict_Section_Key_Option_Value_Tuple = OrderedDict()
            
            
            ''' >>>>>>>>> Projects '''
            str_Section = obj_SSConfig.static_str_Section__Projects
            list_tup_Option_Value = []
    
            ''' Get UID from filename '''
            for str_Existing_Config_Path_And_File in list_Existing_Files:
                str_Path, str_Filename = os__path.split(str_Existing_Config_Path_And_File)
                
                str_Filename_UID = str.split(str_Filename.split('_')[2],'.')[0]
                
                str_Option = obj_SSConfig.static_str_Option__Scenarios_File  + '_' + str_Filename_UID
                value_Option = str_Existing_Config_Path_And_File
                list_tup_Option_Value.append((str_Option, value_Option))
            pass
        
            dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        else:
    
            dict_Section_Key_Option_Value_Tuple = OrderedDict()
            
            ''' >>>>>>>>> Project Details '''
            str_Section = obj_SSConfig.static_str_Section__Project_Details
            list_tup_Option_Value = []
            
            str_Option = obj_SSConfig.static_str_Option__Project_Name 
            value_Option = 'PROJECT_V1'
            list_tup_Option_Value.append((str_Option, value_Option))
            
            str_Option = obj_SSConfig.static_str_Option__Project_UID 
            value_Option = self.obj_SSParams.str_INI_UID_DateTime_Stamp
            list_tup_Option_Value.append((str_Option, value_Option))
            
            dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
    
            ''' >>>>>>>>> Scenarios '''
            str_Section = obj_SSConfig.static_str_Section__Scenarios
            list_tup_Option_Value = []
                    
            str_Option = obj_SSConfig.static_str_Option__Scenarios_File + '_' + self.obj_SSParams.str_INI_UID_DateTime_Stamp
            value_Option = self.obj_SSParams.str_SCENARIOS_Config_File_Path_And_Name
            list_tup_Option_Value.append((str_Option, value_Option))
            
            dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        pass
        
        '''
        ---------------------------------
        Create the config file from the dict values 
        ---------------------------------
        '''
        str_Config_File_Path_And_Name = None
        bool_Success = obj_SSConfig.func_Create_Config_File(str_Config_File_Path_And_Name, dict_Section_Key_Option_Value_Tuple)
     
        return bool_Success

    def func_Create_Config_File_SCENARIOS(self, str_Config_File_Path_And_Name, list_Scenario_Files):
         
        bool_Success = False
        
        obj_SSConfig = object_SSConfigScenarios()
        obj_SSConfig.strUniqueRunID = self.obj_SSParams.strUniqueRunID
        obj_SSConfig.str_INI_UID_DateTime_Stamp = self.obj_SSParams.str_INI_UID_DateTime_Stamp
        obj_SSConfig.func_Initialise()
        
        '''
        --------------------------------
        Define Sections/Options/Values dict
        --------------------------------
        '''

        if len(list_Scenario_Files) > 0:
            dict_Section_Key_Option_Value_Tuple = OrderedDict()
            
            ''' >>>>>>>>> Projects '''
            str_Section = obj_SSConfig.static_str_Section__Scenarios_Batch_Scenarios
            list_tup_Option_Value = []
    
            ''' Get UID from filename '''
            for str_Scenario_Config_Path_And_File in list_Scenario_Files:
                str_Path, str_Filename = os__path.split(str_Scenario_Config_Path_And_File)
                
                str_Filename_UID = str.split(str_Filename.split('_')[2],'.')[0]
                
                str_Option = obj_SSConfig.static_str_Option__Scenarios_Batch_Scenario_File  + '_' + str_Filename_UID
                value_Option = str_Scenario_Config_Path_And_File
                list_tup_Option_Value.append((str_Option, value_Option))
            pass
        
            dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        else:
        
            dict_Section_Key_Option_Value_Tuple = OrderedDict()
            
            ''' >>>>>>>>> Batch Scenario '''
            str_Section = obj_SSConfig.static_str_Section__Scenarios_Batch_Scenarios
            list_tup_Option_Value = []
            
            str_Option = obj_SSConfig.static_str_Option__Scenarios_Batch_Scenario_File + '_' + self.obj_SSParams.str_INI_UID_DateTime_Stamp
            value_Option = self.obj_SSParams.str_BATCH_SCENARIO_Config_File_Path_And_Name
            list_tup_Option_Value.append((str_Option, value_Option))
            
            dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        pass
    
#         ''' >>>>>>>>> Batch Settings '''
#         str_Section = obj_SSConfig.static_str_Section__Scenarios_Batch_Settings
#         list_tup_Option_Value = []
# 
#         str_Option = obj_SSConfig.static_str_Option__Scenarios_Batch_Settings_File + '_' + self.obj_SSParams.str_INI_UID_DateTime_Stamp
#         value_Option = self.obj_SSParams.str_BATCH_SETTINGS_Config_File_Path_And_Name
#         list_tup_Option_Value.append((str_Option, value_Option))
#         
#         dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
#         
        
        '''
        ---------------------------------
        Create the config file from the dict values 
        ---------------------------------
        '''
        bool_Success = obj_SSConfig.func_Create_Config_File(str_Config_File_Path_And_Name, dict_Section_Key_Option_Value_Tuple)
     
        return bool_Success
   
    def func_Create_Config_File_BATCH_SETTINGS(self, str_Config_File_Path_And_Name):
         
        bool_Success = False
        
        obj_SSConfig = object_SSConfigBatchSettings()
        obj_SSConfig.strUniqueRunID = self.obj_SSParams.strUniqueRunID
        obj_SSConfig.str_INI_UID_DateTime_Stamp = self.obj_SSParams.str_INI_UID_DateTime_Stamp        
        obj_SSConfig.func_Initialise()
        
        '''
        --------------------------------
        Define Sections/Options/Values dict
        --------------------------------
        '''
        dict_Section_Key_Option_Value_Tuple = OrderedDict()
        
        ''' >>>>>>>>> Batch_Setting_Details '''
        str_Section = obj_SSConfig.static_str_Section__Batch_Setting_Details
        list_tup_Option_Value = []

        ''' >>>>>>>>> Scenario Details '''
        str_Option = obj_SSConfig.static_str_Option__Batch_Setting_Details__Scenario_Name
        value_Option = 'Scenario_V1'
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Batch_Setting_Details__Scenario_Code_Long
        value_Option = 'SCENARIO_V1'
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Batch_Setting_Details__Scenario_Code_Short
        value_Option = 'SC_V1'
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Batch Scenario '''
        str_Section = obj_SSConfig.static_str_Section__Batch_Setting_Batch_Scenario
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Batch_Setting_Scenario_File
        _, value_Option = os__path.split(self.obj_SSParams.str_BATCH_SCENARIO_Config_File_Path_And_Name)
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Batch_Setting_Pop_Saving '''
        str_Section = obj_SSConfig.static_str_Section__Batch_Setting__Pop_Saving
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Batch_Setting__Pop_Saving__Replicate_Mating_Count_At_Which_Pop_Saving_Starts
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Batch_Setting__Pop_Saving__Save_Pop_Every_Replicate_Mating_Count
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))

        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Batch_Setting_Pop_Saving '''
        str_Section = obj_SSConfig.static_str_Section__Batch_Setting__Pop_Sampling
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Batch_Setting__Pop_Sampling__Sample_Pop_Every_Mating_Count
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Batch_Setting__Pop_Sampling__Post_Sim_Pop_Sampling_Start_At_Replicate_Mating_Count
        value_Option = 103
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Batch_Setting_Genepop_Details '''
        str_Section = obj_SSConfig.static_str_Section__Batch_Setting__Genepop_Details
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_PF_Files
        value_Option = True
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_PF_Files_During_BurnIn
        value_Option = True
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_PF_Embryo_VSP
        value_Option = False
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_SubSample_Percent_Of_PF_Embryo_VSP
        value_Option = 0
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_PF_Mature_VSP
        value_Option = True
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_SubSample_Percent_Of_PF_Mature_VSP
        value_Option = 0.20
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_PF_Full_VSP
        value_Option = False
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_SubSample_Percent_Of_PF_Full_VSP
        value_Option = 0
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_PF_Files_Starts_At_Replicate_Mating_Count
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Batch_Setting__Genepop_Details__Export_Genepop_PF_Files_Every_Replicate_Mating_Count
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        
        '''
        ---------------------------------
        Create the config file from the dict values 
        ---------------------------------
        '''
        bool_Success = obj_SSConfig.func_Create_Config_File(str_Config_File_Path_And_Name, dict_Section_Key_Option_Value_Tuple)
     
        return bool_Success
    
    def func_Create_Config_File_BATCH_SCENARIO(self, str_Config_File_Path_And_Name):
         
        bool_Success = False
        
        obj_SSConfig = object_SSConfigBatchScenario()
        obj_SSConfig.strUniqueRunID = self.obj_SSParams.strUniqueRunID
        obj_SSConfig.str_INI_UID_DateTime_Stamp = self.obj_SSParams.str_INI_UID_DateTime_Stamp        
        obj_SSConfig.func_Initialise()
        
        '''
        --------------------------------
        Define Sections/Options/Values dict
        --------------------------------
        '''
        dict_Section_Key_Option_Value_Tuple = OrderedDict()
        
        ''' >>>>>>>>> Scenario_Details '''
        str_Section = obj_SSConfig.static_str_Section__Scenario_Details
        list_tup_Option_Value = []

        str_Option = obj_SSConfig.static_str_Option__Scenario_Name
        value_Option = 'Scenario_V1'
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Batch_Settings '''
        str_Section = obj_SSConfig.static_str_Section__Scenario_Batch_Settings
        list_tup_Option_Value = []

        str_Option = obj_SSConfig.static_str_Option__Scenario_Batch_Settings_File
        _, value_Option = os__path.split(self.obj_SSParams.str_BATCH_SETTINGS_Config_File_Path_And_Name)
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        
        ''' >>>>>>>>> Sampling_Strategy_Settings '''
        str_Section = obj_SSConfig.static_str_Section__Scenario_Sampling_Strategy_Settings
        list_tup_Option_Value = []

        str_Option = obj_SSConfig.static_str_Option__Scenario_Sampling_Strategy_Settings_File
        _, value_Option = os__path.split(self.obj_SSParams.str_SAMPLING_STRATEGY_Config_File_Path_And_Name)
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Simulation_Batch_Details '''
        str_Section = obj_SSConfig.static_str_Section__Simulation_Batch_Details
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Simulation_Batch_Replicates
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Simulation_Batch_Replicate_Length_Burn_In
        value_Option = 103
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Simulation_Batch_Replicate_Length_Temporal_Evolution
        value_Option = 9
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Population_Details '''
        str_Section = obj_SSConfig.static_str_Section__Population_Demographic_Details
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Population_Size
        value_Option = 1000
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Genome_Details '''
        str_Section = obj_SSConfig.static_str_Section__Genome_Details
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Genome_Mutation_Allowed
        value_Option = False
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Genome_Mutation_Rate
        value_Option = 5e-4
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Genome_Source
        value_Option = obj_SSConfig.static_str_Value__Genome_Source_INTERNAL
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Genome_Locus_Number
        value_Option = 100
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Genome_Alleles_Per_Locus_Distribution
        value_Option = obj_SSConfig.static_str_Value__Genome_Alleles_Per_Locus_Distribution_UNIFORM
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Genome_Alleles_Per_Locus_Distribution_UNIFORM_Number_Alleles_Per_Locus
        value_Option = 10
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Genome_Allele_Frequency_Distribution
        value_Option = obj_SSConfig.static_str_Value__Genome_Allele_Frequency_Distribution_DRICHLET
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Species_Details '''
        str_Section = obj_SSConfig.static_str_Section__Species_Details
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Species_Name
        value_Option = 'Stegostoma fasciatum'
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Code_Long
        value_Option = 'STFA_V1'
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Code_Short
        value_Option = 'ST'
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Life_History '''
        str_Section = obj_SSConfig.static_str_Section__Species_Life_History_Details
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Species_Life_History_Max_Age
        value_Option = 28
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Life_History_Max_Mating_Age
        value_Option = 28
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Life_History_Min_Mating_Age
        value_Option = 6
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Life_History_Allow_Senescence
        value_Option = bool_Allow_Senescence = False
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Mating_Details '''
        str_Section = obj_SSConfig.static_str_Section__Species_Mating_Details
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Species_Mating_Scheme
        value_Option = 21
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Mating_Scheme_Polygamy_Number_Of_Mates
        value_Option = 3
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Mating_Calendar_Month
        value_Option = 8
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        
        ''' >>>>>>>>> Parturition_Details '''
        str_Section = obj_SSConfig.static_str_Section__Species_Parturition_Details
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Species_Parturition_Calendar_Month
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Parturition_Gestation_Length_In_Months
        value_Option = 5
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Parturition_Reproductive_Rest_Length_In_Months
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        
        ''' >>>>>>>>> Offspring_Details '''
        str_Section = obj_SSConfig.static_str_Section__Species_Offspring_Details
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Species_Offspring_Sex_Scheme
        value_Option = 0
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Value__Species_Offspring_Sex_Scheme_PROBABILITY_OF_MALES
        value_Option = obj_SSConfig.static_str_Option__Species_Offspring_Sex_Scheme_PROBABILITY_OF_MALES_Prob_of_Males
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Offspring_Sex_Scheme_PROBABILITY_OF_MALES_Prob_of_Males
        value_Option = 0.5
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Offspring_Distribution
        value_Option = obj_SSConfig.static_str_Value__Species_Offspring_Distribution_BINOMIAL
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Species_Offspring_Distribution_BINOMIAL_Offspring_Mean_Number
        value_Option = 0
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Species_Offspring_Distribution_BINOMIAL_Offsping_StdDev
        value_Option = 0
        list_tup_Option_Value.append((str_Option, value_Option))
        
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        
        ''' >>>>>>>>> Natural_Survival_Details '''
        if bool_Allow_Senescence:
            dict_Survival_Natural_No_Senescence = OrderedDict([
                                                  (globalsSS.SexConstants.static_stringSexMale
                                                        ,OrderedDict([(12, 0.47),( 24, 0.88),( 36, 0.87),( 48, 0.92),( 60, 0.86),( 72, 0.90),( 84, 0.93),( 96, 0.89),( 108, 0.90),( 120, 0.90),( 132, 0.90),( 144, 0.90),( 156, 0.90),( 168, 0.90),( 180, 0.73),( 192, 0.90),( 204, 0.90),( 216, 0.90),( 228, 0.33),( 240, 0.90),( 252, 0.10),( 264, 0.10),( 276, 0.10),( 288, 0.10),( 300, 0.10),( 312, 0.10),( 324, 0.10),( 336, 0.10),( 348, 0.10)]))
                                                   ,(globalsSS.SexConstants.static_stringSexFemale
                                                        ,OrderedDict([(12, 0.41),( 24, 0.85),( 36, 0.88),( 48, 0.96),( 60, 0.93),( 72, 0.92),( 84, 0.90),( 96, 0.90),( 108, 0.90),( 120, 0.90),( 132, 0.90),( 144, 0.90),( 156, 0.94),( 168, 0.90),( 180, 0.90),( 192, 0.81),( 204, 0.90),( 216, 0.90),( 228, 0.90),( 240, 0.50),( 252, 0.90),( 264, 0.90),( 276, 0.90),( 288, 0.90),( 300, 0.90),( 312, 0.90),( 324, 0.90),( 336, 0.90),( 348, 0.90)]))])
        
        else:
            dict_Survival_Natural_No_Senescence = OrderedDict([
                                                  (globalsSS.SexConstants.static_stringSexMale
                                                        ,OrderedDict([(12, 0.47),( 24, 0.88),( 36, 0.87),( 48, 0.92),( 60, 0.86),( 72, 0.90),( 84, 0.93),( 96, 0.89),( 108, 0.90),( 120, 0.90),( 132, 0.90),( 144, 0.90),( 156, 0.90),( 168, 0.90),( 180, 0.73),( 192, 0.90),( 204, 0.90),( 216, 0.90),( 228, 0.33),( 240, 0.90),( 252, 0.10),( 264, 0.10),( 276, 0.10),( 288, 0.10),( 300, 0.10),( 312, 0.10),( 324, 0.10),( 336, 0.10),( 348, 0.10)]))
                                                   ,(globalsSS.SexConstants.static_stringSexFemale
                                                        ,OrderedDict([(12, 0.41),( 24, 0.85),( 36, 0.88),( 48, 0.96),( 60, 0.93),( 72, 0.92),( 84, 0.90),( 96, 0.90),( 108, 0.90),( 120, 0.90),( 132, 0.90),( 144, 0.90),( 156, 0.94),( 168, 0.90),( 180, 0.90),( 192, 0.81),( 204, 0.90),( 216, 0.90),( 228, 0.90),( 240, 0.50),( 252, 0.90),( 264, 0.90),( 276, 0.90),( 288, 0.90),( 300, 0.90),( 312, 0.90),( 324, 0.90),( 336, 0.90),( 348, 0.90)]))])
        pass

        ''' >>>>>>>>> Natural_Survival_Details__MALE '''
        str_Section = obj_SSConfig.static_str_Section__Species_Demographic_Natural_Survival_Details__MALE
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Species_Demographic_Natural_Survival_Mortality_Model_Annual_Mating_That_Mortality_Starts__MALE
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Demographic_Natural_Survival_Mortality_Model__MALE
        value_Option = 3
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Demographic_Natural_Survival_Mortality_Model_Scaling_Total__MALE
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        
        ''' >>>>>>>>> CSV_Age_And_Natural_Survival_Rate__MALE '''
        str_Section = obj_SSConfig.static_str_Section__Species_Demographic_Natural_Survival_CSV_Age_And_Survival_Rate__MALE
        list_tup_Option_Value = []
        
        for key_int_Age, value_float_Survival in dict_Survival_Natural_No_Senescence[globalsSS.SexConstants.static_stringSexMale].items(): 
            str_Option = key_int_Age
            value_Option = value_float_Survival
            list_tup_Option_Value.append((str_Option, value_Option))
        pass
    
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Natural_Survival_Details__FEMALE '''
        str_Section = obj_SSConfig.static_str_Section__Species_Demographic_Natural_Survival_Details__FEMALE
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Species_Demographic_Natural_Survival_Mortality_Model_Annual_Mating_That_Mortality_Starts__FEMALE
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Demographic_Natural_Survival_Mortality_Model__FEMALE
        value_Option = 3
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Demographic_Natural_Survival_Mortality_Model_Scaling_Total__FEMALE
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        
        ''' >>>>>>>>> CSV_Age_And_Natural_Survival_Rate__FEMALE '''
        str_Section = obj_SSConfig.static_str_Section__Species_Demographic_Natural_Survival_CSV_Age_And_Survival_Rate__FEMALE
        list_tup_Option_Value = []
        
        for key_int_Age, value_float_Survival in dict_Survival_Natural_No_Senescence[globalsSS.SexConstants.static_stringSexFemale].items(): 
            str_Option = key_int_Age
            value_Option = value_float_Survival
            list_tup_Option_Value.append((str_Option, value_Option))
        pass
    
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        
        ''' >>>>>>>>> UnNatural_Survival_Details '''
        dict_Survival_UnNatural_No_Senescence = OrderedDict([
                                              (globalsSS.SexConstants.static_stringSexMale
                                                    ,OrderedDict([(12, 0.47),( 24, 0.88),( 36, 0.87),( 48, 0.92),( 60, 0.86),( 72, 0.90),( 84, 0.93),( 96, 0.89),( 108, 0.90),( 120, 0.90),( 132, 0.90),( 144, 0.90),( 156, 0.90),( 168, 0.90),( 180, 0.73),( 192, 0.90),( 204, 0.90),( 216, 0.90),( 228, 0.33),( 240, 0.90),( 252, 0.10),( 264, 0.10),( 276, 0.10),( 288, 0.10),( 300, 0.10),( 312, 0.10),( 324, 0.10),( 336, 0.10),( 348, 0.10)]))
                                               ,(globalsSS.SexConstants.static_stringSexFemale
                                                    ,OrderedDict([(12, 0.41),( 24, 0.85),( 36, 0.88),( 48, 0.96),( 60, 0.93),( 72, 0.92),( 84, 0.90),( 96, 0.90),( 108, 0.90),( 120, 0.90),( 132, 0.90),( 144, 0.90),( 156, 0.94),( 168, 0.90),( 180, 0.90),( 192, 0.81),( 204, 0.90),( 216, 0.90),( 228, 0.90),( 240, 0.50),( 252, 0.90),( 264, 0.90),( 276, 0.90),( 288, 0.90),( 300, 0.90),( 312, 0.90),( 324, 0.90),( 336, 0.90),( 348, 0.90)]))])
        

        ''' >>>>>>>>> UnNatural_Survival_Details__BOTH '''
        str_Section = obj_SSConfig.static_str_Section__Species_Demographic_UnNatural_Survival_Details__BOTH
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Species_Demographic_UnNatural_Survival_Allowed__BOTH
        value_Option = False
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> UnNatural_Survival_Details__MALE '''
        str_Section = obj_SSConfig.static_str_Section__Species_Demographic_UnNatural_Survival_Details__MALE
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Species_Demographic_UnNatural_Survival_Mortality_Model_Annual_Mating_That_Mortality_Starts__MALE
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Demographic_UnNatural_Survival_Mortality_Model__MALE
        value_Option = 3
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Demographic_UnNatural_Survival_Mortality_Model_Scaling_Total__MALE
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        
        ''' >>>>>>>>> CSV_Age_And_UnNatural_Survival_Rate__MALE '''
        str_Section = obj_SSConfig.static_str_Section__Species_Demographic_UnNatural_Survival_CSV_Age_And_Survival_Rate__MALE
        list_tup_Option_Value = []
        
        for key_int_Age, value_float_Survival in dict_Survival_UnNatural_No_Senescence[globalsSS.SexConstants.static_stringSexMale].items(): 
            str_Option = key_int_Age
            value_Option = value_float_Survival
            list_tup_Option_Value.append((str_Option, value_Option))
        pass
    
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> UnNatural_Survival_Details__FEMALE '''
        str_Section = obj_SSConfig.static_str_Section__Species_Demographic_UnNatural_Survival_Details__FEMALE
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Species_Demographic_UnNatural_Survival_Mortality_Model_Annual_Mating_That_Mortality_Starts__FEMALE
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Demographic_UnNatural_Survival_Mortality_Model__FEMALE
        value_Option = 3
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Species_Demographic_UnNatural_Survival_Mortality_Model_Scaling_Total__FEMALE
        value_Option = 1
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        
        ''' >>>>>>>>> CSV_Age_And_UnNatural_Survival_Rate__FEMALE '''
        str_Section = obj_SSConfig.static_str_Section__Species_Demographic_UnNatural_Survival_CSV_Age_And_Survival_Rate__FEMALE
        list_tup_Option_Value = []
        
        for key_int_Age, value_float_Survival in dict_Survival_UnNatural_No_Senescence[globalsSS.SexConstants.static_stringSexFemale].items(): 
            str_Option = key_int_Age
            value_Option = value_float_Survival
            list_tup_Option_Value.append((str_Option, value_Option))
        pass
    
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        
        
        
        '''
        ---------------------------------
        Create the config file from the dict values 
        ---------------------------------
        '''
        bool_Success = obj_SSConfig.func_Create_Config_File(str_Config_File_Path_And_Name, dict_Section_Key_Option_Value_Tuple)
     
        return bool_Success
    
    def func_Create_Config_File_SAMPLING_STRATEGY(self, str_Config_File_Path_And_Name, dict_Section_Key_Option_Value_Tuple):
         
        bool_Success = False
        
        obj_SSConfig = object_SSConfigBatchScenario()
        obj_SSConfig.strUniqueRunID = self.obj_SSParams.strUniqueRunID
        obj_SSConfig.str_INI_UID_DateTime_Stamp = self.obj_SSParams.str_INI_UID_DateTime_Stamp        
        obj_SSConfig.func_Initialise()
        
#         '''
#         --------------------------------
#         Define Sections/Options/Values dict
#         --------------------------------
#         '''
#         dict_Section_Key_Option_Value_Tuple = OrderedDict()
#         
#         ''' >>>>>>>>> Scenario_Details '''
#         str_Section = obj_SSConfig.static_str_Section__Scenario_Details
#         list_tup_Option_Value = []
# 
#         str_Option = obj_SSConfig.static_str_Option__Scenario_Name
#         value_Option = 'Scenario_V1'
#         list_tup_Option_Value.append((str_Option, value_Option))
#         
#         dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        '''
        ---------------------------------
        Create the config file from the dict values 
        ---------------------------------
        '''
        bool_Success = obj_SSConfig.func_Create_Config_File(str_Config_File_Path_And_Name, dict_Section_Key_Option_Value_Tuple)
     
        return bool_Success
    
    def func_Create_FRESH_Config_File_BATCH_SCENARIO(self, strUniqueRunID, str_INI_UID_DateTime_Stamp, str_Config_File_Path_And_Name, dict_Section_Key_Option_Value_Tuple, obj_SSConfig):
         
        bool_Success = False
        
        ''' Check if path exists - If not create it '''
        with FileHandler() as obj_FileHandler:
            str_Config_File_Path, _ = os__path.split(str_Config_File_Path_And_Name)
            obj_FileHandler.method_Create_Path(str_Config_File_Path)
        pass        
        
        ''' Now create the config file '''
        obj_SSConfig.strUniqueRunID = strUniqueRunID
        obj_SSConfig.str_INI_UID_DateTime_Stamp = str_INI_UID_DateTime_Stamp        
        obj_SSConfig.func_Initialise()
        
        '''
        ---------------------------------
        Create the config file from the dict values 
        ---------------------------------
        '''
        bool_Success = obj_SSConfig.func_Create_Config_File(str_Config_File_Path_And_Name, dict_Section_Key_Option_Value_Tuple)
     
        return bool_Success
    
    def func_Create_FRESH_Config_File(self, strUniqueRunID, str_INI_UID_DateTime_Stamp, str_Config_File_Path_And_Name, dict_Section_Key_Option_Value_Tuple, obj_SSConfig):
         
        bool_Success = False
        
        ''' Check if path exists - If not create it '''
        with FileHandler() as obj_FileHandler:
            str_Config_File_Path, _ = os__path.split(str_Config_File_Path_And_Name)
            obj_FileHandler.method_Create_Path(str_Config_File_Path)
        pass        
        
        ''' Now create the config file '''
        obj_SSConfig.strUniqueRunID = strUniqueRunID
        obj_SSConfig.str_INI_UID_DateTime_Stamp = str_INI_UID_DateTime_Stamp        
        obj_SSConfig.func_Initialise()
        
        '''
        ---------------------------------
        Create the config file from the dict values 
        ---------------------------------
        '''
        bool_Success = obj_SSConfig.func_Create_Config_File(str_Config_File_Path_And_Name, dict_Section_Key_Option_Value_Tuple)
     
        return bool_Success
    
    def func_Create_Config_File_SAMPLING_STRATEGY__RAW(self, str_Config_File_Path_And_Name):
         
        bool_Success = False
        
        obj_SSConfig = object_SSConfigSamplingStrategy()
        obj_SSConfig.strUniqueRunID = self.obj_SSParams.strUniqueRunID
        obj_SSConfig.str_INI_UID_DateTime_Stamp = self.obj_SSParams.str_INI_UID_DateTime_Stamp        
        obj_SSConfig.func_Initialise()
        
        '''
        --------------------------------
        Define Sections/Options/Values dict
        --------------------------------
        '''
        dict_Section_Key_Option_Value_Tuple = OrderedDict()
        
        ''' >>>>>>>>> Sampling_Strategy_Details '''
        str_Section = obj_SSConfig.static_str_Section__Sampling_Strategy_Details
        list_tup_Option_Value = []

        str_Option = obj_SSConfig.static_str_Option__Sampling_Strategy_Name        
        value_Option = 'SAMPLING_STRAT_V1'
        list_tup_Option_Value.append((str_Option, value_Option))

        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        
        ''' >>>>>>>>> Sampling_Strategy_Details '''
        str_Section = obj_SSConfig.static_str_Section__Sampling_Strategy_Sample_Details
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Sampling_Strategy_Sample_Range_Min
        value_Option = 90
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Sampling_Strategy_Sample_Range_Max
        value_Option = 150
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Sampling_Strategy_Sample_Range_Increment
        value_Option = 20
        list_tup_Option_Value.append((str_Option, value_Option))

        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Sampling_Strategy_Details '''
        str_Section = obj_SSConfig.static_str_Section__Sampling_Strategy_Locus_Details
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Sampling_Strategy_Locus_Range_Min
        value_Option = 10
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Sampling_Strategy_Locus_Range_Max
        value_Option = 20
        list_tup_Option_Value.append((str_Option, value_Option))
        
        str_Option = obj_SSConfig.static_str_Option__Sampling_Strategy_Locus_Range_Increment
        value_Option = 5
        list_tup_Option_Value.append((str_Option, value_Option))

        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Sampling_Strategy_Details '''
        str_Section = obj_SSConfig.static_str_Section__Sampling_Strategy_LDNe_Details
        list_tup_Option_Value = []

        str_Option = obj_SSConfig.static_str_Option__Sampling_Strategy_LDNe_Replicates
        value_Option = 5
        list_tup_Option_Value.append((str_Option, value_Option))

        str_Option = obj_SSConfig.static_str_Option__Sampling_Strategy_LDNe_PCrit_To_Get
        value_Option = 0.01
        list_tup_Option_Value.append((str_Option, value_Option))

        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value

        ''' >>>>>>>>> Sample_Proportion_Details '''
        str_Section = obj_SSConfig.static_str_Section__Sampling_Strategy_Sample_Proportion_Details
        list_tup_Option_Value = []
        
        str_Option = obj_SSConfig.static_str_Option__Sampling_Strategy_Sample_Proportions_Source
        value_Option = str_Sampling_Strategy_Sample_Proportions_Source = obj_SSConfig.static_str_Value__Sampling_Strategy_Sample_Proportions_Source__USER_AGE_COHORTS
        list_tup_Option_Value.append((str_Option, value_Option))
        
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        
        ''' >>>>>>>>> Sampling_Strategy_Details '''
        if str_Sampling_Strategy_Sample_Proportions_Source == obj_SSConfig.static_str_Value__Sampling_Strategy_Sample_Proportions_Source__USER_PROPORTIONS:
            dict_Sampling_Strategy_1_0__Age_Cohort_Sample_Proportions_Of_Total_Sample = OrderedDict([(12,0.00),(24,0.00),(36,0.00),(48,0.00),(60,0.00),(72,0.045455),(84,0.045455),(96,0.045455),(108,0.045455),(120,0.045455),(132,0.045455),(144,0.045455),(156,0.045455),(168,0.045455),(180,0.045455),(192,0.045455),(204,0.045455),(216,0.045455),(228,0.045455),(240,0.045455),(252,0.045455),(264,0.045455),(276,0.045455),(288,0.045455),(300,0.045455),(312,0.045455),(324,0.045455),(336,0.00)])
            str_Section = obj_SSConfig.static_str_Section__Sampling_Strategy_Sample_Proportions_By_Age
        else:
            dict_Sampling_Strategy_1_0__Age_Cohort_Sample_Proportions_Of_Total_Sample = OrderedDict([(12,0.00),(24,0.00),(36,0.00),(48,0.00),(60,0.00),(72,1.0),(84,1.0),(96,1.0),(108,1.0),(120,1.0),(132,1.0),(144,1.0),(156,1.0),(168,1.0),(180,1.0),(192,1.0),(204,1.0),(216,1.0),(228,1.0),(240,1.0),(252,1.0),(264,1.0),(276,1.0),(288,1.0),(300,1.0),(312,1.0),(324,1.0),(336,0.00)])
            str_Section = obj_SSConfig.static_str_Section__Sampling_Strategy_Sample_Cohorts_By_Age
        pass
        
        list_tup_Option_Value = []
        
        for key_int_Age, value_float_Survival in dict_Sampling_Strategy_1_0__Age_Cohort_Sample_Proportions_Of_Total_Sample.items(): 
            str_Option = key_int_Age
            value_Option = value_float_Survival
            list_tup_Option_Value.append((str_Option, value_Option))
        pass
    
        dict_Section_Key_Option_Value_Tuple[str_Section] = list_tup_Option_Value
        
        
        '''
        ---------------------------------
        Create the config file from the dict values 
        ---------------------------------
        '''
        bool_Success = obj_SSConfig.func_Create_Config_File(str_Config_File_Path_And_Name, dict_Section_Key_Option_Value_Tuple)
     
        return bool_Success

    def func_Read_Config_File_SETTINGS(self, str_Config_File_Path_And_Name):
 
        bool_Success = False
          
        obj_SSConfig = object_SSConfigSettings()
        #obj_SSConfig.strUniqueRunID = self.obj_SSParams.strUniqueRunID
        #obj_SSConfig.str_INI_UID_DateTime_Stamp = self.obj_SSParams.str_INI_UID_DateTime_Stamp        
        obj_SSConfig.func_Initialise()
         
        config_parser_Config = obj_SSConfig.func_Read_Config_File(str_Config_File_Path_And_Name)
        if config_parser_Config != None:
            bool_Success = True
        pass        
      
        return obj_SSConfig
    
    def func_Read_Config_File_PROJECTS(self, str_Config_File_Path_And_Name):
 
        bool_Success = False
          
        obj_SSConfig = object_SSConfigProjects()
        #obj_SSConfig.strUniqueRunID = self.obj_SSParams.strUniqueRunID
        #obj_SSConfig.str_INI_UID_DateTime_Stamp = self.obj_SSParams.str_INI_UID_DateTime_Stamp
        obj_SSConfig.func_Initialise()
         
        config_parser_Config = obj_SSConfig.func_Read_Config_File(str_Config_File_Path_And_Name)
        if config_parser_Config != None:
            bool_Success = True
        pass        
      
        return obj_SSConfig
     
    def func_Read_Config_File_PROJECT(self, str_Config_File_Path_And_Name):
 
        bool_Success = False
          
        obj_SSConfig = object_SSConfigProject()
        #obj_SSConfig.strUniqueRunID = self.obj_SSParams.strUniqueRunID
        #obj_SSConfig.str_INI_UID_DateTime_Stamp = self.obj_SSParams.str_INI_UID_DateTime_Stamp        
        obj_SSConfig.func_Initialise()
         
        config_parser_Config = obj_SSConfig.func_Read_Config_File(str_Config_File_Path_And_Name)
        if config_parser_Config != None:
            bool_Success = True
        pass        
      
        return obj_SSConfig
     
    def func_Read_Config_File_BATCH_SCENARIO(self, str_Config_File_Path_And_Name):
 
        bool_Success = False
          
        obj_SSConfig = object_SSConfigBatchScenario()
        #obj_SSConfig.strUniqueRunID = self.obj_SSParams.strUniqueRunID
        #obj_SSConfig.str_INI_UID_DateTime_Stamp = self.obj_SSParams.str_INI_UID_DateTime_Stamp        
        obj_SSConfig.func_Initialise()
         
        config_parser_Config = obj_SSConfig.func_Read_Config_File(str_Config_File_Path_And_Name)
        if config_parser_Config != None:
            bool_Success = True
        pass        
      
        return obj_SSConfig
     
    def func_Read_Config_File_BATCH_SETTINGS(self, str_Config_File_Path_And_Name):
 
        bool_Success = False
          
        obj_SSConfig = object_SSConfigBatchSettings()
        #obj_SSConfig.strUniqueRunID = self.obj_SSParams.strUniqueRunID
        #obj_SSConfig.str_INI_UID_DateTime_Stamp = self.obj_SSParams.str_INI_UID_DateTime_Stamp        
        obj_SSConfig.func_Initialise()
         
        config_parser_Config = obj_SSConfig.func_Read_Config_File(str_Config_File_Path_And_Name)
        if config_parser_Config != None:
            bool_Success = True
        pass        
      
        return obj_SSConfig
     
    def func_Read_Config_File_SAMPLING_STRATEGY(self, str_Config_File_Path_And_Name):
 
        bool_Success = False
          
        obj_SSConfig = object_SSConfigSamplingStrategy()
        #obj_SSConfig.strUniqueRunID = self.obj_SSParams.strUniqueRunID
        #obj_SSConfig.str_INI_UID_DateTime_Stamp = self.obj_SSParams.str_INI_UID_DateTime_Stamp        
        obj_SSConfig.func_Initialise()
         
        config_parser_Config = obj_SSConfig.func_Read_Config_File(str_Config_File_Path_And_Name)
        if config_parser_Config != None:
            bool_Success = True
        pass        
      
        return obj_SSConfig
     
    def func_Read_Any_Config_File(self, str_Config_File_Path_And_Name, obj_Config):
 
        bool_Success = False
          
        obj_Config.func_Initialise()
         
        config_parser_Config = obj_Config.func_Read_Config_File(str_Config_File_Path_And_Name)
        if config_parser_Config != None:
            bool_Success = True
        pass        
      
        return obj_Config
     
     
    def func_Read_Config_File_SCENARIOS(self, str_Config_File_Path_And_Name):

        bool_Success = False
          
        obj_SSConfig = object_SSConfigScenarios()
        #obj_SSConfig.strUniqueRunID = self.obj_SSParams.strUniqueRunID
        #obj_SSConfig.str_INI_UID_DateTime_Stamp = self.obj_SSParams.str_INI_UID_DateTime_Stamp        
        obj_SSConfig.func_Initialise()
         
        config_parser_Config = obj_SSConfig.func_Read_Config_File(str_Config_File_Path_And_Name)
        if config_parser_Config != None:
            bool_Success = True
        pass        
      
        return obj_SSConfig

    def func_Verify_And_Read_Config_File__BATCH_SCENARIO(self, str_Config_File_Path_And_Name):

        obj_Config = None
        
        with FileHandler() as obj_FileHandler:
            if obj_FileHandler.fileExists(str_Config_File_Path_And_Name):
                obj_Config = self.func_Read_Config_File_BATCH_SCENARIO(str_Config_File_Path_And_Name)
                if obj_Config.config_parser_Config == None:
                    with SSErrorOperation([]) as obj_SSErrorOp:
                        str_Message_Text = 'Config file obj_Config.config_parser_Config = None' + '; Config file: ' + str_Config_File_Path_And_Name
                        int_Stack_Trace_Level = 2
                        obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))
                    pass
                pass
            else:
                with SSErrorOperation([]) as obj_SSErrorOp:
                    str_Message_Text = 'Non-existant config file: ' + str_Config_File_Path_And_Name
                    int_Stack_Trace_Level = 2
                    obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))
                pass
            pass
        pass
        return obj_Config

    def func_Verify_And_Read_Config_File__BATCH_SETTINGS(self, str_Config_File_Path_And_Name):

        obj_Config = None
               
        with FileHandler() as obj_FileHandler:
            if obj_FileHandler.fileExists(str_Config_File_Path_And_Name):
                obj_Config = self.func_Read_Config_File_BATCH_SETTINGS(str_Config_File_Path_And_Name)
                if obj_Config.config_parser_Config != None:
                    self.obj_Config_Batch_Settings = obj_Config
                else:
                    with SSErrorOperation([]) as obj_SSErrorOp:
                        str_Message_Text = 'obj_Config.config_parser_Config = None' + '; Config file: ' + str_Config_File_Path_And_Name
                        int_Stack_Trace_Level = 2
                        obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))
                    pass
                pass
            else:
                with SSErrorOperation([]) as obj_SSErrorOp:
                    str_Message_Text = 'Non-existant config file: ' + str_Config_File_Path_And_Name
                    int_Stack_Trace_Level = 2
                    obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))
                pass
            pass
        pass
        return obj_Config    

    def func_Verify_And_Read_Config_File__SAMPLING_STRATEGY(self, str_Config_File_Path_And_Name):

        obj_Config = None
               
        with FileHandler() as obj_FileHandler:
            if obj_FileHandler.fileExists(str_Config_File_Path_And_Name):
                obj_Config = self.func_Read_Config_File_SAMPLING_STRATEGY(str_Config_File_Path_And_Name)
                if obj_Config.config_parser_Config != None:
                    self.obj_Config_Batch_Settings = obj_Config
                else:
                    with SSErrorOperation([]) as obj_SSErrorOp:
                        str_Message_Text = 'obj_Config.config_parser_Config = None' + '; Config file: ' + str_Config_File_Path_And_Name
                        int_Stack_Trace_Level = 2
                        obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))
                    pass
                pass
            else:
                with SSErrorOperation([]) as obj_SSErrorOp:
                    str_Message_Text = 'Non-existant config file: ' + str_Config_File_Path_And_Name
                    int_Stack_Trace_Level = 2
                    obj_SSErrorOp.func_Error_Handler__Caught_Exceptions(int_Stack_Trace_Level, str_Message_Text, tup_Args = (self.obj_SSParams.str_App_Arg_Output_Base_Path, self.obj_SSParams.strUniqueRunID))
                pass
            pass
        pass
        return obj_Config     
    '''
    --------------------------------------------------------------------------------------------------------
    # Utility Processing
    --------------------------------------------------------------------------------------------------------
    '''

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
    
    
    
    
    