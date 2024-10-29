#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
#from simuPOP
import simuPOP as sim
from globals_SharkSim import globalsSS
from AutoVivificationHandler import AutoVivificationHandler
from SSAnalysisHandler import SSAnalysisHandler
from AnalysisHandler import AnalysisHandler


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
import re

class object_SSVirtualSubPop_V2:
    """Contains SS Simulation level properties and methods"""
    def __enter__(self):

        class obj_SSVirtualSubPop_V2():

# -------------- Class specific routines

            __slots__ = ('stringNotApplicable'
                         ,'stringSuppressed'
                         ,'stringDelimiter'
                         ,'stringDelimiter2'
                         ,'objSSParametersLocal'
                         ,'intLevel'
                         ,'str_Current_Col_Index'
                         ,'pop'
                         ,'intSubPop'
                         ,'intVirtualSubPop'
                         ,'intNumberVirtualSubPops'
                         ,'listVirtSubPopsToOutput'
                         ,'listCurrentVSP'
                         ,'listSingleVirtualSubPop'
                         ,'floatMean'
                         ,'floatVariance'
                         ,'dictSireOffspringCount'
                         ,'dictDameOffspringCount'
                         ,'dictOffspringCount'
                        ,'floatMeanLitterSizeForMaleParents_MeanKsex'
                        ,'floatMeanVarianceLitterSizeForMaleParents_VarKsex'
                        ,'integerNumberofParentsForMaleParents_Nsex'
                        ,'floatNeDemographicByMaleParentsFromKnownOffspring'
                        ,'floatMeanLitterSizeForFemaleParents_MeanKsex'
                        ,'floatMeanVarianceLitterSizeForFemaleParents_VarKsex'
                        ,'integerNumberofParentsForFemaleParents_Nsex'
                        ,'floatNeDemographicByFemaleParentsFromKnownOffspring'
                        ,'integerNumberofParentsForBothSexesParents_Nsex'
                        ,'floatNeDemographicGivenBothSexesNeFromKnownOffspring'

                        #Reporting vars
                        ,'dict_Rep_1_DataSectionNotesLevels'
                        ,'dict_Rep_50_strUniqueRunID'
                        ,'dict_Rep_60_SimCurrentBatch'
                        ,'dict_Rep_65_SimCurrentReplicate'
                        ,'dict_Rep_68_strUniqueRun_Batch_Rep_VSP_ID'
                        ,'dict_Rep_72_Current_Year'                     
                        ,'dict_Rep_73_Current_Month'
                        ,'dict_Rep_90_SubPop_VSP_Name'                        
                        ,'dict_Rep_100_SubPop_VSP'
                        ,'dict_Rep_200_SubPopSize_VSP'
                        ,'dict_Rep_300_NeDemographic_Crow_And_Denniston_1988_DemoNe_From_Last_Mating'
                        ,'dict_Rep_305_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate' 
                        ,'dict_Rep_310_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn' 
                        ,'dict_Rep_315_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn'
                        ,'dict_Rep_400_temporal_JR_P1_ne_VSP'
                        ,'dict_Rep_500_temporal_JR_P1_ne_2_5_CI_VSP'
                        ,'dict_Rep_600_temporal_JR_P1_ne_97_5_CI_VSP'
                        ,'dict_Rep_700_temporal_JR_P2_ne_VSP'
                        ,'dict_Rep_800_temporal_JR_P2_ne_2_5_CI_VSP'
                        ,'dict_Rep_900_temporal_JR_P2_ne_97_5_CI_VSP'
                        ,'dict_Rep_1100_ld_ne_pcrit_0_VSP'
                        ,'dict_Rep_1200_ld_ne_pcrit_0_lwr_ci_VSP'
                        ,'dict_Rep_1300_ld_ne_pcrit_0_upr_ci_VSP'
                        ,'dict_Rep_1400_ld_ne_pcrit_0_05_VSP'
                        ,'dict_Rep_1500_ld_ne_pcrit_0_05_lwr_ci_VSP'
                        ,'dict_Rep_1600_ld_ne_pcrit_0_05_upr_ci_VSP'
                        ,'dict_Rep_1700_ld_ne_pcrit_0_02_VSP'
                        ,'dict_Rep_1800_ld_ne_pcrit_0_02_lwr_ci_VSP'
                        ,'dict_Rep_1900_ld_ne_pcrit_0_02_upr_ci_VSP'
                        ,'dict_Rep_2000_ld_ne_pcrit_0_01_VSP'
                        ,'dict_Rep_2100_ld_ne_pcrit_0_01_lwr_ci_VSP'
                        ,'dict_Rep_2200_ld_ne_pcrit_0_01_upr_ci_VSP'
                        ,'dict_Rep_2600_Num_Sire_Parent'
                        ,'dict_Rep_2700_Mean_Offspring_Per_Sire_Parent'
                        ,'dict_Rep_2800_Mean_Variance_Per_Sire_Parent'
                        ,'dict_Rep_2900_Num_Dame_Parent'
                        ,'dict_Rep_3000_Mean_Offspring_Per_Dame_Parent'
                        ,'dict_Rep_3100_Mean_Variance_Per_Dame_Parent'
                        ,'dict_Rep_3200_Num_Male_Potential_Parent'
                        ,'dict_Rep_3300_Mean_Offspring_Per_Male_Potential_Parent'
                        ,'dict_Rep_3400_Mean_Variance_Per_Male_Potential_Parent'
                        ,'dict_Rep_3500_Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents'
                        ,'dict_Rep_3600_Num_Female_Potential_Parent'
                        ,'dict_Rep_3700_Mean_Offspring_Per_Female_Potential_Parent'
                        ,'dict_Rep_3800_Mean_Variance_Per_Female_Potential_Parent'
                        ,'dict_Rep_3900_Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents'
                        ,'dict_Rep_4000_Num_Actual_Parent'
                        ,'dict_Rep_4100_Mean_Offspring_Per_Actual_Parent'
                        ,'dict_Rep_4200_Mean_Variance_Per_Actual_Parent'
                        ,'dict_Rep_4300_Num_Potential_Parent'
                        ,'dict_Rep_4400_Mean_Offspring_Per_Potential_Parent'
                        ,'dict_Rep_4500_Mean_Variance_Per_Potential_Parent'
                        ,'dict_Rep_4600_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne'
                        ,'dict_Rep_4700_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents'

                        #always have these last as they are variable length
#                         ,'dict_Rep_20000_Natural_Mortality_Male' 
#                         ,'dict_Rep_20100_Natural_Mortality_Female' 
#                         ,'dict_Rep_20200_Natural_SurvivorsMale'
#                         ,'dict_Rep_20300_Natural_SurvivorsFemale'
#                         ,'dict_Rep_20400_UNNatural_Mortality_Male' 
#                         ,'dict_Rep_20500_UNNatural_Mortality_Female' 
#                         ,'dict_Rep_20600_UNNatural_SurvivorsMale'
#                         ,'dict_Rep_20700_UNNatural_SurvivorsFemale'
                        ,'dict_Rep_20900_COMBINED_Mortality_Male' 
                        ,'dict_Rep_21000_COMBINED_Mortality_Female' 
                        ,'dict_Rep_21100_COMBINED_SurvivorsMale'
                        ,'dict_Rep_21200_COMBINED_SurvivorsFemale'
                        ,'dict_Rep_23000_AlleleTotalPerLocus_VSP'
                        ,'dict_Rep_24000_dictAlleleInstanceCountPerLocus_VSP'
                        ,'dict_Rep_25000_dictAlleleFreqs_VSP'

                        )

            def __init__(self):
                
                self.stringNotApplicable = globalsSS.StringUnexpectedResults.static_stringNotApplicable
                self.stringSuppressed = globalsSS.StringUnexpectedResults.static_stringSuppressed
                
                self.stringDelimiter = globalsSS.StringDelimiters.static_stringDelimiter_SEMI_COLON
                self.stringDelimiter2 = globalsSS.StringDelimiters.static_stringDelimiter_COMMA
                self.str_ID_Suf = globalsSS.StringDelimiters.static_stringDelimiter_SPACE

                self.objSSParametersLocal = None

                self.intLevel = 4
                self.str_Current_Col_Index = str(
                                                 str(self.intLevel) +
                                                 globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                                 '0' +
                                                 globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                                 '0' +
                                                 globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                                 '0')
                                                
                self.pop = None
                
                self.intSubPop = 0
                self.intVirtualSubPop = 0
                self.intNumberVirtualSubPops = 0
                self.listVirtSubPopsToOutput = []
                self.listCurrentVSP = []
                self.listSingleVirtualSubPop = []
                self.floatMean = 0
                self.floatVariance = 0
                self.dictSireOffspringCount = AutoVivificationHandler()
                self.dictDameOffspringCount = AutoVivificationHandler()
                self.dictOffspringCount = AutoVivificationHandler()

                self.floatMeanLitterSizeForMaleParents_MeanKsex = 0
                self.floatMeanVarianceLitterSizeForMaleParents_VarKsex = 0
                self.integerNumberofParentsForMaleParents_Nsex = 0
                self.floatNeDemographicByMaleParentsFromKnownOffspring = 0

                self.floatMeanLitterSizeForFemaleParents_MeanKsex = 0
                self.floatMeanVarianceLitterSizeForFemaleParents_VarKsex = 0
                self.integerNumberofParentsForFemaleParents_Nsex = 0
                self.floatNeDemographicByFemaleParentsFromKnownOffspring = 0

                self.integerNumberofParentsForBothSexesParents_Nsex = 0
                self.floatNeDemographicGivenBothSexesNeFromKnownOffspring = 0

                #Reporting variables

                self.dict_Rep_1_DataSectionNotesLevels = {}
                self.dict_Rep_50_strUniqueRunID = {}
                self.dict_Rep_60_SimCurrentBatch = {}
                self.dict_Rep_65_SimCurrentReplicate ={}
                self.dict_Rep_68_strUniqueRun_Batch_Rep_VSP_ID ={}
                
                self.dict_Rep_72_Current_Year = {}
                self.dict_Rep_73_Current_Month = {}  
                              
                self.dict_Rep_90_SubPop_VSP_Name = {}
                self.dict_Rep_100_SubPop_VSP = {}
                self.dict_Rep_200_SubPopSize_VSP = {}
                self.dict_Rep_300_NeDemographic_Crow_And_Denniston_1988_DemoNe_From_Last_Mating = {}
                self.dict_Rep_305_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate = {} 
                self.dict_Rep_310_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn = {} 
                self.dict_Rep_315_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn = {}
                self.dict_Rep_400_temporal_JR_P1_ne_VSP = {}
                self.dict_Rep_500_temporal_JR_P1_ne_2_5_CI_VSP = {}
                self.dict_Rep_600_temporal_JR_P1_ne_97_5_CI_VSP = {}
                self.dict_Rep_700_temporal_JR_P2_ne_VSP = {}
                self.dict_Rep_800_temporal_JR_P2_ne_2_5_CI_VSP = {}
                self.dict_Rep_900_temporal_JR_P2_ne_97_5_CI_VSP = {}
                self.dict_Rep_1000_ld_ne_pcrit_0_VSP = {}
                self.dict_Rep_1100_ld_ne_pcrit_0_lwr_ci_VSP = {}
                self.dict_Rep_1200_ld_ne_pcrit_0_upr_ci_VSP = {}
                self.dict_Rep_1300_ld_ne_pcrit_0_05_VSP = {}
                self.dict_Rep_1400_ld_ne_pcrit_0_05_lwr_ci_VSP = {}
                self.dict_Rep_1500_ld_ne_pcrit_0_05_upr_ci_VSP = {}
                self.dict_Rep_1600_ld_ne_pcrit_0_02_VSP = {}
                self.dict_Rep_1700_ld_ne_pcrit_0_02_lwr_ci_VSP = {}
                self.dict_Rep_1800_ld_ne_pcrit_0_02_upr_ci_VSP = {}
                self.dict_Rep_1900_ld_ne_pcrit_0_01_VSP = {}
                self.dict_Rep_2000_ld_ne_pcrit_0_01_lwr_ci_VSP = {}
                self.dict_Rep_2100_ld_ne_pcrit_0_01_upr_ci_VSP = {}
                self.dict_Rep_2500_Num_Sire_Parent  = {}
                self.dict_Rep_2600_Mean_Offspring_Per_Sire_Parent  = {}
                self.dict_Rep_2700_Mean_Variance_Per_Sire_Parent  = {}
                self.dict_Rep_2800_Num_Dame_Parent  = {}
                self.dict_Rep_2900_Mean_Offspring_Per_Dame_Parent  = {}
                self.dict_Rep_3000_Mean_Variance_Per_Dame_Parent  = {}
                self.dict_Rep_3100_Num_Male_Potential_Parent  = {}
                self.dict_Rep_3200_Mean_Offspring_Per_Male_Potential_Parent  = {}
                self.dict_Rep_3300_Mean_Variance_Per_Male_Potential_Parent  = {}
                self.dict_Rep_3400_Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents = {}
                self.dict_Rep_3500_Num_Female_Potential_Parent  = {}
                self.dict_Rep_3600_Mean_Offspring_Per_Female_Potential_Parent  = {}
                self.dict_Rep_3700_Mean_Variance_Per_Female_Potential_Parent  = {}
                self.dict_Rep_3800_Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents = {}
                self.dict_Rep_3900_Num_Actual_Parent  = {}
                self.dict_Rep_4000_Mean_Offspring_Per_Actual_Parent  = {}
                self.dict_Rep_4100_Mean_Variance_Per_Actual_Parent  = {}
                self.dict_Rep_4200_Num_Potential_Parent  = {}
                self.dict_Rep_4300_Mean_Offspring_Per_Potential_Parent  = {}
                self.dict_Rep_4400_Mean_Variance_Per_Potential_Parent  = {}
                self.dict_Rep_4500_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne  = {}
                self.dict_Rep_4600_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents   = {}

                ''' always have these last as they are variable length '''
