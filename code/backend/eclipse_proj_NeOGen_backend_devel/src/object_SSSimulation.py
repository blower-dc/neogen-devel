#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
#from simuPOP
#import simuPOP as sim
from globals_SharkSim import globalsSS
from AutoVivificationHandler import AutoVivificationHandler
from OutputHandler import OutputHandler
from SSAnalysisHandler import SSAnalysisHandler

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
#from collections import defaultdict
from collections import OrderedDict

class object_SSSimulation:
    """Contains SS Simulation level properties and methods"""
    def __enter__(self):

        class obj_SSSimulation():

# -------------- Class specific routines

            __slots__ =('stringDelimiter'
                        ,'stringDelimiter2'
                        ,'objSSParametersLocal'
                        ,'intLevel'
                        ,'dictDataSectionNotesLevels'
                        ,'dictFilenameEmbeddedFields'
                        ,'dict_SingleRun'
                        ,'dict_BatchRunStart'
                        ,'dict_ReplicateRunStart'
                        ,'dict_SimCurrentBatch'
                        ,'dict_SimCurrentReplicate'
                        ,'dict_SimPopulationSize'
                        ,'dict_IterationsToSimulate'
                        ,'dict_CurrentIteration'
                        ,'dict_InitialAgesRandom'
                        ,'dict_InitialMaleSexRatio'
                        ,'dict_MatingScheme'
                        ,'dict_MaxAge'
                        ,'dict_MinMatinAee'
                        ,'dict_MaxMatingAge'
                        ,'dictPredictedBreedingPopulationSize'
                        ,'dict_MeanOffspringPerIndiv'
                        ,'dict_MatingDistType'
                        ,'dict_MatingDistParamList'
                        ,'dict_NumLoci'
                        ,'dict_NumAllelesPerLoci'
                        ,'dict_LociAlleleFreqScheme'
                        ,'dict_InitialLociAlleleFreqList'
                        ,'dict_dictSimImportedLocusNames'
                        ,'dict_dictSimImportedLocusAlleleNames'
                        
                        ,'dictReportingPropertyObjects'

                       )

            def __init__(self):
                
                self.stringDelimiter = ';'
                self.stringDelimiter2 = ','

                self.objSSParametersLocal = None

                self.intLevel = 1
                
                #Create 3d Dict to hold multiple level header keys and values but can be accessed by intLevel
                #self.dictDataSectionNotes = defaultdict(lambda: defaultdict(dict))
                #self.dictDataSectionNotes[self.intLevel]['Data_Section_Note_' + str(self.intLevel)] = 'Sim_Level_Params'
               
                #self.dictDataSectionNotes ={}
                #self.dictDataSectionNotes['Data_Section_Note_' + str(self.intLevel)] = 'Sim_Level_Params'
                #self.dictDataSectionNotesLevels ={}
                #self.dictDataSectionNotesLevels[self.intLevel] = self.dictDataSectionNotes
                
                self.dictDataSectionNotesLevels = AutoVivificationHandler()

                self.dictFilenameEmbeddedFields = {}

                self.dict_SingleRun = {}
                    
                self.dict_BatchRunStart = {}
                    
                self.dict_ReplicateRunStart = {}
                    
                self.dict_SimPopulationSize = {}
                
                self.dict_SimCurrentBatch = {}
                
                self.dict_SimCurrentReplicate = {}
                    
                self.dict_IterationsToSimulate = {}
                    
                self.dict_CurrentIteration = {}
                    
                self.dict_InitialAgesRandom = {}
                    
                self.dict_InitialMaleSexRatio = {}
                    
                self.dict_MatingScheme = {}
                    
                self.dict_MaxAge = {}
                
                self.dict_MinMatinAee = {}
                    
                self.dict_MaxMatingAge = {}

                self.dictPredictedBreedingPopulationSize = {}
                    
                self.dict_MeanOffspringPerIndiv = {}
                    
                self.dict_MatingDistType = {}
                
                self.dict_MatingDistParamList = {}
                    
                self.dict_NumLoci = {}
                
                self.dict_NumAllelesPerLoci = {}
                    
                self.dict_LociAlleleFreqScheme = {}
                
                self.dict_InitialLociAlleleFreqList = {}

                self.dict_dictSimImportedLocusNames = {}
                
                self.dict_dictSimImportedLocusAlleleNames = {}

                self.dictReportingPropertyObjects = OrderedDict()

            def method_PopulateProperties(self):
                    
                
                self.dictDataSectionNotesLevels[self.intLevel]['Data_Section_Note_' + str(self.intLevel)] = 'Sim_Level_Params'
                                
                self.dictFilenameEmbeddedFields['Filename_Embedded_Fields'] = self.objSSParametersLocal.strFilenameEmbeddedFields

                self.dict_SingleRun['Single_Run'] = self.objSSParametersLocal.boolSingleRun
                    
                self.dict_BatchRunStart['Batch_Run_Started_Y_m_d_H_M'] = self.objSSParametersLocal.dateBatchRunStartTime.strftime("%Y_%m_%d_%H_%M")
                    
                self.dict_ReplicateRunStart['Replicate_Run_Started_Y_m_d_H_M'] = self.objSSParametersLocal.dateReplicateRunStartTime.strftime("%Y_%m_%d_%H_%M")

                self.dict_SimCurrentBatch['Sim_Current_Batch'] = self.objSSParametersLocal.intCurrentBatch
                
                self.dict_SimCurrentReplicate['Sim_Current_Replicate'] = self.objSSParametersLocal.intCurrentReplicate
                    
                self.dict_SimPopulationSize['Sim_Population_size'] = self.objSSParametersLocal.popnSize
                
                self.dict_IterationsToSimulate['Grand_Total_Months_to_simulate'] = self.objSSParametersLocal.intGrandTotalMonthsToSimulate
                    
                self.dict_CurrentIteration['Current_Month'] = self.objSSParametersLocal.intSimulationCurrentMonth
                    
                self.dict_InitialAgesRandom['Initial_population_ages_scheme'] = self.objSSParametersLocal.intPopulationInitialAges
                    
                self.dict_InitialMaleSexRatio['Male_sex_ratio_initial'] = self.objSSParametersLocal.floatSexRatioOfMales
                    
                self.dict_MatingScheme['Mating_scheme'] = self.objSSParametersLocal.intMatingSchemeType
                    
                str_Colname_Prefix = globalsSS.Colnames_BATCH_PARAMETERS.static_str_Colname_Max_age    
                #self.dict_MaxAge['Maximum_age'] = self.objSSParametersLocal.maxAge
                self.dict_MaxAge[str_Colname_Prefix] = self.objSSParametersLocal.maxAge
                
                str_Colname_Prefix = globalsSS.Colnames_BATCH_PARAMETERS.static_str_Colname_Min_mating_age
                #self.dict_MinMatinAee['Minimal_mating_age'] = self.objSSParametersLocal.minMatingAge
                self.dict_MinMatinAee[str_Colname_Prefix] = self.objSSParametersLocal.minMatingAge

                str_Colname_Prefix = globalsSS.Colnames_BATCH_PARAMETERS.static_str_Colname_Max_mating_age                    
                #self.dict_MaxMatingAge['Maximal_mating_age'] = self.objSSParametersLocal.maxMatingAge
                self.dict_MaxMatingAge[str_Colname_Prefix] = self.objSSParametersLocal.maxMatingAge
                
                self.dictPredictedBreedingPopulationSize['Predicted_Breeding_Pop_Size'] = self.objSSParametersLocal.intPredictedBreedingPopulationSize
                    
                self.dict_MeanOffspringPerIndiv['Mean_number_of_offspring_per_individual'] = self.objSSParametersLocal.meanvarnumOffspring
                    
                self.dict_MatingDistType['Mating_distribution_type'] = self.objSSParametersLocal.listOffspringNumberParameters[0]
                
                #Combine multiple values into a single value for output
                #strValues=''
                #boolFirstValue=False
                #for value in self.objSSParametersLocal.listOffspringNumberParameters:
                #    if boolFirstValue == False:
                #        boolFirstValue = True
                #        strValues = strValues + str(value)
                #    else:
                #        strValues = strValues + self.stringDelimiter2 + str(value)

                #outputFileHandle.write(strValues)    
                with OutputHandler() as objOutputOperation:
                    strDelimitedValues = objOutputOperation.method_AccumulateListValuesIntoDelimetedString(self.objSSParametersLocal.listOffspringNumberParameters, self.stringDelimiter2)
                    self.dict_MatingDistParamList['Mating_distribution_parameter_list'] = strDelimitedValues
                    
                self.dict_NumLoci['Number_of_loci'] = self.objSSParametersLocal.nLoci
                
                #Subtract 1 for real number of alleles per locus    
                self.dict_NumAllelesPerLoci['Number_of_alleles_per_loci'] = self.objSSParametersLocal.nAllelesPerLoci-1
                    
                self.dict_LociAlleleFreqScheme['Loci_allele_frequencies_scheme'] = self.objSSParametersLocal.intAlleleFrequencyScheme
                
                with OutputHandler() as objOutputOperation:
                    strDelimitedValues = objOutputOperation.method_AccumulateListValuesIntoDelimetedString(self.objSSParametersLocal.listAlleleFreqs, self.stringDelimiter2)
                    self.dict_InitialLociAlleleFreqList['Loci_initial_allele_frequencies_list'] = strDelimitedValues
                    pass
                
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    listAlleleNames = []
                    listAlleleNames = objSSAnalysisOperation.method_Extract_Imported_Allele_Info_To_List(self.objSSParametersLocal.odictAlleleFreqsAtSimInitialization, 'Locus_Name')
                    with OutputHandler() as objOutputOperation:
                        strDelimitedValues = objOutputOperation.method_AccumulateListValuesIntoDelimetedString(listAlleleNames, self.stringDelimiter2)
                        self.dict_dictSimImportedLocusNames['Sim_Imported_Locus_Names'] = strDelimitedValues
                
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    listAlleleNames = []
                    listAlleleNames = objSSAnalysisOperation.method_Extract_Imported_Allele_Info_To_List(self.objSSParametersLocal.odictAlleleFreqsAtSimInitialization, 'Allele_Name')
                    with OutputHandler() as objOutputOperation:
                        strDelimitedValues = objOutputOperation.method_AccumulateListValuesIntoDelimetedString(listAlleleNames, self.stringDelimiter2)
                        self.dict_dictSimImportedLocusAlleleNames['Sim_Imported_Locus_Allele_Names'] = strDelimitedValues
                
                pass


# -------------- Class specific routines

            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.class_obj_SSSimulation = obj_SSSimulation() 
        return self.class_obj_SSSimulation
 
    def __exit__(self, type, value, traceback): 
        self.class_obj_SSSimulation.classCleanUp()