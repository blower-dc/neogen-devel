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
import sys
#
import os, fnmatch
import csv
#
import pandas
#from openpyxl import load_workbook as openpyxl__load_workbook
from collections import OrderedDict
import numpy
from scipy.stats import hmean as scipy__stats__hmean
#import openpyxl
# DEBUG Imports
#import objgraph
import pdb
from memory_profiler import profile
#------------------< Import DCB_General modules
from FileHandler import FileHandler
#from Bio.PopGen.GenePop.EasyController import EasyController as biopython__Easy_Controller
from handler_Logging import Logging
#------------------< Import SharkSim modules
from SSParameterHandler import SSParameterHandler
from SSOutputHandler import SSOutputHandler
from globals_SharkSim import globalsSS
from SSAnalysisHandler import SSAnalysisHandler

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
class SSResults(object):
    '''
    classdocs
    '''

    str_Results_Base_Path = ''
    

    def __enter__(self):
        
        return self 
         
    def __init__(self, objSSParametersLocal):
        '''
        Constructor
        '''
 
        self.objSSParametersLocal = objSSParametersLocal
        
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
    '''
    -------------------------------------------------------------
    EXPERIMENT_Parent_Offspring_Ne_1 - Summarise Categorised NE2 & Parent Offspring Results 
    -------------------------------------------------------------
    '''   
    def func_EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results__Aggregate_Results(self, str_Search_Path):

        boolSuccess = False

        '''
        Process Results
        '''
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName + '_' + str_Excel_Output_Colname_Prefix

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
 
        '''
        Aggregate Excel Data to dataframe from each input file
        '''
        ''' Input file '''
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results + '*.xlsx'
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results
        str_File_Search_Pattern = str_Input_FileName
        
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName)
        
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_Located:
            
            '''Process Results'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                self.obj_Log_Default.info('Processing Excel File: ' + str_Path_And_File)
                self.obj_Log_Default.info('Processing Excel Sheet: ' + str_Input_Excel_Sheet_Name)
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DFs.append(df_1)
                
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
        
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
    
        if bool_File_Located:
            '''
            Process aggregated dataframes
            '''
            df = self.func__EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results__Aggregated_Dataframes__Process(df)
            
        pass
            
        if bool_File_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass

    
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Default.info('Excel file written.')
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written')
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess


    def func__EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results__Aggregated_Dataframes__Process(self, df):
        

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df      
    

    def func__EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Categorised_Ne2_Sampling_Stats.static_Label_Gen_File
        '''EXPERIMENT_Parent_Offspring_Ne_1 Colnames '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_LDNe_PCrit] = str_Last

        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last

        
        ''' Colnames_Parent_Offspring_Stats_METHOD_2 '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Male_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Female_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Sires] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Dames] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Potential_Parents_PP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Effective_Parents_EP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeEP] = str_Mean
        
        '''Colnames Ne2 Output '''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeLoci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeSamples] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_strPopID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intMatingScheme] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intIndependentAlleles] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatWeightedMeanSampleSize] = str_Mean
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI] = str_Mean
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Genepop_Source_File] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Genepop_Source_Path] = str_Last
        
        '''Get the Actual colnames given generic ones '''
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        #str_Group_Key_Experiment_Label = globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label
        str_Group_Key_Batch =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Stats_Category = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category
        #str_Group_Key_Replicate =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_LDNe_PCrit = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        #str_Col_Name_Experiment_Label = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Experiment_Label)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Stats_Category = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category)
        #str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_LDNe_PCrit = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_LDNe_PCrit)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Stats_Category, str_Col_Name_LDNe_PCrit], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
        ''' Additional Colnames '''
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Mean_Ne2_Burrows_r_Squared_Diff] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Total_Ne2_r_Sqrd_LDNe] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc] = 'func'       
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_DemoNe] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents] = 'func'       
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 


    def func__EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results__Calculate(self, df):

        str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
        str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected

        ''' Get Colname from key '''
        str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
        str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
        
        ''' New Colnames '''
        str_Colname_float_Mean_Ne2_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Mean_Ne2_Burrows_r_Squared_Diff
        str_Colname_float_Total_Ne2_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Total_Ne2_r_Sqrd_LDNe
                
        with SSAnalysisHandler() as obj_SSAnalysis:
            df[str_Colname_float_Mean_Ne2_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
            df[str_Colname_float_Total_Ne2_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
        pass

        str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Total_Ne2_r_Sqrd_LDNe        
        str_Colname_int_Potential_Parents_PP = globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Potential_Parents_PP    
        str_Colname_float_Demo_NePP = globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP      
        str_Colname_int_Effective_Parents_EP = globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Effective_Parents_EP        
        
        ''' Get Colname from key '''
        str_Colname_float_Burrows_r_Sqrd_LDNe = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_float_Burrows_r_Sqrd_LDNe)
        str_Colname_int_Potential_Parents_PP = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_int_Potential_Parents_PP)
        str_Colname_float_Demo_NePP = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_float_Demo_NePP)
        str_Colname_int_Effective_Parents_EP = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_int_Effective_Parents_EP)
        
        ''' New Colnames '''
        str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc       
        str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_DemoNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_DemoNe
        str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents       
        
        
        with SSAnalysisHandler() as obj_SSAnalysis:
            df[str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc] = df.apply(lambda row: obj_SSAnalysis.method_Get_Ratio_Stat(row[str_Colname_float_Burrows_r_Sqrd_LDNe], row[str_Colname_int_Potential_Parents_PP]), axis=1)
            df[str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_DemoNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_Ratio_Stat(row[str_Colname_float_Burrows_r_Sqrd_LDNe], row[str_Colname_float_Demo_NePP]), axis=1)
            df[str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents] = df.apply(lambda row: obj_SSAnalysis.method_Get_Ratio_Stat(row[str_Colname_float_Burrows_r_Sqrd_LDNe], row[str_Colname_int_Effective_Parents_EP]), axis=1)
        pass
        
        return df
    
    '''
    -------------------------------------------------------------
    EXPERIMENT_Parent_Offspring_Ne_1 - Composite Results - MERGE CATEGORISED NE2 & PARENT_OFFSPRING MEAN REPLICATE Results
    -------------------------------------------------------------
    '''   
    def func_EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results__Aggregate_Results(self, str_Search_Path):

        boolSuccess = False
       
        '''
        Process Results
        '''
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results

        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName + '_' + str_Excel_Output_Colname_Prefix

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
 
        '''
        Aggregate Excel Data to dataframe from each input file
        '''
        ''' Input file 1 '''
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results + '*.xlsx'
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results
        str_File_Search_Pattern = str_Input_FileName
        
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName) 
               
        bool_File_1_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_1_Located:
            
            '''Process Results'''
            list_DF_1s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_1s.append(df_1)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_1s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            df1 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

 
        '''
        Aggregate Excel Data to dataframe from each input file
        '''
        ''' Input file 2 '''
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results + '*.xlsx'
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results
        str_File_Search_Pattern = str_Input_FileName
        
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName) 
               
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_2 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_2s.append(df_2)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
            
            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join & Transform the dataframes
            '''
            list_DFs = [df1, df2]
            df = self.func__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results__Aggregated_Dataframes__Process(list_DFs)            
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
        pass
                
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_1_Located and bool_File_2_Located:
            self.func_Save_Excel_Writer(writer)
            boolSuccess = True
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess


    def func__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results__Aggregated_Dataframes__Process(self, list_DFs):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Join Dataframes
        ---------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results__Merge(list_DFs)
        
        '''
        Add calculations
        '''
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
 
 
    def func__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results__Merge(self, list_DFs):


        self.obj_Log_Default.info('Merge Dataframes')
        
        '''
        -------------------------
        Specify Key Colnames to merge on
        -------------------------
        '''
        strKey1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
        strKey2 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Batch
        strKey3 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Replicate

        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        str_Join_How = 'left'
        list_Keys = [strKey1,strKey2,strKey3]
        df = self.func_Merge_Dataframes_By_Key_List(str_Join_How, list_DFs[0], list_DFs[1], list_Keys)

        return df
    
    
    def func__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        #str_Colname_Prefix_1 = globalsSS.Categorised_Ne2_Sampling_Stats.static_Label_Gen_File
        str_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results
        '''EXPERIMENT_Parent_Offspring_Ne_1 Colnames '''
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_LDNe_PCrit] = str_Last

        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last

        
        ''' Colnames_Parent_Offspring_Stats_METHOD_2 '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Male_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Female_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Sires] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Dames] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Potential_Parents_PP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Effective_Parents_EP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeEP] = str_Mean
        
        '''Colnames Ne2 Output '''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeLoci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeSamples] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_strPopID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intMatingScheme] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intIndependentAlleles] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatWeightedMeanSampleSize] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Genepop_Source_File] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Genepop_Source_Path] = str_Last
        
        '''Get the Actual colnames given generic ones '''
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        #str_Group_Key_Experiment_Label = globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Stats_Category = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category
        str_Group_Key_Batch =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_LDNe_PCrit = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        #str_Col_Name_Experiment_Label = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Experiment_Label)
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Stats_Category = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_LDNe_PCrit = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_LDNe_PCrit)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_LDNe_PCrit], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
        ''' Additional Colnames '''
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
    
 
    def func__EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results__Calculate(self, df):

        str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
        str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected

        ''' Get Colname from key '''
        str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
        str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)

        ''' New Colnames '''
        str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
        str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
                 
        with SSAnalysisHandler() as obj_SSAnalysis:
            df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
            df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
        return df
 
    '''
    -------------------------------------------------------------
    EXPERIMENT_Parent_Offspring_Ne_1 -  Categorised NE2 Results Per Replicate Results to summarise
    -------------------------------------------------------------
    '''   
    def func_EXPERIMENT_Parent_Offspring_Ne_1__Ne2_EOR_Results__Aggregate_Results(self, str_Search_Path):

        boolSuccess = False
       
        '''
        Process Results
        '''
        
        ''' Input file '''
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results
        
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName + '_' + str_Excel_Output_Colname_Prefix

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
 
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName)
        
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
            
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__EXPERIMENT_Parent_Offspring_Ne_1__Ne2_EOR_Results__Aggregate__Process(str_Path_And_File)
                list_DFs.append(df)
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
        
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Default.info('Excel file written.')
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written')
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess
    
    
    def func__EXPERIMENT_Parent_Offspring_Ne_1__Ne2_EOR_Results__Aggregate__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 
    '''
    -------------------------------------------------------------
    EXPERIMENT_Parent_Offspring_Ne_1 - PARENT/OFFSPRING Per Fertilization Results to summarise
    -------------------------------------------------------------
    '''   
    def func_EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results__Aggregate_Results(self, str_Search_Path):

        boolSuccess = False

        '''
        Process Results
        '''
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_Colname_Prefix

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
 
        '''
        Aggregate Excel Data to dataframe from each input file
        '''
        ''' Input file '''
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__Embryo_Parent_Ne_Stats_Post_Fertilization + '*.xlsx'
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Embryo_Parent_Ne_Stats_Post_Fertilization
        str_File_Search_Pattern = str_Input_FileName
        
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName)
        
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_Located:
            
            '''Process Results'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                self.obj_Log_Default.info('Processing Excel File: ' + str_Path_And_File)
                self.obj_Log_Default.info('Processing Excel Sheet: ' + str_Input_Excel_Sheet_Name)                
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DFs.append(df_1)
                
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
        
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
    
        if bool_File_Located:
            '''
            Process aggregated dataframes
            '''
            df = self.func__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results__Aggregated_Dataframes__Process(df)
            
        pass
            
        if bool_File_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass

    
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Default.info('Excel file written.')
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written')
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess
    
    
    def func__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results__Aggregated_Dataframes__Process(self, df):
        

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
    
        
#     def func__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results__Aggregate__Process(self, str_Path_And_File):
#         
# 
#         self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)
# 
#         '''Aggregate Results to dataframe'''        
#         df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)
# 
#         ''' Transform dataframe columns'''
#         df = self.func__Transform_Dataframe_Column_Datatypes(df)
# 
#         '''
#         ---------------------
#         Group/Calculate/Rename
#         ---------------------
#         '''
#         df = self.func__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results__Group_Calculate_And_Rename(df)
#         
#     
#         ''' Sort & Reindex dataframe '''
#         df = self.func__Sort_Reindex_Dataframe(df)
# 
# 
#         return df    
#     
    
    
    def func__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Matings] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Replicates] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples] = str_Last

        '''EXPERIMENT_Parent_Offspring_Ne_1 Colnames '''
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = str_Last
        
        ''' Colnames_Parent_Offspring_Stats_METHOD_2 '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Male_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Female_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Sires] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Dames] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Potential_Parents_PP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Effective_Parents_EP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeEP] = str_Mean
        
        '''Get the Actual colnames given generic ones '''
        #dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        SUBSET DF - Subset by Burn-In = False - We remove the Burn-in records as they affect the mean calcs etc.
        -------------------------
        '''
        ''' Specify Subset keys '''
        str_Subset_Key_Burn_In =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual SUBSET KEY colnames from generic ones')
        str_Col_Name_Subset_Key_Burn_In = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Subset_Key_Burn_In)
        
        ''' Subset the DF to get the required records only '''
        self.obj_Log_Default.info('SUBSETing DF')
        str_Burn_In_False = False
        df = df[(df[str_Col_Name_Subset_Key_Burn_In]==str_Burn_In_False)]
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass

        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 

    '''
    -------------------------------------------------------------
    EXPERIMENT_Parent_Offspring_Ne_1 - Summarise Categorised NE2 & Parent Offspring Results 
    -------------------------------------------------------------
    '''   
    def func_EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results__Aggregate_Results(self, str_Search_Path):

        boolSuccess = False

        '''
        Process Results
        '''
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName + '_' + str_Excel_Output_Colname_Prefix

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
 
        '''
        Aggregate Excel Data to dataframe from each input file
        '''
        ''' Input file '''
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results + '*.xlsx'
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results
        str_File_Search_Pattern = str_Input_FileName
        
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName)
        
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_Located:
            
            '''Process Results'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                self.obj_Log_Default.info('Processing Excel File: ' + str_Path_And_File)
                self.obj_Log_Default.info('Processing Excel Sheet: ' + str_Input_Excel_Sheet_Name)
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DFs.append(df_1)
                
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
        
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
    
        if bool_File_Located:
            '''
            Process aggregated dataframes
            '''
            df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results__Aggregated_Dataframes__Process(df)
            
        pass
            
        if bool_File_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass

    
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Default.info('Excel file written.')
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written')
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess


    def func__EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results__Aggregated_Dataframes__Process(self, df):
        

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df      
    

    def func__EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results + '_'
        '''EXPERIMENT_Parent_Offspring_Ne_1 Colnames '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_LDNe_PCrit] = str_Last

        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last

        
        ''' Colnames_Parent_Offspring_Stats_METHOD_2 '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Male_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Female_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Sires] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Dames] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Potential_Parents_PP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Effective_Parents_EP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeEP] = str_Mean
        
        '''Colnames Ne2 Output '''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeLoci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeSamples] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_strPopID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intMatingScheme] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intIndependentAlleles] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatWeightedMeanSampleSize] = str_Mean
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI] = str_Mean
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Genepop_Source_File] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Genepop_Source_Path] = str_Last
        
        '''Get the Actual colnames given generic ones '''
        #dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        #str_Group_Key_Experiment_Label = globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label
        str_Group_Key_Batch =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        #str_Group_Key_Replicate =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Stats_Category = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category
        str_Group_Key_Mating_Count_Replicate_Total =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_LDNe_PCrit = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        #str_Col_Name_Experiment_Label = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Experiment_Label)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        #str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Stats_Category = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_LDNe_PCrit = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_LDNe_PCrit)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        #df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Stats_Category, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Stats_Category, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
        ''' Additional Colnames '''
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Mean_Ne2_Burrows_r_Squared_Diff] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Total_Ne2_r_Sqrd_LDNe] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc] = 'func'       
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_DemoNe] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents] = 'func'       
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 


    def func__EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results__Calculate(self, df):

        str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
        str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected

        ''' Get Colname from key '''
        str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
        str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
        
        ''' New Colnames '''
        str_Colname_float_Mean_Ne2_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Mean_Ne2_Burrows_r_Squared_Diff
        str_Colname_float_Total_Ne2_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Total_Ne2_r_Sqrd_LDNe
                
        with SSAnalysisHandler() as obj_SSAnalysis:
            df[str_Colname_float_Mean_Ne2_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
            df[str_Colname_float_Total_Ne2_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
        pass

        str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Total_Ne2_r_Sqrd_LDNe        
        str_Colname_int_Potential_Parents_PP = globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Potential_Parents_PP    
        str_Colname_float_Demo_NePP = globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP      
        str_Colname_int_Effective_Parents_EP = globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Effective_Parents_EP        
        
        ''' Get Colname from key '''
        str_Colname_float_Burrows_r_Sqrd_LDNe = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_float_Burrows_r_Sqrd_LDNe)
        str_Colname_int_Potential_Parents_PP = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_int_Potential_Parents_PP)
        str_Colname_float_Demo_NePP = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_float_Demo_NePP)
        str_Colname_int_Effective_Parents_EP = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_int_Effective_Parents_EP)
        
        ''' New Colnames '''
        str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc       
        str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_DemoNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_DemoNe
        str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents       
        
        
        with SSAnalysisHandler() as obj_SSAnalysis:
            df[str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc] = df.apply(lambda row: obj_SSAnalysis.method_Get_Ratio_Stat(row[str_Colname_float_Burrows_r_Sqrd_LDNe], row[str_Colname_int_Potential_Parents_PP]), axis=1)
            df[str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_DemoNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_Ratio_Stat(row[str_Colname_float_Burrows_r_Sqrd_LDNe], row[str_Colname_float_Demo_NePP]), axis=1)
            df[str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents] = df.apply(lambda row: obj_SSAnalysis.method_Get_Ratio_Stat(row[str_Colname_float_Burrows_r_Sqrd_LDNe], row[str_Colname_int_Effective_Parents_EP]), axis=1)
        pass
        
        return df

    
    '''
    -------------------------------------------------------------
    EXPERIMENT_Parent_Offspring_Ne_2 - Composite Results - MERGE CATEGORISED NE2 & PARENT_OFFSPRING MEAN REPLICATE Results
    -------------------------------------------------------------
    '''   
    def func_EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results__Aggregate_Results(self, str_Search_Path):

        boolSuccess = False
       
        '''
        Process Results
        '''
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results

        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName + '_' + str_Excel_Output_Colname_Prefix

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
 
        '''
        Aggregate Excel Data to dataframe from each input file
        '''
        ''' Input file 1 '''
        #str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Embryo_Parent_Ne_Stats_Post_Fertilization + '*.xlsx'
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__Embryo_Parent_Ne_Stats_Post_Fertilization + '*.xlsx'
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Embryo_Parent_Ne_Stats_Post_Fertilization
        str_File_Search_Pattern = str_Input_FileName
        
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName) 
               
        bool_File_1_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_1_Located:
            
            '''Process Results'''
            list_DF_1s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_1s.append(df_1)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_1s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            df1 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

 
        '''
        Aggregate Excel Data to dataframe from each input file
        '''
        ''' Input file 2 '''
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results + '*.xlsx'
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results
        str_File_Search_Pattern = str_Input_FileName
        
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName) 
               
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_2 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_2s.append(df_2)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
            
            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join & Transform the dataframes
            '''
            list_DFs = [df1, df2]
            df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results__Aggregated_Dataframes__Process(list_DFs)            
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
        pass
                
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_1_Located and bool_File_2_Located:
            self.func_Save_Excel_Writer(writer)
            boolSuccess = True
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess


    def func__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results__Aggregated_Dataframes__Process(self, list_DFs):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Join Dataframes
        ---------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results__Merge(list_DFs)
        
        '''
        Add calculations
        '''
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
 
 
    def func__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results__Merge(self, list_DFs):


        self.obj_Log_Default.info('Merge Dataframes')
        
        '''
        -------------------------
        Specify Key Colnames to merge on
        -------------------------
        '''
        strKey1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
        strKey2 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Batch
        strKey3 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Replicate
        strKey4 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total

        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        str_Join_How = 'left'
        list_Keys = [strKey1,strKey2,strKey3,strKey4]
        df = self.func_Merge_Dataframes_By_Key_List(str_Join_How, list_DFs[0], list_DFs[1], list_Keys)

        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF 
        
        return df
    
    
    def func__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results
        '''EXPERIMENT_Parent_Offspring_Ne_2 Colnames '''
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_2.static_Str_Colname_LDNe_PCrit] = str_Last

        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last

        
        ''' Colnames_Parent_Offspring_Stats_METHOD_2 '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Male_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Female_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Sires] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Dames] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Potential_Parents_PP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Effective_Parents_EP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeEP] = str_Mean

        '''Colnames Ne2 Output '''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeLoci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeSamples] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_strPopID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intMatingScheme] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intIndependentAlleles] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatWeightedMeanSampleSize] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Genepop_Source_File] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Genepop_Source_Path] = str_Last
        
        '''Get the Actual colnames given generic ones '''
        #dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        #str_Group_Key_Experiment_Label = globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_2.static_Str_Colname_Ne2_Experiment_Label
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Stats_Category = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category
        str_Group_Key_Batch =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Mating_Count_Replicate_Total =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_LDNe_PCrit = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        #str_Col_Name_Experiment_Label = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Experiment_Label)
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Stats_Category = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_LDNe_PCrit = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_LDNe_PCrit)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_2.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF       
        
        return df 
    
 
    def func__EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results__Calculate(self, df):

        str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
        str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected

        ''' Get Colname from key '''
        str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
        str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)

        ''' New Colnames '''
        str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
        str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
                 
        with SSAnalysisHandler() as obj_SSAnalysis:
            df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
            df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
        return df

    
    '''
    -------------------------------------------------------------
    EXPERIMENT_Parent_Offspring_Ne_2 -  Categorised NE2 Results PER FERTILIZATION  Results to AGGREGATE
    -------------------------------------------------------------
    '''   
    def func_EXPERIMENT_Parent_Offspring_Ne_2__Ne2_PF_Results__Aggregate_Results(self, str_Search_Path):

        boolSuccess = False
       
        '''
        Process Results
        '''
        
        ''' Input file '''
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results
        
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName + '_' + str_Excel_Output_Colname_Prefix

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
 
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName)
        
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
            
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__EXPERIMENT_Parent_Offspring_Ne_1__Ne2_PF_Results__Aggregate__Process(str_Path_And_File)
                list_DFs.append(df)
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
        
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Default.info('Excel file written.')
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written')
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess
    
    
    def func__EXPERIMENT_Parent_Offspring_Ne_2__Ne2_PF_Results__Aggregate__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

    '''
    -------------------------------------------------------------
    EXPERIMENT_Parent_Offspring_Ne_1 - PS_Summarise Categorised NE2 & Parent Offspring Results 
    -------------------------------------------------------------
    '''   
    def func_EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results__Aggregate_Results(self, str_Excel_Save_Path, str_Search_Path):

        boolSuccess = False

        '''
        Process Results
        '''
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Ne2_LDNe__Summary_EOR_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__Ne2_LDNe__Summary_EOR_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Summary_EOR_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_Colname_Prefix

        #str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
 
        '''
        Aggregate Excel Data to dataframe from each input file
        '''
        ''' Input file '''
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__Ne2_LDNe__Composite_EOR_Results + '*.xlsx'
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Composite_EOR_Results
        str_File_Search_Pattern = str_Input_FileName
        
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName)
        
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_Located:
            
            '''Process Results'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                self.obj_Log_Default.info('Processing Excel File: ' + str_Path_And_File)
                self.obj_Log_Default.info('Processing Excel Sheet: ' + str_Input_Excel_Sheet_Name)
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DFs.append(df_1)
                
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
        
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
    
        if bool_File_Located:
            '''
            Process aggregated dataframes
            '''
            df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results__Aggregated_Dataframes__Process(df)
            
        pass
            
        if bool_File_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name, list_Columns_To_Write=[], bool_NaN_As_NA = True)            
        pass

    
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Default.info('Excel file written.')
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written')
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results__Aggregated_Dataframes__Process(self, df):
        

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df      
    
    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results__Group_Calculate_And_Rename_RETIRE(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Ne2_LDNe__Composite_EOR_Results + '_'
        '''EXPERIMENT_Parent_Offspring_Ne_1 Colnames '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_LDNe_PCrit] = str_Last

        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last

        
        ''' Colnames_Parent_Offspring_Stats_METHOD_2 '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Male_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Female_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Sires] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Dames] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Potential_Parents_PP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Effective_Parents_EP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeEP] = str_Mean
        
        '''Colnames Ne2 Output '''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeLoci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeSamples] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Loci_Number]  = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_strPopID] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intMatingScheme] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intIndependentAlleles] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatWeightedMeanSampleSize] = str_Mean
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe_Harmonic_Mean] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI] = str_Mean
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNe] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeParametric_Lwr_CI] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeParametric_Upr_CI] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Lwr_CI] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Upr_CI] = str_Sum        
        
        '''Get the Actual colnames given generic ones '''
        #dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        #str_Group_Key_Experiment_Label = globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label
        str_Group_Key_Batch =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        #str_Group_Key_Replicate =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Stats_Category_Code = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
        #str_Group_Key_Stats_Category = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category
        str_Group_Key_Mating_Count_Replicate_Total =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_LDNe_PCrit = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        #str_Col_Name_Experiment_Label = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Experiment_Label)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        #str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Stats_Category_Code = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category_Code)
        #str_Col_Name_Stats_Category = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_LDNe_PCrit = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_LDNe_PCrit)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        #df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Stats_Category, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Stats_Category_Code, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Ne2_LDNe__Composite_EOR_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
        ''' Additional Colnames '''
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Mean_Ne2_Burrows_r_Squared_Diff] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Total_Ne2_r_Sqrd_LDNe] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc] = 'func'       
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_DemoNe] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents] = 'func'       
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Ne2_LDNe__Summary_EOR_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 

    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Ne2_LDNe__Composite_EOR_Results + '_'
        '''EXPERIMENT_Parent_Offspring_Ne_1 Colnames '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_LDNe_PCrit] = str_Last

        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last

        
        ''' Colnames_Parent_Offspring_Stats_METHOD_2 '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Male_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Female_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Sires] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Dames] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Potential_Parents_PP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Effective_Parents_EP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeEP] = str_Mean
        
        '''Colnames Ne2 Output '''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeLoci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeSamples] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Loci_Number]  = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_strPopID] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intMatingScheme] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intIndependentAlleles] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatWeightedMeanSampleSize] = str_Mean
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI] = str_Mean
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNe] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeParametric_Lwr_CI] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeParametric_Upr_CI] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Lwr_CI] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Upr_CI] = str_Sum        
        
        '''Get the Actual colnames given generic ones '''
        #dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        #str_Group_Key_Experiment_Label = globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label
        str_Group_Key_Batch =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        #str_Group_Key_Replicate =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Stats_Category_Code = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
        #str_Group_Key_Stats_Category = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category
        str_Group_Key_Mating_Count_Replicate_Total =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_LDNe_PCrit = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        #str_Col_Name_Experiment_Label = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Experiment_Label)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        #str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Stats_Category_Code = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category_Code)
        #str_Col_Name_Stats_Category = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_LDNe_PCrit = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_LDNe_PCrit)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        #df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Stats_Category, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Stats_Category_Code, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Ne2_LDNe__Composite_EOR_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
        ''' Additional Colnames '''
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Mean_Ne2_Burrows_r_Squared_Diff] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Total_Ne2_r_Sqrd_LDNe] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc] = 'func'       
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_DemoNe] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents] = 'func'       
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Ne2_LDNe__Summary_EOR_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 

    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results__Calculate(self, df):

        str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
        str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected

        ''' Get Colname from key '''
        str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
        str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
        
        ''' New Colnames '''
        str_Colname_float_Mean_Ne2_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Mean_Ne2_Burrows_r_Squared_Diff
        str_Colname_float_Total_Ne2_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Total_Ne2_r_Sqrd_LDNe
                
        with SSAnalysisHandler() as obj_SSAnalysis:
            df[str_Colname_float_Mean_Ne2_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
            df[str_Colname_float_Total_Ne2_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
        pass

        str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Total_Ne2_r_Sqrd_LDNe        
        str_Colname_int_Potential_Parents_PP = globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Potential_Parents_PP    
        str_Colname_float_Demo_NePP = globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP      
        str_Colname_int_Effective_Parents_EP = globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Effective_Parents_EP        
        
        ''' Get Colname from key '''
        str_Colname_float_Burrows_r_Sqrd_LDNe = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_float_Burrows_r_Sqrd_LDNe)
        str_Colname_int_Potential_Parents_PP = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_int_Potential_Parents_PP)
        str_Colname_float_Demo_NePP = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_float_Demo_NePP)
        str_Colname_int_Effective_Parents_EP = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_int_Effective_Parents_EP)
        
        ''' New Colnames '''
        str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc       
        str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_DemoNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_DemoNe
        str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents       
        
        
        with SSAnalysisHandler() as obj_SSAnalysis:
            df[str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Nc] = df.apply(lambda row: obj_SSAnalysis.method_Get_Ratio_Stat(row[str_Colname_float_Burrows_r_Sqrd_LDNe], row[str_Colname_int_Potential_Parents_PP]), axis=1)
            df[str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_DemoNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_Ratio_Stat(row[str_Colname_float_Burrows_r_Sqrd_LDNe], row[str_Colname_float_Demo_NePP]), axis=1)
            df[str_Colname_float_Ratio_Total_Ne2_r_Sqrd_LDNe_To_Mean_Unique_Eff_Parents] = df.apply(lambda row: obj_SSAnalysis.method_Get_Ratio_Stat(row[str_Colname_float_Burrows_r_Sqrd_LDNe], row[str_Colname_int_Effective_Parents_EP]), axis=1)
        pass
        
        return df

    '''
    -------------------------------------------------------------
    EXPERIMENT_Parent_Offspring_Ne_2 - Composite Results - MERGE CATEGORISED NE2 & PARENT_OFFSPRING MEAN REPLICATE Results
    -------------------------------------------------------------
    '''   
    def func_EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Aggregate_Results(self, str_Excel_Save_Path, str_Search_Path__Batch_Scenario_Data, str_Search_Path__Sampling_Strategy_Data):

        boolSuccess = False
       
        '''
        Process Results
        '''
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Ne2_LDNe__Composite_EOR_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__Ne2_LDNe__Composite_EOR_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Composite_EOR_Results

        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_Colname_Prefix

        #str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
 
        '''
        Aggregate Excel Data to dataframe from each input file
        '''
        ''' Input file 1 '''
        #str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Embryo_Parent_Ne_Stats_Post_Fertilization + '*.xlsx'
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__Embryo_Parent_Ne_Stats_Post_Fertilization + '*.xlsx'
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Embryo_Parent_Ne_Stats_Post_Fertilization
        str_File_Search_Pattern = str_Input_FileName
        str_Search_Path = str_Search_Path__Batch_Scenario_Data
        
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName) 
               
        bool_File_1_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_1_Located:
            
            '''Process Results'''
            list_DF_1s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_1s.append(df_1)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_1s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            df1 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

 
        '''
        Aggregate Excel Data to dataframe from each input file
        '''
        ''' Input file 2 '''
