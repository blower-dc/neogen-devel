#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS

#------------------< Python modules
from datetime import datetime
from memory_profiler import profile
import sys
from os import path as os__path
from logging import getLogger as logging__getLogger
#------------------< Import DCB_General modules
from FileHandler import FileHandler
from handler_Logging import Logging
#------------------< Import SharkSim modules
from SharkSimHandler import SharkSimHandler
#from ErrorHandler import ErrorHandler
from SSOutputHandler import SSOutputHandler
from SSSamplingTest import SSSamplingTest 
from handler_Biopython import Biopython
from SSResultsHandler import SSResults
from globals_SharkSim import globalsSS
from SSPlotHandler import SSPlots
from SSConfigHandler import SSConfigOperation
from object_SSConfigSamplingStrategy import object_SSConfigSamplingStrategy
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
gstringModuleName='SSReplicateHandler.py'
gstringClassName='SSReplicateOperation'

class SSReplicateOperation(object):

    def __enter__(self):
    
        return self
    
    def __init__(self, list_Params):
           

        objSSParameters = list_Params[0]
        self.obj_SSParams = objSSParameters
        
        self.obj_Log_RD = logging__getLogger(globalsSS.Logger_Run_Display.static_Logger_Name__Run_Display)

        return None

        
    '''@profile'''
    def method_Replicate_Processing(self):
 
        '''
        -------------------------------------------------
        Process each replicate within a batch
        -------------------------------------------------
        '''
       
        bool_Shark_Sim = True
        bool_Run_Processing_Subset_Only = not bool_Shark_Sim
        if bool_Run_Processing_Subset_Only:
            bool_Process_Replicates = False
            bool_Process_Saved_Pops_CONFIRM = False
            bool_ALL_Exp_SAMP_STRAT_From_CONFIG_CONFIRM = False
            bool_ALL_Exp_100_Percent_User_Specified_Age_Cohorts_1_0_CONFIRM = False
            bool_ALL_Exp_Full_Embryo_Cohort_FEM__CONFIRM = False
            bool_ALL_Exp_Full_Juvenile_Cohorts_FJV__CONFIRM = False
            bool_ALL_Exp_Full_Adult_Cohorts_FMT__CONFIRM = False
            bool_ALL_Exp_Full_Sampling_Of_Cohorts_FUL__CONFIRM = False
            bool_ALL_Exp_Sampling_Proportions_Scaled_By_Max_Proportion_PSMP__CONFIRM = False
            bool_Process_Saved_Pops__ALL_Exp_2_2_CONFIRM = False
            bool_Saved_Pops_Categorised_Ne2_PF_Aggregation_CONFIRM = False
            bool_Plot_Sampling_Indivs_CONFIRM = False
            bool_Plot_Sampling_Plans_Accuracy_And_Others_CONFIRM = True
        else:
            bool_Process_Replicates = True
            bool_Process_Saved_Pops_CONFIRM = True
            bool_Aggregate_PS_PF_Results_CONFIRM = True
            bool_ALL_Exp_SAMP_STRAT_From_CONFIG_CONFIRM = True
            bool_ALL_Exp_100_Percent_User_Specified_Age_Cohorts_1_0_CONFIRM = True
            bool_ALL_Exp_Full_Embryo_Cohort_FEM__CONFIRM = True
            bool_ALL_Exp_Full_Juvenile_Cohorts_FJV__CONFIRM = True
            bool_ALL_Exp_Full_Adult_Cohorts_FMT__CONFIRM = True
            bool_ALL_Exp_Full_Sampling_Of_Cohorts_FUL__CONFIRM = True
            bool_ALL_Exp_Sampling_Proportions_Scaled_By_Max_Proportion_PSMP__CONFIRM = True
            bool_Process_Saved_Pops__ALL_Exp_2_2_CONFIRM = True
            bool_Saved_Pops_Categorised_Ne2_PF_Aggregation_CONFIRM = True
            bool_Plot_Sampling_Indivs_CONFIRM = True
            bool_Plot_Sampling_Plans_Accuracy_And_Others_CONFIRM = True
        pass

        
        bool_Put_On_Hold_Before_Starting_Run = False
        if bool_Put_On_Hold_Before_Starting_Run:
            with globalsSS.Pause_Console() as obj_Pause:
                obj_Pause.method_Pause_Console('WAITING TO START RUN...', bool_Location=True)
            pass
        pass


        '''
        ----------------------------------------------------------------
        Process each step requested
        ----------------------------------------------------------------
        '''
              
        if globalsSS.Run_Processing_Step.static_int_Run_Processing_Step__POP_SIM in self.obj_SSParams.list_int_App_Arg_Run_Processing_Steps:

            if bool_Process_Replicates:            
                '''
                -----------------------
                Specify the output path
                -----------------------
                '''