#                 self.dict_Rep_20000_Natural_MortalityMale = {}
#                 self.dict_Rep_20100_Natural_MortalityFemale = {}
#                 self.dict_Rep_20200_Natural_SurvivorsMale = {}
#                 self.dict_Rep_20300_Natural_SurvivorsFemale = {}
#                 self.dict_Rep_20400_UNNatural_MortalityMale = {}
#                 self.dict_Rep_20500_UNNatural_MortalityFemale = {}
#                 self.dict_Rep_20600_UNNatural_SurvivorsMale = {}
#                 self.dict_Rep_20700_UNNatural_SurvivorsFemale = {}
                self.dict_Rep_20900_COMBINED_MortalityMale = {}
                self.dict_Rep_21000_COMBINED_MortalityFemale = {}
                self.dict_Rep_21100_COMBINED_SurvivorsMale = {}
                self.dict_Rep_21200_COMBINED_SurvivorsFemale = {}
                
                self.dict_Rep_22000_AlleleTotalPerLocus_VSP = {}
                self.dict_Rep_23000_dictAlleleInstanceCountPerLocus_VSP = {}
                self.dict_Rep_24000_dictAlleleFreqs_VSP = {}
                
            def method_PopulateProperties(self, boolIncludeParentOffspringProperties, str_VSP_Group):

                '''
                --------------------
                Get VSP info
                --------------------
                '''
                self.listCurrentVSP.append(self.listVirtSubPopsToOutput[0])
                self.listSingleVirtualSubPop = self.listCurrentVSP[0]
                self.intVirtualSubPop = int(re.findall( r'\,(.*?)\)', str(self.listSingleVirtualSubPop))[0])

                '''
                --------------------
                Prep values
                --------------------
                '''
                if len(self.listSingleVirtualSubPop) > 0:
                    str_Sub_Pop_Name = self.pop.subPopName(self.listSingleVirtualSubPop)
                else:
                    str_Sub_Pop_Name = 'NA'
                pass

                strUniqueRun_Batch_Rep_VSP_ID = str(
                                                    self.objSSParametersLocal.strUniqueRunID + '_' +
                                                    str(self.objSSParametersLocal.intCurrentBatch) + '_' +
                                                    str(self.objSSParametersLocal.intCurrentReplicate) + '_' +
                                                    str_Sub_Pop_Name
                                                    )
                '''
                --------------------
                Load dict
                --------------------
                '''                                       
                self.dict_Rep_1_DataSectionNotesLevels[self.Get_Log_Current_Column_Index(True, True, self.str_ID_Suf) + 'Data_Section_Note_' + str(self.intLevel)] = 'Virtual_Pop_Level_Params'

                self.dict_Rep_50_strUniqueRunID[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Unique_Run_ID'] = self.objSSParametersLocal.strUniqueRunID
                self.dict_Rep_60_SimCurrentBatch[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Sim_Current_Batch'] = self.objSSParametersLocal.intCurrentBatch
                self.dict_Rep_65_SimCurrentReplicate[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Sim_Current_Replicate'] = self.objSSParametersLocal.intCurrentReplicate

                str_Key = globalsSS.SS_LEVEL_VSP_Details.static_Label_Gen_Unique_Run_Batch_Rep_VSP_ID
                self.dict_Rep_68_strUniqueRun_Batch_Rep_VSP_ID[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + str_Key] = strUniqueRun_Batch_Rep_VSP_ID
                
                
                self.dict_Rep_72_Current_Year[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Current_Year'] = self.objSSParametersLocal.intSimulationCurrentMonth//12
                self.dict_Rep_73_Current_Month[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Current_Month'] = self.objSSParametersLocal.intYearCurrentMonth
                

                self.dict_Rep_90_SubPop_VSP_Name[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Sub_Pop_VSP_Name'] = str_Sub_Pop_Name
                self.dict_Rep_100_SubPop_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Sub_Pop_VSP'] = self.listCurrentVSP
                
                intVSPSize = self.pop.subPopSize(self.listSingleVirtualSubPop)
                self.dict_Rep_200_SubPopSize_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Sub_Pop_Size_VSP'] = intVSPSize
                
                boolVSPHasIndivs = False
                if intVSPSize > 0:
                    boolVSPHasIndivs = True
                    self.func_Populate_Properties_For_VSP(boolIncludeParentOffspringProperties, boolVSPHasIndivs, str_VSP_Group)
                else:
                    self.func_Populate_Properties_For_VSP_WO_Indivs(boolIncludeParentOffspringProperties, str_VSP_Group)
                pass
            
                return True
            
            def func_Populate_Properties_For_VSP(self, boolIncludeParentOffspringProperties, boolVSPHasIndivs, str_VSP_Group):
                
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    if self.objSSParametersLocal.boolReportDemographicNe:
                        #Demographic Ne for entire pop
                        #dictNeDemographic = objSSAnalysisOperation.method_Statistics_On_NE_Demographic_Population_Size_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                        #if len(dictNeDemographic) > 0:
                        #    value = dictNeDemographic[0] #Only take the value for the first locus as they should all be the same
                        #else:
                        #    value = self.stringNotApplicable

                        self.dict_Rep_300_NeDemographic_Crow_And_Denniston_1988_DemoNe_From_Last_Mating[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'C_&_D_1988_DemoNe_From_Last_Mating'] = self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating
                        self.dict_Rep_305_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'C_&_D_1988_DemoNe_Mean_From_Matings_Over_Replicate'] = self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate 
                        self.dict_Rep_310_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'C_&_D_1988_DemoNe_Mean_From_Matings_Over_BurnIn'] = self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn 
                        self.dict_Rep_315_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'C_&_D_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn'] = self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn
                        
                        pass
                    else:
                        #value = self.stringSuppressed

                        self.dict_Rep_300_NeDemographic_Crow_And_Denniston_1988_DemoNe_From_Last_Mating[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'C_&_D_1988_DemoNe_From_Last_Mating'] = self.stringSuppressed
                        self.dict_Rep_305_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'C_&_D_1988_DemoNe_Mean_From_Matings_Over_Replicate'] = self.stringSuppressed 
                        self.dict_Rep_310_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'C_&_D_1988_DemoNe_Mean_From_Matings_Over_BurnIn'] = self.stringSuppressed 
                        self.dict_Rep_315_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'C_&_D_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn'] = self.stringSuppressed
                    pass
                
                    #self.dict_Rep_300_NeDemographic_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'demographic_ne_loci_1_VSP'] = value


                    listNeTemporal_JR_P1 = []
                    listNeTemporal_JR_P2 = []
                    
                    if boolVSPHasIndivs:
                        
                        if self.objSSParametersLocal.boolReportTemporalFS_P1_Ne:
                            #Temporal JR P1 Ne for entire pop
                            listNeTemporal_JR_P1 = objSSAnalysisOperation.method_Statistics_On_NE_Temporal_JordeRyman_P1_Population_Size_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                        else:
                            #Output has been suppressed
                            for i in range(0, 3):
                                listNeTemporal_JR_P1.append(self.stringSuppressed)
                            pass
                        pass
                    
                        listNeTemporal_JR_P2 = []
                        if self.objSSParametersLocal.boolReportTemporalFS_P2_Ne:
                            #Temporal JR P2 Ne for entire pop
                            listNeTemporal_JR_P2 = objSSAnalysisOperation.method_Statistics_On_NE_Temporal_JordeRyman_P2_Population_Size_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                        else:
                            #Output has been suppressed
                            for i in range(0, 3):
                                listNeTemporal_JR_P2.append(self.stringSuppressed)
                            pass
                        pass
                    
                    else:
                        #Output is not applicable
                        for i in range(0, 3):
                            listNeTemporal_JR_P1.append(float('nan'))
                            listNeTemporal_JR_P2.append(float('nan'))


                    self.dict_Rep_400_temporal_JR_P1_ne_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'temporal_JR_P1_ne_VSP'] = listNeTemporal_JR_P1[0]
                    self.dict_Rep_500_temporal_JR_P1_ne_2_5_CI_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'temporal_JR_P1_ne_2.5_CI_VSP'] = listNeTemporal_JR_P1[1]
                    self.dict_Rep_600_temporal_JR_P1_ne_97_5_CI_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'temporal_JR_P1_ne_97.5_CI_VSP'] = listNeTemporal_JR_P1[2]
                                    
                    self.dict_Rep_700_temporal_JR_P2_ne_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'temporal_JR_P2_ne_VSP'] = listNeTemporal_JR_P2[0]
                    self.dict_Rep_800_temporal_JR_P2_ne_2_5_CI_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'temporal_JR_P2_ne_2.5_CI_VSP'] = listNeTemporal_JR_P2[1]
                    self.dict_Rep_900_temporal_JR_P2_ne_97_5_CI_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'temporal_JR_P2_ne_97.5_CI_VSP'] = listNeTemporal_JR_P2[2]

                    if self.objSSParametersLocal.boolReportLDNe:

                        #LD Ne - Dict for each PCrit (0.0, 0.05, 0.02, 0.01) listing NE, lower CI, upper CI    
                        dictNeLD = objSSAnalysisOperation.method_Statistics_On_NE_LD_Population_Size_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                    
                        self.dict_Rep_1000_ld_ne_pcrit_0_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0_VSP'] = round(dictNeLD[0.0][0],4)
                        self.dict_Rep_1100_ld_ne_pcrit_0_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0_lwr_ci_VSP'] = round(dictNeLD[0.0][1],4)
                        self.dict_Rep_1200_ld_ne_pcrit_0_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0_upr_ci_VSP'] = round(dictNeLD[0.0][2],4)
                        self.dict_Rep_1300_ld_ne_pcrit_0_05_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.05_VSP'] = round(dictNeLD[0.05][0],4)
                        self.dict_Rep_1400_ld_ne_pcrit_0_05_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.05_lwr_ci_VSP'] = round(dictNeLD[0.05][1],4)
                        self.dict_Rep_1500_ld_ne_pcrit_0_05_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.05_upr_ci_VSP'] = round(dictNeLD[0.05][2],4)
                        self.dict_Rep_1600_ld_ne_pcrit_0_02_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.02_VSP'] = round(dictNeLD[0.02][0],4)
                        self.dict_Rep_1700_ld_ne_pcrit_0_02_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.02_lwr_ci_VSP'] = round(dictNeLD[0.02][1],4)
                        self.dict_Rep_1800_ld_ne_pcrit_0_02_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.02_upr_ci_VSP'] = round(dictNeLD[0.02][2],4)
                        self.dict_Rep_1900_ld_ne_pcrit_0_01_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.01_VSP'] = round(dictNeLD[0.01][0],4)
                        self.dict_Rep_2000_ld_ne_pcrit_0_01_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.01_lwr_ci_VSP'] = round(dictNeLD[0.01][1],4)
                        self.dict_Rep_2100_ld_ne_pcrit_0_01_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.01_upr_ci_VSP'] = round(dictNeLD[0.01][2],4)
                    else:
                        #Output has been suppressed
                        self.dict_Rep_1000_ld_ne_pcrit_0_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0_VSP'] = self.stringSuppressed
                        self.dict_Rep_1100_ld_ne_pcrit_0_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0_lwr_ci_VSP'] = self.stringSuppressed
                        self.dict_Rep_1200_ld_ne_pcrit_0_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0_upr_ci_VSP'] = self.stringSuppressed
                        self.dict_Rep_1300_ld_ne_pcrit_0_05_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.05_VSP'] = self.stringSuppressed
                        self.dict_Rep_1400_ld_ne_pcrit_0_05_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.05_lwr_ci_VSP'] = self.stringSuppressed
                        self.dict_Rep_1500_ld_ne_pcrit_0_05_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.05_upr_ci_VSP'] = self.stringSuppressed
                        self.dict_Rep_1600_ld_ne_pcrit_0_02_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.02_VSP'] = self.stringSuppressed
                        self.dict_Rep_1700_ld_ne_pcrit_0_02_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.02_lwr_ci_VSP'] = self.stringSuppressed
                        self.dict_Rep_1800_ld_ne_pcrit_0_02_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.02_upr_ci_VSP'] = self.stringSuppressed
                        self.dict_Rep_1900_ld_ne_pcrit_0_01_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.01_VSP'] = self.stringSuppressed
                        self.dict_Rep_2000_ld_ne_pcrit_0_01_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.01_lwr_ci_VSP'] = self.stringSuppressed
                        self.dict_Rep_2100_ld_ne_pcrit_0_01_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.01_upr_ci_VSP'] = self.stringSuppressed
                    
                    if boolIncludeParentOffspringProperties:
                        #Output Mean and Variance of the cumulative number of offspring per each parent for VSP (0,0)

                        with SSAnalysisHandler() as objSSAnalysisOperation:
                        
