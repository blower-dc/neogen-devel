#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
#from simuPOP
import simuPOP as sim
from AutoVivificationHandler import AutoVivificationHandler
from SSAnalysisHandler import SSAnalysisHandler
from AnalysisHandler import AnalysisHandler


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
import re

class object_SSVirtualSubPop:
    """Contains SS Simulation level properties and methods"""
    def __enter__(self):

        class obj_SSVirtualSubPop():

# -------------- Class specific routines

            __slots__ = ('stringNotApplicable'
                         ,'stringSuppressed'
                         ,'stringDelimiter'
                         ,'stringDelimiter2'
                         ,'objSSParametersLocal'
                         ,'intLevel'
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

                        ,'dictDataSectionNotesLevels'
                        ,'dict_SubPop_VSP'
                        ,'dict_SubPopSize_VSP'
                        ,'dict_NeDemographic_VSP'
                        ,'dict_temporal_JR_P1_ne_VSP'
                        ,'dict_temporal_JR_P1_ne_2_5_CI_VSP'
                        ,'dict_temporal_JR_P1_ne_97_5_CI_VSP'
                        ,'dict_temporal_JR_P2_ne_VSP'
                        ,'dict_temporal_JR_P2_ne_2_5_CI_VSP'
                        ,'dict_temporal_JR_P2_ne_97_5_CI_VSP'
                        ,'dict_ld_ne_pcrit_0_VSP'
                        ,'dict_ld_ne_pcrit_0_lwr_ci_VSP'
                        ,'dict_ld_ne_pcrit_0_upr_ci_VSP'
                        ,'dict_ld_ne_pcrit_0_05_VSP'
                        ,'dict_ld_ne_pcrit_0_05_lwr_ci_VSP'
                        ,'dict_ld_ne_pcrit_0_05_upr_ci_VSP'
                        ,'dict_ld_ne_pcrit_0_02_VSP'
                        ,'dict_ld_ne_pcrit_0_02_lwr_ci_VSP'
                        ,'dict_ld_ne_pcrit_0_02_upr_ci_VSP'
                        ,'dict_ld_ne_pcrit_0_01_VSP'
                        ,'dict_ld_ne_pcrit_0_01_lwr_ci_VSP'
                        ,'dict_ld_ne_pcrit_0_01_upr_ci_VSP'
                        ,'dict_AlleleTotalPerLocus_VSP'
                        ,'dict_dictAlleleInstanceCountPerLocus_VSP'
                        ,'dict_dictAlleleFreqs_VSP'
                        ,'dict_Num_Sire_Parent'
                        ,'dict_Mean_Offspring_Per_Sire_Parent'
                        ,'dict_Mean_Variance_Per_Sire_Parent'
                        ,'dict_Num_Dame_Parent'
                        ,'dict_Mean_Offspring_Per_Dame_Parent'
                        ,'dict_Mean_Variance_Per_Dame_Parent'
                        ,'dict_Num_Male_Potential_Parent'
                        ,'dict_Mean_Offspring_Per_Male_Potential_Parent'
                        ,'dict_Mean_Variance_Per_Male_Potential_Parent'
                        ,'dict_Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents'
                        ,'dict_Num_Female_Potential_Parent'
                        ,'dict_Mean_Offspring_Per_Female_Potential_Parent'
                        ,'dict_Mean_Variance_Per_Female_Potential_Parent'
                        ,'dict_Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents'
                        ,'dict_Num_Actual_Parent'
                        ,'dict_Mean_Offspring_Per_Actual_Parent'
                        ,'dict_Mean_Variance_Per_Actual_Parent'
                        ,'dict_Num_Potential_Parent'
                        ,'dict_Mean_Offspring_Per_Potential_Parent'
                        ,'dict_Mean_Variance_Per_Potential_Parent'
                        ,'dict_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne'
                        ,'dict_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents'
                        )

            def __init__(self):
                
                self.stringNotApplicable = 'NA'
                self.stringSuppressed = 'SUP'
                
                self.stringDelimiter = ';'
                self.stringDelimiter2 = ','

                self.objSSParametersLocal = None

                self.intLevel = 4
                
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

                self.dictDataSectionNotesLevels = AutoVivificationHandler()
                                 
                self.dict_SubPop_VSP = AutoVivificationHandler()
                    
                self.dict_SubPopSize_VSP = AutoVivificationHandler()
                
                self.dict_NeDemographic_VSP = AutoVivificationHandler()

                self.dict_temporal_JR_P1_ne_VSP = AutoVivificationHandler()

                self.dict_temporal_JR_P1_ne_2_5_CI_VSP = AutoVivificationHandler()

                self.dict_temporal_JR_P1_ne_97_5_CI_VSP = AutoVivificationHandler()

                self.dict_temporal_JR_P2_ne_VSP = AutoVivificationHandler()

                self.dict_temporal_JR_P2_ne_2_5_CI_VSP = AutoVivificationHandler()

                self.dict_temporal_JR_P2_ne_97_5_CI_VSP = AutoVivificationHandler()

                self.dict_ld_ne_pcrit_0_VSP = AutoVivificationHandler()

                self.dict_ld_ne_pcrit_0_lwr_ci_VSP = AutoVivificationHandler()

                self.dict_ld_ne_pcrit_0_upr_ci_VSP = AutoVivificationHandler()

                self.dict_ld_ne_pcrit_0_05_VSP = AutoVivificationHandler()

                self.dict_ld_ne_pcrit_0_05_lwr_ci_VSP = AutoVivificationHandler()

                self.dict_ld_ne_pcrit_0_05_upr_ci_VSP = AutoVivificationHandler()

                self.dict_ld_ne_pcrit_0_02_VSP = AutoVivificationHandler()

                self.dict_ld_ne_pcrit_0_02_lwr_ci_VSP = AutoVivificationHandler()

                self.dict_ld_ne_pcrit_0_02_upr_ci_VSP = AutoVivificationHandler()

                self.dict_ld_ne_pcrit_0_01_VSP = AutoVivificationHandler()

                self.dict_ld_ne_pcrit_0_01_lwr_ci_VSP = AutoVivificationHandler()

                self.dict_ld_ne_pcrit_0_01_upr_ci_VSP = AutoVivificationHandler()

                self.dict_AlleleTotalPerLocus_VSP = AutoVivificationHandler()

                self.dict_dictAlleleInstanceCountPerLocus_VSP = AutoVivificationHandler()

                self.dict_dictAlleleFreqs_VSP = AutoVivificationHandler()

                self.dict_Num_Sire_Parent  = AutoVivificationHandler()

                self.dict_Mean_Offspring_Per_Sire_Parent  = AutoVivificationHandler()
                
                self.dict_Mean_Variance_Per_Sire_Parent  = AutoVivificationHandler()

                self.dict_Num_Dame_Parent  = AutoVivificationHandler()

                self.dict_Mean_Offspring_Per_Dame_Parent  = AutoVivificationHandler()
                
                self.dict_Mean_Variance_Per_Dame_Parent  = AutoVivificationHandler()

                self.dict_Num_Male_Potential_Parent  = AutoVivificationHandler()

                self.dict_Mean_Offspring_Per_Male_Potential_Parent  = AutoVivificationHandler()
                
                self.dict_Mean_Variance_Per_Male_Potential_Parent  = AutoVivificationHandler()
                
                self.dict_Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents = AutoVivificationHandler()

                self.dict_Num_Female_Potential_Parent  = AutoVivificationHandler()

                self.dict_Mean_Offspring_Per_Female_Potential_Parent  = AutoVivificationHandler()
                
                self.dict_Mean_Variance_Per_Female_Potential_Parent  = AutoVivificationHandler()

                self.dict_Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents = AutoVivificationHandler()

                self.dict_Num_Actual_Parent  = AutoVivificationHandler()

                self.dict_Mean_Offspring_Per_Actual_Parent  = AutoVivificationHandler()
                
                self.dict_Mean_Variance_Per_Actual_Parent  = AutoVivificationHandler()

                self.dict_Num_Potential_Parent  = AutoVivificationHandler()

                self.dict_Mean_Offspring_Per_Potential_Parent  = AutoVivificationHandler()
                
                self.dict_Mean_Variance_Per_Potential_Parent  = AutoVivificationHandler()

                self.dict_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne  = AutoVivificationHandler()

                self.dict_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents   = AutoVivificationHandler()

            def method_PopulateProperties(self, boolIncludeParentOffspringProperties):
                    
                
                self.dictDataSectionNotesLevels[self.intLevel]['Data_Section_Note_' + str(self.intLevel)] = 'Virtual_Pop_Level_Params'

                #Why wouldnt I pass this in to cut down on processing instead of always doing them all???  I'll try
                self.intNumberVirtualSubPops = self.pop.numVirtualSubPop()  #This was what it was before
                #self.intNumberVirtualSubPops = intNumberVirtualSubPops
                