#         str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PS_PF_Results + '*.xlsx'
#         str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PS_PF_Results
#         str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__Ne2_LDNe__Raw_EOR_Results + '*.xlsx'
#         str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Raw_EOR_Results
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__Ne2_LDNe__Categorised_EOR_Results + '*.xlsx'
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Categorised_EOR_Results
        str_File_Search_Pattern = str_Input_FileName
        str_Search_Path = str_Search_Path__Sampling_Strategy_Data
        
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName) 
               
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_2 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_2s.append(df_2)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
            
            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join & Transform the dataframes
            '''
            list_DFs = [df1, df2]
            df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Aggregated_Dataframes__Process(list_DFs)            
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
        pass
                
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name, list_Columns_To_Write=[], bool_NaN_As_NA = True)                
        pass
    
        ''' final save of the excel file '''
        if bool_File_1_Located and bool_File_2_Located:
            self.func_Save_Excel_Writer(writer)
            boolSuccess = True
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Aggregated_Dataframes__Process(self, list_DFs):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Join Dataframes
        ---------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Merge(list_DFs)
        
        '''
        Add calculations
        '''
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
 
    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Merge(self, list_DFs):


        self.obj_Log_Default.info('Merge Dataframes')
        
        '''
        -------------------------
        Specify Key Colnames to merge on
        -------------------------
        '''
        #strKey1 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
        strKey1 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total

        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        #str_Join_How = 'left'
        str_Join_How = 'right'
        list_Keys = [strKey1]
        df = self.func_Merge_Dataframes_By_Key_List(str_Join_How, list_DFs[0], list_DFs[1], list_Keys)

        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF 
        
        return df
    
    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')

        '''
        -------------------------
        Pre-aggregation Calculations
        -------------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Calculate_Inf_Counts(df)       
        bool_Use_Harmonic_Mean = True
        if bool_Use_Harmonic_Mean: 
            df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Calculate_Harmonic_Mean_LDNe(df)
        pass
            
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        str_Median = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__median
        
        #scipy_Harmonic_Mean = scipy__stats__hmean
        
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Embryo_Parent_Ne_Stats_Post_Fertilization + '_'
        '''EXPERIMENT_Parent_Offspring_Ne_2 Colnames '''
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_2.static_Str_Colname_LDNe_PCrit] = str_Last

        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last

        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        
        ''' Colnames_Parent_Offspring_Stats_METHOD_2 '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Male_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Female_Potential_Parent] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Sires] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Dames] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Potential_Parents_PP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Effective_Parents_EP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeEP] = str_Mean

        '''Colnames Ne2 Output '''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeLoci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeSamples] = str_Mean #str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Loci_Number]  = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_strPopID] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intMatingScheme] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intIndependentAlleles] = str_Mean #str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatWeightedMeanSampleSize] = str_Mean #str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed] = str_Mean #str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected] = str_Mean #str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe] = scipy_Harmonic_Mean #This wont work with negative numbers or zeros
        
        if bool_Use_Harmonic_Mean:
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe] = str_Last
            bool_Use_Harmonic_Mean_For_CIs = True
            if bool_Use_Harmonic_Mean_For_CIs:
                dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] = str_Last
                dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI] = str_Last
                dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI] = str_Last
                dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI] = str_Last
            else:
                dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] = str_Median
                dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI] = str_Median
                dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI] = str_Median
                dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI] = str_Median
            pass
        else:
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe] = str_Mean        
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] = str_Mean #str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI] = str_Mean #str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI] = str_Mean #str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI] = str_Mean #str_Last
        pass
    
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNe] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeParametric_Lwr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeParametric_Upr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Lwr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Upr_CI] = str_Last
        
        '''Get the Actual colnames given generic ones '''
        #dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        #str_Group_Key_Experiment_Label = globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_2.static_Str_Colname_Ne2_Experiment_Label
        str_Group_Key_RunID = str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Stats_Category_Code = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
        #str_Group_Key_Stats_Category = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category
        str_Group_Key_Batch =  str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate =  str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Mating_Count_Replicate_Total =  str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_LDNe_PCrit = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        #str_Col_Name_Experiment_Label = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Experiment_Label)
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Stats_Category_Code = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category_Code)
        #str_Col_Name_Stats_Category = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_LDNe_PCrit = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_LDNe_PCrit)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Calculate(df)
        #df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Calculate_Inf_Counts(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Embryo_Parent_Ne_Stats_Post_Fertilization + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_2.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_floatLDNe_Harmonic_Mean] = 'func'
        
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI_Inf_Count] = 'sum'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Ne2_LDNe__Composite_EOR_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF       
        
        return df 
    
    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Calculate(self, df):
        
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get Burrows rSquared LDNe    
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''  
        str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
        str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected

        ''' Get Colname from key '''
        str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
        str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)

        ''' New Colnames '''
        str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
        str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe

        with SSAnalysisHandler() as obj_SSAnalysis:
            df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
            df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
        pass
        
        return df

    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Calculate_Inf_Counts(self, df):

        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Count Inf's    
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''  
        str_Colname_Ne2_floatLDNe = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe
        str_Colname_Ne2_floatLDNeParametric_Lwr_CI = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI
        str_Colname_Ne2_floatLDNeParametric_Upr_CI = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI
        str_Colname_Ne2_floatLDNeJackknife_Lwr_CI = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI
        str_Colname_Ne2_floatLDNeJackknife_Upr_CI = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI
        
        ''' Get Colname from key '''
        str_Colname_Ne2_floatLDNe = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_Ne2_floatLDNe)
        str_Colname_Ne2_floatLDNeParametric_Lwr_CI = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_Ne2_floatLDNeParametric_Lwr_CI)
        str_Colname_Ne2_floatLDNeParametric_Upr_CI = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_Ne2_floatLDNeParametric_Upr_CI)
        str_Colname_Ne2_floatLDNeJackknife_Lwr_CI = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_Ne2_floatLDNeJackknife_Lwr_CI)
        str_Colname_Ne2_floatLDNeJackknife_Upr_CI = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_Ne2_floatLDNeJackknife_Upr_CI)
        
        ''' New Colnames '''
        str_Colname_Ne2_Inf_Count_floatLDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNe
        str_Colname_Ne2_Inf_Count_floatLDNeParametric_Lwr_CI = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeParametric_Lwr_CI
        str_Colname_Ne2_Inf_Count_floatLDNeParametric_Upr_CI = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeParametric_Upr_CI
        str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Lwr_CI = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Lwr_CI
        str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Upr_CI = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Upr_CI

        '''
        -------------------------
        Perform GroupBy
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Embryo_Parent_Ne_Stats_Post_Fertilization + '_'
        str_Group_Key_RunID = str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Stats_Category_Code = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
        str_Group_Key_Batch =  str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate =  str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Mating_Count_Replicate_Total =  str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_LDNe_PCrit = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Stats_Category_Code = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category_Code)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_LDNe_PCrit = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_LDNe_PCrit)
 
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        
        bool_Use_NaNs = False
        if bool_Use_NaNs:
            ''' Exchange inf's for Nan's '''
            #df.replace([numpy.inf, -numpy.inf], numpy.nan)
            df = df.replace([float('inf')], numpy.nan)
        pass

        bool_Use_Infs = True
        if bool_Use_Infs:
            df = df.replace([float('inf')], numpy.inf)
            df = df.replace([-float('inf')], -numpy.inf)
        pass
    
        ''' replace JK CI = 0 with PM CI ''' 
        #cond = df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] == float(0)
        df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI][df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] == float(-1)] = df[str_Colname_Ne2_floatLDNeParametric_Lwr_CI]
        df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI][df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI] == float(-1)] = df[str_Colname_Ne2_floatLDNeParametric_Upr_CI]
        
        ''' Perform GroupBy with count - Count negative estimates '''
        df[str_Colname_Ne2_Inf_Count_floatLDNe] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNe].transform(lambda x:(x <= 0).sum())
        
        ''' Perform GroupBy with count - Count NaN or Inf estimates '''
        if bool_Use_NaNs:
            self.obj_Log_Default.info('Grouping results for NaN counts')
            df[str_Colname_Ne2_Inf_Count_floatLDNeParametric_Lwr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeParametric_Lwr_CI].transform(lambda x:(x.isnull()).sum())
            df[str_Colname_Ne2_Inf_Count_floatLDNeParametric_Upr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeParametric_Upr_CI].transform(lambda x:(x.isnull()).sum())
            df[str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Lwr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI].transform(lambda x:(x.isnull()).sum())
            df[str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Upr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeJackknife_Upr_CI].transform(lambda x:(x.isnull()).sum())
        pass
    
        if bool_Use_Infs:
            self.obj_Log_Default.info('Grouping results for Inf counts')
            #df[str_Colname_Ne2_Inf_Count_floatLDNeParametric_Lwr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeParametric_Lwr_CI].transform(lambda x:(x == numpy.inf).sum())
            #df[str_Colname_Ne2_Inf_Count_floatLDNeParametric_Upr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeParametric_Upr_CI].transform(lambda x:(x == numpy.inf).sum())
            #df[str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Lwr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI].transform(lambda x:(x == numpy.inf).sum())
            #df[str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Upr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Upr_CI].transform(lambda x:(x == numpy.inf).sum())

            df[str_Colname_Ne2_Inf_Count_floatLDNeParametric_Lwr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeParametric_Lwr_CI].transform(lambda x:((x == numpy.inf).sum() + (x == -numpy.inf).sum()))
            df[str_Colname_Ne2_Inf_Count_floatLDNeParametric_Upr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeParametric_Upr_CI].transform(lambda x:((x == numpy.inf).sum() + (x == -numpy.inf).sum()))
            df[str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Lwr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI].transform(lambda x:((x == numpy.inf).sum() + (x == -numpy.inf).sum()))
            df[str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Upr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeJackknife_Upr_CI].transform(lambda x:((x == numpy.inf).sum() + (x == -numpy.inf).sum()))
        pass
    
#         df[str_Colname_Ne2_Inf_Count_floatLDNeParametric_Lwr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeParametric_Lwr_CI].transform(lambda x:(x == float('inf')).sum())
#         df[str_Colname_Ne2_Inf_Count_floatLDNeParametric_Upr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeParametric_Upr_CI].transform(lambda x:(x == float('inf')).sum())
#         df[str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Lwr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI].transform(lambda x:(x == float('inf')).sum())
#         df[str_Colname_Ne2_Inf_Count_floatLDNeJackknife_Upr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeJackknife_Upr_CI].transform(lambda x:(x == float('inf')).sum())

        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        
        return df
    
    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Calculate_Harmonic_Mean_LDNe(self, df):

        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get LDNe Harmonic Mean
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''' 
        str_Colname_Ne2_floatLDNe =  globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe
        str_Colname_Ne2_floatLDNeJackknife_Lwr_CI = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI
        str_Colname_Ne2_floatLDNeJackknife_Upr_CI = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI
        str_Colname_Ne2_floatLDNeParametric_Lwr_CI = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI
        str_Colname_Ne2_floatLDNeParametric_Upr_CI = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI
        
        ''' Get Colname from key '''
        str_Colname_Ne2_floatLDNe = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_Ne2_floatLDNe)
        str_Colname_Ne2_floatLDNeJackknife_Lwr_CI = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_Ne2_floatLDNeJackknife_Lwr_CI)
        str_Colname_Ne2_floatLDNeJackknife_Upr_CI = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_Ne2_floatLDNeJackknife_Upr_CI)
        str_Colname_Ne2_floatLDNeParametric_Lwr_CI = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_Ne2_floatLDNeParametric_Lwr_CI)
        str_Colname_Ne2_floatLDNeParametric_Upr_CI = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_Ne2_floatLDNeParametric_Upr_CI)
        
        #''' New Colnames '''
        #str_Colname_Ne2_floatLDNe_Harmonic_Mean = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_floatLDNe_Harmonic_Mean

        '''
        -------------------------
        Perform GroupBy
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Embryo_Parent_Ne_Stats_Post_Fertilization + '_'
        str_Group_Key_RunID = str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Stats_Category_Code = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
        str_Group_Key_Batch =  str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate =  str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Mating_Count_Replicate_Total =  str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_LDNe_PCrit = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit
         
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Stats_Category_Code = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category_Code)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_LDNe_PCrit = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_LDNe_PCrit)
  
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #bool_Pause = False
        #if bool_Pause:
        #    with globalsSS.Pause_Console() as obj_Pause:
        #        obj_Pause.method_Pause_Console()
        #    pass
        #pass
        #DEBUG_OFF
        
        ''' Exchange inf's for Nan's '''
        #df = df.replace([float('inf')], numpy.nan)
        df = df.replace([float('inf')], numpy.inf)
        df = df.replace([-float('inf')], -numpy.inf)

        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #bool_Pause = False
        #if bool_Pause:
        #    with globalsSS.Pause_Console() as obj_Pause:
        #        obj_Pause.method_Pause_Console()
        #    pass
        #pass
        #DEBUG_OFF
        
        ''' Perform GroupBy with custom function '''
        self.obj_Log_Default.info('Grouping results for Harmonic Mean  LDNe')
        with SSAnalysisHandler() as obj_SSAnalysis:
            
            bool_Method_0 = False
            if bool_Method_0:
                ''' THIS WORKS - But what about 0's and Inf's? '''
                #df[str_Colname_Ne2_floatLDNe_Harmonic_Mean] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNe].transform(lambda x: len(x) / (sum(1.0/x)))
            pass
            bool_Method_1 = False
            if bool_Method_1:
                ''' THIS WORKS BETTER - Because it can cope with 0's'''
                df[str_Colname_Ne2_floatLDNe] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNe].transform(obj_SSAnalysis.func_Get_Pandas_Dataframe_Harmonic_Mean_Including_Negatives)
                bool_Use_Harmonic_Mean_For_CIs = True
                if bool_Use_Harmonic_Mean_For_CIs:
                    df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI].transform(obj_SSAnalysis.func_Get_Pandas_Dataframe_Harmonic_Mean_Including_Negatives)
                    df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeJackknife_Upr_CI].transform(obj_SSAnalysis.func_Get_Pandas_Dataframe_Harmonic_Mean_Including_Negatives)
                    df[str_Colname_Ne2_floatLDNeParametric_Lwr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeParametric_Lwr_CI].transform(obj_SSAnalysis.func_Get_Pandas_Dataframe_Harmonic_Mean_Including_Negatives)
                    df[str_Colname_Ne2_floatLDNeParametric_Upr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeParametric_Upr_CI].transform(obj_SSAnalysis.func_Get_Pandas_Dataframe_Harmonic_Mean_Including_Negatives)
                pass
            pass
            bool_Method_2 = True
            if bool_Method_2:
                ''' THIS WORKS BEST - Because it can cope with messy data like NaN's, Inf's & 0's'''
                
                ''' All estimates - Replace 0's with positive near zero number ''' 
                float_Near_Zero = 0.000000001
                df[str_Colname_Ne2_floatLDNe] =  df[str_Colname_Ne2_floatLDNe].replace([0], float_Near_Zero)                
                df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] =  df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI].replace([0], float_Near_Zero)  
                df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI] =  df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI].replace([0], float_Near_Zero)                    
                df[str_Colname_Ne2_floatLDNeParametric_Lwr_CI] =  df[str_Colname_Ne2_floatLDNeParametric_Lwr_CI].replace([0], float_Near_Zero)                
                df[str_Colname_Ne2_floatLDNeParametric_Upr_CI] =  df[str_Colname_Ne2_floatLDNeParametric_Upr_CI].replace([0], float_Near_Zero)       
                               
#                 float_Near_Pos_Inf = 10000000.0                 
#                 df[str_Colname_Ne2_floatLDNe] =  df[str_Colname_Ne2_floatLDNe].replace([numpy.inf], float_Near_Pos_Inf) 
#                 df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] =  df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI].replace([numpy.inf], float_Near_Pos_Inf)
#                 df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI] =  df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI].replace([numpy.inf], float_Near_Pos_Inf)
#                 df[str_Colname_Ne2_floatLDNeParametric_Lwr_CI] =  df[str_Colname_Ne2_floatLDNeParametric_Lwr_CI].replace([numpy.inf], float_Near_Pos_Inf)                      
#                 df[str_Colname_Ne2_floatLDNeParametric_Upr_CI] =  df[str_Colname_Ne2_floatLDNeParametric_Upr_CI].replace([numpy.inf], float_Near_Pos_Inf)                 
#                 
#                 float_Near_Neg_Inf = -10000000.0                 
#                 df[str_Colname_Ne2_floatLDNe] =  df[str_Colname_Ne2_floatLDNe].replace([-numpy.inf], float_Near_Neg_Inf)               
#                 df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] =  df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI].replace([-numpy.inf], float_Near_Neg_Inf)
#                 df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI] =  df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI].replace([-numpy.inf], float_Near_Neg_Inf)                     
#                 df[str_Colname_Ne2_floatLDNeParametric_Lwr_CI] =  df[str_Colname_Ne2_floatLDNeParametric_Lwr_CI].replace([-numpy.inf], float_Near_Neg_Inf)                
#                 df[str_Colname_Ne2_floatLDNeParametric_Upr_CI] =  df[str_Colname_Ne2_floatLDNeParametric_Upr_CI].replace([-numpy.inf], float_Near_Neg_Inf)

                float_Near_Pos_Inf = 100000000.0  #Ne2 defines INFINITE as this 
                float_Near_Neg_Inf = -100000000.0 
                
                ''' Point estimate - Replace Inf or -Inf with relevant near inf value'''               
                df[str_Colname_Ne2_floatLDNe] =  df[str_Colname_Ne2_floatLDNe].replace([numpy.inf], float_Near_Pos_Inf)
                df[str_Colname_Ne2_floatLDNe] =  df[str_Colname_Ne2_floatLDNe].replace([-numpy.inf], float_Near_Neg_Inf)
                
                ''' Lwr CI - Replace Inf or -Inf with negative near inf '''
                df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] =  df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI].replace([numpy.inf], float_Near_Neg_Inf)
                df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] =  df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI].replace([-numpy.inf], float_Near_Neg_Inf)
                df[str_Colname_Ne2_floatLDNeParametric_Lwr_CI] =  df[str_Colname_Ne2_floatLDNeParametric_Lwr_CI].replace([numpy.inf], float_Near_Neg_Inf)                
                df[str_Colname_Ne2_floatLDNeParametric_Lwr_CI] =  df[str_Colname_Ne2_floatLDNeParametric_Lwr_CI].replace([-numpy.inf], float_Near_Neg_Inf)                
              
                ''' Upr CI - Replace Inf or -Inf with positive near inf'''                
                df[str_Colname_Ne2_floatLDNe] =  df[str_Colname_Ne2_floatLDNe].replace([-numpy.inf], float_Near_Neg_Inf)               
                df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI] =  df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI].replace([numpy.inf], float_Near_Pos_Inf)                     
                df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI] =  df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI].replace([-numpy.inf], float_Near_Pos_Inf)                     
                df[str_Colname_Ne2_floatLDNeParametric_Upr_CI] =  df[str_Colname_Ne2_floatLDNeParametric_Upr_CI].replace([numpy.inf], float_Near_Pos_Inf)
                df[str_Colname_Ne2_floatLDNeParametric_Upr_CI] =  df[str_Colname_Ne2_floatLDNeParametric_Upr_CI].replace([-numpy.inf], float_Near_Pos_Inf)
              

                #DEBUG_ON
                #str_Df = df.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #bool_Pause = False
                #if bool_Pause:
                #    with globalsSS.Pause_Console() as obj_Pause:
                #        obj_Pause.method_Pause_Console()
                #    pass
                #pass
                #DEBUG_OFF
                
                ''' Point estimate - Calc harmonic mean '''        
                df[str_Colname_Ne2_floatLDNe] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNe].transform(obj_SSAnalysis.func_Get_Pandas_Dataframe_Harmonic_Mean_Including_Negatives)
                
                bool_Use_Harmonic_Mean_For_CIs = True
                if bool_Use_Harmonic_Mean_For_CIs:
                    ''' CI's - Calc harmnic mean '''
                    df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI].transform(obj_SSAnalysis.func_Get_Pandas_Dataframe_Harmonic_Mean_Including_Negatives)
                    df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeJackknife_Upr_CI].transform(obj_SSAnalysis.func_Get_Pandas_Dataframe_Harmonic_Mean_Including_Negatives)
                    df[str_Colname_Ne2_floatLDNeParametric_Lwr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeParametric_Lwr_CI].transform(obj_SSAnalysis.func_Get_Pandas_Dataframe_Harmonic_Mean_Including_Negatives)
                    df[str_Colname_Ne2_floatLDNeParametric_Upr_CI] = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False)[str_Colname_Ne2_floatLDNeParametric_Upr_CI].transform(obj_SSAnalysis.func_Get_Pandas_Dataframe_Harmonic_Mean_Including_Negatives)
                pass
            
            
                ''' Clean up dataset '''
                ''' Upr CI - Replace positive near inf with Nan'''                

                ''' For some reason the actual values can be slightly less by ~0.0001 than exactly float_Near_Pos_Inf, so we look for a slightly smaller value'''
                float_Almost_Near_Pos_Inf = float_Near_Pos_Inf-1
                float_Almost_Near_Neg_Inf = float_Near_Neg_Inf+1
                
                ''' This works but is hard to debug '''
                #df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI][df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI] >= float(float_Almost_Near_Pos_Inf)] = numpy.nan     
                #df[str_Colname_Ne2_floatLDNeParametric_Upr_CI][df[str_Colname_Ne2_floatLDNeParametric_Upr_CI] >= float(float_Almost_Near_Pos_Inf)] = numpy.nan     

                ''' This works but is easier to debug - put a break point on the .loc and look at the row_index values for True or False '''
                row_index = df[str_Colname_Ne2_floatLDNeJackknife_Upr_CI] > float(float_Almost_Near_Pos_Inf)
                # then with the form .loc[row_indexer,col_indexer]
                df.loc[row_index, str_Colname_Ne2_floatLDNeJackknife_Upr_CI] = numpy.nan
                 
                row_index = df[str_Colname_Ne2_floatLDNeParametric_Upr_CI] > float(float_Almost_Near_Pos_Inf)
                # then with the form .loc[row_indexer,col_indexer]
                df.loc[row_index, str_Colname_Ne2_floatLDNeParametric_Upr_CI] = numpy.nan
                
                row_index = df[str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] < float(float_Almost_Near_Neg_Inf)
                # then with the form .loc[row_indexer,col_indexer]
                df.loc[row_index, str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] = numpy.nan
                 
                row_index = df[str_Colname_Ne2_floatLDNeParametric_Lwr_CI] < float(float_Almost_Near_Neg_Inf)
                # then with the form .loc[row_indexer,col_indexer]
                df.loc[row_index, str_Colname_Ne2_floatLDNeParametric_Lwr_CI] = numpy.nan
                
            pass
        pass
    
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #bool_Pause = False
        #if bool_Pause:
        #    with globalsSS.Pause_Console() as obj_Pause:
        #        obj_Pause.method_Pause_Console()
        #    pass
        #pass
        #DEBUG_OFF
        
        return df

    '''
    -------------------------------------------------------------
    EXPERIMENT_Parent_Offspring_Ne_2 - Cumulative Results - MERGE NE2 & SAMPLING STATS to Categorise Ne2 results
    -------------------------------------------------------------
    '''
    def func_EXPERIMENT_Parent_Offspring_Ne_2__PS_Cumulative_Results__Aggregate_Results(self, str_Excel_Save_Path, str_Search_Path):

        boolSuccess = False
       
        '''
        Process Results
        '''
        ''' Output file '''
