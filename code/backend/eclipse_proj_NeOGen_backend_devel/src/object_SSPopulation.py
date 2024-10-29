#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
#from simuPOP
#import simuPOP as sim
from AutoVivificationHandler import AutoVivificationHandler
from SSAnalysisHandler import SSAnalysisHandler
from OutputHandler import OutputHandler
from globals_SharkSim import globalsSS

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
#from collections import defaultdict
from collections import OrderedDict

class object_SSPopulation:
    """Contains SS Simulation level properties and methods"""
    def __enter__(self):

        class obj_SSPopulation():

# -------------- Class specific routines

            __slots__ = ('stringSuppressed'
                         ,'stringDelimiter'
                         ,'stringDelimiter2'
                         ,'objSSParametersLocal'
                         ,'intLevel'
                         ,'pop'
                         ,'intSubPop'
                         ,'dictDataSectionNotesLevels'
                        ,'dict_SubPop'
                        ,'dict_SubPopSize'
                        ,'dict_NeDemographic'
                        ,'dict_temporal_JR_P1_ne'
                        ,'dict_temporal_JR_P1_ne_2_5_CI'
                        ,'dict_temporal_JR_P1_ne_97_5_CI'
                        ,'dict_temporal_JR_P2_ne'
                        ,'dict_temporal_JR_P2_ne_2_5_CI'
                        ,'dict_temporal_JR_P2_ne_97_5_CI'
                        ,'dict_ld_ne_pcrit_0'
                        ,'dict_ld_ne_pcrit_0_lwr_ci'
                        ,'dict_ld_ne_pcrit_0_upr_ci'
                        ,'dict_ld_ne_pcrit_0_05'
                        ,'dict_ld_ne_pcrit_0_05_lwr_ci'
                        ,'dict_ld_ne_pcrit_0_05_upr_ci'
                        ,'dict_ld_ne_pcrit_0_02'
                        ,'dict_ld_ne_pcrit_0_02_lwr_ci'
                        ,'dict_ld_ne_pcrit_0_02_upr_ci'
                        ,'dict_ld_ne_pcrit_0_01'
                        ,'dict_ld_ne_pcrit_0_01_lwr_ci'
                        ,'dict_ld_ne_pcrit_0_01_upr_ci'
                        ,'dict_AlleleTotalPerLocus'
                        ,'dict_dictAlleleInstanceCountPerLocus'
                        ,'dict_dictAlleleFreqs'
                        ,'dict_dictAlleleFreqsAtPopulationInitialization'
                        
                        ,'dictReportingPropertyObjects'
                        )

            def __init__(self):
                
                self.stringNotApplicable = globalsSS.StringUnexpectedResults.static_stringNotApplicable
                self.stringSuppressed = 'SUP'

                self.stringDelimiter = ';'
                self.stringDelimiter2 = ','

                self.objSSParametersLocal = None

                self.intLevel = 3
                
                self.pop = None
                
                self.intSubPop = 0

                self.dictDataSectionNotesLevels = AutoVivificationHandler()

                self.dict_SubPop = {}
                    
                self.dict_SubPopSize = {}
                
                self.dict_NeDemographic = {}

                self.dict_temporal_JR_P1_ne = {}

                self.dict_temporal_JR_P1_ne_2_5_CI = {}

                self.dict_temporal_JR_P1_ne_97_5_CI = {}

                self.dict_temporal_JR_P2_ne = {}

                self.dict_temporal_JR_P2_ne_2_5_CI = {}

                self.dict_temporal_JR_P2_ne_97_5_CI = {}

                self.dict_ld_ne_pcrit_0 = {}

                self.dict_ld_ne_pcrit_0_lwr_ci = {}

                self.dict_ld_ne_pcrit_0_upr_ci = {}

                self.dict_ld_ne_pcrit_0_05 = {}

                self.dict_ld_ne_pcrit_0_05_lwr_ci = {}

                self.dict_ld_ne_pcrit_0_05_upr_ci = {}

                self.dict_ld_ne_pcrit_0_02 = {}

                self.dict_ld_ne_pcrit_0_02_lwr_ci = {}

                self.dict_ld_ne_pcrit_0_02_upr_ci = {}

                self.dict_ld_ne_pcrit_0_01 = {}

                self.dict_ld_ne_pcrit_0_01_lwr_ci = {}

                self.dict_ld_ne_pcrit_0_01_upr_ci = {}

                self.dict_AlleleTotalPerLocus = {}

                self.dict_dictAlleleInstanceCountPerLocus = {}

                self.dict_dictAlleleFreqs = {}
                
                self.dict_dictAlleleFreqsAtPopulationInitialization = {}
                
                self.dictReportingPropertyObjects = OrderedDict()

            def method_PopulateProperties(self):
                    
                self.dictDataSectionNotesLevels[self.intLevel]['Data_Section_Note_' + str(self.intLevel)] = 'Pop_Level_Params'
                
                self.dict_SubPop['Sub_Pop'] = self.objSSParametersLocal.intSubPop
                    
                self.dict_SubPopSize['Sub_Pop_Size'] = self.pop.subPopSize([self.objSSParametersLocal.intSubPop])
                
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    value = ''
                    if self.objSSParametersLocal.boolReportDemographicNe:
                        #Demographic Ne for entire pop
                        dictNeDemographic = objSSAnalysisOperation.method_Statistics_On_NE_Demographic_Population_Size_For_VirtualSubPop(self.pop, [self.intSubPop])
                        if len(dictNeDemographic) > 0:
                            value = dictNeDemographic[0] #Only take the value for the first locus as they should all be the same
                        else:
                            value = self.stringNotApplicable
                        pass
                    else:
                        value = self.stringSuppressed
                    
                    self.dict_NeDemographic['demographic_ne_loci_1'] = value

                    listNeTemporal_JR_P1 = []
                    if self.objSSParametersLocal.boolReportTemporalFS_P1_Ne:
                        #Temporal JR P1 Ne for entire pop
                        listNeTemporal_JR_P1 = objSSAnalysisOperation.method_Statistics_On_NE_Temporal_JordeRyman_P1_Population_Size_For_VirtualSubPop(self.pop, self.intSubPop)
                    else:
                        #Output has been suppressed
                        for i in range(0, 3):
                            listNeTemporal_JR_P1.append(self.stringSuppressed)
                    
                    listNeTemporal_JR_P2 = []    
                    if self.objSSParametersLocal.boolReportTemporalFS_P2_Ne:
                        #Temporal JR P2 Ne for entire pop
                        listNeTemporal_JR_P2 = objSSAnalysisOperation.method_Statistics_On_NE_Temporal_JordeRyman_P2_Population_Size_For_VirtualSubPop(self.pop, self.intSubPop)
                    else:
                        #Output has been suppressed
                        for i in range(0, 3):
                            listNeTemporal_JR_P2.append(self.stringSuppressed)

                    self.dict_temporal_JR_P1_ne['temporal_JR_P1_ne'] = listNeTemporal_JR_P1[0]
                    self.dict_temporal_JR_P1_ne_2_5_CI['temporal_JR_P1_ne_2.5_CI'] = listNeTemporal_JR_P1[1]
                    self.dict_temporal_JR_P1_ne_97_5_CI['temporal_JR_P1_ne_97.5_CI'] = listNeTemporal_JR_P1[2]

                    self.dict_temporal_JR_P2_ne['temporal_JR_P2_ne'] = listNeTemporal_JR_P2[0]
                    self.dict_temporal_JR_P2_ne_2_5_CI['temporal_JR_P2_ne_2.5_CI'] = listNeTemporal_JR_P2[1]
                    self.dict_temporal_JR_P2_ne_97_5_CI['temporal_JR_P2_ne_97.5_CI'] = listNeTemporal_JR_P2[2]

                    if self.objSSParametersLocal.boolReportLDNe:
                        #LD Ne - Dict for each PCrit (0.0, 0.05, 0.02, 0.01) listing NE, lower CI, upper CI    
                        dictNeLD = objSSAnalysisOperation.method_Statistics_On_NE_LD_Population_Size_For_VirtualSubPop(self.pop, self.intSubPop)
                        #for key, value in dictNeLD.iteritems():
                                ##NE
                                #outputFileHandle.write(str(round(value[0],2)))
                                #outputFileHandle.write(stringDelimiter)
                                ##Lower CI
                                #outputFileHandle.write(str(round(value[1],2)))
                                #outputFileHandle.write(stringDelimiter)
                                ##Upper CI
                                #outputFileHandle.write(str(round(value[2],2)))
                                #outputFileHandle.write(stringDelimiter)

                        self.dict_ld_ne_pcrit_0['ld_ne_pcrit_0'] = round(dictNeLD[0.0][0],2)
                        self.dict_ld_ne_pcrit_0_lwr_ci['ld_ne_pcrit_0_lwr_ci'] = round(dictNeLD[0.0][1],2)
                        self.dict_ld_ne_pcrit_0_upr_ci['ld_ne_pcrit_0_upr_ci'] = round(dictNeLD[0.0][2],2)
                        self.dict_ld_ne_pcrit_0_05['ld_ne_pcrit_0.05'] = round(dictNeLD[0.05][0],2)
                        self.dict_ld_ne_pcrit_0_05_lwr_ci['ld_ne_pcrit_0.05_lwr_ci'] = round(dictNeLD[0.05][1],2)
                        self.dict_ld_ne_pcrit_0_05_upr_ci['ld_ne_pcrit_0.05_upr_ci'] = round(dictNeLD[0.05][2],2)
                        self.dict_ld_ne_pcrit_0_02['ld_ne_pcrit_0.02'] = round(dictNeLD[0.02][0],2)
                        self.dict_ld_ne_pcrit_0_02_lwr_ci['ld_ne_pcrit_0.02_lwr_ci'] = round(dictNeLD[0.02][1],2)
                        self.dict_ld_ne_pcrit_0_02_upr_ci['ld_ne_pcrit_0.02_upr_ci'] = round(dictNeLD[0.02][2],2)
                        self.dict_ld_ne_pcrit_0_01['ld_ne_pcrit_0.01'] = round(dictNeLD[0.01][0],2)
                        self.dict_ld_ne_pcrit_0_01_lwr_ci['ld_ne_pcrit_0.01_lwr_ci'] = round(dictNeLD[0.01][1],2)
                        self.dict_ld_ne_pcrit_0_01_upr_ci['ld_ne_pcrit_0.01_upr_ci'] = round(dictNeLD[0.01][2],2)

                    else:
                        #Output has been suppressed
                        self.dict_ld_ne_pcrit_0['ld_ne_pcrit_0'] = self.stringSuppressed
                        self.dict_ld_ne_pcrit_0_lwr_ci['ld_ne_pcrit_0_lwr_ci'] = self.stringSuppressed
                        self.dict_ld_ne_pcrit_0_upr_ci['ld_ne_pcrit_0_upr_ci'] = self.stringSuppressed
                        self.dict_ld_ne_pcrit_0_05['ld_ne_pcrit_0.05'] = self.stringSuppressed
                        self.dict_ld_ne_pcrit_0_05_lwr_ci['ld_ne_pcrit_0.05_lwr_ci'] = self.stringSuppressed
                        self.dict_ld_ne_pcrit_0_05_upr_ci['ld_ne_pcrit_0.05_upr_ci'] = self.stringSuppressed
                        self.dict_ld_ne_pcrit_0_02['ld_ne_pcrit_0.02'] = self.stringSuppressed
                        self.dict_ld_ne_pcrit_0_02_lwr_ci['ld_ne_pcrit_0.02_lwr_ci'] = self.stringSuppressed
                        self.dict_ld_ne_pcrit_0_02_upr_ci['ld_ne_pcrit_0.02_upr_ci'] = self.stringSuppressed
                        self.dict_ld_ne_pcrit_0_01['ld_ne_pcrit_0.01'] = self.stringSuppressed
                        self.dict_ld_ne_pcrit_0_01_lwr_ci['ld_ne_pcrit_0.01_lwr_ci'] = self.stringSuppressed
                        self.dict_ld_ne_pcrit_0_01_upr_ci['ld_ne_pcrit_0.01_upr_ci'] = self.stringSuppressed
                        
                    #Allele count & frequency reporting
                    #intTotalLoci = self.pop.totNumLoci()
                    #with SSAnalysisHandler() as objSSAnalysisOperation:

                    #Construct dict of Allele totals per locus
                    dictAlleleTotalPerLocus = objSSAnalysisOperation.method_Statistics_On_Allele_TotalPerLocus_For_VirtualSubPop(self.pop, self.intSubPop)
                    #Write dict of Allele Totals Per Locus
                    self.dict_AlleleTotalPerLocus['Loci_Allele_Totals_Per_Locus_List'] = dictAlleleTotalPerLocus

                    #Construct dict of Allele instance count per locus
                    dictAlleleInstanceCountPerLocus = objSSAnalysisOperation.method_Statistics_On_Allele_InstanceCountPerLocus_For_VirtualSubPop(self.pop, self.intSubPop)
                    #Write dict of Allele Instance Counts
                    self.dict_dictAlleleInstanceCountPerLocus['Loci_Allele_Instance_Count_List'] = dictAlleleInstanceCountPerLocus

                    #Get Allele frequencies in list per population per loci per allele
                    #[Locus#]{Allele#1:Allele#1_Freq,Allele#2:Allele#2_Freq,...Allele#n:Allele#n_Freq}
                    #Convert it into a string delimted value
                    
                    #Baseline allele freqs
                    odictSimPerLocusAlleleFreqs = self.objSSParametersLocal.odictAlleleFreqsAtSimInitialization
                    
                    odictPopPerLocusAlleleFreqs = objSSAnalysisOperation.method_Statistics_On_Allele_Frequencies_For_VirtualSubPop(self.pop, self.intSubPop)
                    listAlleleFreqs_All = objSSAnalysisOperation.method_Convert_Allele_Freqs_To_List(odictSimPerLocusAlleleFreqs, odictPopPerLocusAlleleFreqs)
                    
                    with OutputHandler() as objOutputOperation:
                        strDelimitedValues = objOutputOperation.method_AccumulateListValuesIntoDelimetedString(listAlleleFreqs_All, self.stringDelimiter2)
                        self.dict_dictAlleleFreqs['Loci_Allele_Frequencies_List'] = strDelimitedValues
                    pass