#                 for self.intVirtualSubPop in range(0, self.intNumberVirtualSubPops):
#  
#                     #Prime VSP number to process
#                     self.listCurrentVSP =[(self.intSubPop, self.intVirtualSubPop)]
#                     self.listSingleVirtualSubPop = self.listCurrentVSP[0]
                
                for itemVirtualSubPop in self.listVirtSubPopsToOutput:
                    
                    #VSP has individuals so continue
                    self.listCurrentVSP.append(itemVirtualSubPop)
                    self.listSingleVirtualSubPop = self.listCurrentVSP[0]
                    self.intVirtualSubPop = int(re.findall( r'\,(.*?)\)', str(self.listSingleVirtualSubPop))[0])
                       
                    self.dict_SubPop_VSP[self.intVirtualSubPop]['Sub_Pop_VSP'] = self.listCurrentVSP
                    #self.dict_SubPop['Sub_Pop'] = self.objSSParametersLocal.intSubPop
                    
                    intVSPSize = self.pop.subPopSize(self.listSingleVirtualSubPop)
                    self.dict_SubPopSize_VSP[self.listSingleVirtualSubPop]['Sub_Pop_Size_VSP'] = intVSPSize
                    
                    boolVSPHasIndivs = False
                    if intVSPSize > 0:
                        boolVSPHasIndivs = True

                    with SSAnalysisHandler() as objSSAnalysisOperation:
                        if self.objSSParametersLocal.boolReportDemographicNe:
                            #Demographic Ne for entire pop
                            dictNeDemographic = objSSAnalysisOperation.method_Statistics_On_NE_Demographic_Population_Size_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                            value = dictNeDemographic[0] #Only take the value for the first locus as they should all be the same
                        else:
                            value = self.stringSuppressed

                        self.dict_NeDemographic_VSP[self.listSingleVirtualSubPop]['demographic_ne_loci_1_VSP'] = value

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
                                    