#         str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Ne2_LDNe__Cumulative_EOR_Results
#         str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__Ne2_LDNe__Cumulative_EOR_Results
#         str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Cumulative_EOR_Results
        str_Excel_Output_Colname_Prefix = None
        str_Excel_Output_FileName =  None
        str_Excel_Output_Sheet_Name = None

        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_Colname_Prefix

        #str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
 
        '''
        Aggregate Excel Data to dataframe from each input file
        '''
        ''' Input file 1 '''
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__Ne2_LDNe__Raw_EOR_Results + '*.xlsx'
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Raw_EOR_Results
        str_File_Search_Pattern = str_Input_FileName
        
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName) 
               
        bool_File_1_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_1_Located:
            
            '''Process Results'''
            list_DF_1s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_1s.append(df_1)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_1s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            df1 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

 
        '''
        Aggregate Excel Data to dataframe from each input file
        '''
        ''' Input file 2 '''
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__SAMPLING_INDIVS__Aggregate_Results + '*.xlsx'
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__SAMPLING_INDIVS__Aggregate_Results
        str_File_Search_Pattern = str_Input_FileName
        
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName) 
               
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_2 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_2s.append(df_2)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
            
            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join & Transform the dataframes
            '''
            list_DFs = [df1, df2]
            df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Cumulative_Results__Aggregated_Dataframes__Process(list_DFs)            
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
        pass
                
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name, list_Columns_To_Write=[], bool_NaN_As_NA = True)                
        pass
    
        ''' final save of the excel file '''
        if bool_File_1_Located and bool_File_2_Located:
            self.func_Save_Excel_Writer(writer)
            boolSuccess = True
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Cumulative_Results__Aggregated_Dataframes__Process(self, list_DFs):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Join Dataframes
        ---------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Cumulative_Results__Merge(list_DFs)
        
        '''
        Add calculations
        '''
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Cumulative_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
 
    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Cumulative_Results__Merge(self, list_DFs):


        self.obj_Log_Default.info('Merge Dataframes')
        
        df_Ne2_LDNe_Raw, df_Sampling_Indivs = list_DFs[0], list_DFs[1]
        '''
        -------------------------
        Get just the records to merge
        -------------------------
        '''
        ''' Specify key to get colname for '''
        str_Source_VSP_Ages_And_Sizes__Ages = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_VSP_Ages_And_Sizes__Ages
        ''' Get Colname from key '''
        str_Col_Name_Source_VSP_Ages_And_Sizes__Ages = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df_Sampling_Indivs, str_Source_VSP_Ages_And_Sizes__Ages)
        
        df_Sampling_Indivs_Subset = df_Sampling_Indivs[df_Sampling_Indivs[str_Col_Name_Source_VSP_Ages_And_Sizes__Ages]==1]
        
        '''
        -------------------------
        Specify Key Colnames to merge on
        -------------------------
        '''
        #strKey1 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
        list_Keys = [globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total
                     ,globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
                     ,globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicates
                     ,globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit
                     #,globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicate_Filename
                     ]

        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        str_Join_How = 'left'
        df = self.func_Merge_Dataframes_By_Key_List(str_Join_How, df_Ne2_LDNe_Raw, df_Sampling_Indivs_Subset, list_Keys)

        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF 
        
        return df
    
    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Cumulative_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')

        '''
        -------------------------
        Pre-aggregation Calculations
        -------------------------
        '''
        #df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Cumulative_Results__Calculate_Inf_Counts(df)        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean


#         str_Source_File_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__SAMPLING_INDIVS__Aggregate_Results + '_'
#         #str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_Strategy_Results
#         
#         '''Common experiment colnames'''
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
#         dict_Columns_Required_Plus_Function[str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
#         
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
#         dict_Columns_Required_Plus_Function[str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
#         #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_MatingsToSimulate] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_MatingsToSimulatePerReplicate] = str_Last
# 
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
# 
#         ''' Indiv sampling experiment fields '''
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code] = str_Last
#         #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
#         #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
#         #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category] = str_Last
#         #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_strPCritsToProcess] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Search_Path] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sample_Each_Mating_Count_Divisible_By] = str_Last
# 
#         #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Pop_Sampling.static_Str_Colname_Sampling_Params] = str_Last
# 
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
#         #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
#         #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Categories] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Indiv_Number] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Loci_Number] = str_Last
#         
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicates] = str_Last 
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicate_Filename] = str_Last 
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_VSP_Ages_And_Sizes__Ages] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_VSP_Ages_And_Sizes__Sizes] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sample_VSP_Ages_And_Sizes__Sizes] = str_Last
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sample_Percent_VSP_Ages_And_Sizes__Sizes] = str_Last



        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__SAMPLING_INDIVS__Aggregate_Results + '_'        
        #str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Embryo_Parent_Ne_Stats_Post_Fertilization + '_'
        '''EXPERIMENT_Parent_Offspring_Ne_2 Colnames '''
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_2.static_Str_Colname_LDNe_PCrit] = str_Last

        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last

        ''' Colnames_SAMPLINING_INDIVS '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Indiv_Number] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Loci_Number] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicates] = str_Last 
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicate_Filename] = str_Last 
                
        '''Colnames Ne2 Output '''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeLoci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeSamples] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_strPopID] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intMatingScheme] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intIndependentAlleles] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatWeightedMeanSampleSize] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI] = str_Last

       
        '''Get the Actual colnames given generic ones '''
        #dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        #str_Group_Key_Experiment_Label = globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_2.static_Str_Colname_Ne2_Experiment_Label
        str_Group_Key_RunID = str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Stats_Category_Code = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
        #str_Group_Key_Stats_Category = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category
        str_Group_Key_Batch =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Mating_Count_Replicate_Total =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_LDNe_PCrit = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit
        #str_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Raw_EOR_Results        
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        #str_Col_Name_Experiment_Label = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Experiment_Label)
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Stats_Category_Code = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category_Code)
        #str_Col_Name_Stats_Category = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_LDNe_PCrit = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_LDNe_PCrit)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Cumulative_Results__Calculate(df)
        #df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Cumulative_Results__Calculate_Inf_Counts(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Embryo_Parent_Ne_Stats_Post_Fertilization + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_2.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        dict_New_Colnames['PD_INDEX'] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
        
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI_Inf_Count] = 'sum'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        #str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Ne2_LDNe__Cumulative_EOR_Results
        str_Colname_Prefix_1 = None
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF       
        
        return df 
    
    '''
    -------------------------------------------------------------
    EXPERIMENT_Parent_Offspring_Ne_2 - Categorised Results - MERGE NE2 & SAMPLING STATS to Categorise Ne2 results
    -------------------------------------------------------------
    '''
    def func_EXPERIMENT_Parent_Offspring_Ne_2__PS_Categorised_Results__Aggregate_Results(self, str_Excel_Save_Path, str_Search_Path):

        boolSuccess = False
       
        '''
        Process Results
        '''
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Ne2_LDNe__Categorised_EOR_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__Ne2_LDNe__Categorised_EOR_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Categorised_EOR_Results

        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_Colname_Prefix

        #str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
 
        '''
        Aggregate Excel Data to dataframe from each input file
        '''
        ''' Input file 1 '''
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__Ne2_LDNe__Raw_EOR_Results + '*.xlsx'
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Raw_EOR_Results
        str_File_Search_Pattern = str_Input_FileName
        
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName) 
               
        bool_File_1_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_1_Located:
            
            '''Process Results'''
            list_DF_1s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_1s.append(df_1)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_1s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            df1 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

 
        '''
        Aggregate Excel Data to dataframe from each input file
        '''
        ''' Input file 2 '''
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__SAMPLING_INDIVS__Aggregate_Results + '*.xlsx'
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__SAMPLING_INDIVS__Aggregate_Results
        str_File_Search_Pattern = str_Input_FileName
        
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName) 
               
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_2 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_2s.append(df_2)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
            
            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join & Transform the dataframes
            '''
            list_DFs = [df1, df2]
            df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Categorised_Results__Aggregated_Dataframes__Process(list_DFs)            
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
        pass
                
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name, list_Columns_To_Write=[], bool_NaN_As_NA = True)                
        pass
    
        ''' final save of the excel file '''
        if bool_File_1_Located and bool_File_2_Located:
            self.func_Save_Excel_Writer(writer)
            boolSuccess = True
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Categorised_Results__Aggregated_Dataframes__Process(self, list_DFs):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Join Dataframes
        ---------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Categorised_Results__Merge(list_DFs)
        
        '''
        Add calculations
        '''
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Categorised_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
 
    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Categorised_Results__Merge(self, list_DFs):


        self.obj_Log_Default.info('Merge Dataframes')
        
        df_Ne2_LDNe_Raw, df_Sampling_Indivs = list_DFs[0], list_DFs[1]
        '''
        -------------------------
        Get just the records to merge
        -------------------------
        '''
        ''' Specify key to get colname for '''
        str_Source_VSP_Ages_And_Sizes__Ages = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_VSP_Ages_And_Sizes__Ages
        ''' Get Colname from key '''
        str_Col_Name_Source_VSP_Ages_And_Sizes__Ages = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df_Sampling_Indivs, str_Source_VSP_Ages_And_Sizes__Ages)
        
        df_Sampling_Indivs_Subset = df_Sampling_Indivs[df_Sampling_Indivs[str_Col_Name_Source_VSP_Ages_And_Sizes__Ages]==1]
        
        '''
        -------------------------
        Specify Key Colnames to merge on
        -------------------------
        '''
        #strKey1 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
        list_Keys = [
                     #globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total
                     globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Last_Mating_In_Replicate
                     ,globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
                     ,globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicates
                     ,globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit
                     #,globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicate_Filename
                     ]

        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        str_Join_How = 'left'
        df = self.func_Merge_Dataframes_By_Key_List(str_Join_How, df_Ne2_LDNe_Raw, df_Sampling_Indivs_Subset, list_Keys)

        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF 
        
        return df
    
    def func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Categorised_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')

        '''
        -------------------------
        Pre-aggregation Calculations
        -------------------------
        '''
        #df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Categorised_Results__Calculate_Inf_Counts(df)        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean

        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__SAMPLING_INDIVS__Aggregate_Results + '_'        
        #str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Embryo_Parent_Ne_Stats_Post_Fertilization + '_'
        '''EXPERIMENT_Parent_Offspring_Ne_2 Colnames '''
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_2.static_Str_Colname_LDNe_PCrit] = str_Last

        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_Data_Sim_Current_File] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last

        ''' Colnames_SAMPLINING_INDIVS '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Indiv_Number] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Loci_Number] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicates] = str_Last 
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicate_Filename] = str_Last 
                
        '''Colnames Ne2 Output '''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeLoci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeSamples] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_strPopID] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intMatingScheme] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intIndependentAlleles] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatWeightedMeanSampleSize] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI] = str_Last

       
        '''Get the Actual colnames given generic ones '''
        #dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        #str_Group_Key_Experiment_Label = globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_2.static_Str_Colname_Ne2_Experiment_Label
        str_Group_Key_RunID = str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Stats_Category_Code = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
        #str_Group_Key_Stats_Category = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category
        str_Group_Key_Batch =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        #str_Group_Key_Mating_Count_Replicate_Total =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_Sim_Last_Mating_In_Replicate =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Last_Mating_In_Replicate
        str_Group_Key_Sampling_Replicates =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicates
        str_Group_Key_LDNe_PCrit = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit
        #str_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Raw_EOR_Results        
        str_Group_Key_PD_Index = 'PD_INDEX' 
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        #str_Col_Name_Experiment_Label = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Experiment_Label)
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Stats_Category_Code = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category_Code)
        #str_Col_Name_Stats_Category = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category)
        #str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        #str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        #str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_Sim_Last_Mating_In_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sim_Last_Mating_In_Replicate)
        str_Col_Name_Sampling_Replicates = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sampling_Replicates)
        str_Col_Name_LDNe_PCrit = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_LDNe_PCrit)
        #str_Col_Name_PD_Index = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_PD_Index)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        #df = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_LDNe_PCrit], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Stats_Category_Code, str_Col_Name_Sim_Last_Mating_In_Replicate, str_Col_Name_Sampling_Replicates, str_Col_Name_LDNe_PCrit], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
        #df = df.groupby([str_Col_Name_PD_Index], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Categorised_Results__Calculate(df)
        #df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__PS_Categorised_Results__Calculate_Inf_Counts(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Embryo_Parent_Ne_Stats_Post_Fertilization + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_2.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Last_Mating_In_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicates] = str_Last
        dict_New_Colnames[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
        #dict_New_Colnames['PD_INDEX'] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
        
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI_Inf_Count] = 'sum'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Ne2_LDNe__Categorised_EOR_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF       
        
        return df 
    
    '''
    -------------------------------------------------------------
    EXPERIMENT_Parent_Offspring_Ne_2 -  Categorised NE2 Results POST SIM PER FERTILIZATION  Results to AGGREGATE
    -------------------------------------------------------------
    '''   
    def func_EXPERIMENT_Parent_Offspring_Ne_2__Ne2_PS_PF_Results__Aggregate_Results(self, str_Excel_Save_Path, str_Search_Path):

        boolSuccess = False
       
        '''
        Process Results
        '''
        
        ''' Input file '''
        str_File_Search_Pattern = '*' + globalsSS.Ne2_LDNe_Results_Details.static_File_Suffix__Ne2_LDNe_TAB_File_Results
        
        ''' Output file '''
#         str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PS_PF_Results
#         str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PS_PF_Results
#         str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PS_PF_Results
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Ne2_LDNe__Raw_EOR_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__Ne2_LDNe__Raw_EOR_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Raw_EOR_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_Colname_Prefix

        #str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
        str_Excel_Output_Path_And_File_Name = str_Excel_Save_Path + '\\' + str_Excel_Output_File_WO_Suffix + '.xlsx'
 
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName)
        
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
            
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__EXPERIMENT_Parent_Offspring_Ne_2__Ne2_PS_PF_Results__Aggregate__Process(str_Path_And_File)
                list_DFs.append(df)
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 

            str_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Raw_EOR_Results        
            df.index.name = str_Colname_Prefix + '_' + 'PD_INDEX'        
                
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #with globalsSS.Pause_Console() as obj_Pause:
            #    obj_Pause.method_Pause_Console()
            #pass
            #DEBUG_OFF
        
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name, list_Columns_To_Write=[], bool_NaN_As_NA = True)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Debug_Display.debug('Excel file written: ' + str_Excel_Output_Path_And_File_Name)
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written:'  + str_Excel_Output_Path_And_File_Name)
        else:
            self.obj_Log_Default.error('Some results files could not be located.  No Excel file written: '  + str_Excel_Output_Path_And_File_Name)
            boolSuccess = False
        pass
        
        return boolSuccess
    
    def func__EXPERIMENT_Parent_Offspring_Ne_2__Ne2_PS_PF_Results__Aggregate__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''
        
        str_Ne2_Version = self.objSSParametersLocal.str_Sampling_Strategy_Run_Ne_Estimator_External_Process_Version
        
        #DEBUG_ON
        #str_Ne2_Version = '2_0_0'
        #str_Ne2_Version = '2_0_1'
        #str_Ne2_Version = '2_1_0'
        #DEBUG_OFF
        
        if str_Ne2_Version == globalsSS.Shared_External_Resources.static_Win_Binary_Exe_NE_ESTIMATOR_Version_2_0_0 \
        or str_Ne2_Version == globalsSS.Shared_External_Resources.static_Win_Binary_Exe_NE_ESTIMATOR_Version_2_0_1 :
                    
            df = self.func__EXPERIMENT_Parent_Offspring_Ne_2_0__Ne2_PS_PF_Results__Aggregate_Input_File_To_Dataframe(str_Path_And_File)
        pass
    
        if str_Ne2_Version == globalsSS.Shared_External_Resources.static_Win_Binary_Exe_NE_ESTIMATOR_Version_2_1_0:
                    
            df = self.func__EXPERIMENT_Parent_Offspring_Ne_2_1__Ne2_PS_PF_Results__Aggregate_Input_File_To_Dataframe(str_Path_And_File)
        pass
        
        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)
        
        return df 

    def func__EXPERIMENT_Parent_Offspring_Ne_2_0__Ne2_PS_PF_Results__Aggregate_Input_File_To_Dataframe(self, str_Path_And_File):

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()
        pass            

        self.obj_Log_Debug_Display.debug('Aggregating Ne2 LDNe TAB file to dataframe: ' + str_Path_And_File)

        str_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Raw_EOR_Results
        '''Process Results'''
        list_File_Header_Colnames = [
                                     str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Genepop_Source_File
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeLoci
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_strPopID
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeSamples
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatWeightedMeanSampleSize
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intIndependentAlleles
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI
                                     ]       


        ''' Replace Infinite with inf using converters on the pandas.read_csv'''
        def func_Conv_Col_To_Float(x):
                
            float_Value = 0.0
            
            try:
                float_Value = float(x)
            except:
                #float_Value = -1*float('inf')
                if 'Infinite' in x:
                    float_Value = float('inf')
                pass
                if '*' in x: # * indicates that the JK CI's are the same as the PM CIs I think
                    float_Value = float(-1)
                pass
            pass
        
            return float_Value
        
        ''' Specify cols to convert '''
        dict_Converters = {
                         str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe:func_Conv_Col_To_Float
                        ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI:func_Conv_Col_To_Float
                        ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI:func_Conv_Col_To_Float
                        ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI:func_Conv_Col_To_Float
                        ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI:func_Conv_Col_To_Float                           
                          }
       
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Import Ne2 LDNe TAB file
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''                                    
        df = pandas.read_csv(str_Path_And_File, sep='\t', converters=dict_Converters, header=None, skiprows=11, names=list_File_Header_Colnames, skipfooter=7, engine='python')

        
        ''' Get column values from input filename '''
        str_Ne2_LDNe_PCrit = str_Path_And_File.split('x')[0]
        str_Ne2_LDNe_PCrit = str_Ne2_LDNe_PCrit.split('PC')[1]
        int_Ne2_LDNe_PCrit = int(str_Ne2_LDNe_PCrit)
        if int_Ne2_LDNe_PCrit < 10:
            str_Ne2_LDNe_PCrit = '0.0' + str_Ne2_LDNe_PCrit
            float_Ne2_LDNe_PCrit = float(str_Ne2_LDNe_PCrit)
        else:
            str_Ne2_LDNe_PCrit = '0.' + str_Ne2_LDNe_PCrit
            float_Ne2_LDNe_PCrit = float(str_Ne2_LDNe_PCrit)            
        pass
        ''' add it to the df '''
        df[str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = float_Ne2_LDNe_PCrit
        
        self.obj_Log_Debug_Display.debug('Added column to dataframe: ' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit + ' of value: ' + str(float_Ne2_LDNe_PCrit))

        ''' Split Stst cat Code, Sim Mating Count and Replicate Count from the genepop filename in the df '''
        df_Temp = df[str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Genepop_Source_File].str[1:-1].str.split('_').apply(pandas.Series)
        
#         df_Temp[4] = df_Temp[4].astype(float)
#         df_Temp[4] = df_Temp[4].astype(int)
#         df_Temp[3] = df_Temp[3].astype(int)
#         df_Temp.drop(0, axis=1, inplace=True)
#         df_Temp.drop(1, axis=1, inplace=True)
        '''Check if Stat_Cat_Code is a string or an int - if int save as int '''
        try:
            df_Temp[1].astype(int)
        except ValueError:
            df_Temp[1].astype(str)
        pass
        ''' Set type of other values '''
        df_Temp[3] = df_Temp[3].astype(float)
        df_Temp[3] = df_Temp[3].astype(int)
        df_Temp[2] = df_Temp[2].astype(int)
        df_Temp.drop(0, axis=1, inplace=True)
        
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get Experiment details from Experiment Stat Category Code
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
#         if len(self.objSSParametersLocal.dict_Ne2_Sampling_Experiment_Category_By_Key_Category_Code) == -1: #Disablieng this temp    #> 0:
#             dict_Ne2_Sampling_Category_By_Key_Category_Code = OrderedDict(self.objSSParametersLocal.dict_Ne2_Sampling_Experiment_Category_By_Key_Category_Code)
#             df_Temp[4] = df_Temp[1].map(dict_Ne2_Sampling_Category_By_Key_Category_Code)
#             dict_Ne2_Sampling_Experiment_Label_By_Key_Category = OrderedDict(self.objSSParametersLocal.dict_Ne2_Sampling_Experiment_Label_By_Key_Category)
#             df_Temp[5] = df_Temp[4].map(dict_Ne2_Sampling_Experiment_Label_By_Key_Category)
#     
#             df_Temp.columns = [
#                                str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
#                                ,str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total
#                                ,str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples
#                                ,str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category
#                                ,str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label
#                                ]
#         pass
    
        df_Temp.columns = [
                           str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
                           #,str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total
                           ,str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Last_Mating_In_Replicate
                           ,str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples
                           ]
        pass
        #df_Temp.columns = [globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code,globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total,globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples]        
        df_New = pandas.concat((df_Temp, df), axis=1)
        
        df = df_New
        
        #DEBUG_ON
        if globalsSS.Logger_Debug_Display.bool_Debug_Display:
            #str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
            obj_Debug_Loc = Debug_Location()
            str_Message_Location = obj_Debug_Loc.Get_Debug_Location()
            str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
            self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe: %s' % str_Df)
            #pdb.set_trace()
            #with globalsSS.Pause_Console() as obj_Pause:
            #    obj_Pause.method_Pause_Console(str_Message_Location)
            #pass
        pass
                    
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
            #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            #    t2 = Timer2(True)
            #    t2.Start()
            #pass                    
        pass
                    
        return df   
    
    def func__EXPERIMENT_Parent_Offspring_Ne_2_1__Ne2_PS_PF_Results__Aggregate_Input_File_To_Dataframe(self, str_Path_And_File):

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()
        pass            

        self.obj_Log_Debug_Display.debug('Aggregating Ne2 LDNe TAB file to dataframe: ' + str_Path_And_File)

        str_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Ne2_LDNe__Raw_EOR_Results
        '''Process Results'''
        list_File_Header_Colnames = [
                                     str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Genepop_Source_File
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeLoci
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_strPopID
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeSamples
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatWeightedMeanSampleSize
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intIndependentAlleles
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_CI_Eff_DF
                                     ]       


        ''' Replace Infinite with inf using converters on the pandas.read_csv'''
        def func_Conv_Col_To_Float(x):
                
            float_Value = 0.0
            
            try:
                float_Value = float(x)
            except:
                #float_Value = -1*float('inf')
                if 'Infinite' in x:
                    float_Value = float('inf')
                pass
                if '*' in x: # * indicates that the JK CI's are the same as the PM CIs I think
                    float_Value = float(-1)
                pass
            pass
        
            return float_Value
        
        ''' Specify cols to convert '''
        dict_Converters = {
                         str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe:func_Conv_Col_To_Float
                        ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI:func_Conv_Col_To_Float
                        ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI:func_Conv_Col_To_Float
                        ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI:func_Conv_Col_To_Float
                        ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI:func_Conv_Col_To_Float                           
                        ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_CI_Eff_DF:func_Conv_Col_To_Float                           
                          }
       

        ''' Get PCrit column values from input filename '''
        str_Ne2_LDNe_PCrit = str_Path_And_File.split('x')[0]
        str_Ne2_LDNe_PCrit = str_Ne2_LDNe_PCrit.split('PC')[1]
        ''' Check if string is a NUMERIC PCrit '''
        bool_IsNumeric = False
        try:
            int_Ne2_LDNe_PCrit = int(str_Ne2_LDNe_PCrit)
            bool_IsNumeric = True
        except ValueError:
            bool_IsNumeric = False
        pass

        if bool_IsNumeric:
            if int_Ne2_LDNe_PCrit < 10:
                str_Ne2_LDNe_PCrit = '0.0' + str_Ne2_LDNe_PCrit
                float_Ne2_LDNe_PCrit = float(str_Ne2_LDNe_PCrit)
            else:
                str_Ne2_LDNe_PCrit = '0.' + str_Ne2_LDNe_PCrit
                float_Ne2_LDNe_PCrit = float(str_Ne2_LDNe_PCrit)            
            pass    
        else:
            ''' No Singletons PCrit option (Ne2 PCrit option = 1)'''
            str_Ne2_LDNe_PCrit = globalsSS.Ne2Bulk_Processing.static_stringNe2Bulk_PCrit_To_Process_PCrit_NoS
            float_Ne2_LDNe_PCrit = float(globalsSS.LDNe_PCrit__Float.static_float_LDNe_PCrit_NoS)
        pass

   
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Import Ne2 LDNe TAB file
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        if str_Ne2_LDNe_PCrit == globalsSS.Ne2Bulk_Processing.static_stringNe2Bulk_PCrit_To_Process_PCrit_NoS:
            ''' No Singleton PCrit option (Ne2 PCrit option = 1) - Has an extra header line'''
            df = pandas.read_csv(str_Path_And_File, sep='\t', converters=dict_Converters, header=None, skiprows=12, names=list_File_Header_Colnames, skipfooter=7, engine='python')
        else:
            df = pandas.read_csv(str_Path_And_File, sep='\t', converters=dict_Converters, header=None, skiprows=11, names=list_File_Header_Colnames, skipfooter=7, engine='python')
        pass

        ''' add PCrit to the df '''
        df[str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = float_Ne2_LDNe_PCrit
        
        self.obj_Log_Debug_Display.debug('Added column to dataframe: ' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit + ' of value: ' + str(float_Ne2_LDNe_PCrit))

        ''' Split Stst cat Code, Sim Mating Count and Replicate Count from the genepop filename in the df '''
        df_Temp = df[str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Genepop_Source_File].str[1:-1].str.split('_').apply(pandas.Series)
        
#         df_Temp[4] = df_Temp[4].astype(float)
#         df_Temp[4] = df_Temp[4].astype(int)
#         df_Temp[3] = df_Temp[3].astype(int)
#         df_Temp.drop(0, axis=1, inplace=True)
#         df_Temp.drop(1, axis=1, inplace=True)
        '''Check if Stat_Cat_Code is a string or an int - if int save as int '''
        try:
            df_Temp[1].astype(int)
        except ValueError:
            df_Temp[1].astype(str)
        pass
        ''' Set type of other values '''
        df_Temp[3] = df_Temp[3].astype(float)
        df_Temp[3] = df_Temp[3].astype(int)
        df_Temp[2] = df_Temp[2].astype(int)
        df_Temp.drop(0, axis=1, inplace=True)
        
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get Experiment details from Experiment Stat Category Code
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
#         if len(self.objSSParametersLocal.dict_Ne2_Sampling_Experiment_Category_By_Key_Category_Code) == -1: #Disablieng this temp    #> 0:
#             dict_Ne2_Sampling_Category_By_Key_Category_Code = OrderedDict(self.objSSParametersLocal.dict_Ne2_Sampling_Experiment_Category_By_Key_Category_Code)
#             df_Temp[4] = df_Temp[1].map(dict_Ne2_Sampling_Category_By_Key_Category_Code)
#             dict_Ne2_Sampling_Experiment_Label_By_Key_Category = OrderedDict(self.objSSParametersLocal.dict_Ne2_Sampling_Experiment_Label_By_Key_Category)
#             df_Temp[5] = df_Temp[4].map(dict_Ne2_Sampling_Experiment_Label_By_Key_Category)
#     
#             df_Temp.columns = [
#                                str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
#                                ,str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total
#                                ,str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples
#                                ,str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category
#                                ,str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label
#                                ]
#         pass
    
        df_Temp.columns = [
                           str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code
                           #,str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total
                           ,str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Last_Mating_In_Replicate
                           ,str_Colname_Prefix + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples
                           ]
        pass
        #df_Temp.columns = [globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code,globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total,globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Random_SubSamples]        
        df_New = pandas.concat((df_Temp, df), axis=1)
        
        df = df_New
        
        #DEBUG_ON
        if globalsSS.Logger_Debug_Display.bool_Debug_Display:
            #str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
            obj_Debug_Loc = Debug_Location()
            str_Message_Location = obj_Debug_Loc.Get_Debug_Location()
            str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
            self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe: %s' % str_Df)
            #pdb.set_trace()
            #with globalsSS.Pause_Console() as obj_Pause:
            #    obj_Pause.method_Pause_Console(str_Message_Location)
            #pass
        pass
                    
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
            #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            #    t2 = Timer2(True)
            #    t2.Start()
            #pass                    
        pass
                    
        return df   
   
    '''
    -------------------------------------------------------------
    LOCUS_JACKNIFING_Ne2Bulk -  LOCUS_JACKNIFING_Ne2Bulk Results to AGGREGATE
    -------------------------------------------------------------
    '''   
    def func_LOCUS_JACKNIFING_Ne2Bulk_Results__Aggregate_Results(self, str_Search_Path):

        boolSuccess = False
       
        '''
        Process Results
        '''
        
        ''' Input file '''
        str_File_Search_Pattern = '*' + globalsSS.Ne2_LDNe_Results_Details.static_File_Suffix__Ne2_LDNe_TAB_File_Results
        
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__func_LOCUS_JACKNIFING_Ne2Bulk_Results__Aggregate_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__func_LOCUS_JACKNIFING_Ne2Bulk_Results__Aggregate_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__func_LOCUS_JACKNIFING_Ne2Bulk_Results__Aggregate_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName + '_' + str_Excel_Output_Colname_Prefix
        writer = self.func_Get_Excel_Writer(str_Search_Path, str_Excel_Output_File_WO_Suffix)
        str_Excel_Output_Path_And_File_Name = str_Search_Path + '\\' + str_Excel_Output_File_WO_Suffix + '.xlsx'
 
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName)
        
        ''' Locate input files '''
        bool_File_Located = False
        with FileHandler() as obj_FileHandler:
            bool_File_Located, list_Path_And_Files = obj_FileHandler.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        pass
    
        if bool_File_Located:
            
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__LOCUS_JACKNIFING_Ne2Bulk_Results__Aggregate__Process(str_Path_And_File)
                list_DFs.append(df)
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #with globalsSS.Pause_Console() as obj_Pause:
            #    obj_Pause.method_Pause_Console()
            #pass
            #DEBUG_OFF
        
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Debug_Display.debug('Excel file written: ' + str_Excel_Output_Path_And_File_Name)
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written:'  + str_Excel_Output_Path_And_File_Name)
        else:
            self.obj_Log_Default.error('Some results files could not be located.  No Excel file written: '  + str_Excel_Output_Path_And_File_Name)
            boolSuccess = False
        pass
        
        return boolSuccess
    
    
    def func__LOCUS_JACKNIFING_Ne2Bulk_Results__Aggregate__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__LOCUS_JACKNIFING_Ne2Bulk_Results__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 


    def func__LOCUS_JACKNIFING_Ne2Bulk_Results__Aggregate_Input_File_To_Dataframe(self, str_Path_And_File):

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()
        pass            

        self.obj_Log_Debug_Display.debug('Aggregating Ne2 LDNe TAB file to dataframe: ' + str_Path_And_File)

        str_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__func_LOCUS_JACKNIFING_Ne2Bulk_Results__Aggregate_Results
        '''Process Results'''
        list_File_Header_Colnames = [
                                     str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Genepop_Source_File
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeLoci
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_strPopID
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intNeSamples
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatWeightedMeanSampleSize
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_intIndependentAlleles
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI
                                     ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI
                                     ]       


        ''' Replace Infinite with inf using converters on the pandas.read_csv'''
        def func_Conv_Col_To_Float(x):
                
            float_Value = 0.0
            
            try:
                float_Value = float(x)
            except:
                float_Value = -1*float('inf')
            pass
        
            return float_Value
        
        ''' Specify cols to convert '''
        dict_Converters = {
                         str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNe:func_Conv_Col_To_Float
                        ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Lwr_CI:func_Conv_Col_To_Float
                        ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeParametric_Upr_CI:func_Conv_Col_To_Float
                        ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Lwr_CI:func_Conv_Col_To_Float
                        ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatLDNeJackknife_Upr_CI:func_Conv_Col_To_Float                           
                          }
       
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Import Ne2 LDNe TAB file
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''                                    
        df = pandas.read_csv(str_Path_And_File, sep='\t', converters=dict_Converters, header=None, skiprows=11, names=list_File_Header_Colnames, skipfooter=8, engine='python')

        
        ''' Get column values from input filename '''
        str_Ne2_LDNe_PCrit = str_Path_And_File.split('x')[0]
        str_Ne2_LDNe_PCrit = str_Ne2_LDNe_PCrit.split('PC')[1]
        int_Ne2_LDNe_PCrit = int(str_Ne2_LDNe_PCrit)
        if int_Ne2_LDNe_PCrit < 10:
            str_Ne2_LDNe_PCrit = '0.0' + str_Ne2_LDNe_PCrit
            float_Ne2_LDNe_PCrit = float(str_Ne2_LDNe_PCrit)
        else:
            str_Ne2_LDNe_PCrit = '0.' + str_Ne2_LDNe_PCrit
            float_Ne2_LDNe_PCrit = float(str_Ne2_LDNe_PCrit)            
        pass
        ''' add it to the df '''
        df[str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = float_Ne2_LDNe_PCrit
        
        self.obj_Log_Debug_Display.debug('Added column to dataframe: ' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit + ' of value: ' + str(float_Ne2_LDNe_PCrit))

        ''' Split Stst cat Code, Sim Mating Count and Replicate Count from the genepop filename in the df '''
        int_Chars_To_Remove = len(globalsSS.Genepop_Results_File_Details.static_Genepop_File_Suffix__Locus_Jackknifing)
        df_Temp = df[str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_Output.static_Str_Colname_Genepop_Source_File].str[1:-int_Chars_To_Remove].str.split('_').apply(pandas.Series)
        
        df_Temp[2] = df_Temp[2].astype(int)
        df_Temp[1] = df_Temp[1].astype(int)
        df_Temp.drop(0, axis=1, inplace=True)
        df_Temp.columns = [
                           str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_LDNe_TAB_File_Output__Locus_Jackknifing.static_str_Colname_Ne2_TAB_Out__GPFileCount
                           ,str_Colname_Prefix + '_' + globalsSS.Colnames_Ne2_LDNe_TAB_File_Output__Locus_Jackknifing.static_str_Colname_Ne2_TAB_Out__Locus_Combo_Integer
                           ]
        df_New = pandas.concat((df_Temp, df), axis=1)
        
        df = df_New
        

        #DEBUG_ON
        if globalsSS.Logger_Debug_Display.bool_Debug_Display:
            #str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
            obj_Debug_Loc = Debug_Location()
            str_Message_Location = obj_Debug_Loc.Get_Debug_Location()
            str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
            self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe: %s' % str_Df)
            #pdb.set_trace()
            #with globalsSS.Pause_Console() as obj_Pause:
            #    obj_Pause.method_Pause_Console(str_Message_Location)
            #pass
        pass
                    
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
            #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            #    t2 = Timer2(True)
            #    t2.Start()
            #pass                    
        pass
                    
        return df   
   
    '''
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Summarised Reporting 
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''   

    '''
    -------------------------------------------------------------
    AgeNe Sim Per Replicate EOR Results - SUMMARISE AgeNe Details into one table
    -------------------------------------------------------------
    '''   
    def func__AgeNe_Sim_EOR_Summarise_Results__Aggregate_And_Group___Into_One_Table(self, str_Search_Path):

        boolSuccess = False
       
        '''
        -------------------------------
        Specify Final Output File
        -------------------------------
        '''
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Summarise_ALL_EOR__Summary_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Sim_Summarise_ALL_EOR__Summary_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_Summarise_ALL_EOR__Summary_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_Colname_Prefix

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)

        '''
        -------------------------------
        Specify Excel Input file
        -------------------------------
        '''        
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Sim_Merge_ALL_EOR__Summary_Results + '*.xlsx'
        str_File_Search_Pattern = str_Input_FileName
        
        '''
        -------------------------------
        Aggregate Excel Data to dataframe from each sheet of a single Excel input file
        -------------------------------
        '''
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 

        bool_File_1_Located = False               
        bool_File_1_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_1_Located:
            
            '''Process Results'''
            list_DF_1s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_1s.append(df_1)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_1s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            df1 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

    
        if bool_File_1_Located:
            '''
            Transform the dataframes
            '''
            df = self.func__AgeNe_Sim_EOR_Summarise_Results__Composite_Results__Process(df1)            
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
        pass

                
        if bool_File_1_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_1_Located:
            self.func_Save_Excel_Writer(writer)
            boolSuccess = True
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__AgeNe_Sim_EOR_Summarise_Results__Composite_Results__Process(self, df):

        self.obj_Log_Default.info('Processing dataframe')

       
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_EOR_Summarise_Results__Sum_Sex_Results__Group_Calculate_And_Rename(df)
       
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_EOR_Summarise_Results__Mean_Replicate_Results__Group_Calculate_And_Rename(df)
       
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df

    def func__AgeNe_Sim_EOR_Summarise_Results__Sum_Sex_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Sum
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Mean
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Mean  
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Mean

        ''' Colnames_AgeNe_LifeTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Sum

        ''' Colnames_AgeNe_DemographicTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All] = str_Mean

        ''' Colnames_AgeNe_FinalOverall_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nc_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NbDemo] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes_Overall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemo] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNcAdultsOverall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNOverall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_Overall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_Overall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_kbar_All_Sexes] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Male_N1_Ratio] = str_Mean
        
        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        
        '''
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Age = globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Age = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Age)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Age], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__AgeNe_Sim_EOR_Summarise_Results__Sum_Sex_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Summarise_ALL_EOR__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
 
    def func__AgeNe_Sim_EOR_Summarise_Results__Sum_Sex_Results__Calculate(self, df):

#         str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
#         str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
# 
#         ''' Get Colname from key '''
#         str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
#         str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
# 
#         ''' New Colnames '''
#         str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
#         str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
#                  
#         with SSAnalysisHandler() as obj_SSAnalysis:
#             df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#             df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#
        return df

    def func__AgeNe_Sim_EOR_Summarise_Results__Mean_Replicate_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Mean #Mean rather than Sum
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Mean
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Mean #Mean rather than Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Mean #Mean rather than Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Mean #Mean rather than Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Mean  
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Mean

        ''' Colnames_AgeNe_LifeTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Mean #Mean rather than Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Mean #Mean rather than Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Mean #Mean rather than Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Mean #Mean rather than Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Mean #Mean rather than Sum

        ''' Colnames_AgeNe_DemographicTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All] = str_Mean

        ''' Colnames_AgeNe_FinalOverall_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_Overall] = str_Mean #Mean rather than Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Adults_Overall] = str_Mean #Mean rather than Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nc_Adults_Overall] = str_Mean #Mean rather than Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Overall] = str_Mean #Mean rather than Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NbDemo] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes_Overall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemo] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNcAdultsOverall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNOverall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_Overall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_Overall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_kbar_All_Sexes] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Male_N1_Ratio] = str_Mean
        
        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        
        '''
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        #str_Group_Key_Replicate = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Age = globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        #str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Age = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Age)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        #df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Age], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Age], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__AgeNe_Sim_EOR_Summarise_Results__Mean_Replicate_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Summarise_ALL_EOR__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
 
    def func__AgeNe_Sim_EOR_Summarise_Results__Mean_Replicate_Results__Calculate(self, df):

#         str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
#         str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
# 
#         ''' Get Colname from key '''
#         str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
#         str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
# 
#         ''' New Colnames '''
#         str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
#         str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
#                  
#         with SSAnalysisHandler() as obj_SSAnalysis:
#             df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#             df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)

        return df

    '''
    -------------------------------------------------------------
    AgeNe Sim Per Replicate PF Results - SUMMARISE AgeNe Details into one table
    -------------------------------------------------------------
    '''   
    def func__AgeNe_Sim_PF_Summarise_Results__Aggregate_And_Group___Into_One_Table(self, str_Search_Path):

        boolSuccess = False
       
        '''
        -------------------------------
        Specify Final Output File
        -------------------------------
        '''
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Summarise_ALL_PF__Summary_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Sim_Summarise_ALL_PF__Summary_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_Summarise_ALL_PF__Summary_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_Colname_Prefix

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)

        '''
        -------------------------------
        Specify Excel Input file
        -------------------------------
        '''        
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Sim_Merge_ALL_PF__Summary_Results + '*.xlsx'
        str_File_Search_Pattern = str_Input_FileName
        
        '''
        -------------------------------
        Aggregate Excel Data to dataframe from each sheet of a single Excel input file
        -------------------------------
        '''
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 

        bool_File_1_Located = False               
        bool_File_1_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_1_Located:
            
            '''Process Results'''
            list_DF_1s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_1s.append(df_1)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_1s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            df1 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

    
        if bool_File_1_Located:
            '''
            Transform the dataframes
            '''
            df = self.func__AgeNe_Sim_PF_Summarise_Results__Composite_Results__Process(df1)            
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
        pass

                
        if bool_File_1_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_1_Located:
            self.func_Save_Excel_Writer(writer)
            boolSuccess = True
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__AgeNe_Sim_PF_Summarise_Results__Composite_Results__Process(self, df):

        self.obj_Log_Default.info('Processing dataframe')

       
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_PF_Summarise_Results__Sum_Sex_Results__Group_Calculate_And_Rename(df)
       
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_PF_Summarise_Results__Mean_Replicate_Results__Group_Calculate_And_Rename(df)
       
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df

    def func__AgeNe_Sim_PF_Summarise_Results__Sum_Sex_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Mean
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Mean  
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Mean

        ''' Colnames_AgeNe_LifeTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Sum

        ''' Colnames_AgeNe_DemographicTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All] = str_Mean

        ''' Colnames_AgeNe_FinalOverall_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nc_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NbDemo] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes_Overall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemo] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNcAdultsOverall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNOverall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_Overall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_Overall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_kbar_All_Sexes] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Male_N1_Ratio] = str_Mean
        
        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        
        '''
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        #str_Group_Key_Sex = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Mating_Count_Replicate_Total = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_Age = globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        #str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_Age = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Age)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_Age], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__AgeNe_Sim_PF_Summarise_Results__Sum_Sex_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Summarise_ALL_PF__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
 
    def func__AgeNe_Sim_PF_Summarise_Results__Sum_Sex_Results__Calculate(self, df):

#         str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
#         str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
# 
#         ''' Get Colname from key '''
#         str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
#         str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
# 
#         ''' New Colnames '''
#         str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
#         str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
#                  
#         with SSAnalysisHandler() as obj_SSAnalysis:
#             df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#             df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#
        return df

    def func__AgeNe_Sim_PF_Summarise_Results__Mean_Replicate_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Mean #Mean rather than Sum
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Mean
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Mean #Mean rather than Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Mean #Mean rather than Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Mean #Mean rather than Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Mean  
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Mean

        ''' Colnames_AgeNe_LifeTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Mean #Mean rather than Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Mean #Mean rather than Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Mean #Mean rather than Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Mean #Mean rather than Sum
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Mean #Mean rather than Sum

        ''' Colnames_AgeNe_DemographicTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All] = str_Mean

        ''' Colnames_AgeNe_FinalOverall_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_Overall] = str_Mean #Mean rather than Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Adults_Overall] = str_Mean #Mean rather than Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nc_Adults_Overall] = str_Mean #Mean rather than Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Overall] = str_Mean #Mean rather than Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NbDemo] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes_Overall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemo] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNcAdultsOverall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNOverall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_Overall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_Overall] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_kbar_All_Sexes] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Male_N1_Ratio] = str_Mean
        
        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        
        '''
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        #str_Group_Key_Replicate = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Mating_Count_Replicate_Total = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_Age = globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        #str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_Age = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Age)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        #df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Age], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_Age], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__AgeNe_Sim_PF_Summarise_Results__Mean_Replicate_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Summarise_ALL_PF__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
 
    def func__AgeNe_Sim_PF_Summarise_Results__Mean_Replicate_Results__Calculate(self, df):

#         str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
#         str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
# 
#         ''' Get Colname from key '''
#         str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
#         str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
# 
#         ''' New Colnames '''
#         str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
#         str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
#                  
#         with SSAnalysisHandler() as obj_SSAnalysis:
#             df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#             df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)

        return df

    '''
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Merged Reporting 
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''   
    '''
    -------------------------------------------------------------
    AgeNe MAN Per Replicate EOR Results - MERGE AgeNe Details into one table
    -------------------------------------------------------------
    '''   
    def func__AgeNe_Man_EOR_Merge_Results__Aggregate_And_Group___Into_One_Table(self, str_Search_Path):

        boolSuccess = False
       
        '''
        -------------------------------
        Specify Final Output File
        -------------------------------
        '''
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Merge_ALL_EOR__Summary_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Man_Merge_ALL_EOR__Summary_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Man_Merge_ALL_EOR__Summary_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_Colname_Prefix

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)

        '''
        -------------------------------
        Specify Excel Input file
        -------------------------------
        '''        
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Man_Aggregate_ALL_EOR__Summary_Results + '*.xlsx'
        str_File_Search_Pattern = str_Input_FileName
        
        '''
        -------------------------------
        Aggregate Excel Data to dataframe from each sheet of a single Excel input file
        -------------------------------
        '''
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET 1
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Man_Details_EOR_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 

        bool_File_1_Located = False               
        bool_File_1_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_1_Located:
            
            '''Process Results'''
            list_DF_1s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_1s.append(df_1)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_1s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            df1 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET 2
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Man_LifeTables_Total_EOR_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 
        
        bool_File_2_Located = False       
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_2 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_2s.append(df_2)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #raw_input('pausing...')
            #DEBUG_OFF
            
            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join & Transform the dataframes
            '''
            list_DFs = [df1, df2]
            df = self.func__AgeNe_Man_EOR_Merge_Results_1__Composite_Results__Aggregated_Dataframes__Process(list_DFs)            
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #raw_input('pausing...')
            #DEBUG_OFF
        pass

        '''
        ------------------------------------
        Process the additional Sheets
        ------------------------------------
        '''
        df1 = df
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET 3
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Man_DemographicTables_Total_EOR_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 
        
        bool_File_2_Located = False       
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_2 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_2s.append(df_2)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #raw_input('pausing...')
            #DEBUG_OFF
            
            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join & Transform the dataframes
            '''
            list_DFs = [df1, df2]
            df = self.func__AgeNe_Man_EOR_Merge_Results_2__Composite_Results__Aggregated_Dataframes__Process(list_DFs)            
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
        pass

        df1 = df
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET 4
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Man_Final_Totals_EOR_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 
               
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_2 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_2s.append(df_2)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #raw_input('pausing...')
            #DEBUG_OFF
            
            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join & Transform the dataframes
            '''
            list_DFs = [df1, df2]
            df = self.func__AgeNe_Man_EOR_Merge_Results_3__Composite_Results__Aggregated_Dataframes__Process(list_DFs)            
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
        pass

                
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_1_Located and bool_File_2_Located:
            self.func_Save_Excel_Writer(writer)
            boolSuccess = True
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__AgeNe_Man_EOR_Merge_Results_1__Composite_Results__Aggregated_Dataframes__Process(self, list_DFs):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Join Dataframes
        ---------------------
        '''
        df = self.func__AgeNe_Man_EOR_Merge_Results_1__Composite_Results__Merge(list_DFs)
        
        '''
        Add calculations
        '''
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Man_EOR_Merge_Results_1__Composite_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
 
    def func__AgeNe_Man_EOR_Merge_Results_1__Composite_Results__Merge(self, list_DFs):


        self.obj_Log_Default.info('Merge Dataframes')
        
        '''
        -------------------------
        Specify Key Colnames to merge on
        -------------------------
        '''
        strKey1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
        strKey2 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Batch
        strKey3 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Replicate
        strKey4 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex

        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        str_Join_How = 'left'
        list_Keys = [strKey1,strKey2,strKey3,strKey4]
        df = self.func_Merge_Dataframes_By_Key_List(str_Join_How, list_DFs[0], list_DFs[1], list_Keys)

        return df
    
    def func__AgeNe_Man_EOR_Merge_Results_1__Composite_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Details_EOR_Results + '_'
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Last

        ''' Colnames_AgeNe_LifeTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Last

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        
        '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Man_Details_EOR_Results
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Sex = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Result_MultiLine_Count = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Sex, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__AgeNe_Man_EOR_Merge_Results_1__Composite_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = str_Colname_Prefix_1
        ''' Accumulate Colnames '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, '')
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Merge_ALL_EOR__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
    
    def func__AgeNe_Man_EOR_Merge_Results_1__Composite_Results__Calculate(self, df):