#                 ''' Population Simulation Path '''
#                 self.obj_SSParams.str_Current_Run_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path + '\\' + globalsSS.Processing_Path.static_str_Processing_Path__Pop_Sim           
#                 ''' Logs Path '''
#                 #self.obj_SSParams.str_Current_Run_Path__Logs = self.obj_SSParams.str_Current_Run_Path + '\\logs'
#                 '''Create Run Folder if it doesnt exist '''
#                 with FileHandler() as obj_FileHandler:
#                     obj_FileHandler.method_Create_Path(self.obj_SSParams.str_Current_Run_Path)
#                     #obj_FileHandler.method_Create_Path(self.obj_SSParams.str_Current_Run_Path__Logs)
#                 pass              
    
                '''
                -----------------------
                Process population simulation replicates
                -----------------------
                '''            
                for intCurrentReplicate in range(1, self.obj_SSParams.intReplicates+1):  #This is to ensure replicates are displayed as 1, 2, 3 etc (rather than 0, 1, 2 etc)
                    
                    self.obj_SSParams.dateReplicateRunStartTime = datetime.now()
        
                    self.obj_SSParams.intCurrentReplicate = intCurrentReplicate
        
                    with SSOutputHandler() as SSOutputOperation:
                        listOutputDestinations = ['console', self.obj_SSParams.outputFileNameSummaryLogAllBatches, self.obj_SSParams.outputFileNameSummaryLogAllReps, self.obj_SSParams.outputFileNameTimingSummaryLogAllBatches]
                        SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'Replicate Run Started: ' + self.obj_SSParams.dateReplicateRunStartTime.strftime("%Y-%m-%d %H:%M:%S"))
        #             
                    self.obj_Log_RD.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
                    self.obj_Log_RD.info('Replicate Run Started: ' + self.obj_SSParams.dateReplicateRunStartTime.strftime("%Y-%m-%d %H:%M:%S"))
                    self.obj_Log_RD.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
                    
                              
                    #Start processing the replicate 
                    self.obj_SSParams.method_Replicate_Pre_Processing()
        
                    #Run Sim for each set of run parameters
                    with SharkSimHandler() as objSharkSimOperation:
                        
                        objSharkSimOperation.objSSParametersLocal = self.obj_SSParams
        
                        #Output Summary Shark Sim initial parameters 
                        with SSOutputHandler() as SSOutputOperation:
                            SSOutputOperation.methodOutput_SimSummaryInfo(self.obj_SSParams, self.obj_SSParams.listOutputDestinations_SimSummaryInfo, False)
                            boolPauseOutput = False
                            SSOutputOperation.method_Log_Output__SimStartingProperties(self.obj_Log_RD, self.obj_SSParams, boolPauseOutput)
                            SSOutputOperation.method_Log_Output__LifeStageDefinitions(self.obj_Log_RD, self.obj_SSParams)
                        '''
                        -------------------------------------------------
                        Simulate the simupop population REPLICATE
                        -------------------------------------------------
                        '''
                        if bool_Shark_Sim:
                            objSharkSimOperation.bool_Allow_Log_Debug_Console_Output = False                      
                            pop = objSharkSimOperation.method_MainProcessing()
        
                            pop_Out = pop
                            
                    if bool_Shark_Sim:
                        '''
                        -------------------------------------------------
                        Save the simupop population REPLICATE
                        -------------------------------------------------
                        '''
                        with SSOutputHandler() as SSOutputOperation:
                            listOutputDestinations = ['console', self.obj_SSParams.outputFileNameSummaryLogAllBatches, self.obj_SSParams.outputFileNameSummaryLogAllReps, self.obj_SSParams.outputFileNameTimingSummaryLogAllBatches]
                            SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Saving Population', boolIsHeader=True, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
        
                        self.obj_Log_RD.info('Saving Population')
                        
                        with SSSamplingTest() as obj_Sampling:
                            obj_Sampling.method_Initialise(self.obj_SSParams, objSharkSimOperation)
                            
                            strSimuPop_Pop_FilePathAndName = objSharkSimOperation.objSSParametersLocal.outputFileNamePopOutputAllGens
                            obj_Sampling.method_Save_SimuPop_Population(pop_Out, strSimuPop_Pop_FilePathAndName)
                        pass
                    pass    
                    
                    #Log finishing datetime and time for single run
                    self.obj_SSParams.dateReplicateRunFinishTime = datetime.now()
        
                    dateTimeRunTime = self.obj_SSParams.dateReplicateRunFinishTime - self.obj_SSParams.dateReplicateRunStartTime
                    with SSOutputHandler() as SSOutputOperation:
                        listOutputDestinations = ['console', self.obj_SSParams.outputFileNameSummaryLogAllBatches, self.obj_SSParams.outputFileNameSummaryLogAllReps, self.obj_SSParams.outputFileNameTimingSummaryLogAllBatches]
                        SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'Replicate Run Started: ' + self.obj_SSParams.dateReplicateRunStartTime.strftime("%Y-%m-%d %H:%M:%S"))
                        SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'Replicate Run Finished: ' + self.obj_SSParams.dateReplicateRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
                        SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'Replicate Run took: ' + str(dateTimeRunTime))
        
                    self.obj_Log_RD.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
                    self.obj_Log_RD.info('SIM REPLICATE: Started: ' + self.obj_SSParams.dateReplicateRunStartTime.strftime("%Y-%m-%d %H:%M:%S"))
                    self.obj_Log_RD.info('SIM REPLICATE: Finished: ' + self.obj_SSParams.dateReplicateRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
                    self.obj_Log_RD.info('SIM REPLICATE: Took: ' + str(dateTimeRunTime))
                    self.obj_Log_RD.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
                    
                ''' End REPLICATE For Loop '''    
                pass
            pass
    
            '''
            -----------------------
            Process population simulation post-replicates processing
            -----------------------
            '''    
            bool_Run_All_STANDARD_Post_Sim_Processes = False
            
            
            bool_Genepop_Sampling_Override = False
            if bool_Shark_Sim or bool_Genepop_Sampling_Override or bool_Run_All_STANDARD_Post_Sim_Processes:
                bool_Genepop_Sampling = False
                if bool_Genepop_Sampling:
                    str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                    #str_Search_Path = 'C:\\DCB\\MUI\\MUI_Sync_Controlled\\MUI_SC_SharkSim\\v2_71_Py27\\Test\\SS_2_71_Run_2015_05_08_11_56_06\\SS_2_71_Run_2015_05_08_11_56_06'
                    with SSSamplingTest() as objSamplingTestOperation:
                        objSamplingTestOperation.method_Initialise(self.obj_SSParams)
                        #objSamplingTestOperation.method_Initialise(self.obj_SSParams, objSharkSimOperation)
                        list_File_Suffix_Search_Patterns = [
                                                            globalsSS.Genepop_Results_File_Details.static_Genepop_File_Suffix__Embryo_VSP_Post_Fertilization
                                                            ,globalsSS.Genepop_Results_File_Details.static_Genepop_File_Suffix__Mature_VSP_Post_Fertilization
                                                            ,globalsSS.Genepop_Results_File_Details.static_Genepop_File_Suffix__Full_SP_Post_Fertilization
                                                            ]
                        for str_File_Suffix_Search_Pattern in list_File_Suffix_Search_Patterns:
                            objSamplingTestOperation.method_Produce_Genepop_Stats(str_Search_Path, str_File_Suffix_Search_Pattern)
                        pass
                pass
            
            bool_Results_Aggregation_Override = False
            if bool_Shark_Sim or bool_Results_Aggregation_Override or bool_Run_All_STANDARD_Post_Sim_Processes:
                bool_Results_Aggregation = True
                if bool_Results_Aggregation:
                    obj_SSResults = SSResults(self.obj_SSParams)
                    str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path 
                    with obj_SSResults:
                        bool_Genepop = True
                        if bool_Genepop:
                            #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                            obj_SSResults.func_Aggregate_Genpop_Stats(str_Search_Path)
                        pass
                        bool_Genepop_AFBA = False
                        if bool_Genepop_AFBA:
                            #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                            obj_SSResults.func__Genepop_Allele_Freqs_By_Allele_Aggregate_Results__Aggregate_And_Group___At_Lowest_Detail(str_Search_Path)
                        pass
                        bool_SS_Level = True
                        if bool_SS_Level:
                            #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                            obj_SSResults.func_Aggregate_SS_LEVEL_Stats(str_Search_Path)
                        pass
                pass
            pass
        
            bool_Parent_Offspring_Ne2_Sampling_Aggregation_Override =  False
            if bool_Shark_Sim or bool_Parent_Offspring_Ne2_Sampling_Aggregation_Override or bool_Run_All_STANDARD_Post_Sim_Processes or bool_Aggregate_PS_PF_Results_CONFIRM:
                bool_Parent_Offspring_Ne2_Sampling_Aggregation = True
                if bool_Parent_Offspring_Ne2_Sampling_Aggregation:
                    #obj_SSResults = SSResults(self.obj_SSParams) 
                    #obj_SSResults.bool_Allow_Log_Debug_Console_Output = False
                    str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                    #str_Search_Path = 'C:\\DCB\\MUI\\MUI_Sync_Controlled\\MUI_SC_SharkSim\\v2_73_Py27\\Test\\SS_2_73_Run_2015_05_12_17_53_20'
                    with SSResults(self.obj_SSParams) as obj_SSResults:
                        '''
                        ~~~~~~~~~~~~~
                        EXP1
                        ~~~~~~~~~~~~~
                        '''
                        bool_EXP1_EOR_Categorised_Ne2_EOR_Aggregation = True
                        if bool_EXP1_EOR_Categorised_Ne2_EOR_Aggregation:                
                            bool_Parent_Offspring_PF_Aggregation_1 = True
                            if bool_Parent_Offspring_PF_Aggregation_1:
                                #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                                obj_SSResults.func__Parent_Offspring_PF_Results__Aggregate_And_Group___By_Run_By_Mating_Count_Sim_Total(str_Search_Path)
                            pass
                            bool_Parent_Offspring_PF_Aggregation = True
                            if bool_Parent_Offspring_PF_Aggregation:
                                #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                                obj_SSResults.func_EXPERIMENT_Parent_Offspring_Ne_1__Parent_Offspring_PF_Results__Aggregate_Results(str_Search_Path)
                            pass
                            bool_Categorised_Ne2_EOR_Aggregation = False
                            if bool_Categorised_Ne2_EOR_Aggregation:
                                #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                                obj_SSResults.func_EXPERIMENT_Parent_Offspring_Ne_1__Ne2_EOR_Results__Aggregate_Results(str_Search_Path)
                            pass
                            bool_Categorised_Ne2_Parent_Offspring_EOR_Merged_Aggregation = False
                            if bool_Categorised_Ne2_Parent_Offspring_EOR_Merged_Aggregation:
                                #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                                obj_SSResults.func_EXPERIMENT_Parent_Offspring_Ne_1__Composite_Results__Aggregate_Results(str_Search_Path)
                            pass
                            bool_Summarise_Categorised_Ne2_Parent_Offspring_EOR_Aggregation = False
                            if bool_Summarise_Categorised_Ne2_Parent_Offspring_EOR_Aggregation:
                                #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                                obj_SSResults.func_EXPERIMENT_Parent_Offspring_Ne_1__Summary_Results__Aggregate_Results(str_Search_Path)
                            pass
                        '''
                        ~~~~~~~~~~~~~
                        EXP2
                        ~~~~~~~~~~~~~
                        '''
                        bool_EXP2_PF_Categorised_Ne2_PF_Aggregation = False
                        if bool_EXP2_PF_Categorised_Ne2_PF_Aggregation:
                            bool_Categorised_Ne2_PF_Aggregation = True
                            if bool_Categorised_Ne2_PF_Aggregation:
                                #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                                obj_SSResults.func_EXPERIMENT_Parent_Offspring_Ne_2__Ne2_PF_Results__Aggregate_Results(str_Search_Path)
                            pass
                            bool_Categorised_Ne2_Parent_Offspring_PF_Merged_Aggregation = True
                            if bool_Categorised_Ne2_Parent_Offspring_PF_Merged_Aggregation:
                                #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                                obj_SSResults.func_EXPERIMENT_Parent_Offspring_Ne_2__Composite_Results__Aggregate_Results(str_Search_Path)
                            pass
                            bool_Summarise_Categorised_Ne2_Parent_Offspring_PF_Aggregation = True
                            if bool_Summarise_Categorised_Ne2_Parent_Offspring_PF_Aggregation:
                                #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                                obj_SSResults.func_EXPERIMENT_Parent_Offspring_Ne_2__Summary_Results__Aggregate_Results(str_Search_Path)
                            pass
                        pass
                    pass
                pass
            pass
        
            bool_AgeNe_Results_Grouping_Override = False
            if bool_Shark_Sim or bool_AgeNe_Results_Grouping_Override or bool_Run_All_STANDARD_Post_Sim_Processes:
                bool_AgeNe_Results_Grouping = True
                if bool_AgeNe_Results_Grouping:
                    obj_SSResults = SSResults(self.obj_SSParams) 
                    obj_SSResults.bool_Allow_Log_Debug_Console_Output = False
                    str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                    #tr_Search_Path = 'C:\\DCB\\MUI\\MUI_Sync_Controlled\\MUI_SC_SharkSim\\v2_73_Py27\\Test\\SS_2_73_Run_2015_05_12_17_53_20'
                    with obj_SSResults:
                        bool_Man_AgeNe_EOR_Aggregation = True
                        if bool_Man_AgeNe_EOR_Aggregation:
                            #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                            obj_SSResults.func__AgeNe_Man_EOR_Aggregate_Results__Aggregate_And_Group___At_Lowest_Detail(str_Search_Path)
                        pass
                        bool_Sim_AgeNe_EOR_Aggregation = True
                        if bool_Sim_AgeNe_EOR_Aggregation:
                            #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                            obj_SSResults.func__AgeNe_Sim_EOR_Aggregate_Results__Aggregate_And_Group___At_Lowest_Detail(str_Search_Path)
                        pass
                        bool_Sim_AgeNe_PF_Aggregation = True
                        if bool_Sim_AgeNe_PF_Aggregation:
                            #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                            obj_SSResults.func__AgeNe_Sim_PF_Aggregate_Results__Aggregate_And_Group___At_Lowest_Detail(str_Search_Path)
                        pass
                        bool_AgeNe_Man_EOR_Merge = True
                        if bool_AgeNe_Man_EOR_Merge:
                            #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                            obj_SSResults.func__AgeNe_Man_EOR_Merge_Results__Aggregate_And_Group___Into_One_Table(str_Search_Path)
                        pass
                        bool_AgeNe_Sim_EOR_Merge = True
                        if bool_AgeNe_Sim_EOR_Merge:
                            #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                            obj_SSResults.func__AgeNe_Sim_EOR_Merge_Results__Aggregate_And_Group___Into_One_Table(str_Search_Path)
                        pass
                        bool_AgeNe_Sim_PF_Merge = True
                        if bool_AgeNe_Sim_PF_Merge:
                            #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                            obj_SSResults.func__AgeNe_Sim_PF_Merge_Results__Aggregate_And_Group___Into_One_Table(str_Search_Path)
                        pass
                        bool_AgeNe_Sim_EOR_Summarise = True
                        if bool_AgeNe_Sim_EOR_Summarise:
                            #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                            obj_SSResults.func__AgeNe_Sim_EOR_Summarise_Results__Aggregate_And_Group___Into_One_Table(str_Search_Path)
                        pass
                        bool_AgeNe_Sim_PF_Summarise = True
                        if bool_AgeNe_Sim_PF_Summarise:
                            #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                            obj_SSResults.func__AgeNe_Sim_PF_Summarise_Results__Aggregate_And_Group___Into_One_Table(str_Search_Path)
                        pass
                    pass
                pass
            pass
     
      
            bool_Plot_AgeNe_Demographic_Profile = True
            if bool_Plot_AgeNe_Demographic_Profile:
                #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                str_Search_Path = self.obj_SSParams.str_Current_Run_Path__Batch_Scenario__Data
                str_Plot_Save_Path = os__path.join(self.obj_SSParams.str_Current_Run_Path__Batch_Scenario__UID, globalsSS.Processing_Path.static_str_Processing_Path__Plots) 
                with SSPlots(self.obj_SSParams) as obj_SSPlots:
                    obj_SSPlots.func__Plot_EXPERIMENT_AgeNe_Sim_Demographic_Population_Profile__Get_Data(str_Plot_Save_Path, str_Search_Path)
                pass
            pass     
#             bool_Plot_Sampling_Indivs = True
#             if bool_Plot_Sampling_Indivs:
#                 #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
#                 with SSPlots(self.obj_SSParams) as obj_SSPlots:
#                     obj_SSPlots.func__Plot_SAMPLING_INDIVS_Summary__Get_Data(str_Search_Path)
#                 pass
#             pass        
#             if (self.obj_SSParams.str_Species_Code[:1] != 'S') and (self.obj_SSParams.str_Species_Code[:1] != 'T')and (self.obj_SSParams.str_Species_Code[:1] != 'G'):
#                 bool_Plot_Exp2_PS_LDNe_And_Sim_AgeNe_Demographic_Profile = True
#                 if bool_Plot_Exp2_PS_LDNe_And_Sim_AgeNe_Demographic_Profile:
#                     #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
#                     with SSPlots(self.obj_SSParams) as obj_SSPlots:
#                         obj_SSPlots.func__Plot_EXPERIMENT_Parent_Offspring_Ne_2_PS_And_AgeNe_Sim_Demographic_Population_Profile__Get_Data(str_Search_Path)
#                     pass
#                 pass
#             pass        
        pass

        if globalsSS.Run_Processing_Step.static_int_Run_Processing_Step__SAMP_STRAT in self.obj_SSParams.list_int_App_Arg_Run_Processing_Steps:

              
            '''
            -----------------------
            Process Sampling Strategy processes
            -----------------------
            '''          
            bool_Run_All_STANDARD_Post_Sim_Processes = False 

            ''' Get the sampling plan for the accuracy guideline - ensure only the first value is used (there should only be one but just in case) '''
            #self.obj_SSParams.dict_Sampling_Plan_To_Use_For_Accuracy_Guideline = self.obj_SSParams.dict_Sampling_Strategy_Run_LDNe_Accuracy_Line_Sampling_Plan_Dict__PLAN_CODE__REPS
            self.obj_SSParams.dict_Sampling_Plan_To_Use_For_Accuracy_Guideline = {self.obj_SSParams.dict_Sampling_Strategy_Run_LDNe_Accuracy_Line_Sampling_Plan_Dict__PLAN_CODE__REPS.keys()[0]: self.obj_SSParams.dict_Sampling_Strategy_Run_LDNe_Accuracy_Line_Sampling_Plan_Dict__PLAN_CODE__REPS.values()[0]}
            str_Accuracy_Guideline_Sampling_Plan_Code = self.obj_SSParams.dict_Sampling_Plan_To_Use_For_Accuracy_Guideline.keys()[0]
            ''' Get the sampling plans code for the other sampling plans - if any are the same as the accuracy guideline code, remove them '''
            self.obj_SSParams.dict_Other_Sampling_Plans_To_Run = {str_Code:int_Replicates for str_Code,int_Replicates in self.obj_SSParams.dict_Sampling_Strategy_Run_LDNe_Other_Sampling_Plans_CSV_Dict__PLAN_CODE__REPS.items() if str_Code != str_Accuracy_Guideline_Sampling_Plan_Code} 
             
            bool_Process_Saved_Pops = True
            if bool_Process_Saved_Pops and bool_Process_Saved_Pops_CONFIRM:
                
                str_LDNE_Working_Path = self.obj_SSParams.str_Current_Run_Path__Sampling_Strategy__Data
                str_Search_Path__Saved_SimuPops = self.obj_SSParams.str_Batch_Scenario_UID_Path__Previous_Run

                with SSSamplingTest() as objSamplingTestOperation:
                    objSamplingTestOperation.method_Initialise(self.obj_SSParams)
                    ''' Search file pattern - USE THIS TO RUN ONLY CERTAIN POPS'''
                    str_File_Search_Pattern = '*M' + str(self.obj_SSParams.int_Total_MatingsToSimulatePerReplicate) + globalsSS.SS_Per_Fert_PF_File_Output_Details.static_Output_File_Suffix__SimuPOP_Pop_PF
                    
                    '''
                    Sampling Strategy sampling 
                    '''                            
                    bool_ALL_Exp_SAMP_STRAT_From_CONFIG = True
                    if bool_ALL_Exp_SAMP_STRAT_From_CONFIG and bool_ALL_Exp_SAMP_STRAT_From_CONFIG_CONFIRM:
                        if self.obj_SSParams.int_Sampling_Strategy_Sample_Proportions_Source == globalsSS.Experment_Groups.static_int_Experiment_Sampling_Strategy_v1_1__USER_AGE_COHORTS:
                            list_Experiments = [globalsSS.Experment_Groups.static_int_Experiment_Sampling_Strategy_v1_1__USER_AGE_COHORTS]
                            str_Experiment_Label = globalsSS.Experment_Groups.static_str_Experiment_Sampling_Strategy_v1_1__USER_AGE_COHORTS_Label
                            objSamplingTestOperation.method_Saved_Pop_SubSample_Ne2Bulk_Processing_of_SubSampling_Experiments(list_Experiments, str_Experiment_Label, str_LDNE_Working_Path, str_Search_Path__Saved_SimuPops, str_File_Search_Pattern)

                            pass
                        elif self.obj_SSParams.int_Sampling_Strategy_Sample_Proportions_Source == globalsSS.Experment_Groups.static_int_Experiment_Sampling_Strategy_v1_1__USER_PROPORTIONS:
                            list_Experiments = [globalsSS.Experment_Groups.static_int_Experiment_Sampling_Strategy_v1_1__USER_PROPORTIONS]
                            str_Experiment_Label = globalsSS.Experment_Groups.static_str_Experiment_Sampling_Strategy_v1_1__USER_PROPORTIONS_Label
                            objSamplingTestOperation.method_Saved_Pop_SubSample_Ne2Bulk_Processing_of_SubSampling_Experiments(list_Experiments, str_Experiment_Label, str_LDNE_Working_Path, str_Search_Path__Saved_SimuPops, str_File_Search_Pattern)

                            pass
                        elif self.obj_SSParams.int_Sampling_Strategy_Sample_Proportions_Source == globalsSS.Experment_Groups.static_int_Experiment_Sampling_Strategy_v1_1__USER_SAMPLE_NUMBERS:
                            list_Experiments = [globalsSS.Experment_Groups.static_int_Experiment_Sampling_Strategy_v1_1__USER_SAMPLE_NUMBERS]
                            str_Experiment_Label = globalsSS.Experment_Groups.static_str_Experiment_Sampling_Strategy_v1_1__USER_SAMPLE_NUMBERS_Label
                            objSamplingTestOperation.method_Saved_Pop_SubSample_Ne2Bulk_Processing_of_SubSampling_Experiments(list_Experiments, str_Experiment_Label, str_LDNE_Working_Path, str_Search_Path__Saved_SimuPops, str_File_Search_Pattern)

                        elif self.obj_SSParams.int_Sampling_Strategy_Sample_Proportions_Source == globalsSS.Experment_Groups.static_int_Experiment_Sampling_Strategy_v1_1__USER_SAMPLE_PROPORTIONS:
                            list_Experiments = [globalsSS.Experment_Groups.static_int_Experiment_Sampling_Strategy_v1_1__USER_SAMPLE_PROPORTIONS]
                            str_Experiment_Label = globalsSS.Experment_Groups.static_int_Experiment_Sampling_Strategy_v1_1__USER_SAMPLE_PROPORTIONS_Label
                            objSamplingTestOperation.method_Saved_Pop_SubSample_Ne2Bulk_Processing_of_SubSampling_Experiments(list_Experiments, str_Experiment_Label, str_LDNE_Working_Path, str_Search_Path__Saved_SimuPops, str_File_Search_Pattern)

                            pass
                        pass
                    pass                    
                
                    '''
                    Accuracy guidleline /and/or other LDNe sampling plans processing
                    '''
                    bool_ALL_Exp_Sampling_Proportions_Scaled_By_Max_Proportion_PSMP = object_SSConfigSamplingStrategy.static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_PSMP in self.obj_SSParams.dict_Other_Sampling_Plans_To_Run.keys() or \
                                                                                      object_SSConfigSamplingStrategy.static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_PSMP in self.obj_SSParams.dict_Sampling_Plan_To_Use_For_Accuracy_Guideline.keys()
                    if bool_ALL_Exp_Sampling_Proportions_Scaled_By_Max_Proportion_PSMP and bool_ALL_Exp_Sampling_Proportions_Scaled_By_Max_Proportion_PSMP__CONFIRM:
                        list_Experiments = [globalsSS.Experment_Groups.static_int_Experiment_SAMPLING_PROPORTIONS_SCALED_BY_MAX_PROPORTION]
                        str_Experiment_Label = globalsSS.Experment_Groups.static_str_Experiment_SAMPLING_PROPORTIONS_SCALED_BY_MAX_PROPORTION_Label                        
                        objSamplingTestOperation.method_Saved_Pop_SubSample_Ne2Bulk_Processing_of_SubSampling_Experiments(list_Experiments, str_Experiment_Label, str_LDNE_Working_Path, str_Search_Path__Saved_SimuPops, str_File_Search_Pattern)
                    pass
                
                    #bool_ALL_Exp_100_Percent_User_Specified_Age_Cohorts_1_0 = True
                    bool_ALL_Exp_100_Percent_User_Specified_Age_Cohorts_1_0 = object_SSConfigSamplingStrategy.static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FAC in self.obj_SSParams.dict_Other_Sampling_Plans_To_Run.keys() or \
                                                                              object_SSConfigSamplingStrategy.static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FAC in self.obj_SSParams.dict_Sampling_Plan_To_Use_For_Accuracy_Guideline.keys()
                    if bool_ALL_Exp_100_Percent_User_Specified_Age_Cohorts_1_0 and bool_ALL_Exp_100_Percent_User_Specified_Age_Cohorts_1_0_CONFIRM:
                        list_Experiments = [globalsSS.Experment_Groups.static_int_Experiment_100_PERCENT_USER_SPECIFIED_AGE_COHORTS_v1_0]
                        str_Experiment_Label = globalsSS.Experment_Groups.static_str_Experiment_100_PERCENT_USER_SPECIFIED_AGE_COHORTS_v1_0_Label                        
                        objSamplingTestOperation.method_Saved_Pop_SubSample_Ne2Bulk_Processing_of_SubSampling_Experiments(list_Experiments, str_Experiment_Label, str_LDNE_Working_Path, str_Search_Path__Saved_SimuPops, str_File_Search_Pattern)
                    pass
                
                    #bool_ALL_Exp_Full_Embry_Cohort_FEM_ = True
                    bool_ALL_Exp_Full_Embryo_Cohort_FEM = object_SSConfigSamplingStrategy.static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FEM in self.obj_SSParams.dict_Other_Sampling_Plans_To_Run.keys() or \
                                                          object_SSConfigSamplingStrategy.static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FEM in self.obj_SSParams.dict_Sampling_Plan_To_Use_For_Accuracy_Guideline.keys()
                    if bool_ALL_Exp_Full_Embryo_Cohort_FEM and bool_ALL_Exp_Full_Embryo_Cohort_FEM__CONFIRM:
                        list_Experiments = [globalsSS.Experment_Groups.static_int_Experiment_FULL_EMBRYO_COHORT]
                        str_Experiment_Label = globalsSS.Experment_Groups.static_str_Experiment_FULL_EMBRYO_COHORT_Label                        
                        objSamplingTestOperation.method_Saved_Pop_SubSample_Ne2Bulk_Processing_of_SubSampling_Experiments(list_Experiments, str_Experiment_Label, str_LDNE_Working_Path, str_Search_Path__Saved_SimuPops, str_File_Search_Pattern)
                    pass
                
                    #bool_ALL_Exp_Full_Juvenile_Cohorts_FJV = True
                    bool_ALL_Exp_Full_Juvenile_Cohorts_FJV = object_SSConfigSamplingStrategy.static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FJV in self.obj_SSParams.dict_Other_Sampling_Plans_To_Run.keys() or \
                                                             object_SSConfigSamplingStrategy.static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FJV in self.obj_SSParams.dict_Sampling_Plan_To_Use_For_Accuracy_Guideline.keys()
                    if bool_ALL_Exp_Full_Juvenile_Cohorts_FJV and bool_ALL_Exp_Full_Juvenile_Cohorts_FJV__CONFIRM:
                        list_Experiments = [globalsSS.Experment_Groups.static_int_Experiment_FULL_JUVENILE_COHORTS]
                        str_Experiment_Label = globalsSS.Experment_Groups.static_str_Experiment_FULL_JUVENILE_COHORTS_Label                        
                        objSamplingTestOperation.method_Saved_Pop_SubSample_Ne2Bulk_Processing_of_SubSampling_Experiments(list_Experiments, str_Experiment_Label, str_LDNE_Working_Path, str_Search_Path__Saved_SimuPops, str_File_Search_Pattern)
                    pass
                
                    #bool_ALL_Exp_Full_Adult_Cohorts_FMT = True
                    bool_ALL_Exp_Full_Adult_Cohorts_FMT = object_SSConfigSamplingStrategy.static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FMT in self.obj_SSParams.dict_Other_Sampling_Plans_To_Run.keys() or \
                                                          object_SSConfigSamplingStrategy.static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FMT in self.obj_SSParams.dict_Sampling_Plan_To_Use_For_Accuracy_Guideline.keys()
                    if bool_ALL_Exp_Full_Adult_Cohorts_FMT and bool_ALL_Exp_Full_Adult_Cohorts_FMT__CONFIRM:
                        list_Experiments = [globalsSS.Experment_Groups.static_int_Experiment_FULL_ADULT_COHORTS]
                        str_Experiment_Label = globalsSS.Experment_Groups.static_str_Experiment_FULL_ADULT_COHORTS_Label                        
                        objSamplingTestOperation.method_Saved_Pop_SubSample_Ne2Bulk_Processing_of_SubSampling_Experiments(list_Experiments, str_Experiment_Label, str_LDNE_Working_Path, str_Search_Path__Saved_SimuPops, str_File_Search_Pattern)
                    pass
                
                    #bool_ALL_Exp_Full_Sampling_Of_Cohorts_FUL = True
                    bool_ALL_Exp_Full_Sampling_Of_Cohorts_FUL = object_SSConfigSamplingStrategy.static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FUL in self.obj_SSParams.dict_Other_Sampling_Plans_To_Run.keys() or \
                                                                object_SSConfigSamplingStrategy.static_str_Value__Sampling_Strategy_Run_LDNe_Sampling_Plan_Code_FUL in self.obj_SSParams.dict_Sampling_Plan_To_Use_For_Accuracy_Guideline.keys()
                    if bool_ALL_Exp_Full_Sampling_Of_Cohorts_FUL and bool_ALL_Exp_Full_Sampling_Of_Cohorts_FUL__CONFIRM:
                        list_Experiments = [globalsSS.Experment_Groups.static_int_Experiment_FULL_SAMPLING_OF_COHORTS]
                        str_Experiment_Label = globalsSS.Experment_Groups.static_str_Experiment_FULL_SAMPLING_OF_COHORTS_Label                        
                        objSamplingTestOperation.method_Saved_Pop_SubSample_Ne2Bulk_Processing_of_SubSampling_Experiments(list_Experiments, str_Experiment_Label, str_LDNE_Working_Path, str_Search_Path__Saved_SimuPops, str_File_Search_Pattern)
                    pass
 
                               
                    bool_ALL_Exp_2_2 = False #True
                    if bool_ALL_Exp_2_2 and bool_Process_Saved_Pops__ALL_Exp_2_2_CONFIRM:
                        #list_Experiments = [2]
                        #str_Experiment_Label = 'EXP2_2'
                        list_Experiments = [globalsSS.Experment_Groups.static_int_Experiment_2_Ver_2]
                        str_Experiment_Label = globalsSS.Experment_Groups.static_str_Experiment_2_Ver_2_Label                        
                        objSamplingTestOperation.method_Saved_Pop_SubSample_Ne2Bulk_Processing_of_SubSampling_Experiments(list_Experiments, str_Experiment_Label, str_LDNE_Working_Path, str_Search_Path__Saved_SimuPops, str_File_Search_Pattern)
                    pass
                pass
            pass
    
            bool_ReRun_Ne2_FAILED_Processes = True
            if bool_ReRun_Ne2_FAILED_Processes and bool_Process_Saved_Pops_CONFIRM:
                str_LDNE_Working_Path = self.obj_SSParams.str_Current_Run_Path__Sampling_Strategy__Data
                #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                with SSSamplingTest() as objSamplingTestOperation:
                    objSamplingTestOperation.method_Initialise(self.obj_SSParams)
                    objSamplingTestOperation.method_Saved_Pop_SubSample_Ne2Bulk_Rerunning_of_FAILED_Ne2(str_LDNE_Working_Path)
                pass
            pass
                
                    
            bool_Saved_Pops_Categorised_Ne2_PF_Aggregation = True
            if bool_Saved_Pops_Categorised_Ne2_PF_Aggregation and bool_Saved_Pops_Categorised_Ne2_PF_Aggregation_CONFIRM:
                str_Search_Path = self.obj_SSParams.str_Current_Run_Path
                #str_Search_Path__Batch_Scenario_Logs = self.obj_SSParams.str_Current_Run_Path__Batch_Scenario__Logs
                str_Search_Path__Sampling_Strategy_Logs = self.obj_SSParams.str_Current_Run_Path__Sampling_Strategy__Logs
                str_Search_Path__Batch_Scenario_Data = self.obj_SSParams.str_Current_Run_Path__Batch_Scenario__Data
                str_Search_Path__Sampling_Strategy_Data = self.obj_SSParams.str_Current_Run_Path__Sampling_Strategy__Data
                #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                #str_Search_Path = 'C:\\DCB\\MUI\\MUI_Sync_Controlled\\MUI_SC_SharkSim\\v2_75_Py27\\Test\\SS_2_75_Run_2015_05_15_11_42_22\\'
                str_Excel_Save_Path = str_Search_Path__Sampling_Strategy_Data #self.str_Current_Run_Path__Sampling_Strategy__UID
                bool_Aggregate_PS_PF_Results = True
                if bool_Aggregate_PS_PF_Results and bool_Aggregate_PS_PF_Results_CONFIRM:
                    with SSResults(self.obj_SSParams) as obj_SSResults:
    
                        bool_Aggregate_Sampling = True
                        if bool_Aggregate_Sampling:
                            bool_Aggregate_Sampling_Indivs = True
                            if bool_Aggregate_Sampling_Indivs:
                                #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                                with SSResults(self.obj_SSParams) as obj_SSResults:
                                    obj_SSResults.func__Sampling_Individuals_Results__Aggregate_And_Group(str_Excel_Save_Path, str_Search_Path__Sampling_Strategy_Logs)
                                pass
                            pass
                            bool_Aggregate_Sampling_Indivs_Summary = True
                            if bool_Aggregate_Sampling_Indivs_Summary:
                                #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                                with SSResults(self.obj_SSParams) as obj_SSResults:
                                    obj_SSResults.func__Sampling_Individuals_Results_SUMMARY__Aggregate_And_Group(str_Excel_Save_Path, str_Search_Path__Sampling_Strategy_Data)
                                pass
                            pass 
                        pass
                    
                        bool_Ne2_LDNe_Aggregate_Results = True
                        if bool_Ne2_LDNe_Aggregate_Results:
                            bool_PS_PF_Aggregate = True
                            if bool_PS_PF_Aggregate:
                                obj_SSResults.func_EXPERIMENT_Parent_Offspring_Ne_2__Ne2_PS_PF_Results__Aggregate_Results(str_Excel_Save_Path, str_Search_Path__Sampling_Strategy_Data)
                            pass
                            bool_PS_PF_Categorise = True
                            if bool_PS_PF_Categorise:
                                obj_SSResults.func_EXPERIMENT_Parent_Offspring_Ne_2__PS_Categorised_Results__Aggregate_Results(str_Excel_Save_Path, str_Search_Path__Sampling_Strategy_Data)
                            pass
                            bool_PS_PF_Merge = True
                            if bool_PS_PF_Merge:
                                
                                #DEBUG_ON
                                bool_Pause = False
                                if bool_Pause:
                                    with globalsSS.Pause_Console() as obj_Pause:
                                        obj_Pause.method_Pause_Console(str_Message='Pausing to allow input to be altered for testing..')
                                    pass
                                pass
                                #DEBUG_OFF    
                                                            
                                obj_SSResults.func_EXPERIMENT_Parent_Offspring_Ne_2__PS_Composite_Results__Aggregate_Results(str_Excel_Save_Path, str_Search_Path__Batch_Scenario_Data, str_Search_Path__Sampling_Strategy_Data)
                            pass
                            bool_PS_PF_Summarise = True
                            if bool_PS_PF_Summarise:
                                obj_SSResults.func_EXPERIMENT_Parent_Offspring_Ne_2__PS_Summary_Results__Aggregate_Results(str_Excel_Save_Path, str_Search_Path__Sampling_Strategy_Data)
                            pass
                        pass
    
                    pass
                pass
#     
#                 bool_Plot_AgeNe_Demographic_Profile = True
#                 if bool_Plot_AgeNe_Demographic_Profile:
#                     #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
#                     with SSPlots(self.obj_SSParams) as obj_SSPlots:
#                         obj_SSPlots.func__Plot_EXPERIMENT_AgeNe_Sim_Demographic_Population_Profile__Get_Data(str_Search_Path)
#                     pass
#                 pass     
#                 bool_Plot_Sampling_Indivs = True
#                 if bool_Plot_Sampling_Indivs:
#                     #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
#                     with SSPlots(self.obj_SSParams) as obj_SSPlots:
#                         obj_SSPlots.func__Plot_SAMPLING_INDIVS_Summary__Get_Data(str_Search_Path)
#                     pass
#                 pass        
#                 if (self.obj_SSParams.str_Species_Code[:1] != 'S') and (self.obj_SSParams.str_Species_Code[:1] != 'T')and (self.obj_SSParams.str_Species_Code[:1] != 'G'):
#                     bool_Plot_Exp2_PS_LDNe_And_Sim_AgeNe_Demographic_Profile = True
#                     if bool_Plot_Exp2_PS_LDNe_And_Sim_AgeNe_Demographic_Profile:
#                         #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
#                         with SSPlots(self.obj_SSParams) as obj_SSPlots:
#                             obj_SSPlots.func__Plot_EXPERIMENT_Parent_Offspring_Ne_2_PS_And_AgeNe_Sim_Demographic_Population_Profile__Get_Data(str_Search_Path)
#                         pass
#                     pass
#                 pass
#             pass

            bool_Plot_Sampling_Indivs = True
            if bool_Plot_Sampling_Indivs and bool_Plot_Sampling_Indivs_CONFIRM:
                #str_Search_Path = self.obj_SSParams.str_Current_Run_Path__Sampling_Strategy__Data
                str_Search_Path__Batch_Scenario_Data = self.obj_SSParams.str_Current_Run_Path__Batch_Scenario__Data
                str_Search_Path__Sampling_Strategy_Data = self.obj_SSParams.str_Current_Run_Path__Sampling_Strategy__Data
                str_Plot_Save_Path = os__path.join(self.obj_SSParams.str_Current_Run_Path__Sampling_Strategy__UID, globalsSS.Processing_Path.static_str_Processing_Path__Plots)
                with SSPlots(self.obj_SSParams) as obj_SSPlots:
                    obj_SSPlots.func__Plot_SAMPLING_INDIVS_Summary__Get_Data(str_Plot_Save_Path, str_Search_Path__Batch_Scenario_Data, str_Search_Path__Sampling_Strategy_Data)
                pass
            pass        
    
            bool_Plot_Sampling_Plans_Accuracy_And_Others = True
            if bool_Plot_Sampling_Plans_Accuracy_And_Others and bool_Plot_Sampling_Plans_Accuracy_And_Others_CONFIRM:
                #str_Search_Path = self.obj_SSParams.str_Current_Run_Path__Sampling_Strategy__Data
                str_Search_Path__Batch_Scenario_Data = self.obj_SSParams.str_Current_Run_Path__Batch_Scenario__Data
                str_Search_Path__Sampling_Strategy_Data = self.obj_SSParams.str_Current_Run_Path__Sampling_Strategy__Data
                str_Plot_Save_Path = os__path.join(self.obj_SSParams.str_Current_Run_Path__Sampling_Strategy__UID, globalsSS.Processing_Path.static_str_Processing_Path__Plots)
                with SSPlots(self.obj_SSParams) as obj_SSPlots:
                    obj_SSPlots.func__Plot_SAMPLING_PLANS_Accuracy_And_Others_Summary__Get_Data(str_Plot_Save_Path, str_Search_Path__Batch_Scenario_Data, str_Search_Path__Sampling_Strategy_Data)
                pass
            pass        
    
        
            bool_Plot_EXP_SAMP_STRAT_1_0_Results = True
            if bool_Plot_EXP_SAMP_STRAT_1_0_Results:
                with SSPlots(self.obj_SSParams) as obj_SSPlots:
                    list_int_Mating_Count_Replicate_Totals_To_Process = [self.obj_SSParams.int_Total_MatingsToSimulatePerReplicate]
                    #str_Search_Path = self.obj_SSParams.str_Current_Run_Base_Path
                    #str_Search_Path = self.obj_SSParams.strOutputLocation_CumulativeRun_Path
                    str_Search_Path = self.obj_SSParams.str_Current_Run_Path__Sampling_Strategy__Data #+ '\\EXP_SAMP_STRAT_1_0_New_Plots\\'
                    str_Plot_Save_Path = os__path.join(self.obj_SSParams.str_Current_Run_Path__Sampling_Strategy__UID, globalsSS.Processing_Path.static_str_Processing_Path__Plots) 
                    list_Search_Paths = [str_Search_Path]
                    obj_SSPlots.func__Plot_EXP_Sampling_Strategy_1_0_EOR_SUMM__Get_Data(str_Plot_Save_Path, list_int_Mating_Count_Replicate_Totals_To_Process, list_Search_Paths)
                pass
            pass         

           
        return True
    
    def __exit__(self, type, value, traceback): 

        ''' Close loggers '''
        #self.obj_Log_RL.handlers = []
        
        return None

    '''            
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS FINALIZATION
    '''