#                             self.dict_temporal_JR_P1_ne_VSP[self.listSingleVirtualSubPop]['temporal_JR_P1_ne_VSP'] = listNeTemporal_JR_P1[0]
#                             self.dict_temporal_JR_P1_ne_2_5_CI_VSP[self.listSingleVirtualSubPop]['temporal_JR_P1_ne_2.5_CI_VSP'] = listNeTemporal_JR_P1[1]
#                             self.dict_temporal_JR_P1_ne_97_5_CI_VSP[self.listSingleVirtualSubPop]['temporal_JR_P1_ne_97.5_CI_VSP'] = listNeTemporal_JR_P1[2]

                            listNeTemporal_JR_P2 = []
                            if self.objSSParametersLocal.boolReportTemporalFS_P2_Ne:
                                #Temporal JR P2 Ne for entire pop
                                listNeTemporal_JR_P2 = objSSAnalysisOperation.method_Statistics_On_NE_Temporal_JordeRyman_P2_Population_Size_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                            else:
                                #Output has been suppressed
                                for i in range(0, 3):
                                    listNeTemporal_JR_P2.append(self.stringSuppressed)
                        else:
                            #Output is not applicable
                            for i in range(0, 3):
                                listNeTemporal_JR_P1.append(self.stringNotApplicable)
                                listNeTemporal_JR_P2.append(self.stringNotApplicable)

                        self.dict_temporal_JR_P1_ne_VSP[self.listSingleVirtualSubPop]['temporal_JR_P1_ne_VSP'] = listNeTemporal_JR_P1[0]
                        self.dict_temporal_JR_P1_ne_2_5_CI_VSP[self.listSingleVirtualSubPop]['temporal_JR_P1_ne_2.5_CI_VSP'] = listNeTemporal_JR_P1[1]
                        self.dict_temporal_JR_P1_ne_97_5_CI_VSP[self.listSingleVirtualSubPop]['temporal_JR_P1_ne_97.5_CI_VSP'] = listNeTemporal_JR_P1[2]
                                        
                        self.dict_temporal_JR_P2_ne_VSP[self.listSingleVirtualSubPop]['temporal_JR_P2_ne_VSP'] = listNeTemporal_JR_P2[0]
                        self.dict_temporal_JR_P2_ne_2_5_CI_VSP[self.listSingleVirtualSubPop]['temporal_JR_P2_ne_2.5_CI_VSP'] = listNeTemporal_JR_P2[1]
                        self.dict_temporal_JR_P2_ne_97_5_CI_VSP[self.listSingleVirtualSubPop]['temporal_JR_P2_ne_97.5_CI_VSP'] = listNeTemporal_JR_P2[2]

                        #This a temporary fix to cut down on LDNe calculations which slow the sim down.
                        #I only process VSPs 0-2 but when the final output is to be written all the VSP ie. 0-3 are passed and the pop.dvars([0,3)] fails as NE_LD was not recorded
                        if self.listSingleVirtualSubPop[1] !=3:

                            if self.objSSParametersLocal.boolReportLDNe:

                                #LD Ne - Dict for each PCrit (0.0, 0.05, 0.02, 0.01) listing NE, lower CI, upper CI    
                                dictNeLD = objSSAnalysisOperation.method_Statistics_On_NE_LD_Population_Size_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                                #for key, value in dictNeLD.iteritems():
                                        ##NE
                                        #outputFileHandle.write(str(round(value[0],4)))
                                        #outputFileHandle.write(stringDelimiter)
                                        ##Lower CI
                                        #outputFileHandle.write(str(round(value[1],4)))
                                        #outputFileHandle.write(stringDelimiter)
                                        ##Upper CI
                                        #outputFileHandle.write(str(round(value[2],4)))
                                        #outputFileHandle.write(stringDelimiter)
                            
                                self.dict_ld_ne_pcrit_0_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0_VSP'] = round(dictNeLD[0.0][0],4)
                                self.dict_ld_ne_pcrit_0_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0_lwr_ci_VSP'] = round(dictNeLD[0.0][1],4)
                                self.dict_ld_ne_pcrit_0_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0_upr_ci_VSP'] = round(dictNeLD[0.0][2],4)
                                self.dict_ld_ne_pcrit_0_05_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.05_VSP'] = round(dictNeLD[0.05][0],4)
                                self.dict_ld_ne_pcrit_0_05_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.05_lwr_ci_VSP'] = round(dictNeLD[0.05][1],4)
                                self.dict_ld_ne_pcrit_0_05_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.05_upr_ci_VSP'] = round(dictNeLD[0.05][2],4)
                                self.dict_ld_ne_pcrit_0_02_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.02_VSP'] = round(dictNeLD[0.02][0],4)
                                self.dict_ld_ne_pcrit_0_02_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.02_lwr_ci_VSP'] = round(dictNeLD[0.02][1],4)
                                self.dict_ld_ne_pcrit_0_02_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.02_upr_ci_VSP'] = round(dictNeLD[0.02][2],4)
                                self.dict_ld_ne_pcrit_0_01_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.01_VSP'] = round(dictNeLD[0.01][0],4)
                                self.dict_ld_ne_pcrit_0_01_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.01_lwr_ci_VSP'] = round(dictNeLD[0.01][1],4)
                                self.dict_ld_ne_pcrit_0_01_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.01_upr_ci_VSP'] = round(dictNeLD[0.01][2],4)
                            else:
                                #Output has been suppressed
                                self.dict_ld_ne_pcrit_0_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0_VSP'] = self.stringSuppressed
                                self.dict_ld_ne_pcrit_0_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0_lwr_ci_VSP'] = self.stringSuppressed
                                self.dict_ld_ne_pcrit_0_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0_upr_ci_VSP'] = self.stringSuppressed
                                self.dict_ld_ne_pcrit_0_05_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.05_VSP'] = self.stringSuppressed
                                self.dict_ld_ne_pcrit_0_05_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.05_lwr_ci_VSP'] = self.stringSuppressed
                                self.dict_ld_ne_pcrit_0_05_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.05_upr_ci_VSP'] = self.stringSuppressed
                                self.dict_ld_ne_pcrit_0_02_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.02_VSP'] = self.stringSuppressed
                                self.dict_ld_ne_pcrit_0_02_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.02_lwr_ci_VSP'] = self.stringSuppressed
                                self.dict_ld_ne_pcrit_0_02_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.02_upr_ci_VSP'] = self.stringSuppressed
                                self.dict_ld_ne_pcrit_0_01_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.01_VSP'] = self.stringSuppressed
                                self.dict_ld_ne_pcrit_0_01_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.01_lwr_ci_VSP'] = self.stringSuppressed
                                self.dict_ld_ne_pcrit_0_01_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.01_upr_ci_VSP'] = self.stringSuppressed
                        
                        #Construct dict of Allele totals per locus
                        dictAlleleTotalPerLocus = objSSAnalysisOperation.method_Statistics_On_Allele_TotalPerLocus_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                        #Write dict of Allele Totals Per Locus
                        self.dict_AlleleTotalPerLocus_VSP[self.listSingleVirtualSubPop]['Loci_Allele_Totals_Per_Locus_List_VSP'] = dictAlleleTotalPerLocus

                        #Construct dict of Allele instance count per locus
                        dictAlleleInstanceCountPerLocus = objSSAnalysisOperation.method_Statistics_On_Allele_InstanceCountPerLocus_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                        #Write dict of Allele Instance Counts
                        self.dict_dictAlleleInstanceCountPerLocus_VSP[self.listSingleVirtualSubPop]['Loci_Allele_Instance_Count_List_VSP'] = dictAlleleInstanceCountPerLocus

                        #Get Allele frequencies in list per population per loci per allele
                        #[Locus#]{Allele#1:Allele#1_Freq,Allele#2:Allele#2_Freq,...Allele#n:Allele#n_Freq}
                        dictAlleleFreqs = objSSAnalysisOperation.method_Statistics_On_Allele_Frequencies_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                        #Write dict of Allele Frequenecies
                        self.dict_dictAlleleFreqs_VSP[self.listSingleVirtualSubPop]['Loci_Allele_Frequencies_List_VSP'] = dictAlleleFreqs
                    
                        if boolIncludeParentOffspringProperties:
                            if boolVSPHasIndivs:
                                #Output Mean and Variance of the cumulative number of offspring per each parent for VSP (0,0)
                                #Keep results from VSP (0,0) and display on all subsequent VSPs until next offspring batch is created
                                