#         str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
#         str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
# 
#         ''' Get Colname from key '''
#         str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
#         str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
# 
#         ''' New Colnames '''
#         str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
#         str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
#                  
#         with SSAnalysisHandler() as obj_SSAnalysis:
#             df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#             df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)

        return df


    def func__AgeNe_Man_EOR_Merge_Results_2__Composite_Results__Aggregated_Dataframes__Process(self, list_DFs):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Split Dataframe 
        ---------------------
        '''
        #list_DFs = self.func__AgeNe_Man_EOR_Merge_Results_2__Composite_Results__Split(list_DFs)
        '''
        ---------------------
        Join Dataframes
        ---------------------
        '''
        df = self.func__AgeNe_Man_EOR_Merge_Results_2__Composite_Results__Merge(list_DFs)
        
        '''
        Add calculations
        '''
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Man_EOR_Merge_Results_2__Composite_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
 
    def func__AgeNe_Man_EOR_Merge_Results_2__Composite_Results__Merge(self, list_DFs):


        self.obj_Log_Default.info('Merge Dataframes')

        #DEBUG_ON
#         str_Df = list_DFs[0].to_string()
#         self.obj_Log_Debug_Display.debug('Results dataframe D1: %s' % str_Df)
#         raw_input('pausing...')
#         str_Df = list_DFs[1].to_string()
#         self.obj_Log_Debug_Display.debug('Results dataframe D2: %s' % str_Df)
#         raw_input('pausing...')
        #DEBUG_OFF          
        '''
        -------------------------
        Specify Key Colnames to merge on
        -------------------------
        '''
        strKey1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
        strKey2 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Batch
        strKey3 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Replicate
        strKey4 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex

        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        str_Join_How = 'left'
        list_Keys = [strKey1,strKey2,strKey3,strKey4]
        df = self.func_Merge_Dataframes_By_Key_List(str_Join_How, list_DFs[0], list_DFs[1], list_Keys)

        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF
        
        return df
    
    def func__AgeNe_Man_EOR_Merge_Results_2__Composite_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Merge_ALL_EOR__Summary_Results + '_'
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Last

        ''' Colnames_AgeNe_LifeTable_Totals '''
        str_Colname_Prefix_2 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Merge_ALL_EOR__Summary_Results + '_'
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Last

        ''' Colnames_AgeNe_DemographicTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All] = str_Last


        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        
        '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Merge_ALL_EOR__Summary_Results
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Sex = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Result_MultiLine_Count = str_Source_File_Colname_Prefix_1 +'_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Sex, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__AgeNe_Man_EOR_Merge_Results_2__Composite_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Merge_ALL_EOR__Summary_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Merge_ALL_EOR__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
 
    def func__AgeNe_Man_EOR_Merge_Results_2__Composite_Results__Calculate(self, df):

#         str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
#         str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
# 
#         ''' Get Colname from key '''
#         str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
#         str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
# 
#         ''' New Colnames '''
#         str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
#         str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
#                  
#         with SSAnalysisHandler() as obj_SSAnalysis:
#             df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#             df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)

        return df


    def func__AgeNe_Man_EOR_Merge_Results_3__Composite_Results__Aggregated_Dataframes__Process(self, list_DFs):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Join Dataframes
        ---------------------
        '''
        df = self.func__AgeNe_Man_EOR_Merge_Results_3__Composite_Results__Merge(list_DFs)
        
        '''
        Add calculations
        '''
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Man_EOR_Merge_Results_3__Composite_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
 
    def func__AgeNe_Man_EOR_Merge_Results_3__Composite_Results__Merge(self, list_DFs):


        self.obj_Log_Default.info('Merge Dataframes')

        #DEBUG_ON
#         str_Df = list_DFs[0].to_string()
#         self.obj_Log_Debug_Display.debug('Results dataframe D1: %s' % str_Df)
#         raw_input('pausing...')
#         str_Df = list_DFs[1].to_string()
#         self.obj_Log_Debug_Display.debug('Results dataframe D2: %s' % str_Df)
#         raw_input('pausing...')
        #DEBUG_OFF               
        '''
        -------------------------
        Specify Key Colnames to merge on
        -------------------------
        '''
        
        strKey1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
        strKey2 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Batch
        strKey3 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Replicate
        #strKey4 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex

        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        str_Join_How = 'left'
        #list_Keys = [strKey1,strKey2,strKey3,strKey4]
        list_Keys = [strKey1,strKey2,strKey3]
        df = self.func_Merge_Dataframes_By_Key_List(str_Join_How, list_DFs[0], list_DFs[1], list_Keys)

        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe MERGED: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF               
        
        return df
    
    def func__AgeNe_Man_EOR_Merge_Results_3__Composite_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Merge_ALL_EOR__Summary_Results + '_'
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Last

        ''' Colnames_AgeNe_LifeTable_Totals '''
        str_Colname_Prefix_2 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Merge_ALL_EOR__Summary_Results + '_'
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Last

        ''' Colnames_AgeNe_DemographicTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All] = str_Last

        ''' Colnames_AgeNe_FinalOverall_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nc_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NbDemo] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemo] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNcAdultsOverall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNOverall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_kbar_All_Sexes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Male_N1_Ratio] = str_Mean
        
        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        
        '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Merge_ALL_EOR__Summary_Results
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Sex = str_Source_File_Colname_Prefix_1 + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Result_MultiLine_Count = str_Source_File_Colname_Prefix_1 + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Sex, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__AgeNe_Man_EOR_Merge_Results_3__Composite_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Merge_ALL_EOR__Summary_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Merge_ALL_EOR__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
 
    def func__AgeNe_Man_EOR_Merge_Results_3__Composite_Results__Calculate(self, df):

#         str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
#         str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
# 
#         ''' Get Colname from key '''
#         str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
#         str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
# 
#         ''' New Colnames '''
#         str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
#         str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
#                  
#         with SSAnalysisHandler() as obj_SSAnalysis:
#             df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#             df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)

        return df

    
    '''
    -------------------------------------------------------------
    AgeNe Sim Per Replicate EOR Results - MERGE AgeNe Details into one table
    -------------------------------------------------------------
    '''   
    def func__AgeNe_Sim_EOR_Merge_Results__Aggregate_And_Group___Into_One_Table(self, str_Search_Path):

        boolSuccess = False
       
        '''
        -------------------------------
        Specify Final Output File
        -------------------------------
        '''
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Sim_Merge_ALL_EOR__Summary_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_Merge_ALL_EOR__Summary_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_Colname_Prefix

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)

        '''
        -------------------------------
        Specify Excel Input file
        -------------------------------
        '''        
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Sim_Aggregate_ALL_EOR__Summary_Results + '*.xlsx'
        str_File_Search_Pattern = str_Input_FileName
        
        '''
        -------------------------------
        Aggregate Excel Data to dataframe from each sheet of a single Excel input file
        -------------------------------
        '''
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET 1
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_Details_EOR_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 

        bool_File_1_Located = False               
        bool_File_1_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_1_Located:
            
            '''Process Results'''
            list_DF_1s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_1s.append(df_1)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_1s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            df1 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET 2
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_LifeTables_Total_EOR_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 
        
        bool_File_2_Located = False       
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_2 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_2s.append(df_2)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #raw_input('pausing...')
            #DEBUG_OFF
            
            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join & Transform the dataframes
            '''
            list_DFs = [df1, df2]
            df = self.func__AgeNe_Sim_EOR_Merge_Results_1__Composite_Results__Aggregated_Dataframes__Process(list_DFs)            
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #raw_input('pausing...')
            #DEBUG_OFF
        pass

        '''
        ------------------------------------
        Process the additional Sheets
        ------------------------------------
        '''
        df1 = df
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET 3
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_DemographicTables_Total_EOR_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 
        
        bool_File_2_Located = False       
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_2 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_2s.append(df_2)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #raw_input('pausing...')
            #DEBUG_OFF
            
            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join & Transform the dataframes
            '''
            list_DFs = [df1, df2]
            df = self.func__AgeNe_Sim_EOR_Merge_Results_2__Composite_Results__Aggregated_Dataframes__Process(list_DFs)            
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
        pass

        df1 = df
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET 4
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_Final_Totals_EOR_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 
               
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_2 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_2s.append(df_2)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #raw_input('pausing...')
            #DEBUG_OFF
            
            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join & Transform the dataframes
            '''
            list_DFs = [df1, df2]
            df = self.func__AgeNe_Sim_EOR_Merge_Results_3__Composite_Results__Aggregated_Dataframes__Process(list_DFs)            
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
        pass

                
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_1_Located and bool_File_2_Located:
            self.func_Save_Excel_Writer(writer)
            boolSuccess = True
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__AgeNe_Sim_EOR_Merge_Results_1__Composite_Results__Aggregated_Dataframes__Process(self, list_DFs):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Join Dataframes
        ---------------------
        '''
        df = self.func__AgeNe_Sim_EOR_Merge_Results_1__Composite_Results__Merge(list_DFs)
        
        '''
        Add calculations
        '''
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_EOR_Merge_Results_1__Composite_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
 
    def func__AgeNe_Sim_EOR_Merge_Results_1__Composite_Results__Merge(self, list_DFs):


        self.obj_Log_Default.info('Merge Dataframes')
        
        '''
        -------------------------
        Specify Key Colnames to merge on
        -------------------------
        '''
        strKey1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
        strKey2 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Batch
        strKey3 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Replicate
        strKey4 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex

        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        str_Join_How = 'left'
        list_Keys = [strKey1,strKey2,strKey3,strKey4]
        df = self.func_Merge_Dataframes_By_Key_List(str_Join_How, list_DFs[0], list_DFs[1], list_Keys)

        return df
    
    def func__AgeNe_Sim_EOR_Merge_Results_1__Composite_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Details_EOR_Results + '_'
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Last

        ''' Colnames_AgeNe_LifeTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Last

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        
        '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_Details_EOR_Results
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Sex = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Result_MultiLine_Count = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Sex, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__AgeNe_Sim_EOR_Merge_Results_1__Composite_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = str_Colname_Prefix_1
        ''' Accumulate Colnames '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, '')
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
    
    def func__AgeNe_Sim_EOR_Merge_Results_1__Composite_Results__Calculate(self, df):

#         str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
#         str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
# 
#         ''' Get Colname from key '''
#         str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
#         str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
# 
#         ''' New Colnames '''
#         str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
#         str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
#                  
#         with SSAnalysisHandler() as obj_SSAnalysis:
#             df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#             df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)

        return df


    def func__AgeNe_Sim_EOR_Merge_Results_2__Composite_Results__Aggregated_Dataframes__Process(self, list_DFs):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Split Dataframe 
        ---------------------
        '''
        #list_DFs = self.func__AgeNe_Sim_EOR_Merge_Results_2__Composite_Results__Split(list_DFs)
        '''
        ---------------------
        Join Dataframes
        ---------------------
        '''
        df = self.func__AgeNe_Sim_EOR_Merge_Results_2__Composite_Results__Merge(list_DFs)
        
        '''
        Add calculations
        '''
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_EOR_Merge_Results_2__Composite_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
 
    def func__AgeNe_Sim_EOR_Merge_Results_2__Composite_Results__Merge(self, list_DFs):


        self.obj_Log_Default.info('Merge Dataframes')

        #DEBUG_ON
#         str_Df = list_DFs[0].to_string()
#         self.obj_Log_Debug_Display.debug('Results dataframe D1: %s' % str_Df)
#         raw_input('pausing...')
#         str_Df = list_DFs[1].to_string()
#         self.obj_Log_Debug_Display.debug('Results dataframe D2: %s' % str_Df)
#         raw_input('pausing...')
        #DEBUG_OFF          
        '''
        -------------------------
        Specify Key Colnames to merge on
        -------------------------
        '''
        strKey1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
        strKey2 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Batch
        strKey3 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Replicate
        strKey4 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex

        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        str_Join_How = 'left'
        list_Keys = [strKey1,strKey2,strKey3,strKey4]
        df = self.func_Merge_Dataframes_By_Key_List(str_Join_How, list_DFs[0], list_DFs[1], list_Keys)

        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF
        
        return df
    
    def func__AgeNe_Sim_EOR_Merge_Results_2__Composite_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results + '_'
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Last

        ''' Colnames_AgeNe_LifeTable_Totals '''
        str_Colname_Prefix_2 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results + '_'
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Last

        ''' Colnames_AgeNe_DemographicTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All] = str_Last


        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        
        '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Sex = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Result_MultiLine_Count = str_Source_File_Colname_Prefix_1 +'_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Sex, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__AgeNe_Sim_EOR_Merge_Results_2__Composite_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
 
    def func__AgeNe_Sim_EOR_Merge_Results_2__Composite_Results__Calculate(self, df):

#         str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
#         str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
# 
#         ''' Get Colname from key '''
#         str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
#         str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
# 
#         ''' New Colnames '''
#         str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
#         str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
#                  
#         with SSAnalysisHandler() as obj_SSAnalysis:
#             df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#             df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)

        return df


    def func__AgeNe_Sim_EOR_Merge_Results_3__Composite_Results__Aggregated_Dataframes__Process(self, list_DFs):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Join Dataframes
        ---------------------
        '''
        df = self.func__AgeNe_Sim_EOR_Merge_Results_3__Composite_Results__Merge(list_DFs)
        
        '''
        Add calculations
        '''
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_EOR_Merge_Results_3__Composite_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
 
    def func__AgeNe_Sim_EOR_Merge_Results_3__Composite_Results__Merge(self, list_DFs):


        self.obj_Log_Default.info('Merge Dataframes')

        #DEBUG_ON
#         str_Df = list_DFs[0].to_string()
#         self.obj_Log_Debug_Display.debug('Results dataframe D1: %s' % str_Df)
#         raw_input('pausing...')
#         str_Df = list_DFs[1].to_string()
#         self.obj_Log_Debug_Display.debug('Results dataframe D2: %s' % str_Df)
#         raw_input('pausing...')
        #DEBUG_OFF               
        '''
        -------------------------
        Specify Key Colnames to merge on
        -------------------------
        '''
        
        strKey1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
        strKey2 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Batch
        strKey3 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Replicate
        #strKey4 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex

        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        str_Join_How = 'left'
        #list_Keys = [strKey1,strKey2,strKey3,strKey4]
        list_Keys = [strKey1,strKey2,strKey3]
        df = self.func_Merge_Dataframes_By_Key_List(str_Join_How, list_DFs[0], list_DFs[1], list_Keys)

        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe MERGED: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF               
        
        return df
    
    def func__AgeNe_Sim_EOR_Merge_Results_3__Composite_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results + '_'
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Last

        ''' Colnames_AgeNe_LifeTable_Totals '''
        str_Colname_Prefix_2 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results + '_'
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Last

        ''' Colnames_AgeNe_DemographicTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All] = str_Last

        ''' Colnames_AgeNe_FinalOverall_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nc_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NbDemo] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemo] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNcAdultsOverall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNOverall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_kbar_All_Sexes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Male_N1_Ratio] = str_Mean
        
        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        
        '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Sex = str_Source_File_Colname_Prefix_1 + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Result_MultiLine_Count = str_Source_File_Colname_Prefix_1 + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Sex, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__AgeNe_Sim_EOR_Merge_Results_3__Composite_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
 
    def func__AgeNe_Sim_EOR_Merge_Results_3__Composite_Results__Calculate(self, df):