#                             self.dictSireOffspringCount = objSSAnalysisOperation.method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(self.pop, self.intSubPop, self.intVirtualSubPop)
#                             self.dictDameOffspringCount = objSSAnalysisOperation.method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(self.pop, self.intSubPop, self.intVirtualSubPop)
                            self.dictSireOffspringCount = objSSAnalysisOperation.method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(self.pop, self.intSubPop, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)
                            self.dictDameOffspringCount = objSSAnalysisOperation.method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(self.pop, self.intSubPop, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)

                            listPotentialFemaleParents = self.objSSParametersLocal.listPotentialFemaleParents
                            listPotentialMaleParents = self.objSSParametersLocal.listPotentialMaleParents

                            #self.dictOffspringCount = objSSAnalysisOperation.method_Count_Offspring_PerParent_For_VirtualSubPop(self.pop, self.dictSireOffspringCount, self.dictDameOffspringCount, self.intSubPop, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)
                            self.dictOffspringCount = objSSAnalysisOperation.method_Count_Offspring_PerParent_For_VirtualSubPop(self.pop, self.dictSireOffspringCount, self.dictDameOffspringCount, listPotentialMaleParents, listPotentialFemaleParents, self.intSubPop, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)
                        
                            if (len(self.dictOffspringCount[sim.MALE]) > 0) | (len(self.dictOffspringCount[sim.FEMALE]) > 0):
                                with AnalysisHandler() as objAnalysisOperation:
                                    
                                    #Construct a list of ACTUAL SIRE offspring counts
                                    listSireOffspringCount = []
                                    for i in self.dictSireOffspringCount[sim.MALE]:
                                        listSireOffspringCount.append(self.dictSireOffspringCount[sim.MALE][i])
                        
                                    self.floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listSireOffspringCount)
                                    self.floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listSireOffspringCount)
                                    
                                    self.dict_Rep_2500_Num_Sire_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Num_Sire_Parent'] = len(listSireOffspringCount)
                                    self.dict_Rep_2600_Mean_Offspring_Per_Sire_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Offspring_Per_Sire_Parent'] = round(self.floatMean,4)
                                    self.dict_Rep_2700_Mean_Variance_Per_Sire_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Variance_Offspring_Per_Sire_Parent'] = round( self.floatVariance,4)
                        
                                    #Construct a list of POTENTIAL SIRE offspring counts
                                    listMaleOffspringCount = []
                                    for i in self.dictOffspringCount[sim.MALE]:
                                        listMaleOffspringCount.append(self.dictOffspringCount[sim.MALE][i])
                        
                                    self.floatMeanLitterSizeForMaleParents_MeanKsex = objAnalysisOperation.method_Get_Mean_From_A_List(listMaleOffspringCount)
                                    self.floatMeanVarianceLitterSizeForMaleParents_VarKsex = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listMaleOffspringCount)
                                    self.integerNumberofParentsForMaleParents_Nsex = len(listMaleOffspringCount)
                                    self.floatNeDemographicByMaleParentsFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_By_Parental_Sex_Given_Known_Offspring(self.integerNumberofParentsForMaleParents_Nsex, self.floatMeanLitterSizeForMaleParents_MeanKsex, self.floatMeanVarianceLitterSizeForMaleParents_VarKsex)
                                    
                        
                                    self.dict_Rep_3100_Num_Male_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Num_Male_Potential_Parent'] = self.integerNumberofParentsForMaleParents_Nsex
                                    self.dict_Rep_3200_Mean_Offspring_Per_Male_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Offspring_Per_Male_Potential_Parent'] = round(self.floatMeanLitterSizeForMaleParents_MeanKsex,4)
                                    self.dict_Rep_3300_Mean_Variance_Per_Male_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Variance_Offspring_Per_Male_Potential_Parent'] = round( self.floatMeanVarianceLitterSizeForMaleParents_VarKsex,4)
                                    self.dict_Rep_3400_Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents'] = round( self.floatNeDemographicByMaleParentsFromKnownOffspring,4)
                        
                                    #Construct a list of ACTUAL DAME offspring counts
                                    listDameOffspringCount = []
                                    for i in self.dictDameOffspringCount[sim.FEMALE]:
                                        listDameOffspringCount.append(self.dictDameOffspringCount[sim.FEMALE][i])
                        
                                    self.floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listDameOffspringCount)
                                    self.floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listDameOffspringCount)
                                    
                                    self.dict_Rep_2800_Num_Dame_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Num_Dame_Parent'] = len(listDameOffspringCount)
                                    self.dict_Rep_2900_Mean_Offspring_Per_Dame_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Offspring_Per_Dame_Parent'] = round(self.floatMean,4)
                                    self.dict_Rep_3000_Mean_Variance_Per_Dame_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Variance_Offspring_Per_Dame_Parent'] = round( self.floatVariance,4)
                        
                                    #Construct a list of POTENTIAL DAME offspring counts
                                    listFemaleOffspringCount = []
                                    for i in self.dictOffspringCount[sim.FEMALE]:
                                        listFemaleOffspringCount.append(self.dictOffspringCount[sim.FEMALE][i])
                                    
                                    self.floatMeanLitterSizeForFemaleParents_MeanKsex = objAnalysisOperation.method_Get_Mean_From_A_List(listFemaleOffspringCount)
                                    self.floatMeanVarianceLitterSizeForFemaleParents_VarKsex = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listFemaleOffspringCount)
                                    self.integerNumberofParentsForFemaleParents_Nsex = len(listFemaleOffspringCount)
                                    self.floatNeDemographicByFemaleParentsFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_By_Parental_Sex_Given_Known_Offspring(self.integerNumberofParentsForFemaleParents_Nsex, self.floatMeanLitterSizeForFemaleParents_MeanKsex, self.floatMeanVarianceLitterSizeForFemaleParents_VarKsex)
                                    
                        
                                    self.dict_Rep_3500_Num_Female_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Num_Female_Potential_Parent'] = self.integerNumberofParentsForFemaleParents_Nsex
                                    self.dict_Rep_3600_Mean_Offspring_Per_Female_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Offspring_Per_Female_Potential_Parent'] = round(self.floatMeanLitterSizeForFemaleParents_MeanKsex,4)
                                    self.dict_Rep_3700_Mean_Variance_Per_Female_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Variance_Offspring_Per_Female_Potential_Parent'] = round(self.floatMeanVarianceLitterSizeForFemaleParents_VarKsex,4)
                                    self.dict_Rep_3800_Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents'] = round(self.floatNeDemographicByFemaleParentsFromKnownOffspring,4)
                        
                                    listActualParentCount = []
                                    listActualParentCount = listSireOffspringCount + listDameOffspringCount
                        
                                    self.floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listActualParentCount)
                                    self.floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listActualParentCount)
                        
                                    self.dict_Rep_3900_Num_Actual_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Num_Actual_Parent'] = len(listActualParentCount)
                                    self.dict_Rep_4000_Mean_Offspring_Per_Actual_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Offspring_Per_Actual_Parent'] = round(self.floatMean,4)
                                    self.dict_Rep_4100_Mean_Variance_Per_Actual_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Variance_Offspring_Per_Actual_Parent'] = round( self.floatVariance,4)
                        
                        
                                    listBothSexesOffspringCount = []
                                    for intCount in listMaleOffspringCount:
                                        listBothSexesOffspringCount.append(intCount)
                                    for intCount in listFemaleOffspringCount:
                                        listBothSexesOffspringCount.append(intCount)
                        
                                    self.floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listBothSexesOffspringCount)
                                    self.floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listBothSexesOffspringCount)
                                    self.integerNumberofParentsForBothSexesParents_Nsex = len(listBothSexesOffspringCount)
                                    self.floatNeDemographicGivenBothSexesNeFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_From_Known_Offspring_Given_Parental_Sex_Ne(self.floatNeDemographicByMaleParentsFromKnownOffspring, self.floatNeDemographicByFemaleParentsFromKnownOffspring)
                        
                                    self.dict_Rep_4200_Num_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Num_Potential_Parent'] = self.integerNumberofParentsForBothSexesParents_Nsex
                                    self.dict_Rep_4300_Mean_Offspring_Per_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Offspring_Per_Potential_Parent'] = round(self.floatMean,4)
                                    self.dict_Rep_4400_Mean_Variance_Per_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Variance_Offspring_Per_Potential_Parent'] = round( self.floatVariance,4)
                                    self.dict_Rep_4500_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne'] = round( self.floatNeDemographicGivenBothSexesNeFromKnownOffspring,4)
                                    self.dict_Rep_4600_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents'] = round((self.floatNeDemographicGivenBothSexesNeFromKnownOffspring / self.integerNumberofParentsForBothSexesParents_Nsex),4)
                        
                                pass
                            pass
                        pass
                    
                    pass

                    ''' always have these last as they are variable length '''

                    str_Sex_Male = globalsSS.SexConstants.static_stringSexMale
                    str_Sex_Female = globalsSS.SexConstants.static_stringSexFemale
                    intVSP = int(self.listSingleVirtualSubPop[1])                    
                    if str_VSP_Group == globalsSS.VSP_Groups.static_VSP_Group_Age_Class:       
                    