#                     dictAlleleFreqs = objSSAnalysisOperation.method_Statistics_On_Allele_Frequencies_For_VirtualSubPop(self.pop, self.intSubPop)
#                     #Write dict of Allele Frequenecies
#                     self.dict_dictAlleleFreqs['Loci_Allele_Frequencies_List'] = dictAlleleFreqs
#                     
                    odictPopPerLocusAlleleFreqs = self.objSSParametersLocal.odictAlleleFreqsAtPopInitialization
                    listAlleleFreqs_All = objSSAnalysisOperation.method_Convert_Allele_Freqs_To_List(odictSimPerLocusAlleleFreqs, odictPopPerLocusAlleleFreqs)
                    
                    with OutputHandler() as objOutputOperation:
                        strDelimitedValues = objOutputOperation.method_AccumulateListValuesIntoDelimetedString(listAlleleFreqs_All, self.stringDelimiter2)
                        self.dict_dictAlleleFreqsAtPopulationInitialization['Loci_Allele_Frequencies_List_At_Pop_Init'] = strDelimitedValues
                    pass
                    
                    
                pass


# -------------- Class specific routines

            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.class_obj_SSPopulation = obj_SSPopulation() 
        return self.class_obj_SSPopulation
 
    def __exit__(self, type, value, traceback): 
        self.class_obj_SSPopulation.classCleanUp()