#         str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
#         str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
# 
#         ''' Get Colname from key '''
#         str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
#         str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
# 
#         ''' New Colnames '''
#         str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
#         str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
#                  
#         with SSAnalysisHandler() as obj_SSAnalysis:
#             df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#             df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)

        return df


    def func__AgeNe_Sim_EOR_Merge_Results_AgeNe_DemographicTable_AllSex__Composite_Results__Group_Calculate_And_Rename_NOT_REQUIRED_YET(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results + '_'
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Last
        ##dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Last

        ''' Colnames_AgeNe_LifeTable_Totals '''
        ##str_Colname_Prefix_2 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results + '_'
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Last
        ##dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Last

        ''' Colnames_AgeNe_DemographicTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All] = str_Last
        ''' Colnames_AgeNe_DemographicTable_Totals - For ALL sexes'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T_ForAllSex] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All_ForAllSex] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All_ForAllSex] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All_ForAllSex] = str_Last

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        
        '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        #str_Group_Key_Sex = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        #str_Group_Key_Result_MultiLine_Count = str_Source_File_Colname_Prefix_1 +'_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        #str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        #str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        #df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Sex, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__AgeNe_Sim_EOR_Merge_Results_2__Composite_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' SPECIAL CASE -  CHANGE THE COLNAME PREFIX '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Colnames_AgeNe_Results.static_Colname_Prefix_DTT
        ''' Colname prefix to add '''
        #str_Colname_Prefix_ForAllSex = globalsSS.Colnames_AgeNe_Results.static_Colname_Prefix_DTT_Replacement
        str_Colname_Prefix_ForAllSex = None
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Colname_Prefix_ForAllSex)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_EOR__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
    
    def func__AgeNe_Sim_EOR_Merge_Results_2__Composite_Results__Split_NOT_REQUIRED_YET(self, list_DFs):


        self.obj_Log_Default.info('Split AgeNe Demographic Dataframe on Sex and remerge it')
        
        df_To_Split = list_DFs[1]
        '''
        -------------------------
        Specify Subset
        -------------------------
        '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_DemographicTables_Total_EOR_Results + '_' 
        str_Query_Key_1 = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        
        ''' Get Colname from key '''
        str_Col_Name_Query_Key_1 = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df_To_Split, str_Query_Key_1)

        #DEBUG_ON
        #str_Df = df_To_Split.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF
        
#         str_Query = "'" + str_Col_Name_Query_Key_1 + ' == "All"' + "'"
#         df_Split_1 = df_To_Split.query(str_Query)
#         str_Query = "'" + str_Col_Name_Query_Key_1 + ' != "All"' + "'"
#         df_Split_2 = df_To_Split.query(str_Query)

        df_Split_1 = df_To_Split[(df_To_Split[str_Col_Name_Query_Key_1]!=globalsSS.SexConstants.static_stringSexAll)]
        
        #DEBUG_ON
        #str_Df = df_Split_1.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF
                
        df_Split_2 = df_To_Split[(df_To_Split[str_Col_Name_Query_Key_1]==globalsSS.SexConstants.static_stringSexAll)]

        '''
        -------------------------
        Change the Colnames in the second df because they are identical to the first df and cause all manner of downstream headaches
        -------------------------
        '''
        df_Split_2 = self.func__AgeNe_Sim_EOR_Merge_Results_AgeNe_DemographicTable_AllSex__Composite_Results__Group_Calculate_And_Rename(df_Split_2)

        #DEBUG_ON
        #str_Df = df_Split_2.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF
        '''
        -------------------------
        Now merge them together - Specify Key Colnames to merge on
        -------------------------
        '''
        strKey1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
        strKey2 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Batch
        strKey3 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Replicate
        
        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        str_Join_How = 'left'
        list_Keys = [strKey1,strKey2,strKey3]
        #list_Keys = [strKey1]
        str_Colname_Suffix = globalsSS.Colnames_AgeNe_Results.static_Colname_Prefix_DTT
#         list_Colname_Suffixes = ['', str_Colname_Suffix]
#         df_Merged = self.func_Merge_Dataframes_By_Key_List(str_Join_How, df_Split_1, df_Split_2, list_Keys, list_Colname_Suffixes)
        df_Merged = self.func_Merge_Dataframes_By_Key_List(str_Join_How, df_Split_1, df_Split_2, list_Keys)
        
#         '''
#         ~~~~~~~~~~~~
#         Blip - Need to rename Sex_ForAll colname so it wont interfere with downstream colname key matches
#         ~~~~~~~~~~~~
#         '''
# 
#         str_Key_Sex = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex + str_Colname_Suffix
#         ''' Get Colname from key '''
#         str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df_Merged, str_Key_Sex)
#         
#         df_Merged.rename(columns={str_Col_Name_Sex:'REDUNDENT_COL'}, inplace=True)
        
        
        #DEBUG_ON
        #str_Df = df_Merged.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF
            
        listfDFs_New = [list_DFs[0], df_Merged]
        
        return listfDFs_New
    

    '''
    -------------------------------------------------------------
    AgeNe Sim Per Replicate PF Results - MERGE AgeNe Details into one table
    -------------------------------------------------------------
    '''   
    def func__AgeNe_Sim_PF_Merge_Results__Aggregate_And_Group___Into_One_Table(self, str_Search_Path):

        boolSuccess = False
       
        '''
        -------------------------------
        Specify Final Output File
        -------------------------------
        '''
        ''' Output file '''                                                    
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Sim_Merge_ALL_PF__Summary_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_Merge_ALL_PF__Summary_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_Colname_Prefix

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)

        '''
        -------------------------------
        Specify Excel Input file
        -------------------------------
        '''        
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Sim_Aggregate_ALL_PF__Summary_Results + '*.xlsx'
        str_File_Search_Pattern = str_Input_FileName
        
        '''
        -------------------------------
        Aggregate Excel Data to dataframe from each sheet of a single Excel input file
        -------------------------------
        '''
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET 1
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_Details_PF_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 

        bool_File_1_Located = False               
        bool_File_1_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_1_Located:
            
            '''Process Results'''
            list_DF_1s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_1s.append(df_1)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_1s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            df1 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET 2
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_LifeTables_Total_PF_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 
        
        bool_File_2_Located = False       
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_2 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_2s.append(df_2)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #raw_input('pausing...')
            #DEBUG_OFF
            
            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join & Transform the dataframes
            '''
            list_DFs = [df1, df2]
            df = self.func__AgeNe_Sim_PF_Merge_Results_1__Composite_Results__Aggregated_Dataframes__Process(list_DFs)            
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #raw_input('pausing...')
            #DEBUG_OFF
        pass

        '''
        ------------------------------------
        Process the additional Sheets
        ------------------------------------
        '''
        df1 = df
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET 3
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_DemographicTables_Total_PF_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 
        
        bool_File_2_Located = False       
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_2 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_2s.append(df_2)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #raw_input('pausing...')
            #DEBUG_OFF
            
            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join & Transform the dataframes
            '''
            list_DFs = [df1, df2]
            df = self.func__AgeNe_Sim_PF_Merge_Results_2__Composite_Results__Aggregated_Dataframes__Process(list_DFs)            
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
        pass

        df1 = df
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET 4
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_Final_Totals_PF_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 
               
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_2 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_2s.append(df_2)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #raw_input('pausing...')
            #DEBUG_OFF
            
            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join & Transform the dataframes
            '''
            list_DFs = [df1, df2]
            df = self.func__AgeNe_Sim_PF_Merge_Results_3__Composite_Results__Aggregated_Dataframes__Process(list_DFs)            
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
        pass

                
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_1_Located and bool_File_2_Located:
            self.func_Save_Excel_Writer(writer)
            boolSuccess = True
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__AgeNe_Sim_PF_Merge_Results_1__Composite_Results__Aggregated_Dataframes__Process(self, list_DFs):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Join Dataframes
        ---------------------
        '''
        df = self.func__AgeNe_Sim_PF_Merge_Results_1__Composite_Results__Merge(list_DFs)
        
        '''
        Add calculations
        '''
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_PF_Merge_Results_1__Composite_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
 
    def func__AgeNe_Sim_PF_Merge_Results_1__Composite_Results__Merge(self, list_DFs):


        self.obj_Log_Default.info('Merge Dataframes')
        
        '''
        -------------------------
        Specify Key Colnames to merge on
        -------------------------
        '''
        strKey1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
        strKey2 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Batch
        strKey3 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Replicate
        strKey4 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        strKey5 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total

        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        str_Join_How = 'left'
        list_Keys = [strKey1,strKey2,strKey3,strKey4,strKey5]
        df = self.func_Merge_Dataframes_By_Key_List(str_Join_How, list_DFs[0], list_DFs[1], list_Keys)

        return df
    
    def func__AgeNe_Sim_PF_Merge_Results_1__Composite_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Details_PF_Results + '_'
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Last

        ''' Colnames_AgeNe_LifeTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Last

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        
        '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_Details_PF_Results
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Sex = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Mating_Count_Replicate_Total = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_Result_MultiLine_Count = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Sex, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__AgeNe_Sim_PF_Merge_Results_1__Composite_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = str_Colname_Prefix_1
        ''' Accumulate Colnames '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, '')
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
    
    def func__AgeNe_Sim_PF_Merge_Results_1__Composite_Results__Calculate(self, df):

#         str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
#         str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
# 
#         ''' Get Colname from key '''
#         str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
#         str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
# 
#         ''' New Colnames '''
#         str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
#         str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
#                  
#         with SSAnalysisHandler() as obj_SSAnalysis:
#             df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#             df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)

        return df


    def func__AgeNe_Sim_PF_Merge_Results_2__Composite_Results__Aggregated_Dataframes__Process(self, list_DFs):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Split Dataframe 
        ---------------------
        '''
        #list_DFs = self.func__AgeNe_Sim_PF_Merge_Results_2__Composite_Results__Split(list_DFs)
        '''
        ---------------------
        Join Dataframes
        ---------------------
        '''
        df = self.func__AgeNe_Sim_PF_Merge_Results_2__Composite_Results__Merge(list_DFs)
        
        '''
        Add calculations
        '''
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_PF_Merge_Results_2__Composite_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
 
    def func__AgeNe_Sim_PF_Merge_Results_2__Composite_Results__Merge(self, list_DFs):


        self.obj_Log_Default.info('Merge Dataframes')

        #DEBUG_ON
#         str_Df = list_DFs[0].to_string()
#         self.obj_Log_Debug_Display.debug('Results dataframe D1: %s' % str_Df)
#         raw_input('pausing...')
#         str_Df = list_DFs[1].to_string()
#         self.obj_Log_Debug_Display.debug('Results dataframe D2: %s' % str_Df)
#         raw_input('pausing...')
        #DEBUG_OFF          
        '''
        -------------------------
        Specify Key Colnames to merge on
        -------------------------
        '''
        strKey1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
        strKey2 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Batch
        strKey3 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Replicate
        strKey4 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        strKey5 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total

        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        str_Join_How = 'left'
        list_Keys = [strKey1,strKey2,strKey3,strKey4,strKey5]
        df = self.func_Merge_Dataframes_By_Key_List(str_Join_How, list_DFs[0], list_DFs[1], list_Keys)


        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF
        
        return df
    
    def func__AgeNe_Sim_PF_Merge_Results_2__Composite_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results + '_'
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Last

        ''' Colnames_AgeNe_LifeTable_Totals '''
        str_Colname_Prefix_2 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results + '_'
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Last

        ''' Colnames_AgeNe_DemographicTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All] = str_Last


        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        
        '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Sex = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Mating_Count_Replicate_Total = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_Result_MultiLine_Count = str_Source_File_Colname_Prefix_1 +'_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Sex, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__AgeNe_Sim_PF_Merge_Results_2__Composite_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
 
    def func__AgeNe_Sim_PF_Merge_Results_2__Composite_Results__Calculate(self, df):

#         str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
#         str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
# 
#         ''' Get Colname from key '''
#         str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
#         str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
# 
#         ''' New Colnames '''
#         str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
#         str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
#                  
#         with SSAnalysisHandler() as obj_SSAnalysis:
#             df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#             df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)

        return df


    def func__AgeNe_Sim_PF_Merge_Results_3__Composite_Results__Aggregated_Dataframes__Process(self, list_DFs):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Join Dataframes
        ---------------------
        '''
        df = self.func__AgeNe_Sim_PF_Merge_Results_3__Composite_Results__Merge(list_DFs)
        
        '''
        Add calculations
        '''
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_PF_Merge_Results_3__Composite_Results__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
 
    def func__AgeNe_Sim_PF_Merge_Results_3__Composite_Results__Merge(self, list_DFs):


        self.obj_Log_Default.info('Merge Dataframes')

        #DEBUG_ON
#         str_Df = list_DFs[0].to_string()
#         self.obj_Log_Debug_Display.debug('Results dataframe D1: %s' % str_Df)
#         raw_input('pausing...')
#         str_Df = list_DFs[1].to_string()
#         self.obj_Log_Debug_Display.debug('Results dataframe D2: %s' % str_Df)
#         raw_input('pausing...')
        #DEBUG_OFF               
        '''
        -------------------------
        Specify Key Colnames to merge on
        -------------------------
        '''
        
        strKey1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
        strKey2 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Batch
        strKey3 = globalsSS.Logger_Results_File_Details.static_Label_Log_Col_Key_Replicate
        strKey4 = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total

        '''
        -------------------------
        Perform Merge
        -------------------------
        '''
        str_Join_How = 'left'
        list_Keys = [strKey1,strKey2,strKey3,strKey4]
        df = self.func_Merge_Dataframes_By_Key_List(str_Join_How, list_DFs[0], list_DFs[1], list_Keys)

        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe MERGED: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF               
        
        return df
    
    def func__AgeNe_Sim_PF_Merge_Results_3__Composite_Results__Group_Calculate_And_Rename(self, df):


        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results + '_'
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        #dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Last

        ''' Colnames_AgeNe_LifeTable_Totals '''
        str_Colname_Prefix_2 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results + '_'
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_2 + globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Last

        ''' Colnames_AgeNe_DemographicTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All] = str_Last

        ''' Colnames_AgeNe_FinalOverall_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nc_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NbDemo] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemo] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNcAdultsOverall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNOverall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_kbar_All_Sexes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Male_N1_Ratio] = str_Mean
        
        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        
        '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results
        ''' Specify GroupBy keys '''
        str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Sex = str_Source_File_Colname_Prefix_1 + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Mating_Count_Replicate_Total = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_Result_MultiLine_Count = str_Source_File_Colname_Prefix_1 + '_' + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Sex, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Additional Calculations
        -------------------------
        '''
        #df = self.func__AgeNe_Sim_PF_Merge_Results_3__Composite_Results__Calculate(df)
        '''
        -------------------------
        Accumulate New Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        #dict_New_Colnames[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_Ne2_Experiment_Label] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
        ''' Additional Colnames '''
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff] = 'func'
        #dict_New_Colnames[globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe] = 'func'
    
        '''
        -------------------------
        Generate new colnames and rename
        -------------------------
        '''
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Merge_ALL_PF__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df 
 
    def func__AgeNe_Sim_PF_Merge_Results_3__Composite_Results__Calculate(self, df):

#         str_Colname_floatRSquared_Observed = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Observed
#         str_Colname_floatRSquared_Expected = globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatRSquared_Expected
# 
#         ''' Get Colname from key '''
#         str_Colname_floatRSquared_Observed = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Observed)
#         str_Colname_floatRSquared_Expected = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Colname_floatRSquared_Expected)
# 
#         ''' New Colnames '''
#         str_Colname_float_Burrows_r_Squared_Diff = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Squared_Diff
#         str_Colname_float_Burrows_r_Sqrd_LDNe = globalsSS.Colnames_Ne2_Aggregation.static_Str_Colname_float_Ne2_Burrows_r_Sqrd_LDNe
#                  
#         with SSAnalysisHandler() as obj_SSAnalysis:
#             df[str_Colname_float_Burrows_r_Squared_Diff] = df.apply(lambda row: obj_SSAnalysis.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)
#             df[str_Colname_float_Burrows_r_Sqrd_LDNe] = df.apply(lambda row: obj_SSAnalysis.method_Get_LDNe_From_Burrows_r_Squared_Results(row[str_Colname_floatRSquared_Observed], row[str_Colname_floatRSquared_Expected]), axis=1)

        return df


    '''
    -------------------------------------------------------------
    PARENT/OFFSPRING Per Fertilization PF Results - Aggregate and GroupBy Run/Mating Count Sim Total
    -------------------------------------------------------------
    '''   
    def func__Parent_Offspring_PF_Results__Aggregate_And_Group___By_Run_By_Mating_Count_Sim_Total(self, str_Search_Path):

        boolSuccess = False
 
        #str_Search_Path = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\Shared_Data\\LEVEL_Stats_Test'
        #str_Search_Path = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\SharkSim\\v2_54_Py27\\Test\\NEW_AGE_V1'
       
        '''
        Process Results
        '''
        
        ''' Input file '''
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__Embryo_Parent_Ne_Stats_Post_Fertilization
        
        ''' Output file '''
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Embryo_Parent_Ne_Stats_Post_Fertilization
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__Embryo_Parent_Ne_Stats_Post_Fertilization
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__Embryo_Parent_Ne_Stats_Post_Fertilization
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_Colname_Prefix

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
 
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName)
        
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
            
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__Parent_Offspring_PF_Results__Aggregate_And_Group___By_Run_By_Mating_Count_Sim_Total__Process(str_Path_And_File)
                list_DFs.append(df)
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
        
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        
        if bool_File_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Default.info('Excel file written.')
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written')
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess
    
    
    def func__Parent_Offspring_PF_Results__Aggregate_And_Group___By_Run_By_Mating_Count_Sim_Total__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__Parent_Offspring_PF_Results__Aggregate_And_Group__By_Run_By_Mating_Count_Sim_Total__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

 
    def func__Parent_Offspring_PF_Results__Aggregate_And_Group__By_Run_By_Mating_Count_Sim_Total__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last

        ''' Colnames_Parent_Offspring_Stats_METHOD_1 '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_NonUnique_Female_Effective_Gametes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_NonUnique_Male_Effective_Gametes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_NonUnique_Effective_Dame_Sire_Gamete_Pair_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_Unique_Female_Effective_Gametes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_Unique_Male_Effective_Gametes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_Unique_Effective_Dame_Sire_Gamete_Pair_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_Total_NonUnique_Gametes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_Total_Unique_Gametes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_Demo_Ne_By_Sex] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate] = str_Last

        ''' Colnames_Parent_Offspring_Stats_METHOD_2 '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Male_Potential_Parent] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Offspring_Per_Male_Potential_Parent] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Variance_Offspring_Per_Male_Potential_Parent] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeMale_Potential_Parents_NeM] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Sires] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Offspring_Per_Sire] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Variance_Offspring_Per_Sire] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeSires_NeS] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Female_Potential_Parent] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Offspring_Per_Female_Potential_Parent] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Variance_Offspring_Per_Female_Potential_Parent] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Ne_DemoFemale_Potential_Parents_NeF] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Dames] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Offspring_Per_Dame] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Variance_Offspring_Per_Dame] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeDames_NeD] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Potential_Parents_PP] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Offspring_Per_PP] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Variance_Offspring_Per_PP] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP_Rato_Nc] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Effective_Parents_EP] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Offspring_Per_EP] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Variance_Offspring_Per_EP] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeEP] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeEP_Rato_Nc] = str_Last

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Embryo_Offspring_Parent_Ne_Stats.static_Label_Gen_File
        str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        #str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        #str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Mating_Count_Sim_Total = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        #str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        #str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Mating_Count_Sim_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Sim_Total)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        #df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Sim_Total], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Mating_Count_Sim_Total], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Rename Colnames
        -------------------------
        '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Embryo_Parent_Ne_Stats_Post_Fertilization
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df
 
    
    '''
    -------------------------------------------------------------
    MERGE NE2 & SS_LEVEL REPLICATE Results
    -------------------------------------------------------------
    '''   
    def func_Aggregate_Ne2_Samples_And_SS_LEVEL_VSP_Stats(self, str_Search_Path):

        boolSuccess = False
 
        #str_Search_Path = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\Shared_Data\\LEVEL_Stats_Test'
        #str_Search_Path = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\SharkSim\\v2_54_Py27\\Test\\NEW_AGE_V1'
       
        '''
        Process Results
        '''

        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_Ne2_Sub_Sampling_SS_VSP_Aggregate_Results'

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
 
        '''
        Process LEVEL - VSP
        '''
        
        '''Get LEVEL stats'''
        self.obj_Log_Default.info('Dataframing results for SS LEVEL - VSP EOR - End of Replicate')
        
        str_File_Search_Pattern = '*' + globalsSS.SS_Level_Details.static_Output_File_Suffix__Level_Age_Class_VSP_EOR
        bool_File_1_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_1_Located:
            
            '''Process VSP Results'''
            list_DF_1s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df_1 = self.func_Aggregate_SS_LEVEL_VSP_Results(str_Path_And_File)
                list_DF_1s.append(df_1)
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_1s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            df1 = df_Aggregate 

        
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        '''Get Ne2 Sampling stats'''
        self.obj_Log_Default.info('Dataframing results for Ne2 Samples')
        
        str_File_Search_Pattern = '*' + globalsSS.Logger_Details_Sampling.static_Logger_File_Suffix__Genepop_Ne2_Samples
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process REPLICATE Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df_2 = self.func_Aggregate_Ne2_Sampling_Results(str_Path_And_File)
                list_DF_2s.append(df_2)
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF

            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join the dataframes
            '''
            #strKey1 = globalsSS.SS_LEVEL_VSP_Details.static_Label_Gen_UniqueID
            strKey1 = globalsSS.SS_LEVEL_VSP_Details.static_Label_Gen_Unique_Run_Batch_Rep_VSP_ID
            #strKey2 = globalsSS.Ne2_Sampling_Stats.static_Label_Gen_Source_UniqueID
            strKey2 = globalsSS.Ne2_Sampling_Stats.static_Label_Gen_Source_Unique_Run_Batch_Rep_VSP_ID

            df = self.func_Merge_Dataframes_By_Common_Key(strKey1, df1, strKey2, df2)

            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE FINAL: %s' % str_Df)
            #DEBUG_OFF
            
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Write results to Excel
            '''
            str_Sheet_Name = 'NE2_SAMP_VSP_EOR'
            self.func_Export_Results_To_Excel(df, writer, str_Sheet_Name)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_1_Located and bool_File_2_Located:
            self.func_Save_Excel_Writer(writer)
            boolSuccess = True
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess
    
    
    def func_Aggregate_Ne2_Samples_And_SS_LEVEL_REPLICATE_Stats(self, str_Search_Path):

        boolSuccess = False
 
        #str_Search_Path = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\Shared_Data\\LEVEL_Stats_Test'
        #str_Search_Path = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\SharkSim\\v2_54_Py27\\Test\\NEW_AGE_V1'
       
        '''
        Process Results
        '''

        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_Ne2_Sub_Sampling_SS_REP_Aggregate_Results'
        writer = self.func_Get_Excel_Writer(str_Search_Path, str_Excel_Output_File_WO_Suffix)
 
        '''
        Process LEVEL - REPLICATE
        '''
        
        '''Get LEVEL stats'''
        self.obj_Log_Default.info('Dataframing results for SS LEVEL - REPLICATE EOR - End of Replicate')
        
        str_File_Search_Pattern = '*' + globalsSS.SS_Level_Details.static_Output_File_Suffix__Level_REPLICATE_EOR
        bool_File_1_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_1_Located:
            
            '''Process REPLICATE Results'''
            list_DF_1s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df_1 = self.func_Aggregate_SS_LEVEL_REPLICATE_Results(str_Path_And_File)
                list_DF_1s.append(df_1)
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_1s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            df1 = df_Aggregate 

        
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        '''Get Ne2 Sampling stats'''
        self.obj_Log_Default.info('Dataframing results for Ne2 Samples')
        
        str_File_Search_Pattern = '*' + globalsSS.Logger_Details_Sampling.static_Logger_File_Suffix__Genepop_Ne2_Samples
        bool_File_2_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_2_Located:
            
            '''Process REPLICATE Results'''
            list_DF_2s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df_2 = self.func_Aggregate_Ne2_Sampling_Results(str_Path_And_File)
                list_DF_2s.append(df_2)
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_2s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF

            df2 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Join the dataframes
            '''
            strKey1 = globalsSS.SS_LEVEL_Replicate_Details.static_Label_Gen_UniqueID
            strKey2 = globalsSS.Ne2_Sampling_Stats.static_Label_Gen_Source_UniqueID

            df = self.func_Merge_Dataframes_By_Common_Key(strKey1, df1, strKey2, df2)

            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE FINAL: %s' % str_Df)
        
        if bool_File_1_Located and bool_File_2_Located:
            '''
            Write results to Excel
            '''
            str_Sheet_Name = 'NE2_SAMP_REPLICATE_EOR'
            self.func_Export_Results_To_Excel(df, writer, str_Sheet_Name)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_1_Located and bool_File_2_Located:
            self.func_Save_Excel_Writer(writer)
            boolSuccess = True
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess
    
    
    def func_Aggregate_Ne2_Sampling_Results(self, str_Path_And_File):
        
        '''Process HWE Results'''
        dictResults = self.func_Aggregate_Results(str_Path_And_File)
        df = self.func_Manipulate_Ne2_Sampling_Results(dictResults)

        return df


    def func_Manipulate_Ne2_Sampling_Results(self, dictResults):

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()
                    
        '''create dataframe'''
        df = pandas.DataFrame.from_dict(dictResults,'columns', float)
        
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        '''convert non-numerics to numerics'''
        df.convert_objects(convert_numeric=True)
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        
        '''
        Sort DF Columns
        '''
        '''re-arrange columns based on the col name col index prefix number'''
        df = df.reindex_axis(sorted(df.columns), axis=1)        
        