#                         ''' NATURAL Mortality Stats '''      
#                         if self.objSSParametersLocal.boolAllowNATURALMortality:
#                             
#                             str_Sex = str_Sex_Male 
#                             if intVSP in self.objSSParametersLocal.odictKilled_NATURAL_Per_Age_Class_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20000_Natural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Mortality_Male'] = self.objSSParametersLocal.odictKilled_NATURAL_Per_Age_Class_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20000_Natural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Mortality_Male'] = 0
#                             pass
#                             
#                             str_Sex = str_Sex_Female
#                             if intVSP in self.objSSParametersLocal.odictKilled_NATURAL_Per_Age_Class_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20100_Natural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Mortality_Female'] = self.objSSParametersLocal.odictKilled_NATURAL_Per_Age_Class_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20100_Natural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Mortality_Female'] = 0
#                             pass
#                         
#                             str_Sex = str_Sex_Male 
#                             if intVSP in self.objSSParametersLocal.odictKilled_NATURAL_Per_Age_Class_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20200_Natural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Male'] = self.objSSParametersLocal.odictSurvived_NATURAL_Per_Age_Class_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20200_Natural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Male'] = 0
#                             pass
#                         
#                             str_Sex = str_Sex_Female 
#                             if intVSP in self.objSSParametersLocal.odictKilled_NATURAL_Per_Age_Class_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20300_Natural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Female'] = self.objSSParametersLocal.odictSurvived_NATURAL_Per_Age_Class_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20300_Natural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Female'] = 0
#                             pass
#                         else:
#                             self.dict_Rep_20000_Natural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Mortality_Male'] = 0
#                             self.dict_Rep_20100_Natural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Mortality_Female'] = 0
#                             self.dict_Rep_20200_Natural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Male'] = 0
#                             self.dict_Rep_20300_Natural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Female'] = 0
#                             
#                         pass
#                     
#                         ''' UNNATURAL Mortality Stats '''      
#                         if self.objSSParametersLocal.boolAllowUnNATURALMortality:
#                             
#                             str_Sex = str_Sex_Male 
#                             if intVSP in self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Age_Class_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20400_UNNatural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Mortality_Male'] = self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Age_Class_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20400_UNNatural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Mortality_Male'] = 0
#                             pass
#                             
#                             str_Sex = str_Sex_Female
#                             if intVSP in self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Age_Class_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20500_UNNatural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Mortality_Female'] = self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Age_Class_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20500_UNNatural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Mortality_Female'] = 0
#                             pass
#                         
#                             str_Sex = str_Sex_Male 
#                             if intVSP in self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Age_Class_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20600_UNNatural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Survivors_Male'] = self.objSSParametersLocal.odictSurvived_UnNATURAL_Per_Age_Class_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20600_UNNatural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Survivors_Male'] = 0
#                             pass
#                         
#                             str_Sex = str_Sex_Female 
#                             if intVSP in self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Age_Class_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20700_UNNatural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Survivors_Female'] = self.objSSParametersLocal.odictSurvived_UnNATURAL_Per_Age_Class_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20700_UNNatural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Survivors_Female'] = 0
#                             pass
#                         else:
#                             self.dict_Rep_20400_UNNatural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Mortality_Male'] = 0
#                             self.dict_Rep_20500_UNNatural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Mortality_Female'] = 0
#                             self.dict_Rep_20600_UNNatural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Survivors_Male'] = 0
#                             self.dict_Rep_20700_UNNatural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Survivors_Female'] = 0
#                         pass


                        ''' COMBINED Mortality Stats '''
                        boolAllowCOMBINEDMortality = True      
                        if boolAllowCOMBINEDMortality:
                            
                            str_Sex = str_Sex_Male 
                            if intVSP in self.objSSParametersLocal.odictKilled_COMBINED_Per_Age_Class_By_Sex[str_Sex].keys():
                                self.dict_Rep_20900_COMBINED_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Mortality_Male'] = self.objSSParametersLocal.odictKilled_COMBINED_Per_Age_Class_By_Sex[str_Sex][intVSP]
                            else:
                                self.dict_Rep_20900_COMBINED_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Mortality_Male'] = 0
                            pass
                            
                            str_Sex = str_Sex_Female
                            if intVSP in self.objSSParametersLocal.odictKilled_COMBINED_Per_Age_Class_By_Sex[str_Sex].keys():
                                self.dict_Rep_21000_COMBINED_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Mortality_Female'] = self.objSSParametersLocal.odictKilled_COMBINED_Per_Age_Class_By_Sex[str_Sex][intVSP]
                            else:
                                self.dict_Rep_21000_COMBINED_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Mortality_Female'] = 0
                            pass
                        
                            str_Sex = str_Sex_Male 
                            if intVSP in self.objSSParametersLocal.odictKilled_COMBINED_Per_Age_Class_By_Sex[str_Sex].keys():
                                self.dict_Rep_21100_COMBINED_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Survivors_Male'] = self.objSSParametersLocal.odictSurvived_COMBINED_Per_Age_Class_By_Sex[str_Sex][intVSP]
                            else:
                                self.dict_Rep_21100_COMBINED_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Survivors_Male'] = 0
                            pass
                        
                            str_Sex = str_Sex_Female 
                            if intVSP in self.objSSParametersLocal.odictKilled_COMBINED_Per_Age_Class_By_Sex[str_Sex].keys():
                                self.dict_Rep_21200_COMBINED_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Survivors_Female'] = self.objSSParametersLocal.odictSurvived_COMBINED_Per_Age_Class_By_Sex[str_Sex][intVSP]
                            else:
                                self.dict_Rep_21200_COMBINED_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Survivors_Female'] = 0
                            pass
                        else:
                            self.dict_Rep_20900_COMBINED_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Mortality_Male'] = 0
                            self.dict_Rep_21000_COMBINED_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Mortality_Female'] = 0
                            self.dict_Rep_21100_COMBINED_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Survivors_Male'] = 0
                            self.dict_Rep_21200_COMBINED_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Survivors_Female'] = 0
                            
                        pass
                    elif str_VSP_Group == globalsSS.VSP_Groups.static_VSP_Group_Life_Stage:

#                         ''' NATURAL Mortality Stats '''      
#                         if self.objSSParametersLocal.boolAllowNATURALMortality:
#                             
#                             str_Sex = str_Sex_Male 
#                             if intVSP in self.objSSParametersLocal.odictKilled_NATURAL_Per_Life_Stage_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20000_Natural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Mortality_Male'] = self.objSSParametersLocal.odictKilled_NATURAL_Per_Life_Stage_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20000_Natural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Mortality_Male'] = 0
#                             pass
#                             
#                             str_Sex = str_Sex_Female
#                             if intVSP in self.objSSParametersLocal.odictKilled_NATURAL_Per_Life_Stage_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20100_Natural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Mortality_Female'] = self.objSSParametersLocal.odictKilled_NATURAL_Per_Life_Stage_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20100_Natural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Mortality_Female'] = 0
#                             pass
#                         
#                             str_Sex = str_Sex_Male 
#                             if intVSP in self.objSSParametersLocal.odictKilled_NATURAL_Per_Life_Stage_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20200_Natural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Male'] = self.objSSParametersLocal.odictSurvived_NATURAL_Per_Life_Stage_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20200_Natural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Male'] = 0
#                             pass
#                         
#                             str_Sex = str_Sex_Female 
#                             if intVSP in self.objSSParametersLocal.odictKilled_NATURAL_Per_Life_Stage_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20300_Natural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Female'] = self.objSSParametersLocal.odictSurvived_NATURAL_Per_Life_Stage_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20300_Natural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Female'] = 0
#                             pass
#                         else:
#                             self.dict_Rep_20000_Natural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Mortality_Male'] = 0
#                             self.dict_Rep_20100_Natural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Mortality_Female'] = 0
#                             self.dict_Rep_20200_Natural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Male'] = 0
#                             self.dict_Rep_20300_Natural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Female'] = 0
#                             
#                         pass
#                     
#                         ''' UNNATURAL Mortality Stats '''      
#                         if self.objSSParametersLocal.boolAllowUnNATURALMortality:
#                             
#                             str_Sex = str_Sex_Male 
#                             if intVSP in self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Life_Stage_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20400_UNNatural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Mortality_Male'] = self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Life_Stage_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20400_UNNatural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Mortality_Male'] = 0
#                             pass
#                             
#                             str_Sex = str_Sex_Female
#                             if intVSP in self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Life_Stage_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20500_UNNatural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Mortality_Female'] = self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Life_Stage_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20500_UNNatural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Mortality_Female'] = 0
#                             pass
#                         
#                             str_Sex = str_Sex_Male 
#                             if intVSP in self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Life_Stage_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20600_UNNatural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Survivors_Male'] = self.objSSParametersLocal.odictSurvived_UnNATURAL_Per_Life_Stage_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20600_UNNatural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Survivors_Male'] = 0
#                             pass
#                         
#                             str_Sex = str_Sex_Female 
#                             if intVSP in self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Life_Stage_By_Sex[str_Sex].keys():
#                                 self.dict_Rep_20700_UNNatural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Survivors_Female'] = self.objSSParametersLocal.odictSurvived_UnNATURAL_Per_Life_Stage_By_Sex[str_Sex][intVSP]
#                             else:
#                                 self.dict_Rep_20700_UNNatural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Survivors_Female'] = 0
#                             pass
#                         else:
#                             self.dict_Rep_20400_UNNatural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Mortality_Male'] = 0
#                             self.dict_Rep_20500_UNNatural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Mortality_Female'] = 0
#                             self.dict_Rep_20600_UNNatural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Survivors_Male'] = 0
#                             self.dict_Rep_20700_UNNatural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UnNatural_Survivors_Female'] = 0
#                         pass                    

                        ''' COMBINED Mortality Stats '''
                        boolAllowCOMBINEDMortality = True       
                        if boolAllowCOMBINEDMortality:
                            
                            str_Sex = str_Sex_Male 
                            if intVSP in self.objSSParametersLocal.odictKilled_COMBINED_Per_Life_Stage_By_Sex[str_Sex].keys():
                                self.dict_Rep_20900_COMBINED_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Mortality_Male'] = self.objSSParametersLocal.odictKilled_COMBINED_Per_Life_Stage_By_Sex[str_Sex][intVSP]
                            else:
                                self.dict_Rep_20900_COMBINED_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Mortality_Male'] = 0
                            pass
                            
                            str_Sex = str_Sex_Female
                            if intVSP in self.objSSParametersLocal.odictKilled_COMBINED_Per_Life_Stage_By_Sex[str_Sex].keys():
                                self.dict_Rep_21000_COMBINED_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Mortality_Female'] = self.objSSParametersLocal.odictKilled_COMBINED_Per_Life_Stage_By_Sex[str_Sex][intVSP]
                            else:
                                self.dict_Rep_21000_COMBINED_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Mortality_Female'] = 0
                            pass
                        
                            str_Sex = str_Sex_Male 
                            if intVSP in self.objSSParametersLocal.odictKilled_COMBINED_Per_Life_Stage_By_Sex[str_Sex].keys():
                                self.dict_Rep_21100_COMBINED_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Survivors_Male'] = self.objSSParametersLocal.odictSurvived_COMBINED_Per_Life_Stage_By_Sex[str_Sex][intVSP]
                            else:
                                self.dict_Rep_21100_COMBINED_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Survivors_Male'] = 0
                            pass
                        
                            str_Sex = str_Sex_Female 
                            if intVSP in self.objSSParametersLocal.odictKilled_COMBINED_Per_Life_Stage_By_Sex[str_Sex].keys():
                                self.dict_Rep_21200_COMBINED_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Survivors_Female'] = self.objSSParametersLocal.odictSurvived_COMBINED_Per_Life_Stage_By_Sex[str_Sex][intVSP]
                            else:
                                self.dict_Rep_21200_COMBINED_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Survivors_Female'] = 0
                            pass
                        else:
                            self.dict_Rep_20900_COMBINED_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Mortality_Male'] = 0
                            self.dict_Rep_21000_COMBINED_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Mortality_Female'] = 0
                            self.dict_Rep_21100_COMBINED_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Survivors_Male'] = 0
                            self.dict_Rep_21200_COMBINED_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Survivors_Female'] = 0
                            
                    pass  
                      
