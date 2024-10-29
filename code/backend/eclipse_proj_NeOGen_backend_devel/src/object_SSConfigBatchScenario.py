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
class object_SSConfigBatchScenario(object_SSConfigFiles):

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
    static_str_Value__INI_Filename = 'BATCH_SCENARIO'
    static_str_Option__INI_Creation_Run_ID = 'INI_Creation_Run_ID'
    static_str_Option__INI_UID = 'INI_UID'
                    
    static_str_Section__Scenario_Project_Details = 'Project_Details'
    static_str_Option__Scenario_Project_Name = 'Project_Name'
    static_str_Option__Scenario_Project_UID = 'Project_UID'
    static_str_Option__Scenario_Project_Species_Name = 'Project_Species_Name'
    
    static_str_Section__Scenario_Details = 'Scenario_Details'
    static_str_Option__Scenario_Name = 'Scenario_Name'
    static_str_Option__Scenario_UID = 'Scenario_UID'

    #static_str_Option__Scenario_Code_Long = 'Scenario_Code_Long'
    #static_str_Option__Scenario_Code_Short = 'Scenario_Code_Short'

    static_str_Section__Scenario_Batch_Settings = 'Batch_Settings'
    static_str_Option__Scenario_Batch_Settings_File = 'Batch_Settings_File'

    static_str_Section__Scenario_Run_Details = 'Scenario_Run_Details'
    static_str_Option__Scenario_Run_Simulation_Working_Base_Path = 'Scenario_Run_Simulation_Working_Base_Path'
    static_str_Option__Scenario_Run_Simulation_Output_Base_Path = 'Scenario_Run_Simulation_Output_Base_Path'

    static_str_Section__Scenario_Sampling_Strategy_File_List = 'Scenario_Sampling_Strategy_File_List'
    static_str_Option__Scenario_Sampling_Strategy_File = 'Sampling_Strategy_File'

    static_str_Section__Scenario_Sampling_Strategy_Name_List = 'Scenario_Sampling_Strategy_Name_List'
    static_str_Option__Scenario_Sampling_Strategy_Name = 'Sampling_Strategy_Name'
        
    static_str_Section__Simulation_Batch_Details = 'Simulation_Batch_Details'
    static_str_Option__Simulation_Batch_Replicates = 'Population_Replicates'
    static_str_Option__Simulation_Batch_Replicate_Length_Burn_In = 'Burn_In_Annual_Matings'
    static_str_Option__Simulation_Batch_Replicate_Length_Temporal_Evolution = 'Temporal_Evolution_Annual_Matings'
    
    static_str_Section__Population_Demographic_Details = 'Population_Details'
    static_str_Option__Population_Size = 'Population_Size'

    static_str_Section__Genome_Details = 'Genome_Details'
    #static_str_Option__Genome_Mutation_Allowed = 'Mutation_Allowed'
    static_str_Option__Genome_Mutation_Rate = 'Mutation_Rate' 
    static_str_Option__Genome_Source = 'Genome_Source'
    static_str_Value__Genome_Source_ALL_ALLELE_FREQUENCIES = 'ALL_ALLELE_FREQUENCIES'
    static_str_Value__Genome_Source_INTERNAL = 'INTERNAL'
    static_str_Option__Genome__Source_ALL_ALLELE_FREQUENCIES_File_Path_And_Name = 'AllAlleleFrequencies_File_Path_And_Name'
    static_str_Option__Genome__Source_GENEPOP_File_Path_And_Name = 'Genepop_File_Path_And_Name'
    static_str_Option__Genome_Locus_Number = 'Locus_Number' 
    static_str_Option__Genome_Alleles_Per_Locus_Distribution = 'Alleles_Per_Locus_Distribution' 
    static_str_Value__Genome_Alleles_Per_Locus_Distribution_UNIFORM = 'UNIFORM' 
    static_str_Value__Genome_Alleles_Per_Locus_Distribution_BINOMIAL = 'BINOMIAL' 
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_UNIFORM_Number_Alleles_Per_Locus = 'Number_Alleles_Per_Locus'
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_BINOMIAL_Mean_Number_Alleles_Per_Locus = 'Mean_Number_Alleles_Per_Locus'
    static_str_Option__Genome_Alleles_Per_Locus_Distribution_BINOMIAL_StdDev_Alleles_Per_Locus = 'Standard_Deviation_Alleles_Per_Locus'
    static_str_Option__Genome_Allele_Frequency_Distribution = 'Allele_Frequency_Distribution' 
    static_str_Value__Genome_Allele_Frequency_Distribution_UNIFORM = 'UNIFORM' #Phase this out in favour of NON_RANDOM
    static_str_Value__Genome_Allele_Frequency_Distribution_NON_RANDOM = 'NON_RANDOM' 
    static_str_Value__Genome_Allele_Frequency_Distribution_DRICHLET = 'DRICHLET' 
    static_str_Value__Genome_Allele_Frequency_Distribution_ALL_ALLELE_FREQUENCIES = 'ALL_ALLELE_FREQUENCIES_FILE'
    static_str_Value__Genome_Allele_Frequency_Distribution_GENEPOP = 'GENEPOP_FILE'
    
    static_str_Section__Species_Details = 'Species_Details'
    static_str_Option__Species_Name = 'Species_Name'
    static_str_Option__Species_Code_Long = 'Species_Code_Long'
    static_str_Option__Species_Code_Short = 'Species_Code_Short'


    static_str_Section__Species_Life_History_Details = 'Life_History'
    static_str_Option__Species_Life_History_Max_Age = 'Max_Age'
    static_str_Option__Species_Life_History_Max_Mating_Age = 'Max_mating_Age'
    static_str_Option__Species_Life_History_Min_Mating_Age = 'Min_Mating_Age'
    static_str_Option__Species_Life_History_Allow_Senescence = 'Allow_Senescence'


    static_str_Section__Species_Mating_Details = 'Mating_Details'
    static_str_Option__Species_Mating_Scheme = 'Mating_Scheme'
    static_str_Option__Species_Mating_Scheme_Polygamy_Number_Of_Mates = 'Mating_Scheme_Polygamy_Number_Of_Mates'
    static_str_Option__Species_Mating_Calendar_Month = 'Mating_Calendar_Month'


    static_str_Section__Species_Parturition_Details = 'Parturition_Details'
    static_str_Option__Species_Parturition_Calendar_Month = 'Parturition_Calendar_Month'
    static_str_Option__Species_Parturition_Gestation_Length_In_Months = 'Gestation_Length_In_Months'
    static_str_Option__Species_Parturition_Reproductive_Rest_Length_In_Months = 'Reproductive_Rest_Length_In_Months'


    static_str_Section__Species_Offspring_Details = 'Offspring_Details'
    static_str_Option__Species_Offspring_Sex_Scheme = 'Offspring_Sex_Scheme'
    static_str_Value__Species_Offspring_Sex_Scheme_PROBABILITY_OF_MALES = 'PROBABILITY_OF_MALES'
    static_str_Value__Species_Offspring_Sex_Scheme_EXACT_PARITY_MALES_AND_FEMALES = 'EXACT_PARITY_MALES_AND_FEMALES'
    static_str_Option__Species_Offspring_Sex_Scheme_PROBABILITY_OF_MALES_Prob_of_Males = 'Probability_of_Males'
    static_str_Option__Species_Offspring_Distribution = 'Offspring_Distribution'
    static_str_Value__Species_Offspring_Distribution_ABSOLUTE = 'ABSOLUTE'
    static_str_Value__Species_Offspring_Distribution_POISSON = 'POISSON'
    static_str_Value__Species_Offspring_Distribution_BINOMIAL = 'BINOMIAL'
    static_str_Value__Species_Offspring_Distribution_UNIFORM = 'UNIFORM'
    static_str_Value__Species_Offspring_Distribution_GEOMETRIC = 'GEOMETRIC'
    static_str_Option__Species_Offspring_Distribution_ABSOLUTE_Offspring_Number = 'Offspring_Distribution_ABSOLUTE__Number_Of_Offspring_Per_Mating'
    static_str_Option__Species_Offspring_Distribution_POISSON_Offspring_Mean_Number = 'Offspring_Distribution_POISSON__Mean_Number_Of_Offspring_Per_Mating'
    static_str_Option__Species_Offspring_Distribution_BINOMIAL_Offspring_Mean_Number = 'Offspring_Distribution_BINOMIAL__Mean_Number_Of_Offspring_Per_Mating'
    static_str_Option__Species_Offspring_Distribution_BINOMIAL_Offspring_StdDev = 'Offspring_Distribution_BINOMIAL__Standard_Deviation_Of_Offspring_Per_Mating'
    static_str_Option__Species_Offspring_Distribution_UNIFORM_Offspring_Min = 'Offspring_Distribution_UNIFORM__Min_Number_Of_Offspring_Per_Mating'
    static_str_Option__Species_Offspring_Distribution_UNIFORM_Offspring_Max = 'Offspring_Distribution_UNIFORM__Max_Number_Of_Offspring_Per_Mating'
    static_str_Option__Species_Offspring_Distribution_GEOMETRIC_Offspring_Mean = 'Offspring_Distribution_GEOMETRIC__Mean_Of_Offspring_Per_Mating'
    
    
    static_str_Section__Species_Demographic_Natural_Mortality_Details__MALE = 'Natural_Mortality_Details__MALE'
    static_str_Option__Species_Demographic_Natural_Mortality_Model_Annual_Mating_That_Mortality_Starts__MALE = 'Natural_Mortality_Model_Annual_Mating_That_Mortality_Starts__MALE'
    static_str_Option__Species_Demographic_Natural_Mortality_Model__MALE = 'Natural_Mortality_Model__MALE'
    static_str_Option__Species_Demographic_Natural_Mortality_Model_Scaling_Total__MALE = 'Natural_Mortality_Model_Scaling_Total__MALE'


    static_str_Section__Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__MALE = 'CSV_Age_And_Natural_Mortality_Rate__MALE'

    static_str_Section__Species_Demographic_Natural_Mortality_Details__FEMALE = 'Natural_Mortality_Details__FEMALE'
    static_str_Option__Species_Demographic_Natural_Mortality_Model_Annual_Mating_That_Mortality_Starts__FEMALE = 'Natural_Mortality_Model_Annual_Mating_That_Mortality_Starts__FEMALE'
    static_str_Option__Species_Demographic_Natural_Mortality_Model__FEMALE = 'Natural_Mortality_Model__FEMALE'
    static_str_Option__Species_Demographic_Natural_Mortality_Model_Scaling_Total__FEMALE = 'Natural_Mortality_Model_Scaling_Total__FEMALE'
    
    
    static_str_Section__Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__FEMALE = 'CSV_Age_And_Natural_Mortality_Rate__FEMALE'


    static_str_Section__Species_Demographic_UnNatural_Mortality_Details__BOTH = 'UnNatural_Mortality_Details__BOTH'
    static_str_Option__Species_Demographic_UnNatural_Mortality_Allowed__BOTH = 'UnNatural_Mortality_Allowed__BOTH'

    
    static_str_Section__Species_Demographic_UnNatural_Mortality_Details__MALE = 'UnNatural_Mortality_Details__MALE'
    static_str_Option__Species_Demographic_UnNatural_Mortality_Model_Annual_Mating_That_Mortality_Starts__MALE = 'UnNatural_Mortality_Model_Annual_Mating_That_Mortality_Starts__MALE'
    static_str_Option__Species_Demographic_UnNatural_Mortality_Model__MALE = 'UnNatural_Mortality_Model__MALE'
    static_str_Option__Species_Demographic_UnNatural_Mortality_Model_Scaling_Total__MALE = 'UnNatural_Mortality_Model_Scaling_Total__MALE'
    
    
    static_str_Section__Species_Demographic_UnNatural_Mortality_CSV_Age_And_Mortality_Rate__MALE = 'CSV_Age_And_UnNatural_Mortality_Rate__MALE'


    static_str_Section__Species_Demographic_UnNatural_Mortality_Details__FEMALE = 'UnNatural_Mortality_Details__FEMALE'
    static_str_Option__Species_Demographic_UnNatural_Mortality_Model_Annual_Mating_That_Mortality_Starts__FEMALE = 'UnNatural_Mortality_Model_Annual_Mating_That_Mortality_Starts__FEMALE'
    static_str_Option__Species_Demographic_UnNatural_Mortality_Model__FEMALE = 'UnNatural_Mortality_Model__FEMALE'
    static_str_Option__Species_Demographic_UnNatural_Mortality_Model_Scaling_Total__FEMALE = 'UnNatural_Mortality_Model_Scaling_Total__FEMALE'
    
    
    static_str_Section__Species_Demographic_UnNatural_Mortality_CSV_Age_And_Mortality_Rate__FEMALE = 'CSV_Age_And_UnNatural_Mortality_Rate__FEMALE'


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
    