#         '''
#         Apply interpretations to the results
#         '''
#         df = self.func_Interpret_HWE_P_Values(df)
        

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            '''log the results'''
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe: %s' % str_Df)
            #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
            t2.Stop(self.obj_Log_Debug_Display)
        
        return df


    '''
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Non-Customised Reporting 
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''   
    
    '''
    -------------------------------------------------------------
    Aggregate any set of files 
    -------------------------------------------------------------
    '''   
    def func_Aggregate_ANY__Aggregate_Results(self, str_Search_Path, str_File_Search_Pattern, str_Excel_Output_Colname_Prefix, str_Excel_Output_FileName, str_Excel_Output_Sheet_Name):

        boolSuccess = False
       
        '''
        Process Results
        '''

        ''' Output file '''
        #str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results
        str_Excel_Output_FileName =  str_Excel_Output_FileName + '_ALL'
        #str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName + '_' + str_Excel_Output_Colname_Prefix
        writer = self.func_Get_Excel_Writer(str_Search_Path, str_Excel_Output_File_WO_Suffix)
        str_Excel_Output_Path_And_File_Name = str_Search_Path + '\\' + str_Excel_Output_File_WO_Suffix + '.xlsx'
  
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName)
        
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
            
            '''Process each file in turn'''
            '''Process Results'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df = xl.parse(str_Excel_Output_Sheet_Name)
                list_DFs.append(df)
                
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
        
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        if bool_File_Located:
            '''
            Write results to Excel
            '''
            self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)            
        pass
    
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Debug_Display.debug('Excel file written: ' + str_Excel_Output_Path_And_File_Name)
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written:'  + str_Excel_Output_Path_And_File_Name)
        else:
            self.obj_Log_Default.error('Some results files could not be located.  No Excel file written: '  + str_Excel_Output_Path_And_File_Name)
            boolSuccess = False
        pass
        
        return boolSuccess
    
    
    def func__Aggregate_ANY__Aggregate__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 


    '''
    -------------------------------------------------------------
    CURRENT NEOGEN SPREADSHEET - Individuals Sampling Results - Aggregate Details into one Excel file
    -------------------------------------------------------------
    '''   
   
    def func__Sampling_Individuals_Results_SUMMARY__Aggregate_And_Group(self, str_Excel_Save_Path, str_Search_Path):

        boolSuccess = False
       
        '''
        -------------------------------
        Specify Final Output File
        -------------------------------
        '''
        ''' Output file '''                                                    
        str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__SAMPLING_INDIVS_Summary__Aggregate_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__SAMPLING_INDIVS_Summary__Aggregate_Results
        str_Excel_Output_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__SAMPLING_INDIVS_Summary__Aggregate_Results
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_Colname_Prefix

        #str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
        str_Excel_Output_Path_And_File_Name = str_Excel_Save_Path + '\\' + str_Excel_Output_File_WO_Suffix + '.xlsx'
        
        '''
        -------------------------------
        Specify Excel Input file
        -------------------------------
        '''        
        str_Input_FileName = '*' + globalsSS.Excel_Results_File_Details.static_Excel_FileName__SAMPLING_INDIVS__Aggregate_Results + '*.xlsx'
        str_File_Search_Pattern = str_Input_FileName
        
        '''
        -------------------------------
        Aggregate Excel Data to dataframe from each sheet of a single Excel input file
        -------------------------------
        '''
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get & Process Input SHEET 1
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        str_Input_Excel_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__SAMPLING_INDIVS__Aggregate_Results

        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Input_Excel_Sheet_Name) 

        bool_File_1_Located = False               
        bool_File_1_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_1_Located:
            
            '''Process Results'''
            list_DF_1s = []            
            for str_Path_And_File in list_Path_And_Files:
                
                '''Get the data from the excel files with the specified sheet'''
                xl = pandas.ExcelFile(str_Path_And_File)
                df_1 = xl.parse(str_Input_Excel_Sheet_Name)
                list_DF_1s.append(df_1)
                
            pass

            ''' concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DF_1s:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            df1 = df_Aggregate 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

        if bool_File_1_Located:
            '''
            Join & Transform the dataframes
            '''
            df = self.func__Sampling_Individuals_Results_SUMMARY__Aggregate_And_Group__Process(df1)            
            
            #DEBUG_ON
            #str_Df = df_Aggregate.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 2: %s' % str_Df)
            #DEBUG_OFF
        pass

        ''' final save of the excel file '''
        if bool_File_1_Located:
            try:
                boolSuccess = True
                #self.func_Save_Excel_Writer(writer)
                '''
                Write results to Excel
                '''
                self.func_Export_Results_To_Excel(df, writer, str_Excel_Output_Sheet_Name)                  
                self.obj_Log_Debug_Display.debug('Excel file written: ' + str_Excel_Output_Path_And_File_Name)
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written:'  + str_Excel_Output_Path_And_File_Name)
        else:
            self.obj_Log_Default.error('Some results files could not be located.  No Excel file written: '  + str_Excel_Output_Path_And_File_Name)
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__Sampling_Individuals_Results_SUMMARY__Aggregate_And_Group__Process(self, df):

        self.obj_Log_Default.info('Processing aggregated dataframe')

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__Sampling_Individuals_Results_SUMMARY__Aggregate_And_Group__Process__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df
    
    def func__Sampling_Individuals_Results_SUMMARY__Aggregate_And_Group__Process__Group_Calculate_And_Rename_RETIRE(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_Strategy_Results
        
        '''Common experiment colnames'''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        dict_Columns_Required_Plus_Function[str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last

        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last

        ''' Indiv sampling experiment fields '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_strPCritsToProcess] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Search_Path] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sample_Each_Mating_Count_Divisible_By] = str_Last

        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Pop_Sampling.static_Str_Colname_Sampling_Params] = str_Last

        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Categories] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Indiv_Number] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Loci_Number] = str_Mean

        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicates] = str_Last 
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_VSP_Ages_And_Sizes__Ages] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_VSP_Ages_And_Sizes__Sizes] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sample_VSP_Ages_And_Sizes__Sizes] = str_Mean
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sample_Percent_VSP_Ages_And_Sizes__Sizes] = str_Mean
        
        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)

        bool_Group_By = True   
        if bool_Group_By:     
            '''
            -------------------------
            Perform GroupBy with Aggregate Functions
            -------------------------
            '''
            ''' Specify GroupBy keys '''
            str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_Strategy_Results
            #str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
            #str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
            #str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
            #str_Group_Key_Mating_Count_Sim_Total = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total
            str_Group_Key_Sampling_Indiv_Number = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Indiv_Number
            str_Group_Key_Source_VSP_Ages_And_Sizes__Ages = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_VSP_Ages_And_Sizes__Ages
            
            ''' Get Colname from key '''
            self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones with colname prefix: ' + str_Source_File_Colname_Prefix_1)
            #str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
            #str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
            #str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
            #str_Col_Name_Mating_Count_Sim_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Sim_Total)
            str_Col_Name_Sampling_Indiv_Number = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sampling_Indiv_Number)
            str_Col_Name_Source_VSP_Ages_And_Sizes__Ages = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Source_VSP_Ages_And_Sizes__Ages)
            
            ''' Perform GroupBy with aggregate '''
            self.obj_Log_Default.info('Grouping results')
            #df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Sim_Total], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
            #df = df.groupby([str_Col_Name_RunID, str_Col_Name_Mating_Count_Sim_Total], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
            #df = df.groupby([str_Col_Name_RunID], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
            #df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Sampling_Indiv_Number], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
            #df = df.groupby([str_Col_Name_Sampling_Indiv_Number], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
            df = df.groupby([str_Col_Name_Sampling_Indiv_Number, str_Col_Name_Source_VSP_Ages_And_Sizes__Ages], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
            
            '''
            -------------------------
            Rename Colnames
            -------------------------
            '''
            self.obj_Log_Default.info('Renaming results')
            dict_New_Colnames = OrderedDict()
            #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
            #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
            #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
            #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
            dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Indiv_Number] = str_Last
            dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_VSP_Ages_And_Sizes__Ages] = str_Last
            
            for key, value in dict_Columns_Required_Plus_Function.items():
                dict_New_Colnames[key] = value
            pass
         
            str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__SAMPLING_INDIVS_Summary__Aggregate_Results
            list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)
     
            df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        pass
    
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df

    def func__Sampling_Individuals_Results_SUMMARY__Aggregate_And_Group__Process__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Source_File_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__SAMPLING_INDIVS__Aggregate_Results + '_'
        
        '''Common experiment colnames'''
        int_Col_Order = 0
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = (str_Last, int_Col_Order)
#         int_Col_Order += 1        
#         dict_Columns_Required_Plus_Function[str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = (str_Last, int_Col_Order)
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = (str_Last, int_Col_Order)
        
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = (str_Last, int_Col_Order)
        #int_Col_Order += 1        
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_MatingsToSimulate] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_MatingsToSimulatePerReplicate] = (str_Last, int_Col_Order)

        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = (str_Last, int_Col_Order)
#         int_Col_Order += 1        
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = (str_Last, int_Col_Order)
#         int_Col_Order += 1        
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = (str_Last, int_Col_Order)

        ''' Indiv sampling experiment fields '''
#         int_Col_Order += 1        
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code] = (str_Last, int_Col_Order)
        #int_Col_Order += 1        
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = (str_Last, int_Col_Order)
        #int_Col_Order += 1        
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category] = (str_Last, int_Col_Order)

        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = (str_Last, int_Col_Order)
#         int_Col_Order += 1        
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Indiv_Number] = (str_Mean, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Loci_Number] = (str_Mean, int_Col_Order)
        
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = (str_Last, int_Col_Order)
        #int_Col_Order += 1        
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category] = (str_Last, int_Col_Order)
        #int_Col_Order += 1        
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_strPCritsToProcess] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Search_Path] = (str_Last, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sample_Each_Mating_Count_Divisible_By] = (str_Last, int_Col_Order)

        #int_Col_Order += 1        
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Pop_Sampling.static_Str_Colname_Sampling_Params] = (str_Last, int_Col_Order)

#         int_Col_Order += 1        
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = (str_Last, int_Col_Order)
        #int_Col_Order += 1        
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = (str_Last, int_Col_Order)
        #int_Col_Order += 1        
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Categories] = (str_Last, int_Col_Order)
        
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicates] = (str_Last, int_Col_Order) 
#         int_Col_Order += 1        
#         dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_VSP_Ages_And_Sizes__Ages] = (str_Last, int_Col_Order)
        int_Col_Order += 1
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicate_Filename] = (str_Last, int_Col_Order)        
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_VSP_Ages_And_Sizes__Sizes] = (str_Mean, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sample_VSP_Ages_And_Sizes__Sizes] = (str_Mean, int_Col_Order)
        int_Col_Order += 1        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sample_Percent_VSP_Ages_And_Sizes__Sizes] = (str_Mean, int_Col_Order)
        int_Col_Order += 1        
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = (str_Last, int_Col_Order)
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = (str_Last, int_Col_Order)
        
        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function_With_Order = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions_With_Order(df, dict_Columns_Required_Plus_Function)

        bool_Group_By = True   
        if bool_Group_By:     
            '''
            -------------------------
            Perform GroupBy with Aggregate Functions
            -------------------------
            '''
            dict_Specific_Columns_Required_Plus_Function = OrderedDict(([key_Colname, value_str_Function]) for key_Colname, (value_str_Function, value_int_Order) in dict_Specific_Columns_Required_Plus_Function_With_Order.items())
            
            ''' Specify GroupBy keys '''
            #str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_Strategy_Results
            str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
            str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
            str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
            #str_Group_Key_Mating_Count_Sim_Total = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total
            str_Group_Key_Experiment_Label  =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label            
            str_Group_Key_Stats_Category_Code  =  globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code            
            str_Group_Key_Sampling_Indiv_Number = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Indiv_Number
            str_Group_Key_Source_VSP_Ages_And_Sizes__Ages = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_VSP_Ages_And_Sizes__Ages
            
            ''' Get Colname from key '''
            self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones with colname prefix: ' + str_Source_File_Colname_Prefix_1)
            str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
            str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
            str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
            #str_Col_Name_Mating_Count_Sim_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Sim_Total)
            str_Col_Name_Experiment_Label = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Experiment_Label)
            str_Col_Name_Stats_Category_Code = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Stats_Category_Code)
            str_Col_Name_Sampling_Indiv_Number = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sampling_Indiv_Number)
            str_Col_Name_Source_VSP_Ages_And_Sizes__Ages = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Source_VSP_Ages_And_Sizes__Ages)
            
            ''' Perform GroupBy with aggregate '''
            self.obj_Log_Default.info('Grouping results')
            df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Experiment_Label, str_Col_Name_Stats_Category_Code, str_Col_Name_Sampling_Indiv_Number, str_Col_Name_Source_VSP_Ages_And_Sizes__Ages], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
            
            '''
            -------------------------
            Rename Colnames
            -------------------------
            '''
            self.obj_Log_Default.info('Renaming results')
            dict_New_Colnames = OrderedDict()
            
            int_Col_Order += 1
            dict_New_Colnames[str_Col_Name_RunID] = (str_Last, 0.1)
            int_Col_Order += 1
            dict_New_Colnames[str_Col_Name_Batch] = (str_Last, 12.1)
            int_Col_Order += 1
            dict_New_Colnames[str_Col_Name_Replicate] = (str_Last, 12.2)
            #int_Col_Order += 1
            #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
            int_Col_Order += 1
            dict_New_Colnames[str_Col_Name_Experiment_Label] = (str_Last, 16.1)
            int_Col_Order += 1
            dict_New_Colnames[str_Col_Name_Stats_Category_Code] = (str_Last, 17.1)
            int_Col_Order += 1
            dict_New_Colnames[str_Col_Name_Sampling_Indiv_Number] = (str_Last, 17.2)
            int_Col_Order += 1
            dict_New_Colnames[str_Col_Name_Source_VSP_Ages_And_Sizes__Ages] = (str_Last, 24.1)
                        
            for key_Colname, (value_str_Function, value_int_Col_Order) in dict_Specific_Columns_Required_Plus_Function_With_Order.items():
                dict_New_Colnames[key_Colname] = (value_str_Function, value_int_Col_Order)
            pass
         
            ''' Get current df colnames their order '''
            list_Df_Colnames = df.columns.tolist()
            
            ''' Sort columns by order '''
            dict_New_Colnames_Sorted = OrderedDict(sorted(dict_New_Colnames.items(), key=lambda x: x[1][1]))
            dict_New_Colnames_Ordered = OrderedDict(([key_Colname, value_str_Function]) for key_Colname, (value_str_Function, value_int_Col_Order) in dict_New_Colnames_Sorted.items())
            
            '''Rearragen df columns with a reordered colnames list '''
            list_Df_Colnames_Reordered = [key_str_Colname for key_str_Colname in dict_New_Colnames_Ordered.keys()]
            df = df[list_Df_Colnames_Reordered]
            
            '''Rename columns '''
            str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__SAMPLING_INDIVS_Summary__Aggregate_Results
            list_Colname_Prefixes = [str_Source_File_Colname_Prefix_1]
            #list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames_Ordered)
            list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions_New(str_Colname_Prefix_1, dict_New_Colnames_Ordered, list_Colname_Prefixes)
            
            df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        pass
    
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df


    '''
    -------------------------------------------------------------
    CURRENT NEOGEN SPREADSHEET - Individuals Sampling Results - Aggregate Details into one Excel file
    -------------------------------------------------------------
    '''   
   
    def func__Sampling_Individuals_Results__Aggregate_And_Group(self, str_Excel_Save_Path, str_Search_Path):

        boolSuccess = False
       
        '''
        -------------------------------
        Specify Final Output File
        -------------------------------
        '''
        ''' Output file '''
        #str_Excel_Output_Colname_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__SAMPLING_INDIVS__Aggregate_Results
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__SAMPLING_INDIVS__Aggregate_Results
        #str_Excel_Output_FileName_Short_Name =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__Genepop_Allele_Freqs_By_Allele__SP_0_Full_PF__Aggregate_ALL__Summary_Results_Short_Name
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_Colname_Prefix

        #str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
        str_Excel_Output_Path_And_File_Name = str_Excel_Save_Path + '\\' + str_Excel_Output_File_WO_Suffix + '.xlsx'
          
        '''
        -------------------------------
        Get & Process Input files
        -------------------------------
        '''
        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  Individual Sampling
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_SheetName__SAMPLING_INDIVS__Aggregate_Results

        ''' Search file pattern '''
        str_Input_File_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__Sampling_Strategy_Results
        str_File_Search_Pattern = '*' + str_Input_File_Suffix
 
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Sheet_Name) 
        self.obj_Log_Default.info('Dataframing results with file of sarch pattern: ' + str_File_Search_Pattern + ' in search path: ' + str_Search_Path) 

        ''' Locate input files '''
        bool_File_Located = False
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
            
            '''Process each file in turn'''
            list_DFs = []
            df = None            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__Sampling_Individuals_Results__Aggregate_And_Group__Process(str_Path_And_File)
                list_DFs.append(df)
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name, list_Columns_To_Write=[], bool_NaN_As_NA = True) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
   
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Debug_Display.debug('Excel file written: ' + str_Excel_Output_Path_And_File_Name)
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written:'  + str_Excel_Output_Path_And_File_Name)
        else:
            self.obj_Log_Default.error('Some results files could not be located.  No Excel file written: '  + str_Excel_Output_Path_And_File_Name)
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__Sampling_Individuals_Results__Aggregate_And_Group__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)


        '''  REMOVE records where the sample size is 0 to speed up the sorting of this dataframe '''
        
        
        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        bool_Group_Calculate_And_Rename = True
        if bool_Group_Calculate_And_Rename:
            df = self.func__Sampling_Individuals_Results__Aggregate_And_Group__Process__Group_Calculate_And_Rename(df)
        pass
    
        ''' Sort & Reindex dataframe '''
        bool_Sort = True
        ''' Turn off sort by col name index to speed up processing '''
        if bool_Sort:
            df = self.func__Sort_Reindex_Dataframe(df)
        pass

        return df 

    def func__Sampling_Individuals_Results__Aggregate_And_Group__Process__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')


        '''
        -------------------------
        Remove File specific Colname prefix
        -------------------------
        '''
        ''' String to remove if required '''
        list_Remove_Colname_Text = [globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_Strategy_Results
                                    ,globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_100P_A_COHORTS_Results
                                    ,globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_FULL_EMBRYO_COHORT_Results
                                    ,globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_FULL_JUVENILE_COHORTS_Results
                                    ,globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_FULL_ADULT_COHORTS_Results
                                    ,globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_FULL_SAMPLING_OF_COHORTS_Results
                                    ,globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_SAMPLING_PROPORTIONS_SCALED_BY_MAX_PROPORTION_Results
                                    ,globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_Exp_2_2_Results
                                    ]
        #str_Remove_Colname_Text = globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_Exp_2_2_Results + '_'
        ''' String to add if required '''
        str_Add_Colname_Text = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__SAMPLING_INDIVS__Aggregate_Results + '_'
        ''' Rename '''
        self.obj_Log_Default.info('Remove file specific colname prefix from dataframe')
        list_Colname = df.columns
        list_Colnames_New = []
        for str_Colname in list_Colname:
            for str_Remove_Colname_Text in list_Remove_Colname_Text:
                str_Colname = str_Colname.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            pass
            list_Colnames_New.append(str_Colname)
        pass
    
        df.columns = list_Colnames_New

        bool_Group_By = False   
        if bool_Group_By:         
            '''
            -------------------------
            Specify Required Colnames
            -------------------------
            '''
            dict_Columns_Required_Plus_Function = OrderedDict()
            str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
            str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
            str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
            str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
            
            str_Source_File_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__SAMPLING_INDIVS__Aggregate_Results + '_'
            #str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_Strategy_Results
            
            '''Common experiment colnames'''
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
            dict_Columns_Required_Plus_Function[str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
            #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
            
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
            dict_Columns_Required_Plus_Function[str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
            #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_MatingsToSimulate] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_MatingsToSimulatePerReplicate] = str_Last
    
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
    
            ''' Indiv sampling experiment fields '''
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category_Code] = str_Last
            #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
            #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category] = str_Last
            #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category] = str_Last
            #dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_Ne2_Output.static_Str_Colname_Ne2_floatPCrit] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_strPCritsToProcess] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Search_Path] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sample_Each_Mating_Count_Divisible_By] = str_Last
    
            #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Pop_Sampling.static_Str_Colname_Sampling_Params] = str_Last
    
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = str_Last
            #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories] = str_Last
            #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Categories] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Indiv_Number] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Loci_Number] = str_Last
            
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicates] = str_Last 
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sampling_Replicate_Filename] = str_Last 
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_VSP_Ages_And_Sizes__Ages] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_VSP_Ages_And_Sizes__Sizes] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sample_VSP_Ages_And_Sizes__Sizes] = str_Last
            dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sample_Percent_VSP_Ages_And_Sizes__Sizes] = str_Last
            
            '''Get the Actual colnames given generic ones '''
            self.obj_Log_Default.info('Getting actual colnames from generic ones results')
            dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)

    
            '''
            -------------------------
            Perform GroupBy with Aggregate Functions
            -------------------------
            '''
            ''' Specify GroupBy keys '''
            str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_Strategy_Results
            str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
            #str_Group_Key_RunID = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
            #str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
            #str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
            #str_Group_Key_Mating_Count_Sim_Total = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total
            
            ''' Get Colname from key '''
            self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones with colname prefix: ' + str_Source_File_Colname_Prefix_1)
            str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
            #str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
            #str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
            #str_Col_Name_Mating_Count_Sim_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Sim_Total)
            
            ''' Perform GroupBy with aggregate '''
            self.obj_Log_Default.info('Grouping results')
            #df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Sim_Total], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
            #df = df.groupby([str_Col_Name_RunID, str_Col_Name_Mating_Count_Sim_Total], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
            df = df.groupby([str_Col_Name_RunID], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)
            