#                                if self.listSingleVirtualSubPop == (0,0):
                                    self.listCurrentVSP
                                    with SSAnalysisHandler() as objSSAnalysisOperation:
        
                                        self.dictSireOffspringCount = objSSAnalysisOperation.method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(self.pop, self.intSubPop, self.intVirtualSubPop)
                                        self.dictDameOffspringCount = objSSAnalysisOperation.method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(self.pop, self.intSubPop, self.intVirtualSubPop)
                                        
                                        #intSireCount = len(self.dictSireOffspringCount[sim.MALE])
                                        #intDameCount = len(self.dictDameOffspringCount[sim.FEMALE])
        
                                        #intSireCount = 0
                                        #for intID, intOffspringCount in self.dictSireOffspringCount[sim.MALE].iteritems():
                                        #    if intOffspringCount > 0:
                                        #        intSireCount += 1
        
                                        #WITHOUT DEEPCOPY in this function the passed dict objects will be updated by reference 
                                        self.dictOffspringCount = objSSAnalysisOperation.method_Count_Offspring_PerParent_For_VirtualSubPop(self.pop, self.intSubPop, self.intVirtualSubPop, self.dictSireOffspringCount, self.dictDameOffspringCount)
        
                                        if (len(self.dictOffspringCount[sim.MALE]) > 0) | (len(self.dictOffspringCount[sim.FEMALE]) > 0):
                                            with AnalysisHandler() as objAnalysisOperation:
                                                
                                                #Construct a list of ACTUAL SIRE offspring counts
                                                listSireOffspringCount = []
                                                for i in self.dictSireOffspringCount[sim.MALE]:
                                                    listSireOffspringCount.append(self.dictSireOffspringCount[sim.MALE][i])
        
                                                self.floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listSireOffspringCount)
                                                self.floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listSireOffspringCount)
                                                
                                                self.dict_Num_Sire_Parent[self.listSingleVirtualSubPop]['Num_Sire_Parent'] = len(listSireOffspringCount)
                                                self.dict_Mean_Offspring_Per_Sire_Parent[self.listSingleVirtualSubPop]['Mean_Offspring_Per_Sire_Parent'] = round(self.floatMean,4)
                                                self.dict_Mean_Variance_Per_Sire_Parent[self.listSingleVirtualSubPop]['Mean_Variance_Offspring_Per_Sire_Parent'] = round( self.floatVariance,4)
        
                                                #Construct a list of POTENTIAL SIRE offspring counts
                                                listMaleOffspringCount = []
                                                for i in self.dictOffspringCount[sim.MALE]:
                                                    listMaleOffspringCount.append(self.dictOffspringCount[sim.MALE][i])
        
                                                self.floatMeanLitterSizeForMaleParents_MeanKsex = objAnalysisOperation.method_Get_Mean_From_A_List(listMaleOffspringCount)
                                                self.floatMeanVarianceLitterSizeForMaleParents_VarKsex = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listMaleOffspringCount)
                                                self.integerNumberofParentsForMaleParents_Nsex = len(listMaleOffspringCount)
                                                self.floatNeDemographicByMaleParentsFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_By_Parental_Sex_Given_Known_Offspring(self.integerNumberofParentsForMaleParents_Nsex, self.floatMeanLitterSizeForMaleParents_MeanKsex, self.floatMeanVarianceLitterSizeForMaleParents_VarKsex)
                                                
        
                                                self.dict_Num_Male_Potential_Parent[self.listSingleVirtualSubPop]['Num_Male_Potential_Parent'] = self.integerNumberofParentsForMaleParents_Nsex
                                                self.dict_Mean_Offspring_Per_Male_Potential_Parent[self.listSingleVirtualSubPop]['Mean_Offspring_Per_Male_Potential_Parent'] = round(self.floatMeanLitterSizeForMaleParents_MeanKsex,4)
                                                self.dict_Mean_Variance_Per_Male_Potential_Parent[self.listSingleVirtualSubPop]['Mean_Variance_Offspring_Per_Male_Potential_Parent'] = round( self.floatMeanVarianceLitterSizeForMaleParents_VarKsex,4)
                                                self.dict_Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents[self.listSingleVirtualSubPop]['Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents'] = round( self.floatNeDemographicByMaleParentsFromKnownOffspring,4)
        
                                                #Construct a list of ACTUAL DAME offspring counts
                                                listDameOffspringCount = []
                                                for i in self.dictDameOffspringCount[sim.FEMALE]:
                                                    listDameOffspringCount.append(self.dictDameOffspringCount[sim.FEMALE][i])
        
                                                self.floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listDameOffspringCount)
                                                self.floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listDameOffspringCount)
                                                
                                                self.dict_Num_Dame_Parent[self.listSingleVirtualSubPop]['Num_Dame_Parent'] = len(listDameOffspringCount)
                                                self.dict_Mean_Offspring_Per_Dame_Parent[self.listSingleVirtualSubPop]['Mean_Offspring_Per_Dame_Parent'] = round(self.floatMean,4)
                                                self.dict_Mean_Variance_Per_Dame_Parent[self.listSingleVirtualSubPop]['Mean_Variance_Offspring_Per_Dame_Parent'] = round( self.floatVariance,4)
        
                                                #Construct a list of POTENTIAL DAME offspring counts
                                                listFemaleOffspringCount = []
                                                for i in self.dictOffspringCount[sim.FEMALE]:
                                                    listFemaleOffspringCount.append(self.dictOffspringCount[sim.FEMALE][i])
                                                
                                                self.floatMeanLitterSizeForFemaleParents_MeanKsex = objAnalysisOperation.method_Get_Mean_From_A_List(listFemaleOffspringCount)
                                                self.floatMeanVarianceLitterSizeForFemaleParents_VarKsex = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listFemaleOffspringCount)
                                                self.integerNumberofParentsForFemaleParents_Nsex = len(listFemaleOffspringCount)
                                                self.floatNeDemographicByFemaleParentsFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_By_Parental_Sex_Given_Known_Offspring(self.integerNumberofParentsForFemaleParents_Nsex, self.floatMeanLitterSizeForFemaleParents_MeanKsex, self.floatMeanVarianceLitterSizeForFemaleParents_VarKsex)
                                                
        
                                                self.dict_Num_Female_Potential_Parent[self.listSingleVirtualSubPop]['Num_Female_Potential_Parent'] = self.integerNumberofParentsForFemaleParents_Nsex
                                                self.dict_Mean_Offspring_Per_Female_Potential_Parent[self.listSingleVirtualSubPop]['Mean_Offspring_Per_Female_Potential_Parent'] = round(self.floatMeanLitterSizeForFemaleParents_MeanKsex,4)
                                                self.dict_Mean_Variance_Per_Female_Potential_Parent[self.listSingleVirtualSubPop]['Mean_Variance_Offspring_Per_Female_Potential_Parent'] = round(self.floatMeanVarianceLitterSizeForFemaleParents_VarKsex,4)
                                                self.dict_Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents[self.listSingleVirtualSubPop]['Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents'] = round(self.floatNeDemographicByFemaleParentsFromKnownOffspring,4)
        
                                                listActualParentCount = []
                                                listActualParentCount = listSireOffspringCount + listDameOffspringCount
        
                                                self.floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listActualParentCount)
                                                self.floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listActualParentCount)
        
                                                self.dict_Num_Actual_Parent[self.listSingleVirtualSubPop]['Num_Actual_Parent'] = len(listActualParentCount)
                                                self.dict_Mean_Offspring_Per_Actual_Parent[self.listSingleVirtualSubPop]['Mean_Offspring_Per_Actual_Parent'] = round(self.floatMean,4)
                                                self.dict_Mean_Variance_Per_Actual_Parent[self.listSingleVirtualSubPop]['Mean_Variance_Offspring_Per_Actual_Parent'] = round( self.floatVariance,4)
        
        
                                                listBothSexesOffspringCount = []
                                                for intCount in listMaleOffspringCount:
                                                    listBothSexesOffspringCount.append(intCount)
                                                for intCount in listFemaleOffspringCount:
                                                    listBothSexesOffspringCount.append(intCount)
        
                                                self.floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listBothSexesOffspringCount)
                                                self.floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listBothSexesOffspringCount)
                                                self.integerNumberofParentsForBothSexesParents_Nsex = len(listBothSexesOffspringCount)
                                                self.floatNeDemographicGivenBothSexesNeFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_From_Known_Offspring_Given_Parental_Sex_Ne(self.floatNeDemographicByMaleParentsFromKnownOffspring, self.floatNeDemographicByFemaleParentsFromKnownOffspring)
          
                                                self.dict_Num_Potential_Parent[self.listSingleVirtualSubPop]['Num_Potential_Parent'] = self.integerNumberofParentsForBothSexesParents_Nsex
                                                self.dict_Mean_Offspring_Per_Potential_Parent[self.listSingleVirtualSubPop]['Mean_Offspring_Per_Potential_Parent'] = round(self.floatMean,4)
                                                self.dict_Mean_Variance_Per_Potential_Parent[self.listSingleVirtualSubPop]['Mean_Variance_Offspring_Per_Potential_Parent'] = round( self.floatVariance,4)
                                                self.dict_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne[self.listSingleVirtualSubPop]['Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne'] = round( self.floatNeDemographicGivenBothSexesNeFromKnownOffspring,4)
                                                self.dict_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents[self.listSingleVirtualSubPop]['Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents'] = round((self.floatNeDemographicGivenBothSexesNeFromKnownOffspring / self.integerNumberofParentsForBothSexesParents_Nsex),4)

                pass


# -------------- Class specific routines

            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.class_obj_SSVirtualSubPop = obj_SSVirtualSubPop() 
        return self.class_obj_SSVirtualSubPop
 
    def __exit__(self, type, value, traceback): 
        self.class_obj_SSVirtualSubPop.classCleanUp()