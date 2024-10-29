
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
#from collections import defaultdict

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import SharkSim modules
from globals_SharkSim import globalsSS
from AutoVivificationHandler import AutoVivificationHandler
from OutputHandler import OutputHandler
from SSAnalysisHandler import SSAnalysisHandler


class object_SSBatch_V2:
    """Contains SS Batch level properties and methods"""
    def __enter__(self):

        class obj_SSBatch_V2():

# -------------- Class specific routines

            __slots__ = ('stringDelimiter'
                         ,'stringDelimiter2'
                         ,'objSSParametersLocal'

                         ,'intLevel'
                         ,'self.str_Current_Col_Index'
                         
                         #Reporting vars
                         ,'dict_Rep_1_DataSectionNotesLevels'
                        ,'dict_Rep_50_strUniqueRunID'
                        ,'dict_Rep_60_SimCurrentBatch'
                        ,'dict_Rep_70_SimCurrentReplicate'
                        
                        ,'dict_Rep_400_BatchRunStart'
                        ,'dict_Rep_500_ReplicateRunStart'
                        ,'dict_Rep_600_SimCurrentBatch'
                        ,'dict_Rep_700_SimCurrentReplicate'
                        #Pop Size
                        ,'dict_Rep_800_SimPopulationSize'
                        #Replicates
                        ,'dict_Rep_900_IterationsToSimulate'
                        #Current Batch?
                        ,'dict_Rep_1000_CurrentIteration'
                        #Initial Ages - Initial Age Dist
                        ,'dict_Rep_1100_InitialAgesRandom'
                        #Initial Male Sex Ratio
                        ,'dict_Rep_1200_InitialMaleSexRatio'
                        ,'dict_Rep_1300_MatingScheme'
                        ,'dict_Rep_1400_MaxAge'
                        ,'dict_Rep_1500_MaxMatingAge'
                        ,'dict_Rep_1600_MinMatingAge'
                        ,'dict_Rep_1700_intMinNumOffspring'
                        ,'dict_Rep_1800_meanvarnumOffspring'
                        ,'dict_Rep_1900_intMaxNumOffspring'
                        # Start - listOffspringNumberParameters
                        ,'dict_Rep_2000_PredictedBreedingPopulationSize'
                        ,'dict_Rep_2100_MeanOffspringPerIndiv'
                        ,'dict_Rep_2200_MatingDistType'
                        ,'dict_Rep_2300_MatingDistParamList'
                        # End - listOffspringNumberParameters
                        ,'dict_Rep_2400_NumLoci'
                        ,'dict_Rep_2500_NumAllelesPerLoci'
                        ,'dict_Rep_2600_LociAlleleFreqScheme'
                        #Start - listAlleleFreqs
                        ,'dict_Rep_2700_InitialLociAlleleFreqList'
                        ,'dict_Rep_2800_dictSimImportedLocusNames'
                        ,'dict_Rep_2900_dictSimImportedLocusAlleleNames'
                        #End - listAlleleFreqs
                        ,'dict_Rep_2950_bool_Allow_Mutation'
                        ,'dict_Rep_2910_float_Mutation_Rate'
                        #Reporting vars
                        ,'dict_Rep_3000_boolReportDemographicNe'
                        ,'dict_Rep_3100_boolReportLDNe'
                        ,'dict_Rep_3200_listLociToReportNE'
                        ,'dict_Rep_3300_boolReportTemporalFS_P1_Ne'
                        ,'dict_Rep_3400_boolReportTemporalFS_P2_Ne'
                         #--------------------------------- 5 params
                        
                        ,'dict_Rep_3500_intMatingCalenderMonth'
                        ,'dict_Rep_3600_intParturitionCalenderMonth'
                        
                        ,'dict_Rep_3700_intGestationLengthInMonths'
                        ,'dict_Rep_3800_intReproductiveRestLengthInMonths'
                         #--------------------------------- 4 params
                        
                        ,'dict_Rep_3900_intTotalYearsToSimulate'
                        ,'dict_Rep_4000_intTotalMonthsToSimulate'
                         #--------------------------------- 2 params
                        ,'dict_Rep_4100_boolSuppressBurnInOutput'
                        
                        
                        #mortality vars
                        ,'dict_Rep_4200_boolAllowNATURALMortality'
                        ,'dict_Rep_4300_dictProbabilityDistribution_P_SurvivalNATURALBySexByAge'
                         #--------------------------------- 2 params
                        ,'dict_Rep_4400_boolAllowUnNATURALMortality'
                        ,'dict_Rep_4500_dictProbabilityDistribution_P_SurvivalUnNATURALBySexByAge'
                         #--------------------------------- 2 params
                        ,'dict_Rep_4600_boolReportSimAgeNe'                        
                        )

            def __init__(self):
                
                self.stringDelimiter = globalsSS.StringDelimiters.static_stringDelimiter_SEMI_COLON
                self.stringDelimiter2 = globalsSS.StringDelimiters.static_stringDelimiter_COMMA
                self.str_ID_Suf = globalsSS.StringDelimiters.static_stringDelimiter_SPACE
                
                self.objSSParametersLocal = None
                self.intLevel = 2
                self.str_Current_Col_Index = str(
                                                 str(self.intLevel) +
                                                 globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                                 '0' +
                                                 globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                                 '0' +
                                                 globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                                 '0')
                
                self.dict_Rep_1_DataSectionNotesLevels = {}

                self.dict_Rep_50_strUniqueRunID = {}
                self.dict_Rep_60_SimCurrentBatch = {}
                self.dict_Rep_70_SimCurrentReplicate = {}
                                
                #self.dict_Rep_200_ReplicateBatches = {}
                #self.dict_Rep_300_CurrentReplicateBatch = {}

                self.dict_Rep_400_BatchRunStart = {}
                self.dict_Rep_500_ReplicateRunStart = {}

                self.dict_Rep_600_SimCurrentBatch = {}
                self.dict_Rep_700_SimCurrentReplicate = {}
                
                self.dict_Rep_800_SimPopulationSize = {}
                self.dict_Rep_900_IterationsToSimulate = {}
                self.dict_Rep_1000_CurrentIteration = {}
                self.dict_Rep_1100_InitialAgesRandom = {}
                self.dict_Rep_1200_InitialMaleSexRatio = {}
                self.dict_Rep_1300_MatingScheme = {}
                self.dict_Rep_1400_MaxAge = {}
                self.dict_Rep_1500_MaxMatingAge = {}
                self.dict_Rep_1600_MinMatingAge = {}

                self.dict_Rep_1700_intMinNumOffspring = {}
                self.dict_Rep_1800_meanvarnumOffspring = {}
                self.dict_Rep_1900_intMaxNumOffspring = {}
                        
                self.dict_Rep_2000_PredictedBreedingPopulationSize = {}
                self.dict_Rep_2100_MeanOffspringPerIndiv = {}
                self.dict_Rep_2200_MatingDistType = {}
                self.dict_Rep_2300_MatingDistParamList = {}
                self.dict_Rep_2400_NumLoci = {}
                self.dict_Rep_2500_NumAllelesPerLoci = {}
                self.dict_Rep_2600_LociAlleleFreqScheme = {}
                self.dict_Rep_2700_InitialLociAlleleFreqList = {}
                self.dict_Rep_2800_dictSimImportedLocusNames = {}
                self.dict_Rep_2900_dictSimImportedLocusAlleleNames = {}
                self.dict_Rep_2950_bool_Allow_Mutation = {}
                self.dict_Rep_2910_float_Mutation_Rate = {}
                                
                self.dict_Rep_3000_boolReportDemographicNe = {}
                self.dict_Rep_3100_boolReportLDNe = {}
                self.dict_Rep_3200_listLociToReportNE = {}
                self.dict_Rep_3300_boolReportTemporalFS_P1_Ne = {}
                self.dict_Rep_3400_boolReportTemporalFS_P2_Ne = {}
                self.dict_Rep_3500_intMatingCalenderMonth = {}
                self.dict_Rep_3600_intParturitionCalenderMonth = {}
                self.dict_Rep_3700_intGestationLengthInMonths = {}
                self.dict_Rep_3800_intReproductiveRestLengthInMonths = {}
                self.dict_Rep_3900_intTotalYearsToSimulate = {}
                self.dict_Rep_4000_intTotalMonthsToSimulate = {}
                self.dict_Rep_4100_boolSuppressBurnInOutput = {}
                self.dict_Rep_4200_boolAllowNATURALMortality = {}
                self.dict_Rep_4300_dictProbabilityDistribution_P_SurvivalNATURALBySexByAge = {}
                self.dict_Rep_4400_boolAllowUnNATURALMortality = {}
                self.dict_Rep_4500_dictProbabilityDistribution_P_SurvivalUnNATURALBySexByAge = {}
                self.dict_Rep_4600_boolReportSimAgeNe = {}                        

                return None
            
            def method_PopulateProperties(self):
                    
                
                #self.dict_Rep_1_DataSectionNotesLevels[self.intLevel]['Data_Section_Note_' + str(self.intLevel)] = 'Batch_Level_Params'
                self.dict_Rep_1_DataSectionNotesLevels[self.Get_Log_Current_Column_Index(True, True, self.str_ID_Suf) + 'Data_Section_Note_' + str(self.intLevel)] = 'Batch_Level_Params'

                self.dict_Rep_50_strUniqueRunID[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Unique_Run_ID'] = self.objSSParametersLocal.strUniqueRunID
                self.dict_Rep_60_SimCurrentBatch[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Sim_Current_Batch'] = self.objSSParametersLocal.intCurrentBatch
                self.dict_Rep_70_SimCurrentReplicate[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Sim_Current_Replicate'] = self.objSSParametersLocal.intCurrentReplicate
                
                #self.dict_Rep_200_ReplicateBatches[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Replicate_Batches'] = self.objSSParametersLocal.intReplicateBatches
                #self.dict_Rep_300_CurrentReplicateBatch[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Current_Replicate_Batch'] = self.objSSParametersLocal.intCurrentReplicateBatch

                self.dict_Rep_400_BatchRunStart[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Batch_Run_Started_Y_m_d_H_M_S'] = self.objSSParametersLocal.dateBatchRunStartTime.strftime("%Y_%m_%d_%H_%M_%S")
                self.dict_Rep_500_ReplicateRunStart[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Replicate_Run_Started_Y_m_d_H_M_S'] = self.objSSParametersLocal.dateReplicateRunStartTime.strftime("%Y_%m_%d_%H_%M_%S")

                self.dict_Rep_600_SimCurrentBatch[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Sim_Current_Batch'] = self.objSSParametersLocal.intCurrentBatch
                self.dict_Rep_700_SimCurrentReplicate[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Sim_Current_Replicate'] = self.objSSParametersLocal.intCurrentReplicate
                
                self.dict_Rep_800_SimPopulationSize[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Sim_Population_size'] = self.objSSParametersLocal.popnSize
                self.dict_Rep_900_IterationsToSimulate[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Grand_Total_Months_to_simulate'] = self.objSSParametersLocal.intGrandTotalMonthsToSimulate
                self.dict_Rep_1000_CurrentIteration[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Current_Month'] = self.objSSParametersLocal.intSimulationCurrentMonth
                self.dict_Rep_1100_InitialAgesRandom[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Initial_population_ages_scheme'] = self.objSSParametersLocal.intPopulationInitialAges
                self.dict_Rep_1200_InitialMaleSexRatio[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Male_sex_ratio_initial'] = self.objSSParametersLocal.floatSexRatioOfMales
                self.dict_Rep_1300_MatingScheme[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mating_scheme'] = self.objSSParametersLocal.intMatingSchemeType
                str_Colname_Prefix = globalsSS.Colnames_BATCH_PARAMETERS.static_str_Colname_Max_age
                #self.dict_Rep_1400_MaxAge[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Maximum_age'] = self.objSSParametersLocal.maxAge
                self.dict_Rep_1400_MaxAge[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + str_Colname_Prefix] = self.objSSParametersLocal.maxAge
                str_Colname_Prefix = globalsSS.Colnames_BATCH_PARAMETERS.static_str_Colname_Max_mating_age
                #self.dict_Rep_1500_MaxMatingAge[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Maximal_mating_age'] = self.objSSParametersLocal.maxMatingAge
                self.dict_Rep_1500_MaxMatingAge[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + str_Colname_Prefix] = self.objSSParametersLocal.maxMatingAge
                str_Colname_Prefix = globalsSS.Colnames_BATCH_PARAMETERS.static_str_Colname_Min_mating_age
                #self.dict_Rep_1600_MinMatingAge[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Minimal_mating_age'] = self.objSSParametersLocal.minMatingAge
                self.dict_Rep_1600_MinMatingAge[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + str_Colname_Prefix] = self.objSSParametersLocal.minMatingAge
                
                self.dict_Rep_1700_intMinNumOffspring[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Min_Num_Offspring'] = self.objSSParametersLocal.intMinNumOffspring
                self.dict_Rep_1800_meanvarnumOffspring[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Var_Num_Offspring'] = self.objSSParametersLocal.meanvarnumOffspring
                self.dict_Rep_1900_intMaxNumOffspring[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Max_Num_Offspring'] = self.objSSParametersLocal.intMaxNumOffspring
                                
                self.dict_Rep_2000_PredictedBreedingPopulationSize[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Predicted_Breeding_Pop_Size'] = self.objSSParametersLocal.intPredictedBreedingPopulationSize
                self.dict_Rep_2100_MeanOffspringPerIndiv[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_number_of_offspring_per_individual'] = self.objSSParametersLocal.meanvarnumOffspring
                self.dict_Rep_2200_MatingDistType[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mating_distribution_type'] = self.objSSParametersLocal.listOffspringNumberParameters[0]
                with OutputHandler() as objOutputOperation:
                    strDelimitedValues = objOutputOperation.method_AccumulateListValuesIntoDelimetedString(self.objSSParametersLocal.listOffspringNumberParameters, self.stringDelimiter2)
                    self.dict_Rep_2300_MatingDistParamList[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mating_distribution_parameter_list'] = strDelimitedValues
                self.dict_Rep_2400_NumLoci[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Number_of_loci'] = self.objSSParametersLocal.nLoci
                #Subtract 1 for real number of alleles per locus    
                self.dict_Rep_2500_NumAllelesPerLoci[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Number_of_alleles_per_loci'] = self.objSSParametersLocal.nAllelesPerLoci-1
                self.dict_Rep_2600_LociAlleleFreqScheme[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Loci_allele_frequencies_scheme'] = self.objSSParametersLocal.intAlleleFrequencyScheme
                with OutputHandler() as objOutputOperation:
                    strDelimitedValues = objOutputOperation.method_AccumulateListValuesIntoDelimetedString(self.objSSParametersLocal.listAlleleFreqs, self.stringDelimiter2)
                    self.dict_Rep_2700_InitialLociAlleleFreqList[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Loci_initial_allele_frequencies_list'] = strDelimitedValues
                    pass
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    listAlleleNames = []
                    listAlleleNames = objSSAnalysisOperation.method_Extract_Imported_Allele_Info_To_List(self.objSSParametersLocal.odictAlleleFreqsAtSimInitialization, 'Locus_Name')
                    with OutputHandler() as objOutputOperation:
                        strDelimitedValues = objOutputOperation.method_AccumulateListValuesIntoDelimetedString(listAlleleNames, self.stringDelimiter2)
                        self.dict_Rep_2800_dictSimImportedLocusNames[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Sim_Imported_Locus_Names'] = strDelimitedValues
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    listAlleleNames = []
                    listAlleleNames = objSSAnalysisOperation.method_Extract_Imported_Allele_Info_To_List(self.objSSParametersLocal.odictAlleleFreqsAtSimInitialization, 'Allele_Name')
                    with OutputHandler() as objOutputOperation:
                        strDelimitedValues = objOutputOperation.method_AccumulateListValuesIntoDelimetedString(listAlleleNames, self.stringDelimiter2)
                        self.dict_Rep_2900_dictSimImportedLocusAlleleNames[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Sim_Imported_Locus_Allele_Names'] = strDelimitedValues

                self.dict_Rep_2950_bool_Allow_Mutation[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Allow_Mutation'] = self.objSSParametersLocal.bool_Allow_Mutation
                self.dict_Rep_2910_float_Mutation_Rate[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mutation_Rate'] = self.objSSParametersLocal.float_Mutation_Rate

                self.dict_Rep_3000_boolReportDemographicNe[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ReportDemographicNe'] = self.objSSParametersLocal.boolReportDemographicNe
                self.dict_Rep_3100_boolReportLDNe[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ReportLDNe'] = self.objSSParametersLocal.boolReportLDNe
                self.dict_Rep_3200_listLociToReportNE[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'listLociToReportNE'] = self.objSSParametersLocal.listLociToReportNE
                self.dict_Rep_3300_boolReportTemporalFS_P1_Ne[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ReportTemporalFS_P1_Ne'] = self.objSSParametersLocal.boolReportTemporalFS_P1_Ne
                self.dict_Rep_3400_boolReportTemporalFS_P2_Ne[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ReportTemporalFS_P2_Ne'] = self.objSSParametersLocal.boolReportTemporalFS_P2_Ne
                self.dict_Rep_3500_intMatingCalenderMonth[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'MatingCalenderMonth'] = self.objSSParametersLocal.intMatingCalenderMonth
                self.dict_Rep_3600_intParturitionCalenderMonth[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ParturitionCalenderMonth'] = self.objSSParametersLocal.intParturitionCalenderMonth
                self.dict_Rep_3700_intGestationLengthInMonths[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'GestationLengthInMonths'] = self.objSSParametersLocal.intGestationLengthInMonths
                self.dict_Rep_3800_intReproductiveRestLengthInMonths[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ReproductiveRestLengthInMonths'] = self.objSSParametersLocal.intReproductiveRestLengthInMonths
                self.dict_Rep_3900_intTotalYearsToSimulate[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'TotalYearsToSimulate'] = self.objSSParametersLocal.intTotalYearsToSimulate
                self.dict_Rep_4000_intTotalMonthsToSimulate[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'TotalMonthsToSimulate'] = self.objSSParametersLocal.intTotalMonthsToSimulate
                self.dict_Rep_4100_boolSuppressBurnInOutput[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'SuppressBurnInOutput'] = self.objSSParametersLocal.boolSuppressBurnInOutput
                self.dict_Rep_4200_boolAllowNATURALMortality[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'AllowNATURALMortality'] = self.objSSParametersLocal.boolAllowNATURALMortality
                self.dict_Rep_4300_dictProbabilityDistribution_P_SurvivalNATURALBySexByAge[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ProbabilityDistribution_P_SurvivalNATURALBySexByAge'] = self.objSSParametersLocal.dictProbabilityDistribution_P_SurvivalNATURALBySexByAge
                self.dict_Rep_4400_boolAllowUnNATURALMortality[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'AllowUnNATURALMortality'] = self.objSSParametersLocal.boolAllowUnNATURALMortality
                self.dict_Rep_4500_dictProbabilityDistribution_P_SurvivalUnNATURALBySexByAge[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ProbabilityDistribution_P_SurvivalUnNATURALBySexByAge'] = self.objSSParametersLocal.dictProbabilityDistribution_P_SurvivalUnNATURALBySexByAge
                self.dict_Rep_4600_boolReportSimAgeNe[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ReportSimAgeNe'] = self.objSSParametersLocal.boolReportSimAgeNe

                return True

            def Get_Log_Current_Column_Index(self, bool_Reset, bool_Add_Suffix = False, str_Suffix = ''):
                
                if bool_Reset:
                    self.str_Current_Col_Index = str(
                                                     str(self.intLevel) +
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
                                        str(self.intLevel) +
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
        

# -------------- Class specific routines

            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.class_obj_SSBatch_V2 = obj_SSBatch_V2() 
        return self.class_obj_SSBatch_V2
 
    def __exit__(self, type, value, traceback): 
        self.class_obj_SSBatch_V2.classCleanUp()