#             '''
#             -------------------------
#             Rename Colnames
#             -------------------------
#             '''
#             self.obj_Log_Default.info('Renaming results')
#             dict_New_Colnames = OrderedDict()
#             dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
#             #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
#             #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
#             #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
#             for key, value in dict_Columns_Required_Plus_Function.items():
#                 dict_New_Colnames[key] = value
#             pass
    
            '''
            -------------------------
            Accumulate New Colnames
            -------------------------
            '''
            ''' String to remove if required '''
            list_Remove_Colname_Text = [globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_Strategy_Results
                                        ,globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_100P_A_COHORTS_Results
                                        ,globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_FULL_EMBRYO_COHORT_Results
                                        ,globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_FULL_JUVENILE_COHORTS_Results
                                        ,globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_FULL_ADULT_COHORTS_Results
                                        ,globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_FULL_SAMPLING_OF_COHORTS_Results                                        
                                        ,globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_SAMPLING_PROPORTIONS_SCALED_BY_MAX_PROPORTION_Results                                        
                                        ,globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_Exp_2_2_Results
                                        ]
            #str_Remove_Colname_Text = globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Sampling_Exp_2_2_Results + '_'
            ''' String to add if required '''
            str_Add_Colname_Text = ''
            ''' Rename '''
            self.obj_Log_Default.info('Renaming results')
            dict_New_Colnames = OrderedDict()
            #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
            #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
            #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
            #dict_New_Colnames[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
            for key, value in dict_Columns_Required_Plus_Function.items():
                if len(list_Remove_Colname_Text) > 0:
                    for str_Remove_Colname_Text in list_Remove_Colname_Text:
                        key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
                    pass
                pass
                dict_New_Colnames[key_New] = value
            pass
             
            str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__SAMPLING_INDIVS__Aggregate_Results
            list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)
     
            df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        pass


    
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df

    '''
    -------------------------------------------------------------
    Genepop Allele Freqs By Allele Per Fertilization PF Results - Aggregate Details into one Excel file
    -------------------------------------------------------------
    '''   
    def func__Genepop_Allele_Freqs_By_Allele_Aggregate_Results__Aggregate_And_Group___At_Lowest_Detail(self, str_Search_Path):

        boolSuccess = False
       
        '''
        -------------------------------
        Specify Final Output File
        -------------------------------
        '''
        ''' Output file '''
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__Genepop_Allele_Freqs_By_Allele__Aggregate_ALL__Summary_Results
        str_Excel_Output_FileName_Short_Name =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__Genepop_Allele_Freqs_By_Allele__SP_0_Full_PF__Aggregate_ALL__Summary_Results_Short_Name
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName + '_' + str_Excel_Output_FileName_Short_Name

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)

        
        '''
        -------------------------------
        Get & Process Input files
        -------------------------------
        '''
        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  Embryo VSP Genepop_Allele_Freqs_By_Allele_Results
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__Genepop_Allele_Freqs_By_Allele__Embryo_PF__Aggregate_ALL__Summary_Results_Sheet_Name

        ''' Search file pattern '''
        str_Genepop_File_Suffix = globalsSS.Genepop_Results_File_Details.static_Genepop_File_Suffix__Embryo_VSP_Post_Fertilization.replace('.','')
        str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__Genepop_Allele_Freq_By_Allele_PF_Results + str_Genepop_File_Suffix
        str_File_Search_Pattern = '*' + str_Logger_FileName_Suffix
 
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Sheet_Name) 
        self.obj_Log_Default.info('Dataframing results with file of sarch pattern: ' + str_File_Search_Pattern + ' in search path: ' + str_Search_Path) 

        ''' Locate input files '''
        bool_File_Located = False
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
            
            '''Process each file in turn'''
            list_DFs = []
            df = None            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__Genepop_Allele_Freqs_By_Allele_Aggregate_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
   
        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  Mature VSP Genepop_Allele_Freqs_By_Allele_Results
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__Genepop_Allele_Freqs_By_Allele__Mature_PF__Aggregate_ALL__Summary_Results_Sheet_Name

        ''' Search file pattern '''
        str_Genepop_File_Suffix = globalsSS.Genepop_Results_File_Details.static_Genepop_File_Suffix__Mature_VSP_Post_Fertilization.replace('.','')
        str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__Genepop_Allele_Freq_By_Allele_PF_Results + str_Genepop_File_Suffix
        str_File_Search_Pattern = '*' + str_Logger_FileName_Suffix
 
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Sheet_Name) 
        self.obj_Log_Default.info('Dataframing results with file of sarch pattern: ' + str_File_Search_Pattern + ' in search path: ' + str_Search_Path) 

        ''' Locate input files '''
        bool_File_Located = False
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
            
            '''Process each file in turn'''
            list_DFs = []
            df = None            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__Genepop_Allele_Freqs_By_Allele_Aggregate_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
   
        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  SP_0_Full Genepop_Allele_Freqs_By_Allele_Results
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__Genepop_Allele_Freqs_By_Allele__SP_0_Full_PF__Aggregate_ALL__Summary_Results_Sheet_Name

        ''' Search file pattern '''
        str_Genepop_File_Suffix = globalsSS.Genepop_Results_File_Details.static_Genepop_File_Suffix__Full_SP_Post_Fertilization.replace('.','')
        str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__Genepop_Allele_Freq_By_Allele_PF_Results + str_Genepop_File_Suffix
        str_File_Search_Pattern = '*' + str_Logger_FileName_Suffix
 
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_Excel_Output_FileName + ' and for SHEET: ' + str_Sheet_Name) 
        self.obj_Log_Default.info('Dataframing results with file of sarch pattern: ' + str_File_Search_Pattern + ' in search path: ' + str_Search_Path) 

        ''' Locate input files '''
        bool_File_Located = False
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
            
            '''Process each file in turn'''
            list_DFs = []
            df = None            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__Genepop_Allele_Freqs_By_Allele_Aggregate_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Default.info('Excel file written.')
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written')
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__Genepop_Allele_Freqs_By_Allele_Aggregate_Results__Aggregate_And_Group__At_Lowest_Detail__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__Genepop_Allele_Freqs_By_Allele_Aggregate_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

    def func__Genepop_Allele_Freqs_By_Allele_Aggregate_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_File_Heading__Prefix_1__Genepop_Allele_Freq_By_Allele_PF_Results
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_Data_Unique_Run_ID] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_Data_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_Data_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_Data_Sim_Current_Replicate_Mating] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Population_Sampled] = str_Last


        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Genepop_Allele_Freqs_By_Allele_Results.static_str_Colname_Pop_Name] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Genepop_Allele_Freqs_By_Allele_Results.static_str_Colname_Pop_Gene_Count] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_Genepop_Allele_Freqs_By_Allele_Results.static_str_Colname_Locus_Allele_Freqs] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Genepop_Allele_Freqs_By_Allele_Results.static_str_Colname_Locus_Name] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Genepop_Allele_Freqs_By_Allele_Results.static_str_Colname_Allele_Name] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_Genepop_Allele_Freqs_By_Allele_Results.static_str_Colname_Allele_Freq] = str_Last


        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Source_File_Colname_Prefix_2 = globalsSS.Logger_Results_File_Details.static_Logger_File_Heading__Prefix_1__Genepop_Allele_Freq_By_Allele_PF_Results
        str_Group_Key_SourceRunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_Data_Unique_Run_ID
        str_Group_Key_SourceBatch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_Data_Sim_Current_Batch
        str_Group_Key_SourceReplicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_Data_Sim_Current_Replicate
        str_Group_Key_Result_MultiLine_Count = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_SourceRunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_SourceRunID)
        str_Col_Name_SourceBatch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_SourceBatch)
        str_Col_Name_SourceReplicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_SourceReplicate)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_SourceRunID, str_Col_Name_SourceBatch, str_Col_Name_SourceReplicate, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Rename Colnames
        -------------------------
        '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_Data_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_Data_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Source_Data_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__Genepop_Allele_Freqs_By_Allele__Aggregate_ALL__Summary_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df


    
    '''
    -------------------------------------------------------------
    AgeNe Man Per Replicate EOR Results - Aggregate AgeNe Details, AgeNe Life Table Totals, AgeNe Demographic Table Totals, AgeNe Overall Totals into one Excel file
    -------------------------------------------------------------
    '''   
    def func__AgeNe_Man_EOR_Aggregate_Results__Aggregate_And_Group___At_Lowest_Detail(self, str_Search_Path):

        boolSuccess = False
       
        '''
        -------------------------------
        Specify Final Output File
        -------------------------------
        '''
        ''' Output file '''
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Man_Aggregate_ALL_EOR__Summary_Results
        str_Excel_Output_FileName_Short_Name =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Man_Aggregate_ALL_EOR__Summary_Results_Short_Name
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_FileName_Short_Name
        
        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)

        
        '''
        -------------------------------
        Get & Process Input files
        -------------------------------
        '''
        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  AgeNe Details
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Man_Details_EOR_Results
        
        bool_File_Located = False
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Man_Details_EOR_Results
 
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_File_Search_Pattern)
        
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
            
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__AgeNe_Man_EOR_Aggregate_AgeNe_Details_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    

        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  AgeNe LifeTable Totals
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Man_LifeTables_Total_EOR_Results
         
        bool_File_Located = False
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Man_LifeTables_Total_EOR_Results
  
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_File_Search_Pattern)
         
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
             
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__AgeNe_Man_EOR_Aggregate_AgeNe_LifeTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass
 
            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                 
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                 
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass
 
            df = df_Aggregate 
             
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
             
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
     
        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  AgeNe DemographicTable Totals
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Man_DemographicTables_Total_EOR_Results
         
        bool_File_Located = False
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Man_DemographicTables_Total_EOR_Results
  
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_File_Search_Pattern)
         
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
             
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__AgeNe_Man_EOR_Aggregate_AgeNe_DemographicTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass
 
            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                 
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                 
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass
 
            df = df_Aggregate 
             
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
             
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
     
        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  AgeNe Final Overall Totals
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Man_Final_Totals_EOR_Results
         
        bool_File_Located = False
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Man_Final_Totals_EOR_Results
  
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_File_Search_Pattern)
         
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
             
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__AgeNe_Man_EOR_Aggregate_AgeNe_FinalOverallTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass
 
            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                 
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                 
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass
 
            df = df_Aggregate 
             
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
             
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Default.info('Excel file written.')
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written')
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__AgeNe_Man_EOR_Aggregate_AgeNe_Details_Results__Aggregate_And_Group__At_Lowest_Detail__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Man_EOR_Aggregate_AgeNe_Details_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

    def func__AgeNe_Man_EOR_Aggregate_AgeNe_Details_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Last


        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Man_Details_EOR_Results
        str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        #str_Group_Key_Sex = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Result_MultiLine_Count = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        #str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Rename Colnames
        -------------------------
        '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Details_EOR_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df

    def func__AgeNe_Man_EOR_Aggregate_AgeNe_LifeTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Man_EOR_Aggregate_AgeNe_LifeTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

    def func__AgeNe_Man_EOR_Aggregate_AgeNe_LifeTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_LifeTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Last


        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Man_LifeTables_Total_EOR_Results
        str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        #str_Group_Key_Sex = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Result_MultiLine_Count = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        #str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Rename Colnames
        -------------------------
        '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_LifeTables_Total_EOR_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df

    def func__AgeNe_Man_EOR_Aggregate_AgeNe_DemographicTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Man_EOR_Aggregate_AgeNe_DemographicTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

    def func__AgeNe_Man_EOR_Aggregate_AgeNe_DemographicTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_DemographicTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All] = str_Last



        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Man_DemographicTables_Total_EOR_Results
        str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        #str_Group_Key_Sex = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Result_MultiLine_Count = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        #str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Rename Colnames
        -------------------------
        '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_DemographicTables_Total_EOR_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df

    def func__AgeNe_Man_EOR_Aggregate_AgeNe_FinalOverallTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Man_EOR_Aggregate_AgeNe_FinalOverallTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

    def func__AgeNe_Man_EOR_Aggregate_AgeNe_FinalOverallTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Man_Final_Totals_EOR_Results
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_FinalOverall_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nc_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NbDemo] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemo] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNcAdultsOverall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNOverall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_kbar_All_Sexes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Male_N1_Ratio] = str_Mean

        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Man_Final_Totals_EOR_Results
        str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        #str_Group_Key_Sex = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Result_MultiLine_Count = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        #str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Rename Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Man_Final_Totals_EOR_Results
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Man_Final_Totals_EOR_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df

    '''
    -------------------------------------------------------------
    AgeNe Sim Per Replicate EOR Results - Aggregate AgeNe Details, AgeNe Life Table Totals, AgeNe Demographic Table Totals, AgeNe Overall Totals into one Excel file
    -------------------------------------------------------------
    '''   
    def func__AgeNe_Sim_EOR_Aggregate_Results__Aggregate_And_Group___At_Lowest_Detail(self, str_Search_Path):

        boolSuccess = False
       
        '''
        -------------------------------
        Specify Final Output File
        -------------------------------
        '''
        ''' Output file '''
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Sim_Aggregate_ALL_EOR__Summary_Results
        str_Excel_Output_FileName_Short_Name =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Sim_Aggregate_ALL_EOR__Summary_Results_Short_Name
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_FileName_Short_Name

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
        
        '''
        -------------------------------
        Get & Process Input files
        -------------------------------
        '''
        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  AgeNe Details
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_Details_EOR_Results
        
        bool_File_Located = False
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_Details_EOR_Results
 
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_File_Search_Pattern)
        
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
            
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__AgeNe_Sim_EOR_Aggregate_AgeNe_Details_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    

        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  AgeNe LifeTable Totals
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_LifeTables_Total_EOR_Results
         
        bool_File_Located = False
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_LifeTables_Total_EOR_Results
  
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_File_Search_Pattern)
         
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
             
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__AgeNe_Sim_EOR_Aggregate_AgeNe_LifeTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass
 
            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                 
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                 
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass
 
            df = df_Aggregate 
             
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
             
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
     
        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  AgeNe DemographicTable Totals
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_DemographicTables_Total_EOR_Results
         
        bool_File_Located = False
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_DemographicTables_Total_EOR_Results
  
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_File_Search_Pattern)
         
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
             
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__AgeNe_Sim_EOR_Aggregate_AgeNe_DemographicTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass
 
            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                 
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                 
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass
 
            df = df_Aggregate 
             
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
             
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
     
        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  AgeNe Final Overall Totals
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_Final_Totals_EOR_Results
         
        bool_File_Located = False
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_Final_Totals_EOR_Results
  
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_File_Search_Pattern)
         
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
             
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__AgeNe_Sim_EOR_Aggregate_AgeNe_FinalOverallTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass
 
            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                 
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                 
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass
 
            df = df_Aggregate 
             
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
             
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Default.info('Excel file written.')
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written')
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__AgeNe_Sim_EOR_Aggregate_AgeNe_Details_Results__Aggregate_And_Group__At_Lowest_Detail__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_EOR_Aggregate_AgeNe_Details_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

    def func__AgeNe_Sim_EOR_Aggregate_AgeNe_Details_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Last


        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_Details_EOR_Results
        str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        #str_Group_Key_Sex = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Result_MultiLine_Count = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        #str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Rename Colnames
        -------------------------
        '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Details_EOR_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df

    def func__AgeNe_Sim_EOR_Aggregate_AgeNe_LifeTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_EOR_Aggregate_AgeNe_LifeTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

    def func__AgeNe_Sim_EOR_Aggregate_AgeNe_LifeTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_LifeTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Last


        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_LifeTables_Total_EOR_Results
        str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        #str_Group_Key_Sex = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Result_MultiLine_Count = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        #str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Rename Colnames
        -------------------------
        '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_LifeTables_Total_EOR_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df

    def func__AgeNe_Sim_EOR_Aggregate_AgeNe_DemographicTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_EOR_Aggregate_AgeNe_DemographicTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

    def func__AgeNe_Sim_EOR_Aggregate_AgeNe_DemographicTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_DemographicTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All] = str_Last



        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_DemographicTables_Total_EOR_Results
        str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        #str_Group_Key_Sex = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Result_MultiLine_Count = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        #str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Rename Colnames
        -------------------------
        '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_DemographicTables_Total_EOR_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df

    def func__AgeNe_Sim_EOR_Aggregate_AgeNe_FinalOverallTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_EOR_Aggregate_AgeNe_FinalOverallTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

    def func__AgeNe_Sim_EOR_Aggregate_AgeNe_FinalOverallTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_Final_Totals_EOR_Results
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_FinalOverall_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nc_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NbDemo] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemo] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNcAdultsOverall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNOverall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_kbar_All_Sexes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Male_N1_Ratio] = str_Mean
        
        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_Final_Totals_EOR_Results
        str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        #str_Group_Key_Sex = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex
        str_Group_Key_Result_MultiLine_Count = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        #str_Col_Name_Sex = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Sex)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Rename Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_Final_Totals_EOR_Results
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''        
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        #dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Final_Totals_EOR_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df

    '''
    -------------------------------------------------------------
    AgeNe Sim Per Replicate PF Results - Aggregate AgeNe Details, AgeNe Life Table Totals, AgeNe Demographic Table Totals, AgeNe Overall Totals into one Excel file
    -------------------------------------------------------------
    '''   
    def func__AgeNe_Sim_PF_Aggregate_Results__Aggregate_And_Group___At_Lowest_Detail(self, str_Search_Path):

        boolSuccess = False
       
        '''
        -------------------------------
        Specify Final Output File
        -------------------------------
        '''
        ''' Output file '''
        str_Excel_Output_FileName =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Sim_Aggregate_ALL_PF__Summary_Results
        str_Excel_Output_FileName_Short_Name =  globalsSS.Excel_Results_File_Details.static_Excel_FileName__AgeNe_Sim_Aggregate_ALL_PF__Summary_Results_Short_Name
        
        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_FileName #+ '_' + str_Excel_Output_FileName_Short_Name

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
        
        '''
        -------------------------------
        Get & Process Input files
        -------------------------------
        '''
        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  AgeNe Details
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_Details_PF_Results
        
        bool_File_Located = False
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_Details_PF_Results
 
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_File_Search_Pattern)
        
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
            
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__AgeNe_Sim_PF_Aggregate_AgeNe_Details_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass

            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass

            df = df_Aggregate 
            
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
            
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    

        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  AgeNe LifeTable Totals
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_LifeTables_Total_PF_Results
         
        bool_File_Located = False
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_LifeTables_Total_PF_Results
  
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_File_Search_Pattern)
         
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
             
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__AgeNe_Sim_PF_Aggregate_AgeNe_LifeTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass
 
            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                 
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                 
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass
 
            df = df_Aggregate 
             
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
             
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
     
        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  AgeNe DemographicTable Totals
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_DemographicTables_Total_PF_Results
         
        bool_File_Located = False
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_DemographicTables_Total_PF_Results
  
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_File_Search_Pattern)
         
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
             
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__AgeNe_Sim_PF_Aggregate_AgeNe_DemographicTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass
 
            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                 
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                 
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass
 
            df = df_Aggregate 
             
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
             
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
     
        '''
        ~~~~~~~~~~~~~~~~~~~
        Process files for:  AgeNe Final Overall Totals
        ~~~~~~~~~~~~~~~~~~~
        '''
        ''' Excel Output Sheet '''
        str_Sheet_Name =  globalsSS.Excel_Results_File_Details.static_Excel_SheetName__AgeNe_Sim_Final_Totals_PF_Results
         
        bool_File_Located = False
        str_File_Search_Pattern = '*' + globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_Final_Totals_PF_Results
  
        '''
        Aggregate Data to dataframe from each input file
        '''
        self.obj_Log_Default.info('Dataframing results for: ' + str_File_Search_Pattern)
         
        ''' Locate input files '''
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        if bool_File_Located:
             
            '''Process each file in turn'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                df = self.func__AgeNe_Sim_PF_Aggregate_AgeNe_FinalOverallTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(str_Path_And_File)
                list_DFs.append(df)
            pass
 
            ''' Concatinate the dfs '''
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                #DEBUG_ON
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                #DEBUG_OFF
                 
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                 
                #DEBUG_ON
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
                #DEBUG_OFF
            pass
 
            df = df_Aggregate 
             
            #DEBUG_ON
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
            #DEBUG_OFF
             
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name) 
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        ''' final save of the excel file '''
        if bool_File_Located:
            try:
                boolSuccess = True
                self.func_Save_Excel_Writer(writer)
                self.obj_Log_Default.info('Excel file written.')
            except:
                boolSuccess = False
                self.obj_Log_Default.error('Excel save error.  No Excel file written')
        else:
            self.obj_Log_Default.error('Some results files could be located.  No Excel file written')
            boolSuccess = False
        pass
        
        return boolSuccess

    def func__AgeNe_Sim_PF_Aggregate_AgeNe_Details_Results__Aggregate_And_Group__At_Lowest_Detail__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_PF_Aggregate_AgeNe_Details_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

    def func__AgeNe_Sim_PF_Aggregate_AgeNe_Details_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_Details '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Age] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_sx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_lx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxlx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_b_x] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Bx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_xBx_Div_N1] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Dx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarAll] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_delta_kbar] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDIx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDGx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSDx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Yx] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All] = str_Last


        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_Details_PF_Results
        str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Mating_Count_Replicate_Total = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_Result_MultiLine_Count = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Rename Colnames
        -------------------------
        '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Details_PF_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df

    def func__AgeNe_Sim_PF_Aggregate_AgeNe_LifeTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_PF_Aggregate_AgeNe_LifeTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

    def func__AgeNe_Sim_PF_Aggregate_AgeNe_LifeTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_LifeTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_N_Adults] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_Nc_Adults] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nx_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_bxNx_Sum_All] = str_Last


        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_LifeTables_Total_PF_Results
        str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Mating_Count_Replicate_Total = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_Result_MultiLine_Count = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Rename Colnames
        -------------------------
        '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_LifeTables_Total_PF_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df

    def func__AgeNe_Sim_PF_Aggregate_AgeNe_DemographicTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_PF_Aggregate_AgeNe_DemographicTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

    def func__AgeNe_Sim_PF_Aggregate_AgeNe_DemographicTableTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_DemographicTable_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_SSD_T] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_All] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbarx_Dx_All] = str_Last



        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_DemographicTables_Total_PF_Results
        str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Mating_Count_Replicate_Total = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_Result_MultiLine_Count = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Rename Colnames
        -------------------------
        '''
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            dict_New_Colnames[key] = value
        pass
    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_DemographicTables_Total_PF_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df

    def func__AgeNe_Sim_PF_Aggregate_AgeNe_FinalOverallTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Process(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Processing file: ' + str_Path_And_File)

        '''Aggregate Results to dataframe'''        
        df = self.func__Aggregate_Input_File_To_Dataframe(str_Path_And_File)

        ''' Transform dataframe columns'''
        df = self.func__Transform_Dataframe_Column_Datatypes(df)

        '''
        ---------------------
        Group/Calculate/Rename
        ---------------------
        '''
        df = self.func__AgeNe_Sim_PF_Aggregate_AgeNe_FinalOverallTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(df)
        
    
        ''' Sort & Reindex dataframe '''
        df = self.func__Sort_Reindex_Dataframe(df)


        return df 

    def func__AgeNe_Sim_PF_Aggregate_AgeNe_FinalOverallTotals_Results__Aggregate_And_Group__At_Lowest_Detail__Group_Calculate_And_Rename(self, df):

        self.obj_Log_Default.info('Grouping, Calculating & Renaming results')
        
        '''
        -------------------------
        Specify Required Colnames
        -------------------------
        '''
        dict_Columns_Required_Plus_Function = OrderedDict()
        str_First = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__first
        str_Last = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__last
        str_Sum = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__sum
        str_Mean = globalsSS.Pandas_Aggregate_Function_Keyword.static_str_Pandas_Aggregate_Function_Keyword__mean
        
        str_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_Final_Totals_PF_Results
        '''Common experiment colnames'''
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = str_Last
        
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = str_Last


        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = str_Last
        #dict_Columns_Required_Plus_Function[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_Columns_Required_Plus_Function[str_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Last

        ''' Colnames_AgeNe_FinalOverall_Totals '''
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_L_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nc_Adults_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_N_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NbDemo] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemo] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNcAdultsOverall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_NeDemoDivNOverall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Vk_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_kbar_Overall] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_Vx_All_Sexes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Nb_kbar_All_Sexes] = str_Last
        dict_Columns_Required_Plus_Function[globalsSS.Colnames_AgeNe_Results.static_str_Colname_Male_N1_Ratio] = str_Mean
        
        '''Get the Actual colnames given generic ones '''
        self.obj_Log_Default.info('Getting actual colnames from generic ones results')
        dict_Specific_Columns_Required_Plus_Function = self.func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(df, dict_Columns_Required_Plus_Function)
        
        '''
        -------------------------
        Perform GroupBy with Aggregate Functions
        -------------------------
        '''
        ''' Specify GroupBy keys '''
        str_Source_File_Colname_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_Final_Totals_PF_Results
        str_Group_Key_RunID = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID
        str_Group_Key_Batch = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch
        str_Group_Key_Replicate = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate
        str_Group_Key_Mating_Count_Replicate_Total = str_Source_File_Colname_Prefix_1 + globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total
        str_Group_Key_Result_MultiLine_Count = globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count
        
        ''' Get Colname from key '''
        self.obj_Log_Default.info('Getting actual GROUPBY KEY colnames from generic ones')
        str_Col_Name_RunID = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_RunID)
        str_Col_Name_Batch = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Batch)
        str_Col_Name_Replicate = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Replicate)
        str_Col_Name_Mating_Count_Replicate_Total = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Mating_Count_Replicate_Total)
        str_Col_Name_Result_MultiLine_Count = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Group_Key_Result_MultiLine_Count)
        
        ''' Perform GroupBy with aggregate '''
        self.obj_Log_Default.info('Grouping results')
        df = df.groupby([str_Col_Name_RunID, str_Col_Name_Batch, str_Col_Name_Replicate, str_Col_Name_Mating_Count_Replicate_Total, str_Col_Name_Result_MultiLine_Count], as_index=False).agg(dict_Specific_Columns_Required_Plus_Function)

        '''
        -------------------------
        Rename Colnames
        -------------------------
        '''
        ''' String to remove if required '''
        str_Remove_Colname_Text = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_Final_Totals_PF_Results
        ''' String to add if required '''
        str_Add_Colname_Text = ''
        ''' Rename '''        
        self.obj_Log_Default.info('Renaming results')
        dict_New_Colnames = OrderedDict()
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = str_Last
        dict_New_Colnames[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Result_MultiLine_Count] = str_Last
        for key, value in dict_Columns_Required_Plus_Function.items():
            key_New = key.replace(str_Remove_Colname_Text, str_Add_Colname_Text)
            dict_New_Colnames[key_New] = value
        pass
    
        str_Colname_Prefix_1 = globalsSS.Excel_Results_File_Details.static_Excel_Colname_Prefix__AgeNe_Sim_Final_Totals_PF_Results
        list_New_Colnames = self.func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(str_Colname_Prefix_1, dict_New_Colnames)

        df = self.func_Rename_Columns_From_List(df, list_New_Colnames)    
        
        #DEBUG_ON
        #str_Df = df.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OF       
        
        return df

    '''
    -------------------------------------------------------------
    SS LEVEL Results
    -------------------------------------------------------------
    '''   
    
    def func_Aggregate_SS_LEVEL_Stats(self, str_Search_Path):

        boolSuccess = False
 
        #str_Search_Path = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\Shared_Data\\LEVEL_Stats_Test'
        #str_Search_Path = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\SharkSim\\v2_54_Py27\\Test\\NEW_AGE_V1'
       
        '''
        Process Results
        '''

        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Rep = str(self.objSSParametersLocal.intCurrentReplicate)
        #str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_Aggregate_Results_Rep_' + str_Rep.zfill(len(str_Rep)+1)   
        str_Excel_Output_File_Name_Prefix = globalsSS.Excel_Results_File_Details.static_Excel_FileName__SS_LEVEL_Results
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_' + str_Excel_Output_File_Name_Prefix + '_' + str_Rep.zfill(len(str_Rep)+1)   

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
                
        '''
        Process LEVEL - SIM
        '''
        self.obj_Log_Default.info('Aggregating results for SS LEVEL stats')
        
        '''Get LEVEL stats'''
        self.obj_Log_Default.info('Aggregating results for SS LEVEL - SIM')
        
        str_File_Search_Pattern = '*' + globalsSS.SS_Level_Details.static_Output_File_Suffix__Level_SIM
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_Located:
            
            '''Process SIM Results'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df = self.func_Aggregate_SS_LEVEL_SIM_Results(str_Path_And_File)
                list_DFs.append(df)
            pass

            '''
            Write results to Excel
            '''
            #str_Sheet_Name = 'SIM'
            str_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__SS_LEVEL_SIM_Results
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name)            
                
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

        '''
        Process LEVEL - BATCH
        '''
        
        '''Get LEVEL stats'''
        self.obj_Log_Default.info('Aggregating results for SS LEVEL - BATCH')
        
        str_File_Search_Pattern = '*' + globalsSS.SS_Level_Details.static_Output_File_Suffix__Level_BATCH
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_Located:
            
            '''Process BATCH Results'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df = self.func_Aggregate_SS_LEVEL_BATCH_Results(str_Path_And_File)
                list_DFs.append(df)
            pass

            '''
            Write results to Excel
            '''
            #str_Sheet_Name = 'BATCH'
            str_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__SS_LEVEL_BATCH_Results
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name)            
                
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

        '''
        Process LEVEL - REPLICATE
        '''
        
        '''Get LEVEL stats'''
        self.obj_Log_Default.info('Aggregating results for SS LEVEL - REPLICATE EOR - End of Replicate')
        
        str_File_Search_Pattern = '*' + globalsSS.SS_Level_Details.static_Output_File_Suffix__Level_REPLICATE_EOR
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_Located:
            
            '''Process REPLICATE Results'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df = self.func_Aggregate_SS_LEVEL_REPLICATE_Results(str_Path_And_File)
                list_DFs.append(df)
            pass

            '''
            Write results to Excel
            '''
            #str_Sheet_Name = 'REPLICATE_EOR'
            str_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__SS_LEVEL_REPLICATE_EOR_Results
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name)            
                
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        '''Get LEVEL stats'''
        self.obj_Log_Default.info('Aggregating results for SS LEVEL - REPLICATE PF - Post-fertilization')
        
        str_File_Search_Pattern = '*' + globalsSS.SS_Level_Details.static_Output_File_Suffix__Level_REPLICATE_PF
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_Located:
            
            '''Process REPLICATE Results'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df = self.func_Aggregate_SS_LEVEL_REPLICATE_Results(str_Path_And_File)
                list_DFs.append(df)
            pass

            '''
            Write results to Excel
            '''
            #str_Sheet_Name = 'REPLICATE_PF'
            str_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__SS_LEVEL_REPLICATE_PF_Results
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name)            
                
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

        '''
        Process LEVEL - VSP
        '''
        
        '''Get LEVEL stats'''
        self.obj_Log_Default.info('Aggregating results for SS LEVEL - VSP AC EOR - Age Class - End of Replicate')
        
        str_File_Search_Pattern = '*' + globalsSS.SS_Level_Details.static_Output_File_Suffix__Level_Age_Class_VSP_EOR
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_Located:
            
            '''Process VSP Results'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df = self.func_Aggregate_SS_LEVEL_VSP_Results(str_Path_And_File)
                list_DFs.append(df)
            pass

            '''
            Write results to Excel
            '''
            #str_Sheet_Name = 'VSP_AC_EOR'
            str_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__SS_LEVEL_VSP_AgeCohort_EOR_Results
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name)            
                
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

        '''Get LEVEL stats'''
        self.obj_Log_Default.info('Aggregating results for SS LEVEL - VSP AC PF - Age Class - Post-Fertilization')
        
        str_File_Search_Pattern = '*' + globalsSS.SS_Level_Details.static_Output_File_Suffix__Level_Age_Class_VSP_PF
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_Located:
            
            '''Process VSP Results'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df = self.func_Aggregate_SS_LEVEL_VSP_Results(str_Path_And_File)
                list_DFs.append(df)
            pass

            '''
            Write results to Excel
            '''
            #str_Sheet_Name = 'VSP_AC_PF'
            str_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__SS_LEVEL_VSP_AgeCohort_PF_Results
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name)            
                
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

        '''Get LEVEL stats'''
        self.obj_Log_Default.info('Aggregating results for SS LEVEL - VSP LS EOR - Life Stage - End of Replicate')
        
        str_File_Search_Pattern = '*' + globalsSS.SS_Level_Details.static_Output_File_Suffix__Level_Life_Stage_VSP_EOR
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_Located:
            
            '''Process VSP Results'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df = self.func_Aggregate_SS_LEVEL_VSP_Results(str_Path_And_File)
                list_DFs.append(df)
            pass

            '''
            Write results to Excel
            '''
            #str_Sheet_Name = 'VSP_LS_EOR'
            str_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__SS_LEVEL_VSP_LifeStage_EOR_Results
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name)            
                
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

        '''Get LEVEL stats'''
        self.obj_Log_Default.info('Aggregating results for SS LEVEL - VSP LS PF - Age Class - Post-Fertilization')
        
        str_File_Search_Pattern = '*' + globalsSS.SS_Level_Details.static_Output_File_Suffix__Level_Life_Stage_VSP_PF
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_Located:
            
            '''Process VSP Results'''
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df = self.func_Aggregate_SS_LEVEL_VSP_Results(str_Path_And_File)
                list_DFs.append(df)
            pass

            '''
            Write results to Excel
            '''
            #str_Sheet_Name = 'VSP_LS_PF'
            str_Sheet_Name = globalsSS.Excel_Results_File_Details.static_Excel_SheetName__SS_LEVEL_VSP_LifeStage_PF_Results
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name)            
                
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass


        
        ''' final save of the excel file '''
        if bool_File_Located:
            self.func_Save_Excel_Writer(writer)
        else:
            self.obj_Log_Default.error('NO Results files could be located.  No Excel file written')
        pass
        
        return True


    def func_Aggregate_SS_LEVEL_SIM_Results(self, str_Path_And_File):
        
        '''Process HWE Results'''
        dictResults = self.func_Aggregate_Results(str_Path_And_File)
        df = self.func_Manipulate_SS_LEVEL_SIM(dictResults)

        return df


    def func_Aggregate_SS_LEVEL_BATCH_Results(self, str_Path_And_File):
        
        '''Process HWE Results'''
        dictResults = self.func_Aggregate_Results(str_Path_And_File)
        df = self.func_Manipulate_SS_LEVEL_BATCH(dictResults)

        return df


    def func_Aggregate_SS_LEVEL_REPLICATE_Results(self, str_Path_And_File):
        
        '''Process HWE Results'''
        dictResults = self.func_Aggregate_Results(str_Path_And_File)
        df = self.func_Manipulate_SS_LEVEL_REPLICATE(dictResults)

        return df


    def func_Aggregate_SS_LEVEL_VSP_Results(self, str_Path_And_File):
        
        '''Process HWE Results'''
        dictResults = self.func_Aggregate_Results(str_Path_And_File)
        df = self.func_Manipulate_SS_LEVEL_VSP(dictResults)

        return df


    def func_Manipulate_SS_LEVEL_SIM(self, dictResults):

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()
                    
        '''create dataframe'''
        df = pandas.DataFrame.from_dict(dictResults,'columns', float)
        
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        '''convert non-numerics to numerics'''
        df.convert_objects(convert_numeric=True)
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        
        '''
        Sort DF Columns
        '''
        '''re-arrange columns based on the col name col index prefix number'''
        df = df.reindex_axis(sorted(df.columns), axis=1)        
        
#         '''
#         Apply interpretations to the results
#         '''
#         df = self.func_Interpret_HWE_P_Values(df)
        

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            '''log the results'''
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe: %s' % str_Df)
            #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
            t2.Stop(self.obj_Log_Debug_Display)
        
        return df


    def func_Manipulate_SS_LEVEL_BATCH(self, dictResults):

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()
                    
        '''create dataframe'''
        df = pandas.DataFrame.from_dict(dictResults,'columns', float)
        
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        '''convert non-numerics to numerics'''
        df.convert_objects(convert_numeric=True)
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        
        '''
        Sort DF Columns
        '''
        '''re-arrange columns based on the col name col index prefix number'''
        df = df.reindex_axis(sorted(df.columns), axis=1)        
        
#         '''
#         Apply interpretations to the results
#         '''
#         df = self.func_Interpret_HWE_P_Values(df)
        

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            '''log the results'''
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe: %s' % str_Df)
            #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
            t2.Stop(self.obj_Log_Debug_Display)
        
        return df


    def func_Manipulate_SS_LEVEL_REPLICATE(self, dictResults):

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()
                    
        '''create dataframe'''
        df = pandas.DataFrame.from_dict(dictResults,'columns', float)
        
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        '''convert non-numerics to numerics'''
        df.convert_objects(convert_numeric=True)
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        
        '''
        Sort DF Columns
        '''
        '''re-arrange columns based on the col name col index prefix number'''
        df = df.reindex_axis(sorted(df.columns), axis=1)        
        
#         '''
#         Apply interpretations to the results
#         '''
#         df = self.func_Interpret_HWE_P_Values(df)
        

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            '''log the results'''
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe: %s' % str_Df)
            #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
            t2.Stop(self.obj_Log_Debug_Display)
        
        return df


    def func_Manipulate_SS_LEVEL_VSP(self, dictResults):

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()
                    
        '''create dataframe'''
        df = pandas.DataFrame.from_dict(dictResults,'columns', float)
        
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        '''convert non-numerics to numerics'''
        df.convert_objects(convert_numeric=True)
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        
        '''
        Sort DF Columns
        '''
        '''re-arrange columns based on the col name col index prefix number'''
        df = df.reindex_axis(sorted(df.columns), axis=1)        
        