# 
#                     ''' UNNATURAL Mortality Stats '''      
#                     intIndivsKilled = 0
#                     str_Sex = globalsSS.SexConstants.static_stringSexMale
#                     if self.objSSParametersLocal.boolAllowUnNATURALMortality:
#                         for key, value in self.objSSParametersLocal.odictPostUNNATURALMortalityNumIndividualsKilledPerAgeClass[str_Sex].items():
#                             intIndivsKilled += value
#                         pass   
#                     pass
#                     self.dict_Rep_20400_UNNatural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UNNatural_Mortality_Male'] = intIndivsKilled
#                     
#                     intIndivsKilled = 0
#                     str_Sex = globalsSS.SexConstants.static_stringSexFemale
#                     if self.objSSParametersLocal.boolAllowUnNATURALMortality:
#                         for key, value in self.objSSParametersLocal.odictPostUNNATURALMortalityNumIndividualsKilledPerAgeClass[str_Sex].items():
#                             intIndivsKilled += value
#                         pass
#                     pass
#                     self.dict_Rep_20500_UNNatural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UNNatural_Mortality_Female'] = intIndivsKilled
#                     
#                     intIndivsSurvived = 0
#                     str_Sex = globalsSS.SexConstants.static_stringSexMale
#                     if self.objSSParametersLocal.boolAllowUnNATURALMortality:
#                         for key, value in self.objSSParametersLocal.odictPostUNNATURALMortalityNumIndividualsSurvivingPerAgeClass[str_Sex].items():
#                             intIndivsSurvived += value
#                         pass
#                     pass
#                     self.dict_Rep_20600_UNNatural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Male'] = intIndivsSurvived
#                                             
#                     intIndivsSurvived = 0
#                     str_Sex = globalsSS.SexConstants.static_stringSexFemale
#                     if self.objSSParametersLocal.boolAllowUnNATURALMortality:
#                         for key, value in self.objSSParametersLocal.odictPostUNNATURALMortalityNumIndividualsSurvivingPerAgeClass[str_Sex].items():
#                             intIndivsSurvived += value
#                         pass   
#                     pass
#                     self.dict_Rep_20700_UNNatural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Female'] = intIndivsSurvived

                    ''' allele frequencies '''
                    #Construct dict of Allele totals per locus
                    dictAlleleTotalPerLocus = objSSAnalysisOperation.method_Statistics_On_Allele_TotalPerLocus_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                    #Write dict of Allele Totals Per Locus
                    self.dict_Rep_22000_AlleleTotalPerLocus_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Loci_Allele_Totals_Per_Locus_List_VSP'] = dictAlleleTotalPerLocus

                    #Construct dict of Allele instance count per locus
                    dictAlleleInstanceCountPerLocus = objSSAnalysisOperation.method_Statistics_On_Allele_InstanceCountPerLocus_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                    #Write dict of Allele Instance Counts
                    self.dict_Rep_23000_dictAlleleInstanceCountPerLocus_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Loci_Allele_Instance_Count_List_VSP'] = dictAlleleInstanceCountPerLocus

                    #Get Allele frequencies in list per population per loci per allele
                    #[Locus#]{Allele#1:Allele#1_Freq,Allele#2:Allele#2_Freq,...Allele#n:Allele#n_Freq}
                    dictAlleleFreqs = objSSAnalysisOperation.method_Statistics_On_Allele_Frequencies_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                    #Write dict of Allele Frequenecies
                    self.dict_Rep_24000_dictAlleleFreqs_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Loci_Allele_Frequencies_List_VSP'] = dictAlleleFreqs

                return True

            def func_Populate_Properties_For_VSP_WO_Indivs(self, boolIncludeParentOffspringProperties, str_VSP_Group):
                
                #self.dict_Rep_300_NeDemographic_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'demographic_ne_loci_1_VSP'] = float('nan')

                self.dict_Rep_300_NeDemographic_Crow_And_Denniston_1988_DemoNe_From_Last_Mating[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'C_&_D_1988_DemoNe_From_Last_Mating'] = float('nan')
                self.dict_Rep_305_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'C_&_D_1988_DemoNe_Mean_From_Matings_Over_Replicate'] = float('nan')
                self.dict_Rep_310_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'C_&_D_1988_DemoNe_Mean_From_Matings_Over_BurnIn'] = float('nan')
                self.dict_Rep_315_NeDemographic_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'C_&_D_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn'] = float('nan')

                listNeTemporal_JR_P1 = []
                listNeTemporal_JR_P2 = []
                
                #Output is not applicable
                for i in range(0, 3):
                    listNeTemporal_JR_P1.append(float('nan'))
                    listNeTemporal_JR_P2.append(float('nan'))
                pass
            
                self.dict_Rep_400_temporal_JR_P1_ne_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'temporal_JR_P1_ne_VSP'] = listNeTemporal_JR_P1[0]
                self.dict_Rep_500_temporal_JR_P1_ne_2_5_CI_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'temporal_JR_P1_ne_2.5_CI_VSP'] = listNeTemporal_JR_P1[1]
                self.dict_Rep_600_temporal_JR_P1_ne_97_5_CI_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'temporal_JR_P1_ne_97.5_CI_VSP'] = listNeTemporal_JR_P1[2]
                                
                self.dict_Rep_700_temporal_JR_P2_ne_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'temporal_JR_P2_ne_VSP'] = listNeTemporal_JR_P2[0]
                self.dict_Rep_800_temporal_JR_P2_ne_2_5_CI_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'temporal_JR_P2_ne_2.5_CI_VSP'] = listNeTemporal_JR_P2[1]
                self.dict_Rep_900_temporal_JR_P2_ne_97_5_CI_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'temporal_JR_P2_ne_97.5_CI_VSP'] = listNeTemporal_JR_P2[2]

                if self.objSSParametersLocal.boolReportLDNe:

                    #LD Ne - Dict for each PCrit (0.0, 0.05, 0.02, 0.01) listing NE, lower CI, upper CI    
                    self.dict_Rep_1000_ld_ne_pcrit_0_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0_VSP'] = float('nan')
                    self.dict_Rep_1100_ld_ne_pcrit_0_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0_lwr_ci_VSP'] = float('nan')
                    self.dict_Rep_1200_ld_ne_pcrit_0_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0_upr_ci_VSP'] = float('nan')
                    self.dict_Rep_1300_ld_ne_pcrit_0_05_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.05_VSP'] = float('nan')
                    self.dict_Rep_1400_ld_ne_pcrit_0_05_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.05_lwr_ci_VSP'] = float('nan')
                    self.dict_Rep_1500_ld_ne_pcrit_0_05_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.05_upr_ci_VSP'] = float('nan')
                    self.dict_Rep_1600_ld_ne_pcrit_0_02_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.02_VSP'] = float('nan')
                    self.dict_Rep_1700_ld_ne_pcrit_0_02_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.02_lwr_ci_VSP'] = float('nan')
                    self.dict_Rep_1800_ld_ne_pcrit_0_02_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.02_upr_ci_VSP'] = float('nan')
                    self.dict_Rep_1900_ld_ne_pcrit_0_01_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.01_VSP'] = float('nan')
                    self.dict_Rep_2000_ld_ne_pcrit_0_01_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.01_lwr_ci_VSP'] = float('nan')
                    self.dict_Rep_2100_ld_ne_pcrit_0_01_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.01_upr_ci_VSP'] = float('nan')
                else:
                    #Output has been suppressed
                    self.dict_Rep_1000_ld_ne_pcrit_0_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0_VSP'] = self.stringSuppressed
                    self.dict_Rep_1100_ld_ne_pcrit_0_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0_lwr_ci_VSP'] = self.stringSuppressed
                    self.dict_Rep_1200_ld_ne_pcrit_0_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0_upr_ci_VSP'] = self.stringSuppressed
                    self.dict_Rep_1300_ld_ne_pcrit_0_05_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.05_VSP'] = self.stringSuppressed
                    self.dict_Rep_1400_ld_ne_pcrit_0_05_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.05_lwr_ci_VSP'] = self.stringSuppressed
                    self.dict_Rep_1500_ld_ne_pcrit_0_05_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.05_upr_ci_VSP'] = self.stringSuppressed
                    self.dict_Rep_1600_ld_ne_pcrit_0_02_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.02_VSP'] = self.stringSuppressed
                    self.dict_Rep_1700_ld_ne_pcrit_0_02_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.02_lwr_ci_VSP'] = self.stringSuppressed
                    self.dict_Rep_1800_ld_ne_pcrit_0_02_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.02_upr_ci_VSP'] = self.stringSuppressed
                    self.dict_Rep_1900_ld_ne_pcrit_0_01_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.01_VSP'] = self.stringSuppressed
                    self.dict_Rep_2000_ld_ne_pcrit_0_01_lwr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.01_lwr_ci_VSP'] = self.stringSuppressed
                    self.dict_Rep_2100_ld_ne_pcrit_0_01_upr_ci_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'ld_ne_pcrit_0.01_upr_ci_VSP'] = self.stringSuppressed
                pass
            
                if boolIncludeParentOffspringProperties:
                                    
                    self.dict_Rep_2500_Num_Sire_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Num_Sire_Parent'] = float('nan')
                    self.dict_Rep_2600_Mean_Offspring_Per_Sire_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Offspring_Per_Sire_Parent'] = float('nan')
                    self.dict_Rep_2700_Mean_Variance_Per_Sire_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Variance_Offspring_Per_Sire_Parent'] = float('nan')

                    self.dict_Rep_3100_Num_Male_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Num_Male_Potential_Parent'] = float('nan')
                    self.dict_Rep_3200_Mean_Offspring_Per_Male_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Offspring_Per_Male_Potential_Parent'] = float('nan')
                    self.dict_Rep_3300_Mean_Variance_Per_Male_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Variance_Offspring_Per_Male_Potential_Parent'] = float('nan')
                    self.dict_Rep_3400_Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents'] = float('nan')

                    self.dict_Rep_2800_Num_Dame_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Num_Dame_Parent'] = float('nan')
                    self.dict_Rep_2900_Mean_Offspring_Per_Dame_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Offspring_Per_Dame_Parent'] = float('nan')
                    self.dict_Rep_3000_Mean_Variance_Per_Dame_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Variance_Offspring_Per_Dame_Parent'] = float('nan')

                    self.dict_Rep_3500_Num_Female_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Num_Female_Potential_Parent'] = float('nan')
                    self.dict_Rep_3600_Mean_Offspring_Per_Female_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Offspring_Per_Female_Potential_Parent'] = float('nan')
                    self.dict_Rep_3700_Mean_Variance_Per_Female_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Variance_Offspring_Per_Female_Potential_Parent'] = float('nan')
                    self.dict_Rep_3800_Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents'] = float('nan')

                    self.dict_Rep_3900_Num_Actual_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Num_Actual_Parent'] = float('nan')
                    self.dict_Rep_4000_Mean_Offspring_Per_Actual_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Offspring_Per_Actual_Parent'] = float('nan')
                    self.dict_Rep_4100_Mean_Variance_Per_Actual_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Variance_Offspring_Per_Actual_Parent'] = float('nan')

                    self.dict_Rep_4200_Num_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Num_Potential_Parent'] = float('nan')
                    self.dict_Rep_4300_Mean_Offspring_Per_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Offspring_Per_Potential_Parent'] = float('nan')
                    self.dict_Rep_4400_Mean_Variance_Per_Potential_Parent[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Mean_Variance_Offspring_Per_Potential_Parent'] = float('nan')
                    self.dict_Rep_4500_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne'] = float('nan')
                    self.dict_Rep_4600_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents'] = float('nan')
                pass

                ''' always have these last as they are variable length '''
#                 self.dict_Rep_20000_Natural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Mortality_Male'] = float('nan')
#                 self.dict_Rep_20100_Natural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Mortality_Female'] = float('nan')
#                 self.dict_Rep_20200_Natural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Male'] = float('nan')
#                 self.dict_Rep_20300_Natural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Natural_Survivors_Female'] = float('nan')
#                 self.dict_Rep_20400_UNNatural_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UNNatural_Mortality_Male'] = float('nan')
#                 self.dict_Rep_20500_UNNatural_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UNNatural_Mortality_Female'] = float('nan')
#                 self.dict_Rep_20600_UNNatural_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UNNatural_Survivors_Male'] = float('nan')
#                 self.dict_Rep_20700_UNNatural_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'UNNatural_Survivors_Female'] = float('nan')
                self.dict_Rep_20900_COMBINED_MortalityMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Mortality_Male'] = float('nan')
                self.dict_Rep_21000_COMBINED_MortalityFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Mortality_Female'] = float('nan')
                self.dict_Rep_21100_COMBINED_SurvivorsMale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Survivors_Male'] = float('nan')
                self.dict_Rep_21200_COMBINED_SurvivorsFemale[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'COMBINED_Survivors_Female'] = float('nan')
                
                self.dict_Rep_22000_AlleleTotalPerLocus_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Loci_Allele_Totals_Per_Locus_List_VSP'] = float('nan')
                self.dict_Rep_23000_dictAlleleInstanceCountPerLocus_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Loci_Allele_Instance_Count_List_VSP'] = float('nan')
                self.dict_Rep_24000_dictAlleleFreqs_VSP[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Loci_Allele_Frequencies_List_VSP'] = float('nan')
            
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

        self.class_obj_SSVirtualSubPop_V2 = obj_SSVirtualSubPop_V2() 
        return self.class_obj_SSVirtualSubPop_V2
 
    def __exit__(self, type, value, traceback): 
        self.class_obj_SSVirtualSubPop_V2.classCleanUp()