#         '''
#         Apply interpretations to the results
#         '''
#         df = self.func_Interpret_HWE_P_Values(df)
        

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            '''log the results'''
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe: %s' % str_Df)
            #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
            t2.Stop(self.obj_Log_Debug_Display)
        
        return df


    '''
    -------------------------------------------------------------
    GENEPOP Results
    -------------------------------------------------------------
    '''
       
    def func_Aggregate_Genpop_Stats(self, str_Search_Path):

        boolSuccess = False
         
        #str_Search_Path = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\Shared_Data\\GP_Test\\BioP_Stats'
        #str_Search_Path = 'C:\\DCB\\MUI\\MUI_Sync_Auto\\MUI_A_Analyses\\SharkSim\\v2_54_Py27\\Test\\NEW_AGE_V1'
        
        '''
        Process Results
        '''

        ''' Get Initial Excel Writer to write all subsequent data sheets'''
        str_Rep = str(self.objSSParametersLocal.intCurrentReplicate)
        str_Excel_Output_File_WO_Suffix = self.objSSParametersLocal.strUniqueRunID + '_Aggregate_Genepop_Rep_' + str_Rep.zfill(len(str_Rep)+1)   

        str_Excel_Save_Path = self.objSSParametersLocal.str_Current_Run_Path
        writer = self.func_Get_Excel_Writer(str_Excel_Save_Path, str_Excel_Output_File_WO_Suffix)
        
        '''
        Process HWE
        '''
        
        '''Get HWE'''
        self.obj_Log_Default.info('Aggregating results for HWE')
        
        str_File_Search_Pattern = '*' + globalsSS.Logger_Details.static_Logger_File_Suffix__Genepop_HWE
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)
        
        if bool_File_Located:
            
            '''Process HWE Results'''

            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df = self.func_Aggregate_HWE_Results(str_Path_And_File)
                list_DFs.append(df)
            pass

            '''
            Write results to Excel
            '''
            str_Sheet_Name = 'HWE'
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass

            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name)            
                
        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
        
        #DEBUG_ON
        #with SSOutputHandler() as obj_Output:
            #obj_Output.method_Pause_Console()
        #DEBUG_OFF
            
        '''
        Process LD
        '''
        
        '''Get LD'''
        self.obj_Log_Default.info('Aggregating results for LD')

        str_File_Search_Pattern = '*' + globalsSS.Logger_Details.static_Logger_File_Suffix__Genepop_LD
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)

        if bool_File_Located:
            
            '''Process LD Results'''

            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df = self.func_Aggregate_LD_Results(str_Path_And_File)
                list_DFs.append(df)
            pass

            '''
            Write results to Excel
            '''
            str_Sheet_Name = 'LD'
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass
        
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name)            

        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        '''
        Process He
        '''
        
        '''Get Ho & He'''
        self.obj_Log_Default.info('Aggregating results for He')
        
        str_File_Search_Pattern = '*' + globalsSS.Logger_Details.static_Logger_File_Suffix__Genepop_He_All_Loci
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)

        if bool_File_Located:
            
            '''Process Ho & He Results'''

            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df = self.func_Aggregate_He_Results(str_Path_And_File)
                list_DFs.append(df)
            pass

            '''
            Write results to Excel
            '''
            str_Sheet_Name = 'Ho & He'
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass
        
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name)            

        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
    
        '''
        Process Allele Freq
        '''
        
        '''Get Allele Freqs'''
        self.obj_Log_Default.info('Aggregating results for Allele Freqs')
        
        str_File_Search_Pattern = '*' + globalsSS.Logger_Details.static_Logger_File_Suffix__Genepop_Allele_Freq
        bool_File_Located, list_Path_And_Files = self.func_Locate_Files(str_Search_Path, str_File_Search_Pattern)

        if bool_File_Located:
            
            '''Process Allele Freq Results'''
            
            list_DFs = []            
            for str_Path_And_File in list_Path_And_Files:
                
                df = self.func_Aggregate_Allele_Freq_Results(str_Path_And_File)
                list_DFs.append(df)
            pass

            '''
            Write results to Excel
            '''
            str_Sheet_Name = 'Allele Freqs'
            df_Aggregate = pandas.DataFrame()
            for df_New in list_DFs:
                '''log the results'''
                #str_Df = df_New.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe NEW: %s' % str_Df)
                
                #Concat DFs - Tried df.append() but it wont work
                df_Aggregate = pandas.concat([df_Aggregate,df_New], ignore_index=True)
                
                #str_Df = df_Aggregate.to_string()
                #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE: %s' % str_Df)

            pass
        
            self.func_Export_Results_To_Excel(df_Aggregate, writer, str_Sheet_Name)            

        else:
            self.obj_Log_Default.error('File specified could not be located; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass

        if bool_File_Located:
            self.func_Save_Excel_Writer(writer)
        else:
            self.obj_Log_Default.error('NO Results files could be located.  No Excel file written')
        pass
        
        return True
    

    def func_Aggregate_HWE_Results(self, str_Path_And_File):
        
        '''Process HWE Results'''
        dictResults = self.func_Aggregate_Results(str_Path_And_File)
        df = self.func_Manipulate_HWE(dictResults)

        return df
    
    
    def func_Aggregate_LD_Results(self, str_Path_And_File):
        
        '''Process HWE Results'''
        dictResults = self.func_Aggregate_Results(str_Path_And_File)
        df = self.func_Manipulate_LD(dictResults)

        return df


    def func_Aggregate_He_Results(self, str_Path_And_File):
        
        '''Process HWE Results'''
        dictResults = self.func_Aggregate_Results(str_Path_And_File)
        df = self.func_Manipulate_He(dictResults)

        return df    
    
    
    def func_Aggregate_Allele_Freq_Results(self, str_Path_And_File):
        
        '''Process HWE Results'''
        dictResults = self.func_Aggregate_Results(str_Path_And_File)
        df = self.func_Manipulate_Allele_Freqs(dictResults)

        return df    
    
    
    def func_Interpret_HWE_P_Values(self, df):   
        
        '''
        Interpret P=Values
        '''
        str_Sort_Key = globalsSS.Genepop_Stats.static_Label_HWE_P
        str_Sort_Col = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Sort_Key)

        str_Col_Existing = str_Sort_Col
        str_Col_New = globalsSS.Genepop_Stats.static_Label_Gen_Sig
        
        ''' add column next to one being interpreted'''
        intColIndex_Existing = df.columns.get_loc(str_Col_Existing)
        df.insert(intColIndex_Existing + 1, globalsSS.Genepop_Stats.static_Label_Gen_Sig, 0)

        '''rank significance based on p-value'''
        df[str_Col_New][df[str_Col_Existing] < globalsSS.Genepop_Stats.static_Interpret_Gen_Sig_P_Value_0_05] = 1
        df[str_Col_New][df[str_Col_Existing] < globalsSS.Genepop_Stats.static_Interpret_Gen_Sig_P_Value_0_01] = 2
                      
        return df


    def func_Interpret_LD_P_Values(self, df):   
        
        '''
        Interpret P=Values
        '''
        str_Sort_Key = globalsSS.Genepop_Stats.static_Label_LD_P
        str_Sort_Col = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Sort_Key)

        str_Col_Existing = str_Sort_Col
        str_Col_New = globalsSS.Genepop_Stats.static_Label_Gen_Sig
        
        ''' add column next to one being interpreted'''
        intColIndex_Existing = df.columns.get_loc(str_Col_Existing)
        df.insert(intColIndex_Existing + 1, globalsSS.Genepop_Stats.static_Label_Gen_Sig, 0)

        '''rank significance based on p-value'''
        df[str_Col_New][df[str_Col_Existing] < globalsSS.Genepop_Stats.static_Interpret_Gen_Sig_P_Value_0_05] = 1
        df[str_Col_New][df[str_Col_Existing] < globalsSS.Genepop_Stats.static_Interpret_Gen_Sig_P_Value_0_01] = 2
        df[str_Col_New][df[str_Col_Existing] < globalsSS.Genepop_Stats.static_Interpret_Gen_Sig_P_Value_0_001] = 3
        df[str_Col_New][df[str_Col_Existing] < globalsSS.Genepop_Stats.static_Interpret_Gen_Sig_P_Value_0_0001] = 4
        df[str_Col_New][df[str_Col_Existing] < globalsSS.Genepop_Stats.static_Interpret_Gen_Sig_P_Value_0_00001] = 5
                      
        return df
     
     
    def func_Manipulate_HWE(self, dictResults):

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()
                    
        '''create dataframe'''
        df = pandas.DataFrame.from_dict(dictResults,'columns', float)

        
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        '''convert non-numerics to numerics'''
        df.convert_objects(convert_numeric=True)
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        
        #'''sort DF'''
        #df = df.sort(globalsSS.Genepop_Stats.static_Label_HWE_P, ascending=True)

        '''
        Sort DF Rows by Sort Col
        '''
        '''get identify the full column name from the wanted sort key'''
        #Get col that contains the sort key
        str_Sort_Key = globalsSS.Genepop_Stats.static_Label_HWE_P
        bool_Sort_Direction_Ascending = True
        str_Sort_Col = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Sort_Key)
        df = df.sort(str_Sort_Col, ascending=bool_Sort_Direction_Ascending)

        '''
        Sort DF Cols by Heading Index (DOT notation 0.0.0.0)
        '''
        '''re-arrange columns based on the col name col index prefix number'''
        df = df.reindex_axis(sorted(df.columns), axis=1)        
        
        '''
        Apply interpretations to the results
        '''
        df = self.func_Interpret_HWE_P_Values(df)
        

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            '''log the results'''
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe: %s' % str_Df)
            #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
            t2.Stop(self.obj_Log_Debug_Display)
        
        return df


     
    def func_Manipulate_LD(self, dictResults):

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()
                    
        '''create dataframe'''
        df = pandas.DataFrame.from_dict(dictResults,'columns', float)
        
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        '''convert non-numerics to numerics'''
        df.convert_objects(convert_numeric=True)
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        
        '''
        Sort DF Rows by Sort Col
        '''
        '''get identify the full column name from the wanted sort key'''
        #Get col that contains the sort key
        str_Sort_Key = globalsSS.Genepop_Stats.static_Label_LD_P
        bool_Sort_Direction_Ascending = True
        str_Sort_Col = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Sort_Key)
        df = df.sort(str_Sort_Col, ascending=bool_Sort_Direction_Ascending)

        '''
        Sort DF Cols by Heading Index (DOT notation 0.0.0.0)
        '''
        '''re-arrange columns based on the col name col index prefix number'''
        df = df.reindex_axis(sorted(df.columns), axis=1)        
        
        '''
        Apply interpretations to the results
        '''
        df = self.func_Interpret_LD_P_Values(df)
        

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            '''log the results'''
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe: %s' % str_Df)
            #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
            t2.Stop(self.obj_Log_Debug_Display)
        
        return df


    def func_Manipulate_He(self, dictResults):

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()
                    
        '''create dataframe'''
        df = pandas.DataFrame.from_dict(dictResults,'columns', float)
        
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        '''convert non-numerics to numerics'''
        df.convert_objects(convert_numeric=True)
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)

        '''
        Sort DF Rows by Sort Col
        '''
        '''get identify the full column name from the wanted sort key'''
        #Get col that contains the sort key
        str_Sort_Key = globalsSS.Genepop_Stats.static_Label_Gen_Locus
        bool_Sort_Direction_Ascending = True
        str_Sort_Col = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Sort_Key)
        df = df.sort(str_Sort_Col, ascending=bool_Sort_Direction_Ascending)

        '''
        Sort DF Cols by Heading Index (DOT notation 0.0.0.0)
        '''
        '''re-arrange columns based on the col name col index prefix number'''
        df = df.reindex_axis(sorted(df.columns), axis=1)        
        
        '''
        Apply interpretations to the results
        '''
        #df = self.func_Interpret_LD_P_Values(df)
        

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            '''log the results'''
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe: %s' % str_Df)
            #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
            t2.Stop(self.obj_Log_Debug_Display)
        
        return df


    def func_Manipulate_Allele_Freqs(self, dictResults):

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()   
                    
        '''create dataframe'''
        df = pandas.DataFrame.from_dict(dictResults,'columns', float)
        
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        '''convert non-numerics to numerics'''
        df.convert_objects(convert_numeric=True)
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        
        '''
        Sort DF Cols
        '''
        
        '''get identify the full column name from the wanted sort key'''
        #Get colnames
        str_Sort_Key = globalsSS.Genepop_Stats.static_Label_Gen_Locus
        bool_Sort_Direction_Ascending = True
        str_Sort_Col = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Sort_Key)
         
        '''sort on a number take from a string column value'''
        # Add of a column containing a numbered version of the index
        list_Index = []
        int_Col_Value_List_Index = 0
        int_String_Split_List_Item_Wanted = 1
        for i in df[str_Sort_Col].values:
            str_Index = i.split(globalsSS.StringDelimiters.static_stringDelimiter_HYPHEN)[int_String_Split_List_Item_Wanted]
            #str_Index = i[int_Col_Value_List_Index].split(globalsSS.StringDelimiters.static_stringDelimiter_HYPHEN)[int_String_Split_List_Item_Wanted]
            int_Index = int(str_Index)
            list_Index.append(int_Index)
 
        '''
        Sort DF Rows
        '''
         
        #Add temp index to df
        df['temp_index'] = list_Index 
        # Perform sort of the rows on temp index
        df.sort(['temp_index'], ascending = [True], inplace = True)
        # Deletion of the added temp index column
        df.drop('temp_index', 1, inplace = True)

        '''
        Sort DF Columns
        '''
        '''re-arrange columns based on the col name col index prefix number'''
        df = df.reindex_axis(sorted(df.columns), axis=1)
         
        '''
        Apply interpretations to the results
        '''
        #df = self.func_Interpret_LD_P_Values(df)
        

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            '''log the results'''
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe: %s' % str_Df)
            #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
            t2.Stop(self.obj_Log_Debug_Display)
        
        return df

    '''
    --------------------------------------------------------------------------------------------------------
    # Utility Processing
    --------------------------------------------------------------------------------------------------------
    '''
    def func_Get_Dataframe_Col_Name_From_Sort_Key(self, df, str_Sort_Key):
        
        str_Sort_Col = ''
        
        '''get identify the full column name from the wanted sort key'''
        #Get colnames
        list_Col_Names = list(df.columns.values)
        #Get col that contains the sort key
        #str_Sort_Key = globalsSS.Genepop_Stats.static_Label_HWE_P
        list_str_Sort_Col = [s for s in list_Col_Names if str_Sort_Key in s]
        '''Get the first result - any more and there is an error '''
        if len(list_str_Sort_Col) > 1:
            self.obj_Log_Default.error('More than one column name found for str_Sort_Key: ' + str_Sort_Key + ' |--> Given candidates: ' + str(list_str_Sort_Col))
        elif len(list_str_Sort_Col) == 0:
            self.obj_Log_Default.error('No column name found for str_Sort_Key: %s ' % str_Sort_Key)
        else:
            str_Sort_Col = list_str_Sort_Col[0]
        pass
    
        return str_Sort_Col
  
    
    def func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions(self, df, dict_Generic_Colnames_With_Aggregate_Functions):
        
        dict_Specific_Colnames = OrderedDict()

        for key_Str_Generic_Colname, value_Str_Function in dict_Generic_Colnames_With_Aggregate_Functions.items():
            str_DF_Specific_ColName = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, key_Str_Generic_Colname)
            dict_Specific_Colnames[str_DF_Specific_ColName] = value_Str_Function
        pass    

        return dict_Specific_Colnames

    def func_Get_Specific_Colname_Given_Generic_Name_For_Dict_Of_Aggregate_Functions_With_Order(self, df, dict_Generic_Colnames_With_Aggregate_Functions):
        
        dict_Specific_Colnames = OrderedDict()

        for key_str_Generic_Colname, (value_str_Function, value_int_Order) in dict_Generic_Colnames_With_Aggregate_Functions.items():
            str_DF_Specific_ColName = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, key_str_Generic_Colname)
            dict_Specific_Colnames[str_DF_Specific_ColName] = (value_str_Function, value_int_Order)
        pass    

        return dict_Specific_Colnames
      
    
    def func_Merge_Dataframes_By_Common_Key(self, strKey1, df1, strKey2, df2):

        ''' Get Colname from key '''
        str_Col_Name_1 = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df1, strKey1)
        str_Col_Name_2 = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df2, strKey2)

        #df2.join(df1, on=[str_Col_Name_2, str_Col_Name_1])
        df = pandas.merge(df2, df1, left_on = str_Col_Name_2, right_on = str_Col_Name_1)        
        
        return df
    
    
    def func_Merge_Dataframes_By_Key_List(self, str_Join_How, df1, df2, list_Keys, list_Colname_Suffixes=[]):

        list_Generic_Colnames = list_Keys
        ''' Get Colname from key '''
        list_DFs = [df1, df2]
        list_DFs = self.func_Rename_Like_DF_Colnames_To_Same_Name(list_DFs, list_Generic_Colnames)
        
        df1 = list_DFs[0]
        df2 = list_DFs[1]
        
        #df2.join(df1, on=[str_Col_Name_2, str_Col_Name_1])
        if len(list_Colname_Suffixes) > 1:
            df = pandas.merge(df1, df2, how = str_Join_How, on = list_Generic_Colnames, suffixes = (list_Colname_Suffixes[0],list_Colname_Suffixes[1]))  
        else:
            df = pandas.merge(df1, df2, how = str_Join_How, on = list_Generic_Colnames)        
        pass
    
        return df


    def func_Rename_Like_DF_Colnames_To_Same_Name(self, list_DFs, list_Generic_Colnames):
        
        for df in list_DFs:
            dict_Cols_To_Rename = OrderedDict()
            list_Col_Names_To_Join = []
            for str_Generic_Colname in list_Generic_Colnames:
                str_DF_Specific_ColName = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Generic_Colname)
                list_Col_Names_To_Join.append(str_DF_Specific_ColName)
                
                dict_Cols_To_Rename[str_DF_Specific_ColName] = str_Generic_Colname
            pass    
        
            df.rename(columns=dict_Cols_To_Rename, inplace=True)    
        pass
    
        return list_DFs
    
    
    def func_Rename_DF_Colnames_To_New_Name(self, list_DFs, list_Generic_Colnames, list_New_Colnames):
        
        for df in list_DFs:
            dict_Cols_To_Rename = OrderedDict()
            list_Col_Names_To_Join = []
            int_Colname = 0
            for str_Generic_Colname in list_Generic_Colnames:
                str_DF_Specific_ColName = self.func_Get_Dataframe_Col_Name_From_Sort_Key(df, str_Generic_Colname)
                list_Col_Names_To_Join.append(str_DF_Specific_ColName)
                
                dict_Cols_To_Rename[str_DF_Specific_ColName] = list_New_Colnames[int_Colname]
                int_Colname += 1
            pass    
        
            df.rename(columns=dict_Cols_To_Rename, inplace=True)    
        pass
    
        return list_DFs
       
           

    def func_Sort_DataFrame_Cols_On_Partial_Heading_NOT_USED(self, df_In, str_Sort_Key):
        
        '''
        Sort DF rows
        '''
        '''get identify the full column name from the wanted sort key'''
        #Get colnames
        list_Col_Names = list(df_In.columns.values)
        #Get col that contains the sort key
        str_Sort_Col = [s for s in list_Col_Names if str_Sort_Key in s]
        
        '''sort on a number take from a string column value'''
        # Add of a column containing a numbered version of the index
        list_Index = []
        int_Col_Value_List_Index = 0
        int_String_Split_List_Item_Wanted = 1
        for i in df_In[str_Sort_Col].values:
            #str_Index = i[int_Col_Value_List_Index].split(globalsSS.StringDelimiters.static_stringDelimiter_HYPHEN)[int_String_Split_List_Item_Wanted]
            str_Index = i[int_Col_Value_List_Index].split(globalsSS.StringDelimiters.static_stringDelimiter_SPACE)[int_String_Split_List_Item_Wanted]
            int_Index = int(str_Index)
            list_Index.append(int_Index)
 
        '''
        Sort DF Rows
        '''

        #Add temp index to df
        df_In['temp_index'] = list_Index 
        # Perform sort of the rows on temp index
        df_In.sort(['temp_index'], ascending = [True], inplace = True)
        # Deletion of the added temp index column
        df_In.drop('temp_index', 1, inplace = True)

        '''
        Sort DF Columns
        '''
        '''re-arrange columns based on the col name col index prefix number'''
        df_In = df_In.reindex_axis(sorted(df_In.columns), axis=1)
        
        
        df_Out = df_In
        
        return df_Out
 
    
    def func_Export_Results_To_Excel(self, df, writer, str_Sheet_Name, list_Columns_To_Write=[], bool_NaN_As_NA = False):

        if len(list_Columns_To_Write) > 0:
            if bool_NaN_As_NA:
                df.to_excel(writer, sheet_name = str_Sheet_Name, columns = list_Columns_To_Write, na_rep='NA')
            else:
                df.to_excel(writer, sheet_name = str_Sheet_Name, columns = list_Columns_To_Write)
            pass
        else:
            if bool_NaN_As_NA:
                df.to_excel(writer, sheet_name = str_Sheet_Name, na_rep='NA')
            else:
                df.to_excel(writer, sheet_name = str_Sheet_Name)
            pass
        
        return writer


    def func_Get_Excel_Writer(self, str_Excel_Output_Path, str_Excel_Output_File_WO_Suffix):
    
        bool_Success = False
        writer = None
        
        str_Excel_Output_File_Suffix = '.xlsx' 
        str_Excel_Output_File = str_Excel_Output_File_WO_Suffix + str_Excel_Output_File_Suffix
        str_Excel_Output_Path_And_File = str_Excel_Output_Path + '\\' + str_Excel_Output_File
        
        with FileHandler() as obj_FileHandler:
            bool_File_Located, str_File_And_Path = obj_FileHandler.func_Locate_Specific_File(str_Excel_Output_Path, str_Excel_Output_File)
        pass

#         if not bool_File_Located:
#             self.obj_Log_Default.error('Excel file already exists and new excell writer cannot be created: ' + str_Excel_Output_Path_And_File)
#             bool_Success = False
#             return writer
#         pass
    
        try:
            writer = pandas.ExcelWriter(str_Excel_Output_Path_And_File)
            bool_Success = True
        except:
            self.obj_Log_Default.error('Excel writer could not be obtained: ' + str_Excel_Output_Path_And_File)
            bool_Success = False
        pass
    
        if writer == None:
            self.obj_Log_Default.error('Excel writer could not be created: ' + str_Excel_Output_Path_And_File)
            bool_Success = False
        pass
            
        return writer


    def func_Save_Excel_Writer(self, writer):
        
        bool_Success = False
        
        try:
            writer.save()
            bool_Success = True
        except:
            bool_Success = False
        pass
    
        return bool_Success
 
 
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

       
    def func__Aggregate_Input_File_To_Dataframe(self, str_Path_And_File):
        

        self.obj_Log_Default.info('Aggregating file to dataframe: ' + str_Path_And_File)

        '''Process Results'''        
        dictResults = self.func_Aggregate_Results(str_Path_And_File)

        '''create dataframe'''
        df = pandas.DataFrame.from_dict(dictResults,'columns', float)
        
        return df    


    def func_Aggregate_Results(self, str_Path_And_File):   
        
        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()

        self.obj_Log_Default.info('Aggregating results')
                    
        with FileHandler() as obj_File_Operation:
            fileHandle = obj_File_Operation.fileOpen(str_Path_And_File, 'read')
            str_Delim = globalsSS.StringDelimiters.static_stringDelimiter
            #csv.field_size_limit(2147483647)
            csv.field_size_limit(sys.maxint)
            readerDelim = csv.DictReader(fileHandle, delimiter=str_Delim, quotechar='|', lineterminator='\r\n')
            
            dictResults = {}
            dictResults = OrderedDict()
            dictDelim = OrderedDict()
            intCount = 0
            for dictDelim in readerDelim:
                
                ''' add source filename to the data '''
                
                dictDelim['Results_File'] = str_Path_And_File
                
                #self.obj_Log_Debug_Display.debug(str(dictDelim))
                
                if intCount == 0:
                    
                    for key, value in dictDelim.iteritems():
                        
                        if globalsSS.StringDelimiters.static_stringDelimiter_RESULTS_START in key:
                            #key = globalsSS.Logger_Details.static_Logger_Field_Heading_When_delim_RESULTS_START
                            #Ignore it
                            pass
                        else:
                            dictResults[key] = [value]
                        pass
                        
                else:
                    for key in dictResults.keys():

                        if key in dictDelim:
                            dictResults[key].append(dictDelim[key])
                        pass
                pass
                
                intCount += 1
            pass

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            #self.obj_Log_Debug_Display.debug('Results dict: %s' % str(dictResults))
            t2.Stop(self.obj_Log_Debug_Display)
                        
        return dictResults


    def func__Transform_Dataframe_Column_Datatypes(self, df):

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()

        self.obj_Log_Default.info('Transforming dataframe columns')
  
                            
        '''convert non-numerics to numerics'''
        df.convert_objects(convert_numeric=True)
        #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
        

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            '''log the results'''
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe: %s' % str_Df)
            #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
            t2.Stop(self.obj_Log_Debug_Display)
        
        return df
 
    def func__Sort_Reindex_Dataframe(self, df):

        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            t2 = Timer2(True)
            t2.Start()

        self.obj_Log_Default.info('Sorting dataframe')
                            
        '''
        Sort DF Columns & Reindex
        '''
        '''re-arrange columns based on the col name col index prefix number'''
        df = df.reindex_axis(sorted(df.columns), axis=1)        


        if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
            '''log the results'''
            #str_Df = df.to_string()
            #self.obj_Log_Debug_Display.debug('Results dataframe: %s' % str_Df)
            #self.obj_Log_Debug_Display.debug('Results dataframe datatypes: %s' % df.dtypes)
            t2.Stop(self.obj_Log_Debug_Display)
        
        return df


    def func_Rename_Columns_From_List(self, df, list_Colnames_New):
        
            
        '''Rename colnames '''
        int_Len_DF_Existing_Colnames = len(df.columns)
        list_Colnames_Existing = [x for x in df.columns]
        int_Len_DF_New_Colnames = len(list_Colnames_New)
        if int_Len_DF_Existing_Colnames != int_Len_DF_New_Colnames:
            self.obj_Log_Default.error('The number of Existing Colnames: ' + str(int_Len_DF_Existing_Colnames) + ' does NOT equal the number of New Colnames: ' + str(int_Len_DF_New_Colnames))
            int_Larger_List_Size = 0
            int_Smaller_List_Size = 0
            if int_Len_DF_Existing_Colnames > int_Len_DF_New_Colnames:
                int_Larger_List_Size = int_Len_DF_Existing_Colnames
                int_Smaller_List_Size = int_Len_DF_New_Colnames
            else:
                int_Larger_List_Size = int_Len_DF_New_Colnames
                int_Smaller_List_Size = int_Len_DF_Existing_Colnames
            pass
            for int_Colname_Count in range(0, int_Smaller_List_Size):
                
                self.obj_Log_Default.error('Existing Colname' + str(int_Colname_Count).zfill(len(str(int_Len_DF_Existing_Colnames))) + ' : '
                                            + list_Colnames_Existing[int_Colname_Count]
                                            + ' <--> '
                                            + list_Colnames_New[int_Colname_Count]
                                            + ' : New Colname ' + str(int_Colname_Count).zfill(len(str(int_Len_DF_New_Colnames))))
            pass
        
            ''' Set df to None to ensure programs fails'''
            df = None
            pass
        else:
            df.columns = list_Colnames_New
        pass
    
        return df
   
    def func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions(self, str_Colname_Prefix_1, dict_Colnames_With_Applied_Functions):
        
        
        #str_ID_Suf = globalsSS.StringDelimiters.static_stringDelimiterSPACE
        str_ID_Suf = globalsSS.StringDelimiters.static_stringDelimiter_UNDERSCORE
        int_Level = 1
        int_Key_Count = 0
        list_Colnames_New = []
        for key_New_Colname, value_Function_Applied_To_Col in dict_Colnames_With_Applied_Functions.items():
            if int_Key_Count == 0:
                bool_Reset_Count = True
            else:
                bool_Reset_Count = False
            pass

            str_Colname_New = str(self.func_Get_Log_Current_Column_Index(bool_Reset_Count, int_Level, True, str_ID_Suf)
                                  + value_Function_Applied_To_Col + '_' 
                                  + str_Colname_Prefix_1 + '_'
                                  + key_New_Colname)
                                       
            list_Colnames_New.append(str_Colname_New)
            int_Key_Count += 1
        pass
    
        return list_Colnames_New       

    def func_Generate_New_Colnames_With_Col_Index_From_Dict_With_Applied_Functions_New(self, str_Colname_Prefix_1, dict_Colnames_With_Applied_Functions, list_Colname_Prefixes):
        
        
        #str_ID_Suf = globalsSS.StringDelimiters.static_stringDelimiterSPACE
        str_ID_Suf = globalsSS.StringDelimiters.static_stringDelimiter_UNDERSCORE
        int_Level = 1
        int_Key_Count = 0
        list_Colnames_New = []
        for key_Colname, value_Function_Applied_To_Col in dict_Colnames_With_Applied_Functions.items():
            if int_Key_Count == 0:
                bool_Reset_Count = True
            else:
                bool_Reset_Count = False
            pass

            '''Find and remove unwanted colname prefixes and numbers '''
            for str_Colname_Prefix in list_Colname_Prefixes:
                if str_Colname_Prefix in key_Colname:
                    #match = re.search(r"[^a-zA-Z_](" + str_Colname_Prefix + ")[^a-zA-Z_]", key_Colname)
                    int_Substring_Start_Pos = key_Colname.find(str_Colname_Prefix)
                    int_Substring_End_Pos = int_Substring_Start_Pos + len(str_Colname_Prefix)
                    key_New_Colname = key_Colname[int_Substring_End_Pos:]
                pass
            pass
        
            str_Colname_New = str(self.func_Get_Log_Current_Column_Index(bool_Reset_Count, int_Level, True, str_ID_Suf)
                                  + value_Function_Applied_To_Col + '_' 
                                  + str_Colname_Prefix_1 + '_'
                                  + key_New_Colname)
                                       
            list_Colnames_New.append(str_Colname_New)
            int_Key_Count += 1
        pass
    
        return list_Colnames_New       
    
    def func__Subset_Dataframe_By_Query_DOESNT_WORK(self, df, list_Colnames_To_Index, str_Subset_Df_Query):


        self.obj_Log_Default.info('Subset dataframe')

        '''
        -------------------------
        Specify dataframe
        -------------------------
        '''
        
        df_To_Split = df

        '''
        -------------------------
        Specify Query
        -------------------------
        '''
        
        df_To_Split = df_To_Split.set_index(list_Colnames_To_Index)
        df_To_Split.index.name = list_Colnames_To_Index[0]
#         str_Query = "'" + str_Col_Name_Query_Key_1 + ' == "All"' + "'"
        df_Split_1 = df_To_Split.query(str_Subset_Df_Query)

        #df_Split_1 = df_To_Split[(df_To_Split[str_Col_Name_Query_Key_1]!=globalsSS.SexConstants.static_stringSexAll)]
        
        #DEBUG_ON
        #str_Df = df_Split_1.to_string()
        #self.obj_Log_Debug_Display.debug('Results dataframe AGGREGATE 1: %s' % str_Df)
        #raw_input('pausing...')
        #DEBUG_OFF
        
        return df_Split_1
 
    
    def func_Locate_Files(self, str_Search_Path, str_File_Search_Pattern):
         
        bool_Files_Located = False
         
        def failed(exc):
            bool_Files_Located = False
            raise exc
         
        list_Path_And_Files = []
        for dirpath, dirs, files in os.walk(str_Search_Path, topdown=True, onerror=failed):
            #intCount = 0
            str_Path_And_File = ''
            for str_File_Name in fnmatch.filter(files, str_File_Search_Pattern):
                bool_Files_Located = True
                str_Path_And_File = dirpath + '\\' + str_File_Name
                list_Path_And_Files.append(str_Path_And_File)
                #intCount += 1
                pass
            pass
        pass
          
        if len(list_Path_And_Files) == 0:
            bool_Files_Located = False
            self.obj_Log_Default.error('No files found. Expecting files on search path; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
        pass
                     
        return bool_Files_Located, list_Path_And_Files
 
     
    def func_Locate_Specific_File(self, str_Search_Path, str_File_Search_Pattern):
         
        def failed(exc):
            boolSuccessful = False
            raise exc
 
 
        for dirpath, dirs, files in os.walk(str_Search_Path, topdown=True, onerror=failed):
            bool_File_Located = False
            intCount = 0
            for str_File_Name in fnmatch.filter(files, str_File_Search_Pattern):
                bool_File_Located = True
                intCount += 1
                if intCount > 1:
                    self.obj_Log_Default.error('More than one file found. Expecting only one on search path; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
                pass
            pass
         
        str_Path_And_File = ''
        if bool_File_Located:
            str_Path_And_File = dirpath + '\\' + str_File_Name
             
        return bool_File_Located, str_Path_And_File
                     
    def __exit__(self, type, value, traceback):
         
        pass
    
    
    
    
    
