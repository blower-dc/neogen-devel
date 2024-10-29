#import random
#from random import randint as numpy__random.randint  #MUCH SLOWER THAN NUMPY__RANDINT
from random import sample as random__sample
#import itertools
from collections import OrderedDict
#from pprint import pprint 
from numpy import random as numpy__random
#import re
#import math
from datetime import datetime, timedelta
#import gc

from math import floor as math__floor
import itertools
import pandas
from logging import getLogger as logging__getLogger
from collections import Counter as collections__Counter
from decimal import *
import sys
# DEBUG Imports
#import objgraph
import pdb
from memory_profiler import profile
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import SharkSim modules
from globals_SharkSim import globalsSS
from object_SSReportingObject import object_SSReportingObject
from SSOutputHandler import SSOutputHandler
from SSAnalysisHandler import SSAnalysisHandler
from SSSamplingTest import SSSamplingTest
#------------------< Import DCB_General modules
# DEBUG Imports
from handler_Debug import Debug_Location as dcb_Debug_Location
from handler_Debug import Timer
from handler_Debug import Timer2
from handler_Debug import Debug_Location
from FileHandler import FileHandler
from handler_Logging import Logging
#from EnumeratorHandler import EnumeratorHandler

#from DebugHandler import DebugHandler
from AutoVivificationHandler import AutoVivificationHandler
from AnalysisHandler import  AnalysisHandler

##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
## PROD simuPOP
#from simuPOP import *
#import simuPOP 
#import simuPOP as simm
import simuPOP as simupop
from simuPOP import utils as simuPOP__utils
from simuPOP.sampling import drawRandomSample


class SharkSimHandler:
    
    """Handle OutputOperation objects"""
    def __enter__(self):

        def __init__(self):
            
            return None
            
        class SharkSimOperation: 
            '''Explicitly control all fundamental SharkSim operations'''

            def __init__(self):

                '''
                ------------------
                Initialise class specific variables
                ------------------
                '''                        
                self.objSSParametersLocal = None
                self.gen = 0
                self.pop = None
                #self.sim = simm
                self.listSSChooserParents = []
                self.bool_Abort_Processing_Gracefully = False
                
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
        
                ''' Get Debug Logger '''
                self.obj_Log_Debug_Display = logging__getLogger(globalsSS.Logger_Debug_Display.static_Logger_Name__Debug_Display)
        
                ''' Get Debug Timer '''
                #self.obj_Log_Debug_Timing = None
                #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                self.obj_Log_Debug_Timing = logging__getLogger(globalsSS.Logger_Debug_Timing.static_Logger_Name__Debug_Timing)
                #pass

                ''' Get Debug AgeNe Logger '''
                self.obj_Log_Debug_AgeNe = None
                if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                    self.obj_Log_Debug_AgeNe = logging__getLogger(globalsSS.Logger_Debug_AgeNe.static_Logger_Name__Debug_AgeNe)
                pass
                                        
                return True

           
            '''
            --------------------------------------------------------------------------------------------------------
            Simupop STATS
            --------------------------------------------------------------------------------------------------------
            '''

            '''@profile'''
            def method_SimStat_DemographicNe_Baseline_Reporting(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
                
                    if self.objSSParametersLocal.boolReportDemographicNe:
                        listVirtualSubPop = param
                        
                        if globalsSS.SP_SubPops.static_intSP_SubPop_Primary in listVirtualSubPop:
                            simupop.stat(pop, effectiveSize=self.objSSParametersLocal.listLociToReportNE, subPops=simupop.ALL_AVAIL, vars=['Ne_demo_base']),
                        
                        #SubPops with 0 popsize cause an error ie (0,3)
                        simupop.stat(pop, effectiveSize=self.objSSParametersLocal.listLociToReportNE, subPops=listVirtualSubPop, vars=['Ne_demo_base_sp']),                
                
                return True

            '''@profile'''
            def method_SimStat_TemporalNe_Baseline_Reporting(self, pop, param):
 
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
               
                    if self.objSSParametersLocal.boolReportTemporalFS_P1_Ne and self.objSSParametersLocal.boolReportTemporalFS_P2_Ne:
                        listVirtualSubPop = param
                        
                        if globalsSS.SP_SubPops.static_intSP_SubPop_Primary in listVirtualSubPop:
                            simupop.stat(pop, effectiveSize=self.objSSParametersLocal.listLociToReportNE, subPops=simupop.ALL_AVAIL, vars=['Ne_temporal_base']),
                        
                        #SubPops with 0 popsize cause an error ie (0,3)
                        simupop.stat(pop, effectiveSize=self.objSSParametersLocal.listLociToReportNE, subPops=listVirtualSubPop, vars=['Ne_temporal_base_sp']),                
                
                return True

            '''@profile'''
            def method_SimStat_DemographicNe_Reporting(self, pop, param):    
                            
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    if self.objSSParametersLocal.boolReportDemographicNe:
                        listVirtualSubPop = param
                        listLociToReportDemoNE = [0] 
                        
                        if globalsSS.SP_SubPops.static_intSP_SubPop_Primary in listVirtualSubPop:
                            simupop.stat(pop, effectiveSize=listLociToReportDemoNE, subPops=simupop.ALL_AVAIL, vars=['Ne_demo'])
                            
                        simupop.stat(pop, effectiveSize=listLociToReportDemoNE, subPops=listVirtualSubPop, vars=['Ne_demo_sp'])
                
                return True


            '''@profile'''
            def method_SimStat_LDNe_Reporting(self, pop, param):

#                 if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
#                     pass
#                 else:
                    
                if self.objSSParametersLocal.boolReportLDNe:
                    
                    listVirtualSubPop = param
                    
                    #DEBUG_ON
                    #self.methodOutput_outputPopulationDump(pop)
                    #Pause for testing
                    #raw_input('\n In method_SimStat_LDNe_Reporting - Press return to continue... \n')
                    #DEBUG_OFF

                    #listVirtualSubPop = [(0, 0)]
                    
                    intSP_Primary = globalsSS.SP_SubPops.static_intSP_SubPop_Primary
                    #if intSP_Primary in listVirtualSubPop:
                    #    simupop.stat(pop, effectiveSize=self.objSSParametersLocal.listLociToReportNE, subPops=[intSP_Primary], vars=['Ne_LD'])
                    #else:
                    simupop.stat(pop, effectiveSize=self.objSSParametersLocal.listLociToReportNE, subPops=listVirtualSubPop, vars=['Ne_LD_sp'])
                    
                    #self.method_Output_NE_Statistics(pop, param=[True, True, 0, (0,0), (0,1), (0,2)])
                    
                return True
            
#             '''@profile'''
#             def method_SimStat_LDNe_Reporting_2(self, pop_In, param):
# 
# #                 if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
# #                     pass
# #                 else:
#                     
#                 if self.objSSParametersLocal.boolReportLDNe:
#                     
#                     listVirtualSubPop = param
#                     
#                     #DEBUG_ON
#                     #self.methodOutput_outputPopulationDump(pop)
#                     #Pause for testing
#                     #raw_input('\n In method_SimStat_LDNe_Reporting - Press return to continue... \n')
#                     #DEBUG_OFF
# 
#                     #listVirtualSubPop = [(0, 0)]
#                     
#                     intSP_Primary = globalsSS.SP_SubPops.static_intSP_SubPop_Primary
#                     #if intSP_Primary in listVirtualSubPop:
#                     #    simupop.stat(pop, effectiveSize=self.objSSParametersLocal.listLociToReportNE, subPops=[intSP_Primary], vars=['Ne_LD'])
#                     
#                     simupop.stat(pop_In, effectiveSize=self.objSSParametersLocal.listLociToReportNE, subPops=listVirtualSubPop, vars=['Ne_LD_sp'])
#                     
#                     #self.method_Output_NE_Statistics(pop, param=[True, True, 0, (0,0), (0,1), (0,2)])
#                     
#                     pop_Out = pop_In
#                     
#                 return pop_Out
            
            '''@profile'''
            def method_SimStat_AlleleFreq_Reporting(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
                     
                    listVirtualSubPop = param
                    
                    #DEBUG_ON
                    #self.methodOutput_outputPopulationDump(pop)
                    #Pause for testing
                    #raw_input('\n In method_SimStat_LDNe_Reporting - Press return to continue... \n')
                    #DEBUG_OFF
    
                    #listVirtualSubPop = [(0, 0)]
                    
                    ##############  REPORT: Allele Freq Statistics
                    #sim.Stat(pop, alleleFreq=simupop.ALL_AVAIL, subPops=[(0,0), (0,1), (0,2), (0,3)]),
                    if globalsSS.SP_SubPops.static_intSP_SubPop_Primary in listVirtualSubPop:
                        simupop.stat(pop, alleleFreq=simupop.ALL_AVAIL, subPops=simupop.ALL_AVAIL, vars=['alleleFreq','alleleNum']),
                     
                    simupop.stat(pop, alleleFreq=simupop.ALL_AVAIL, subPops=listVirtualSubPop, vars=['alleleFreq_sp','alleleNum_sp']),
                    
                return True
            
            '''@profile'''
            def method_SimStat_HWE_Reporting(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
                     
                    listVirtualSubPop = param
                    
                    #DEBUG_ON
                    #self.methodOutput_outputPopulationDump(pop)
                    #Pause for testing
                    #raw_input('\n In method_SimStat_LDNe_Reporting - Press return to continue... \n')
                    #DEBUG_OFF
    
                    #listVirtualSubPop = [(0, 0)]
                    
                    ##############  REPORT: Allele Freq Statistics
                    #sim.Stat(pop, alleleFreq=simupop.ALL_AVAIL, subPops=[(0,0), (0,1), (0,2), (0,3)]),
                    if globalsSS.SP_SubPops.static_intSP_SubPop_Primary in listVirtualSubPop:
                        simupop.stat(pop, HWE=simupop.ALL_AVAIL, subPops=simupop.ALL_AVAIL, vars=['HWE']),
                     
                    simupop.stat(pop, HWE=simupop.ALL_AVAIL, subPops=listVirtualSubPop, vars=['HWE_sp']),
                    
                    for intVSP in listVirtualSubPop:
                        if intVSP == globalsSS.SP_SubPops.static_intSP_SubPop_Primary:
                            floatValue = pop.dvars(intVSP).HWE
                            self.obj_Log_Debug_Display.debug('SS Stats - Pop = ' + str(intVSP) + 'Stat - HWE = ' + str(floatValue) )
                        else:
                            floatValue = pop.dvars([globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVSP]).HWE
                            self.obj_Log_Debug_Display.debug('SS Stats - VSP = [' + str(globalsSS.SP_SubPops.static_intSP_SubPop_Primary) + ', ' + str(intVSP) + '] Stat - HWE = ' + str(floatValue) )
                    pass    
                        
                return True
            
            '''@profile'''
            def method_SimStat_TemporalFS_P1_Ne_Reporting(self, pop, param):
 
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
               
                    if self.objSSParametersLocal.boolReportTemporalFS_P1_Ne:
                        listVirtualSubPop = param
        
                        #SubPops with 0 pop cause an error ie (0,3)
                        
                        if globalsSS.SP_SubPops.static_intSP_SubPop_Primary in listVirtualSubPop:
                            simupop.stat(pop, effectiveSize=self.objSSParametersLocal.listLociToReportNE, vars=['Ne_tempoFS_P1'])
                            
                        simupop.stat(pop, effectiveSize=self.objSSParametersLocal.listLociToReportNE, subPops=listVirtualSubPop, vars=['Ne_tempoFS_P1_sp'])
                
                return True

            '''@profile'''
            def method_SimStat_TemporalFS_P2_Ne_Reporting(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
                
                    if self.objSSParametersLocal.boolReportTemporalFS_P2_Ne:
                        listVirtualSubPop = param
        
                        #SubPops with 0 pop cause an error ie (0,3)
                        
                        if globalsSS.SP_SubPops.static_intSP_SubPop_Primary in listVirtualSubPop:
                            simupop.stat(pop, effectiveSize=self.objSSParametersLocal.listLociToReportNE, vars=['Ne_tempoFS_P2'])
                            
                        simupop.stat(pop, effectiveSize=self.objSSParametersLocal.listLociToReportNE, subPops=listVirtualSubPop, vars=['Ne_tempoFS_P2_sp'])
                
                return True

            '''@profile'''
            def method_Output_NE_Statistics(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    if self.objSSParametersLocal.boolReportLDNe:
                        if self.objSSParametersLocal.listOutputDestinations_PopulationNEStatistics != []:
        
                            with SSOutputHandler() as SSOutputOperation:
                                #DEBUG ON
                                #listOutputDestinations_PopulationNEStatistics = ['console', outputFileName]
                                #listOutputDestinations_PopulationNEStatistics = ['console']
                                #param = 2
                                #DEBUG OFF
        
                                #intSubPop = 0
#                                 listVirtualSubPop = []
#                                 for i in range(2, len(param)):
#                                     listVirtualSubPop.append(param[i])
                                #listVirtualSubPop = [(0, 0)]
                                boolHeader= param[0]
                                boolFooter = param[1]
                                listVirtualSubPop = param[2]
                                listLDNePCritOutput = param[3]
                                boolPauseAfterOutput = param[4]
                                SSOutputOperation.method_Output_Sim_NE_Summary_Info(self, pop, boolHeader, boolFooter, self.objSSParametersLocal.listOutputDestinations_PopulationNEStatistics, listVirtualSubPop, listLDNePCritOutput)
                                
                                if boolPauseAfterOutput:
                                    SSOutputOperation.method_Pause_Console()
                                    
                return True

            def method_Calculate_And_Output_LDNE_To_Console(self, pop, listVSPsToReport, listLDNePCritOutput, listOutputDestinations, strPrefixMessage):

                with SSAnalysisHandler() as objSSAnalysisOperation:
                    #objOutput=sys.stdout
                    dictNeLD = objSSAnalysisOperation.method_Statistics_On_NE_LD_Population_Size_For_VirtualSubPop(pop, listVSPsToReport)
                   
                with SSOutputHandler() as objSSOutputOperation:
                    objSSOutputOperation.methodOutput_Output_LDNE_Info(listOutputDestinations, strPrefixMessage, False, False, dictNeLD, listLDNePCritOutput) 
#                     dictRounded = {}
#                     for listItem in listLDNePCritOutput:
#                         listRounded = []
#                         for i in range(0,3):
#                             listRounded.append(round(dictNeLD[listItem][i],2))
#                         pass
#                         dictRounded[listItem] = listRounded
# 
#                     objOutput.write('    LDNe: ' + str(dictRounded))
#                     objOutput.write('\n')
                
                return True
            
            def method_CountMatings(self, pop):
                
#                 if self.objSSParametersLocal.boolBurnIn:
#                     self.objSSParametersLocal.intCurrentBurnInFertilisation = self.objSSParametersLocal.intCurrentBurnInFertilisation + 1
#                 else:
#                     self.objSSParametersLocal.intCurrentFertilisation = self.objSSParametersLocal.intCurrentFertilisation + 1 
                
                self.objSSParametersLocal.intCurrentEvolveFertilisation = self.objSSParametersLocal.intCurrentEvolveFertilisation + 1 
                
                return True


            def method_InitGenotypes_ByLoci_ByVSP(self, pop, param):
                
                #listSubPopsToIndependentlyAssignGenotypesTo=param
 
                #for intVirtualSubPop in listSubPopsToIndependentlyAssignGenotypesTo:
                if self.objSSParametersLocal.intAlleleFrequencyScheme == globalsSS.Allele_Frequency_Distribution.static_int_Allele_Frequency_Distribution_Distribution__ALL_ALLELE_FREQUENCIES_FILE:
                    #Initialiase all loci with their own specific Allele frequencies
             
                    #Note the lowercase beginning to "initGenotype" as opposed to "InitGenotype"
                    # The latter will not work in an external function but the former WILL
                    #For further documenation see - SimuPop Documentation - Function form of operators
             
                    #sim.initGenotype(pop, freq=self.objSSParametersLocal.listAlleleFreqs[0], loci=0)
                    #sim.initGenotype(pop, freq=self.objSSParametersLocal.listAlleleFreqs[1], loci=1)
                    
                    initOps = []
                    for intLoci in range(0, self.objSSParametersLocal.nLoci):
                        initOps.append( 
                        simupop.initGenotype(pop,
                                              freq=self.objSSParametersLocal.listAlleleFreqs[intLoci],
                                              loci=intLoci)
                                       )
                    pass
#                 elif self.objSSParametersLocal.intAlleleFrequencyScheme == globalsSS.Allele_Frequency_Distribution.static_int_Allele_Frequency_Distribution_Distribution__DRICHLET:
#                     simupop.initGenotype(pop,
#                                           freq=self.objSSParametersLocal.listAlleleFreqs,
#                                           loci=simupop.ALL_AVAIL, subPops=[intVirtualSubPop])
     
                else: # default --> self.objSSParametersLocal.intAlleleFrequencyScheme == 0
                    #simupop.initGenotype(pop, freq=self.objSSParametersLocal.listAlleleFreqs, loci=simupop.ALL_AVAIL, subPops=[intVirtualSubPop])
     
                    self.method_Initialize_Allele_Frequencies(pop)
                    return True
    
            def method_InitGenotypes_RETIRE(self, pop_In):
                
                #listSubPopsToIndependentlyAssignGenotypesTo=param
 
                #for intVirtualSubPop in listSubPopsToIndependentlyAssignGenotypesTo:
                #if self.objSSParametersLocal.int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__UNIFORM:
                if self.objSSParametersLocal.intAlleleFrequencyScheme == 0:
                
                    #Initialiase all loci with their own specific Allele frequencies
             
                    #Note the lowercase beginning to "initGenotype" as opposed to "InitGenotype"
                    # The latter will not work in an external function but the former WILL
                    #For further documenation see - SimuPop Documentation - Function form of operators

                    for intLoci in range(0, self.objSSParametersLocal.nLoci):
                        simupop.initGenotype(pop_In,
                                              freq=self.objSSParametersLocal.listAlleleFreqs,
                                              loci=intLoci)
                    #
                    
                    #DEBUG_ON
                    #simupop.initGenotype(pop_In, freq=[0.5, 0.5])
                    #DEBUG_OFF
                    pass
     
                else:      
                    pop_In = self.method_Initialize_Allele_Frequencies(pop_In)
                pass
              
                pop_Out = pop_In
                    
                return pop_Out
            
            def method_InitGenotypes(self, pop_In):
                
                pop_Out = self.method_Initialize_Allele_Frequencies(pop_In)
              
                return pop_Out
    
            def method_Initialize_Allele_Frequencies_LESS(self, pop):
                
                startAlleles = 10
                numMSats = self.objSSParametersLocal.nLoci
                numSNPs = 0
                ###########
                maxAlleleN = self.objSSParametersLocal.nAllelesPerLoci
                
                loci = (numMSats+numSNPs)*[1]
                initOps = []
            
                for msat in range(numMSats):
                    diri = numpy__random.mtrand.dirichlet([1.0]*startAlleles)
                    if type(diri[0]) == float:
                        diriList = diri
                    else:
                        diriList = list(diri)
            
                    initOps.append(
                        simupop.initGenotype(pop,
                            freq = diriList,
                            loci=msat
                       )
                    )
                pass
            
                return True

            def method_Initialize_Allele_Frequencies_RETIRE(self, pop_In):
                
                startAlleles = self.objSSParametersLocal.nAllelesPerLoci
                numMSats = self.objSSParametersLocal.nLoci
                numSNPs = 0
                ###########
                maxAlleleN = self.objSSParametersLocal.nAllelesPerLoci
                
                loci = (numMSats+numSNPs)*[1]
                initOps = []
            
                for msat in range(numMSats):
                    diri = numpy__random.mtrand.dirichlet([1.0]*startAlleles)
                    if type(diri[0]) == float:
                        diriList = diri
                    else:
                        diriList = list(diri)
                    pass
#                     initOps.append(
#                         simupop.initGenotype(pop_In,
#                             freq = [0.0] * ((maxAlleleN+1-8)//2) +
#                                 diriList +
#                                 [0.0] * ((maxAlleleN+1-8)//2),
#                             loci=msat
#                        )
                    simupop.initGenotype(pop_In,
                        freq = [0.0] * ((maxAlleleN+1-8)//2) +
                            diriList +
                            [0.0] * ((maxAlleleN+1-8)//2),
                        loci=msat)
                    
                pop_Out = pop_In
                
                return pop_Out
            
            def method_Initialize_Allele_Frequencies_RETIRE2(self, pop_In):
                
                numMSats = self.objSSParametersLocal.nLoci
                int_Loci = self.objSSParametersLocal.nLoci
                
                bool_Allele_Number_Per_Locus_Is_Uniform = False
                int_Allele_Number_Per_Locus_Distribution = self.objSSParametersLocal.int_Allele_Number_Per_Locus_Distribution
                
#                 if str_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__UNIFORM:
#                     int_Alleles_Per_Locus = self.objSSParametersLocal.nAllelesPerLoci
#                     bool_Allele_Number_Per_Locus_Is_Uniform = True
#                 elif str_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__NORMAL:
#                     bool_Allele_Number_Per_Locus_Is_Uniform = False
#                 else:
#                     self.objSSParametersLocal.str_Alleles_Number_Per_Locus = globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__UNIFORM
#                     str_Allele_Number_Per_Locus_Distribution = self.objSSParametersLocal.str_Alleles_Number_Per_Locus
#                     bool_Allele_Number_Per_Locus_Is_Uniform = True
#                 pass
            
                if int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__UNIFORM:
                    int_Alleles_Per_Locus = self.objSSParametersLocal.int_Genome_UNIFORM_Number_Alleles_Per_Locus
                    bool_Allele_Number_Per_Locus_Is_Uniform = True
                elif int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__NORMAL:
                    bool_Allele_Number_Per_Locus_Is_Uniform = False
                    int_Alleles_Per_Locus__Mean = self.objSSParametersLocal.float_Genome_BINOMIAL_Mean_Number_Alleles_Per_Locus
                    int_Alleles_Per_Locus__StdDev = self.objSSParametersLocal.float_Genome_BINOMIAL_StdDev_Alleles_Per_Locus
#                     int_Alleles_Per_Locus__Mean = 14.92 #self.objSSParametersLocal.int_Alleles_Per_Locus__Mean
#                     int_Alleles_Per_Locus__StdDev = 9.25 #0.7 #self.objSSParametersLocal.int_Alleles_Per_Locus__StdDev
                    m, n, k = 1000,1,1, #self.objSSParametersLocal.int_Alleles_Per_Locus__Shape
                    int_Loci = m*n*k
                    with AnalysisHandler() as obj_Analysis:
                        list_Alleles_Per_Locus = obj_Analysis.method_Get_Distribution__NORMAL(int_Alleles_Per_Locus__Mean, int_Alleles_Per_Locus__StdDev, int_Loci)
                    pass
                elif int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__BINOMIAL:
                    bool_Allele_Number_Per_Locus_Is_Uniform = False
#                     int_Alleles_Per_Locus__Mean = 14.92 #self.objSSParametersLocal.int_Alleles_Per_Locus__Mean
#                     int_Alleles_Per_Locus__StdDev = 9.25 #0.7 #self.objSSParametersLocal.int_Alleles_Per_Locus__StdDev
#                     m, n, k = 10,1,1, #self.objSSParametersLocal.int_Alleles_Per_Locus__Shape
#                     int_Loci = numMSats #m*n*k
#                     m = numMSats
#                     p = 0.15
#                     mean = p*m
#                     variance = mean*(1-p)
                    #int_Alleles_Per_Locus__Mean, int_Alleles_Per_Locus__StdDev = self.objSSParametersLocal.tup_Allele_Number_Per_Locus_Distribution
                    int_Alleles_Per_Locus__Mean = self.objSSParametersLocal.float_Genome_BINOMIAL_Mean_Number_Alleles_Per_Locus
                    int_Alleles_Per_Locus__StdDev = self.objSSParametersLocal.float_Genome_BINOMIAL_StdDev_Alleles_Per_Locus
                    p = int_Alleles_Per_Locus__Mean / int_Loci
                    with AnalysisHandler() as obj_Analysis:
                        bool_Allow_Zeros = False
                        list_Alleles_Per_Locus = obj_Analysis.method_Get_Distribution__BINOMIAL(p, int_Loci, int_Loci, bool_Allow_Zeros)
                    pass
                else:
                    self.objSSParametersLocal.str_Alleles_Number_Per_Locus = globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__UNIFORM
                    int_Allele_Number_Per_Locus_Distribution = self.objSSParametersLocal.str_Alleles_Number_Per_Locus
                    bool_Allele_Number_Per_Locus_Is_Uniform = True
                pass                    
                
                numMSats = self.objSSParametersLocal.nLoci
                numSNPs = 0
                ###########
                #maxAlleleN = self.objSSParametersLocal.nAllelesPerLoci
                
            #     
            #     loci = (numMSats+numSNPs)*[1]
            #     initOps = []
                
                with AnalysisHandler() as obj_Analysis:
                    
                    for msat in range(numMSats):
                
                        if bool_Allele_Number_Per_Locus_Is_Uniform:
                            int_Alleles_Per_Locus = self.objSSParametersLocal.nAllelesPerLoci
                        else:
                            int_Alleles_Per_Locus = list_Alleles_Per_Locus[msat]
                        pass
                    
                        diri = numpy__random.mtrand.dirichlet([1.0]*int_Alleles_Per_Locus)
                
                        #print('msat: ' + str(msat) + '; diri: ' + str(str(diri)))
                        
                        if type(diri[0]) == float:
                            diriList = diri
                        else:
                            diriList = list(diri)
                        pass
                
                        #floatFreq = [0.0] * ((maxAlleleN+1-8)//2) + diriList + [0.0] * ((maxAlleleN+1-8)//2)
                        listFloatAlleleFreq = diriList
                        
                        #print('listFloatAlleleFreq: ' + str(listFloatAlleleFreq))
                        
                        simupop.initGenotype(pop_In, freq = listFloatAlleleFreq, loci=msat)
                        
                    pass
                pass
            
                #simupop.stat(pop_In, alleleFreq=simupop.ALL_AVAIL, subPops=simupop.ALL_AVAIL, vars=['alleleFreq','alleleNum'])
                #dict_Pop_Allele_Stats = pop_In.dvars().alleleFreq
                #print('dict_Pop_Allele_Stats : ' + str(dict_Pop_Allele_Stats))
                    
                pop_Out = pop_In
                
                return pop_Out
            
            def method_Initialize_Allele_Frequencies_RETIRE3(self, pop_In):
                
                numMSats = self.objSSParametersLocal.nLoci
                int_Loci = self.objSSParametersLocal.nLoci
                
                bool_Allele_Number_Per_Locus_Is_Uniform = False
                #int_Allele_Number_Per_Locus_Distribution = self.objSSParametersLocal.int_Allele_Number_Per_Locus_Distribution
                
#                 if str_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__UNIFORM:
#                     int_Alleles_Per_Locus = self.objSSParametersLocal.nAllelesPerLoci
#                     bool_Allele_Number_Per_Locus_Is_Uniform = True
#                 elif str_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__NORMAL:
#                     bool_Allele_Number_Per_Locus_Is_Uniform = False
#                 else:
#                     self.objSSParametersLocal.str_Alleles_Number_Per_Locus = globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__UNIFORM
#                     str_Allele_Number_Per_Locus_Distribution = self.objSSParametersLocal.str_Alleles_Number_Per_Locus
#                     bool_Allele_Number_Per_Locus_Is_Uniform = True
#                 pass
            
#                 if int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__UNIFORM:
#                     int_Alleles_Per_Locus = self.objSSParametersLocal.int_Genome_UNIFORM_Number_Alleles_Per_Locus
#                     bool_Allele_Number_Per_Locus_Is_Uniform = True
                if self.objSSParametersLocal.int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__NORMAL:
                    bool_Allele_Number_Per_Locus_Is_Uniform = False
                    int_Alleles_Per_Locus__Mean = self.objSSParametersLocal.float_Genome_BINOMIAL_Mean_Number_Alleles_Per_Locus
                    int_Alleles_Per_Locus__StdDev = self.objSSParametersLocal.float_Genome_BINOMIAL_StdDev_Alleles_Per_Locus
#                     int_Alleles_Per_Locus__Mean = 14.92 #self.objSSParametersLocal.int_Alleles_Per_Locus__Mean
#                     int_Alleles_Per_Locus__StdDev = 9.25 #0.7 #self.objSSParametersLocal.int_Alleles_Per_Locus__StdDev
                    m, n, k = 1000,1,1, #self.objSSParametersLocal.int_Alleles_Per_Locus__Shape
                    int_Loci = m*n*k
                    with AnalysisHandler() as obj_Analysis:
                        list_Alleles_Per_Locus = obj_Analysis.method_Get_Distribution__NORMAL(int_Alleles_Per_Locus__Mean, int_Alleles_Per_Locus__StdDev, int_Loci)
                    pass
                elif self.objSSParametersLocal.int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__BINOMIAL:
                    bool_Allele_Number_Per_Locus_Is_Uniform = False
#                     int_Alleles_Per_Locus__Mean = 14.92 #self.objSSParametersLocal.int_Alleles_Per_Locus__Mean
#                     int_Alleles_Per_Locus__StdDev = 9.25 #0.7 #self.objSSParametersLocal.int_Alleles_Per_Locus__StdDev
#                     m, n, k = 10,1,1, #self.objSSParametersLocal.int_Alleles_Per_Locus__Shape
#                     int_Loci = numMSats #m*n*k
#                     m = numMSats
#                     p = 0.15
#                     mean = p*m
#                     variance = mean*(1-p)
                    #int_Alleles_Per_Locus__Mean, int_Alleles_Per_Locus__StdDev = self.objSSParametersLocal.tup_Allele_Number_Per_Locus_Distribution
                    int_Alleles_Per_Locus__Mean = self.objSSParametersLocal.float_Genome_BINOMIAL_Mean_Number_Alleles_Per_Locus
                    int_Alleles_Per_Locus__StdDev = self.objSSParametersLocal.float_Genome_BINOMIAL_StdDev_Alleles_Per_Locus
                    p = 1-(float(int_Alleles_Per_Locus__StdDev)/ float(int_Alleles_Per_Locus__Mean))
                    #p = int_Alleles_Per_Locus__Mean / int_Loci
                    n = float(int_Alleles_Per_Locus__Mean)/p
                    with AnalysisHandler() as obj_Analysis:
                        bool_Allow_Zeros = False
                        #list_Alleles_Per_Locus = obj_Analysis.method_Get_Distribution__BINOMIAL(p, int_Loci, int_Loci, bool_Allow_Zeros)
                        list_Alleles_Per_Locus = obj_Analysis.method_Get_Distribution__BINOMIAL(p, n, int_Loci, bool_Allow_Zeros)
                    pass
                else:
                    self.objSSParametersLocal.str_Alleles_Number_Per_Locus = globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__UNIFORM
                    self.objSSParametersLocal.int_Allele_Number_Per_Locus_Distribution = self.objSSParametersLocal.str_Alleles_Number_Per_Locus
                    bool_Allele_Number_Per_Locus_Is_Uniform = True
                pass                    
                
                numMSats = self.objSSParametersLocal.nLoci
                numSNPs = 0
                ###########
                #maxAlleleN = self.objSSParametersLocal.nAllelesPerLoci
                
            #     
            #     loci = (numMSats+numSNPs)*[1]
            #     initOps = []

                if self.objSSParametersLocal.int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__BINOMIAL:
                   
                    if self.objSSParametersLocal.intAlleleFrequencyScheme == globalsSS.Allele_Frequency_Distribution.static_int_Allele_Frequency_Distribution_Distribution__DRICHLET:
                
                        with AnalysisHandler() as obj_Analysis:
                            
                            listFloatAlleleFreqs = []
                            
                            for msat in range(numMSats):
                    
                                int_Alleles_Per_Locus = list_Alleles_Per_Locus[msat]
        
                                diri = numpy__random.mtrand.dirichlet([1.0]*int_Alleles_Per_Locus)
                        
                                #print('msat: ' + str(msat) + '; diri: ' + str(str(diri)))
                                
                                if type(diri[0]) == float:
                                    diriList = diri
                                else:
                                    diriList = list(diri)
                                pass
                        
                                #floatFreq = [0.0] * ((maxAlleleN+1-8)//2) + diriList + [0.0] * ((maxAlleleN+1-8)//2)
                                listFloatAlleleFreq = diriList
                                pass
                            
                                #print('listFloatAlleleFreq: ' + str(listFloatAlleleFreq))
                                
                                simupop.initGenotype(pop_In, freq = listFloatAlleleFreq, loci=msat) 
                                
                                #DEBUG_ON
                                listFloatAlleleFreqs.append(listFloatAlleleFreq[0]) 
                                #DEBUG_OFF                          
                            pass
                        pass
                    else:
                        #DEBUG_ON
                        list_Alleles_Per_Locus_Check = list(list_Alleles_Per_Locus)
                        #DEBUG_OFF
                        odict_Counter = OrderedDict(collections__Counter(list_Alleles_Per_Locus))
                        list_Alleles_Type_Count = odict_Counter.values()
                        listFloatAlleleFreq = [int_Alleles_Per_Locus / float(numMSats) for int_Alleles_Per_Locus in list_Alleles_Type_Count]                               
                        
                        #print('listFloatAlleleFreq: ' + str(listFloatAlleleFreq))

                        for intLoci in range(0, self.objSSParametersLocal.nLoci):
                            simupop.initGenotype(pop_In,
                                                  freq=listFloatAlleleFreq,
                                                  loci=intLoci)    
                                                
                        #simupop.initGenotype(pop_In, freq = listFloatAlleleFreq, loci=numMSats)                        
                    pass
                pass
            
                #simupop.stat(pop_In, alleleFreq=simupop.ALL_AVAIL, subPops=simupop.ALL_AVAIL, vars=['alleleFreq','alleleNum'])
                #dict_Pop_Allele_Stats = pop_In.dvars().alleleFreq
                #print('dict_Pop_Allele_Stats : ' + str(dict_Pop_Allele_Stats))
                    
                pop_Out = pop_In
                
                return pop_Out

            def method_Initialize_Allele_Frequencies(self, pop_In):
                
                int_Loci = self.objSSParametersLocal.nLoci

                if self.objSSParametersLocal.int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__UNIFORM and \
                   self.objSSParametersLocal.intAlleleFrequencyScheme == globalsSS.Allele_Frequency_Distribution.static_int_Allele_Frequency_Distribution_Distribution__NON_RANDOM:    
                        '''
                        ------------------
                        Alleles per locus scheme: UNIFORM locus per alleles distribution
                        +
                        Allele Freq Scheme: NON-Randomly generated allele frequencies
                        ------------------
                        '''

                        int_Alleles_Per_Locus = self.objSSParametersLocal.int_Alleles_Per_Locus                            
                          
                        pop_Out = self.method_Initialize_Allele_Frequencies__UNIFORM_And_NON_RANDOM(pop_In, int_Loci, int_Alleles_Per_Locus)
                        
                        pass                        
                elif self.objSSParametersLocal.int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__UNIFORM and \
                     self.objSSParametersLocal.intAlleleFrequencyScheme == globalsSS.Allele_Frequency_Distribution.static_int_Allele_Frequency_Distribution_Distribution__DRICHLET:
                        '''
                        ------------------
                        Alleles per locus scheme: UNIFORM locus per alleles distribution
                        +
                        Allele Freq Scheme: NON-Randomly generated allele frequencies
                        ------------------
                        '''
                        int_Alleles_Per_Locus = self.objSSParametersLocal.int_Alleles_Per_Locus                            
                           
                        pop_Out = self.method_Initialize_Allele_Frequencies__UNIFORM_And_DIRICHLET_RANDOM(pop_In, int_Loci, int_Alleles_Per_Locus)
                        
                        pass                        
                elif self.objSSParametersLocal.int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__BINOMIAL and \
                     self.objSSParametersLocal.intAlleleFrequencyScheme == globalsSS.Allele_Frequency_Distribution.static_int_Allele_Frequency_Distribution_Distribution__NON_RANDOM:
                        '''
                        ------------------
                        Alleles per locus scheme: BINOMIAL locus per alleles distribution
                        +
                        Allele Freq Scheme: NON_RANDOM Randomly generated allele frequencies
                        ------------------
                        '''

                        float_Alleles_Per_Locus__Mean = self.objSSParametersLocal.float_Genome_BINOMIAL_Mean_Number_Alleles_Per_Locus
                        float_Alleles_Per_Locus__StdDev = self.objSSParametersLocal.float_Genome_BINOMIAL_StdDev_Alleles_Per_Locus
                        
                        pop_Out = self.method_Initialize_Allele_Frequencies__BINOMIAL_And_NON_RANDOM(pop_In, int_Loci, float_Alleles_Per_Locus__Mean, float_Alleles_Per_Locus__StdDev)
                        
                        pass
                elif self.objSSParametersLocal.int_Allele_Number_Per_Locus_Distribution == globalsSS.Allele_Number_Per_Locus_Distribution.static_int_Allele_Number_Per_Locus_Distribution__BINOMIAL and \
                     self.objSSParametersLocal.intAlleleFrequencyScheme == globalsSS.Allele_Frequency_Distribution.static_int_Allele_Frequency_Distribution_Distribution__DRICHLET:
                        '''
                        ------------------
                        Alleles per locus scheme: BINOMIAL locus per alleles distribution
                        +
                        Allele Freq Scheme: DIRICHLET Randomly generated allele frequencies
                        ------------------
                        '''  
                    
                        float_Alleles_Per_Locus__Mean = self.objSSParametersLocal.float_Genome_BINOMIAL_Mean_Number_Alleles_Per_Locus
                        float_Alleles_Per_Locus__StdDev = self.objSSParametersLocal.float_Genome_BINOMIAL_StdDev_Alleles_Per_Locus
                        
                        pop_Out = self.method_Initialize_Allele_Frequencies__BINOMIAL_And_DIRICHLET_RANDOM(pop_In, int_Loci, float_Alleles_Per_Locus__Mean, float_Alleles_Per_Locus__StdDev)
                    
                else:
                    '''
                    ------------------
                    Alleles per locus scheme: UNIFORM locus per alleles distribution
                    +
                    Allele Freq Scheme: NON-Randomly generated allele frequencies
                    ------------------
                    '''

                    int_Alleles_Per_Locus = self.objSSParametersLocal.int_Alleles_Per_Locus                            
                       
                    pop_Out = self.method_Initialize_Allele_Frequencies__UNIFORM_AND_NON_RANDOM(pop_In, int_Loci, int_Alleles_Per_Locus)
                    
                    pass                        
                pass
                
                return pop_Out


            def method_Initialize_Allele_Frequencies__BINOMIAL_And_DIRICHLET_RANDOM(self, pop_In, int_Loci, float_Alleles_Per_Locus__Mean, float_Alleles_Per_Locus__StdDev):

                '''
                ------------------
                Alleles per locus scheme: BINOMIAL locus per alleles distribution
                +
                Allele Freq Scheme: DIRICHLET RANDOM generated allele frequencies
                ------------------
                '''          
                ''' Create list of alleles per locus ''' 
                p = 1-(float(float_Alleles_Per_Locus__StdDev)/ float(float_Alleles_Per_Locus__Mean))
                n = float(float_Alleles_Per_Locus__Mean)/p
                bool_Allow_Zeros = False
                
                with AnalysisHandler() as obj_Analysis:
                    
                    list_Alleles_Per_Locus = obj_Analysis.method_Get_Distribution__BINOMIAL(p, n, int_Loci, bool_Allow_Zeros)
                    
                pass

                listFloatAlleleFreqs = []
                ''' Process locus by locus for all loci'''
                for int_Locus in range(int_Loci):
        
                    ''' Get alleles per locus for each locus '''
                    int_Alleles_Per_Locus = list_Alleles_Per_Locus[int_Locus]

                    '''
                    Get a numpy array of DRICHLET RANDOM allele frequencies adding up to 1
                    given the number of alleles requested for this locus
                    '''
                    nparray_Random_Allele_Frequencies__Drichlet = numpy__random.mtrand.dirichlet([1.0]*int_Alleles_Per_Locus)
            
                    #print('msat: ' + str(msat) + '; nparray_Random_Allele_Frequencies__Drichlet: ' + str(str(nparray_Random_Allele_Frequencies__Drichlet)))
                    
                    ''' Change type from numpy array to list if integers '''
                    if type(nparray_Random_Allele_Frequencies__Drichlet[0]) == float:
                        nparray_Random_Allele_Frequencies__Drichlet_LIST = nparray_Random_Allele_Frequencies__Drichlet
                    else:
                        nparray_Random_Allele_Frequencies__Drichlet_LIST = list(nparray_Random_Allele_Frequencies__Drichlet)
                    pass
            
                    #floatFreq = [0.0] * ((maxAlleleN+1-8)//2) + diriList + [0.0] * ((maxAlleleN+1-8)//2)
                    list_Allele_Frequencies_For_Locus = nparray_Random_Allele_Frequencies__Drichlet_LIST
                    pass
                
                    #print('list_Allele_Freq: ' + str(list_Allele_Freq))
                    
                    ''' Assign allele frequencies by FREQUENCY to all individuals  '''
                    simupop.initGenotype(pop_In, freq = list_Allele_Frequencies_For_Locus, loci=int_Locus) 
                    
                    #DEBUG_ON
                    #listFloatAlleleFreqs.append(list_Allele_Frequencies_For_Locus) 
                    #DEBUG_OFF                          
                pass
                
                pop_Out = pop_In
                    
                return pop_Out

            def method_Initialize_Allele_Frequencies__UNIFORM_And_DIRICHLET_RANDOM(self, pop_In, int_Loci, int_Alleles_Per_Locus):

                '''
                ------------------
                Alleles per locus scheme: UNIFORM locus per alleles distribution
                +
                Allele Freq Scheme: DIRICHLET RANDOM generated allele frequencies
                ------------------
                '''          
                ''' Create list of alleles per locus '''     
                list_Alleles_Per_Locus = [int_Alleles_Per_Locus] * int_Loci
                
                listFloatAlleleFreqs = []
                ''' Process locus by locus for all loci'''
                for int_Locus in range(int_Loci):
        
                    ''' Get alleles per locus for each locus '''
                    int_Alleles_Per_Locus = list_Alleles_Per_Locus[int_Locus]

                    '''
                    Get a numpy array of DRICHLET RANDOM allele frequencies adding up to 1
                    given the number of alleles requested for this locus
                    '''
                    nparray_Random_Allele_Frequencies__Drichlet = numpy__random.mtrand.dirichlet([1.0]*int_Alleles_Per_Locus)
            
                    ''' Change type from numpy array to list if integers '''
                    if type(nparray_Random_Allele_Frequencies__Drichlet[0]) == float:
                        nparray_Random_Allele_Frequencies__Drichlet_LIST = nparray_Random_Allele_Frequencies__Drichlet
                    else:
                        nparray_Random_Allele_Frequencies__Drichlet_LIST = list(nparray_Random_Allele_Frequencies__Drichlet)
                    pass
            
                    list_Allele_Frequencies_For_Locus = nparray_Random_Allele_Frequencies__Drichlet_LIST
                    pass
                    
                    ''' Assign allele frequencies by FREQUENCY to all individuals  '''
                    simupop.initGenotype(pop_In, freq = list_Allele_Frequencies_For_Locus, loci=int_Locus) 
                    
                    #DEBUG_ON
                    #listFloatAlleleFreqs.append(list_Allele_Frequencies_For_Locus) 
                    #DEBUG_OFF                          
                pass
                
                pop_Out = pop_In
                    
                return pop_Out
            
            def method_Initialize_Allele_Frequencies__BINOMIAL_And_NON_RANDOM(self, pop_In, int_Loci, float_Alleles_Per_Locus__Mean, float_Alleles_Per_Locus__StdDev):

                '''
                ------------------
                Alleles per locus scheme: BINOMIAL locus per alleles distribution
                +
                Allele Freq Scheme: NON-Randomly generated allele frequencies
                ------------------
                '''                
                
                p = 1-(float(float_Alleles_Per_Locus__StdDev)/ float(float_Alleles_Per_Locus__Mean))
                n = float(float_Alleles_Per_Locus__Mean)/p
                bool_Allow_Zeros = False
                
                with AnalysisHandler() as obj_Analysis:
                    
                    list_Alleles_Per_Locus = obj_Analysis.method_Get_Distribution__BINOMIAL(p, n, int_Loci, bool_Allow_Zeros)
                    
                pass
                        
                '''
                Assign allele frequencies by FREQUENCY to all individuals 
                '''

                #DEBUG_ON
                #list_Alleles_Per_Locus_Check = list(list_Alleles_Per_Locus)
                #DEBUG_OFF
                
                '''
                Convert BINOMIAL array of alleles per locus to allele frequencies for each locus
                '''
                odict_Counter = OrderedDict(collections__Counter(list_Alleles_Per_Locus))
                list_Allele_Types_Count = odict_Counter.values()
                list_Allele_Frequencies_For_Locus = [int_Alleles_Per_Locus / float(int_Loci) for int_Alleles_Per_Locus in list_Allele_Types_Count]                               
                
    
                for int_Locus in range(0, int_Loci):

                    simupop.initGenotype(pop_In, freq=list_Allele_Frequencies_For_Locus, loci=int_Locus)
                    
                pass
     
                pop_Out = pop_In
                    
                return pop_Out
                        
            def method_Initialize_Allele_Frequencies__UNIFORM_And_NON_RANDOM(self, pop_In, int_Loci, int_Alleles_Per_Locus):

                '''
                ------------------
                Alleles per locus scheme: UNIFORM locus per alleles distribution
                +
                Allele Freq Scheme: NON-Randomly generated allele frequencies
                ------------------
                '''                
                list_Allele_Frequencies_Per_Locus = [1 / float(int_Alleles_Per_Locus)] * int_Alleles_Per_Locus
                                         
                '''
                Assign allele frequencies by FREQUENCY to all individuals 
                 
                Note the lowercase beginning to "initGenotype" as opposed to "InitGenotype"
                 The latter will not work in an external function but the former WILL
                For further documenation see - SimuPop Documentation - Function form of operators
                '''
            
                for int_Locus in range(0, int_Loci):

                    #DEBUG_ON
                    #simupop.initGenotype(pop_In, freq=[0.5, 0.5])
                    #DEBUG_OFF
                                    
                    simupop.initGenotype(pop_In, freq=list_Allele_Frequencies_Per_Locus, loci=int_Locus)
                    
                pass
     
                pop_Out = pop_In
                    
                return pop_Out
           
           
                        
            def method_Initialize_Allele_Frequencies_PREV(self, pop_In):
                
                startAlleles = self.objSSParametersLocal.nAllelesPerLoci
                numMSats = self.objSSParametersLocal.nLoci
                numSNPs = 0
                ###########
                #maxAlleleN = self.objSSParametersLocal.nAllelesPerLoci
                
            #     
            #     loci = (numMSats+numSNPs)*[1]
            #     initOps = []
            
                for msat in range(numMSats):
            
                    diri = numpy__random.mtrand.dirichlet([1.0]*startAlleles)
            
                    #print('msat: ' + str(msat) + '; diri: ' + str(str(diri)))
                    
                    if type(diri[0]) == float:
                        diriList = diri
                    else:
                        diriList = list(diri)
                    pass
            
                    #floatFreq = [0.0] * ((maxAlleleN+1-8)//2) + diriList + [0.0] * ((maxAlleleN+1-8)//2)
                    listFloatAlleleFreq = diriList
                    
                    #print('listFloatAlleleFreq: ' + str(listFloatAlleleFreq))
                    
                    simupop.initGenotype(pop_In, freq = listFloatAlleleFreq, loci=msat)
                    
                pass
            
                #simupop.stat(pop_In, alleleFreq=simupop.ALL_AVAIL, subPops=simupop.ALL_AVAIL, vars=['alleleFreq','alleleNum'])
                #dict_Pop_Allele_Stats = pop_In.dvars().alleleFreq
                #print('dict_Pop_Allele_Stats : ' + str(dict_Pop_Allele_Stats))
                    
                pop_Out = pop_In
                
                return pop_Out

            def method_InitGenotypes_ByLoci(self, pop_In):
                
                
                if self.objSSParametersLocal.intAlleleFrequencyScheme == globalsSS.Allele_Frequency_Distribution.static_int_Allele_Frequency_Distribution_Distribution__ALL_ALLELE_FREQUENCIES_FILE:
                    #Initialiase all loci with their own specific Allele frequencies
                
                    #Note the lowercase beginning to "initGenotype" as opposed to "InitGenotype"
                    # The latter will not work in an external function but the former WILL
                    #For further documenation see - SimuPop Documentation - Function form of operators
                
                    #simupop.initGenotype(pop, freq=self.objSSParametersLocal.listAlleleFreqs[0], loci=0)
                    #simupop.initGenotype(pop, freq=self.objSSParametersLocal.listAlleleFreqs[1], loci=1)

                    for intLoci in range(0, self.objSSParametersLocal.nLoci):
                        simupop.initGenotype(pop_In, freq=self.objSSParametersLocal.listAlleleFreqs[intLoci], loci=intLoci)
                    pass
                elif self.objSSParametersLocal.intAlleleFrequencyScheme == globalsSS.Allele_Frequency_Distribution.static_int_Allele_Frequency_Distribution_Distribution__GENEPOP_FILE:

                    for intLoci in range(0, self.objSSParametersLocal.nLoci):
                        simupop.initGenotype(pop_In, freq=self.objSSParametersLocal.listAlleleFreqs[intLoci], loci=intLoci)
                    pass
                elif self.objSSParametersLocal.intAlleleFrequencyScheme == globalsSS.Allele_Frequency_Distribution.static_int_Allele_Frequency_Distribution_Distribution__DRICHLET:
                    simupop.initGenotype(pop_In, freq=self.objSSParametersLocal.listAlleleFreqs, loci=simupop.ALL_AVAIL)

                else: # default --> self.objSSParametersLocal.intAlleleFrequencyScheme == 0
                    simupop.initGenotype(pop_In, freq=self.objSSParametersLocal.listAlleleFreqs, loci=simupop.ALL_AVAIL)
                pass
            
                pop_Out = pop_In
                
                return pop_Out

            '''
            --------------------------------------------------------------------------------------------------------
            VSP Splits
            --------------------------------------------------------------------------------------------------------
            '''
           
            def method_SplitRandomSampleIntoVSP(self, pop_In, listRanges):
                
                
                pop_In.setVirtualSplitter(simupop.RangeSplitter(
                                            ranges=listRanges),
                                                    )
                                                              
                #DEBUG_ON
                #self.methodOutput_outputPopulationDump(pop_In)
                #Pause for testing
                #input('\n After INITIAL method_SplitLifeStagesIntoVSPs_By_AgeInMonths_AndThen_GestationMonth - Press return to continue... \n')
                #DEBUG_OFF
                
                pop_Out = pop_In
                
                return pop_Out
            
            def method_SplitLifeStagesIntoVSPs_By_AgeInYears(self, pop_In):
                
                
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # Define the ages in each virtual subpopulation
                # 
                # Neonate                       - (0,0) = age < maxNeonateAge - 0.1
                # Juvenile                      - (0,1) = age < maxJuvenileAge - 0.1
                # Sub-adult                     - (0,2) = age < minSubAdultAge - 0.1
                # Reproductively mature
                # adults (inc. resting females) - (0.3) = age >= minMatingAge and age =< maxMatingAge - 0.1  [age < maxMatingAge]
                # Gestating Females             - (0,4) = boolReproductiveAge and boolGestating and not boolResting [age < maxMatingAge + boolGestating]
                # Senescent adults              - (0,5) = age >= maxMatingAge and age =< maxAge - 0.1        [maxMatingAge < age < maxAge]
                # Mort                          - (0,6) = age >= maxAge                                      [age > maxAge] DIED! So should always be Zero
                
                pop_In.setVirtualSplitter(simupop.InfoSplitter('age',
                    cutoff=[self.objSSParametersLocal.minMatingAge - 0.1, # (0,0)
                            self.objSSParametersLocal.maxMatingAge - 0.1, # (0,1)
                            self.objSSParametersLocal.maxAge - 0.1]))     # (0,2)
                
                #DEBUG_ON
                # Output the summary of  age class totals(virtualSubPops) at each generation
                #self.methodOutput_outputPopulationAgeClassTotals(self.pop)
                
                # Output a population dump every generation
                #self.methodOutput_outputPopulationDump(self.pop)

                #DEBUG_OFF

                #self.pop.removeSubPops([(0, 3)])
                
                pop_Out = pop_In
                
                return pop_Out

#            def method_SplitLifeStagesIntoVSPs_By_AgeInMonths_ORIG(self, boolDisplayOnly):
                
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # Define the age classes in each virtual subpopulation
                # 
                # Neonate                         - (0,0) = age < maxNeonateAge - 0.1
                # Reproductively available adults - (0,1) = age >= minMatingAge and age =< maxMatingAge - 0.1  [age < maxMatingAge]
                # Senescent adults                - (0,2) = age >= maxMatingAge and age =< maxAge - 0.1        [maxMatingAge < age < maxAge]
                # Died old age                    - (0,3) = age >= maxAge                                      [age > maxAge] DIED! So should always be Zero
                
#                 self.pop.setVirtualSplitter(simupop.InfoSplitter('age_in_months',
#                     cutoff=[
#                             #(self.objSSParametersLocal.minMatingAge*self.objSSParametersLocal.intParturationSeasonIntervalInMonths)-0.1,  # (0,0)
#                             self.objSSParametersLocal.minMatingAge*self.objSSParametersLocal.intParturationSeasonIntervalInMonths,  # (0,0)
#                             self.objSSParametersLocal.maxMatingAge*self.objSSParametersLocal.intParturationSeasonIntervalInMonths,  # (0,1)
#                             self.objSSParametersLocal.maxAge*self.objSSParametersLocal.intParturationSeasonIntervalInMonths
#                             ],         # (0,2)
#                     names=[
#                             static_stringMediumNameVSP_AgeClass_Neonate,
#                             static_stringMediumNameVSP_AgeClass_Reproductivly_available_adult,
#                             static_stringMediumNameVSP_AgeClass_Senescent_adult,
#                             static_stringMediumNameVSP_AgeClass_Died_Old_Age
#                             ]))     
#                  
#                 if boolDisplayOnly == False:
#                     #Update age_class indicator
#                     self.pop.setIndInfo(static_intVSP_AgeClass_Neonate, 'age_class', subPop=(0,0))
#                     self.pop.setIndInfo(static_intVSP_AgeClass_Reproductivly_available_adult, 'age_class', subPop=(0,1))
#                     self.pop.setIndInfo(static_intVSP_AgeClass_Senescent_adult, 'age_class', subPop=(0,2))
#                     self.pop.setIndInfo(static_intVSP_AgeClass_Died, 'age_class', subPop=(0,3))

#                 self.method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(globalsSS.SP_SubPops.static_intSP_SubPop_Primary,
#                                                                                  boolUpdateInfoField=True,
#                                                                                  stringVSPSplitOperator = 'cutoff',
#                                                                                  stringInfoFieldToSplitBy = 'age_in_months',
#                                                                                  listVSPSplitValues = [ 
#                                                                                                         self.objSSParametersLocal.intGestationLengthInMonths,
#                                                                                                         self.objSSParametersLocal.minMatingAge*self.objSSParametersLocal.intParturationSeasonIntervalInMonths,
#                                                                                                         self.objSSParametersLocal.maxMatingAge*self.objSSParametersLocal.intParturationSeasonIntervalInMonths,
#                                                                                                         self.objSSParametersLocal.maxAge*self.objSSParametersLocal.intParturationSeasonIntervalInMonths
#                                                                                                         ],
#                                                                                  listVSPSplitNames = [
#                                                                                                         globalsSS.VSP_AgeClass.static_stringShortNameVSP_AgeClass_Embryo + '_' + globalsSS.VSP_AgeClass.static_stringMediumNameVSP_AgeClass_Embryo,
#                                                                                                         globalsSS.VSP_AgeClass.static_stringShortNameVSP_AgeClass_Neonate + '_' + globalsSS.VSP_AgeClass.static_stringMediumNameVSP_AgeClass_Neonate,
#                                                                                                         globalsSS.VSP_AgeClass.static_stringShortNameVSP_AgeClass_Reproductivly_available_adult + '_' + globalsSS.VSP_AgeClass.static_stringMediumNameVSP_AgeClass_Reproductivly_available_adult,
#                                                                                                         globalsSS.VSP_AgeClass.static_stringShortNameVSP_AgeClass_Senescent_adult + '_' + globalsSS.VSP_AgeClass.static_stringMediumNameVSP_AgeClass_Senescent_adult,
#                                                                                                         globalsSS.VSP_AgeClass.static_stringShortNameVSP_AgeClass_Died_Old_Age + '_' + globalsSS.VSP_AgeClass.static_stringMediumNameVSP_AgeClass_Died_Old_Age
#                                                                                                         ],
#                                                                                  stringInfoFieldToUpdate = 'age_class',
#                                                                                  listVSPsToUpdate = [
#                                                                                                         globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo,
#                                                                                                         globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Neonate,
#                                                                                                         globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult,
#                                                                                                         globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Senescent_adult,
#                                                                                                         globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Died
#                                                                                                         ],
#                                                                                  listUpdateValues = [
#                                                                                                         globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo,
#                                                                                                         globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Neonate,
#                                                                                                         globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult,
#                                                                                                         globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Senescent_adult,
#                                                                                                         globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Died
#                                                                                                         ])

           
            def method_SplitLifeStagesInto_AgeInMonths_VSPs_By_AgeInMonths(self, pop_In):
                 
                pop_Out = self.method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary,
                                                                                 boolUpdateInfoField=True,
                                                                                 stringVSPSplitOperator = 'cutoff',
                                                                                 stringInfoFieldToSplitBy = 'age_in_months',
                                                                                 listVSPSplitValues = [ 
                                                                                                        (intAgeInYears) for intAgeInYears in range(0, self.objSSParametersLocal.maxAge*12, 1)
                                                                                                        ],
                                                                                 listVSPSplitNames = [],
                                                                                 stringInfoFieldToUpdate = '',
                                                                                 listVSPsToUpdate = [],
                                                                                 listUpdateValues = [])

                return pop_Out
            
            def method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(self, pop_In, boolUpdate):
                
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # Define the age classes in each virtual subpopulation
                # 
                # Neonate                         - (0,0) = age < maxNeonateAge - 0.1
                # Reproductively available adults - (0,1) = age >= minMatingAge and age =< maxMatingAge - 0.1  [age < maxMatingAge]
                # Senescent adults                - (0,2) = age >= maxMatingAge and age =< maxAge - 0.1        [maxMatingAge < age < maxAge]
                # Died old age                    - (0,3) = age >= maxAge                                      [age > maxAge] DIED! So should always be Zero
                
                #self.method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(self.pop, globalsSS.SP_SubPops.static_intSP_SubPop_Primary,
                pop_Out = self.method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary,
                                                                                 boolUpdateInfoField=boolUpdate,
                                                                                 stringVSPSplitOperator = 'cutoff',
                                                                                 stringInfoFieldToSplitBy = 'age_in_months',
                                                                                 listVSPSplitValues = [ 
                                                                                                        self.objSSParametersLocal.intGestationLengthInMonths,
                                                                                                        (self.objSSParametersLocal.minMatingAge*12),
                                                                                                        (self.objSSParametersLocal.maxMatingAge*12),
                                                                                                        (self.objSSParametersLocal.maxAge*12)
                                                                                                        ],
                                                                                 listVSPSplitNames = [
#                                                                                                         globalsSS.VSP_AgeClass.static_stringShortNameVSP_AgeClass_Embryo + '_' + globalsSS.VSP_AgeClass.static_stringMediumNameVSP_AgeClass_Embryo,
#                                                                                                         globalsSS.VSP_AgeClass.static_stringShortNameVSP_AgeClass_Neonate + '_' + globalsSS.VSP_AgeClass.static_stringMediumNameVSP_AgeClass_Neonate,
#                                                                                                         globalsSS.VSP_AgeClass.static_stringShortNameVSP_AgeClass_Reproductivly_available_adult + '_' + globalsSS.VSP_AgeClass.static_stringMediumNameVSP_AgeClass_Reproductivly_available_adult,
#                                                                                                         globalsSS.VSP_AgeClass.static_stringShortNameVSP_AgeClass_Senescent_adult + '_' + globalsSS.VSP_AgeClass.static_stringMediumNameVSP_AgeClass_Senescent_adult,
#                                                                                                         globalsSS.VSP_AgeClass.static_stringShortNameVSP_AgeClass_Died + '_' + globalsSS.VSP_AgeClass.static_stringMediumNameVSP_AgeClass_Died
                                                                                                        globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Embryo
                                                                                                        #,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Neonate
                                                                                                        ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Juvenile
                                                                                                        ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult
                                                                                                        ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Senescent_adult
                                                                                                        ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Died
                                                                                                        ],
                                                                                 stringInfoFieldToUpdate = 'age_class',
                                                                                 listVSPsToUpdate = [
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo,
                                                                                                        #globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Neonate,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Juvenile,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Senescent_adult,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Died
                                                                                                        ],
                                                                                 listUpdateValues = [
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo,
                                                                                                        #globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Neonate,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Juvenile,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Senescent_adult,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Died
                                                                                                        ])
                return pop_Out
            
            def method_SplitLifeStagesIntoVSPs_By_AgeClass(self, pop_In):
                
                pop_Out = self.method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary,
                                                                                 boolUpdateInfoField=False,
                                                                                 stringVSPSplitOperator = 'values',
                                                                                 stringInfoFieldToSplitBy = 'age_class',
                                                                                 listVSPSplitValues = [ 
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo,
                                                                                                        #globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Neonate,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Juvenile,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Senescent_adult,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Died
                                                                                                        ],
                                                                                 listVSPSplitNames = [
                                                                                                        globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Embryo
                                                                                                        #,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Neonate
                                                                                                        ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Juvenile
                                                                                                        ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult
                                                                                                        ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Senescent_adult
                                                                                                        ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Died
                                                                                                        ])
                return pop_Out
            
            def method_SplitLifeStagesIntoVSPs_By_VSP_AgeClass_Updating_LifeStage(self, pop_In, boolUpdate):
                
                
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # Define the life stages in each virtual subpopulation
                # 
                # Neonate                         - (0,0) = age < maxNeonateAge - 0.1
                # Juvenile                        - (0,1) = age < maxJuvenileAge - 0.1
                # Sub-adult                       - (0,2) = age < minSubAdultAge - 0.1
                # Reproductively available adults - (0.3) = age >= minMatingAge and age =< maxMatingAge - 0.1  [age < maxMatingAge]
                # Gestating Females               - (0,4) = boolReproductiveAge and boolGestating and not boolResting [age < maxMatingAge + boolGestating]
                # Resting females                 - (0,5) = boolReproductiveAge and boolResting
                # Senescent adults                - (0,6) = age >= maxMatingAge and age =< maxAge - 0.1        [maxMatingAge < age < maxAge]
                # Died old age                    - (0,7) = age >= maxAge                                      [age > maxAge] DIED! So should always be Zero
                
                #Split 
                # 99 is just a dummy number that will not be associated with any individuals
                #this is just to ensure that the final VSPs contain the correct individuals

                pop_Out = self.method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary,
                                                                                 boolUpdateInfoField=boolUpdate,
                                                                                 stringVSPSplitOperator = 'values',
                                                                                 stringInfoFieldToSplitBy = 'age_class',
                                                                                 listVSPSplitValues = [
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo,
                                                                                                        #globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Neonate,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Juvenile,
                                                                                                        #globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Sub_adult,
                                                                                                        #99,
                                                                                                        #99,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Gestating_adult_female,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Resting_adult_female,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Senescent_adult,
                                                                                                        globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Died
                                                                                                      ],
                                                                                 listVSPSplitNames = [
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Embryo + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Embryo,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Neonate + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Neonate,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Juvenile + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Juvenile,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Sub_adult + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Sub_adult,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Reproductivly_available_adult + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Reproductivly_available_adult,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Gestating_adult_female + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Gestating_adult_female,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Resting_adult_female + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Resting_adult_female,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Senescent_adult + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Senescent_adult,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Died + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Died
                                                                                                        globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo
                                                                                                        #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Neonate
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Juvenile
                                                                                                        #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Sub_adult
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Gestating_adult_female
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Resting_adult_female
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Senescent_adult
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Died
                                                                                                        ],
                                                                                 stringInfoFieldToUpdate = 'life_stage',
                                                                                 listVSPsToUpdate = [
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo,
                                                                                                        #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Neonate,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Juvenile,
                                                                                                        #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Sub_adult,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Gestating_adult_female,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Resting_adult_female,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Senescent_adult,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Died
                                                                                                        ],
                                                                                 listUpdateValues = [
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo,
                                                                                                        #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Neonate,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Juvenile,
                                                                                                        #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Sub_adult,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Gestating_adult_female,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Resting_adult_female,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Senescent_adult,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Died
                                                                                                        ])
                return pop_Out
            
            def method_SplitLifeStagesIntoVSPs_By_Age_In_Months_Updating_LifeStage(self, pop_In, boolUpdate):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass                
                
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # Define the life stages in each virtual subpopulation
                # 
                # Neonate                         - (0,0) = age < maxNeonateAge - 0.1
                # Juvenile                        - (0,1) = age < maxJuvenileAge - 0.1
                # Sub-adult                       - (0,2) = age < minSubAdultAge - 0.1
                # Reproductively available adults - (0.3) = age >= minMatingAge and age =< maxMatingAge - 0.1  [age < maxMatingAge]
                # Gestating Females               - (0,4) = boolReproductiveAge and boolGestating and not boolResting [age < maxMatingAge + boolGestating]
                # Resting females                 - (0,5) = boolReproductiveAge and boolResting
                # Senescent adults                - (0,6) = age >= maxMatingAge and age =< maxAge - 0.1        [maxMatingAge < age < maxAge]
                # Died old age                    - (0,7) = age >= maxAge                                      [age > maxAge] DIED! So should always be Zero
                
                #Split 
                # 99 is just a dummy number that will not be associated with any individuals
                #this is just to ensure that the final VSPs contain the correct individuals

                pop_In = self.method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary,
                                                                                 boolUpdateInfoField=boolUpdate,
                                                                                 stringVSPSplitOperator = 'cutoff',
                                                                                 stringInfoFieldToSplitBy = 'age_in_months',
                                                                                 listVSPSplitValues = [ 
                                                                                                        self.objSSParametersLocal.intGestationLengthInMonths,
                                                                                                        #self.objSSParametersLocal.intGestationLengthInMonths+12,
                                                                                                        (self.objSSParametersLocal.minMatingAge*12),
                                                                                                        (self.objSSParametersLocal.maxMatingAge*12),
                                                                                                        (self.objSSParametersLocal.maxAge*12)
                                                                                                        ],
                                                                                 listVSPSplitNames = [
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Embryo + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Embryo,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Neonate + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Neonate,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Juvenile + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Juvenile,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Sub_adult + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Sub_adult,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Reproductivly_available_adult + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Reproductivly_available_adult,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Gestating_adult_female + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Gestating_adult_female,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Resting_adult_female + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Resting_adult_female,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Senescent_adult + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Senescent_adult,
#                                                                                                         globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Died + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Died
                                                                                                        globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo
                                                                                                        #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Neonate
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Juvenile
                                                                                                        #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Sub_adult
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult
                                                                                                        #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Gestating_adult_female
                                                                                                        #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Resting_adult_female
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Senescent_adult
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Died
                                                                                                        ],
                                                                                 stringInfoFieldToUpdate = 'life_stage',
                                                                                 listVSPsToUpdate = [
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo,
                                                                                                        #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Neonate,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Juvenile,
                                                                                                        #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Sub_adult,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult,
                                                                                                        #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Gestating_adult_female,
                                                                                                        #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Resting_adult_female,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Senescent_adult,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Died
                                                                                                        ],
                                                                                 listUpdateValues = [
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo,
                                                                                                        #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Neonate,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Juvenile,
                                                                                                        #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Sub_adult,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult,
                                                                                                        #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Gestating_adult_female,
                                                                                                        #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Resting_adult_female,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Senescent_adult,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Died
                                                                                                        ])

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    bool_Debug_Display__Pop_Dump_By_VSP = False
                    if bool_Debug_Display__Pop_Dump_By_VSP:                
                        intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            simupop.dump(pop_In, subPops=[(0,intVirtualSubPop)])
                            with SSAnalysisHandler() as SSAnalysisOperation:
                                listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                                print('SEX COUNT - Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))   
                            pass
                        pass
                    pass
                    bool_Debug_Display__Pop_Sexes_Count = False
                    if bool_Debug_Display__Pop_Sexes_Count:                         
                        #simupop.dump(pop_In)
                        with SSAnalysisHandler() as SSAnalysisOperation:
                            listTotalCountofMaleFemale = [0,0]
                            intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                            for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                                listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                                listTotalCountofMaleFemale[0] += listCountofMaleFemale[0]
                                listTotalCountofMaleFemale[1] += listCountofMaleFemale[1]
                            pass 
                            print('SEX COUNT - Total Males:' + str(listTotalCountofMaleFemale[0]) + ' Total Females:' + str(listTotalCountofMaleFemale[1]))   
                        pass
                    pass
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    #pass
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass

                pop_Out = pop_In
                
                return pop_Out
                
            def method_SplitLifeStagesIntoVSPs_By_VSP_AgeClass_Updating_Single_VSP(self, pop_In, boolUpdate):
                
                
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # Define the life stages in each virtual subpopulation
                # 
                # Neonate                         - (0,0) = age < maxNeonateAge - 0.1
                # Juvenile                        - (0,1) = age < maxJuvenileAge - 0.1
                # Sub-adult                       - (0,2) = age < minSubAdultAge - 0.1
                # Reproductively available adults - (0.3) = age >= minMatingAge and age =< maxMatingAge - 0.1  [age < maxMatingAge]
                # Gestating Females               - (0,4) = boolReproductiveAge and boolGestating and not boolResting [age < maxMatingAge + boolGestating]
                # Resting females                 - (0,5) = boolReproductiveAge and boolResting
                # Senescent adults                - (0,6) = age >= maxMatingAge and age =< maxAge - 0.1        [maxMatingAge < age < maxAge]
                # Died old age                    - (0,7) = age >= maxAge                                      [age > maxAge] DIED! So should always be Zero
                
                #Split 
                # 99 is just a dummy number that will not be associated with any individuals
                #this is just to ensure that the final VSPs contain the correct individuals

                pop_Out = self.method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary,
                                                                                 boolUpdateInfoField=True,
                                                                                 stringVSPSplitOperator = 'values',
                                                                                 stringInfoFieldToSplitBy = 'age_class',
                                                                                 listVSPSplitValues = [99, globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult],
                                                                                 listVSPSplitNames = ['NA', globalsSS.VSP_AgeClass.static_stringShortNameVSP_AgeClass_Reproductivly_available_adult + '_' + globalsSS.VSP_AgeClass.static_stringMediumNameVSP_AgeClass_Reproductivly_available_adult],
                                                                                 stringInfoFieldToUpdate = 'life_stage',
                                                                                 listVSPsToUpdate = [1],
                                                                                 listUpdateValues = [globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult])
                return pop_Out
            
            def method_SplitLifeStagesIntoVSPs_By_Age_In_Months_Updating_Life_Stage_Juvenile_To_Adult(self, pop_In):
                
                
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # Define the life stages in each virtual subpopulation
                # 
                # Neonate                         - (0,0) = age < maxNeonateAge - 0.1
                # Juvenile                        - (0,1) = age < maxJuvenileAge - 0.1
                # Sub-adult                       - (0,2) = age < minSubAdultAge - 0.1
                # Reproductively available adults - (0.3) = age >= minMatingAge and age =< maxMatingAge - 0.1  [age < maxMatingAge]
                # Gestating Females               - (0,4) = boolReproductiveAge and boolGestating and not boolResting [age < maxMatingAge + boolGestating]
                # Resting females                 - (0,5) = boolReproductiveAge and boolResting
                # Senescent adults                - (0,6) = age >= maxMatingAge and age =< maxAge - 0.1        [maxMatingAge < age < maxAge]
                # Died old age                    - (0,7) = age >= maxAge                                      [age > maxAge] DIED! So should always be Zero
                
                #Split 
                # 99 is just a dummy number that will not be associated with any individuals
                #this is just to ensure that the final VSPs contain the correct individuals

                pop_Out = self.method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary,
                                                                                 boolUpdateInfoField=True,
                                                                                 stringVSPSplitOperator = 'values',
                                                                                 stringInfoFieldToSplitBy = 'age_in_months',
                                                                                 listVSPSplitValues = [self.objSSParametersLocal.minMatingAge*12],
                                                                                 listVSPSplitNames = ['NA'],
                                                                                 stringInfoFieldToUpdate = 'life_stage',
                                                                                 listVSPsToUpdate = [0],
                                                                                 listUpdateValues = [globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult])
                return pop_Out

            def method_SplitLifeStagesIntoVSPs_By_Age_In_Months_Updating_Pre_Adult_Life_Stages(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass                 
                
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # Define the life stages in each virtual subpopulation
                # 
                # Neonate                         - (0,0) = age < maxNeonateAge - 0.1
                # Juvenile                        - (0,1) = age < maxJuvenileAge - 0.1
                # Sub-adult                       - (0,2) = age < minSubAdultAge - 0.1
                # Reproductively available adults - (0.3) = age >= minMatingAge and age =< maxMatingAge - 0.1  [age < maxMatingAge]
                # Gestating Females               - (0,4) = boolReproductiveAge and boolGestating and not boolResting [age < maxMatingAge + boolGestating]
                # Resting females                 - (0,5) = boolReproductiveAge and boolResting
                # Senescent adults                - (0,6) = age >= maxMatingAge and age =< maxAge - 0.1        [maxMatingAge < age < maxAge]
                # Died old age                    - (0,7) = age >= maxAge                                      [age > maxAge] DIED! So should always be Zero
                
                #Split 
                # 99 is just a dummy number that will not be associated with any individuals
                #this is just to ensure that the final VSPs contain the correct individuals

                pop_In = self.method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(pop_In
                                                                                 ,globalsSS.SP_SubPops.static_intSP_SubPop_Primary
                                                                                 ,boolUpdateInfoField=True
                                                                                 ,stringVSPSplitOperator = 'cutoff'
                                                                                 ,stringInfoFieldToSplitBy = 'age_in_months'
                                                                                 ,listVSPSplitValues = [
                                                                                                        self.objSSParametersLocal.intGestationLengthInMonths
                                                                                                        #,self.objSSParametersLocal.intGestationLengthInMonths+12
                                                                                                        ,self.objSSParametersLocal.minMatingAge*12
                                                                                                        ]
                                                                                ,listVSPSplitNames = [
                                                                                                       #globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo
                                                                                                       #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Neonate
                                                                                                       #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Juvenile
                                                                                                       #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Sub_adult
                                                                                                       #,'NA'#,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult
                                                                                                      ]
                                                                                 ,stringInfoFieldToUpdate = 'life_stage'
                                                                                 ,listVSPsToUpdate = [
                                                                                                       globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo
#                                                                                                         ,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Neonate
                                                                                                       ,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Juvenile
#                                                                                                         ,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Sub_adult
#                                                                                                         #,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult
#                                                                                                         globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo
#                                                                                                         ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Neonate
#                                                                                                         #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Juvenile
#                                                                                                         ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Sub_adult
                                                                                                        ]
                                                                                 ,listUpdateValues = [
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo
                                                                                                        #,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Neonate
                                                                                                        ,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Juvenile
                                                                                                        #,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Sub_adult
                                                                                                        #,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult
                                                                                                        ])
                
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    bool_Debug_Display__Pop_Dump_By_VSP = False
                    if bool_Debug_Display__Pop_Dump_By_VSP:                
                        intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            simupop.dump(pop_In, subPops=[(0,intVirtualSubPop)])
                            with SSAnalysisHandler() as SSAnalysisOperation:
                                listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                                print('SEX COUNT - Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))   
                            pass
                        pass
                    pass
                    bool_Debug_Display__Pop_Sexes_Count = False
                    if bool_Debug_Display__Pop_Sexes_Count:                         
                        #simupop.dump(pop_In)
                        with SSAnalysisHandler() as SSAnalysisOperation:
                            listTotalCountofMaleFemale = [0,0]
                            intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                            for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                                listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                                listTotalCountofMaleFemale[0] += listCountofMaleFemale[0]
                                listTotalCountofMaleFemale[1] += listCountofMaleFemale[1]
                            pass 
                            print('SEX COUNT - Total Males:' + str(listTotalCountofMaleFemale[0]) + ' Total Females:' + str(listTotalCountofMaleFemale[1]))   
                        pass
                    pass
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    #pass
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                           
                pop_Out = pop_In
                
                return pop_Out



                
            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            VSP Splits - GESTATING
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
            
            def method_SplitLifeStagesIntoVSPs_By_Gestation_Month_Count_SPLITTING_Life_Stage_Into_Resting_Or_Gestating(self, pop_In, boolUpdate):
                
                
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # Define the life stages in each virtual subpopulation
                # 
                # Neonate                         - (0,0) = age < maxNeonateAge - 0.1
                # Juvenile                        - (0,1) = age < maxJuvenileAge - 0.1
                # Sub-adult                       - (0,2) = age < minSubAdultAge - 0.1
                # Reproductively available adults - (0.3) = age >= minMatingAge and age =< maxMatingAge - 0.1  [age < maxMatingAge]
                # Gestating Females               - (0,4) = boolReproductiveAge and boolGestating and not boolResting [age < maxMatingAge + boolGestating]
                # Resting females                 - (0,5) = boolReproductiveAge and boolResting
                # Senescent adults                - (0,6) = age >= maxMatingAge and age =< maxAge - 0.1        [maxMatingAge < age < maxAge]
                # Died old age                    - (0,7) = age >= maxAge                                      [age > maxAge] DIED! So should always be Zero
                
                #Split 
                # 99 is just a dummy number that will not be associated with any individuals
                #this is just to ensure that the final VSPs contain the correct individuals

                pop_Out = self.method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary,
                                                                                 boolUpdateInfoField=boolUpdate,
                                                                                 stringVSPSplitOperator = 'cutoff',
                                                                                 stringInfoFieldToSplitBy = 'gestation_resting_countdown',
                                                                                 listVSPSplitValues = [
                                                                                                       1
                                                                                                       ,2
                                                                                                       ,self.objSSParametersLocal.intReproductiveRestLengthInMonths
                                                                                                       ],
                                                                                 listVSPSplitNames = [
                                                                                                    'Not_Pregnant'
                                                                                                    ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult
                                                                                                    ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Resting_adult_female
                                                                                                    ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Gestating_adult_female
                                                                                                    ],
                                                                                 stringInfoFieldToUpdate = 'life_stage',
                                                                                 listVSPsToUpdate = [
                                                                                                     1
                                                                                                     ,2
                                                                                                     ,3
                                                                                                    ],
                                                                                 listUpdateValues = [
                                                                                                     globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult 
                                                                                                     ,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Resting_adult_female 
                                                                                                     ,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Gestating_adult_female 
                                                                                                     ])
                return pop_Out

            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            VSP Splits - RESTING
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
       
            def method_SplitLifeStagesIntoVSPs_By_INITIAL_Is_Resting_Reproductively_InfoField(self, pop_In):
                
                
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # Define the life stages in each virtual subpopulation
                # 
                # Neonate                         - (0,0) = age < maxNeonateAge - 0.1
                # Juvenile                        - (0,1) = age < maxJuvenileAge - 0.1
                # Sub-adult                       - (0,2) = age < minSubAdultAge - 0.1
                # Reproductively available adults - (0.3) = age >= minMatingAge and age =< maxMatingAge - 0.1  [age < maxMatingAge]
                # Gestating Females               - (0,4) = boolReproductiveAge and boolGestating and not boolResting [age < maxMatingAge + boolGestating]
                # Resting females                 - (0,5) = boolReproductiveAge and boolResting
                # Senescent adults                - (0,6) = age >= maxMatingAge and age =< maxAge - 0.1        [maxMatingAge < age < maxAge]
                # Died old age                    - (0,7) = age >= maxAge                                      [age > maxAge] DIED! So should always be Zero
                
                #Split 
                # 99 is just a dummy number that will not be associated with any individuals
                #this is just to ensure that the final VSPs contain the correct individuals

                pop_Out = self.method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary,
                                                                                 boolUpdateInfoField=False,
                                                                                 stringVSPSplitOperator = 'values',
                                                                                 stringInfoFieldToSplitBy = 'is_resting_reproductively',
                                                                                 listVSPSplitValues = [
                                                                                                       0,
                                                                                                       1,
                                                                                                       2],
                                                                                 listVSPSplitNames = [
                                                                                                      'NA1',
                                                                                                      globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Resting_adult_female + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Resting_adult_female + '_Resting_1st_month',
                                                                                                      globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Resting_adult_female + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Resting_adult_female + '_Resting_Greater_Than_1_month'
                                                                                                      ],
                                                                                )
                return pop_Out
            
           
            def method_SplitLifeStagesIntoVSPs_By_Resting_Reproductively_Month_Count_SPLITTING_Life_Stage_Reproductively_Available_AND_Resting(self, pop_In, boolUpdate):
                
                
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # Define the life stages in each virtual subpopulation
                # 
                # Neonate                         - (0,0) = age < maxNeonateAge - 0.1
                # Juvenile                        - (0,1) = age < maxJuvenileAge - 0.1
                # Sub-adult                       - (0,2) = age < minSubAdultAge - 0.1
                # Reproductively available adults - (0.3) = age >= minMatingAge and age =< maxMatingAge - 0.1  [age < maxMatingAge]
                # Gestating Females               - (0,4) = boolReproductiveAge and boolGestating and not boolResting [age < maxMatingAge + boolGestating]
                # Resting females                 - (0,5) = boolReproductiveAge and boolResting
                # Senescent adults                - (0,6) = age >= maxMatingAge and age =< maxAge - 0.1        [maxMatingAge < age < maxAge]
                # Died old age                    - (0,7) = age >= maxAge                                      [age > maxAge] DIED! So should always be Zero
                
                #Split 
                # 99 is just a dummy number that will not be associated with any individuals
                #this is just to ensure that the final VSPs contain the correct individuals

                pop_Out = self.method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary,
                                                                                 boolUpdateInfoField=boolUpdate,
                                                                                 stringVSPSplitOperator = 'cutoff',
                                                                                 stringInfoFieldToSplitBy = 'resting_reproductively_month_count',
                                                                                 listVSPSplitValues = [
                                                                                                       1,
                                                                                                       2,
                                                                                                       self.objSSParametersLocal.intGestationLengthInMonths,
                                                                                                       ],
                                                                                 listVSPSplitNames = [
                                                                                                    'Not_Pregnant',
                                                                                                    'Gestating_1st_Month',
#                                                                                                     globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Resting_adult_female + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Resting_adult_female,
#                                                                                                     globalsSS.VSP_LifeStage.static_stringShortNameVSP_LifeStage_Reproductivly_available_adult + '_' + globalsSS.VSP_LifeStage.static_stringMediumNameVSP_LifeStage_Reproductivly_available_adult,
                                                                                                    globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Resting_adult_female,
                                                                                                    globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult,
                                                                                                    ],
                                                                                 stringInfoFieldToUpdate = 'life_stage',
                                                                                 listVSPsToUpdate = [
                                                                                                     1,
                                                                                                     2,
                                                                                                     3
                                                                                                    #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Gestating_adult_female,
                                                                                                    #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult,
                                                                                                    ],
                                                                                 listUpdateValues = [
                                                                                                     globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Resting_adult_female, 
                                                                                                     globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Resting_adult_female, 
                                                                                                     globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult
                                                                                                     ])
                return pop_Out
 
            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            VSP Splits - LIFE STAGE
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
                  
            def method_SplitLifeStagesIntoVSPs_By_LifeStage(self, pop_In, boolUpdate):
                
                
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # Define the life stages in each virtual subpopulation
                # 
                # Neonate                         - (0,0) = age < maxNeonateAge - 0.1
                # Juvenile                        - (0,1) = age < maxJuvenileAge - 0.1
                # Sub-adult                       - (0,2) = age < minSubAdultAge - 0.1
                # Reproductively available adults - (0.3) = age >= minMatingAge and age =< maxMatingAge - 0.1  [age < maxMatingAge]
                # Gestating Females               - (0,4) = boolReproductiveAge and boolGestating and not boolResting [age < maxMatingAge + boolGestating]
                # Resting females                 - (0,5) = boolReproductiveAge and boolResting
                # Senescent adults                - (0,6) = age >= maxMatingAge and age =< maxAge - 0.1        [maxMatingAge < age < maxAge]
                # Died old age                    - (0,7) = age >= maxAge                                      [age > maxAge] DIED! So should always be Zero
                
                pop_Out = self.method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary,
                                                                                 boolUpdateInfoField=boolUpdate,
                                                                                 stringVSPSplitOperator = 'values',
                                                                                 stringInfoFieldToSplitBy = 'life_stage',
                                                                                 listVSPSplitValues = [
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo,
                                                                                                        #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Neonate,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Juvenile,
                                                                                                        #globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Sub_adult,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Gestating_adult_female,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Resting_adult_female,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Senescent_adult,
                                                                                                        globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Died
                                                                                                        ],
                                                                                 listVSPSplitNames = [
                                                                                                        globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo
                                                                                                        #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Neonate
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Juvenile
                                                                                                        #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Sub_adult
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Gestating_adult_female
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Resting_adult_female
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Senescent_adult
                                                                                                        ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Died
                                                                                                        ])
                return pop_Out
            
            
            def method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(self, pop_In, intSubPop, boolUpdateInfoField, stringVSPSplitOperator, stringInfoFieldToSplitBy, listVSPSplitValues, listVSPSplitNames=[], stringInfoFieldToUpdate='', listVSPsToUpdate=[], listUpdateValues=[]):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass     
                                    
                #Split 
                # 99 is just a dummy number that will not be associated with any individuals
                #this is just to ensure that the final VSPs contain the correct individuals
                if stringVSPSplitOperator == 'cutoff':
                    pop_In.setVirtualSplitter(simupop.InfoSplitter(stringInfoFieldToSplitBy,
                        cutoff=listVSPSplitValues,
                         names=listVSPSplitNames))
                    #DEBUG_ON
                    #simupop.dump(pop_In)
                    #DEBUG_OFF
                else:
                    if stringVSPSplitOperator == 'values':
                        pop_In.setVirtualSplitter(simupop.InfoSplitter(stringInfoFieldToSplitBy,
                            values=listVSPSplitValues,
                             names=listVSPSplitNames))
                
                intUpdateCount = 0
                if boolUpdateInfoField:
                    #Update info fields
                    for intVSP in listVSPsToUpdate:
                        pop_In.setIndInfo(listUpdateValues[intUpdateCount], stringInfoFieldToUpdate, subPop=(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVSP))
                        intUpdateCount += 1

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    bool_Debug_Display__Pop_Dump_By_VSP = False
                    if bool_Debug_Display__Pop_Dump_By_VSP:                
                        intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            simupop.dump(pop_In, subPops=[(0,intVirtualSubPop)])
                            with SSAnalysisHandler() as SSAnalysisOperation:
                                listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                                print('SEX COUNT - Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))   
                            pass
                        pass
                    pass
                    bool_Debug_Display__Pop_Sexes_Count = False
                    if bool_Debug_Display__Pop_Sexes_Count:                         
                        #simupop.dump(pop_In)
                        with SSAnalysisHandler() as SSAnalysisOperation:
                            listTotalCountofMaleFemale = [0,0]
                            intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                            for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                                listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                                listTotalCountofMaleFemale[0] += listCountofMaleFemale[0]
                                listTotalCountofMaleFemale[1] += listCountofMaleFemale[1]
                            pass 
                            print('SEX COUNT - Total Males:' + str(listTotalCountofMaleFemale[0]) + ' Total Females:' + str(listTotalCountofMaleFemale[1]))   
                        pass
                    pass
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    #pause
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                           
                pop_Out = pop_In
                
                return pop_Out
 
#             '''
#             VSP Splits - SEX
#             '''
#             def method_Split_Pop_By_Sex_Into_VSP(self, pop_In):
#                 
#                 pop_In.setVirtualSplitter(SexSplitter())
# 
#                 pop_Out = pop_In
#                 
#                 return pop_Out


            def method_Split_Reproductively_Mature_VSP_By_Sex_OLD(self, pop_In):
                
                pop_In.setVirtualSplitter(
                              simupop.ProductSplitter([
                                         simupop.InfoSplitter('life_stage',
                                         values=[globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult],
                                         names=[globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult]),
                                         simupop.SexSplitter()
                                         ], 
                                         names=[
                                                globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult_Male
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult_Female
                                                ]))
                
                pop_Out = pop_In    
                
                return pop_Out   

            def method_Split_By_Sex_Then_By_AgeInMonths_VSPs(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass   
                    
                    
                pop_In.setVirtualSplitter(
                              simupop.ProductSplitter([
                                        simupop.SexSplitter()
                                        ,simupop.InfoSplitter('age_in_months'
                                            ,cutoff=[(intAgeInYears) for intAgeInYears in range(0, self.objSSParametersLocal.maxAge*12, 1)],
                                         #names=[globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult]),
                                         )]))
 
 
                #DEBUG_ON
#                 intNumberVirtualSubPops = pop_In.numVirtualSubPop()
#                 for intVirtualSubPop in range(0, intNumberVirtualSubPops):
#                     simupop.dump(pop_In, subPops=[(0,intVirtualSubPop)])
#                     with SSAnalysisHandler() as SSAnalysisOperation:
#                         listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
#                         print('SEX COUNT - Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))   
#                     
#                 pass
#                 raw_input('pausing...')
                #DEBUG_OFF

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
            
                                               
                pop_Out = pop_In    

                
                return pop_Out
                                               
            '''
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            Main Processing
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            '''    
            '''
            Main Processing routine
            '''   
            '''@profile'''
            def method_MainProcessing(self):


                '''
                ---------------------
                Open - EOR - End of Replicate Loggers
                ---------------------
                '''
                self.method_Open_Log_Files_For_End_Of_Replicate_EOR_Reporting() 
                               
                #<<<<<<<<<<<<<<<<<< INITILIZE POPULATION <<<<<<<<<<<<<<<<<<<<
                
                #Initialise populations and initial ages
                pop_In = self.method_InitialisePopulations()
                #self.createSim()
                
                #DEBUG_ON
                # Output the summary of  age class totals(virtualSubPops) at each generation
                #self.methodOutput_outputPopulationDump(self.pop, ['method_MainProcessing - post method_InitialisePopulations'])
                #raw_input('\n After Initialise Populations - Press return to continue... \n')
                #DEBUG_OFF
                
                '''
                ---------------------------
                Initial Mating
                ---------------------------
                '''
                self.int_MatingCount_Total = 0
                self.int_MatingCount_BurnIn = 0
                self.int_MatingCount_PostBurnIn = 0
                
                self.objSSParametersLocal.boolInitialEvolve = True
                #self.method_EvolveWithBurnInMating()
#                 list_Simupop_Evolve_Function_InitOps = [simupop.IdTagger()]
#                 if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_WF_Diploid_Sexual_Random_Mating:
#                     list_Simupop_Evolve_Function_PreOps = [simupop.InfoExec('age += 1'), simupop.StepwiseMutator(rates=5e-4, loci=simupop.ALL_AVAIL)]
#                 else:
#                     list_Simupop_Evolve_Function_PreOps = [simupop.InfoExec('age += 1')]
#                 pass
                
                pop_In = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(pop_In, boolUpdate=True)
                
                list_Simupop_Evolve_Function_InitOps = []
                list_Simupop_Evolve_Function_PreOps = []
                #self.pop = self.method_EvolvePedigreeWithMating(self.pop, 0, list_Simupop_Evolve_Function_InitOps, list_Simupop_Evolve_Function_PreOps)
                
                self.objSSParametersLocal.boolInitialEvolve = False

                #DEBUG_ON
                # Output the summary of  age class totals(virtualSubPops) at each generation
                #self.methodOutput_outputPopulationDump(self.pop, ['method_MainProcessing - post method_EvolveWithBurnInMating'])
                #raw_input('\n After Initial Evolve - Press return to continue... \n')
                #DEBUG_OFF
                
                

                #Advance ages inline with fertilisation and parturition months
                #self.method_Initial_Advance_of_Ages()

                #DEBUG_ON
                # Output the summary of  age class totals(virtualSubPops) at each generation
                #self.methodOutput_outputPopulationDump(self.pop, ['method_MainProcessing - post method_Initial_Advance_of_Ages'])
                #raw_input('\n After Initial Evolve - Press return to continue... \n')
                #DEBUG_OFF
                
                '''
                ---------------------------
                Burn-in Processing
                ---------------------------
                '''              
                #Flag as Burn-in to allow burn-in pedigree output to be turned on or of with boolBurnInOutput
                self.objSSParametersLocal.boolBurnIn = True
                
                self.objSSParametersLocal.stringEventMessage = 'Burn-in - Several rounds of mating and parturition'
            
                with SSOutputHandler() as SSOutputOperation:
                    listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, '')
                    #
                    stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> BurnIn - START   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                    boolNewline=True
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                    #
                    stringMessage = '> Running Burn-in fertilisations...'  +'\n'
                    boolNewline=True
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                    
                #Perform Temporal Burn-in cycles of fertilisation and birth
                pop_In = self.method_TemporalPopulationProcessing_Initiate(pop_In)
                #DEBUG_ON
                #self.method_TemporalPopulationProcessing_PROTOTYPE()
                #DEBUG_OFF

                with SSOutputHandler() as SSOutputOperation:
                    listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> BurnIn - END   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                    boolNewline=True
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                    #
                    listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    SSOutputOperation.methodOutput_SimGeneralMessageFooter(listOutputDestinations, '')
                     
                #Burn in finished so turn off flag
                self.objSSParametersLocal.boolBurnIn = False
                
                #DEBUG_ON
                #Pause for testing
                #input('\n After TRUE Burn-in - Press return to continue... \n')
                #DEBUG_OFF
                
                #<<<<<<<<<<<<<<<<<< SIMULATON RUN <<<<<<<<<<<<<<<<<<<<

                with SSOutputHandler() as SSOutputOperation:
                    listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, '')
                    #
                    stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> Simulation - START   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                    boolNewline=True
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                    #
                    stringMessage = '> Running Simulation fertilisations...'  +'\n'
                    boolNewline=True
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                
                #Perform Simulation specific Temporal cycles of fertilisation and birth
                pop_In = self.method_TemporalPopulationProcessing_Initiate(pop_In)
                #DEBUG_ON
                #self.method_TemporalPopulationProcessing_PROTOTYPE()
                #DEBUG_OFF

                with SSOutputHandler() as SSOutputOperation:
                    listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> Simulation - END   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                    boolNewline=True
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                    #
                    listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    SSOutputOperation.methodOutput_SimGeneralMessageFooter(listOutputDestinations, '')
                
                
                '''
                ---------------------
                End of SIM REPLICATE reporting
                ---------------------
                '''
                self.method_End_Of_SIM_REPLICATE_Reporting(pop_In)
 
                '''
                ---------------------
                Close - EOR - End of Replicate Loggers
                ---------------------
                '''
                self.method_Close_Log_Files_EOR_End_Of_replicate()
                
                pop_Out = pop_In
                               
                return pop_Out
 
            '''
            --------------------------------------------------------------------------------------------------------
            # Sub-main processing
            --------------------------------------------------------------------------------------------------------
            '''

            '''
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            Temporal Processing
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            '''
            '''@profile'''
            def method_TemporalPopulationProcessing_Initiate(self, pop_In):
              
            
                self.objSSParametersLocal.boolGestating = False
                
                #Perform initial aging and InfoField initilisation
                pop_In = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(pop_In, boolUpdate=True)
                
                #DEBUG_ON
                #self.methodOutput_outputPopulationDump(self.pop,['method_TemporalPopulationProcessing - initialization'])
                #self.methodOutput_outputPopulationAgeClassTotals(self.pop, [False, False])
                #self.methodOutput_outputPopulationLifeStageTotals(self.pop, [False, False])
                #Pause for testing
                #input('\n After INITIAL method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths - Press return to continue... \n')
                #DEBUG_OFF
                
                #DEBUG_ON
                #Pause for testing
                #input('\n After Initial Evolve - Press return to close this window... \n')
                #DEBUG_OFF
                
                #>>>>>>>>>>>>>>>>>>>>> CALENDAR PROCESSING - Start cycling by calendar month>>>>>>>>
                                
                #>>>>>>>>>>>>>>> COUNTER & FLAG INITILIZATION
                
                #Initialze Gen count back to zero for each replicate                    
                self.objSSParametersLocal.intCurrentTemporalFertilisation = 0;


                
#                 boolEOCY = False
                
                self.objSSParametersLocal.intSimulationCurrentMonth = 1
                self.objSSParametersLocal.intYearCurrentMonth = 1
                self.objSSParametersLocal.intYearReproductiveCycleCurrentMonth = 1
#                 if self.objSSParametersLocal.boolGestating:
#                     self.objSSParametersLocal.intGestationCurrentMonth += 1   
                
                if self.objSSParametersLocal.boolBurnIn:
                    intTemporalProcessingLengthInMonths = self.objSSParametersLocal.intReplicateBurnInLengthInMonths
                else:
                    intTemporalProcessingLengthInMonths = self.objSSParametersLocal.intGrandTotalMonthsToSimulate
                
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #pop_In = self.method_SplitLifeStagesIntoVSPs_By_VSP_AgeClass_Updating_LifeStage(pop_In, boolUpdate=True)
                pop_In = self.method_SplitLifeStagesIntoVSPs_By_Age_In_Months_Updating_LifeStage(pop_In, boolUpdate=True)
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                intSimulationCurrentMonth = self.objSSParametersLocal.intSimulationCurrentMonth
                for intSimulationCurrentMonth in range(0, intTemporalProcessingLengthInMonths):
                     
                    self.objSSParametersLocal.intSimulationCurrentMonth = intSimulationCurrentMonth
                     
                    #DEBUG_ON
                    #pdb.set_trace()
                    #DEBUG_OFF
                    
                    pop_Out = self.method_TemporalPopulationProcessing_Execute(pop_In)
                    
                    if self.bool_Abort_Processing_Gracefully:
                        break
                    pass
                pass
            
                
                return pop_Out

            '''@profile'''
            def method_TemporalPopulationProcessing_Execute(self, pop_In):

                boolEOCY = False
              
                #stringEvent = ''
                string_const_EventEOCM = 'EOMY'         #End of calendar month
                string_const_EventEOCY = 'EOCY'         #End of calendar year
                string_const_EventEORY = 'EORY'         #End of reproductive year
                string_const_EventMating = 'MATE'       #Mating occurs
                string_const_EventParturition = 'PART'  #Parturition occurs
                string_const_EventFertilization = 'FERT'#Fertilization occurs
                string_const_EventMortalityNatural = 'MORT'  #NATURAL Mortality occurs
                string_const_EventMortalityUnNatural = 'UNMO'  #UnNATURAL Mortality occurs
                string_const_EventMortalityCombined = 'COMB'  #COMBINED Mortality occurs
                            
                stringEvent = ''
                self.objSSParametersLocal.stringEventMessage = ' '
                
                #DEBUG_ON
                #                     if self.objSSParametersLocal.intSimulationCurrentMonth == 69:
                #                         pass
                #DEBUG_OFF
                
                #>>>>>>>>>>>>>>>>>>>>> START OF MONTH REPORTING 
                #pop_In = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(pop_In, boolUpdate=True)
                #----->pop_In = self.method_SplitLifeStagesIntoVSPs_By_VSP_AgeClass_Updating_LifeStage(pop_In, boolUpdate=True)
                pop_In = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop_In, boolUpdate=False)
                
                self.objSSParametersLocal.stringEventMessageLocal = 'START OF MONTH REPORTING; '
                self.objSSParametersLocal.stringEventMessage = self.objSSParametersLocal.stringEventMessageLocal + self.objSSParametersLocal.stringEventMessage
                
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
                    #DEBUG_ON
                    #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - ' + self.objSSParametersLocal.stringEventMessage])
                    #DEBUG_OFF
                    self.methodOutput_outputPopulationTemporalProcessingSummaryInfo(pop_In, [False, False])
                    self.methodOutput_outputPopulationAgeClassTotals(pop_In, [False, False])
                    self.methodOutput_outputPopulationLifeStageTotals(pop_In, [False, False])
                
                #DEBUG_ON
                #Pause for testing
                #raw_input('\n Location: ' + self.objSSParametersLocal.stringEventMessageLocal + ' After ' + self.objSSParametersLocal.stringEventMessage + ' - Press return to continue... \n')
                #DEBUG_OFF
                
                '''
                #>>>>>>>>>>>>>>>>>>>>>>> MORTALITY & MATING - Check if its the month for MATING
                '''
                if self.objSSParametersLocal.intYearCurrentMonth == self.objSSParametersLocal.intMatingCalenderMonth:
                    
                    #COMBINED MORTALITY occurs here every 12 months and must occur before mating to free up slots for new embryos
                    if self.objSSParametersLocal.boolBurnIn == False or \
                        self.objSSParametersLocal.boolBurnIn == True:
                         
                        #>>> COMBINED MORTALITY START <<<
                        if self.objSSParametersLocal.boolBurnIn == True and \
                           (self.objSSParametersLocal.intSimulationCurrentMonth / 12) < 1:
                            pass
                        elif self.objSSParametersLocal.boolAllowNATURALMortality:
                             
                            stringEvent = string_const_EventMortalityCombined
                             
                            #DEBUG_ON
                            # Output the summary of  age class totals(virtualSubPops) at each generation
                            #pop_In = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(pop_In, boolUpdate=True)
                            #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - pre COMBINED mortality'])
                            #self.objSSParametersLocal.stringEventMessage = 'Debug2; ' + self.objSSParametersLocal.stringEventMessage
                            #self.methodOutput_outputPopulationAgeClassTotals(pop_In, [False, False])
                            #self.methodOutput_outputPopulationLifeStageTotals(pop_In, [False, False])
                            #Pause for testing
                            #if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                            #    pass
                            #else:   
                            #    raw_input('\n Before COMBINED MORTALITY - Press return to close this window... \n')
                            #    pass
                            #DEBUG_OFF

                            ''' Reporting variable cleared at each mortality event '''
                            self.objSSParametersLocal.odictKilled_COMBINED_Per_Age_Class_By_Sex = OrderedDict()
                            self.objSSParametersLocal.odictKilled_COMBINED_Per_Life_Stage_By_Sex = OrderedDict()
                            self.objSSParametersLocal.odictSurvived_COMBINED_Per_Age_Class_By_Sex = OrderedDict()
                            self.objSSParametersLocal.odictSurvived_COMBINED_Per_Life_Stage_By_Sex = OrderedDict()
                
                            ''' Apply mortality to each sex separately '''
                            boolRemoveIndividuals = True
                            pop_In = self.method_SpecifyMortalityScheme(pop_In, globalsSS.MortalitySource.static_intMortalityType_COMBINED, globalsSS.SexConstants.static_stringSexMale, boolRemoveIndividuals)
                            pop_In = self.method_SpecifyMortalityScheme(pop_In, globalsSS.MortalitySource.static_intMortalityType_COMBINED, globalsSS.SexConstants.static_stringSexFemale, boolRemoveIndividuals)
                                                
                            self.objSSParametersLocal.stringEventMessage = '$$ COMBINED MORITALITY OCCURED - Deceased Individuals will be replaced at fertilization $$; ' + self.objSSParametersLocal.stringEventMessage
                             
                            #DEBUG_ON
                            # Output the summary of  age class totals(virtualSubPops) at each generation
                            #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post COMBINED mortality'])
                            #self.objSSParametersLocal.stringEventMessage = 'Debug2; ' + self.objSSParametersLocal.stringEventMessage
                            #self.methodOutput_outputPopulationAgeClassTotals(pop_In, [False, False])
                            #self.methodOutput_outputPopulationLifeStageTotals(pop_In, [False, False])
                            #Pause for testing
                            if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                                pass
                            else:   
                                #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post COMBINED mortality 2'])
                                #self.methodOutput_outputPopulationAgeClassTotals(pop_In, [False, False])
                                #self.methodOutput_outputPopulationLifeStageTotals(pop_In, [False, False])
                
                                #raw_input('\n After COMBINED MORTALITY - Press return to close this window... \n')
                                pass
                            #DEBUG_OFF
                         
                        #---- COMBINED MORTALITY END ----
                    pass
                
                    '''
                    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    FERTILIZATION - Choose Parents
                    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    '''
                    
                    stringEvent = string_const_EventMating
                        
                    pop_In = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop_In, boolUpdate=False)
                    
                    #MATING = Choose parents
                    self.objSSParametersLocal.stringEventMessage = '%% MATING OCCURED - Pregnancy results %%; ' + self.objSSParametersLocal.stringEventMessage
                
                    #DEBUG_ON
                    # Output the summary of  age class totals(virtualSubPops) at each generation
                    #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post ' + self.objSSParametersLocal.stringEventMessage])
                    #self.methodOutput_outputPopulationAgeClassTotals(pop_In, [False, False])
                    #self.methodOutput_outputPopulationLifeStageTotals(pop_In, [False, False])
                    #Pause for testing
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        pass
                    else:   
                        #raw_input('\n Location: ' + self.objSSParametersLocal.stringEventMessageLocal + ' BEFORE ' + self.objSSParametersLocal.stringEventMessage + ' - Press return to continue... \n')
                        pass
                    #DEBUG_OFF
                
                   
                    '''Determine the embryos required '''
                    intEmbryoNumberToBeGenerated = pop_In.subPopSize([globalsSS.SP_SubPops.static_intSP_SubPop_Primary,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Died])
                    
                    #DEBUG_ON
                    self.obj_Log_Debug_Display.debug('Embryos to be generated: ' + str(intEmbryoNumberToBeGenerated))
                    #with SSOutputHandler() as obj_SSOutputOperation:
                        #obj_SSOutputOperation.method_Pause_Console()
                    #DEBUG_OFF
                
                    '''
                    -------------------------
                    If pre-mating parent selection required
                    -------------------------
                    '''
                    if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Random_Mating_WITH_Replacement or \
                       self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Random_Mating_WITHOUT_Replacement:                         
                        '''
                        ---------------------------------
                        Select Putative Parent Pairs
                        ---------------------------------
                        '''
                                                
                        ''' Select enough parents to produce those embryos '''
                        self.method_SelectParents_Relative_To_Mating_Scheme(intEmbryoNumberToBeGenerated)
                    pass
                    #DEBUG_ON
                    # Output the summary of  age class totals(virtualSubPops) at each generation
                    #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post ' + self.objSSParametersLocal.stringEventMessage])
                    #self.methodOutput_outputPopulationAgeClassTotals(pop_In, [False, False])
                    #self.methodOutput_outputPopulationLifeStageTotals(pop_In, [False, False])
                    #Pause for testing
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        pass
                    else:   
                        #raw_input('\n Location: ' + self.objSSParametersLocal.stringEventMessageLocal + ' After ' + self.objSSParametersLocal.stringEventMessage + ' - Press return to continue... \n')
                        pass
                    #DEBUG_OFF
                    
                    #--- MATING END ---
                
                    '''
                    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    FERTILIZATION - Mating
                    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    '''                        
                    
                    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FERTILIZATION - Perform AGING, FERTILIZATION and produce EMBRYOS
                
                    stringEvent = string_const_EventFertilization
                    #DEBUG_ON
                    # Output the summary of  age class totals(virtualSubPops) at each generation
                    #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post ' + self.objSSParametersLocal.stringEventMessage])
                    #self.methodOutput_outputPopulationAgeClassTotals(pop_In, [False, False])
                    #self.methodOutput_outputPopulationLifeStageTotals(pop_In, [False, False])
                    #Pause for testing
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        pass
                    else:   
                        #raw_input('\n Location: ' + self.objSSParametersLocal.stringEventMessageLocal + ' After ' + self.objSSParametersLocal.stringEventMessage + ' - Press return to continue... \n')
                        pass
                    #DEBUG_OFF
                    
                    self.objSSParametersLocal.stringEventMessageLocal = ' !! FERTILIZATION OCCURED !!; ' + self.objSSParametersLocal.stringEventMessage
                    self.objSSParametersLocal.stringEventMessage = self.objSSParametersLocal.stringEventMessageLocal + self.objSSParametersLocal.stringEventMessage
                
                    self.objSSParametersLocal.intCurrentTemporalFertilisation += 1
                    
                    '''
                    ---------------------
                    Open PF Loggers
                    ---------------------
                    '''
                    self.method_Open_Log_Files_PF_Per_Fertilization()

                    '''
                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    >>>>>>>>>>>>>>>>>>> START - Evolve with Mating
                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    '''
                                        
                    '''
                    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    LIFE STAGE update by LIFE_STAGE
                    Always perform before FERTILIZATION event in order to terminate old animals and make room in the population
                    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    '''
                    #pop_In = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(pop_In, boolUpdate=True)
                    pop_In = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop_In, boolUpdate=False)

                    list_Simupop_Evolve_Function_InitOps = []
                    list_Simupop_Evolve_Function_PreOps = []                    
                    pop_In = self.method_EvolvePedigreeWithMating(pop_In, self.objSSParametersLocal.intSimulationCurrentMonth / 12, list_Simupop_Evolve_Function_InitOps, list_Simupop_Evolve_Function_PreOps)
                    
                    ''' NOTE >>> The pop was split by AgeClass when EVOLVE finished '''
                    
                    '''
                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    >>>>>>>>>>>>>>>>>>> END - Evolve with Mating
                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    '''
                    
                    '''
                    ------------------------------------------
                    REPLICATE ABORT Check - Abort GRACEFULLY if the number of parents drops below threshold 
                    ------------------------------------------
                    '''
                    bool_ABORT_Replicate__Too_Few_Mating_Individuals = True
                    if bool_ABORT_Replicate__Too_Few_Mating_Individuals:                
                        with SSAnalysisHandler() as SSAnalysisOperation:
                            pop_In = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop_In, boolUpdate=False)
                            listCountofMaleFemale = []
                            if self.objSSParametersLocal.intGestationLengthInMonths > 12:
                                listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult)
                            else:
                                listCountofMaleFemale_Reproductively_Available = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult)
                                listCountofMaleFemale_Gestating = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Gestating_adult_female)
                                listCountofMaleFemale_Resting = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Resting_adult_female)
                                listCountofMaleFemale.append(listCountofMaleFemale_Reproductively_Available[0])
                                listCountofMaleFemale.append(listCountofMaleFemale_Reproductively_Available[1] + listCountofMaleFemale_Gestating[1] + listCountofMaleFemale_Resting[1])
                            pass
                            self.obj_Log_Debug_Display.debug('SEX COUNT - Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))   
                            #raw_input('\n Before COMBINED MORTALITY - Press return to close this window... \n')
                            if self.objSSParametersLocal.boolAllowNATURALMortality:
                                int_Abort_Replicate__Reproductively_Available_Indivs__Cutoff = 10
                                
                                int_Mating_Mortality_Quota_Total_Male = int_Abort_Replicate__Reproductively_Available_Indivs__Cutoff
                                int_Mating_Mortality_Quota_Total_Female = int_Abort_Replicate__Reproductively_Available_Indivs__Cutoff
                                if listCountofMaleFemale[0] <= int_Mating_Mortality_Quota_Total_Male or \
                                   listCountofMaleFemale[1] <= int_Mating_Mortality_Quota_Total_Female:
                                    self.obj_Log_Default_Display.error('REPLICATE ABORT - Post Mating - Parent threshold exceeded: ' + str(int_Abort_Replicate__Reproductively_Available_Indivs__Cutoff) + ' SEX COUNT - Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))
                                    self.bool_Abort_Processing_Gracefully = True
                                    return pop_In
                                pass
            
                            if self.objSSParametersLocal.boolAllowUnNATURALMortality:
                                bool_Start_UnNatural_Mortality = False
                                int_Current_Replicate_Mating_Count = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                                int_Mating_Mortality_Starts__UnNat = self.objSSParametersLocal.dict_Mortality_Application_Specs_By_Sex__UnNATURAL[globalsSS.MortalityApplication.static_str_Mating_Mortlity_Starts__UnNat][globalsSS.SexConstants.static_stringSexMale]
                                if int_Current_Replicate_Mating_Count >= int_Mating_Mortality_Starts__UnNat:
                                    bool_Start_UnNatural_Mortality = True
                                pass
                                ''' Get Scaled UnNatural Survival Numbers for a sex'''
                                if bool_Start_UnNatural_Mortality:    
                                    ''' Get the size of the QUOTA of animals to kill '''
                                    int_Mating_Mortality_Quota_Total_Male = self.objSSParametersLocal.dict_Mortality_Application_Specs_By_Sex__UnNATURAL[globalsSS.MortalityApplication.static_str_Mortality_Scaling_Total__UnNat][globalsSS.SexConstants.static_stringSexMale]
                                    int_Mating_Mortality_Quota_Total_Female = self.objSSParametersLocal.dict_Mortality_Application_Specs_By_Sex__UnNATURAL[globalsSS.MortalityApplication.static_str_Mortality_Scaling_Total__UnNat][globalsSS.SexConstants.static_stringSexFemale]
    
                                    if listCountofMaleFemale[0] <= int_Mating_Mortality_Quota_Total_Male or \
                                       listCountofMaleFemale[1] <= int_Mating_Mortality_Quota_Total_Female:
                                        self.obj_Log_Default_Display.error('REPLICATE ABORT - Post Mating - Parent threshold exceeded: Male: ' + str(int_Mating_Mortality_Quota_Total_Male) + ' or Female: ' + str(int_Mating_Mortality_Quota_Total_Female) + ' SEX COUNT - Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))
                                        self.bool_Abort_Processing_Gracefully = True
                                        return pop_In
                                    pass
                                pass
                            pass
                        pass
                    pass 
                                         
#                     '''
#                     -------------------------
#                     If post-mating parent selection required
#                     -------------------------
#                     '''
#                     if not \
#                       (self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Random_Mating_WITH_Replacement or \
#                        self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Random_Mating_WITHOUT_Replacement):                         
#                 
#                         '''
#                         ---------------------------------
#                         Post-Mating Operations
#                         Female: Update LIFE_STAGE to GESTATING
#                         ---------------------------------
#                         '''
#                         ''' Effective Females: Update LIFE_STAGE to GESTATING'''
#                         pop_In = self.method_Effective_Parent_Post_Mating_Operations(pop_In)
#                     pass
                
                    '''
                    ---------------------------------
                    Post-Mating GENEPOP File export of selected life stages
                    ---------------------------------
                    '''
                    if self.objSSParametersLocal.bool_Export_Genepop_PF_Files:
                        if self.objSSParametersLocal.bool_Export_Genepop_PF_Files_During_BurnIn:
                            if self.objSSParametersLocal.int_MatingCount_Replicate_Total >= self.objSSParametersLocal.int_Genpop_For_BioP_Saving_Starts__Replicate_Mating_Count:
                                int_Replicate_Mating_Count_Div = float(self.objSSParametersLocal.int_MatingCount_Replicate_Total) / float(self.objSSParametersLocal.int_Genpop_For_BioP_Save_Every__Replicate_Mating_Count) 
                                bool_Save_Genepop_For_BioP = (int_Replicate_Mating_Count_Div).is_integer()
                                if bool_Save_Genepop_For_BioP:
                                    pop_In = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(pop_In, boolUpdate=False)
                                    #pop_In = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop_In, boolUpdate=False)
                                    self.method_Output_Genpop_File_PF_Per_Fertilization(pop_In)
                                pass
                            pass
                        pass
                    pass
                
                    '''
                    LIFE STAGE has been updated by fertilization - Reproductively available ----> Gestating
                    This occcurs when a female is paired to a male in the random parent pair choosing during mating/fertilization
                    '''
                
                    self.objSSParametersLocal.intYearReproductiveCycleCurrentMonth = 0
#                 
#                     '''
#                     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                     LIFE STAGE change from immature to mature
#                     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                     '''
#                     pop_In = self.method_SplitLifeStagesIntoVSPs_By_Age_In_Months_Updating_Life_Stage_Juvenile_To_Adult(pop_In)
                
#                     '''
#                     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                     GESTATION/RESTING LIFE STAGE update - Post-fertilization
#                     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                     '''
#                 
#                     #DEBUG_ON
#                     #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post ' + self.objSSParametersLocal.stringEventMessage])
#                     #DEBUG_OFF
#                                             
#                     pop_In = self.method_SplitLifeStagesIntoVSPs_By_Gestation_Month_Count_SPLITTING_Life_Stage_Into_Resting_Or_Gestating(pop_In, boolUpdate=True)
#                 
#                     #DEBUG_ON
#                     #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post ' + self.objSSParametersLocal.stringEventMessage])
#                     #DEBUG_OFF
#                     
#                     pop_In = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop_In, boolUpdate=False)
                
                    #DEBUG_ON
                    # Output the summary of  age class totals(virtualSubPops) at each generation
                    #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post ' + self.objSSParametersLocal.stringEventMessage])
                    self.methodOutput_outputPopulationAgeClassTotals(pop_In, [False, False])
                    self.methodOutput_outputPopulationLifeStageTotals(pop_In, [False, False])
                    #Pause for testing
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        #raw_input('\n Location: ' + self.objSSParametersLocal.stringEventMessageLocal + ' After ' + self.objSSParametersLocal.stringEventMessage + ' - Press return to continue... \n')
                        pass
                    else:   
                        #raw_input('\n Location: ' + self.objSSParametersLocal.stringEventMessageLocal + ' After ' + self.objSSParametersLocal.stringEventMessage + ' - Press return to continue... \n')
                        pass
                    #DEBUG_OFF
                
                
                    '''
                    ---------------------------------
                    FERTILIZATION STAGE REPORTING 
                    ---------------------------------
                    '''                        
                   
                    '''
                    ~~~~~~~~~~~~~~~~
                    AgeNE Stats Gathering
                    ~~~~~~~~~~~~~~~~
                    '''
                    if self.objSSParametersLocal.int_MatingCount_Replicate_Total >= self.objSSParametersLocal.intAgeNe_Data_Collection_Start__Replicate_Mating_Count:
                        self.method_AgeNe_PF_Stats_Gathering(pop_In)
                    pass                    
                    
                    if self.objSSParametersLocal.boolBurnIn == False: #and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        '''
                        ---------------------------------
                        NE Custom 1 STATS
                        ---------------------------------
                        '''
                        with SSOutputHandler() as SSOutputOperation:
                            listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                            #
                            SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Gathering Post-Fertilisation AgeNe Stats', boolIsHeader=True, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
                        
                        #self.method_AgeNe_PF_Stats_Gathering(pop_In)  
                                                  
                        with SSOutputHandler() as SSOutputOperation:
                            listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                            #
                            SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Gathering Post-Fertilisation AgeNe Stats', boolIsHeader=False, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
                
                        listVSPsToExperimentOn = [(0,1)]
                        self.method_In_Sim_Reporting_NEStatistics(listVSPsToExperimentOn)
                        #raw_input('\n After FERTILIZATION NE STATS - Press return to continue... \n')
                        pass
                    pass
                    #else:
                    '''
                    ---------------------------------
                    POST-FERTILIZATION LEVEL STATS
                    ---------------------------------
                    '''
                    
                    self.method_Post_Fertilization_Reporting(pop_In)
                    pass
                '''    
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                PARTURITION - GESTATION period has elapsed so perform PARTURITION
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                '''
                
                pop_In = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop_In, boolUpdate=True)
                   
                #DEBUG_ON
                #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post ' + self.objSSParametersLocal.stringEventMessage])
                #self.methodOutput_outputPopulationAgeClassTotals(pop_In,[False, False])
                #self.methodOutput_outputPopulationLifeStageTotals(pop_In, [False, False])
                #Pause for testing
                #raw_input('\n After ' + self.objSSParametersLocal.stringEventMessage + ' - Press return to continue... \n')
                #DEBUG_OFF
                
                #if self.objSSParametersLocal.boolGestating:
                if self.objSSParametersLocal.intYearCurrentMonth == self.objSSParametersLocal.intParturitionCalenderMonth:
                    stringEvent = string_const_EventParturition
                    #PARTURITION = SimuPOP Evolve with mating given parents mated (simupop chosen) several months before therby simulating gestation time
                    self.objSSParametersLocal.stringEventMessageLocal = ' ** PARTURITION OCCURED **; '
                    self.objSSParametersLocal.stringEventMessage = self.objSSParametersLocal.stringEventMessageLocal + self.objSSParametersLocal.stringEventMessage
                    
                    #DEBUG_ON
                    #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post ' + self.objSSParametersLocal.stringEventMessage])
                    self.methodOutput_outputPopulationAgeClassTotals(pop_In,[False, False])
                    self.methodOutput_outputPopulationLifeStageTotals(pop_In, [False, False])
                    #Pause for testing
                    #raw_input('\n Location: ' + self.objSSParametersLocal.stringEventMessageLocal + ' After ' + self.objSSParametersLocal.stringEventMessage + ' - Press return to continue... \n')
                    #DEBUG_OFF
                    
                if self.objSSParametersLocal.intYearCurrentMonth == 12:
                    stringEvent = string_const_EventEOCY
                    boolEOCY = True
                    self.objSSParametersLocal.stringEventMessage = 'End of Calendar year; ' + self.objSSParametersLocal.stringEventMessage
                    
                if stringEvent != string_const_EventEOCY and \
                   stringEvent != string_const_EventEORY and \
                   stringEvent != string_const_EventMating and \
                   stringEvent != string_const_EventFertilization and \
                   stringEvent != string_const_EventParturition:
                    stringEvent = string_const_EventEOCM
                    self.objSSParametersLocal.stringEventMessageLocal = 'End of month; '
                    self.objSSParametersLocal.stringEventMessage = self.objSSParametersLocal.stringEventMessageLocal + self.objSSParametersLocal.stringEventMessage
                pass
                
                
                '''
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                MONTHLY AGEING - Age the population and update appropriate info fields
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                '''
                
                #DEBUG_ON
                #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post ' + self.objSSParametersLocal.stringEventMessage])
                #self.methodOutput_outputPopulationAgeClassTotals(pop_In,[False, False])
                #self.methodOutput_outputPopulationLifeStageTotals(pop_In, [False, False])
                #Pause for testing
                #raw_input('\n After ' + self.objSSParametersLocal.stringEventMessage + ' - Press return to continue... \n')
                #DEBUG_OFF
                
                '''
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                AGE CLASS & LIFE STAGE - Initial MONTH END update of appropriate info fields
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                '''
                ''' >>>>>>> AGE_IN_MONTHS update '''
                simupop.infoExec(pop_In, 'age_in_months += 1')
                ''' >>>>>>> AGE CLASS update by AGE_IN_MONTHS '''
                pop_In = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(pop_In, boolUpdate=True)
                ''' >>>>>>> LIFE STAGE update by AGE CLASS '''
                pop_In = self.method_SplitLifeStagesIntoVSPs_By_VSP_AgeClass_Updating_LifeStage(pop_In, boolUpdate=True) #<-----
                ''' >>>>>>> LIFE STAGE update GESTATION & RESTING by GESTATION_MONTH_COUNT '''
                pop_In = self.method_SplitLifeStagesIntoVSPs_By_Gestation_Month_Count_SPLITTING_Life_Stage_Into_Resting_Or_Gestating(pop_In, boolUpdate=True)
                ''' >>>>>>> LIFE STAGE update PRE-ADULT LIFE_STAGES '''
                pop_In = self.method_SplitLifeStagesIntoVSPs_By_Age_In_Months_Updating_Pre_Adult_Life_Stages(pop_In)
                
                '''
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                GESTATION/RESTING LIFE STAGE and COUNTDOWN update - End of month
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                '''
                
                bool_Gest_Rest = True
                if bool_Gest_Rest:
                
                    '''
                    ---------------------------------
                    GESTATION & RESTING month count decrement
                    ---------------------------------
                    '''
                    pop_In = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop_In, boolUpdate=False)
                    
                    #DEBUG_ON
                    #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post ' + self.objSSParametersLocal.stringEventMessage])
                    #DEBUG_OFF
                
                    if pop_In.subPopSize([globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult]) > 0:
                
                        simupop.infoExec(pop_In, 'gestation_resting_countdown = 0', subPops=[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult)])
                
                    pass
                    if pop_In.subPopSize([globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Gestating_adult_female]) > 0:
                
                        simupop.infoExec(pop_In, 'gestation_resting_countdown -= 1', subPops=[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Gestating_adult_female)])
                
                    pass
                    if pop_In.subPopSize([globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Resting_adult_female]) > 0:
                
                        simupop.infoExec(pop_In, 'gestation_resting_countdown -= 1', subPops=[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Resting_adult_female)])
                
                    pass
                
                    '''
                    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    AGE CLASS & LIFE STAGE - Final MONTH END update of appropriate info fields
                    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    '''
                
                    ''' >>>>>>> AGE CLASS update by AGE_IN_MONTHS '''
                    pop_In = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(pop_In, boolUpdate=True)
                    ''' >>>>>>> LIFE STAGE update by AGE CLASS '''
                    pop_In = self.method_SplitLifeStagesIntoVSPs_By_VSP_AgeClass_Updating_LifeStage(pop_In, boolUpdate=True) #<-----
                    ''' >>>>>>> LIFE STAGE update GESTATION & RESTING by GESTATION_MONTH_COUNT '''
                    pop_In = self.method_SplitLifeStagesIntoVSPs_By_Gestation_Month_Count_SPLITTING_Life_Stage_Into_Resting_Or_Gestating(pop_In, boolUpdate=True)
                    ''' >>>>>>> LIFE STAGE update PRE-ADULT LIFE_STAGES '''
                    pop_In = self.method_SplitLifeStagesIntoVSPs_By_Age_In_Months_Updating_Pre_Adult_Life_Stages(pop_In)
                pass
                
                #DEBUG_ON
                #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post ' + self.objSSParametersLocal.stringEventMessage])
                #self.methodOutput_outputPopulationAgeClassTotals(pop_In,[False, False])
                #self.methodOutput_outputPopulationLifeStageTotals(pop_In, [False, False])
                #Pause for testing
                #raw_input('\n Location: ' +self.objSSParametersLocal.stringEventMessageLocal + ' After ' + self.objSSParametersLocal.stringEventMessage + ' - Press return to continue... \n')
                #DEBUG_OFF
                
                '''
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                END OF MONTH REPORTING
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                '''
                
                self.objSSParametersLocal.stringEventMessage = 'END OF MONTH AGING; ' + self.objSSParametersLocal.stringEventMessage
                
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    self.methodOutput_outputPopulationTemporalProcessingSummaryInfo(pop_In, [False, False])
                    
                #DEBUG_ON
                #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post ' + self.objSSParametersLocal.stringEventMessage])
                #self.methodOutput_outputPopulationAgeClassTotals(pop_In,[False, False])
                #self.methodOutput_outputPopulationLifeStageTotals(pop_In, [False, False])
                #Pause for testing
                #raw_input('\n After ' + self.objSSParametersLocal.stringEventMessage + ' - Press return to continue... \n')
                #DEBUG_OFF
                
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> COUNTER INCREMENTATION
                
                self.objSSParametersLocal.intSimulationCurrentMonth += 1
                self.objSSParametersLocal.intYearCurrentMonth += 1
                self.objSSParametersLocal.intYearReproductiveCycleCurrentMonth += 1
                
                #                     if self.objSSParametersLocal.boolGestating:
                #                         self.objSSParametersLocal.intGestationCurrentMonth += 1   
                
                if boolEOCY:
                    self.objSSParametersLocal.intYearCurrentMonth = 1
                    boolEOCY = False
                                
                pop_Out = pop_In
                       
                return pop_Out

            #--------------------------------------------------------------------------------------------------------
            # Evolve Processing
            #--------------------------------------------------------------------------------------------------------


            def method_TemporalPopulationProcessing_PROTOTYPE(self):
              
                intPopSize = 240
                maxAge = 5
                maxMatingAge = 4
                minMatingAge = 2
                intGestationLength = 1
                gen = 20
                intLoci = 2
                listAlleleFreqs = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125] #Also defines Num alleles per locus
                #listAlleleFreqs = [0.25, 0.25, 0.25, 0.25] #Also defines Num alleles per locus
                #listAlleleFreqs = [0.5, 0.5] #Also defines Num alleles per locus
                
                # Generate list of loci names
                with SSOutputHandler() as objSSOutputOperation:
                    listLociNames = objSSOutputOperation.AutomaticLociNamesList(intLoci)


                self.pop = simupop.Population(
                                              intPopSize
                                              ,loci=[1]*intLoci
                                              ,lociNames=listLociNames
                                              , infoFields=['ind_id','age','age_in_months','father_id','mother_id']
                                              )
                #self.pop.setIndInfo([numpy__random.randint(0, maxAge) for x in range(intPopSize)], 'age')
                
                listAgesInYears = []
                for intAgeInYears in range(0, maxAge, 1):
                    listAgesInYears.append(intAgeInYears)
                self.pop.setIndInfo(listAgesInYears, 'age')
                
                listAgesInMonths = []
                for intAgeInMonths in range(0, maxAge*12, 12):
                    listAgesInMonths.append(intAgeInMonths)
                self.pop.setIndInfo(listAgesInMonths, 'age_in_months')
                
                listAgesInYears = [x / 12 for x in listAgesInMonths]
                self.pop.setIndInfo(listAgesInYears, 'age')
                
                # define virtual subpopulations
                self.pop.setVirtualSplitter(simupop.InfoSplitter('age_in_months',
                cutoff=[
                        intGestationLength*12 #(0,0)
                        ,minMatingAge*12 # (0,1)
                        ,maxMatingAge*12 # (0,2)
                        ,maxAge*12        # (0,3)
                        #Died (0,4)
                        ]))     

                ''' initialise sex by VSP '''
                intNumberVirtualSubPops = self.pop.numVirtualSubPop()
                for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                    simupop.initSex(self.pop, maleProp=0.5, subPops=[(0,intVirtualSubPop)])
                pass
                #simupop.initSex(self.pop, maleProp=0.5)
                #simupop.initSex(pop, sex=[simupop.MALE, simupop.FEMALE])
                simupop.initGenotype(self.pop, freq=listAlleleFreqs)
                simupop.IdTagger().reset(1)
            

                for intGen in range(0, gen):
                    
                    if intGen == 0:
                        list_Simupop_Evolve_Function_InitOps = [simupop.IdTagger()]
                    else:
                        list_Simupop_Evolve_Function_InitOps = []
                    pass
                
                    self.pop = self.method_EvolvePedigreeWithMating_PROTOTYPE_3B(self.pop, intGen, list_Simupop_Evolve_Function_InitOps)

                    simuPOP__utils.export(self.pop, format='GENEPOP', adjust=1, output= self.objSSParametersLocal.outfilePath + 'genepop_VSP_0_0_Gen_' + str(intGen).zfill(3) + globalsSS.Genepop_Details.static_Output_File_Suffix__Genepop_Pop_Data_EOR_POP, gui=False, subPops=[(0,0)])
                    simuPOP__utils.export(self.pop, format='GENEPOP', adjust=1, output=self.objSSParametersLocal.outfilePath + 'genepop_SP_0_Gen_' + str(intGen).zfill(3) + '.txt', gui=False)
                    #DEBUG_OFF
                pass
            
                #DEBUG_ON
                simuPOP__utils.export(self.pop, format='GENEPOP', adjust=1, output=self.objSSParametersLocal.outfilePath + 'genepop_VSP_0_0_Gen_' + str(intGen).zfill(3) + '_Final.txt', gui=False, subPops=[(0,0)])
                simuPOP__utils.export(self.pop, format='GENEPOP', adjust=1, output=self.objSSParametersLocal.outfilePath + 'genepop_SP_0_Gen_' + str(intGen).zfill(3) + '_Final.txt', gui=False)
                #DEBUG_OFF     
                
                return self.pop

            '''@profile'''
            def method_Initial_Advance_of_Ages_RETIRED(self):
                
                self.pop = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(self.pop, boolUpdate=True)
                self.pop = self.method_SplitLifeStagesIntoVSPs_By_VSP_AgeClass_Updating_LifeStage(self.pop, boolUpdate=True)
                
                
                #>>>>>>>> IMPORTANT - Adjust ages of population to align with mating month in simulation run
                
                '''
                First check if overlapping gens are being modeled
                '''
                if self.objSSParametersLocal.bool_Overlapping_Gens_Simulation == False:
                    intAdvanceLifeStageAge1 = (-self.objSSParametersLocal.intMatingCalenderMonth)+1 #+1 because the embryos are currently 0 age
                    pass
                else:
                
                    #Push the Embryo life stage forward to ensure that birth occurs at first parturition month irrelevant of how long the gestation length is
                    #intAdvanceLifeStageAge1 = (self.objSSParametersLocal.intGestationLengthInMonths - (self.objSSParametersLocal.intParturitionCalenderMonth))
                    if self.objSSParametersLocal.intGestationLengthInMonths > 12:
                        intAdvanceLifeStageAge1 = (12+(12-self.objSSParametersLocal.intMatingCalenderMonth))+1  #+1 because the embryos are currently 0 age
                    else:                    
                        intAdvanceLifeStageAge1 = (12-(self.objSSParametersLocal.intMatingCalenderMonth))+1  #+1 because the embryos are currently 0 age
                    pass
                pass
            
                self.pop = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(self.pop, boolUpdate=False)
                
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    listVSPs = objSSAnalysisOperation.method_Get_VSP_List(self.pop, boolReportVSPIfEmpty=False)
                    
                    for tupVSP in listVSPs:
                        simupop.infoExec(self.pop, 'age_in_months+=' + str(intAdvanceLifeStageAge1), subPops=[tupVSP])
                    pass
                pass
            
                #self.methodOutput_outputPopulationDump(self.pop)
                self.methodOutput_outputPopulationAgeClassTotals(self.pop, [False, False])
                self.methodOutput_outputPopulationLifeStageTotals(self.pop, [False, False])
                
                with SSOutputHandler() as SSOutputOperation:
                    listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    #SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, '')
                    #
                    stringMessage = ' Advance ages by intAdvanceLifeStageAge1 = ' + str(intAdvanceLifeStageAge1)  +'\n'
                    boolNewline=True
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                    #
                    #stringMessage = ' Advance ages by intAdvanceLifeStageAge2 = ' + str(intAdvanceLifeStageAge2)  +'\n'
                    #boolNewline=True
                    #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                    #
                    #SSOutputOperation.methodOutput_SimGeneralMessageFooter(listOutputDestinations, '')

                #print('\n Advance ages by intAdvanceLifeStageAge1 = ' + str(intAdvanceLifeStageAge1))
                #print('\n Advance ages by intAdvanceLifeStageAge2 = ' + str(intAdvanceLifeStageAge2))
                #raw_input('\n After Advance ages - Press return to close this window... \n')
                #DEBUG_OFF
                
                return True
            
            '''@profile'''
            def method_ImportPopulationFromFile(self):         
                
                'Read data from ``filename`` and create a population'
                data = open(self.objSSParametersLocal.inputFileNameInitialPopulation)
                header = data.readline()
                fields = header.split(',')
                # columns 1, 3, 5, ..., without trailing '_1'
                intImportFileStartColumn = 2
                names = [fields[x].strip()[:-2] for x in range(intImportFileStartColumn, len(fields), 2)]
                popSize = 0
                alleleNames = set()
                for line in data.readlines():
                    # get all allele names
                    alleleNames |= set([x.strip() for x in line.split(',')[1:]])
                    popSize += 1
                # create a population
                alleleNames = list(alleleNames)
                #pop = simupop.Population(size=popSize, loci=len(names), lociNames=names,
                #    alleleNames=alleleNames)
                self.objSSParametersLocal.popnSize = popSize
                self.objSSParametersLocal.nLoci = len(names)
                self.objSSParametersLocal.listLociNames = names

                pop = simupop.Population(self.objSSParametersLocal.popnSize,
                                     infoFields=self.objSSParametersLocal.ssinfoFields,
                                     loci=[self.objSSParametersLocal.nLoci], lociNames=self.objSSParametersLocal.listLociNames
                                     #,ancGen=-1
                                    )

                # start from beginning of the file again
                data.seek(0)
                # discard the first line
                data.readline()
                for ind, line in zip(pop.individuals(), data.readlines()):
                    fields = [x.strip() for x in line.split(',')]
                    sex = simupop.MALE if fields[0] == '1' else simupop.FEMALE
                    ploidy0 = [alleleNames.index(fields[x]) for x in range(1, len(fields), 2)]
                    ploidy1 = [alleleNames.index(fields[x]) for x in range(2, len(fields), 2)]
                    ind.setGenotype(ploidy0, 0)
                    ind.setGenotype(ploidy1, 1)
                    ind.setSex(sex)
                # close the file
                data.close()
                
                #DEBUG_ON
                #self.methodOutput_outputPopulationDump(self.pop)
                #self.methodOutput_outputPopulationAgeClassTotals(self.pop, [False, True])
                #DEBUG_OFF
                
                return pop
            
            '''@profile'''
            def method_InitialisePopulations(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass      
                           
                #print('\n <<<<<<<<<<<<<<<<<<< method_InitialisePopulations - START   <<<<<<<<<<<<<<<<<<<<<\n')

                #Reset Unique Individual IDs for each replicate
                simupop.IdTagger().reset(1)

                #Either import initial population from file or create from scratch
                boolImportPopulationFromFile = False
                if boolImportPopulationFromFile:
                    
                    pop_In = self.method_Population_Creation_From_File()

                else:
                    #pop_In = self.method_Population_Creation_From_Scratch()

                    #Define the population initial parameters and info fields
                    pop_In = simupop.Population(self.objSSParametersLocal.popnSize
                                         ,infoFields=self.objSSParametersLocal.ssinfoFields
                                         ,ploidy=2
                                         ,loci=[1]*self.objSSParametersLocal.nLoci
                                         ,chromTypes=[simupop.AUTOSOME]*self.objSSParametersLocal.nLoci
                                         ,lociNames=self.objSSParametersLocal.listLociNames
                                        )
#                     pop_In = simupop.Population(self.objSSParametersLocal.popnSize
#                                          ,infoFields=self.objSSParametersLocal.ssinfoFields
#                                          ,ploidy=2
#                                          ,loci=self.objSSParametersLocal.nLoci
# #                                         ,chromTypes=[simupop.AUTOSOME]*self.objSSParametersLocal.nLoci
#                                          ,lociNames=self.objSSParametersLocal.listLociNames
#                                         )

                    pop_In = self.method_Initialise_Ages(pop_In)

                pass
            
                '''
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Initialise InfoFields
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                '''            
                simupop.infoExec(pop_In, 'birth_generation=0')
                simupop.infoExec(pop_In, 'gestation_resting_countdown=0')
            
                '''
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Initialise SEX
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                '''
                if self.objSSParametersLocal.intOffspringSexScheme == globalsSS.MatingOffspringSexModeSchemeType.static_int_Mating_Offspring_Sex_Mode_PROB_OF_MALES:
                    simupop.initSex(pop_In, maleProp=self.objSSParametersLocal.floatSexRatioOfMales)
                elif self.objSSParametersLocal.intOffspringSexScheme == globalsSS.MatingOffspringSexModeSchemeType.static_int_Mating_Offspring_Sex_Mode_GLOBAL_SEQ_OF_SEX_MF:
                    simupop.initSex(pop_In, sex=[simupop.MALE, simupop.FEMALE])
                else:
                    simupop.initSex(pop_In, sex=[simupop.MALE, simupop.FEMALE])
                pass

                '''
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Initialise PEDIGREE TAGGER
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                '''            
                simupop.IdTagger().reset(1)
                
                '''
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Initialise GENOTYPES
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                '''
                if self.objSSParametersLocal.boolInitGenotypeByVSP:                                         
                    # Assign genotypes with the allele frequencies specified
                    self.method_InitGenotypes_ByLoci_ByVSP(pop_In, param=[(0,0),(0,1),(0,2),(0,3)])
                elif self.objSSParametersLocal.boolInitGenotypeByLoci: 
                    # Assign genotypes with the allele frequencies specified
                    pop_In = self.method_InitGenotypes_ByLoci(pop_In)
                else:
                    pop_In = self.method_InitGenotypes(pop_In)
                    
                #Get the initial allele freqencies at the population level
                listSubPops = []
                listSubPops.append(globalsSS.SP_SubPops.static_intSP_SubPop_Primary)
                self.method_SimStat_AlleleFreq_Reporting(pop_In, listSubPops)
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    self.objSSParametersLocal.odictAlleleFreqsAtPopInitialization = objSSAnalysisOperation.method_Statistics_On_Allele_Frequencies_For_VirtualSubPop(pop_In, listSubPops)
                    
                #DEBUG_ON
                #self.method_OutputPopulationOffspringTotalsByParent(pop_In, param=1)
                #DEBUG_OFF
                #DEBUG_ON            
                # Output the summary of  age class totals(virtualSubPops) at each generation
                #self.methodOutput_outputPopulationDump(pop_In, ['method_InitialisePopulations 2'])
                self.methodOutput_outputPopulationAgeClassTotals(pop_In, [False, True])
                #!!!!!!!!!!!!!!!Have to split again after methodOutput_outputPopulationAgeClassTotals or else VSPs are wrong and aging doesnt occur
                # Split the ages into each virtual subpopulation
                pop_In = self.method_SplitLifeStagesIntoVSPs_By_AgeInYears(pop_In)
                #self.method_SplitLifeStagesIntoVSPs_ForBurnIn_By_AgeInMonths(boolDisplayOnly=False)
                pop_In = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(pop_In, boolUpdate=True)
                #
                #self.methodOutput_outputPopulationDump(pop_In, ['method_InitialisePopulations 3'])
                self.methodOutput_outputPopulationAgeClassTotals(pop_In, [False, True])
                #Pause for testing
                #raw_input('\n After AGE_SPLIT during INITILIZATION - Press return to close this window... \n')
                #DEBUG_OFF


                #print('\n <<<<<<<<<<<<<<<<<<< method_InitialisePopulations - END   <<<<<<<<<<<<<<<<<<<<<\n')

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    bool_Debug_Display__Sex_Count = True
                    if bool_Debug_Display__Sex_Count:                
                        with SSAnalysisHandler() as SSAnalysisOperation:
                            listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary)
                            self.obj_Log_Debug_Display.debug('SEX COUNT - Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))   
                        pass
                    pass
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    #pause
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass                 
                pop_Out = pop_In
                
                return pop_Out
            
            
            def method_Population_Creation_From_Scratch_RETIRE(self):
                
#                 list_Allele_Names = []
#                 if self.objSSParametersLocal.boolObtainAlleleFrequenciesFromFile:
#                     list_Allele_Names = self.objSSParametersLocal.listAlleleNames_EntireNested
#                 pass    
                    
                #Define the population initial parameters and info fields
                pop_Out = simupop.Population(self.objSSParametersLocal.popnSize
                                     ,infoFields=self.objSSParametersLocal.ssinfoFields
                                     ,ploidy=2
                                     ,loci=[1]*self.objSSParametersLocal.nLoci
                                     ,chromTypes=[simupop.AUTOSOME]*self.objSSParametersLocal.nLoci
                                     ,lociNames=self.objSSParametersLocal.listLociNames
                                     #,alleleNames=list_Allele_Names
                                     #loci=self.objSSParametersLocal.nLoci, lociNames=self.objSSParametersLocal.listLociNames
                                     #,ancGen=-1
                                    )
            
                return pop_Out

            '''@profile'''
            def method_Initialise_Ages(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
                                    
                listAgesInYears = []
                listAgesInMonths = []
                #If ages are to be randoimised
                if self.objSSParametersLocal.intPopulationInitialAges == globalsSS.InitialAgeDistribution.static_EvenAgeAndNumberSpreadAcrossLifeStages:
                    
                    intNumInEachAgeClass = self.objSSParametersLocal.popnSize / globalsSS.VSP_AgeClass.static_intVSP_AgeClass_NumberofVSPs
                    for intAgeInYears in range(0, self.objSSParametersLocal.maxAge):
                        listAgesInYears.append(intAgeInYears)
                        listAgesInMonths.append((intAgeInYears*12)+self.objSSParametersLocal.intGestationLengthInMonths)
                    
                elif self.objSSParametersLocal.intPopulationInitialAges == globalsSS.InitialAgeDistribution.static_RandomAgeAndNumberSpreadAcrossLifeStages:
                    #Individuals are initialized with random ages between 0 and maxAge.
                    for x in range(self.objSSParametersLocal.popnSize):
                        intAgeInYears = numpy__random.randint(0, self.objSSParametersLocal.maxAge)
                        listAgesInYears.append(intAgeInYears)
                        listAgesInMonths.append((intAgeInYears*12)+self.objSSParametersLocal.intGestationLengthInMonths)

                elif self.objSSParametersLocal.intPopulationInitialAges == globalsSS.InitialAgeDistribution.static_SameAgeAndEvenSpreadAcrossLifeStages_1CohortPerLifeStage:
                    #Check if there is any need for an embryo population (there isnt when the gestation length is zero as in most discrete generations sims
                    if self.objSSParametersLocal.intGestationLengthInMonths > 0:
                    #                         listAgesInMonths.append(self.objSSParametersLocal.intGestationLengthInMonths-12)
                    #                         listAgesInMonths.append(self.objSSParametersLocal.intGestationLengthInMonths)
                        listAgesInMonths.append(0)
                        listAgesInMonths.append(self.objSSParametersLocal.intGestationLengthInMonths)
                        listAgesInMonths.append((self.objSSParametersLocal.minMatingAge*12))
                        listAgesInMonths.append((self.objSSParametersLocal.maxMatingAge*12))
                        #listAgesInMonths.append(self.objSSParametersLocal.maxAge*12)
                    else:
                        listAgesInMonths.append(0)
                        listAgesInMonths.append((self.objSSParametersLocal.minMatingAge*12))
                        listAgesInMonths.append((self.objSSParametersLocal.maxMatingAge*12))
                        listAgesInMonths.append(self.objSSParametersLocal.maxAge*12)

                    #METHOD -  intParturationSeasonIntervalInMonths
                    #Starting individuals ages are evenly spread across all life stages
                    #pop.setIndInfo([0,1,2], 'age')

#                     intNumInEachAge = self.objSSParametersLocal.popnSize / (self.objSSParametersLocal.maxAge)
#                     for intAgeInYears in range(0, self.objSSParametersLocal.maxAge):
#                         listAgesInYears.append(intAgeInYears)
#                         listAgesInMonths.append(intAgeInYears*self.objSSParametersLocal.intParturationSeasonIntervalInMonths)
  
                    #DEBUG_ON
                    #listAgesInMonths=[-4,4,16,28] #orks with gestation months = 2
                    #as does [0, 2, 14, 26] from age classes of 1,2,3 (ie 3 = maxage)
                    #listAgesInMonths=[6,18,30]
                    #listAgesInMonths=[0-8-2, 0, 12-8+2, 24-8+2, 36-8+2]
                    #listAgesInMonths=[0, 2, 14, 26]
                    #listAgesInMonths=[-7, 5, 17, 29]
                    #listAgesInMonths=[0, 10, 22, 34, 58, 70]
                    #DEBUG_OFF

                elif self.objSSParametersLocal.intPopulationInitialAges == globalsSS.InitialAgeDistribution.static_SameAgeAndEvenSpreadAcrossLifeStages_1CohortPer12Months:

                    listAgesInMonths = []
                    for intAgeInMonths in range(0, self.objSSParametersLocal.maxAge*12, 12):
                        listAgesInMonths.append(intAgeInMonths)
                    pass
                
                    listAgesInYears = [x / 12 for x in listAgesInMonths]

                    self.obj_Log_Debug_Display.debug('listAgesInMonths: ' + str(listAgesInMonths))
                    self.obj_Log_Debug_Display.debug('listAgesInYears: ' + str(listAgesInYears))

                    '''
                    ---------------------------
                    IMPORTANT - Adjust ages of population to align with mating month in simulation run
                    ---------------------------
                    '''
                    
                    '''
                    First check if overlapping gens are being modeled
                    '''
                    if self.objSSParametersLocal.bool_Overlapping_Gens_Simulation == False:
                        intAdvanceLifeStageAge1 = (-self.objSSParametersLocal.intMatingCalenderMonth)+1 #+1 because the embryos are currently 0 age
                        pass
                    else:
                    
                        #Push the Embryo life stage forward to ensure that birth occurs at first parturition month irrelevant of how long the gestation length is
                        #intAdvanceLifeStageAge1 = (self.objSSParametersLocal.intGestationLengthInMonths - (self.objSSParametersLocal.intParturitionCalenderMonth))
                        if self.objSSParametersLocal.intGestationLengthInMonths > 12:
                            intAdvanceLifeStageAge1 = (12+(12-self.objSSParametersLocal.intMatingCalenderMonth))+1  #+1 because the embryos are currently 0 age
                        else:                    
                            intAdvanceLifeStageAge1 = (12-(self.objSSParametersLocal.intMatingCalenderMonth))+1  #+1 because the embryos are currently 0 age
                        pass
                    pass

                    self.obj_Log_Debug_Display.debug('intAdvanceLifeStageAge1: ' + str(intAdvanceLifeStageAge1))
                    
                    listAgesInMonths = [x + intAdvanceLifeStageAge1 for x in listAgesInMonths]
                    listAgesInYears = [x / 12 for x in listAgesInMonths]

                    self.obj_Log_Debug_Display.debug('listAgesInMonths: ' + str(listAgesInMonths))
                    self.obj_Log_Debug_Display.debug('listAgesInYears: ' + str(listAgesInYears))

                    ''' Update ages in the pop '''
                    pop_In.setIndInfo(listAgesInMonths, 'age_in_months')
                    pop_In.setIndInfo(listAgesInYears, 'age')
                    
                    #DEBUG_ON
                    #raw_input('\n Press return to continue... \n')
                    #DEBUG_OFF
                    
                elif self.objSSParametersLocal.intPopulationInitialAges == globalsSS.InitialAgeDistribution.static_Embryo_And_Mature_Only_1CohortPer12Months:

                    '''
                    ---------------------------
                    IMPORTANT - Special Age Initialization for DISCRETE GENS ONLY
                    ---------------------------
                    '''
                    intAdvanceLifeStageAge1 = (-self.objSSParametersLocal.intMatingCalenderMonth)+1 #+1 because the embryos are currently 0 age
                    self.obj_Log_Debug_Display.debug('intAdvanceLifeStageAge1: ' + str(intAdvanceLifeStageAge1))
                    
                    int_AgeInMonths__Embryo_Cohort = 0
                    int_AgeInMonths__Neonate_Cohort = self.objSSParametersLocal.minMatingAge*12 + intAdvanceLifeStageAge1
                    int_AgeInMonths__Mature_Cohort = 0
                    int_AgeInMonths__Senescent_Cohort = self.objSSParametersLocal.maxAge*12 + intAdvanceLifeStageAge1
                    int_AgeInMonths__Died_Cohort = 0
                    listAgesInMonths = [int_AgeInMonths__Neonate_Cohort
                                        ,int_AgeInMonths__Senescent_Cohort]

                    listAgesInYears = [x // 12 for x in listAgesInMonths]

                    self.obj_Log_Debug_Display.debug('listAgesInMonths: ' + str(listAgesInMonths))
                    self.obj_Log_Debug_Display.debug('listAgesInYears: ' + str(listAgesInYears))


                    pop_In.setIndInfo(listAgesInMonths, 'age_in_months')
                    pop_In.setIndInfo(listAgesInYears, 'age')
                pass
            

                '''
                -------------------------
                Split the ages into each virtual subpopulation
                -------------------------
                '''

                pop_In = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(pop_In, boolUpdate=True)

                #DEBUG_ON
                #intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                #for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                #    simupop.dump(pop_In, subPops=[(0,intVirtualSubPop)])
                #pass
                #self.obj_Log_Debug_Display.debug('\n method_Initialise_Ages - POP DUMP - Gen ')
                #raw_input('\n Press return to continue... \n')
                #DEBUG_OFF

                with SSAnalysisHandler() as SSAnalysisOperation:
                    odictCountIndividualsWithInfoField =  SSAnalysisOperation.method_Count_Individuals_By_InfoField(pop_In, 'age_in_months')
                    #print('Numbers per age in months: ' + str(odictCountIndividualsWithInfoField))

                with SSOutputHandler() as SSOutputOperation:
                    listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    #SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, '')
                    #
                    stringMessage = ' method_InitialisePopulations - listAgesInMonths:' + str(listAgesInMonths)  +'\n'
                    boolNewline=True
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                    #
                    stringMessage = ' method_InitialisePopulations - Numbers per age in months: ' + str(odictCountIndividualsWithInfoField) +'\n'
                    boolNewline=True
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                    #
                    #SSOutputOperation.methodOutput_SimGeneralMessageFooter(listOutputDestinations, '')

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    #pass
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                #raw_input('\n method_InitialisePopulations - press enter to continue')


                #TESTING_ON
                #intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                #self.methodOutput_outputPopulationDump(pop_In)
                ##############  REPORT: Info field Statistics
                # age_in_months
                #simupop.stat(pop_In, maxOfInfo=['age_in_months'], subPops=simupop.simupop.ALL_AVAIL, vars=['maxOfInfo'])
                #simupop.stat(pop_In, maxOfInfo=['age_in_months'], subPops=[0, (0,1), (0,2)], vars=['maxOfInfo', 'maxOfInfo_sp'])
                #simupop.stat(pop_In, maxOfInfo=['age_in_months'], subPops=simupop.simupop.ALL_AVAIL, vars=['maxOfInfo_sp'])
                #simupop.PyEval(pop_In, r"'MaxAge: %.2f \n' %(maxOfInfo['age_in_months'])")
                #simupop.PyEval(r"'MaxAge: %.2f \n' %(maxOfInfo['age_in_months'])")
                #TESTING_OFF

#                 #DEBUG_ON            
#                 # Output the summary of  age class totals(virtualSubPops) at each generation
#                 self.methodOutput_outputPopulationDump(pop_In)
#                 self.methodOutput_outputPopulationAgeClassTotals(pop_In, [False, True])
#                 #!!!!!!!!!!!!!!!Have to split again after methodOutput_outputPopulationAgeClassTotals or else VSPs are wrong and aging doesnt occur
#                 # Split the ages into each virtual subpopulation
#                 self.method_SplitLifeStagesIntoVSPs_By_AgeInYears()
#                 #self.method_SplitLifeStagesIntoVSPs_ForBurnIn_By_AgeInMonths(boolDisplayOnly=False)
#                 pop_In = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(pop_In, boolUpdate=True)
#                 #Pause for testing
#                 #input('\n After AGE_SPLIT during INITILIZATION - Press return to close this window... \n')
#                 #DEBUG_OFF
                
                pop_Out = pop_In
                    
                return pop_Out
      
                
            def method_Population_Creation_From_File(self):
                
                pop = self.method_ImportPopulationFromFile()
                
                pop.setIndInfo([10, 22, 34, 46], 'age_in_months')
                #self.pop.setIndInfo(self.objSSParametersLocal.intParturationSeasonIntervalInMonths, 'parturation_season_interval_in_months')
                
                # Split the ages into each virtual subpopulation
                #self.method_SplitLifeStagesIntoVSPs_By_AgeInYears()
                #self.method_SplitLifeStagesIntoVSPs_ForBurnIn_By_AgeInMonths(boolDisplayOnly=False)
                self.pop = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(self.pop, boolUpdate=True)

                #TESTING_ON
                #intNumberVirtualSubPops = self.pop.numVirtualSubPop()
                #self.methodOutput_outputPopulationDump(self.pop)
                ##############  REPORT: Info field Statistics
                # age_in_months
                simupop.stat(pop, maxOfInfo=['age_in_months'], subPops=simupop.ALL_AVAIL, vars=['maxOfInfo'])
                #simupop.stat(self.pop, maxOfInfo=['age_in_months'], subPops=[0, (0,1), (0,2)], vars=['maxOfInfo', 'maxOfInfo_sp'])
                #simupop.stat(self.pop, maxOfInfo=['age_in_months'], subPops=simupop.simupop.ALL_AVAIL, vars=['maxOfInfo_sp'])
                #simupop.PyEval(self.pop, r"'MaxAge: %.2f \n' %(maxOfInfo['age_in_months'])")
                #simupop.PyEval(r"'MaxAge: %.2f \n' %(maxOfInfo['age_in_months'])")
                #TESTING_OFF

                #DEBUG_ON            
                # Output the summary of  age class totals(virtualSubPops) at each generation
#                     self.methodOutput_outputPopulationDump(self.pop)
#                     self.methodOutput_outputPopulationAgeClassTotals(self.pop, [False, True])
#                     #!!!!!!!!!!!!!!!Have to split again after methodOutput_outputPopulationAgeClassTotals or else VSPs are wrong and aging doesnt occur
#                     # Split the ages into each virtual subpopulation
#                     self.method_SplitLifeStagesIntoVSPs_By_AgeInYears()
#                     #self.method_SplitLifeStagesIntoVSPs_ForBurnIn_By_AgeInMonths(boolDisplayOnly=False)
#                     self.pop = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(self.pop, boolUpdate=True)
                #Pause for testing
                #input('\n After AGE_SPLIT during INITILIZATION - Press return to close this window... \n')
                #DEBUG_OFF

                return pop


            '''
            --------------------------------------------------------------------------------------------------------
            # Evolve Processing
            --------------------------------------------------------------------------------------------------------
            '''

            '''@profile'''
            def method_EvolvePedigreeWithMating(self, pop_In, intGen, \
                                                list_Simupop_Evolve_Function_InitOps, \
                                                list_Simupop_Evolve_Function_PreOps, \
                                                ):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass    
                     
                self.obj_Log_Default_Display.info('START - Evolve Pedigree With Mating')

                '''
                ---------------------------------
                Display Life Stage - BEFORE MATING
                ---------------------------------
                '''
                bool_Display_Age_In_Year_Numbers_BF = False
                if bool_Display_Age_In_Year_Numbers_BF:
                    self.obj_Log_Run_Display.info('--------------------------------------------------------------- BEFORE MATING --------------------------------------------------------')
                    #pop_In = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop_In, boolUpdate=False)
    
                    with SSAnalysisHandler() as obj_Analysis:
                        boolReportVSPIfEmpty = True
                        #odictVSPSizes = obj_Analysis.method_Get_VSP_Sizes(pop_In, boolReportVSPIfEmpty)
                        str_InfoField = 'age'
                        listExpectedKeyValues = [x for x in range(0, self.objSSParametersLocal.maxAge)]
                        odictVSPSizes = obj_Analysis.method_Get_VSP_Sizes_By_InfoField(pop_In, True, listExpectedKeyValues, str_InfoField)

                        str_Message_Header_1 = '| '
                        str_Message_Header_2 = '| '
                        str_Message_Values = '| '
                        for key, value in odictVSPSizes.items():
                            #if int(key) != globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Juvenile:
                            ''' Construct string of VSP Headings 1 '''
                            stringPadChar = ' '
                            intLargestSize = 11
                            strFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                            str_Key_Out = strFormat.format(str(int(key)))
                            str_Message_Header_1 += '' + str_Key_Out + ' | '
                            ''' Construct string of VSP Headings 2 '''
                            obj_VSP_Life_Stage_Names = globalsSS.VSP_Life_Stage_Names()
                            str_VSP_Name = obj_VSP_Life_Stage_Names.func_Get_VSP_Name_From_VSP_Number(key)
                            stringPadChar = ' '
                            intLargestSize = 11
                            strFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                            str_VSP_Name_Out = strFormat.format(str_VSP_Name)
                            str_Message_Header_2 += '' + str_VSP_Name_Out + ' | '
                            ''' Construct string of values '''
                            stringPadChar = ' '
                            intLargestSize = 11
                            strFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                            #strFormat = '{:<'+ str(intLargestSize) + '}'
                            str_Cohort_Size = str(int(value))
                            str_Cohort_Size_Out = strFormat.format(str_Cohort_Size)
                            str_Message_Values += '' + str_Cohort_Size_Out + ' | '
                            #str_Message_Values += '' + str(key) + ', ' + str_Cohort_Size_Out + ' | '
                            pass
                        pass
                        self.obj_Log_Run_Display.info('Size of age cohorts; ' + str_Message_Header_1)
                        #self.obj_Log_Run_Display.info('Size of age cohorts; ' + str_Message_Header_2)
                        self.obj_Log_Run_Display.info('Size of age cohorts; ' + str_Message_Values)
                        #self.obj_Log_Run_Display.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
                        #DEBUG_ON
                        #with globalsSS.Pause_Console() as obj_Pause:
                        #    obj_Pause.method_Pause_Console()  
                        #DEBUG_OFF                  
                    pass
                pass
                bool_Display_Life_Stage_Numbers_BF = True
                if bool_Display_Life_Stage_Numbers_BF:
                    self.obj_Log_Run_Display.info('--------------------------------------------------------------- BEFORE MATING --------------------------------------------------------')
                    #pop_In = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop_In, boolUpdate=False)
    
                    with SSAnalysisHandler() as obj_Analysis:
                        boolReportVSPIfEmpty = True
                        #odictVSPSizes = obj_Analysis.method_Get_VSP_Sizes(pop_In, boolReportVSPIfEmpty)
                        str_InfoField = 'life_stage'
                        listExpectedKeyValues = [x for x in range(0, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_NumberofVSPs)]
                        odictVSPSizes = obj_Analysis.method_Get_VSP_Sizes_By_InfoField(pop_In, True, listExpectedKeyValues, str_InfoField)

                        str_Message_Header_1 = '| '
                        str_Message_Header_2 = '| '
                        str_Message_Values = '| '
                        for key, value in odictVSPSizes.items():
                            #if int(key) != globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Juvenile:
                            ''' Construct string of VSP Headings 1 '''
                            stringPadChar = ' '
                            intLargestSize = 11
                            strFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                            str_Key_Out = strFormat.format(str(int(key)))
                            str_Message_Header_1 += '' + str_Key_Out + ' | '
                            ''' Construct string of VSP Headings 2 '''
                            obj_VSP_Life_Stage_Names = globalsSS.VSP_Life_Stage_Names()
                            str_VSP_Name = obj_VSP_Life_Stage_Names.func_Get_VSP_Name_From_VSP_Number(key)
                            stringPadChar = ' '
                            intLargestSize = 11
                            strFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                            str_VSP_Name_Out = strFormat.format(str_VSP_Name)
                            str_Message_Header_2 += '' + str_VSP_Name_Out + ' | '
                            ''' Construct string of values '''
                            stringPadChar = ' '
                            intLargestSize = 11
                            strFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                            #strFormat = '{:<'+ str(intLargestSize) + '}'
                            str_Cohort_Size = str(int(value))
                            str_Cohort_Size_Out = strFormat.format(str_Cohort_Size)
                            str_Message_Values += '' + str_Cohort_Size_Out + ' | '
                            #str_Message_Values += '' + str(key) + ', ' + str_Cohort_Size_Out + ' | '
                            pass
                        pass
                        self.obj_Log_Run_Display.info('Size of Life Stages; ' + str_Message_Header_1)
                        self.obj_Log_Run_Display.info('Size of Life Stages; ' + str_Message_Header_2)
                        self.obj_Log_Run_Display.info('Size of Life Stages; ' + str_Message_Values)
                        #self.obj_Log_Run_Display.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
                        #DEBUG_ON
                        #with globalsSS.Pause_Console() as obj_Pause:
                        #    obj_Pause.method_Pause_Console()  
                        #DEBUG_OFF                  
                    pass
                pass
                '''
                --------------------------------
                Specify mating scheme to be used in simulation
                --------------------------------
                '''
                self.objSSParametersLocal.objMatingScheme = self.SpecifyMatingScheme()
                
                if self.objSSParametersLocal.int_MatingCount_Replicate_Total == 0: 
                    list_Simupop_Evolve_Function_InitOps.append(simupop.IdTagger())
                pass

                if self.objSSParametersLocal.bool_Allow_Mutation:
                    #list_Simupop_Evolve_Function_InitOps.append(simupop.StepwiseMutator(rates=self.objSSParametersLocal.float_Mutation_Rate, loci=simupop.ALL_AVAIL))
                    list_Simupop_Evolve_Function_PreOps.append(simupop.StepwiseMutator(rates=self.objSSParametersLocal.float_Mutation_Rate, loci=simupop.ALL_AVAIL))
                pass
            
                list_Simupop_Evolve_Function_PreOps.append(simupop.InfoExec('age += 1'))
                if self.objSSParametersLocal.int_MatingCount_Replicate_Total == 0:
                    if self.objSSParametersLocal.boolReportDemographicNe:
                        #list_Simupop_Evolve_Function_PreOps.append(simupop.Stat(effectiveSize=[0], vars=['Ne_demo_base']))
                        list_Simupop_Evolve_Function_PreOps.append(simupop.Stat(effectiveSize=[0], subPops=[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult)], vars=['Ne_demo_base_sp']))                    
                    pass
                pass
                
                '''
                --------------------------------
                Run EVOLVE
                --------------------------------
                '''
                try:
                    pop_In.evolve(
                        initOps = list_Simupop_Evolve_Function_InitOps,
     
                        preOps = list_Simupop_Evolve_Function_PreOps,
     
                        matingScheme = self.objSSParametersLocal.objMatingScheme,
     
                        postOps = [
                            # count the individuals in each virtual subpopulation
                            #simupop.Stat(popSize=True, subPops=[(0,0), (0,1), (0,2), (0,3), (0,4)]),
                            #simupop.Stat(popSize=True, subPops=[(0,0), (0,1), (0,2), (0,3), (0,4),(0,5), (0,6), (0,7), (0,8)]),
                            # print virtual subpopulation sizes (there is no individual with age > maxAge after mating)
                            #simupop.PyEval(r"'Size of age groups: %s\n' % (','.join(['%d' % x for x in subPopSize]))"),
                            #simupop.Stat(alleleFreq=[0], genoFreq=[0]),
                            #simupop.PyEval(r"'%.3f\t%.3f (%.3f)\t%.3f (%.3f)\t%.3f (%.3f)\n' % (alleleFreq[0][0], "\
                            #"genoFreq[0][(0,0)], alleleFreq[0][0]*alleleFreq[0][0], "\
                            #"genoFreq[0][(0,1)], 2*alleleFreq[0][0]*(1-alleleFreq[0][0]), "\
                            #"genoFreq[0][(1,1)], (1-alleleFreq[0][0])*(1-alleleFreq[0][0]) )"),
                        ],
                        gen = 1
                    )
                except RuntimeError, e:
#                     if e.message[:26] == 'RandomParentsChooser fails':
#                         return 'pyparted - no root access'
                    raise
                pass
            
                '''
                ---------------------------------
                Pre-Mating Fertilisation Stats _ MUST OCCUR JUST AFTER MATING AND BEFORE SPLITTING THE POP...
                to ensure Embryos and their parents in the 
                Reproductively Available Adults are still in the correct VSPs
                ---------------------------------
                '''
                self.method_Pre_Fertilization_Stats_Gathering(pop_In)

                '''
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                LIFE STAGE change from immature to mature
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                '''
                #
                pop_In = self.method_SplitLifeStagesIntoVSPs_By_Age_In_Months_Updating_Pre_Adult_Life_Stages(pop_In)
                pop_In = self.method_SplitLifeStagesIntoVSPs_By_Age_In_Months_Updating_Life_Stage_Juvenile_To_Adult(pop_In)
                                
                '''
                -------------------------
                Perform GESTATION Life-stage update
                If post-mating parent selection required
                -------------------------
                '''
                if not \
                  (self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Random_Mating_WITH_Replacement or \
                   self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Random_Mating_WITHOUT_Replacement):                         
            
                    '''
                    ---------------------------------
                    Post-Mating Operations
                    Female: Update LIFE_STAGE to GESTATING
                    ---------------------------------
                    '''
                    ''' Effective Females: Update LIFE_STAGE to GESTATING'''
                    pop_In = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop_In, boolUpdate=False)
                    pop_In = self.method_Effective_Parent_Post_Mating_Operations(pop_In)
                pass

                

                '''
                ---------------------------------
                Count matings
                ---------------------------------
                '''
                self.objSSParametersLocal.int_MatingCount_LifeSpan += 1
                if self.objSSParametersLocal.int_MatingCount_LifeSpan > self.objSSParametersLocal.maxAge:
                    self.objSSParametersLocal.int_MatingCount_LifeSpan = 0
                pass
            
                self.objSSParametersLocal.int_MatingCount_Replicate_Total += 1
                if self.objSSParametersLocal.boolBurnIn:
                    self.objSSParametersLocal.int_MatingCount_Replicate_BurnIn += 1
                else:
                    self.objSSParametersLocal.int_MatingCount_Replicate_PostBurnIn += 1
                
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Replicate_Total: ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_Total))
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Replicate_BurnIn: ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_BurnIn))
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Replicate_PostBurnIn ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_PostBurnIn))

                self.objSSParametersLocal.int_MatingCount_Batch_Total += 1
                if self.objSSParametersLocal.boolBurnIn:
                    self.objSSParametersLocal.int_MatingCount_Batch_BurnIn += 1
                else:
                    self.objSSParametersLocal.int_MatingCount_Batch_PostBurnIn += 1
                                    
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Batch_Total: ' + str(self.objSSParametersLocal.int_MatingCount_Batch_Total))
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Batch_BurnIn: ' + str(self.objSSParametersLocal.int_MatingCount_Batch_BurnIn))
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Batch_PostBurnIn ' + str(self.objSSParametersLocal.int_MatingCount_Batch_PostBurnIn))

                self.objSSParametersLocal.int_MatingCount_Sim_Total += 1
                if self.objSSParametersLocal.boolBurnIn:
                    self.objSSParametersLocal.int_MatingCount_Sim_BurnIn += 1
                else:
                    self.objSSParametersLocal.int_MatingCount_Sim_PostBurnIn += 1
                   
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Sim_Total: ' + str(self.objSSParametersLocal.int_MatingCount_Sim_Total))
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Sim_BurnIn: ' + str(self.objSSParametersLocal.int_MatingCount_Sim_BurnIn))
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Sim_PostBurnIn ' + str(self.objSSParametersLocal.int_MatingCount_Sim_PostBurnIn))

                '''
                ---------------------------------
                Display Life Stage - AFTER MATING
                ---------------------------------
                '''
                bool_Display_Life_Stage_Numbers_AF = True
                if bool_Display_Life_Stage_Numbers_AF:
                    self.obj_Log_Run_Display.info('---------------------------------------------------------------  AFTER MATING --------------------------------------------------------')
                    pop_In = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop_In, boolUpdate=False)
    
                    with SSAnalysisHandler() as obj_Analysis:
                        boolReportVSPIfEmpty = True
                        #odictVSPSizes = obj_Analysis.method_Get_VSP_Sizes(pop_In, boolReportVSPIfEmpty)
                        str_InfoField = 'life_stage'
                        listExpectedKeyValues = [x for x in range(0, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_NumberofVSPs)]
                        odictVSPSizes = obj_Analysis.method_Get_VSP_Sizes_By_InfoField(pop_In, True, listExpectedKeyValues, str_InfoField)
                        str_Message_Values = '| '
                        for key, value in odictVSPSizes.items():
#                            if int(key) != globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Juvenile:
                            ''' Construct string of values '''
                            stringPadChar = ' '
                            intLargestSize = 11
                            strFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                            str_Cohort_Size = str(int(value))
                            str_Cohort_Size_Out = strFormat.format(str_Cohort_Size)
                            str_Message_Values += '' + str_Cohort_Size_Out + ' | '
                            pass
                        pass
                        self.obj_Log_Run_Display.info('Size of Life Stages; ' + str_Message_Values)
                        self.obj_Log_Run_Display.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
                    pass
                pass

                bool_Display_Age_In_Years_Numbers_AF = False
                if bool_Display_Age_In_Years_Numbers_AF:
                    self.obj_Log_Run_Display.info('---------------------------------------------------------------  AFTER MATING --------------------------------------------------------')
                    #pop_In = self.method_SplitLifeStagesIntoVSPs_By_AgeInYears(pop_In)    
                    with SSAnalysisHandler() as obj_Analysis:
                        boolReportVSPIfEmpty = True
                        #odictVSPSizes = obj_Analysis.method_Get_VSP_Sizes(pop_In, boolReportVSPIfEmpty)
                        str_InfoField = 'age'
                        listExpectedKeyValues = [x for x in range(0, self.objSSParametersLocal.maxAge)]
                        odictVSPSizes = obj_Analysis.method_Get_VSP_Sizes_By_InfoField(pop_In, True, listExpectedKeyValues, str_InfoField)
                        str_Message_Values = '| '
                        for key, value in odictVSPSizes.items():
#                            if int(key) != globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Juvenile:
                            ''' Construct string of values '''
                            stringPadChar = ' '
                            intLargestSize = 11
                            strFormat = '{:' +  stringPadChar + '^' + str(intLargestSize) + '}'
                            str_Cohort_Size = str(int(value))
                            str_Cohort_Size_Out = strFormat.format(str_Cohort_Size)
                            str_Message_Values += '' + str_Cohort_Size_Out + ' | '
                            pass
                        pass
                        self.obj_Log_Run_Display.info('Size of Age cohorts; ' + str_Message_Values)
                        self.obj_Log_Run_Display.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
                    pass
                pass
            
            
                '''
                ---------------------------------
                Display some basic info
                ---------------------------------
                '''
                
                self.obj_Log_Run_Display.info('Sim Folder: ' + self.objSSParametersLocal.strRunSpecificUserDefinedFolder)
                self.obj_Log_Run_Display.info('RunID: '+ self.objSSParametersLocal.strUniqueRunID)
                self.obj_Log_Run_Display.info('Batch: ' + str(self.objSSParametersLocal.intCurrentBatch) +  ' of Batches: ' + str(self.objSSParametersLocal.intBatches))
                self.obj_Log_Run_Display.info('Replicate: ' + str(self.objSSParametersLocal.intCurrentReplicate) +  ' of Replicates: ' + str(self.objSSParametersLocal.intReplicates))
                self.obj_Log_Run_Display.info('Replicate Mating: ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_Total) +  ' of Replicate Matings: ' + str(self.objSSParametersLocal.int_Total_MatingsToSimulatePerReplicate))
                '''
                ---------------------------------
                Display Age Classes 
                ---------------------------------
                '''            
                '''
                ~~~~~~~~~~~~~~~~~~~~~~~~~
                >>> NOTE >>> This split must be the last when EVOLVE finishes
                ~~~~~~~~~~~~~~~~~~~~~~~~~
                '''
                bool_Display_Age_Class_Numbers = True
                if bool_Display_Age_Class_Numbers:                
                    pop_In = self.method_SplitLifeStagesInto_AgeClass_VSPs_By_AgeInMonths(pop_In, boolUpdate=True)
                    with SSAnalysisHandler() as obj_Analysis:
                        boolReportVSPIfEmpty = True
                        #odictVSPSizes = obj_Analysis.method_Get_VSP_Sizes(pop_In, boolReportVSPIfEmpty)
                        str_InfoField = 'age_class'
                        listExpectedKeyValues = [x for x in range(0, globalsSS.VSP_AgeClass.static_intVSP_AgeClass_NumberofVSPs)]
                        odictVSPSizes = obj_Analysis.method_Get_VSP_Sizes_By_InfoField(pop_In, True, listExpectedKeyValues, str_InfoField)
                        str_Message = '| '
                        for key, value in odictVSPSizes.items():
                            str_Message += '' + str(int(key)) + ', ' + str(int(value)) + ' | '
                        pass
                        self.obj_Log_Run_Display.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
                        self.obj_Log_Run_Display.info('Size of Age Classes; ' + str_Message)
                    pass
                pass
            
                self.obj_Log_Run_Display.info(globalsSS.Output_Display_Constants.static_str_Message_Separator)
                
                '''
                ~~~~~~~~~~~~~~~~~~~~
                Update File OUtput Path Modifier
                ~~~~~~~~~~~~~~~~~~~~
                '''
                str_Tot_Matings = str(self.objSSParametersLocal.int_Total_MatingsToSimulatePerReplicate)
                str_Current_Mating = str(self.objSSParametersLocal.int_MatingCount_Replicate_Total)
                str_Current_Mating_Out = '_M' + str_Current_Mating.zfill(len(str_Tot_Matings))
                self.str_Sim_Batch_Replicate_Mating_Identifier_Short = self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short + str_Current_Mating_Out

                str_Sim_Tot_Matings = str(self.objSSParametersLocal.int_Sim_Total_MatingsToSimulate)
                str_Sim_Current_Mating = str(self.objSSParametersLocal.int_MatingCount_Sim_Total)
                str_Sim_Current_Mating_Out = '_SM' + str_Sim_Current_Mating.zfill(len(str_Sim_Tot_Matings))
                self.str_Sim_Total_Mating_Batch_Replicate_Mating_Identifier_Short = str_Sim_Current_Mating_Out + '_' + self.str_Sim_Batch_Replicate_Mating_Identifier_Short
                    

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    bool_Debug_Display__Counts = False
                    if bool_Debug_Display__Counts: 
                        self.obj_Log_Debug_Display.debug('int_MatingCount_LifeSpan: ' + str(self.objSSParametersLocal.int_MatingCount_LifeSpan))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Replicate_Total: ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_Total))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Replicate_BurnIn: ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_BurnIn))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Replicate_PostBurnIn ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_PostBurnIn))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Batch_Total: ' + str(self.objSSParametersLocal.int_MatingCount_Batch_Total))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Batch_BurnIn: ' + str(self.objSSParametersLocal.int_MatingCount_Batch_BurnIn))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Batch_PostBurnIn ' + str(self.objSSParametersLocal.int_MatingCount_Batch_PostBurnIn))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Sim_Total: ' + str(self.objSSParametersLocal.int_MatingCount_Sim_Total))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Sim_BurnIn: ' + str(self.objSSParametersLocal.int_MatingCount_Sim_BurnIn))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Sim_PostBurnIn ' + str(self.objSSParametersLocal.int_MatingCount_Sim_PostBurnIn))
                    pass
                    bool_Debug_Display__Pop_Dump_By_VSP = False
                    if bool_Debug_Display__Pop_Dump_By_VSP:                
                        intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            simupop.dump(pop_In, subPops=[(0,intVirtualSubPop)])
                            with SSAnalysisHandler() as SSAnalysisOperation:
                                listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                                self.obj_Log_Debug_Display.debug('SEX COUNT - Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))   
                            pass
                        pass
                    pass
                    bool_Debug_Display__Pop_Sexes_Count = True
                    if bool_Debug_Display__Pop_Sexes_Count:                         
                        #simupop.dump(pop_In)
                        with SSAnalysisHandler() as SSAnalysisOperation:
                            listTotalCountofMaleFemale = [0,0]
                            intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                            for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                                listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                                self.obj_Log_Debug_Display.debug('VSP: ' + str(intVirtualSubPop) + '; SEX COUNT - Males:' + str(listCountofMaleFemale[0]) + ' Females:' + str(listCountofMaleFemale[1]))
                                listTotalCountofMaleFemale[0] += listCountofMaleFemale[0]
                                listTotalCountofMaleFemale[1] += listCountofMaleFemale[1]
                            pass 
                            self.obj_Log_Debug_Display.debug('FULL POP SEX COUNT - Total Males:' + str(listTotalCountofMaleFemale[0]) + ' Total Females:' + str(listTotalCountofMaleFemale[1]))   
                        pass
                    pass
                    if self.objSSParametersLocal.boolReportDemographicNe:
                        '''
                        ---------------------------------
                        Get Crow_And_Denniston_1988_DemoNe Stats
                        ---------------------------------
                        '''
                        #simupop.stat(pop_In, effectiveSize=[0], vars=['Ne_demo'])
                        simupop.stat(pop_In, effectiveSize=[0], subPops=[(0,2)], vars=['Ne_demo_sp'])
                        with SSAnalysisHandler() as obj_SSAnalysis:
                            float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating = obj_SSAnalysis.method_Get_SimupopStat_Demographic_Ne_Crow_And_Denniston_1988(pop_In)
                            self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating = float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating
                            
                            self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Sum_From_Matings_Over_Replicate += self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating
                            self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate = self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Sum_From_Matings_Over_Replicate / self.objSSParametersLocal.int_MatingCount_Replicate_Total
                            if self.objSSParametersLocal.boolBurnIn:
                                self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Sum_From_Matings_Over_BurnIn += self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating 
                                self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn = self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Sum_From_Matings_Over_BurnIn / self.objSSParametersLocal.int_MatingCount_Replicate_BurnIn 
                            elif (not self.objSSParametersLocal.boolInitialEvolve) and (not self.objSSParametersLocal.boolBurnIn):
                                self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Sum_From_Matings_Over_PostBurnIn +=self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating
                                self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn = self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Sum_From_Matings_Over_PostBurnIn / self.objSSParametersLocal.int_MatingCount_Replicate_PostBurnIn
                            pass
                        pass
                        
                        self.obj_Log_Debug_Display.debug('float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating: ' + str(self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating))
                        self.obj_Log_Debug_Display.debug('float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate: ' + str(self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate))
                        self.obj_Log_Debug_Display.debug('float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn: ' + str(self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn))
                        self.obj_Log_Debug_Display.debug('float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn: ' + str(self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn))
                    pass                    
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    pass
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
                
                pop_Out = pop_In
 
                self.obj_Log_Default_Display.info('END - Evolve Pedigree With Mating')
                                       
                return pop_Out
            
            '''@profile'''
            def method_EvolvePedigreeWithMating_DEBUG(self, pop_In, intGen, \
                                                list_Simupop_Evolve_Function_InitOps, \
                                                list_Simupop_Evolve_Function_PreOps, \
                                                ):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass    
                
                #DEBUG_ON
                bool_Debug_Pauses = False
                bool_Debug_Dumps = False
                #DEBUG_OFF
                     
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    #print('\n <<<<<<<<<<<<<<<<<<< method_EvolvePedigreeWithMating - START   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass
                
                with SSOutputHandler() as SSOutputOperation:
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    else:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Evolve Pedigree With Mating', boolIsHeader=True, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
                    
                ############################################ EVOLVE - START
                #DEBUG_ON
                #pop.turnOnDebug(code="")
                #DEBUG_OFF

                #DEBUG_ON
                if bool_Debug_Dumps:
                    self.obj_Log_Debug_Display.debug('\n A - BEFORE method_EvolvePedigreeWithMating - POP DUMP - Gen ' + str(intGen).zfill(3))
                    #simupop.dump(pop_In)
                    with SSAnalysisHandler() as SSAnalysisOperation:
                        listTotalCountofMaleFemale = [0,0]
                        intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                        self.obj_Log_Debug_Display.debug('Number of VSPs: ' + str(intNumberVirtualSubPops))
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            simupop.dump(pop_In, subPops=[(0,intVirtualSubPop)])
                        pass
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                            listTotalCountofMaleFemale[0] += listCountofMaleFemale[0]
                            listTotalCountofMaleFemale[1] += listCountofMaleFemale[1]
                        pass 
                        self.obj_Log_Debug_Display.debug('SEX COUNT - Total Males:' + str(listTotalCountofMaleFemale[0]) + ' Total Females:' + str(listTotalCountofMaleFemale[1]))   

                #self.methodOutput_outputPopulationDump(pop_In, ['method_TemporalPopulationProcessing - post ' + self.objSSParametersLocal.stringEventMessage])
                #self.methodOutput_outputPopulationAgeClassTotals(pop_In,[False, False])
                #self.methodOutput_outputPopulationLifeStageTotals(pop_In, [False, False])
                #Pause for testing
                if bool_Debug_Pauses:
                    self.obj_Log_Debug_Display.debug('\n B - BEFORE method_EvolvePedigreeWithMating - POP DUMP - Gen ' + str(intGen).zfill(3))
                    raw_input('\n Press return to continue... \n')
                #DEBUG_OFF

                #Dump VSPs
                if bool_Debug_Dumps:
                    intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                    for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                        simupop.dump(pop_In, subPops=[(0,intVirtualSubPop)])
                        with SSAnalysisHandler() as SSAnalysisOperation:
                            listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                            print('SEX COUNT - Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))   
                    pass
        
                if bool_Debug_Pauses:
                    raw_input('\n BEFORE method_EvolvePedigreeWithMating - VSP DUMP Gen ' + str(intGen).zfill(3) + ' - Press return to continue... \n')

                '''
                --------------------------------
                Specify mating scheme to be used in simulation
                --------------------------------
                '''
                self.objSSParametersLocal.objMatingScheme = self.SpecifyMatingScheme()
                
                #DEBUG_ON
                  #####################################################
                  #PROTOTYPE WF_Diploid_Sexual_Random_Mating
                  #####################################################                
#                 self.objSSParametersLocal.objMatingScheme = simupop.HeteroMating(
#                         # age <= maxAge, copy to the next generation (weight=-1)
#                         [simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3)], weight=-1),
#                         # random mating for individuals in mating ages
#                         simupop.RandomMating(ops=[
#                                          simupop.IdTagger(),                # give new born an ID
#                                          simupop.PedigreeTagger(),             # track parents of each individual
#                                          simupop.MendelianGenoTransmitter(),   # transmit genotype
#                                          ],
#                                      #sexMode=(simupop.PROB_OF_MALES, 0.5),
#                                      sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE),
#                                      #numOffspring=(sim.UNIFORM_DISTRIBUTION, 1, 3),
#                                      subPops=[(0, 2)])])

                ####################################################
                #method_MatingScheme_WF_Diploid_Sexual_Random_Mating
                ####################################################
#                 self.objSSParametersLocal.objMatingScheme = simupop.HeteroMating(
#                         [simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3, 4)], weight=-1),
#                          simupop.RandomMating(ops=[
#                                             simupop.IdTagger(),                # give new born an ID
#                                             simupop.PedigreeTagger(),             # track parents of each individual
#                                             simupop.MendelianGenoTransmitter(),   # transmit genotype
#                                             simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
#                                             simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
#                                            ],
#                                             sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE),
#                                             subPops=[(0, globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult)])])

#                 if intGen == 0:
#                     #####################################################
#                     #method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP
#                     #####################################################
#                     self.objSSParametersLocal.objMatingScheme = simupop.HeteroMating(
#                             [simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3)], weight=-1),
#                              simupop.HomoMating(
#                                 chooser=simupop.CombinedParentsChooser(simupop.RandomParentChooser(sexChoice=simupop.MALE_ONLY,replacement=True), simupop.RandomParentChooser(sexChoice=simupop.FEMALE_ONLY,replacement=True)),
#                                 generator=simupop.OffspringGenerator(
#                                     ops=[
#                                          simupop.IdTagger(),                # give new born an ID
#                                          simupop.PedigreeTagger(),             # track parents of each individual
#                                          simupop.MendelianGenoTransmitter(),   # transmit genotype
#                                          simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
#                                          simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
#                                          simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
#                                         ],
#                                     sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE),
#                                     #subPops=[(0, globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult)])])
#                                     numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters)),
#                                     subPops=[(0, globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult)])])
# 
#                 else:
#                     #####################################################
#                     #method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement
#                     #####################################################                    
#                     self.objSSParametersLocal.objMatingScheme = simupop.HeteroMating(
#                             [simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3)], weight=-1),
#                              simupop.HomoMating(
#                                 chooser=simupop.PyParentsChooser(self.method_ParentChooser_RandomParentPairs),
#                                 generator=simupop.OffspringGenerator(
#                                     ops=[
#                                          simupop.IdTagger(),                # give new born an ID
#                                          simupop.PedigreeTagger(),             # track parents of each individual
#                                          simupop.MendelianGenoTransmitter(),   # transmit genotype
#                                          simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
#                                          simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
#                                         ],
#                                     sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE),
#                                     #subPops=[(0, globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult)])])
#                                     numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters)))])
             
                #DEBUG_OFF
                
                #if self.objSSParametersLocal.boolInitialEvolve:
                if self.objSSParametersLocal.int_MatingCount_Replicate_Total == 0: 
                    list_Simupop_Evolve_Function_InitOps.append(simupop.IdTagger())
                pass
                #list_Simupop_Evolve_Function_InitOps = []
                if self.objSSParametersLocal.bool_Allow_Mutation:
                    #list_Simupop_Evolve_Function_InitOps.append(simupop.StepwiseMutator(rates=self.objSSParametersLocal.float_Mutation_Rate, loci=simupop.ALL_AVAIL))
                    list_Simupop_Evolve_Function_PreOps.append(simupop.StepwiseMutator(rates=self.objSSParametersLocal.float_Mutation_Rate, loci=simupop.ALL_AVAIL))
                pass
            
                #list_Simupop_Evolve_Function_PreOps = []
                list_Simupop_Evolve_Function_PreOps.append(simupop.InfoExec('age += 1'))
                if self.objSSParametersLocal.int_MatingCount_Replicate_Total == 0:
                    if self.objSSParametersLocal.boolReportDemographicNe:
                        #list_Simupop_Evolve_Function_PreOps.append(simupop.Stat(effectiveSize=[0], vars=['Ne_demo_base']))
                        list_Simupop_Evolve_Function_PreOps.append(simupop.Stat(effectiveSize=[0], subPops=[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult)], vars=['Ne_demo_base_sp']))                    
    
                    pass
                pass
                
                '''
                --------------------------------
                Run EVOLVE
                --------------------------------
                '''
            
                pop_In.evolve(
                    initOps = list_Simupop_Evolve_Function_InitOps,
 
                    preOps = list_Simupop_Evolve_Function_PreOps,
 
                    matingScheme = self.objSSParametersLocal.objMatingScheme,
 
                    postOps = [
                        # count the individuals in each virtual subpopulation
                        #simupop.Stat(popSize=True, subPops=[(0,0), (0,1), (0,2), (0,3), (0,4)]),
                        simupop.Stat(popSize=True, subPops=[(0,0), (0,1), (0,2), (0,3), (0,4),(0,5), (0,6), (0,7), (0,8)]),
                        # print virtual subpopulation sizes (there is no individual with age > maxAge after mating)
                        simupop.PyEval(r"'Size of age groups: %s\n' % (','.join(['%d' % x for x in subPopSize]))"),
                        #simupop.Stat(alleleFreq=[0], genoFreq=[0]),
                        #simupop.PyEval(r"'%.3f\t%.3f (%.3f)\t%.3f (%.3f)\t%.3f (%.3f)\n' % (alleleFreq[0][0], "\
                        #"genoFreq[0][(0,0)], alleleFreq[0][0]*alleleFreq[0][0], "\
                        #"genoFreq[0][(0,1)], 2*alleleFreq[0][0]*(1-alleleFreq[0][0]), "\
                        #"genoFreq[0][(1,1)], (1-alleleFreq[0][0])*(1-alleleFreq[0][0]) )"),
                    ],
                    gen = 1
                )
                '''
                ---------------------------------
                Count matings
                ---------------------------------
                '''
                self.objSSParametersLocal.int_MatingCount_LifeSpan += 1
                if self.objSSParametersLocal.int_MatingCount_LifeSpan > self.objSSParametersLocal.maxAge:
                    self.objSSParametersLocal.int_MatingCount_LifeSpan = 0
                pass
            
                self.objSSParametersLocal.int_MatingCount_Replicate_Total += 1
                if self.objSSParametersLocal.boolBurnIn:
                    self.objSSParametersLocal.int_MatingCount_Replicate_BurnIn += 1
                else:
                    self.objSSParametersLocal.int_MatingCount_Replicate_PostBurnIn += 1
                
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Replicate_Total: ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_Total))
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Replicate_BurnIn: ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_BurnIn))
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Replicate_PostBurnIn ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_PostBurnIn))

                self.objSSParametersLocal.int_MatingCount_Batch_Total += 1
                if self.objSSParametersLocal.boolBurnIn:
                    self.objSSParametersLocal.int_MatingCount_Batch_BurnIn += 1
                else:
                    self.objSSParametersLocal.int_MatingCount_Batch_PostBurnIn += 1
                                    
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Batch_Total: ' + str(self.objSSParametersLocal.int_MatingCount_Batch_Total))
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Batch_BurnIn: ' + str(self.objSSParametersLocal.int_MatingCount_Batch_BurnIn))
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Batch_PostBurnIn ' + str(self.objSSParametersLocal.int_MatingCount_Batch_PostBurnIn))

                self.objSSParametersLocal.int_MatingCount_Sim_Total += 1
                if self.objSSParametersLocal.boolBurnIn:
                    self.objSSParametersLocal.int_MatingCount_Sim_BurnIn += 1
                else:
                    self.objSSParametersLocal.int_MatingCount_Sim_PostBurnIn += 1
                   
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Sim_Total: ' + str(self.objSSParametersLocal.int_MatingCount_Sim_Total))
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Sim_BurnIn: ' + str(self.objSSParametersLocal.int_MatingCount_Sim_BurnIn))
#                 self.obj_Log_Debug_Display.debug('int_MatingCount_Sim_PostBurnIn ' + str(self.objSSParametersLocal.int_MatingCount_Sim_PostBurnIn))

 
                '''
                ---------------------------------
                Display some basic info
                ---------------------------------
                '''
#                 self.obj_Log_Default.info('Sim Folder: ' + self.objSSParametersLocal.strRunSpecificUserDefinedFolder)
#                 self.obj_Log_Default.info('RunID: '+ self.objSSParametersLocal.strUniqueRunID)
#                 self.obj_Log_Default.info('Batch: ' + str(self.objSSParametersLocal.intCurrentBatch) +  ' of Batches: ' + str(self.objSSParametersLocal.intBatches))
#                 self.obj_Log_Default.info('Replicate: ' + str(self.objSSParametersLocal.intCurrentReplicate) +  ' of Replicates: ' + str(self.objSSParametersLocal.intReplicates))
#                 self.obj_Log_Default.info('Replicate Mating: ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_Total) +  ' of Replicate Matings: ' + str(self.objSSParametersLocal.int_Total_MatingsToSimulatePerReplicate))
                self.obj_Log_Run_Display.info('Sim Folder: ' + self.objSSParametersLocal.strRunSpecificUserDefinedFolder)
                self.obj_Log_Run_Display.info('RunID: '+ self.objSSParametersLocal.strUniqueRunID)
                self.obj_Log_Run_Display.info('Batch: ' + str(self.objSSParametersLocal.intCurrentBatch) +  ' of Batches: ' + str(self.objSSParametersLocal.intBatches))
                self.obj_Log_Run_Display.info('Replicate: ' + str(self.objSSParametersLocal.intCurrentReplicate) +  ' of Replicates: ' + str(self.objSSParametersLocal.intReplicates))
                self.obj_Log_Run_Display.info('Replicate Mating: ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_Total) +  ' of Replicate Matings: ' + str(self.objSSParametersLocal.int_Total_MatingsToSimulatePerReplicate))
               
                '''
                ~~~~~~~~~~~~~~~~~~~~
                Update File OUtput Path Modifier
                ~~~~~~~~~~~~~~~~~~~~
                '''
                str_Tot_Matings = str(self.objSSParametersLocal.int_Total_MatingsToSimulatePerReplicate)
                str_Current_Mating = str(self.objSSParametersLocal.int_MatingCount_Replicate_Total)
                str_Current_Mating_Out = '_M' + str_Current_Mating.zfill(len(str_Tot_Matings))
                self.str_Sim_Batch_Replicate_Mating_Identifier_Short = self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short + str_Current_Mating_Out

                str_Sim_Tot_Matings = str(self.objSSParametersLocal.int_Sim_Total_MatingsToSimulate)
                str_Sim_Current_Mating = str(self.objSSParametersLocal.int_MatingCount_Sim_Total)
                str_Sim_Current_Mating_Out = '_SM' + str_Sim_Current_Mating.zfill(len(str_Sim_Tot_Matings))
                self.str_Sim_Total_Mating_Batch_Replicate_Mating_Identifier_Short = str_Sim_Current_Mating_Out + '_' + self.str_Sim_Batch_Replicate_Mating_Identifier_Short
                    

                
                #Dump VSPs
                if bool_Debug_Dumps:
                    intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                    for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                        simupop.dump(pop_In, subPops=[(0,intVirtualSubPop)])
                        with SSAnalysisHandler() as SSAnalysisOperation:
                            listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                            print('SEX COUNT - Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))   
                        
                    pass
                
                if bool_Debug_Pauses:
                    raw_input('\n AFTER method_EvolvePedigreeWithMating - VSP DUMP Gen ' + str(intGen).zfill(3) + ' - Press return to continue... \n')

                if bool_Debug_Dumps:                
                    simupop.dump(pop_In)
                    with SSAnalysisHandler() as SSAnalysisOperation:
                        listTotalCountofMaleFemale = [0,0]
                        intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                            listTotalCountofMaleFemale[0] += listCountofMaleFemale[0]
                            listTotalCountofMaleFemale[1] += listCountofMaleFemale[1]
                        pass 
                        print('SEX COUNT - Total Males:' + str(listTotalCountofMaleFemale[0]) + ' Total Females:' + str(listTotalCountofMaleFemale[1]))   
                
                if bool_Debug_Pauses:
                    raw_input('\n AFTER method_EvolvePedigreeWithMating - POP DUMP Gen ' + str(intGen).zfill(3) + ' - Press return to continue... \n')
                

                    
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        pass
                else:   
                    #print('\n <<<<<<<<<<<<<<<<<<< method_EvolveWithMating - END   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass

                with SSOutputHandler() as SSOutputOperation:
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    else:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Evolve Pedigree With Mating', boolIsHeader=False, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
 
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    bool_Debug_Display__Counts = False
                    if bool_Debug_Display__Counts: 
                        self.obj_Log_Debug_Display.debug('int_MatingCount_LifeSpan: ' + str(self.objSSParametersLocal.int_MatingCount_LifeSpan))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Replicate_Total: ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_Total))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Replicate_BurnIn: ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_BurnIn))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Replicate_PostBurnIn ' + str(self.objSSParametersLocal.int_MatingCount_Replicate_PostBurnIn))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Batch_Total: ' + str(self.objSSParametersLocal.int_MatingCount_Batch_Total))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Batch_BurnIn: ' + str(self.objSSParametersLocal.int_MatingCount_Batch_BurnIn))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Batch_PostBurnIn ' + str(self.objSSParametersLocal.int_MatingCount_Batch_PostBurnIn))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Sim_Total: ' + str(self.objSSParametersLocal.int_MatingCount_Sim_Total))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Sim_BurnIn: ' + str(self.objSSParametersLocal.int_MatingCount_Sim_BurnIn))
                        self.obj_Log_Debug_Display.debug('int_MatingCount_Sim_PostBurnIn ' + str(self.objSSParametersLocal.int_MatingCount_Sim_PostBurnIn))
                    pass
                    bool_Debug_Display__Pop_Dump_By_VSP = False
                    if bool_Debug_Display__Pop_Dump_By_VSP:                
                        intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            simupop.dump(pop_In, subPops=[(0,intVirtualSubPop)])
                            with SSAnalysisHandler() as SSAnalysisOperation:
                                listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                                print('SEX COUNT - Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))   
                            pass
                        pass
                    pass
                    bool_Debug_Display__Pop_Sexes_Count = False
                    if bool_Debug_Display__Pop_Sexes_Count:                         
                        #simupop.dump(pop_In)
                        with SSAnalysisHandler() as SSAnalysisOperation:
                            listTotalCountofMaleFemale = [0,0]
                            intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                            for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                                listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                                listTotalCountofMaleFemale[0] += listCountofMaleFemale[0]
                                listTotalCountofMaleFemale[1] += listCountofMaleFemale[1]
                            pass 
                            print('SEX COUNT - Total Males:' + str(listTotalCountofMaleFemale[0]) + ' Total Females:' + str(listTotalCountofMaleFemale[1]))   
                        pass
                    pass
                    if self.objSSParametersLocal.boolReportDemographicNe:
                        '''
                        ---------------------------------
                        Get Crow_And_Denniston_1988_DemoNe Stats
                        ---------------------------------
                        '''
                        #simupop.stat(pop_In, effectiveSize=[0], vars=['Ne_demo'])
                        simupop.stat(pop_In, effectiveSize=[0], subPops=[(0,2)], vars=['Ne_demo_sp'])
                        with SSAnalysisHandler() as obj_SSAnalysis:
                            float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating = obj_SSAnalysis.method_Get_SimupopStat_Demographic_Ne_Crow_And_Denniston_1988(pop_In)
                            self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating = float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating
                            
                            self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Sum_From_Matings_Over_Replicate += self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating
                            self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate = self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Sum_From_Matings_Over_Replicate / self.objSSParametersLocal.int_MatingCount_Replicate_Total
                            if self.objSSParametersLocal.boolBurnIn:
                                self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Sum_From_Matings_Over_BurnIn += self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating 
                                self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn = self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Sum_From_Matings_Over_BurnIn / self.objSSParametersLocal.int_MatingCount_Replicate_BurnIn 
                            elif (not self.objSSParametersLocal.boolInitialEvolve) and (not self.objSSParametersLocal.boolBurnIn):
                                self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Sum_From_Matings_Over_PostBurnIn +=self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating
                                self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn = self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Sum_From_Matings_Over_PostBurnIn / self.objSSParametersLocal.int_MatingCount_Replicate_PostBurnIn
                            pass
                        pass
                        
                        self.obj_Log_Debug_Display.debug('float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating: ' + str(self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating))
                        self.obj_Log_Debug_Display.debug('float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate: ' + str(self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate))
                        self.obj_Log_Debug_Display.debug('float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn: ' + str(self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn))
                        self.obj_Log_Debug_Display.debug('float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn: ' + str(self.objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn))
                    pass                    
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    #pass
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
                
                pop_Out = pop_In
                                        
                return pop_Out
            
            '''@profile'''
            def method_EvolvePedigreeWithMating_PROTOTYPE_3B(self, pop_In, intGen, list_Simupop_Evolve_Function_InitOps):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                
                #DEBUG_ON
                #bool_Debug_Pauses = True
                bool_Debug_Pauses = False
                bool_Debug_Dumps = False
                #DEBUG_OFF
                     
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    #print('\n <<<<<<<<<<<<<<<<<<< method_EvolvePedigreeWithMating - START   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass
                
                with SSOutputHandler() as SSOutputOperation:
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    else:
                        listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Evolve Pedigree With Mating', boolIsHeader=True, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
                    
                ############################################ EVOLVE - START
                #DEBUG_ON
                #pop.turnOnDebug(code="")
                #DEBUG_OFF

                #DEBUG_ON
                if bool_Debug_Dumps:
                    simupop.dump(pop_In)
                    with SSAnalysisHandler() as SSAnalysisOperation:
                        listTotalCountofMaleFemale = [0,0]
                        intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(self.pop, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                            listTotalCountofMaleFemale[0] += listCountofMaleFemale[0]
                            listTotalCountofMaleFemale[1] += listCountofMaleFemale[1]
                        pass 
                        print('SEX COUNT - Total Males:' + str(listTotalCountofMaleFemale[0]) + ' Total Females:' + str(listTotalCountofMaleFemale[1]))   

                #self.methodOutput_outputPopulationDump(self.pop, ['method_TemporalPopulationProcessing - post ' + self.objSSParametersLocal.stringEventMessage])
                #self.methodOutput_outputPopulationAgeClassTotals(self.pop,[False, False])
                #self.methodOutput_outputPopulationLifeStageTotals(self.pop, [False, False])
                #Pause for testing
                if bool_Debug_Pauses:
                    raw_input('\n BEFORE method_EvolvePedigreeWithMating_PROTOTYPE_3B - POP DUMP - Gen ' + str(intGen).zfill(3) + ' - Press return to continue... \n')
                #DEBUG_OFF

                #Dump VSPs
                if bool_Debug_Dumps:
                    intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                    for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                        simupop.dump(pop_In, subPops=[(0,intVirtualSubPop)])
                        with SSAnalysisHandler() as SSAnalysisOperation:
                            listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(self.pop, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                            print('SEX COUNT - Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))   
                    pass
        
                if bool_Debug_Pauses:
                    raw_input('\n BEFORE method_EvolvePedigreeWithMating_PROTOTYPE_3B - VSP DUMP Gen ' + str(intGen).zfill(3) + ' - Press return to continue... \n')
                
                pop_In.evolve(
                    initOps = list_Simupop_Evolve_Function_InitOps,
                    # increase age by 1 year
                    #preOps = simupop.InfoExec('age_in_months += 12'),
                    # PRE-OPS - Operations applied at the start of each life-cycle (gen).  Operators are applied to the PARENTAL generation.
                    preOps = [
                            #Count each mating
                            #simupop.PyOperator(func=self.method_CountMatings),
                            simupop.InfoExec('age += 1'),
                            simupop.InfoExec('age_in_months += 12')
                    ],                    
                    matingScheme = simupop.HeteroMating(
                        # age <= maxAge, copy to the next generation (weight=-1)
                        [simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3)], weight=-1),
                        # random mating for individuals in mating ages
                        simupop.RandomMating(ops=[
                                         simupop.IdTagger(),                # give new born an ID
                                         simupop.PedigreeTagger(),             # track parents of each individual
                                         simupop.MendelianGenoTransmitter(),   # transmit genotype
                                         ],
                                     #sexMode=(simupop.PROB_OF_MALES, 0.5),
                                     sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE),
                                     #numOffspring=(sim.UNIFORM_DISTRIBUTION, 1, 3),
                                     subPops=[(0, 2)])]),
                    postOps = [
                        # count the individuals in each virtual subpopulation
                        simupop.Stat(popSize=True, subPops=[(0,0), (0,1), (0,2), (0,3), (0,4)]),
                        # print virtual subpopulation sizes (there is no individual with age > maxAge after mating)
                        simupop.PyEval(r"'Size of age groups: %s\n' % (','.join(['%d' % x for x in subPopSize]))"),
                        simupop.Stat(alleleFreq=[0], genoFreq=[0]),
                        simupop.PyEval(r"'%.3f\t%.3f (%.3f)\t%.3f (%.3f)\t%.3f (%.3f)\n' % (alleleFreq[0][0], "\
                        "genoFreq[0][(0,0)], alleleFreq[0][0]*alleleFreq[0][0], "\
                        "genoFreq[0][(0,1)], 2*alleleFreq[0][0]*(1-alleleFreq[0][0]), "\
                        "genoFreq[0][(1,1)], (1-alleleFreq[0][0])*(1-alleleFreq[0][0]) )"),
                    ],
                    gen = 1
                )
                
                
                #Dump VSPs
                if bool_Debug_Dumps:
                    intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                    for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                        simupop.dump(pop_In, subPops=[(0,intVirtualSubPop)])
                        with SSAnalysisHandler() as SSAnalysisOperation:
                            listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(self.pop, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                            print('SEX COUNT - Total Males:' + str(listCountofMaleFemale[0]) + ' Total Females:' + str(listCountofMaleFemale[1]))   
                        
                    pass
                
                if bool_Debug_Pauses:
                    raw_input('\n AFTER method_EvolvePedigreeWithMating_PROTOTYPE_3B - VSP DUMP Gen ' + str(intGen).zfill(3) + ' - Press return to continue... \n')

                if bool_Debug_Dumps:                
                    simupop.dump(pop_In)
                    with SSAnalysisHandler() as SSAnalysisOperation:
                        listTotalCountofMaleFemale = [0,0]
                        intNumberVirtualSubPops = pop_In.numVirtualSubPop()
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            listCountofMaleFemale = SSAnalysisOperation.methodCount_SexesInAPop(self.pop, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                            listTotalCountofMaleFemale[0] += listCountofMaleFemale[0]
                            listTotalCountofMaleFemale[1] += listCountofMaleFemale[1]
                        pass 
                        print('SEX COUNT - Total Males:' + str(listTotalCountofMaleFemale[0]) + ' Total Females:' + str(listTotalCountofMaleFemale[1]))   
                
                if bool_Debug_Pauses:
                    raw_input('\n AFTER method_EvolvePedigreeWithMating_PROTOTYPE_3B - POP DUMP Gen ' + str(intGen).zfill(3) + ' - Press return to continue... \n')
                
                
                
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        pass
                else:   
                    #print('\n <<<<<<<<<<<<<<<<<<< method_EvolveWithMating - END   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass

                with SSOutputHandler() as SSOutputOperation:
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    else:
                        listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Evolve Pedigree With Mating', boolIsHeader=False, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
 
 
                    if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                        t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                        #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                        #    t2 = Timer2(True)
                        #    t2.Start()
                        #pass                    
                    pass       
                
                pop_Out = pop_In
                                        
                return pop_Out


            '''
            -------------------------------------------------------------------------------------------------------
            # Mating Scheme Processing
            --------------------------------------------------------------------------------------------------------
            '''
           
            '''@profile'''
            def method_SelectParents_Relative_To_Mating_Scheme(self, intEmbryoNumberToBeGenerated):

                with SSOutputHandler() as SSOutputOperation:
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    else:
                        listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Selecting Parents', boolIsHeader=True, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
                
#                 if globalsSS.MatingParentSelectionScheme.static_Mating_Parent_Selection_Scheme_Gestating in self.objSSParametersLocal.listMatingSchemeType:
#                     '''
#                     Select only female parents that are not currently gestating
#                     '''
#                     #Set life_stage to Gestating adult female
#                     simupopIndividual.life_stage = globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Gestating_adult_female #Same as simupopIndividual.setInfo(4, 'life_stage')
#                     simupopIndividual.gestation_month_count = 0                   
#                 
                if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_WF_Diploid_Sexual_Random_Mating:
                    pass
                # Use simuPop random mating method, bypassing the manual parent choosing process
                elif self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP:
                    pass
                
                
                '''
                If mating scheme is one that requires pre-selected parents...
                create sex-specific lists of putative parents
                '''
                if self.objSSParametersLocal.intMatingSchemeType >= 10:

                        ''' 
                        Allocating putative parents into sex-specific lists
                        '''
                        if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                            listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        else:
                            listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        #
                        SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Allocating putative parents into sex-specific lists', boolIsHeader=True, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
                        
                        #self.method_PutativeParentListFromVSP(0, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult)
                        
                        #pop_In = self.pop.clone()
                        pop_In = self.pop
                        with SSAnalysisHandler() as obj_Analysis:
                            self.objSSParametersLocal.listPutativeFemaleParents, self.objSSParametersLocal.listPutativeMaleParents = obj_Analysis.method_PutativeParentListFromVSP(pop_In, 0, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult)

                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        stringMessage = 'Putative Dames; ' + str(len(self.objSSParametersLocal.listPutativeFemaleParents)) + '; ' + str(self.objSSParametersLocal.listPutativeFemaleParents)
                        self.obj_Log_Debug_Display.debug(stringMessage)
                        stringMessage = '\n ' + stringMessage
                        boolNewline=True
                        SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                        #
                        stringMessage = 'Putative Sires; ' + str(len(self.objSSParametersLocal.listPutativeMaleParents)) + '; ' + str(self.objSSParametersLocal.listPutativeMaleParents)
                        self.obj_Log_Debug_Display.debug(stringMessage)
                        stringMessage = '\n ' + stringMessage
                        boolNewline=True
                        SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                        #
                        stringMessage = 'Putative Parents = ' + str(len(self.objSSParametersLocal.listPutativeMaleParents)+len(self.objSSParametersLocal.listPutativeFemaleParents))
                        self.obj_Log_Debug_Display.debug(stringMessage)
                        stringMessage = '\n ' + stringMessage
                        boolNewline=True
                        SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                        
                        if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                            listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        else:
                            listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        #
                        SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Allocating putative parents into sex-specific lists', boolIsHeader=False, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
    
                        '''
                        Then create parent-pairs depending on the mating scheme
                        '''
                    
                        if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                            listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        else:
                            listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        #
                        SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Selecting Parents for mating scheme: ' + str(self.objSSParametersLocal.intMatingSchemeType) + ' to produce embryos: ' + str(intEmbryoNumberToBeGenerated), boolIsHeader=True, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
                        
                        #Start selecting parent-pairs into parent-pair list
                        
                        if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Random_Mating_WITH_Replacement:
                            # Manually select parents from a pre-populated list of adults (putative parents) and supply them to the simuPop mating method
                            
                            boolReplacement = True
                            self.method_ParentSelector_RandomParentPairs(boolReplacement, intEmbryoNumberToBeGenerated)
                            pass
                        
                        elif self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Random_Mating_WITHOUT_Replacement:
                            
                            boolReplacement = False
                            self.method_ParentSelector_RandomParentPairs(boolReplacement, intEmbryoNumberToBeGenerated)
                            pass
                        
                        elif self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Monecious_Random_Mating_SP:
                            pass
                        
                        elif self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Polyandrous_Random_Mating:
                            
                            self.method_ParentSelector_Random_Polygamous_ParentPairs()
                            pass                

                        #DEBUG_ON
                        #print('\n Putative Dames; ' + str(len(self.objSSParametersLocal.listPutativeFemaleParents)) + '; ' + str(self.objSSParametersLocal.listPutativeFemaleParents))
                        #print('\n Putative Sires; ' + str(len(self.objSSParametersLocal.listPutativeMaleParents)) + '; ' + str(self.objSSParametersLocal.listPutativeMaleParents))
                        #DEBUG_OFF
                        
                        #Finshed selecting parent-pairs
                        
                        if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                            listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        else:
                            listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        #
                        SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Selecting Parents for mating scheme: ' + str(self.objSSParametersLocal.intMatingSchemeType)  + ' to produce embryos: ' + str(intEmbryoNumberToBeGenerated), boolIsHeader=False, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)

                with SSOutputHandler() as SSOutputOperation:
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    else:
                        listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Selecting Parents', boolIsHeader=False, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
            

            def method_Extract_VSPs_From_Pop(self, pop_In, list_tupVSPs): 
                
                ##DOES NOT WORK TO EXTRACT VSPs
                pop_VSP_Out = pop_In.extractSubPops(list_tupVSPs)
                
                self.obj_Log_Debug_Display.debug('VSPs extracted from pop: %s' % str(list_tupVSPs))
                
                return pop_VSP_Out
            
            
            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            Parent SELECTORS
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
               
            '''@profile'''           
            def method_ParentSelector_RandomParentPairs(self, boolReplacement, intEmbryoNumberToBeGenerated):
              
                #Re-initilse the parent pairs list every time its created
                self.objSSParametersLocal.olistPutativeParentsPairs = OrderedDict()

                
                intOrigNumMaleParents = len(self.objSSParametersLocal.listPutativeMaleParents)
                intOrigNumFemaleParents = len(self.objSSParametersLocal.listPutativeFemaleParents)

                if boolReplacement == False: 
                    if intOrigNumMaleParents != intOrigNumFemaleParents: 
                        with SSOutputHandler() as SSOutputOperation:
                    
                            listOutputDestinations = ['console',self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                            #
                            SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, 'method_ParentSelector_RandomParentPairs')
                            #
                            if intOrigNumMaleParents > intOrigNumFemaleParents:
                                stringMessage = '??? WARNING - UNEVEN SEX RATIO - MORE MALES (' + str(intOrigNumMaleParents) + ') THAN FEMALES (' + str(intOrigNumFemaleParents) + ') - WARNING ???\n'
                            else:
                                stringMessage = '??? WARNING - UNEVEN SEX RATIO - MORE FEMALES (' + str(intOrigNumFemaleParents) + ') THAN MALES (' + str(intOrigNumMaleParents) + ') - WARNING ???\n'
    
                            boolNewline=False
                            SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                            #
                            SSOutputOperation.methodOutput_SimGeneralMessageFooter(listOutputDestinations, 'method_ParentSelector_RandomParentPairs')
                    else:
                        simupopMaleIndividualChooser = self.method_ParentChooser_Random_Male(boolReplacement)
                        simupopFemaleIndividualChooser = self.method_ParentChooser_Random_Female(boolReplacement)
           
                        #The number of Females is used because they are limited in number by gestaion and reproductive restig
                        for intIndiv in range(0, intOrigNumFemaleParents):
        
                            floatMaleIndiv_ID = simupopMaleIndividualChooser.next()
                            floatFemaleIndiv_ID = simupopFemaleIndividualChooser.next()
                                
                            listParentPair = [floatMaleIndiv_ID, floatFemaleIndiv_ID]
                            
                            dictParentPair = {intIndiv:listParentPair}
                            self.objSSParametersLocal.olistPutativeParentsPairs.update(dictParentPair)
                else:

                    simupopMaleIndividualChooser = self.method_ParentChooser_Random_Male(boolReplacement)
                    simupopFemaleIndividualChooser = self.method_ParentChooser_Random_Female(boolReplacement)
                    
                    
                    for intIndiv in range(0, intEmbryoNumberToBeGenerated):
                
                        floatMaleIndiv_ID = simupopMaleIndividualChooser.next()
                        floatFemaleIndiv_ID = simupopFemaleIndividualChooser.next()

                        listParentPair = [floatMaleIndiv_ID, floatFemaleIndiv_ID]

                        dictParentPair = {intIndiv:listParentPair}
                        self.objSSParametersLocal.olistPutativeParentsPairs.update(dictParentPair)
                            
                pass

                self.obj_Log_Debug_Display.debug('method_ParentSelector_RandomParentPairs; olistPutativeParentsPairs: ' + str(self.objSSParametersLocal.olistPutativeParentsPairs))
                
                return True
 
            '''@profile'''           
            def method_ParentSelector_Random_Polygamous_ParentPairs(self):
                 
                #Re-initilse the parent pairs list every time its created
                self.objSSParametersLocal.olistPutativeParentsPairs = OrderedDict()

                intOrigNumMaleParents = len(self.objSSParametersLocal.listPutativeMaleParents)
                intOrigNumFemaleParents = len(self.objSSParametersLocal.listPutativeFemaleParents)

                if intOrigNumMaleParents != intOrigNumFemaleParents: 
                    with SSOutputHandler() as SSOutputOperation:
                
                        listOutputDestinations = ['console',self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        #
                        SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, 'method_ParentSelector_Random_Polygamous_ParentPairs')
                        #
                        if intOrigNumMaleParents > intOrigNumFemaleParents:
                            stringMessage = 'ERROR - UNEVEN SEX RATIO - MORE MALES (' + str(intOrigNumMaleParents) + ') THAN FEMALES (' + str(intOrigNumFemaleParents) + ') - ERROR\n'
                        else:
                            stringMessage = 'ERROR - UNEVEN SEX RATIO - MORE FEMALES (' + str(intOrigNumFemaleParents) + ') THAN MALES (' + str(intOrigNumMaleParents) + ') - ERROR\n'

                        boolNewline=False
                        SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                        #
                        SSOutputOperation.methodOutput_SimGeneralMessageFooter(listOutputDestinations, 'method_ParentSelector_Random_Polygamous_ParentPairs')
                else:
                    if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Polyandrous_Random_Mating:        
                        
                        '''
                        Dict of Polygamous mating
                        
                        Polyandry - Multiple male mate ith one female
                        intNum_Paternities_Per_Litter - The number of Paternities per litter = #Males per single Female
                        intFraction_Of_Paternities_Per_Mating_Event_Per_Num_Paternities - The number of MP and non-MP litters
                            produced in a mating event.
                        
                        Polygyny - One male mate ith multiple females
                        intNum_Female_Mates_Per_Male - The number of female mates 1 male can have 
                        intFraction_Of_Polygyny_Per_Mating_Event_Per_Num_Female_Mates_Per_Male - The proportion of Polygyny per mating event per number of female mates 1 male can have
                        e.g.
                            25% of the mating event have 3 Paternities per litter
                            50% of the mating event have 2 Paternities per litter
                            10% of the mating event have 1 Paternity   per litter
                             5% of the mating event have one male who mates with 10 females
                            15% of the mating event have one male who mates with  5 females
                            
                            ...all of which must add up to 1 (ie 100%)
                            Percentage must be a whole number
                                                      
                            dictPolygamousMatingRates = {'Polyandry_NumPaternities_and_FractionPerMatingEvent':{1:0.25,2:0.50,3:0.10}, 'Polygyny_NumFemaleMates_and_FractionPerMatingEvent':{10:0.05, 5:0.10}}
                        '''
                        dictPolygamousMatingRates = OrderedDict()    
                        #dictPolygamousMatingRates = ({'Polyandry_NumPaternities_and_FractionPerMatingEvent':{1:0.25,2:0.50,3:0.10}}),({'Polygyny_NumFemaleMates_and_FractionPerMatingEvent':{10:0.05, 5:0.10}})
                        dictPolygamousMatingRates['Polyandry_NumPaternities_and_FractionPerMatingEvent'] = {1:0.25,2:0.50,3:0.10}
                        dictPolygamousMatingRates['Polygyny_NumFemaleMates_and_FractionPerMatingEvent'] =  {10:0.05, 5:0.10}
                        
                        # Check that the Polygamy fractions add up to 1
                        intTotalOfFractions = 0
                        intPolygamySpecsCount = 0
                        for keyPolygamyType, valuePolygamyDict in dictPolygamousMatingRates.items():
                            
                            #That each fraction is a whole number
                            #Total up the fractions - should total to 1
                            for keyNum, valueNum in valuePolygamyDict.iteritems():
                                #Convert to percentage
                                intValuePercentage = valueNum * 100
                                if not intValuePercentage.is_integer():
                                    with SSOutputHandler() as SSOutputOperation:
                                        listOutputDestinations = ['console',self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                                        #
                                        SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, 'method_ParentSelector_Random_Polygamous_ParentPairs')
                                        #
                                        stringMessage = 'ERROR - Percentage is a NOT a whole number, FRACTION EQUALS: ' + str(valueNum) + ' - ERROR\n'
                                else:
                                    intTotalOfFractions += valueNum
                                pass
                            pass

                            #Save the Polygamy specifications for later use
                            if intPolygamySpecsCount == 0:
                                dictPolyandrySpecs = valuePolygamyDict
                            elif intPolygamySpecsCount == 1:
                                dictPolygynySpecs = valuePolygamyDict
                        
                            intPolygamySpecsCount += 1
                        pass
                    
                        #Check if fractions total up to 1 as expected - If not output error
                        if intTotalOfFractions <> 1:
                            with SSOutputHandler() as SSOutputOperation:
                                listOutputDestinations = ['console',self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                                #
                                SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, 'method_ParentSelector_Random_Polygamous_ParentPairs')
                                #
                                if intOrigNumMaleParents > intOrigNumFemaleParents:
                                    stringMessage = 'ERROR - POLYGAMY FACTION <> 1, EQUALS: ' + str(intTotalOfFractions) + ' - ERROR\n'
                           
                        '''
                        Process Polygamy
                        
                        First - Process Polyandry by selecting multiple males and pairing with one female
                        '''
                        # Setup parent choosers
                        simupopMaleIndividualChooser = self.method_ParentChooser_RandomMaleWITHOUTReplacement()
                        simupopFemaleIndividualChooser = self.method_ParentChooser_RandomFemaleWITHOUTReplacement()

                        '''
                        Process Polyandry
                        '''
                        
                        intTotalAdults = 0
                        for key_intNum_Paternities_Per_Litter, value_intFraction_Of_Paternities_Per_Mating_Event_Per_Num_Paternities in dictPolyandrySpecs.iteritems():
                            
                            #Determine how many Polyanderous Males are required as a fraction of the total Male adults
                            floatProportionOfAdults = (value_intFraction_Of_Paternities_Per_Mating_Event_Per_Num_Paternities * intOrigNumMaleParents)
                            #floatProportionOfAdults = (value_intFraction_Of_Paternities_Per_Mating_Event_Per_Num_Paternities * intOrigNumMaleParents)/ key_intNum_Paternities_Per_Litter
                            if not floatProportionOfAdults.is_integer():
                                    with SSOutputHandler() as SSOutputOperation:
                                        listOutputDestinations = ['console',self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                                        #
                                        SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, 'method_ParentSelector_Random_Polygamous_ParentPairs')
                                        #
                                        intProportionOfAdults = int(math__floor(floatProportionOfAdults))
                                        #
                                        stringMessage = 'WARNING - Proportion of adults is a NOT a whole number, Male Parent number: ' + str(intOrigNumMaleParents) + ', Calculated Adults required: ' + str(floatProportionOfAdults) + ', Polyandry specs: ' + str(key_intNum_Paternities_Per_Litter) + ' and Adults Fraction:' + str(value_intFraction_Of_Paternities_Per_Mating_Event_Per_Num_Paternities) + ', ROUNDING DOWN number of Adults to: ' + str(intProportionOfAdults) + ' - WARNING\n'
                                        
                                        
                            else:
                                intProportionOfAdults = int(floatProportionOfAdults)

                            '''
                            Process that number of adults by selectin MP parent-pairs
                            first by selecting a Female then pairing her with
                            as many males as specified by the MP number
                            '''
                            intAdultsIncudingMPs = 0
                            for intAdults in range(0, intProportionOfAdults):
                                
                                # First - Select the mother
                                floatFemaleIndiv_ID = simupopFemaleIndividualChooser.next()
                        
                                #Second - select each father and create the parent-pair
                                for intMP in range(0, key_intNum_Paternities_Per_Litter):
                                    
                                    if len(self.objSSParametersLocal.listPutativeMaleParents) > 0:    
                                        floatMaleIndiv_ID = simupopMaleIndividualChooser.next()
                                    else:
                                        with SSOutputHandler() as SSOutputOperation:
                                            listOutputDestinations = ['console',self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                                            #
                                            SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, 'method_ParentSelector_Random_Polygamous_ParentPairs')
                                            #
                                            stringMessage = 'ERROR - POLYANDRY Processing ran out of Males for Paternities: ' + str(key_intNum_Paternities_Per_Litter) + ' and Adults Fraction:' + str(value_intFraction_Of_Paternities_Per_Mating_Event_Per_Num_Paternities) + ' - ERROR\n'
                                            break
                                    pass
                                        
                                    listParentPair = [floatMaleIndiv_ID, floatFemaleIndiv_ID]
                                
                                    intTotalAdults += 1
                                    dictParentPair = {intTotalAdults:listParentPair}
                                    self.objSSParametersLocal.olistPutativeParentsPairs.update(dictParentPair)
                                    
                                    intAdultsIncudingMPs += 1
                                    if intAdultsIncudingMPs == intProportionOfAdults:
                                        break
                                    pass
                                pass
                            
                                if intAdultsIncudingMPs == intProportionOfAdults:
                                    break
                            pass

                        '''
                        Process Polygyny
                        '''
                        
                        for key_intNum_Female_Mates_Per_Male, value_intFraction_Of_Polygyny_Per_Mating_Event_Per_Num_Female_Mates_Per_Male in dictPolygynySpecs.iteritems():
                            
                            #Determine how many Polygynous Females are required as a fraction of the total Female adults
                            floatProportionOfAdults = (value_intFraction_Of_Polygyny_Per_Mating_Event_Per_Num_Female_Mates_Per_Male * intOrigNumFemaleParents) / key_intNum_Female_Mates_Per_Male
                            if not floatProportionOfAdults.is_integer():
                                    with SSOutputHandler() as SSOutputOperation:
                                        listOutputDestinations = ['console',self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                                        #
                                        SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, 'method_ParentSelector_Random_Polygamous_ParentPairs')
                                        #
                                        intProportionOfAdults = int(math__floor(floatProportionOfAdults))
                                        #
                                        stringMessage = 'WARNING - Proportion of adults is a NOT a whole number, Female Parent number: ' + str(intOrigNumFemaleParents) + ', Calculated Adults required: ' + str(floatProportionOfAdults) + ', Polyandry specs: ' + str(key_intNum_Female_Mates_Per_Male) + ' and Adults Fraction:' + str(value_intFraction_Of_Polygyny_Per_Mating_Event_Per_Num_Female_Mates_Per_Male) + ', ROUNDING DOWN number of Adults to: ' + str(intProportionOfAdults) + ' - WARNING\n'
                                        
                                        
                            else:
                                intProportionOfAdults = int(floatProportionOfAdults)

                            '''
                            Process that number of adults by selecting Polygynous parent-pairs
                            first by selecting a Male then pairing him with
                            as many Females as specified by the specified number of Females fer single Male mate
                            '''
                            intAdultsIncudingNum_Female_Mates_Per_Male = 0
                            for intAdults in range(0, intProportionOfAdults):
                                
                                # First - Select the father
                                floatMaleIndiv_ID = simupopMaleIndividualChooser.next()
                        
                                #Second - select each mother and create the parent-pair
                                for intNum_Female_Mates_Per_Male in range(0, key_intNum_Female_Mates_Per_Male):
                                    
                                    if len(self.objSSParametersLocal.listPutativeMaleParents) > 0:    
                                        floatFemaleIndiv_ID = simupopFemaleIndividualChooser.next()
                                    else:
                                        with SSOutputHandler() as SSOutputOperation:
                                            listOutputDestinations = ['console',self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                                            #
                                            SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, 'method_ParentSelector_Random_Polygamous_ParentPairs')
                                            #
                                            stringMessage = 'ERROR - POLYANDRY Processing ran out of Females for Paternities: ' + str(key_intNum_Female_Mates_Per_Male) + ' and Adults Fraction:' + str(value_intFraction_Of_Polygyny_Per_Mating_Event_Per_Num_Female_Mates_Per_Male) + ' - ERROR\n'
                                            break
                                    pass
                                        
                                    listParentPair = [floatMaleIndiv_ID, floatFemaleIndiv_ID]
                                
                                    intTotalAdults += 1
                                    dictParentPair = {intTotalAdults:listParentPair}
                                    self.objSSParametersLocal.olistPutativeParentsPairs.update(dictParentPair)
                                    
                                    intAdultsIncudingNum_Female_Mates_Per_Male += 1
                                    if intAdultsIncudingNum_Female_Mates_Per_Male == intProportionOfAdults:
                                        break
                                    pass
                                pass
                            
                                if intAdultsIncudingNum_Female_Mates_Per_Male == intProportionOfAdults:
                                    break
                            pass
                        
                                                  
                pass

            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            Parent CHOOSERS
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
            
            '''@profile'''
            def method_ParentChooser_RandomParentPairs(self, pop):

                
                with SSOutputHandler() as SSOutputOperation:
            
                    listOutputDestinations = ['console',self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, 'Choosing Parents')
                    #
                    stringMessage = 'Parent pairs avaliable:\n'
                    boolNewline=False
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                     
                    #DEBUG_ON
                    #print('Parent pairs avaliable:')
                    #print('         '),
                    #DEBUG_OFF
                     
                    for key, value in self.objSSParametersLocal.olistPutativeParentsPairs.items():
     
                            stringMessage = str(key) + ':(M-'+ str(int(value[0])) + ',' + 'F-'+ str(int(value[1])) + ') '
                            boolNewline=False
                            SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
     
                         
                        #print(str(key) + ':(M-'+ str(int(value[0])) + ',' + 'F-'+ str(int(value[1])) + ') '),
                    pass
     
                    intNumberOfParentPairs = len(self.objSSParametersLocal.olistPutativeParentsPairs)-1
                    intCount = 0
                    intRoundCount = 0
                     
                    #DEBUG_ON
                    #print('\nParent pairs yielded:'),
                    #DEBUG_OFF
                    stringMessage = '\nParent pairs yielded:'
                    boolNewline=False
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
    
                    while True:
                        #DEBUG_ON
                        #print('\nRound ' + str(intRoundCount) + ': '),
                        #DEBUG_OFF
                        stringMessage = '\nRound ' + str(intRoundCount) + ': '
                        boolNewline=False
                        SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                        
                        for key, value in self.objSSParametersLocal.olistPutativeParentsPairs.items():
                            
                            floatMaleIndiv_ID = value[0]
                            floatFemaleIndiv_ID = value[1]
                            
                            '''
                            Get the individuals as simupop objects
                            '''
                            simupopMaleIndividual = pop.indByID(floatMaleIndiv_ID)
                            simupopFemaleIndividual = pop.indByID(floatFemaleIndiv_ID)
                            
                            '''
                            Update the processing flags for each individual
                            ''' 
                            if globalsSS.MatingParentSelectionScheme.static_Mating_Parent_Selection_Scheme_Gestating in self.objSSParametersLocal.listMatingParentSelectionScheme:
                                '''
                                LIFE STAGE Update - Update female parents to indicate that they are now gestating
                                '''
                                #Set life_stage to Gestating adult female
                                simupopFemaleIndividual.life_stage = globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Gestating_adult_female #Same as simupopIndividual.setInfo(4, 'life_stage')
                                #simupopFemaleIndividual.gestation_month_count = 0                   
                                                  
                                #simupopFemaleIndividual.is_gestating = 1                   
                                
                                
                                simupopFemaleIndividual.gestation_resting_countdown = self.objSSParametersLocal.intGestationLengthInMonths - 1  + self.objSSParametersLocal.intReproductiveRestLengthInMonths
                  
                            pass
                
                            '''
                            Pair them up
                            '''
                            listSimupopParentPair = [simupopMaleIndividual, simupopFemaleIndividual]
                            
                            #DEBUG_ON
                            value = listSimupopParentPair
                            if value[0].sex() == simupop.MALE:
                                strInd1Sex = 'M'
                            else: 
                                strInd1Sex = 'F'
                            if value[1].sex() == simupop.MALE:
                                strInd2Sex = 'M'
                            else: 
                                strInd2Sex = 'F'
                             
                            stringMessage = str(key) + ':(' + strInd1Sex + '-'+ str(int(value[0].ind_id)) + ',' + strInd2Sex + '-'+ str(int(value[1].ind_id)) + ') '
                            boolNewline=False
                            SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
    
                            #print(str(key) + ':(' + strInd1Sex + '-'+ str(int(value[0].ind_id)) + ',' + strInd2Sex + '-'+ str(int(value[1].ind_id)) + ') '),
                            #DEBUG_OFF
        
                            yield listSimupopParentPair
                            
                            intCount += 1
                            if intCount > intNumberOfParentPairs:
                                intRoundCount += 1
                                intCount = 0

            
            def method_ParentChooser_Random_Female(self, boolReplacement):
                
                while True:

                    intRandomParentIndex = numpy__random.randint(0, len(self.objSSParametersLocal.listPutativeFemaleParents))   
                    floatIndiv_ID = self.objSSParametersLocal.listPutativeFemaleParents[intRandomParentIndex]

                    #self.obj_Log_Debug_Display.debug('Putative parent Female ID: %s' % int(floatIndiv_ID))

                    if boolReplacement == False:
                        del self.objSSParametersLocal.listPutativeFemaleParents[intRandomParentIndex]
                    
                    yield floatIndiv_ID
 
 
            def method_ParentChooser_Random_Male(self, boolReplacement):

                while True:
                    
                    intRandomParentIndex = numpy__random.randint(0, len(self.objSSParametersLocal.listPutativeMaleParents))   
                    floatIndiv_ID = self.objSSParametersLocal.listPutativeMaleParents[intRandomParentIndex]

                    #self.obj_Log_Debug_Display.debug('Putative parent Male ID  : %s' % int(floatIndiv_ID))

                    if boolReplacement == False:
                        del self.objSSParametersLocal.listPutativeMaleParents[intRandomParentIndex]

                    yield floatIndiv_ID

            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            Pre-mating Operations
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
            def method_Pre_Mating_Potential_Parent_Determination(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass
             
                ''' Must be applied straight after mating BEFORE population is split into lifestages or age classes'''
                with SSAnalysisHandler() as obj_SSAnalysisOp:
                    
                    intSubPop = globalsSS.SP_SubPops.static_intSP_SubPop_Primary
                    listPotentialFemaleParents, listPotentialMaleParents = obj_SSAnalysisOp.method_PutativeParentListFromVSP(pop_In, intSubPop)

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    #pass
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
            
                return listPotentialFemaleParents, listPotentialMaleParents
            
                    
            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            Post-mating Operations
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
            def method_Effective_Parent_Post_Mating_Operations(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()

                ''' 
                ~~~~~~~~~~~~~~~~~~~~~~~
                UPDATE LIFE STAGE: REPRODUCTIVELY AVAILABLE --> GESTATING
                For each mother get her as a simupop individual and update here lifestage to Gestating
                and update the gestation resting counter to the the combined total of months
                ~~~~~~~~~~~~~~~~~~~~~~~
                '''                
                listDameParents = self.method_Dame_Parent_Determination_Post_Mating(pop_In)
                pop_Out = self.method_Dame_Parent_Info_Update_Post_Mating(pop_In, listDameParents)

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass

                
                return pop_Out
            
            
            def method_Effective_Parent_Determination_Post_Mating_RETIRE(self, pop_In):


                with SSAnalysisHandler() as obj_SSAnalysisOp:
                    
                    intSubPop = globalsSS.SP_SubPops.static_intSP_SubPop_Primary
                    intVirtualSubPop = globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo
                    listEffectiveFemaleParents, listEffectiveMaleParents = obj_SSAnalysisOp.method_PutativeParentListFromVSP(pop_In, intSubPop)

                return listEffectiveFemaleParents, listEffectiveMaleParents
            
            def method_Dame_Parent_Determination_Post_Mating(self, pop_In):


                with SSAnalysisHandler() as obj_SSAnalysisOp:
                    listDameParents = obj_SSAnalysisOp.method_Effective_Female_List_From_Embryo_VSP(pop_In)

                return listDameParents


            def method_Dame_Parent_Info_Update_Post_Mating(self, pop_In, listDameParents):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass      
            
                ''' 
                ~~~~~~~~~~~~~~~~~~~~~~~
                UPDATE LIFE STAGE: REPRODUCTIVELY AVAILABLE --> GESTATING
                For each mother get her as a simupop individual and update here lifestage to Gestating
                and update the gestation resting counter to the the combined total of months
                ~~~~~~~~~~~~~~~~~~~~~~~
                '''
                ''' Get the UNIQUE Dame parent IDs only to imporve performance '''
                listDameParents.sort()
                setFound = set()
                setFound_Add = setFound.add
                listUniqueDameParents = [item for item in listDameParents if not (item in setFound or setFound_Add(item))]
                listUniqueDameParents.sort()

                for mother_ID in listUniqueDameParents:
                    try:
                        simupopFemaleIndividual = pop_In.indByID(mother_ID)
                
                        '''
                        LIFE STAGE Update - Update female parents to indicate that they are now gestating
                        '''
                        #Set life_stage to Gestating adult female
                        simupopFemaleIndividual.life_stage = globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Gestating_adult_female #Same as simupopIndividual.setInfo(4, 'life_stage')
                        simupopFemaleIndividual.gestation_resting_countdown = self.objSSParametersLocal.intGestationLengthInMonths - 1  + self.objSSParametersLocal.intReproductiveRestLengthInMonths
                    except:
                        ''' Individual was not found and probably has been removed by mortality '''
                        pass
                    pass
                pass

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    bool_Display_Dame_Parents = True
                    if bool_Display_Dame_Parents:
                        self.obj_Log_Debug_Display.debug('Pop Info_Field Update - LIFE_STAGE: Mature -> Gestating for ' + str(len(listDameParents)) + ' Dame Female Parents: ' + globalsSS.StringDelimiters.static_stringDelimiter_COMMA.join(str(int(item)) for item in listDameParents))
                        self.obj_Log_Debug_Display.debug('Pop Info_Field Update - LIFE_STAGE: Mature -> Gestating for ' + str(len(listUniqueDameParents)) + ' UNIQUE Dame Female Parents: ' + globalsSS.StringDelimiters.static_stringDelimiter_COMMA.join(str(int(item)) for item in listUniqueDameParents))
                    pass
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    #pass
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 


                pop_Out = pop_In
                
                return pop_Out
                   
 
            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            Mating Schemes
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
            def SpecifyMatingScheme(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()

#                 if self.objSSParametersLocal.intCurrentFertilisation == 0:
#                     objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating_ORIG()
#                     pass
#                 else:

            
                '''
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                CURRENT Mating Schemes
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                '''

                if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Sexual_Random_Mating_LS_with_SELFING_with_REPLACEMENT:
                    if self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_Diploid_Sexual_Random_Mating_LS_with_SELFING_with_REPLACEMENT()
                    else:
                        objMatingScheme = self.method_MatingScheme_Diploid_Sexual_Random_Mating_LS_with_SELFING_with_REPLACEMENT()
                    pass
                pass
            
                if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Sexual_Random_Mating_LS_WITHOUT_SELFING_with_REPLACEMENT:
                    if self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_Diploid_Sexual_Random_Mating_LS_WITHOUT_SELFING_with_REPLACEMENT()
                    else:
                        objMatingScheme = self.method_MatingScheme_Diploid_Sexual_Random_Mating_LS_WITHOUT_SELFING_with_REPLACEMENT()
                    pass
                pass
            
                if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Sexual_Random_Mating_LS_WITHOUT_SELFING_WITHOUT_REPLACEMENT:
                    if self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_Diploid_Sexual_Random_Mating_LS_WITHOUT_SELFING_WITHOUT_REPLACEMENT()
                    else:
                        objMatingScheme = self.method_MatingScheme_Diploid_Sexual_Random_Mating_LS_WITHOUT_SELFING_WITHOUT_REPLACEMENT()
                    pass
                pass
            
                if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Sexual_Random_POLYANDROUS_Mating_LS_WITHOUT_SELFING_with_REPLACEMENT:
                    if self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_Diploid_Sexual_Random_POLYANDROUS_Mating_LS_WITHOUT_SELFING_with_REPLACEMENT()
                    else:
                        objMatingScheme = self.method_MatingScheme_Diploid_Sexual_Random_POLYANDROUS_Mating_LS_WITHOUT_SELFING_with_REPLACEMENT()
                    pass
                pass
            
                '''
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Unused Mating Schemes
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                '''
                if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Sexual_Random_Mating_LS_with_SELFING_with_REPLACEMENT_CONTROLLED_ALLELE_FREQS:
                    if self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_Diploid_Sexual_Random_Mating_LS_with_SELFING_with_REPLACEMENT_CONTROLLED_ALLELE_FREQS()
                    else:
                        objMatingScheme = self.method_MatingScheme_Diploid_Sexual_Random_Mating_LS_with_SELFING_with_REPLACEMENT_CONTROLLED_ALLELE_FREQS()
                    pass
                pass
            
                # WF_Diploid_Sexual_Random_Mating with HARDCODING 1
                if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_WF_Diploid_Sexual_Random_Mating_HARDCODED_1:
                    if self.objSSParametersLocal.boolInitialEvolve:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating_HARDCODED_1()
                    elif self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating_HARDCODED_1()
                    else:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating_HARDCODED_1()
                    pass
                pass
            
                # WF_Diploid_Sexual_Random_Mating
                if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_WF_Diploid_Sexual_Random_Mating:
                    if self.objSSParametersLocal.boolInitialEvolve:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating()
                    elif self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating()
                    else:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating()
                # WF_Diploid_Sexual_Random_Mating using the simupop RANDOM PARENT CHOOSER
                if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_WF_Diploid_Sexual_Random_Mating_RANDOM_PARENT_CHOOSER:
                    if self.objSSParametersLocal.boolInitialEvolve:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_PARENT_CHOOSER()
                    elif self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_PARENT_CHOOSER()
                    else:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_PARENT_CHOOSER()

                # WF_Diploid_Sexual_Random_Mating using the simupop RANDOM PARENT CHOOSER
                if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_with_REPLACEMENT:
                    if self.objSSParametersLocal.boolInitialEvolve:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_with_REPLACEMENT()
                    elif self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_with_REPLACEMENT()
                    else:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_with_REPLACEMENT()

                # WF_Diploid_Sexual_Random_Mating
                if self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_WITHOUT_REPLACEMENT:
                    if self.objSSParametersLocal.boolInitialEvolve:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_WITHOUT_REPLACEMENT()
                    elif self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_WITHOUT_REPLACEMENT()
                    else:
                        objMatingScheme = self.method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_WITHOUT_REPLACEMENT()
                
                # Diploid_Dioecious_Random_Mating_WITH_Replacement using simupops parent chooser        
                elif self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP:
                    if self.objSSParametersLocal.boolInitialEvolve:
                        objMatingScheme = self.method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP()
                    elif self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP()
                    else:
                        objMatingScheme = self.method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP()
                
                # Diploid_Dioecious_Random_Mating_WITH_Replacement using my parent choosers 
                #2014-12-15 - Current mating scheme for both CAPL & CAOB      
                elif self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Random_Mating_WITH_Replacement:
                    if self.objSSParametersLocal.boolInitialEvolve:
                        objMatingScheme = self.method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement()
                    elif self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement()
                    else:
                        objMatingScheme = self.method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement()
                
                #Diploid_Dioecious_Random_Mating_WITHOUT_Replacement using my parent choosers 
                elif self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Random_Mating_WITHOUT_Replacement:
                    if self.objSSParametersLocal.boolInitialEvolve:
                        objMatingScheme = self.method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement()
                    elif self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_Diploid_Dioecious_Random_Mating_WITHOUT_Replacement()
                    else:
                        objMatingScheme = self.method_MatingScheme_Diploid_Dioecious_Random_Mating_WITHOUT_Replacement()
                
                # Diploid_Monecious_Random_Mating  using simupops parent chooser
                elif self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Monecious_Random_Mating_SP:
                    if self.objSSParametersLocal.boolInitialEvolve:
                        objMatingScheme = self.method_MatingScheme_Diploid_Monecious_Random_Mating()
                    elif self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_Diploid_Monecious_Random_Mating()
                    else:
                        objMatingScheme = self.method_MatingScheme_Diploid_Monecious_Random_Mating()

                # Diploid_Polygamous_Random_Mating  using simupops parent chooser    
                elif self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Dioecious_Polyandrous_Random_Mating_SP:
                    if self.objSSParametersLocal.boolInitialEvolve:
                        objMatingScheme = self.method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP()
                    elif self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_Diploid_Dioecious_Random_Mating_WITHOUT_Replacement()
                    else:
                        objMatingScheme = self.method_MatingScheme_Diploid_Dioecious_Random_Mating_WITHOUT_Replacement()
                    
                # Diploid_Polygamous_Random_Mating using simupops parent chooser    
                elif self.objSSParametersLocal.intMatingSchemeType == globalsSS.MatingSchemeType.static_Diploid_Polygamous_Random_Mating_SP:
                    if self.objSSParametersLocal.boolInitialEvolve:
                        objMatingScheme = self.method_MatingScheme_Diploid_Polygamous_Random_Mating()
                    elif self.objSSParametersLocal.boolBurnIn:
                        objMatingScheme = self.method_MatingScheme_Diploid_Polygamous_Random_Mating()
                    else:
                        objMatingScheme = self.method_MatingScheme_Diploid_Polygamous_Random_Mating()

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass

                                           
                        
                return objMatingScheme


            def method_Specify_Mating_Offspring_Sex_Scheme(self):
                
                if self.objSSParametersLocal.intOffspringSexScheme == globalsSS.MatingOffspringSexModeSchemeType.static_int_Mating_Offspring_Sex_Mode_PROB_OF_MALES:
                    sexMode=(simupop.PROB_OF_MALES, self.objSSParametersLocal.floatSexRatioOfMales)
                elif self.objSSParametersLocal.intOffspringSexScheme == globalsSS.MatingOffspringSexModeSchemeType.static_int_Mating_Offspring_Sex_Mode_GLOBAL_SEQ_OF_SEX_MF:
                    sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE)
                else:
                    sexMode=(simupop.PROB_OF_MALES, self.objSSParametersLocal.floatSexRatioOfMales)
                pass
            
                return sexMode


            def func_Controlled_Offspring_Allele_Freqs(self, gen):
                
                int_Locus = 0
                
                list_Allele_Freqs_For_Locus = []
                 
                dict_Locus_Alleles = self.objSSParametersLocal.odictAlleleFreqsAtSimInitialization[int_Locus]
                 
                for key, value in dict_Locus_Alleles.iteritems():
                    list_Allele_Freqs_For_Locus.append(value['Allele_Freq'])
                pass
            
                #list_Allele_Freqs_For_Locus = self.objSSParametersLocal.listAlleleFreqs_Entire
                
                return list_Allele_Freqs_For_Locus
            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            CURRENT Mating Schemes
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
            def method_MatingScheme_Diploid_Sexual_Random_Mating_LS_with_SELFING_with_REPLACEMENT(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
                
                #simupop.RNG(name=None, seed=0)
                
                self.obj_Log_Debug_Display.debug('MATING: Random Number Generator (RNG): ' + str(simupop.getRNG().name()))
                self.obj_Log_Debug_Display.debug('MATING: Random Seed: ' + str(simupop.getRNG().seed()))
                self.obj_Log_Debug_Display.debug('MATING: method_MatingScheme_Diploid_Sexual_Random_Mating_LS_with_SELFING_with_REPLACEMENT')
                    
                #self.method_Debug_Mating()
                
                objMatingScheme = simupop.HeteroMating(
                            [
                             #All this CloneMating does is remove individuals in the Died VSP
                             simupop.CloneMating(subPops=[(0, intVSP) for intVSP in range(0, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_NumberofVSPs - 1)], weight=-1),
                             # Random Mating for individuals in mating ages
                             simupop.RandomMating(
                                    ops=[
                                         # give new born an ID
                                         simupop.IdTagger(),
                                         # track parents of each individual                   
                                         simupop.PedigreeTagger(),   
                                         # transmit genotype          
                                         simupop.MendelianGenoTransmitter(), 
                                         # set the offspring info fields to their initial values  
                                         simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                         simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                         simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                        ],
                                    #sex ratio of offspring per mating pair determined by ssParameter intOffspringSexScheme
                                    sexMode=self.method_Specify_Mating_Offspring_Sex_Scheme()
                                    #number of offspring per mating pair as specified by list of distribution parameters supplied
                                    ,numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters) 
                                    #VSP to get the mating pairs from
                                    ,subPops=[(0, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult)] #VSP to mate
                                    #,subPops=[(0, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult)] #VSP to mate
                                    )])

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)

                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    #pass
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                                        
                return objMatingScheme
            
            
            def method_MatingScheme_Diploid_Sexual_Random_Mating_LS_WITHOUT_SELFING_with_REPLACEMENT(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
                                    
                self.obj_Log_Default_Display.info('MATING: method_MatingScheme_Diploid_Sexual_Random_Mating_LS_WITHOUT_SELFING_with_REPLACEMENT')
                    
                #self.method_Debug_Mating()
                
                objMatingScheme = simupop.HeteroMating(
                            [
                             #All this CloneMating does is remove individuals in the Died VSP
                             simupop.CloneMating(subPops=[(0, intVSP) for intVSP in range(0, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_NumberofVSPs - 1)], weight=-1),
                             # Random Mating for individuals in mating ages
                             simupop.HomoMating(
                                #Choose parents randomly by sex - parents should always be a MALE-FEMALE pair unlike diploid sexual Wright-Fisher random mating                                             
                                chooser=simupop.CombinedParentsChooser(simupop.RandomParentChooser(sexChoice=simupop.MALE_ONLY,replacement=True), simupop.RandomParentChooser(sexChoice=simupop.FEMALE_ONLY,replacement=True)),
                                generator=simupop.OffspringGenerator(
                                    ops=[
                                         # give new born an ID
                                         simupop.IdTagger(),
                                         # track parents of each individual                   
                                         simupop.PedigreeTagger(),   
                                         # transmit genotype          
                                         simupop.MendelianGenoTransmitter(), 
                                         # set the offspring info fields to their initial values  
                                         simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                         simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                         simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                        ],
                                    #sex ratio of offspring per mating pair determined by ssParameter intOffspringSexScheme
                                    sexMode=self.method_Specify_Mating_Offspring_Sex_Scheme()
                                    #number of offspring per mating pair as specified by list of distribution parameters supplied
                                    ,numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters)
                                    ) #End OffspringGenerator
                                    #VSP to get the mating pairs from
                                    ,subPops=[(0, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult)] #VSP to mate
                                    )])

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)

                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    #pass
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                                        
                return objMatingScheme
            
            
            def method_MatingScheme_Diploid_Sexual_Random_Mating_LS_WITHOUT_SELFING_WITHOUT_REPLACEMENT(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
                                    
                self.obj_Log_Default_Display.info('MATING: method_MatingScheme_Diploid_Sexual_Random_Mating_LS_WITHOUT_SELFING_WITHOUT_REPLACEMENT')
                    
                #self.method_Debug_Mating()
                
                objMatingScheme = simupop.HeteroMating(
                            [
                             #All this CloneMating does is remove individuals in the Died VSP
                             simupop.CloneMating(subPops=[(0, intVSP) for intVSP in range(0, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_NumberofVSPs - 1)], weight=-1),
                             # Random Mating for individuals in mating ages
                             simupop.HomoMating(
                                #Choose parents randomly by sex - parents should always be a MALE-FEMALE pair unlike diploid sexual Wright-Fisher random mating                                             
                                chooser=simupop.CombinedParentsChooser(simupop.RandomParentChooser(sexChoice=simupop.MALE_ONLY,replacement=False), simupop.RandomParentChooser(sexChoice=simupop.FEMALE_ONLY,replacement=False)),
                                generator=simupop.OffspringGenerator(
                                    ops=[
                                         # give new born an ID
                                         simupop.IdTagger(),
                                         # track parents of each individual                   
                                         simupop.PedigreeTagger(),   
                                         # transmit genotype          
                                         simupop.MendelianGenoTransmitter(), 
                                         # set the offspring info fields to their initial values  
                                         simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                         simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                         simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                        ],
                                    #sex ratio of offspring per mating pair determined by ssParameter intOffspringSexScheme
                                    sexMode=self.method_Specify_Mating_Offspring_Sex_Scheme()
                                    #number of offspring per mating pair as specified by list of distribution parameters supplied
                                    ,numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters)
                                    ) #End OffspringGenerator
                                    #VSP to get the mating pairs from
                                    ,subPops=[(0, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult)] #VSP to mate
                                    )])

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)

                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    #pass
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                                        
                return objMatingScheme
            
            
            def method_MatingScheme_Diploid_Sexual_Random_POLYANDROUS_Mating_LS_WITHOUT_SELFING_with_REPLACEMENT(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
                                    
                self.obj_Log_Default_Display.info('MATING: method_MatingScheme_Diploid_Sexual_Random_POLYANDROUS_Mating_LS_WITHOUT_SELFING_with_REPLACEMENT')
                    
                #self.method_Debug_Mating()
                
                objMatingScheme = simupop.HeteroMating(
                            [
                             #All this CloneMating does is remove individuals in the Died VSP
                             simupop.CloneMating(subPops=[(0, intVSP) for intVSP in range(0, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_NumberofVSPs - 1)], weight=-1),
                             # Random Mating for individuals in mating ages
                             # random POLYANDEROUS mating for individuals in mating ages
                             simupop.PolygamousMating(
                                    polySex = simupop.FEMALE,
                                    polyNum = self.objSSParametersLocal.intPolygamousMateNumber,
                                    ops=[
                                         # give new born an ID
                                         simupop.IdTagger(),
                                         # track parents of each individual                   
                                         simupop.PedigreeTagger(),   
                                         # transmit genotype          
                                         simupop.MendelianGenoTransmitter(), 
                                         # set the offspring info fields to their initial values  
                                         simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                         simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                         simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                        ],
                                    #sex ratio of offspring per mating pair determined by ssParameter intOffspringSexScheme
                                    sexMode=self.method_Specify_Mating_Offspring_Sex_Scheme()
                                    #number of offspring per mating pair as specified by list of distribution parameters supplied
                                    ,numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters)
                                    #VSP to get the mating pairs from
                                    ,subPops=[(0, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult)] #VSP to mate
                                    )])

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)

                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    #pass
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                                        
                return objMatingScheme
            
            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            Unused Mating Schemes
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
            def method_MatingScheme_Diploid_Sexual_Random_Mating_LS_with_SELFING_with_REPLACEMENT_CONTROLLED_ALLELE_FREQS(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
                                    
                self.obj_Log_Default_Display.info('MATING: method_MatingScheme_Diploid_Sexual_Random_Mating_LS_with_SELFING_with_REPLACEMENT_CONTROLLED_ALLELE_FREQS')
                    
                #self.method_Debug_Mating()
                objMatingScheme = simupop.HeteroMating(
                            [
                             #All this CloneMating does is remove individuals in the Died VSP
                             simupop.CloneMating(subPops=[(0, intVSP) for intVSP in range(0, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_NumberofVSPs - 1)], weight=-1),
                             # Random Mating for individuals in mating ages
                             simupop.ControlledRandomMating(
                                    #loci=[x for x in range(0, self.objSSParametersLocal.nLoci)]
                                    #,alleles=self.objSSParametersLocal.listAlleleCounts_Entire
                                    loci=0
                                    ,alleles=[0,1,2,3,4,5]
                                    ,freqFunc=self.func_Controlled_Offspring_Allele_Freqs
                                    ,ops=[
                                         # give new born an ID
                                         simupop.IdTagger(),
                                         # track parents of each individual                   
                                         simupop.PedigreeTagger(),   
                                         # transmit genotype          
                                         simupop.MendelianGenoTransmitter(), 
                                         # set the offspring info fields to their initial values  
                                         simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                         simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                         simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                        ],
                                    #sex ratio of offspring per mating pair determined by ssParameter intOffspringSexScheme
                                    sexMode=self.method_Specify_Mating_Offspring_Sex_Scheme()
                                    #number of offspring per mating pair as specified by list of distribution parameters supplied
                                    ,numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters) 
                                    #VSP to get the mating pairs from
                                    ,subPops=[(0, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult)] #VSP to mate
                                    )])

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)

                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    #pass
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                                        
                return objMatingScheme
            
            
           
            '''@profile'''    
            def method_MatingScheme_Diploid_Dioecious_Random_Mating_WITHOUT_Replacement(self):

                '''
                !!! This mating scheme will only work if the number of ofspring is filled before all the parent are exhaused.  
                !!! Otherwise a runtime error occurs.
                ''' 
                
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    #print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_WF_Diploid_Sexual_Random_Mating_OLD - START   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass

                self.method_Debug_Mating()
                
                objMatingScheme = simupop.HeteroMating([
                
                                simupop.HomoMating(
                                   chooser=simupop.PyParentsChooser(self.method_ParentChooser_RandomParentPairs),
                                   #chooser=simupop.CombinedParentsChooser(PyParentsChooser(self.method_ParentChooser_RandomMaleWITHOUTReplacement), PyParentsChooser(self.method_ParentChooser_RandomFemaleWITHOUTReplacement)),
                                   #chooser=simupop.CombinedParentsChooser(PyParentsChooser(self.method_ParentChooser_RandomMaleWithReplacement), PyParentsChooser(self.method_ParentChooser_RandomFemaleWithReplacement)),
                                   generator=simupop.OffspringGenerator(
                                                                   ops=[
                                                                       # transmit genotype
                                                                       simupop.MendelianGenoTransmitter(),
                                                                       #Recombine loci prior to mating - MUST go prior to IdTagger()
                                                                       #simupop.Recombinator(simupop.ALL_AVAIL),
                                                                       # new ID for offspring
                                                                       simupop.IdTagger(),
                                                                       
                                                                       simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                                                       simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                                                       #InfoExec('birth_generation=gen'),
                                                                       #InfoExec('birth_generation+=1'),
                                                                       #InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentEvolveFertilisation)),
                                                                       simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                                                       simupop.InfoExec('age_in_months=0'),
                                                                       #InfoExec('age_in_months=' + str(self.objSSParametersLocal.intGestationLengthInMonths)),
                                                                       simupop.InfoExec('parturation_season_interval_in_months=' + str(self.objSSParametersLocal.intParturationSeasonIntervalInMonths)),
                                                                       # InfoField=age will always be zero and will not be subsequently updated in the pedigree file.  Only the initial population will have valid ages in pedigree file.
                                                                       # Record complete pedigree for all generation post-zero generation.  This will only work properly here not at postOps or finalOps.
                                                                       #Onlu outputs offspring per generation not entire population in a gen
                                                                       #sim.PedigreeTagger(output='>>' + self.objSSParametersLocal.outputFileNameIndividualMatingPedigreeLogPostZeroGens, outputFields=['birth_generation','age'], outputLoci=simupop.ALL_AVAIL),
                
                                                                       #Tag all offspring with parent id's
                                                                       simupop.PedigreeTagger()
                                   
                                                                       ], 
                                                                   #number of offspring as specified by list of distribution parameters supplied
                                                                   numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters),
                                                                   #sex ratio of offspring
                                                                   #sexMode=(PROB_OF_MALES, self.objSSParametersLocal.numfloatSexRatioOfMales)),
                                                                   sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE))
                                   , weight=1),
                                   #, subPops=[(0, 2)], weight=1),  #VSPs are not allowed for PyParentChooser but I an submitting only parents from the mature VSP so that is ok
                                   #)
                        # ? individuals with age over maxAge are not involved in mating. (died)
                        # individuals not in mating ages are copied to the next generation.
                        # age <= maxAge, copy to the next generation (weight=-1)
                        simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3)], weight=-1),
                       ])

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    #print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_WF_Diploid_Sexual_Random_Mating_OLD - END   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass
                
                return objMatingScheme
            
            
            def method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                                   
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    #print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement - START   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass
                
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #self.method_Debug_Mating()
                    pass

                objMatingScheme = simupop.HeteroMating(
                            [
                             # ? individuals with age over maxAge are not involved in mating. (died)
                             # individuals not in mating ages are copied to the next generation.
                             # age <= maxAge, copy to the next generation (weight=-1)
                             simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3)], weight=-1),
                             # random mating for individuals in mating ages
                             simupop.HomoMating(
                                #Choose parents from randomly selected males and females of reproductive age                                                
                                chooser=simupop.PyParentsChooser(self.method_ParentChooser_RandomParentPairs),
                                generator=simupop.OffspringGenerator(
                                    ops=[
                                         simupop.IdTagger(),                   # give new born an ID
                                         simupop.PedigreeTagger(),             # track parents of each individual
                                         simupop.MendelianGenoTransmitter(),   # transmit genotype
                                         simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                         simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                         simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                        ],
                                    #sex ratio of offspring
                                    sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE),
                                    #number of offspring as specified by list of distribution parameters supplied
                                    numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters)))])
                
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    #print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement - END   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass      
                                        
                return objMatingScheme
            
            
            def method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement_OLD(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                   t2 = Timer2(True)
                   t2.Start()
                                   
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement - START   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass
                
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #self.method_Debug_Mating()
                    pass
                
                objMatingScheme = simupop.HeteroMating([
                
                simupop.HomoMating(
                                   chooser=simupop.PyParentsChooser(self.method_ParentChooser_RandomParentPairs),
                                   #chooser=simupop.CombinedParentsChooser(PyParentsChooser(self.method_ParentChooser_RandomMaleWITHOUTReplacement), PyParentsChooser(self.method_ParentChooser_RandomFemaleWITHOUTReplacement)),
                                   #chooser=simupop.CombinedParentsChooser(PyParentsChooser(self.method_ParentChooser_RandomMaleWithReplacement), PyParentsChooser(self.method_ParentChooser_RandomFemaleWithReplacement)),
                                   generator=simupop.OffspringGenerator(
                                                                   ops=[
                                                                       # transmit genotype
                                                                       simupop.MendelianGenoTransmitter(),
                                                                       #Recombine loci prior to mating - MUST go prior to IdTagger()
                                                                       #simupop.Recombinator(simupop.ALL_AVAIL),
                                                                       # new ID for offspring
                                                                       simupop.IdTagger(),
                                                                       
                                                                       simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                                                       simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                                                       #InfoExec('birth_generation=gen'),
                                                                       #InfoExec('birth_generation+=1'),
                                                                       #InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentEvolveFertilisation)),
                                                                       simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                                                       simupop.InfoExec('age_in_months=0'),
                                                                       #InfoExec('age_in_months=' + str(self.objSSParametersLocal.intGestationLengthInMonths)),
                                                                       simupop.InfoExec('parturation_season_interval_in_months=' + str(self.objSSParametersLocal.intParturationSeasonIntervalInMonths)),
                                                                       # InfoField=age will always be zero and will not be subsequently updated in the pedigree file.  Only the initial population will have valid ages in pedigree file.
                                                                       # Record complete pedigree for all generation post-zero generation.  This will only work properly here not at postOps or finalOps.
                                                                       #Onlu outputs offspring per generation not entire population in a gen
                                                                       #sim.PedigreeTagger(output='>>' + self.objSSParametersLocal.outputFileNameIndividualMatingPedigreeLogPostZeroGens, outputFields=['birth_generation','age'], outputLoci=simupop.ALL_AVAIL),
                
                                                                       #Tag all offspring with parent id's
                                                                       simupop.PedigreeTagger()
                                   
                                                                       ], 
                                                                   #number of offspring as specified by list of distribution parameters supplied
                                                                   numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters),
                                                                   #sex ratio of offspring
                                                                   #sexMode=(simupop.PROB_OF_MALES, self.objSSParametersLocal.floatSexRatioOfMales))
                                                                   sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE))
                                   , weight=1),
                                   #, subPops=[(0, 2)], weight=1),  #VSPs are not allowed for PyParentChooser but I an submitting only parents from the mature VSP so that is ok
                                   #)
                        # ? individuals with age over maxAge are not involved in mating. (died)
                        # individuals not in mating ages are copied to the next generation.
                        # age <= maxAge, copy to the next generation (weight=-1)
                        simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3)], weight=-1),
                       ])

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement - END   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass  
                                        
                return objMatingScheme

            '''@profile'''
            def method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                                    
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP - START   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass
                    
                self.method_Debug_Mating()
                
                objMatingScheme = simupop.HeteroMating(
                            [
                             # ? individuals with age over maxAge are not involved in mating. (died)
                             # individuals not in mating ages are copied to the next generation.
                             # age <= maxAge, copy to the next generation (weight=-1)
                             simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3)], weight=-1),
                             # random mating for individuals in mating ages
                             simupop.HomoMating(
                                #Choose parents randomly by sex - parents should always be a MALE-FEMALE pair unlike diploid sexual Wright-Fisher random mating                                             
                                chooser=simupop.CombinedParentsChooser(simupop.RandomParentChooser(sexChoice=simupop.MALE_ONLY,replacement=True), simupop.RandomParentChooser(sexChoice=simupop.FEMALE_ONLY,replacement=True)),
                                generator=simupop.OffspringGenerator(
                                    ops=[
                                         simupop.IdTagger(),                   # give new born an ID
                                         simupop.PedigreeTagger(),             # track parents of each individual
                                         simupop.MendelianGenoTransmitter(),   # transmit genotype
                                         simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                         simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                         simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                        ],
                                    #sex ratio of offspring
                                    #----2015-03-19--> sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE),
                                    #----2015-03-19--> sexMode=(simupop.PROB_OF_MALES, self.objSSParametersLocal.floatSexRatioOfMales),
                                    sexMode=self.method_Specify_Mating_Offspring_Sex_Scheme(), #determined by ssParameter intOffspringSexScheme
                                    numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters)), #number of offspring as specified by list of distribution parameters supplied
                                    subPops=[(0, globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult)])]) #VSP to mate
                             
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP - END   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass  
                                        
                return objMatingScheme

                       
            '''@profile'''
            def method_MatingScheme_WF_Diploid_Sexual_Random_Mating_HARDCODED_1(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                                    
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    #print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_WF_Diploid_Sexual_Random_Mating - START   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass
                    
                #self.method_Debug_Mating()
                
                objMatingScheme = simupop.HeteroMating(
                            [
                             # ? individuals with age over maxAge are not involved in mating. (died)
                             # individuals not in mating ages are copied to the next generation.
                             # age <= maxAge, copy to the next generation (weight=-1)
                             simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3)], weight=-1),
                             # random mating for individuals in mating ages
                             simupop.RandomMating(
                                    ops=[
                                         simupop.IdTagger(),                   # give new born an ID
                                         simupop.PedigreeTagger(),             # track parents of each individual
                                         simupop.MendelianGenoTransmitter(),   # transmit genotype
                                         simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                         simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                         simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                        ]
                                    #sex ratio of offspring
                                    #----2015-03-19--> sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE),
                                    #----2015-03-19--> sexMode=(simupop.PROB_OF_MALES, self.objSSParametersLocal.floatSexRatioOfMales),
                                    ,sexMode=(simupop.PROB_OF_MALES, 0.5) #determined by ssParameter intOffspringSexScheme
                                    ,numOffspring= 1 #number of offspring as specified by list of distribution parameters supplied
                                    ,subPops=[(0, 2)] #VSP to mate
                                    )])

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    #print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_WF_Diploid_Sexual_Random_Mating - END   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass  
                                        
                return objMatingScheme
            
            '''@profile'''
            def method_MatingScheme_WF_Diploid_Sexual_Random_Mating(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                                    
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    #print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_WF_Diploid_Sexual_Random_Mating - START   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass
                    
                #self.method_Debug_Mating(pop_In)
                
                objMatingScheme = simupop.HeteroMating(
                            [
                             # ? individuals with age over maxAge are not involved in mating. (died)
                             # individuals not in mating ages are copied to the next generation.
                             # age <= maxAge, copy to the next generation (weight=-1)
                             simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3)], weight=-1),
                             # random mating for individuals in mating ages
                             simupop.RandomMating(
                                    ops=[
                                         simupop.IdTagger(),                   # give new born an ID
                                         simupop.PedigreeTagger(),             # track parents of each individual
                                         simupop.MendelianGenoTransmitter(),   # transmit genotype
                                         simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                         simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                         simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                        ],
                                    #sex ratio of offspring
                                    #----2015-03-19--> sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE),
                                    #----2015-03-19--> sexMode=(simupop.PROB_OF_MALES, self.objSSParametersLocal.floatSexRatioOfMales),
                                    sexMode=self.method_Specify_Mating_Offspring_Sex_Scheme() #determined by ssParameter intOffspringSexScheme
                                    ,numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters) #number of offspring as specified by list of distribution parameters supplied
                                    ,subPops=[(0, globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult)] #VSP to mate
                                    )])

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    #print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_WF_Diploid_Sexual_Random_Mating - END   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass  
            
                return objMatingScheme
            
            '''@profile'''
            def method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_PARENT_CHOOSER(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                                    
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP - START   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass
                    
                self.method_Debug_Mating()
                
                objMatingScheme = simupop.HeteroMating(
                            [
                             # ? individuals with age over maxAge are not involved in mating. (died)
                             # individuals not in mating ages are copied to the next generation.
                             # age <= maxAge, copy to the next generation (weight=-1)
                             simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3)], weight=-1),
                             # random mating for individuals in mating ages
                             simupop.HomoMating(
                                #Choose parents randomly irrespective of sex - with an even # of each sex the chance of a hermaphroditic mating should be 1/N
                                chooser=simupop.CombinedParentsChooser(simupop.RandomParentChooser(replacement=True), simupop.RandomParentChooser(replacement=True)),                                
                                generator=simupop.OffspringGenerator(
                                    ops=[
                                         simupop.IdTagger(),                   # give new born an ID
                                         simupop.PedigreeTagger(),             # track parents of each individual
                                         simupop.MendelianGenoTransmitter(),   # transmit genotype
                                         simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                         simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                         simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                        ],
                                    #sex ratio of offspring
                                    #----2015-03-19--> sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE),
                                    #----2015-03-19--> sexMode=(simupop.PROB_OF_MALES, self.objSSParametersLocal.floatSexRatioOfMales),
                                    sexMode=self.method_Specify_Mating_Offspring_Sex_Scheme() #determined by ssParameter intOffspringSexScheme
                                    ,numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters)) #number of offspring as specified by list of distribution parameters supplied
                                    ,subPops=[(0, globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult)] #VSP to mate
                                    )])
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP - END   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass  
                                        
                return objMatingScheme

            '''@profile'''
            def method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_with_REPLACEMENT(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                                    
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_with_REPLACEMENT - START   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass
                    
                self.method_Debug_Mating()
                
                objMatingScheme = simupop.HeteroMating(
                            [
                             # ? individuals with age over maxAge are not involved in mating. (died)
                             # individuals not in mating ages are copied to the next generation.
                             # age <= maxAge, copy to the next generation (weight=-1)
                             simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3)], weight=-1),
                             # random mating for individuals in mating ages
                             simupop.HomoMating(
                                #Choose parents randomly by sex - parents should always be a MALE-FEMALE pair unlike diploid sexual Wright-Fisher random mating                                             
                                chooser=simupop.CombinedParentsChooser(simupop.RandomParentChooser(sexChoice=simupop.MALE_ONLY,replacement=True), simupop.RandomParentChooser(sexChoice=simupop.FEMALE_ONLY,replacement=True)),
                                generator=simupop.OffspringGenerator(
                                    ops=[
                                         simupop.IdTagger(),                   # give new born an ID
                                         simupop.PedigreeTagger(),             # track parents of each individual
                                         simupop.MendelianGenoTransmitter(),   # transmit genotype
                                         simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                         simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                         simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                        ],
                                    #sex ratio of offspring
                                    #----2015-03-19--> sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE),
                                    #----2015-03-19--> sexMode=(simupop.PROB_OF_MALES, self.objSSParametersLocal.floatSexRatioOfMales),
                                    sexMode=self.method_Specify_Mating_Offspring_Sex_Scheme() #determined by ssParameter intOffspringSexScheme
                                    ,numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters)) #number of offspring as specified by list of distribution parameters supplied
                                    ,subPops=[(0, globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult)] #VSP to mate
                                    )])
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_with_REPLACEMENT - END   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass  
                                        
                return objMatingScheme
            
            '''@profile'''
            def method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_WITHOUT_REPLACEMENT(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                                    
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_WITHOUT_REPLACEMENT - START   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass
                    
                self.method_Debug_Mating()
                
                objMatingScheme = simupop.HeteroMating(
                            [
                             # ? individuals with age over maxAge are not involved in mating. (died)
                             # individuals not in mating ages are copied to the next generation.
                             # age <= maxAge, copy to the next generation (weight=-1)
                             simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3)], weight=-1),
                             # random mating for individuals in mating ages
                             simupop.HomoMating(
                                #Choose parents randomly by sex - parents should always be a MALE-FEMALE pair unlike diploid sexual Wright-Fisher random mating                                             
                                chooser=simupop.CombinedParentsChooser(simupop.RandomParentChooser(sexChoice=simupop.MALE_ONLY,replacement=False), simupop.RandomParentChooser(sexChoice=simupop.FEMALE_ONLY,replacement=False)),
                                generator=simupop.OffspringGenerator(
                                    ops=[
                                         simupop.IdTagger(),                   # give new born an ID
                                         simupop.PedigreeTagger(),             # track parents of each individual
                                         simupop.MendelianGenoTransmitter(),   # transmit genotype
                                         simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                         simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                         simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                        ],
                                    #sex ratio of offspring
                                    #----2015-03-19--> sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE),
                                    #----2015-03-19--> sexMode=(simupop.PROB_OF_MALES, self.objSSParametersLocal.floatSexRatioOfMales),
                                    sexMode=self.method_Specify_Mating_Offspring_Sex_Scheme() #determined by ssParameter intOffspringSexScheme
                                    ,numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters)) #number of offspring as specified by list of distribution parameters supplied
                                    ,subPops=[(0, globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult)] #VSP to mate
                                    )])
                
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_WF_Diploid_Sexual_Random_Mating_RANDOM_EQUAL_SEX_PARENT_CHOOSER_WITHOUT_REPLACEMENT - END   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass  
                                        
                return objMatingScheme
            
            
            def method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP_NEWISH(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                                    
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP - START   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass

                self.method_Debug_Mating()

                objMatingScheme = simupop.HeteroMating(
                            [
                             # ? individuals with age over maxAge are not involved in mating. (died)
                             # individuals not in mating ages are copied to the next generation.
                             # age <= maxAge, copy to the next generation (weight=-1)
                             simupop.CloneMating(subPops=[(0, x) for x in (0, 1, 2, 3)], weight=-1),
                             # random mating for individuals in mating ages
                             simupop.HomoMating(
                                #Choose parents randomly by sex - parents should always be a MALE-FEMALE pair unlike diploid sexual Wright-Fisher random mating                                             
                                chooser=simupop.CombinedParentsChooser(simupop.RandomParentChooser(sexChoice=simupop.MALE_ONLY,replacement=True), simupop.RandomParentChooser(sexChoice=simupop.FEMALE_ONLY,replacement=True)),
                                generator=simupop.OffspringGenerator(
                                    ops=[
                                         simupop.IdTagger(),                   # give new born an ID
                                         simupop.PedigreeTagger(),             # track parents of each individual
                                         simupop.MendelianGenoTransmitter(),   # transmit genotype
                                         simupop.InfoExec('age_class=' + str(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)),
                                         simupop.InfoExec('life_stage=' + str(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)),
                                         simupop.InfoExec('birth_generation=' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation)),
                                        ],
                                    #sex ratio of offspring
                                    #----2015-03-19 sexMode=(simupop.GLOBAL_SEQUENCE_OF_SEX, simupop.MALE, simupop.FEMALE),
                                    sexMode=(simupop.PROB_OF_MALES, self.objSSParametersLocal.floatSexRatioOfMales),
                                    
                                    #subPops=[(0, globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult)])])
                                    #number of offspring as specified by list of distribution parameters supplied
                                    numOffspring=(self.objSSParametersLocal.listOffspringNumberParameters)),
                                    subPops=[(0, globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult)])])
                             
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:   
                    print('\n <<<<<<<<<<<<<<<<<<< method_MatingScheme_Diploid_Dioecious_Random_Mating_WITH_Replacement_SP - END   <<<<<<<<<<<<<<<<<<<<<\n')
                    pass

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass  
                                        
                return objMatingScheme
            
            
            def method_Debug_Mating_PREV(self):

                '''Message output '''
                with SSOutputHandler() as SSOutputOperation:
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        listOutputDestinations = [ self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    else:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, 'Pre-Mating Stats')
                    #
                    stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> Population Size:' + str([int(x) for x in self.pop.subPopSizes(globalsSS.SP_SubPops.static_intSP_SubPop_Primary)]) + ' >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                    boolNewline=True
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                 
                    intNumVSPS = self.pop.numVirtualSubPop()
                    listVSPSizes = []
                    for intVSP in range(0, intNumVSPS):
                        intVSPSize = int(self.pop.subPopSize([globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVSP]))
                        listVSPSizes.append(intVSPSize)   

                    '''Message output '''
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    else:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> ' + 'VSP Sizes: ' + str(listVSPSizes) + ' >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                    boolNewline=False
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                    #
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    else:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #    
                    SSOutputOperation.methodOutput_SimGeneralMessageFooter(listOutputDestinations, 'Pre-Mating Stats')

                #DEBUG_ON
                #raw_input('\n AT MATING -Press return to close this window... \n')
                #DEBUG_OFF

                #pass
                return True
             
            def method_Debug_Mating(self, pop_In):

                '''Message output '''
                with SSOutputHandler() as SSOutputOperation:
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        listOutputDestinations = [ self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    else:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, 'Pre-Mating Stats')
                    #
                    stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> Population Size:' + str([int(x) for x in pop_In.subPopSizes(globalsSS.SP_SubPops.static_intSP_SubPop_Primary)]) + ' >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                    boolNewline=True
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                 
                    intNumVSPS = pop_In.numVirtualSubPop()
                    listVSPSizes = []
                    for intVSP in range(0, intNumVSPS):
                        intVSPSize = int(pop_In.subPopSize([globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVSP]))
                        listVSPSizes.append(intVSPSize)   

                    '''Message output '''
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    else:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> ' + 'VSP Sizes: ' + str(listVSPSizes) + ' >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                    boolNewline=False
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                    #
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    else:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #    
                    SSOutputOperation.methodOutput_SimGeneralMessageFooter(listOutputDestinations, 'Pre-Mating Stats')

                #DEBUG_ON
                #raw_input('\n AT MATING -Press return to close this window... \n')
                #DEBUG_OFF

                #pass
                return True
             
            
            def method_Determine_Number_Of_Offspring(self, static_intOffspringDistModel_IndividualSpecific):
                
                '''
                    Determine the number of offspring an individual pariturates
                    There are many different models for this:
                '''
                if static_intOffspringDistModel_IndividualSpecific == globalsSS.OffspringNumberDistributionModel_IndividualSpecific.static_OffspringNumberDistributionModel_IndividualSpecific_AGE_FIXED_NUMBER:
                    pass
                elif static_intOffspringDistModel_IndividualSpecific == globalsSS.OffspringNumberDistributionModel_IndividualSpecific.static_OffspringNumberDistributionModel_IndividualSpecific_AGE_RANDOM:
                    pass
                    return numpy__random.randint(self.objSSParametersLocal.intMinNumOffspring, self.objSSParametersLocal.intMaxNumOffspring)
                elif static_intOffspringDistModel_IndividualSpecific == globalsSS.OffspringNumberDistributionModel_IndividualSpecific.static_OffspringNumberDistributionModel_IndividualSpecific_AGE_RANDOM_WEIGHTED:
                    pass
                elif static_intOffspringDistModel_IndividualSpecific == globalsSS.OffspringNumberDistributionModel_IndividualSpecific.static_OffspringNumberDistributionModel_IndividualSpecific_AGE_FIXED_PROBABILITY:
                    pass
                
                return True
            

            '''
            -------------------------------------------------------------------------------------------------------
            # Mortality Scheme Processing
            --------------------------------------------------------------------------------------------------------
            '''
            def method_Predict_Mortality_For_Sex_For_Age_Cohort(self, int_Mortality_Type, bool_Use_Original_Rate_Dist, bool_Scale_Mortality_By_QUOTA, str_Sex, float_Age_In_Months, int_Age_Cohort_Size):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass 
            
                int_Mating_Mortality_Quota_Total = 0
                
                ''' Determine the type of mortaility to get the right survival dist '''
                if int_Mortality_Type == globalsSS.MortalitySource.static_intMortalityType_NATURAL:
                    str_Mortality_Type = globalsSS.MortalitySource.static_strMortalityType_NATURAL
                    if bool_Use_Original_Rate_Dist:
                        dict_Rates_Of_Survival = self.objSSParametersLocal.Arg_Survival_Natural[str_Sex]
                    else:
                        dict_Rates_Of_Survival = self.objSSParametersLocal.odictRates_Of_Survival_NATURAL_BySex_ByAge[str_Sex]
                    pass
                elif int_Mortality_Type == globalsSS.MortalitySource.static_intMortalityType_UnNATURAL:
                    str_Mortality_Type = globalsSS.MortalitySource.static_strMortalityType_UnNATURAL
                    if bool_Use_Original_Rate_Dist:
                        dict_Rates_Of_Survival = self.objSSParametersLocal.Arg_Survival_UnNatural[str_Sex]
                    else:
                        dict_Rates_Of_Survival = self.objSSParametersLocal.odictRates_Of_Survival_UnNATURAL_BySex_ByAge[str_Sex]
                    pass
                    if bool_Scale_Mortality_By_QUOTA:
                        ''' Get the size of the QUOTA of animals to kill '''
                        int_Mating_Mortality_Quota_Total = self.objSSParametersLocal.dict_Mortality_Application_Specs_By_Sex__UnNATURAL[globalsSS.MortalityApplication.static_str_Mortality_Scaling_Total__UnNat][str_Sex]
                    pass
                elif int_Mortality_Type == globalsSS.MortalitySource.static_intMortalityType_COMBINED:
                    str_Mortality_Type = globalsSS.MortalitySource.static_strMortalityType_COMBINED
                    dict_Rates_Of_Survival = self.objSSParametersLocal.odictRates_Of_Survival_COMBINED_BySex_ByAge[str_Sex]
                pass

                ''' Work out the MORTALITY RATE '''
                float_Age_Cohort_Survival_Rate = dict_Rates_Of_Survival[float_Age_In_Months]
                dec_Mortality_Rate_For_Age = Decimal(1-(float_Age_Cohort_Survival_Rate))
                                
                if bool_Scale_Mortality_By_QUOTA:
                    ''' Convert the rates into the original absolute numbers by the QUOTA total ''' 
                    int_Age_Cohort_Mortality_Count = int(round(dec_Mortality_Rate_For_Age*int_Mating_Mortality_Quota_Total))
                else:
                    ''' Work out the ABSOLUTE mortality '''    
                    int_Age_Cohort_Mortality_Count = int(round(dec_Mortality_Rate_For_Age*int_Age_Cohort_Size)) #Round out the decimal result to the nearest whole individual
                pass
                
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 

        
                return int_Age_Cohort_Mortality_Count
           
            def method_Create_UnNatural_Mortality_Rate_Dist__Deplete_Younger_Cohorts_Age_Cohorts_Are_Empty(self, odictIndividualCountPerAgeClass, str_Sex, odictAgeCohortAbsMortality_Scaled):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass                 
            
                '''
                ------------------
                Apply NATURAL mortality first
                ------------------
                '''
                int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_NATURAL
                odict_Age_Cohort_Indiv_Count__Post_NATURAL_Mortality = OrderedDict()
                for key_Age, value_Indiv_Count in odictIndividualCountPerAgeClass.items():
                    
                    ''' Reduce the max cohort number by the NATURAL mortality of that age cohort first '''
                    int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_NATURAL
                    intNumIndividualsToKillPerAgeClass_NATURAL = self.method_Predict_Mortality_For_Sex_For_Age_Cohort(int_Mortality_Type, False, False, str_Sex, key_Age, value_Indiv_Count)
                    int_New_Indiv_Count = value_Indiv_Count - intNumIndividualsToKillPerAgeClass_NATURAL
                    if int_New_Indiv_Count < 0:
                        int_New_Indiv_Count = 0
                    pass  
                
                    odict_Age_Cohort_Indiv_Count__Post_NATURAL_Mortality[key_Age] = int_New_Indiv_Count
                pass
            
            
                '''
                ------------------
                Apply UnNATURAL mortality
                
                Apply unnatural mortality to each age.  
                If the indiv count for an age goes to zero apply that mortality rate 
                to each younger cohort until full quota of mortality is used up.
                Work backwards through the age cohorts from old to young as the indiv count inceases with decreasing age
                ------------------
                '''
                int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_UnNATURAL
                
                ''' Sort the age cohorts backwards '''
                ''' Sort Age in DESCENDING order '''
                odict_Age_Cohort_Indiv_Count__Post_NATURAL_Mortality = OrderedDict(sorted(odict_Age_Cohort_Indiv_Count__Post_NATURAL_Mortality.items(), key=lambda x: x[0], reverse=True))

                ''' Creat a dict to have the killed indivs depleted from '''
                odict_Age_Cohort_Indiv_Count__Surviving = odict_Age_Cohort_Indiv_Count__Post_NATURAL_Mortality
                ''' Sort Age in DESCENDING order '''
                odict_Age_Cohort_Indiv_Count__Surviving = OrderedDict(sorted(odict_Age_Cohort_Indiv_Count__Surviving.items(), key=lambda x: x[0], reverse=True))
                
                odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota = OrderedDict()
                odict_Age_Cohort_Indiv_Count__Killed = OrderedDict()                    
#                 bool_Quota_Full = False
#                 while not bool_Quota_Full:


                dict_Rates_Of_Survival = self.objSSParametersLocal.Arg_Survival_UnNatural[str_Sex]
                    
                for key_Age, value_Indiv_Count in odict_Age_Cohort_Indiv_Count__Post_NATURAL_Mortality.items():
                    
                    #DEBUG_ON
                    #if key_Age == 396 and str_Sex == 'Male':
                    #    self.obj_Log_Debug_Display.debug('key_Age == 396')
                    #pass
                    #DEBUG_OFF
                    ''' Apply the UNatural mortality rate to calc under BAU and Scaled by the QUOTA how many indivs will be removed and how many will be left '''
                    bool_Use_Original_Rate_Dist = True
                    bool_Scale_Mortality_By_QUOTA = True
                    intNumIndividualsToKillPerAgeClass_UnNATURAL = self.method_Predict_Mortality_For_Sex_For_Age_Cohort(int_Mortality_Type, bool_Use_Original_Rate_Dist, bool_Scale_Mortality_By_QUOTA, str_Sex, key_Age, value_Indiv_Count)
                    ''' Record the BAU Scaled MOrtality for DEBUG '''
                    odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota[key_Age] = intNumIndividualsToKillPerAgeClass_UnNATURAL
                    ''' Determine how many REALLY survive after UnNatural moratlity '''
                    int_Indiv_Count__Surviving = odict_Age_Cohort_Indiv_Count__Surviving[key_Age]
                    int_Indivs_Left_Alive = int(round(int_Indiv_Count__Surviving*0.1))  
                    int_New_Indiv_Count = int_Indiv_Count__Surviving - intNumIndividualsToKillPerAgeClass_UnNATURAL
                    
                    ''' If too few in coohrt to sustain cull then look for the next youngest cohort that can sustain it '''
                    if int_New_Indiv_Count <= int_Indivs_Left_Alive:
                        ''' Scan until the next cohort that has enough indivs to deplete '''
                        bool_Indivs_Found = False
                        int_Indiv_Count__Leftover_To_Kill = 0
                        for key_Age_Next, value_Indiv_Count_Next in odict_Age_Cohort_Indiv_Count__Surviving.items():
                            if key_Age_Next <= key_Age:
                                int_Indivs_Left_Alive_Next = int(round(value_Indiv_Count*0.1))
                                #value_Indiv_Count_Next = value_Indiv_Count_Next - int_Indivs_Left_Alive 
                                if value_Indiv_Count_Next > int_Indivs_Left_Alive_Next:
                                    int_Indiv_Count__Putative_Surviving = value_Indiv_Count_Next - intNumIndividualsToKillPerAgeClass_UnNATURAL
                                    if int_Indiv_Count__Putative_Surviving > int_Indivs_Left_Alive_Next:
                                        ''' Age cohort with enough indivs has been found - remove them from that cohort '''
                                        bool_Indivs_Found = True
                                        int_Indiv_Count__Leftover_To_Kill = 0
                                        ''' Update the surviving totals '''
                                        odict_Age_Cohort_Indiv_Count__Surviving[key_Age_Next] = int_Indiv_Count__Putative_Surviving
                                        ''' Update the killed totals '''
                                        if key_Age_Next in odict_Age_Cohort_Indiv_Count__Killed:
                                            int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age_Next]
                                        else:
                                            int_Indiv_Count__Already_Killed = 0
                                        pass
                                        odict_Age_Cohort_Indiv_Count__Killed[key_Age_Next] = int_Indiv_Count__Already_Killed + intNumIndividualsToKillPerAgeClass_UnNATURAL
                                        
                                        if key_Age in odict_Age_Cohort_Indiv_Count__Killed:
                                            int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age]
                                        else:
                                            int_Indiv_Count__Already_Killed = 0
                                        pass
                                        odict_Age_Cohort_Indiv_Count__Killed[key_Age] = int_Indiv_Count__Already_Killed + 0                                            
                                        ''' no need to search the other age cohorts '''
                                        break
                                    elif int_Indiv_Count__Putative_Surviving < int_Indivs_Left_Alive_Next and value_Indiv_Count_Next >= int_Indivs_Left_Alive_Next:
                                        '''Age cohort with some indivs but not enough has been found - kill what we found but keep searching the younger cohorts to remove the rest '''
                                        #int_Indiv_Count__Putative_Surviving = value_Indiv_Count_Next - int_Indivs_Left_Alive_Next
                                        int_Indiv_Count__Killed = value_Indiv_Count_Next - int_Indivs_Left_Alive_Next
                                        int_Indiv_Count__Leftover_To_Kill = intNumIndividualsToKillPerAgeClass_UnNATURAL - int_Indiv_Count__Killed
                                        intNumIndividualsToKillPerAgeClass_UnNATURAL = int_Indiv_Count__Leftover_To_Kill
                                        ''' Update the surviving totals '''
                                        odict_Age_Cohort_Indiv_Count__Surviving[key_Age_Next] = int_Indivs_Left_Alive_Next #int_Indiv_Count__Putative_Surviving
                                        ''' Update the killed totals '''
                                        if key_Age_Next in odict_Age_Cohort_Indiv_Count__Killed:
                                            int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age_Next]
                                        else:
                                            int_Indiv_Count__Already_Killed = 0
                                        pass
                                        odict_Age_Cohort_Indiv_Count__Killed[key_Age_Next] = int_Indiv_Count__Already_Killed + int_Indiv_Count__Killed #value_Indiv_Count_Next
                                        ''' Keep searching the younger cohorst to get rid of the leftover kills '''
                                        pass
                                    pass
                                pass
                            else:
                                '''The key_Age & key_Age_Next are the same age and no indivs exist in cohort so continue search '''
                                pass
                            pass
                        pass
                        if bool_Indivs_Found == False or int_Indiv_Count__Leftover_To_Kill > 0:
                            with dcb_Debug_Location() as obj_DebugLoc:
                                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                            pass
                            str_Message = str_Message_Location + ' >> Not enough individuals in any age cohort to satisfy quota for Age: ' + str(key_Age) + ' Indivs to kill: ' + str(intNumIndividualsToKillPerAgeClass_UnNATURAL) + ' at a mortality rate of 1-Survival rate: ' + str(dict_Rates_Of_Survival[key_Age])
                            self.obj_Log_Default_Display.error(str_Message)
                            raise ValueError(str_Message)
                        pass
                    else:
                        ''' Enough indivs in age cohort - Kill indivs as per normal '''
                        odict_Age_Cohort_Indiv_Count__Surviving[key_Age] = int_New_Indiv_Count
                                                    
                        if key_Age in odict_Age_Cohort_Indiv_Count__Killed:
                            int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age]
                        else:
                            int_Indiv_Count__Already_Killed = 0
                        pass
                        odict_Age_Cohort_Indiv_Count__Killed[key_Age] = int_Indiv_Count__Already_Killed + intNumIndividualsToKillPerAgeClass_UnNATURAL
                    pass
                pass
                
                
#                 '''
#                 ----------------------------
#                 Convert surviving numbers into mortality
#                 ----------------------------
#                 '''
#                 
#                 for key_Age, value_Indiv_Count in odict_Age_Cohort_Indiv_Count__Surviving.items():
#                     odict_Age_Cohort_Indiv_Count__Killed[key_Age] = value_Indiv_Count
#                 pass

                ''' Sort Age in ascending order '''
                odict_Age_Cohort_Indiv_Count__Killed = OrderedDict(sorted(odict_Age_Cohort_Indiv_Count__Killed.items(), key=lambda x: x[0]))
                
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    pass
                pass
                #DEBUG_ON
                if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                    ''' ACTUAL Individuals per age cohort BEFORE NATURAL mortality'''
                    odict_Logging = odictIndividualCountPerAgeClass
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odictIndividualCountPerAgeClass: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 
                    
                    ''' ACTUAL Individuals per age cohort after NATURAL mortality'''
                    odict_Logging = odict_Age_Cohort_Indiv_Count__Post_NATURAL_Mortality
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Post_NATURAL_Mortality: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 

                    ''' Individuals Killed by BAU but Scaled by the Quota per age cohort '''
                    odict_Logging = odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 
                    
                    ''' ACTUAL Individuals SURVIVING per age cohort '''
                    odict_Logging = odict_Age_Cohort_Indiv_Count__Surviving
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Surviving: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 
                                        
                    ''' UNNATURAL deaths per age cohort '''
                    odict_Logging = odict_Age_Cohort_Indiv_Count__Killed
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Killed: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 
                    
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()                 
                pass                   
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
                        
                return odict_Age_Cohort_Indiv_Count__Killed, odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota, odict_Age_Cohort_Indiv_Count__Post_NATURAL_Mortality




            def method_Create_UnNatural_Mortality_Rate_Dist__Deplete_Younger_Cohorts_Age_Cohorts_Are_Empty_EMPTY_COHORT(self, odictIndividualCountPerAgeClass, str_Sex, odictAgeCohortAbsMortality_Scaled):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass                 
            
                '''
                ------------------
                Apply NATURAL mortality first
                ------------------
                '''
                int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_NATURAL
                
                for key_Age, value_Indiv_Count in odictIndividualCountPerAgeClass.items():
                    
                    ''' Reduce the max cohort number by the NATURAL mortality of that age cohort first '''
                    int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_NATURAL
                    intNumIndividualsToKillPerAgeClass_NATURAL = self.method_Predict_Mortality_For_Sex_For_Age_Cohort(int_Mortality_Type, False, False, str_Sex, key_Age, value_Indiv_Count)
                    int_New_Indiv_Count = value_Indiv_Count - intNumIndividualsToKillPerAgeClass_NATURAL
                    if int_New_Indiv_Count < 0:
                        int_New_Indiv_Count = 0
                    pass  
                
                    odictIndividualCountPerAgeClass[key_Age] = int_New_Indiv_Count
                pass
            
            
                '''
                ------------------
                Apply UnNATURAL mortality
                
                Apply unnatural mortality to each age.  
                If the indiv count for an age goes to zero apply that mortality rate 
                to each younger cohort until full quota of mortality is used up.
                Work backwards through the age cohorts from old to young as the indiv count inceases with decreasing age
                ------------------
                '''
                int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_UnNATURAL
                
                ''' Sort the age cohorts backwards '''
                odict_Age_Cohort_Indiv_Count = odictIndividualCountPerAgeClass
                ''' Sort Age in DESCENDING order '''
                odict_Age_Cohort_Indiv_Count = OrderedDict(sorted(odict_Age_Cohort_Indiv_Count.items(), key=lambda x: x[0], reverse=True))

                ''' Creat a dict to have the killed indivs depleted from '''
                odict_Age_Cohort_Indiv_Count__Surviving = odictIndividualCountPerAgeClass
                ''' Sort Age in DESCENDING order '''
                odict_Age_Cohort_Indiv_Count__Surviving = OrderedDict(sorted(odict_Age_Cohort_Indiv_Count__Surviving.items(), key=lambda x: x[0], reverse=True))
                
                odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota = OrderedDict()
                odict_Age_Cohort_Indiv_Count__Killed = OrderedDict()                    
#                 bool_Quota_Full = False
#                 while not bool_Quota_Full:


                dict_Rates_Of_Survival = self.objSSParametersLocal.Arg_Survival_UnNatural[str_Sex]
                    
                for key_Age, value_Indiv_Count in odict_Age_Cohort_Indiv_Count.items():
                    
                    ''' Check if the survival rate is 1 and if so ignore '''
                    #float_Survival_Rate_Orig = dict_Rates_Of_Survival[key_Age]
                    #if float_Survival_Rate_Orig != 1:
                        
                    ''' Apply the UNatural mortality rate to calc under BAU and Scaled by the QUOTA how many indivs will be removed and how many will be left '''
                    bool_Use_Original_Rate_Dist = True
                    bool_Scale_Mortality_By_QUOTA = True
                    intNumIndividualsToKillPerAgeClass_UnNATURAL = self.method_Predict_Mortality_For_Sex_For_Age_Cohort(int_Mortality_Type, bool_Use_Original_Rate_Dist, bool_Scale_Mortality_By_QUOTA, str_Sex, key_Age, value_Indiv_Count)
                    ''' Record the BAU Scaled MOrtality for DEBUG '''
                    odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota[key_Age] = intNumIndividualsToKillPerAgeClass_UnNATURAL
                    ''' Determine how many REALLY survive after UnNatural moratlity '''
                    int_Indiv_Count__Surviving = odict_Age_Cohort_Indiv_Count__Surviving[key_Age] 
                    int_New_Indiv_Count = int_Indiv_Count__Surviving - intNumIndividualsToKillPerAgeClass_UnNATURAL
                    
                    ''' If too few in coohrt to sustain cull then look for the next youngest cohort that can sustain it '''
                    if int_New_Indiv_Count < 0:
                        ''' Scan until the next cohort that has enough indivs to deplete '''
                        bool_Indivs_Found = False
                        int_Indiv_Count__Leftover_To_Kill = 0
                        for key_Age_Next, value_Indiv_Count_Next in odict_Age_Cohort_Indiv_Count__Surviving.items():
                            if key_Age_Next <= key_Age:
                                if value_Indiv_Count_Next > 0:
                                    int_Indiv_Count__Putative_Surviving = value_Indiv_Count_Next - intNumIndividualsToKillPerAgeClass_UnNATURAL
                                    if int_Indiv_Count__Putative_Surviving >= 0:
                                        ''' Age cohort with enough indivs has been found - remove them from that cohort '''
                                        bool_Indivs_Found = True
                                        int_Indiv_Count__Leftover_To_Kill = 0
                                        ''' Update the surviving totals '''
                                        odict_Age_Cohort_Indiv_Count__Surviving[key_Age_Next] = int_Indiv_Count__Putative_Surviving
                                        ''' Update the killed totals '''
                                        if key_Age_Next in odict_Age_Cohort_Indiv_Count__Killed:
                                            int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age_Next]
                                        else:
                                            int_Indiv_Count__Already_Killed = 0
                                        pass
                                        odict_Age_Cohort_Indiv_Count__Killed[key_Age_Next] = int_Indiv_Count__Already_Killed + intNumIndividualsToKillPerAgeClass_UnNATURAL
                                        
                                        if key_Age in odict_Age_Cohort_Indiv_Count__Killed:
                                            int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age]
                                        else:
                                            int_Indiv_Count__Already_Killed = 0
                                        pass
                                        odict_Age_Cohort_Indiv_Count__Killed[key_Age] = int_Indiv_Count__Already_Killed + 0                                            
                                        ''' no need to search the other age cohorts '''
                                        break
                                    elif int_Indiv_Count__Putative_Surviving < 0 and value_Indiv_Count_Next > 0:
                                        '''Age cohort with some indivs but not enough has been found - kill what we found but keep searching the younger cohorts to remove the rest '''
                                        #int_Indiv_Count__Putative_Surviving = 0
                                        int_Indiv_Count__Leftover_To_Kill = intNumIndividualsToKillPerAgeClass_UnNATURAL - value_Indiv_Count_Next
                                        intNumIndividualsToKillPerAgeClass_UnNATURAL = int_Indiv_Count__Leftover_To_Kill
                                        ''' Update the surviving totals '''
                                        odict_Age_Cohort_Indiv_Count__Surviving[key_Age_Next] = 0 #int_Indiv_Count__Putative_Surviving
                                        ''' Update the killed totals '''
                                        if key_Age_Next in odict_Age_Cohort_Indiv_Count__Killed:
                                            int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age_Next]
                                        else:
                                            int_Indiv_Count__Already_Killed = 0
                                        pass
                                        odict_Age_Cohort_Indiv_Count__Killed[key_Age_Next] = int_Indiv_Count__Already_Killed + value_Indiv_Count_Next
                                        ''' Keep searching the younger cohorst to get rid of the leftover kills '''
                                        pass
                                    pass
                                pass
                            else:
                                '''The key_Age & key_Age_Next are the same age and no indivs exist in cohort so continue search '''
                                pass
                            pass
                        pass
                        if bool_Indivs_Found == False or int_Indiv_Count__Leftover_To_Kill > 0:
                            with dcb_Debug_Location() as obj_DebugLoc:
                                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                            pass
                            float_Survival_Rate_Orig = 0.0
                            str_Message = str_Message_Location + ' >> Not enough individuals in any age cohort to satisfy quota for Age: ' + str(key_Age) + ' Indivs to kill: ' + str(intNumIndividualsToKillPerAgeClass_UnNATURAL) + ' at a mortality rate of 1-Survival rate: ' + str(float_Survival_Rate_Orig)
                            self.obj_Log_Default_Display.error(str_Message)
                            raise ValueError(str_Message)
                        pass
                    else:
                        ''' Enough indivs in age cohort - Kill indivs as per normal '''
#                             if key_Age in odict_Age_Cohort_Indiv_Count__Surviving:
#                                 int_Indiv_Count__Already_Surviving = odict_Age_Cohort_Indiv_Count__Surviving[key_Age]
#                             else:
#                                 int_Indiv_Count__Already_Surviving = 0
#                             pass
#                             odict_Age_Cohort_Indiv_Count__Surviving[key_Age] = int_Indiv_Count__Already_Surviving + int_New_Indiv_Count

                        odict_Age_Cohort_Indiv_Count__Surviving[key_Age] = int_New_Indiv_Count
                                                    
                        if key_Age in odict_Age_Cohort_Indiv_Count__Killed:
                            int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age]
                        else:
                            int_Indiv_Count__Already_Killed = 0
                        pass
                        #odict_Age_Cohort_Indiv_Count__Killed[key_Age] = int_Indiv_Count__Already_Killed + (int_New_Indiv_Count - intNumIndividualsToKillPerAgeClass_UnNATURAL)
                        odict_Age_Cohort_Indiv_Count__Killed[key_Age] = int_Indiv_Count__Already_Killed + intNumIndividualsToKillPerAgeClass_UnNATURAL
                    pass
#                     else:
#                         if key_Age in odict_Age_Cohort_Indiv_Count__Killed:
#                             int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age]
#                         else:
#                             int_Indiv_Count__Already_Killed = 0
#                         pass
#                         odict_Age_Cohort_Indiv_Count__Killed[key_Age] = int_Indiv_Count__Already_Killed + 0
#                     pass
                pass
                
                
#                 '''
#                 ----------------------------
#                 Convert surviving numbers into mortality
#                 ----------------------------
#                 '''
#                 
#                 for key_Age, value_Indiv_Count in odict_Age_Cohort_Indiv_Count__Surviving.items():
#                     odict_Age_Cohort_Indiv_Count__Killed[key_Age] = value_Indiv_Count
#                 pass

                ''' Sort Age in ascending order '''
                odict_Age_Cohort_Indiv_Count__Killed = OrderedDict(sorted(odict_Age_Cohort_Indiv_Count__Killed.items(), key=lambda x: x[0]))
                
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    pass
                pass
                #DEBUG_ON
                if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                    ''' ACTUAL Individuals per age cohort '''
                    odict_Logging = odictIndividualCountPerAgeClass
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odictIndividualCountPerAgeClass: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 

                    ''' Individuals Killed by BAU but Scaled by the Quota per age cohort '''
                    odict_Logging = odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 
                    
                    ''' ACTUAL Individuals SURVIVING per age cohort '''
                    odict_Logging = odict_Age_Cohort_Indiv_Count__Surviving
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Surviving: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 
                                        
                    ''' UNNATURAL deaths per age cohort '''
                    odict_Logging = odict_Age_Cohort_Indiv_Count__Killed
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Killed: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 
                    
                    with globalsSS.Pause_Console() as obj_Pause:
                        obj_Pause.method_Pause_Console()                 
                pass                   
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
                        
                return odict_Age_Cohort_Indiv_Count__Killed


            
            def method_Create_UnNatural_Mortality_Rate_Dist__Deplete_Younger_Cohorts_Age_Cohorts_Are_Empty_ORIG(self, odictIndividualCountPerAgeClass, str_Sex, odictAgeCohortAbsMortality_Scaled):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass                 
            
                '''
                ------------------
                Apply NATURAL mortality first
                ------------------
                '''
                int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_NATURAL
                
                for key_Age, value_Indiv_Count in odictIndividualCountPerAgeClass.items():
                    
                    ''' Reduce the max cohort number by the NATURAL mortality of that age cohort first '''
                    int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_NATURAL
                    intNumIndividualsToKillPerAgeClass_NATURAL = self.method_Predict_Mortality_For_Sex_For_Age_Cohort(int_Mortality_Type, False, False, str_Sex, key_Age, value_Indiv_Count)
                    int_New_Indiv_Count = value_Indiv_Count - intNumIndividualsToKillPerAgeClass_NATURAL
                    if int_New_Indiv_Count < 0:
                        int_New_Indiv_Count = 0
                    pass  
                
                    odictIndividualCountPerAgeClass[key_Age] = int_New_Indiv_Count
                pass
            
            
                '''
                ------------------
                Apply UnNATURAL mortality
                
                Apply unnatural mortality to each age.  
                If the indiv count for an age goes to zero apply that mortality rate 
                to each younger cohort until full quota of mortality is used up.
                Work backwards through the age cohorts from old to young as the indiv count inceases with decreasing age
                ------------------
                '''
                int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_UnNATURAL
                
                ''' Sort the age cohorts backwards '''
                odict_Age_Cohort_Indiv_Count = odictIndividualCountPerAgeClass
                ''' Sort Age in DESCENDING order '''
                odict_Age_Cohort_Indiv_Count = OrderedDict(sorted(odict_Age_Cohort_Indiv_Count.items(), key=lambda x: x[0], reverse=True))

                ''' Creat a dict to have the killed indivs depleted from '''
                odict_Age_Cohort_Indiv_Count__Surviving = odictIndividualCountPerAgeClass
                ''' Sort Age in DESCENDING order '''
                odict_Age_Cohort_Indiv_Count__Surviving = OrderedDict(sorted(odict_Age_Cohort_Indiv_Count__Surviving.items(), key=lambda x: x[0], reverse=True))
                
                odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota = OrderedDict()
                odict_Age_Cohort_Indiv_Count__Killed = OrderedDict()                    
#                 bool_Quota_Full = False
#                 while not bool_Quota_Full:


                dict_Rates_Of_Survival = self.objSSParametersLocal.Arg_Survival_UnNatural[str_Sex]
                    
                for key_Age, value_Indiv_Count in odict_Age_Cohort_Indiv_Count__Surviving.items():
                    
                    ''' Check if the survival rate is 1 and if so ignore '''
                    float_Survival_Rate_Orig = dict_Rates_Of_Survival[key_Age]
                    if float_Survival_Rate_Orig != 1:
                        
                        ''' Apply the UNatural mortality rate to calc under BAU and Scaled by the QUOTA how many indivs will be removed and how many will be left '''
                        bool_Use_Original_Rate_Dist = True
                        bool_Scale_Mortality_By_QUOTA = True
                        intNumIndividualsToKillPerAgeClass_UnNATURAL = self.method_Predict_Mortality_For_Sex_For_Age_Cohort(int_Mortality_Type, bool_Use_Original_Rate_Dist, bool_Scale_Mortality_By_QUOTA, str_Sex, key_Age, value_Indiv_Count)
                        ''' Record the BAU Scaled MOrtality for DEBUG '''
                        odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota[key_Age] = intNumIndividualsToKillPerAgeClass_UnNATURAL
                        ''' Determine how many REALLY survive after UnNatural moratlity ''' 
                        int_New_Indiv_Count = value_Indiv_Count - intNumIndividualsToKillPerAgeClass_UnNATURAL
                        
                        ''' If too few in coohrt to sustain cull then look for the next youngest cohort that can sustain it '''
                        if int_New_Indiv_Count < 0:
                            ''' Scan until the next cohort that has enough indivs to deplete '''
                            bool_Indivs_Found = False
                            int_Indiv_Count__Leftover_To_Kill = 0
                            for key_Age_Next, value_Indiv_Count_Next in odict_Age_Cohort_Indiv_Count__Surviving.items():
                                if key_Age_Next < key_Age:
                                    if value_Indiv_Count_Next > 0:
                                        int_Indiv_Count__Putative_Surviving = value_Indiv_Count_Next - intNumIndividualsToKillPerAgeClass_UnNATURAL
                                        if int_Indiv_Count__Putative_Surviving >= 0:
                                            ''' Age cohort with enough indivs has been found - remove them from that cohort '''
                                            bool_Indivs_Found = True
                                            int_Indiv_Count__Leftover_To_Kill = 0
                                            ''' Update the surviving totals '''
                                            odict_Age_Cohort_Indiv_Count__Surviving[key_Age_Next] = int_Indiv_Count__Putative_Surviving
                                            ''' Update the killed totals '''
                                            if key_Age_Next in odict_Age_Cohort_Indiv_Count__Killed:
                                                int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age_Next]
                                            else:
                                                int_Indiv_Count__Already_Killed = 0
                                            pass
                                            odict_Age_Cohort_Indiv_Count__Killed[key_Age_Next] = int_Indiv_Count__Already_Killed + intNumIndividualsToKillPerAgeClass_UnNATURAL
                                            
                                            if key_Age in odict_Age_Cohort_Indiv_Count__Killed:
                                                int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age]
                                            else:
                                                int_Indiv_Count__Already_Killed = 0
                                            pass
                                            odict_Age_Cohort_Indiv_Count__Killed[key_Age] = int_Indiv_Count__Already_Killed + 0                                            
                                            ''' no need to search the other age cohorts '''
                                            break
                                        elif int_Indiv_Count__Putative_Surviving < 0 and value_Indiv_Count_Next > 0:
                                            '''Age cohort with some indivs but not enough has been found - kill what we found but keep searching the younger cohorts to remove the rest '''
                                            int_Indiv_Count__Putative_Surviving = 0
                                            int_Indiv_Count__Leftover_To_Kill = intNumIndividualsToKillPerAgeClass_UnNATURAL - value_Indiv_Count_Next
                                            intNumIndividualsToKillPerAgeClass_UnNATURAL = int_Indiv_Count__Leftover_To_Kill
                                            ''' Update the surviving totals '''
                                            odict_Age_Cohort_Indiv_Count__Surviving[key_Age_Next] = int_Indiv_Count__Putative_Surviving
                                            ''' Update the killed totals '''
                                            if key_Age_Next in odict_Age_Cohort_Indiv_Count__Killed:
                                                int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age_Next]
                                            else:
                                                int_Indiv_Count__Already_Killed = 0
                                            pass
                                            odict_Age_Cohort_Indiv_Count__Killed[key_Age_Next] = int_Indiv_Count__Already_Killed + value_Indiv_Count_Next
                                            ''' Keep searching the younger cohorst to get rid of the leftover kills '''
                                            pass
                                        pass
                                    pass
                                pass
                            pass
                            if bool_Indivs_Found == False or int_Indiv_Count__Leftover_To_Kill > 0:
                                with dcb_Debug_Location() as obj_DebugLoc:
                                    str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                                pass
                                str_Message = str_Message_Location + ' >> Not enough individuals in any age cohort to satisfy quota for Age: ' + str(key_Age) + ' Indivs to kill: ' + str(intNumIndividualsToKillPerAgeClass_UnNATURAL) + ' at a mortality rate of 1-Survival rate: ' + str(float_Survival_Rate_Orig)
                                self.obj_Log_Default_Display.error(str_Message)
                                raise ValueError(str_Message)
                            pass
                        else:
                            ''' Enough indivs in age cohort - Kill indivs as per normal '''
#                             if key_Age in odict_Age_Cohort_Indiv_Count__Surviving:
#                                 int_Indiv_Count__Already_Surviving = odict_Age_Cohort_Indiv_Count__Surviving[key_Age]
#                             else:
#                                 int_Indiv_Count__Already_Surviving = 0
#                             pass
#                             odict_Age_Cohort_Indiv_Count__Surviving[key_Age] = int_Indiv_Count__Already_Surviving + int_New_Indiv_Count

                            odict_Age_Cohort_Indiv_Count__Surviving[key_Age] = int_New_Indiv_Count
                                                        
                            if key_Age in odict_Age_Cohort_Indiv_Count__Killed:
                                int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age]
                            else:
                                int_Indiv_Count__Already_Killed = 0
                            pass
                            odict_Age_Cohort_Indiv_Count__Killed[key_Age] = int_Indiv_Count__Already_Killed + (int_New_Indiv_Count - intNumIndividualsToKillPerAgeClass_UnNATURAL)
                        pass
                    else:
                        if key_Age in odict_Age_Cohort_Indiv_Count__Killed:
                            int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age]
                        else:
                            int_Indiv_Count__Already_Killed = 0
                        pass
                        odict_Age_Cohort_Indiv_Count__Killed[key_Age] = int_Indiv_Count__Already_Killed + 0
                    pass
                pass
                
                
#                 '''
#                 ----------------------------
#                 Convert surviving numbers into mortality
#                 ----------------------------
#                 '''
#                 
#                 for key_Age, value_Indiv_Count in odict_Age_Cohort_Indiv_Count__Surviving.items():
#                     odict_Age_Cohort_Indiv_Count__Killed[key_Age] = value_Indiv_Count
#                 pass

                ''' Sort Age in ascending order '''
                odict_Age_Cohort_Indiv_Count__Killed = OrderedDict(sorted(odict_Age_Cohort_Indiv_Count__Killed.items(), key=lambda x: x[0]))
                
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    pass
                pass
                #DEBUG_ON
                if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                    ''' ACTUAL Individuals per age cohort '''
                    odict_Logging = odictIndividualCountPerAgeClass
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odictIndividualCountPerAgeClass: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 

                    ''' Individuals Killed by BAU but Scaled by the Quota per age cohort '''
                    odict_Logging = odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 
                    
                    ''' ACTUAL Individuals SURVIVING per age cohort '''
                    odict_Logging = odict_Age_Cohort_Indiv_Count__Surviving
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Surviving: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 
                                        
                    ''' UNNATURAL deaths per age cohort '''
                    odict_Logging = odict_Age_Cohort_Indiv_Count__Killed
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Killed: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 
                    
                    with globalsSS.Pause_Console() as obj_Pause:
                        obj_Pause.method_Pause_Console()                 
                pass                   
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
                        
                return odict_Age_Cohort_Indiv_Count__Killed

            def method_Create_UnNatural_Mortality_Rate_Dist__Deplete_Younger_Cohorts_Age_Cohorts_Are_Empty_ORIG_1(self, odictIndividualCountPerAgeClass, str_Sex, odictAgeCohortAbsMortality_Scaled):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass                 
            
                '''
                ------------------
                Apply NATURAL mortality first
                ------------------
                '''
                int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_NATURAL
                
                for key_Age, value_Indiv_Count in odictIndividualCountPerAgeClass.items():
                    
                    ''' Reduce the max cohort number by the NATURAL mortality of that age cohort first '''
                    int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_NATURAL
                    intNumIndividualsToKillPerAgeClass_NATURAL = self.method_Predict_Mortality_For_Sex_For_Age_Cohort(int_Mortality_Type, False, False, str_Sex, key_Age, value_Indiv_Count)
                    int_New_Indiv_Count = value_Indiv_Count - intNumIndividualsToKillPerAgeClass_NATURAL
                    if int_New_Indiv_Count < 0:
                        int_New_Indiv_Count = 0
                    pass  
                
                    odictIndividualCountPerAgeClass[key_Age] = int_New_Indiv_Count
                pass
            
            
                '''
                ------------------
                Apply UnNATURAL mortality
                
                Apply unnatural mortality to each age.  
                If the indiv count for an age goes to zero apply that mortality rate 
                to each younger cohort until full quota of mortality is used up.
                Work backwards through the age cohorts from old to young as the indiv count inceases with decreasing age
                ------------------
                '''
                int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_UnNATURAL
                
                ''' Sort the age cohorts backwards '''
                odict_Age_Cohort_Indiv_Count = odictIndividualCountPerAgeClass
                ''' Sort Age in DESCENDING order '''
                odict_Age_Cohort_Indiv_Count = OrderedDict(sorted(odict_Age_Cohort_Indiv_Count.items(), key=lambda x: x[0], reverse=True))

                ''' Creat a dict to have the killed indivs depleted from '''
                odict_Age_Cohort_Indiv_Count__Surviving = odictIndividualCountPerAgeClass
                ''' Sort Age in DESCENDING order '''
                odict_Age_Cohort_Indiv_Count__Surviving = OrderedDict(sorted(odict_Age_Cohort_Indiv_Count__Surviving.items(), key=lambda x: x[0], reverse=True))
                
                odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota = OrderedDict()
                odict_Age_Cohort_Indiv_Count__Killed = OrderedDict()                    
#                 bool_Quota_Full = False
#                 while not bool_Quota_Full:


                dict_Rates_Of_Survival = self.objSSParametersLocal.Arg_Survival_Natural[str_Sex]
                    
                for key_Age, value_Indiv_Count in odict_Age_Cohort_Indiv_Count__Surviving.items():
                    
                    ''' Check if the survival rate is 1 and if so ignore '''
                    float_Survival_Rate_Orig = dict_Rates_Of_Survival[key_Age]
                    if float_Survival_Rate_Orig != 1:
                        
                        ''' Apply the UNatural mortality rate to calc under BAU and Scaled by the QUOTA how many indivs will be removed and how many will be left '''
                        bool_Use_Original_Rate_Dist = True
                        bool_Scale_Mortality_By_QUOTA = True
                        intNumIndividualsToKillPerAgeClass_UnNATURAL = self.method_Predict_Mortality_For_Sex_For_Age_Cohort(int_Mortality_Type, bool_Use_Original_Rate_Dist, bool_Scale_Mortality_By_QUOTA, str_Sex, key_Age, value_Indiv_Count)
                        ''' Record the BAU Scaled MOrtality for DEBUG '''
                        odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota[key_Age] = intNumIndividualsToKillPerAgeClass_UnNATURAL
                        ''' Determine how many REALLY survive after UnNatural moratlity ''' 
                        int_New_Indiv_Count = value_Indiv_Count - intNumIndividualsToKillPerAgeClass_UnNATURAL
                        
                        ''' If too few in coohrt to sustain cull then look for the next youngest cohort that can sustain it '''
                        if int_New_Indiv_Count < 0:
                            ''' Scan until the next cohort that has enough indivs to deplete '''
                            bool_Indivs_Found = False
                            for key_Age_Next, value_Indiv_Count_Next in odict_Age_Cohort_Indiv_Count__Surviving.items():
                                if key_Age_Next < key_Age:
                                    #int_Indiv_Count__Putative_Surviving = value_Indiv_Count_Next - intNumIndividualsToKillPerAgeClass_UnNATURAL
                                    #if int_Indiv_Count__Putative_Surviving >= 0:
                                    if value_Indiv_Count_Next > 0:
                                        ''' Age cohort with indivs has been found - remove that as many as possible from that cohort '''
                                        int_Indiv_Count__Putative_Surviving = value_Indiv_Count_Next - intNumIndividualsToKillPerAgeClass_UnNATURAL
                                        if int_Indiv_Count__Putative_Surviving >= 0:

                                            bool_Indivs_Found = True
                                            ''' Update the surviving totals '''
                                            odict_Age_Cohort_Indiv_Count__Surviving[key_Age_Next] = int_Indiv_Count__Putative_Surviving
                                            ''' Update the killed totals '''
                                            if key_Age_Next in odict_Age_Cohort_Indiv_Count__Killed:
                                                int_Indiv_Count__Already_Killed = odict_Age_Cohort_Indiv_Count__Killed[key_Age_Next]
                                            else:
                                                int_Indiv_Count__Already_Killed = 0
                                            pass
                                            odict_Age_Cohort_Indiv_Count__Killed[key_Age_Next] = int_Indiv_Count__Already_Killed + intNumIndividualsToKillPerAgeClass_UnNATURAL
                                            ''' no need to search the other age cohorts '''
                                            break
                                        else:
                                            '''Check the next age cohort for enough indivs to kill '''
                                            pass
                                        pass
                                    pass
                                pass
                            pass
                            if bool_Indivs_Found == False:
                                with dcb_Debug_Location() as obj_DebugLoc:
                                    str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                                pass
                                str_Message = str_Message_Location + ' >> Not enough individuals in any age cohort to satisfy quota for Age: ' + str(key_Age) + ' Indivs to kill: ' + str(intNumIndividualsToKillPerAgeClass_UnNATURAL) + ' at a mortality rate of 1-Survival rate: ' + str(float_Survival_Rate_Orig)
                                self.obj_Log_Default_Display.error(str_Message)
                                raise ValueError(str_Message)
                            pass
                        else:
                            ''' Enough indivs in age cohort - Kill indivs as per normal '''
                            odict_Age_Cohort_Indiv_Count__Surviving[key_Age] = int_New_Indiv_Count
                            odict_Age_Cohort_Indiv_Count__Killed[key_Age] = intNumIndividualsToKillPerAgeClass_UnNATURAL
                        pass
                    else:
                        odict_Age_Cohort_Indiv_Count__Killed[key_Age] = 0
                    pass
                pass
                
                
#                 '''
#                 ----------------------------
#                 Convert surviving numbers into mortality
#                 ----------------------------
#                 '''
#                 
#                 for key_Age, value_Indiv_Count in odict_Age_Cohort_Indiv_Count__Surviving.items():
#                     odict_Age_Cohort_Indiv_Count__Killed[key_Age] = value_Indiv_Count
#                 pass

                ''' Sort Age in ascending order '''
                odict_Age_Cohort_Indiv_Count__Killed = OrderedDict(sorted(odict_Age_Cohort_Indiv_Count__Killed.items(), key=lambda x: x[0]))
                
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    pass
                pass
                #DEBUG_ON
                if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                    ''' ACTUAL Individuals per age cohort '''
                    odict_Logging = odictIndividualCountPerAgeClass
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odictIndividualCountPerAgeClass: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 

                    ''' Individuals Killed by BAU but Scaled by the Quota per age cohort '''
                    odict_Logging = odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Killed_BAU_Scaled_By_Quota: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 
                    
                    ''' ACTUAL Individuals SURVIVING per age cohort '''
                    odict_Logging = odict_Age_Cohort_Indiv_Count__Surviving
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Surviving: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 
                                        
                    ''' UNNATURAL deaths per age cohort '''
                    odict_Logging = odict_Age_Cohort_Indiv_Count__Killed
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Killed: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 
                    
                    with globalsSS.Pause_Console() as obj_Pause:
                        obj_Pause.method_Pause_Console()                 
                pass                   
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
                        
                return odict_Age_Cohort_Indiv_Count__Killed



            def method_UnNatural_Mortality__Get_Absolute_Number_Age_Cohort_Mortality_Distribution_For_Rate(self, str_Sex, odictIndividualCountPerAgeClass):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
                           
                odictAgeCohortAbsMortality_Orig = OrderedDict()
                
                ''' Get the size of the QUOTA of animals to kill '''
                int_Mating_Mortality_Quota_Total__UnNat = self.objSSParametersLocal.dict_Mortality_Application_Specs_By_Sex__UnNATURAL[globalsSS.MortalityApplication.static_str_Mortality_Scaling_Total__UnNat][str_Sex]
                
                ''' Get the ORIG unchanged survival rates '''
                dictAgeCohortSampleRates_Orig = OrderedDict(sorted( self.objSSParametersLocal.Arg_Survival_UnNatural[str_Sex].items()))
                    
                ''' Convert the rates into the original absolute numbers by the QUOTA total ''' 
                for key_int_Age, value_float_Survival_Rate in dictAgeCohortSampleRates_Orig.iteritems():
                   
                    int_Abs_Mortality_Orig = int(round((float(1-value_float_Survival_Rate)*int_Mating_Mortality_Quota_Total__UnNat),0))
                    odictAgeCohortAbsMortality_Orig[key_int_Age] = int_Abs_Mortality_Orig
                
                pass

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
                            
                return odictAgeCohortAbsMortality_Orig


            def method_Mortality__Create_Survival_Rate_Age_Cohort_Distribution(self, odictIndividualCountPerAgeClass, str_Sex, odictAgeCohortAbsMortality_Scaled):
            
                '''
                -------------------------
                Create survival rates based on the absolute mortality ditribution and the REAL Age Coort indivs count
                -------------------------
                '''
                odictAgeCohortSurvivalRate = OrderedDict()
                
                for key_Age, value_int_Abs_Mortality in odictAgeCohortAbsMortality_Scaled.items():
                    
#                     if key_Age == (self.objSSParametersLocal.maxAge *12):
#                         int_Age_Cohort_Size = 0
#                         float_Mortality_Rate_Scaled = float(0)
#                     else:
                    if key_Age in odictIndividualCountPerAgeClass:
                        
                        ''' Check if the survival rate is 0 (NATURAL Mort kills them all first and so UnNATURAL survival is set to 1) and if so ignore '''
                        if self.objSSParametersLocal.odictRates_Of_Survival_NATURAL_BySex_ByAge[str_Sex][key_Age] == 0:
                            float_Mortality_Rate_Scaled = float(0)
                        else:
                            int_Age_Cohort_Size = odictIndividualCountPerAgeClass[key_Age]
                            ''' Reduce the max cohort number by the NATURAL mortality of that age cohort first '''
                            int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_NATURAL
                            intNumIndividualsToKillPerAgeClass_NATURAL = self.method_Predict_Mortality_For_Sex_For_Age_Cohort(int_Mortality_Type, False, False, str_Sex, key_Age, int_Age_Cohort_Size)
                            int_Age_Cohort_Size = int_Age_Cohort_Size - intNumIndividualsToKillPerAgeClass_NATURAL 
                
                            if value_int_Abs_Mortality > int_Age_Cohort_Size:
                                float_Mortality_Rate_Scaled = float(1)
                            else:
                                if int_Age_Cohort_Size > 0:
                                    float_Mortality_Rate_Scaled = float(value_int_Abs_Mortality) / float(int_Age_Cohort_Size)
                                else:
                                    float_Mortality_Rate_Scaled = float(0)
                                pass
                            pass
#                         else:
#                             float_Mortality_Rate_Scaled = float(0)
                        pass
                    pass
                    
                    float_Survival_Rate_Scaled = 1-float_Mortality_Rate_Scaled
                    odictAgeCohortSurvivalRate[key_Age] = float_Survival_Rate_Scaled
                    pass
                pass
            
                return odictAgeCohortSurvivalRate


            def method_Mortality_By_Mortality_Rate_Scaled_By_Age_Cohort_Size(self, str_Sex, odictIndividualCountPerAgeClass):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
                           
                #Sampling by ABSOLUTE NUMBER SCALED BY MAXIMUM ABSOLUTE per Age Cohort VSP
                odictAgeCohortAbsMortality_Orig = OrderedDict()
                odictAgeCohortAbsMortality_Scaled = OrderedDict()
                odictAgeCohortSurvivalRate_Scaled = OrderedDict()
                
                ''' 
                ------------------------------
                Get the ABSOLUTE NUMBERS of indivs to kill based on the ORIG unchange survival rate distribution and the QUOTA total
                ------------------------------
                '''
                odictAgeCohortAbsMortality_Orig = self.method_UnNatural_Mortality__Get_Absolute_Number_Age_Cohort_Mortality_Distribution_For_Rate(str_Sex, odictIndividualCountPerAgeClass)
                
                
                '''
                ------------------------------
                Get a SCALED ABSOLUTE NUMBERS of indivs to kill using the MAX MORTALITY AGE COHORT, the SIZE OF THAT COHORT in reallity, and the proportion of that REAL COHORT to moderate the scaling factor
                ------------------------------
                '''
                '''get Max Absolute Number from ABSOLUTE NUMBER OF DEATHS dist'''
                int_Age_Cohort_With_Max_ABS_Mortality_Key =  max(odictAgeCohortAbsMortality_Orig.keys(), key=(lambda key: odictAgeCohortAbsMortality_Orig[key])) 
                int_Max_Sample_Size_Value =  odictAgeCohortAbsMortality_Orig[int_Age_Cohort_With_Max_ABS_Mortality_Key] 
                '''get the REAL AGE COHORT size for Max Absolute Number'''
                
                int_VSP_ID_Adjustment = 0 #2  #Adjust the VSP number to match the current ages in the pop
                int_Age_Cohort_With_Max_Mortality_NEW_Key = int_Age_Cohort_With_Max_ABS_Mortality_Key + int_VSP_ID_Adjustment
                
                ''' first, factor in deaths from NATURAL mortality '''
                if int_Age_Cohort_With_Max_Mortality_NEW_Key in odictIndividualCountPerAgeClass:                   
                    int_Age_Cohort_With_MAX_Mortality_REAL_Indiv_Count =  odictIndividualCountPerAgeClass[int_Age_Cohort_With_Max_Mortality_NEW_Key]
                    ''' Reduce the max cohort number by the NATURAL mortality of that age cohort first '''
                    int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_NATURAL
                    intNumIndividualsToKillPerAgeClass_NATURAL = self.method_Predict_Mortality_For_Sex_For_Age_Cohort(int_Mortality_Type, False, False, str_Sex, int_Age_Cohort_With_Max_Mortality_NEW_Key, int_Age_Cohort_With_MAX_Mortality_REAL_Indiv_Count)
                    int_Age_Cohort_With_MAX_Mortality_REAL_Indiv_Count_Minus_Nat_Deaths = int_Age_Cohort_With_MAX_Mortality_REAL_Indiv_Count - intNumIndividualsToKillPerAgeClass_NATURAL 
                else:
                    int_Age_Cohort_With_MAX_Mortality_REAL_Indiv_Count_Minus_Nat_Deaths =  0
                pass
 
                '''
                ------------------------------
                Get a SCALED ABSOLUTE MORTALITY Age distribution of indivs that survive after UnNatural mortality
                ------------------------------
                ''' 
                bool_Use_Business_As_Usual_Abs_Mortality = False
                if bool_Use_Business_As_Usual_Abs_Mortality:
                    odictAgeCohortAbsMortality_Scaled = odictAgeCohortAbsMortality_Orig

                bool_Use_SCALED_Business_As_Usual_Abs_Mortality = False
                if bool_Use_SCALED_Business_As_Usual_Abs_Mortality:
                    '''Get max percentage'''
                    float_Max_Proportion = 1 #dictSamplingParams[globalsSS.Sampling_SamplingParameters.static_SampleSizeIsAbsScaledByMaxAbsPerVSPCohort_MaxProportion]
                    '''Convert sample numbers to percentages using the Max absolute vaulue as 100% or whatever the float_Max_Percentage is'''
                    for key, value in odictAgeCohortAbsMortality_Orig.items():
                        int_Age_Cohort_SCALED_ABS_Mortality_Indiv_Count = int(int_Age_Cohort_With_MAX_Mortality_REAL_Indiv_Count_Minus_Nat_Deaths*((float(value)*float_Max_Proportion) / float(int_Max_Sample_Size_Value)))
                        odictAgeCohortAbsMortality_Scaled[key] = int_Age_Cohort_SCALED_ABS_Mortality_Indiv_Count
                    pass
                    
                    ''' Get a SCALED RATE Age distribution of indivs that survive after UnNatural mortality'''
                    ''' Now create survival rates based on the scaled absolute mortality '''
                    odictAgeCohortSurvivalRate_Scaled = self.method_Mortality__Create_Survival_Rate_Age_Cohort_Distribution(odictIndividualCountPerAgeClass, str_Sex, odictAgeCohortAbsMortality_Scaled)
                pass
                odict_Age_Cohort_Indiv_Count__Killed_BAU = odictAgeCohortAbsMortality_Scaled
                
                '''
                ------------------------------
                Get a QUOTA FULLFILLED Age distribution of indivs that survive after UnNatural mortality
                ------------------------------
                '''             
                bool_Fullfill_Quota = True
                if bool_Fullfill_Quota:
#                     '''First , assign the new UnNat Survival Rate distribution to the PARAMETER OBJECT'''
#                     for key_int_Age, value_float_Survival_Rate_Scaled in odictAgeCohortSurvivalRate_Scaled.items():
#                         self.objSSParametersLocal.odictRates_Of_Survival_UnNATURAL_BySex_ByAge[str_Sex][key_int_Age] = value_float_Survival_Rate_Scaled
#                     pass
                
                    ''' Then, create new QUOTA FULLFILLED survival ABS MORTALITY dist '''                    
                    odictAgeCohortAbsMortality_Scaled_Quota_Fullfilled, odict_Age_Cohort_Indiv_Count__Killed_BAU, odictIndividualCountPerAgeClass_After_Nat_Mort = self.method_Create_UnNatural_Mortality_Rate_Dist__Deplete_Younger_Cohorts_Age_Cohorts_Are_Empty(odictIndividualCountPerAgeClass, str_Sex, odictAgeCohortAbsMortality_Scaled)
                
                    ''' Now create survival rates based on the scaled absolute mortality '''
                    odictAgeCohortSurvivalRate_Scaled = self.method_Mortality__Create_Survival_Rate_Age_Cohort_Distribution(odictIndividualCountPerAgeClass, str_Sex, odictAgeCohortAbsMortality_Scaled_Quota_Fullfilled)
                pass  
            
                '''
                -----------------------
                Assign the new UnNat Survival Rate distribution to the PARAMETER OBJECT
                -----------------------
                '''
                for key_int_Age, value_float_Survival_Rate_Scaled in odictAgeCohortSurvivalRate_Scaled.items():
                    self.objSSParametersLocal.odictRates_Of_Survival_UnNATURAL_BySex_ByAge[str_Sex][key_int_Age] = value_float_Survival_Rate_Scaled
                pass            
            
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    pass
                pass
                #DEBUG_ON
                if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                    ''' ACTUAL Individuals per age cohort '''
                    odict_Logging = odictIndividualCountPerAgeClass
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odictIndividualCountPerAgeClass: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 

                    if bool_Fullfill_Quota:
                        ''' ACTUAL Individuals per age cohort after NATURAL mortality'''
                        odict_Logging = odictIndividualCountPerAgeClass_After_Nat_Mort
                        odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                        str_Message = '>>> Survival Stat: odictIndividualCountPerAgeClass_After_Nat_Mort: '
                        self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                        str_Message += ':::Age;Num\t'
                        for int_Age, value in odict_Logging.items():
                            str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                        pass 
                        self.obj_Log_Debug_AgeNe.debug(str_Message) 
                    pass
                
                    ''' Individuals Killed by BAU (but may beScaled by the Quota) per age cohort '''
                    odict_Logging = odict_Age_Cohort_Indiv_Count__Killed_BAU
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Killed_BAU: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 

                    if bool_Fullfill_Quota:
                        ''' UNNATURAL deaths per age cohort '''
                        odict_Logging = odictAgeCohortAbsMortality_Scaled_Quota_Fullfilled
                        odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                        str_Message = '>>> Survival Stat: odict_Age_Cohort_Indiv_Count__Killed: '
                        self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                        str_Message += ':::Age;Num\t'
                        for int_Age, value in odict_Logging.items():
                            str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                        pass 
                        self.obj_Log_Debug_AgeNe.debug(str_Message) 
                    pass
                
                    ''' Rates of UnNatural Survival By Age Cohort '''
                    odict_Logging = self.objSSParametersLocal.odictRates_Of_Survival_UnNATURAL_BySex_ByAge[str_Sex]
                    odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                    str_Message = '>>> Survival Stat: odictRates_Of_Survival_UnNATURAL_BySex_ByAge: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message) 

                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()                 
                pass   
                     
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass                 
                
                return True    
                

                                  
            def method_Mortality_By_Mortality_Rate_Scaled_By_Age_Cohort_Size_OLD(self, str_Sex, odictIndividualCountPerAgeClass):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
                           
                #Sampling by ABSOLUTE NUMBER SCALED BY MAXIMUM ABSOLUTE per Age Cohort VSP
                odictAgeCohortAbsMortality_Orig = OrderedDict()
                odictAgeCohortAbsMortality_Scaled = OrderedDict()
                odictAgeCohortSurvivalRate_Scaled = OrderedDict()
                
                int_Mating_Mortality_Scaling_Total__UnNat = self.objSSParametersLocal.dict_Mortality_Application_Specs_By_Sex__UnNATURAL[globalsSS.MortalityApplication.static_str_Mortality_Scaling_Total__UnNat][str_Sex]
                ''' Get the ORIG unchanged survival rates '''
                dictAgeCohortSampleRates_Orig = OrderedDict(sorted( self.objSSParametersLocal.Arg_Survival_UnNatural[str_Sex].items()))
                    
                ''' Convert the rates into the original absolute numbers by the scaling total ''' 
                for key_int_Age, value_float_Survival_Rate in dictAgeCohortSampleRates_Orig.iteritems():
                   
                    int_Abs_Mortality_Orig = int(round((float(1-value_float_Survival_Rate)*int_Mating_Mortality_Scaling_Total__UnNat),0))
                    odictAgeCohortAbsMortality_Orig[key_int_Age] = int_Abs_Mortality_Orig
                
                pass
                
                '''get Max Absolute Number from dist'''
                int_Max_Sample_Size_Key =  max(odictAgeCohortAbsMortality_Orig.keys(), key=(lambda key: odictAgeCohortAbsMortality_Orig[key])) 
                int_Max_Sample_Size_Value =  odictAgeCohortAbsMortality_Orig[int_Max_Sample_Size_Key] 
                '''get VSP size for Max Absolute Number'''
                #Adjust the VSP number to match the current ages in the pop
                intVSP_ID_Adjustment = 0 #2
                int_New_Key = int_Max_Sample_Size_Key+intVSP_ID_Adjustment     
                if int_New_Key in odictIndividualCountPerAgeClass:                   
                    int_VSP_Size_Value =  odictIndividualCountPerAgeClass[int_New_Key]
                    ''' Reduce the max cohort number by the NATURAL mortality of that age cohort first '''
                    int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_NATURAL
                    intNumIndividualsToKillPerAgeClass_NATURAL = self.method_Predict_Mortality_For_Sex_For_Age_Cohort(self, int_Mortality_Type, False, False, str_Sex, int_New_Key, int_VSP_Size_Value)
                    int_VSP_Size_Value = int_VSP_Size_Value - intNumIndividualsToKillPerAgeClass_NATURAL 
                
                else:
                    int_VSP_Size_Value =  0
                pass
            
                float_Max_Proportion = 0
                bool_Use_Business_As_Usual_Abs_Mortality = True
                if bool_Use_Business_As_Usual_Abs_Mortality:
                    odictAgeCohortAbsMortality_Scaled = odictAgeCohortAbsMortality_Orig
                else:
                    '''Get max percentage'''
                    float_Max_Proportion = 1 #dictSamplingParams[globalsSS.Sampling_SamplingParameters.static_SampleSizeIsAbsScaledByMaxAbsPerVSPCohort_MaxProportion]
                    '''Convert sample numbers to percentages using the Max absolute vaulue as 100% or whatever the float_Max_Percentage is'''
                    for key, value in odictAgeCohortAbsMortality_Orig.items():
                        int_New_Sample_Size = int(int_VSP_Size_Value*((float(value)*float_Max_Proportion) / float(int_Max_Sample_Size_Value)))
                        odictAgeCohortAbsMortality_Scaled[key] = int_New_Sample_Size
                    pass
                pass
            
                ''' Now create survival rates based on the scaled absolute mortality '''
                for key_int_Age, value_int_Scaled_Abs_Mortality in odictAgeCohortAbsMortality_Scaled.items():
                    if key_int_Age == (self.objSSParametersLocal.maxAge *12):
                        int_Age_Cohort_Size = 0
                        float_Mortality_Rate_Scaled = float(0)
                    else:
                        if key_int_Age in odictIndividualCountPerAgeClass:
                            int_Age_Cohort_Size = odictIndividualCountPerAgeClass[key_int_Age]
                            ''' Reduce the max cohort number by the NATURAL mortality of that age cohort first '''
                            int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_NATURAL
                            intNumIndividualsToKillPerAgeClass_NATURAL = self.method_Predict_Mortality_For_Sex_For_Age_Cohort(self, int_Mortality_Type, False, False, str_Sex, key_int_Age, int_Age_Cohort_Size)
                            int_Age_Cohort_Size = int_Age_Cohort_Size - intNumIndividualsToKillPerAgeClass_NATURAL 

                            if value_int_Scaled_Abs_Mortality > int_Age_Cohort_Size:
                                float_Mortality_Rate_Scaled = float(1)
                            else:
                                if int_Age_Cohort_Size > 0:
                                    float_Mortality_Rate_Scaled = float(value_int_Scaled_Abs_Mortality) / float(int_Age_Cohort_Size)
                                else:
                                    float_Mortality_Rate_Scaled = float(0)
                                pass
                            pass
                        else:
                            float_Mortality_Rate_Scaled = float(0)
                        pass
                    pass
                    #float_Mortality_Rate_Scaled = float(int_Age_Cohort_Size - value_int_Scaled_Abs_Mortality) / float(int_Age_Cohort_Size)
                    
                    float_Survival_Rate_Scaled = 1-float_Mortality_Rate_Scaled
                    odictAgeCohortSurvivalRate_Scaled[key_int_Age] = float_Survival_Rate_Scaled
                    pass
                pass
                
                ''' Assign the new UnNat Survival Rate distribution to the paramaters '''
                for key_int_Age, value_float_Survival_Rate_Scaled in odictAgeCohortSurvivalRate_Scaled.items():
                    self.objSSParametersLocal.odictRates_Of_Survival_UnNATURAL_BySex_ByAge[str_Sex][key_int_Age] = value_float_Survival_Rate_Scaled
                pass

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    pass
                pass
                #DEBUG_ON
                if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:

                    str_Message = '>>> Survival Stat: SCALED odictAgeCohortAbsMortality_Orig: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odictAgeCohortAbsMortality_Orig).values()),2)))
                    str_Message += 'Age;Num\t'
                    for int_Age, value in odictAgeCohortAbsMortality_Orig.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message)

                    str_Message = '>>> Survival Stat: SCALED odictAgeCohortAbsMortality_Scaled: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(odictAgeCohortAbsMortality_Scaled).values()),2)))
                    str_Message += 'Age;Num\t'
                    for int_Age, value in odictAgeCohortAbsMortality_Scaled.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message)                    
                    
                    self.obj_Log_Debug_AgeNe.debug('>>> Survival Stat: SCALED float_Max_Proportion: ' + str(float_Max_Proportion))

                    self.obj_Log_Debug_AgeNe.debug('>>> Survival Stat: SCALED odictRates_Of_Survival_UnNATURAL_BySex_ByAge')
                    for str_Sex, value in self.objSSParametersLocal.odictRates_Of_Survival_UnNATURAL_BySex_ByAge.items():
                        self.obj_Log_Debug_AgeNe.debug('Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(value).values()),2)) + ' ; Values: ' + str(value)) 
                    pass 
                pass   
                     
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass                 
                
                return True    
                

                
            def method_Mortality_Parameter_Assignment(self, str_Sex):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass

                '''
                ~~~~~~~~~~~~~~~~~~~
                MATING MORTALITY STARTS
                Does mating start at this mating event?
                Construct the Survivorship Age Distribution to reflect the outcome
                ~~~~~~~~~~~~~~~~~~~
                '''
                bool_Mortality_Starts_Nat = False
                bool_Mortality_Starts_UnNat = False
                
                ''' Compare the current replicate mating with the one that will start a type of mortality '''
                int_Current_Replicate_Mating_Count = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                int_Mating_Mortality_Starts__Nat = self.objSSParametersLocal.dict_Mortality_Application_Specs_By_Sex__NATURAL[globalsSS.MortalityApplication.static_str_Mating_Mortlity_Starts__Nat][str_Sex]
                int_Mating_Mortality_Starts__UnNat = self.objSSParametersLocal.dict_Mortality_Application_Specs_By_Sex__UnNATURAL[globalsSS.MortalityApplication.static_str_Mating_Mortlity_Starts__UnNat][str_Sex]

                if self.objSSParametersLocal.boolAllowNATURALMortality:
                    if int_Current_Replicate_Mating_Count >= int_Mating_Mortality_Starts__Nat:
                        bool_Mortality_Starts_Nat = True
                    pass
                pass
                if self.objSSParametersLocal.boolAllowUnNATURALMortality:
                    if int_Current_Replicate_Mating_Count >= int_Mating_Mortality_Starts__UnNat:
                        bool_Mortality_Starts_UnNat = True
                    pass
                pass
            
                '''
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                COMBINED Mortality - Used for performing mortality
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                '''
                
                dict_Survival_COMBINED = OrderedDict()

#                 ''' Provide some default values if Natrual mortality os turned off '''
#                 if self.boolAllowNATURALMortality == False:
#                     for intAgeInMonths in self.objSSParametersLocal.dictProbabilityDistribution_P_SurvivalNATURALBySexByAge[str_Sex].keys():
#                         if str_Sex in self.odictRates_Of_Survival_NATURAL_BySex_ByAge:
#                             dict_Survival_COMBINED[str_Sex].update(OrderedDict([(intAgeInMonths, 1)]))    #1 = All survive
#                         else:
#                             dict_Survival_COMBINED[str_Sex] = OrderedDict([(intAgeInMonths, 1)])    #1 = All survive
#                         pass
#                     pass
#                 pass
            
                if bool_Mortality_Starts_Nat:
                    ''' Take the NATURAL Survivorship rates and insert them into the COMBINED rate dict '''
                    for key_str_Sex, value_Dict in self.objSSParametersLocal.odictRates_Of_Survival_NATURAL_BySex_ByAge.items():
                        dict_Survival_COMBINED[key_str_Sex] = OrderedDict([(key,valuelist) for key,valuelist in value_Dict.iteritems()])
                    pass
                else:
                    ''' Provide some default values if Natrual mortality os turned off '''
                    for intAgeInMonths in self.objSSParametersLocal.dictProbabilityDistribution_P_SurvivalNATURALBySexByAge[str_Sex].keys():
                        if str_Sex in dict_Survival_COMBINED:
                            dict_Survival_COMBINED[str_Sex].update(OrderedDict([(intAgeInMonths, 1)]))    #1 = All survive
                        else:
                            dict_Survival_COMBINED[str_Sex] = OrderedDict([(intAgeInMonths, 1)])    #1 = All survive
                        pass
                    pass
                pass
            
                if bool_Mortality_Starts_UnNat:
                    ''' Make the COMBINED survivorship rate a product of the NATURAL (already in the COMBINED dict) and UNNATURAL survivorship rates '''
                    for strSex, dictValues in self.objSSParametersLocal.odictRates_Of_Survival_UnNATURAL_BySex_ByAge.items():
                        for intAgeInMonths, float_UnNatural_Survival in dictValues.iteritems():

                            if intAgeInMonths in dict_Survival_COMBINED[strSex]:
                                float_Natural_Survival = dict_Survival_COMBINED[strSex][intAgeInMonths]
                                float_Overall_Survival_sx = float_Natural_Survival* float_UnNatural_Survival
                                dictNewValues = {intAgeInMonths:float_Overall_Survival_sx}
                                dict_Survival_COMBINED[strSex].update(dictNewValues)
                            else:
                                self.obj_Log_Default_Display.error('Ages in month in UnNatural Survival: ' + intAgeInMonths + '; missing from odictRates_Of_Survival_COMBINED_BySex_ByAge')
                                self.obj_Log_Default_Display.error('>>> Survival Stat: odictRates_Of_Survival_COMBINED_BySex_ByAge')
                                for str_Sex, value in dict_Survival_COMBINED.items():
                                    self.obj_Log_Default_Display.error('Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(value).values()),2)) + ' ; Values: ' + str(value)) 
                                pass    
                                self.obj_Log_Default_Display.error('>>> Survival Stat: odictRates_Of_Survival_NATURAL_BySex_ByAge')
                                for str_Sex, value in self.odictRates_Of_Survival_NATURAL_BySex_ByAge.items():
                                    self.obj_Log_Default_Display.error('Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(value).values()),2)) + ' ; Values: ' + str(value)) 
                                pass    
                                self.obj_Log_Default_Display.error('>>> Survival Stat: odictRates_Of_Survival_UnNATURAL_BySex_ByAge')
                                for str_Sex, value in self.odictRates_Of_Survival_UnNATURAL_BySex_ByAge.items():
                                    self.obj_Log_Default_Display.error('Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(value).values()),2)) + ' ; Values: ' + str(value)) 
                                pass 
                            pass   
                        pass
                    pass
                pass

                ''' Finally - Assign the COMBINED dict to the Parameter object '''
                if str_Sex in self.objSSParametersLocal.odictRates_Of_Survival_COMBINED_BySex_ByAge:
                    self.objSSParametersLocal.odictRates_Of_Survival_COMBINED_BySex_ByAge[str_Sex].update(dict_Survival_COMBINED[str_Sex])
                else:
                    self.objSSParametersLocal.odictRates_Of_Survival_COMBINED_BySex_ByAge[str_Sex] = dict_Survival_COMBINED[str_Sex]
                pass
            
                #DEBUG_ON
                if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:

                    self.obj_Log_Debug_AgeNe.debug('>>> Survival Stat: odictRates_Of_Survival_NATURAL_BySex_ByAge')
                    for str_Sex, value in self.objSSParametersLocal.odictRates_Of_Survival_NATURAL_BySex_ByAge.iteritems():
                        self.obj_Log_Debug_AgeNe.debug('Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(value).values()),2)) + ' ; Values: ' + str(value)) 
                    pass    
                    self.obj_Log_Debug_AgeNe.debug('>>> Survival Stat: odictRates_Of_Survival_UnNATURAL_BySex_ByAge')
                    for str_Sex, value in self.objSSParametersLocal.odictRates_Of_Survival_UnNATURAL_BySex_ByAge.iteritems():
                        self.obj_Log_Debug_AgeNe.debug('Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(value).values()),2)) + ' ; Values: ' + str(value)) 
                    pass 
                    self.obj_Log_Debug_AgeNe.debug('>>> Survival Stat: odictRates_Of_Survival_COMBINED_BySex_ByAge')
                    for str_Sex, value in self.objSSParametersLocal.odictRates_Of_Survival_COMBINED_BySex_ByAge.iteritems():
                        self.obj_Log_Debug_AgeNe.debug('Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(value).values()),2)) + ' ; Values: ' + str(value)) 
                    pass
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message='', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
                #DEBUG_OFF
                           
                return True

                       
            '''@profile'''
            def method_SpecifyMortalityScheme(self, pop_In, intMortalityType, strSex, boolRemoveIndividuals):
                
#                 '''
#                 ~~~~~~~~~~~~~~~~~~~
#                 MATING MORTALITY STARTS
#                 Does mating start at this mating event?
#                 Construct the Survivorship Age Distribution to reflect the outcome
#                 ~~~~~~~~~~~~~~~~~~~
#                 '''
#                 
#                 self.method_Mortality_Parameter_Assignment(strSex)
                    
                '''
                ~~~~~~~~~~~~~~~~~~~
                MORTALITY APPLICATION MODEL
                Determine the number of idivids to die and by extension how many survive
                There are many different models for this:  Except I've only implemented one
                ~~~~~~~~~~~~~~~~~~~
                '''
                dictProbabilityDistribution_P_SurvivalForSexByAge = OrderedDict()

                ''' NOTE: Hardcoded to COMBINED mortality only to improve performace '''
                intMortalityNumberDistributionModel_IndividualSpecificForSex = globalsSS.MortalityNumberDistributionModel_IndividualSpecific.static_MortalityNumberDistributionModel_IndividualSpecific_AGE_FIXED_PROBABILITY
                strMortalityNumberDistributionModel_IndividualSpecificForSex = globalsSS.MortalitySource.static_strMortalityType_COMBINED

#                 '''
#                 ~~~~~~~~~~~~~~~~~~~
#                 Get the COMBINED survivorship distribution for this upcoming mating event (mortality ony occurs just before mating)
#                 These rates determine the number of DEATHS and then survivors is the remaiing indivs
#                 ~~~~~~~~~~~~~~~~~~~
#                 '''
#                 dictProbabilityDistribution_P_SurvivalForSexByAge.update(self.objSSParametersLocal.odictRates_Of_Survival_COMBINED_BySex_ByAge[strSex])

                '''
                ~~~~~~~~~~~~~~~~~~~
                Select the Mortality Model to be applied
                ~~~~~~~~~~~~~~~~~~~
                '''
                '''Message output '''
                with SSOutputHandler() as SSOutputOperation:
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        #listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    else:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    stringMessage = 'Remove Indivs(' + str(boolRemoveIndividuals) + ') of Sex ' + strSex + ' by ' + strMortalityNumberDistributionModel_IndividualSpecificForSex + ' Mortality'
                    SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, stringMessage)
                    #
                    #stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> ' + 'Remove Indivs(' + str(boolRemoveIndividuals) + ') of Sex ' + strSex + ' by ' + strMortalityNumberDistributionModel_IndividualSpecificForSex + ' Mortality - START   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                    #boolNewline=True
                    #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                
                '''Processing'''    
                #Apply the mortality model you want to apply
                if intMortalityNumberDistributionModel_IndividualSpecificForSex == globalsSS.MortalityNumberDistributionModel_IndividualSpecific.static_MortalityNumberDistributionModel_IndividualSpecific_AGE_FIXED_NUMBER:
                    #AGE_FIXED_NUMBER
                    pass
                elif intMortalityNumberDistributionModel_IndividualSpecificForSex == globalsSS.MortalityNumberDistributionModel_IndividualSpecific.static_MortalityNumberDistributionModel_IndividualSpecific_AGE_RANDOM:
                    #AGE_RANDOM
                    return numpy__random.randint(self.objSSParametersLocal.intMinNumMortality, self.objSSParametersLocal.intMaxNumMortality)
                elif intMortalityNumberDistributionModel_IndividualSpecificForSex == globalsSS.MortalityNumberDistributionModel_IndividualSpecific.static_MortalityNumberDistributionModel_IndividualSpecific_AGE_RANDOM_WEIGHTED:
                    #AGE_RANDOM_WEIGHTED
                    pass
                
                elif intMortalityNumberDistributionModel_IndividualSpecificForSex == globalsSS.MortalityNumberDistributionModel_IndividualSpecific.static_MortalityNumberDistributionModel_IndividualSpecific_AGE_FIXED_PROBABILITY:
                    #AGE_FIXED_PROBABILITY

                    ''' Apply mortality to a specified sex '''
                    pop_In = self.method_Mortality_Applied_To_A_Sex_Given_AGE_FIXED_RATE_Mortality_Scheme(pop_In, intMortalityType, dictProbabilityDistribution_P_SurvivalForSexByAge, strSex, boolRemoveIndividuals)

                    pass
                
                '''Message output '''
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                else:
                    if boolRemoveIndividuals:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    else:
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                #
                #stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> ' + 'Remove Indivs(' + str(boolRemoveIndividuals) + ') of Sex ' + strSex + ' by ' + strMortalityNumberDistributionModel_IndividualSpecificForSex + ' Mortality - END   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                #boolNewline=True
                #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                #
                stringMessage = 'Remove Indivs(' + str(boolRemoveIndividuals) + ') of Sex ' + strSex + ' by ' + strMortalityNumberDistributionModel_IndividualSpecificForSex + ' Mortality'
                SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, stringMessage, boolIsHeader=False, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
                
                pop_Out = pop_In
                
                return pop_Out
            
            '''@profile'''
            def method_Mortality_Applied_To_A_Sex_Given_AGE_FIXED_RATE_Mortality_Scheme(self, pop_In, intMortalityType, dictProbabilityDistribution_P_SurvivalForSexByAge, strSex, boolRemoveIndividuals):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass         
                                
                if strSex == globalsSS.SexConstants.static_stringSexMale:
                    static_simupop_Sex = globalsSS.SexConstants.static_simupop_Sex_MALE
                    static_strSex = globalsSS.SexConstants.static_stringSexMale
                elif strSex == globalsSS.SexConstants.static_stringSexFemale: 
                    static_simupop_Sex = globalsSS.SexConstants.static_simupop_Sex_FEMALE
                    static_strSex = globalsSS.SexConstants.static_stringSexFemale
                
                ''' Get a dict of indive IDs and ages for a specific sex '''
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    #DEBUG_ON
                    #odictCountIndividualsWithInfoField = objSSAnalysisOperation.method_Count_Individuals_By_InfoField(pop_In, 'age_in_months')
                    #print(str(odictCountIndividualsWithInfoField))
                    #DEBUG_OFF
                    tupVSP = 0
                    listSimupopInfoFieldsToReturn = ['ind_id', 'age_in_months'] 
                    #odictIndividualsOfSpecificSex_NEW = objSSAnalysisOperation.method_Get_InfoFields_For_Pop_By_Sex_New(pop_In, tupVSP, static_strSex, listSimupopInfoFieldsToReturn) 
                    #DEBUG_ON
                    int_Current_Replicate_Mating_Count = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                    if int_Current_Replicate_Mating_Count == 74:
                        self.obj_Log_Debug_Display.debug('int_Current_Replicate_Mating_Count == 74')
                    pass
                    #DEBUG_OF
                    
                    #boolReportVSPIfEmpty = False
                    #listExpectedKeyValues = []
                    boolReportVSPIfEmpty = True
                    listExpectedKeyValues = [x*12 for x in range(1,self.objSSParametersLocal.maxAge)]
                    odictIndividualsOfSpecificSex_NEW = objSSAnalysisOperation.method_Get_InfoFields_For_Pop_By_Sex_New(pop_In, tupVSP, static_strSex, listSimupopInfoFieldsToReturn, boolReportVSPIfEmpty, listExpectedKeyValues) 

                '''Messaging'''
                with SSOutputHandler() as objSSOutputOperation:
                    if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                        #listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        #listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_PopulationOffspringTotalsByParent
                    else:
                        if boolRemoveIndividuals:
                            #listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                            listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                            #listOutputDestinations = ['console'] + self.objSSParametersLocal.listOutputDestinations_PopulationOffspringTotalsByParent
                        else:
                            #listOutputDestinations = ['console'] + self.objSSParametersLocal.listOutputDestinations_PopulationOffspringTotalsByParent
                            listOutputDestinations = []
            
                    #
                    objSSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, '')
                pass

                '''Count the individuals in each age class '''
                odictIndividualCountPerAgeClass = OrderedDict([(int(key), len(list)) for key, list in odictIndividualsOfSpecificSex_NEW.items()])
                
                ''' Check if UnNatural Mortality has started '''
                bool_Start_UnNatural_Mortality = False
                if self.objSSParametersLocal.boolAllowUnNATURALMortality:
                    bool_Start_UnNatural_Mortality = False
                    int_Current_Replicate_Mating_Count = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                    int_Mating_Mortality_Starts__UnNat = self.objSSParametersLocal.dict_Mortality_Application_Specs_By_Sex__UnNATURAL[globalsSS.MortalityApplication.static_str_Mating_Mortlity_Starts__UnNat][strSex]
                    if int_Current_Replicate_Mating_Count >= int_Mating_Mortality_Starts__UnNat:
                        bool_Start_UnNatural_Mortality = True
                    pass
                    ''' Get Scaled UnNatural Survival Numbers for a sex'''
                    if bool_Start_UnNatural_Mortality:    
                        int_Mortality_Scaled_Total = self.objSSParametersLocal.dict_Mortality_Application_Specs_By_Sex__UnNATURAL[globalsSS.MortalityApplication.static_str_Mortality_Scaling_Total__UnNat][strSex]
                        
                        if int_Mortality_Scaled_Total > 1:
                            #odictIndividualCountPerAgeClass_Copy  = OrderedDict([(int(key), len(list)) for key, list in odictIndividualsOfSpecificSex_NEW.items()])
                            self.method_Mortality_By_Mortality_Rate_Scaled_By_Age_Cohort_Size(strSex, odictIndividualCountPerAgeClass)
                        pass
                    pass
                pass
            
                ''' Get COMBINED Survival rate for a sex '''
                '''
                ~~~~~~~~~~~~~~~~~~~
                MATING MORTALITY STARTS
                Does mating start at this mating event?
                Construct the Survivorship Age Distribution to reflect the outcome
                ~~~~~~~~~~~~~~~~~~~
                '''
                
                self.method_Mortality_Parameter_Assignment(strSex)            
                '''
                ~~~~~~~~~~~~~~~~~~~
                Get the COMBINED survivorship distribution for this upcoming mating event (mortality ony occurs just before mating)
                These rates determine the number of DEATHS and then survivors is the remaiing indivs
                ~~~~~~~~~~~~~~~~~~~
                '''
                dictProbabilityDistribution_P_SurvivalForSexByAge.update(self.objSSParametersLocal.odictRates_Of_Survival_COMBINED_BySex_ByAge[strSex])
                
                
                
                                                                   
                '''Processing'''  
                #DEBUG_ON
#                 stringMessage = '> ' + strSex + ' ' + ' dictProbabilityDistribution_P_SurvivalForSexByAge = ' + str(dictProbabilityDistribution_P_SurvivalForSexByAge) +'\n'
#                 boolNewline=True
#                 objSSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                #DEBUG_OFF
                
                #Convert Survival rate into Mortality rate
                dictProbabilityDistribution_P_MortalityByAge = OrderedDict()
                for key, value in dictProbabilityDistribution_P_SurvivalForSexByAge.items():
                    dictProbabilityDistribution_P_MortalityByAge[key] = Decimal(float(1)- float(value))

                #DEBUG_ON
#                 stringMessage = '> ' + strSex + ' ' + ' dictProbabilityDistribution_P_MortalityByAge = ' + str(dictProbabilityDistribution_P_MortalityByAge) +'\n'
#                 boolNewline=True
#                 objSSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                #DEBUG_OFF
            
                                     
                #odictIndividualCountPerAgeClass = OrderedDict()
                ''' Process for each age class in the probability distribution '''

                #DEBUG_ON
#                 int_Current_Replicate_Mating_Count = self.objSSParametersLocal.int_MatingCount_Replicate_Total
#                 if int_Current_Replicate_Mating_Count == 75:
#                     self.obj_Log_Debug_Display.debug('int_Current_Replicate_Mating_Count == 75')
#                 pass
                #DEBUG_OF                
  

                '''
                ~~~~~~~~~~~~~~~~~~~~~~~~~~
                Mortality
                Work out how many individuals to kill based on the mortality rate for that age class
                and how many individuals are in it
                
                Rounding - To round to the nearest DEAD individual, this uses "Round Half up" decimal classroom rounding I.e 1.5 = 2.
                However, SURVIVORS are calculated as ALIVE - DEAD to ensure that PREV ALIVE = DEAD + SURVIVORS
                Therefore, this model is conservative as mortality will be slightly skewed to deaths rather than survivors 
                ~~~~~~~~~~~~~~~~~~~~~~~~~~
                '''
                odictNumIndividualsToKillPerAgeClass = OrderedDict()
                odictNumIndividualsToKillPerAgeClass_NATURAL = OrderedDict()
                odictNumIndividualsToKillPerAgeClass_UnNATURAL = OrderedDict()
                odictNumIndividualsSurvivingPerAgeClass_NATURAL = OrderedDict()
                odictNumIndividualsSurvivingPerAgeClass_UnNATURAL = OrderedDict()
                
                for keyAgeInMonths, valueIndivsInAgeClass in odictIndividualCountPerAgeClass.items():
                    
                    bool_OverMaxAge = False
                    if keyAgeInMonths > (self.objSSParametersLocal.maxAge * 12):
                        decRateofMortalityForAge = Decimal(1)
                        bool_OverMaxAge = True
                    else:
                        decRateofMortalityForAge = Decimal(dictProbabilityDistribution_P_MortalityByAge[keyAgeInMonths])
                    pass
                
                    #DEBUG_ON
                    #int_Stop_Age = 384
                    #if int(keyAgeInMonths) == int_Stop_Age:
                    #    if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                    #        self.obj_Log_Debug_AgeNe.debug('Age: ' + str(int_Stop_Age))
                    #    pass
                    #pass
                    #DEBUG_OFF
                    '''
                    ~~~~~~~~~~~~
                    Mortality - COMBINED
                    ~~~~~~~~~~~~
                    '''
                    decNumIndividualsInPerAgeClass = Decimal(valueIndivsInAgeClass)
                    intNumIndividualsToKillPerAgeClass = int(round(decRateofMortalityForAge*decNumIndividualsInPerAgeClass)) #Round out the decimal result to the nearest whole individual
                    odictNumIndividualsToKillPerAgeClass[keyAgeInMonths] = intNumIndividualsToKillPerAgeClass
                
                    '''
                    ~~~~~~~~~~~~
                    Mortality - 1st Pass NATURAL - For reporting only
                    ~~~~~~~~~~~~
                    '''
                    if bool_OverMaxAge:
                        decRateofMortalityForAge_NATURAL = decRateofMortalityForAge
                    else:
                        decRateofMortalityForAge_NATURAL = Decimal(1-(self.objSSParametersLocal.odictRates_Of_Survival_NATURAL_BySex_ByAge[strSex][keyAgeInMonths]))
                    pass
                    ''' Deaths '''
                    intNumIndividualsToKillPerAgeClass_NATURAL = int(round(decRateofMortalityForAge_NATURAL*decNumIndividualsInPerAgeClass)) #Round out the decimal result to the nearest whole individual
                    ''' Survivors '''
                    intNumIndividualsSurvivingPerAgeClass_NATURAL = int(decNumIndividualsInPerAgeClass) - intNumIndividualsToKillPerAgeClass_NATURAL
                
                    '''
                    ~~~~~~~~~~~~
                    Mortality - 1st Pass UnNATURAL - For reporting only
                    ~~~~~~~~~~~~
                    '''
                    if bool_Start_UnNatural_Mortality:
                        if bool_OverMaxAge:
                            decRateofMortalityForAge_UnNATURAL = decRateofMortalityForAge
                        else:
                            decRateofMortalityForAge_UnNATURAL = Decimal(1-(self.objSSParametersLocal.odictRates_Of_Survival_UnNATURAL_BySex_ByAge[strSex][keyAgeInMonths]))
                        pass
                    else:
                        decRateofMortalityForAge_UnNATURAL = Decimal(0)
                    pass
                
                    ''' Deaths  - From Survivors after NATURAL mortality is applied first'''
                    decNumIndividualsSurvivingPerAgeClass = Decimal(intNumIndividualsSurvivingPerAgeClass_NATURAL)
                    intNumIndividualsToKillPerAgeClass_UnNATURAL = int(round(decRateofMortalityForAge_UnNATURAL*decNumIndividualsSurvivingPerAgeClass)) #Round out the decimal result to the nearest whole individual
                    
                    ''' NOTE: These totals may differ by 1 indive per age cohort due to different rounding of COMBINED vs NATURAL + UNNATURAL rates of mortality...
                    Unless this correction is preformed and the NATURAL deaths DEBITED by the correction factor.
                    NATURAL mort was selected for the debit because the UnNATURAL may need to reconcile prefectly for mortality analysis. NATURAL mort is also easire to calculate and factor in this corretion ''' 
                    ''' Check totals with the Killed with COMBINED rate and adjust by 1 if they dont match - Rounding error when separating Nat from UnNat Mort '''
                    int_Idiv_Correction = intNumIndividualsToKillPerAgeClass - (intNumIndividualsToKillPerAgeClass_NATURAL + intNumIndividualsToKillPerAgeClass_UnNATURAL)
                    if int_Idiv_Correction != 0:
                        if intNumIndividualsToKillPerAgeClass_NATURAL > 0:
                            intNumIndividualsToKillPerAgeClass_NATURAL = intNumIndividualsToKillPerAgeClass_NATURAL + int_Idiv_Correction
                        elif intNumIndividualsToKillPerAgeClass_UnNATURAL > 0:
                            intNumIndividualsToKillPerAgeClass_UnNATURAL = intNumIndividualsToKillPerAgeClass_UnNATURAL + int_Idiv_Correction
                        pass
                    pass
                    '''
                    ~~~~~~~~~~~~
                    Mortality - 2nd Pass After correction -  NATURAL - For reporting only
                    ~~~~~~~~~~~~
                    '''
                    ''' Deaths - After correction '''
                    odictNumIndividualsToKillPerAgeClass_NATURAL[keyAgeInMonths] = intNumIndividualsToKillPerAgeClass_NATURAL
                    ''' Survivors - After correction  '''
                    intNumIndividualsSurvivingPerAgeClass_NATURAL = int(decNumIndividualsInPerAgeClass) - intNumIndividualsToKillPerAgeClass_NATURAL
                    odictNumIndividualsSurvivingPerAgeClass_NATURAL[keyAgeInMonths] = intNumIndividualsSurvivingPerAgeClass_NATURAL

                    '''
                    ~~~~~~~~~~~~
                    Mortality - 2nd Pass After correction -  UnNATURAL - For reporting only
                    ~~~~~~~~~~~~
                    '''
                    '''Deaths - After correction  '''
                    odictNumIndividualsToKillPerAgeClass_UnNATURAL[keyAgeInMonths] = intNumIndividualsToKillPerAgeClass_UnNATURAL
                    ''' Survivors - After correction - From Survivors - Deaths, after NATURAL mortality is applied first'''
                    decNumIndividualsSurvivingPerAgeClass = Decimal(intNumIndividualsSurvivingPerAgeClass_NATURAL)
                    intNumIndividualsSurvivingPerAgeClass_UnNATURAL = int(decNumIndividualsSurvivingPerAgeClass) - intNumIndividualsToKillPerAgeClass_UnNATURAL
                    odictNumIndividualsSurvivingPerAgeClass_UnNATURAL[keyAgeInMonths] = intNumIndividualsSurvivingPerAgeClass_UnNATURAL

                pass
                '''
                ~~~~~~~~~~~~
                Survival Stats - Indivs Per Age Cohort -  Update Parameter object stats
                ~~~~~~~~~~~~
                '''
                self.objSSParametersLocal.odictPreMortalityNumIndividualsPerAgeClass[strSex] = odictIndividualCountPerAgeClass
                '''
                ~~~~~~~~~~~~
                Survival Stats - Mortality -  Update Parameter object stats
                ~~~~~~~~~~~~
                '''
                self.objSSParametersLocal.odictPostCOMBINEDMortalityNumIndividualsKilledPerAgeClass[strSex] = odictNumIndividualsToKillPerAgeClass

                if self.objSSParametersLocal.boolAllowNATURALMortality: 
                    self.objSSParametersLocal.odictPostNATURALMortalityNumIndividualsKilledPerAgeClass[strSex] = odictNumIndividualsToKillPerAgeClass_NATURAL
                pass
                if self.objSSParametersLocal.boolAllowUnNATURALMortality:
                    self.objSSParametersLocal.odictPostUNNATURALMortalityNumIndividualsKilledPerAgeClass[strSex] = odictNumIndividualsToKillPerAgeClass_UnNATURAL
                pass
                '''
                ~~~~~~~~~~~~
                Survival Stats - Survival -  Update Parameter object stats
                ~~~~~~~~~~~~
                '''
                odictNumIndividualsSurvivingPerAgeClass = odictNumIndividualsSurvivingPerAgeClass_UnNATURAL
                self.objSSParametersLocal.odictPostCOMBINEDMortalityNumIndividualsSurvivingPerAgeClass[strSex] = odictNumIndividualsSurvivingPerAgeClass 
                
                if self.objSSParametersLocal.boolAllowNATURALMortality: 
                    self.objSSParametersLocal.odictPostNATURALMortalityNumIndividualsSurvivingPerAgeClass[strSex] = odictNumIndividualsSurvivingPerAgeClass_NATURAL
                pass
                if self.objSSParametersLocal.boolAllowUnNATURALMortality: 
                    self.objSSParametersLocal.odictPostUNNATURALMortalityNumIndividualsSurvivingPerAgeClass[strSex] = odictNumIndividualsSurvivingPerAgeClass_UnNATURAL
                pass      
            
                '''
                >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                Number of Individuals to be killed and the associated stats have been gathered
                >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                '''
                
                '''
                -----------------
                Get IDs of indivs to die givent the number of deaths per age cohort
                -----------------
                '''
                ''' Need to remove individuals randomly one by one from each age class...
                #So get all the indexes of all the indivs in each age class '''    
                
                #DEBUG_ON
                #stringMessage = '> ' + 'dictIndexsofIndividualsByInfoField = ' + str(dictIndexsofIndividualsByInfoField) +'\n'
                #boolNewline=True
                #objSSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                #DEBUG_OFF
                
                #odictIndividuals_ind_id_ToKillPerAgeClass = {}
                odictIndividuals_ind_id_ToKillPerAgeClass = OrderedDict()
                for key, value in odictNumIndividualsToKillPerAgeClass.items():
                    #intNumIndividualsToKillPerAgeClass = int(round(value)) #Round out the decimal
                    intNumIndividualsToKillPerAgeClass = value
                    #DEBUG_ON
#                     stringMessage = '> ' + strSex + ' key = ' + str(key) + ' > ' + 'odictNumIndividualsToKillPerAgeClass[key] = ' + str(odictNumIndividualsToKillPerAgeClass[key]) + '\n'
#                     boolNewline=True
#                     objSSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                    #DEBUG_OFF
                    listIndividualIDsInAgeClass = odictIndividualsOfSpecificSex_NEW[key]
                    
                    ''' Take the number to kill in an age class from that age class '''
                    odictIndividuals_ind_id_ToKillPerAgeClass[key] = random__sample(listIndividualIDsInAgeClass, intNumIndividualsToKillPerAgeClass) 
                pass
            
                #DEBUG_ON
                #stringMessage = '> ' + 'odictIndividuals_ind_id_ToKillPerAgeClass = ' + str(odictIndividuals_ind_id_ToKillPerAgeClass) +'\n'
                #boolNewline=True
                #2015-05-04 --> objSSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                #DEBUG_OFF

                #DEBUG_ON
#                 int_Current_Replicate_Mating_Count = self.objSSParametersLocal.int_MatingCount_Replicate_Total
#                 if int_Current_Replicate_Mating_Count == 76:
#                     self.obj_Log_Debug_Display.debug('int_Current_Replicate_Mating_Count == 76')
#                 pass
                #DEBUG_OFF  
      

                '''
                ~~~~~~~~~~~~~~~~~~~~~~~~~~
                Mortality - FINALLY...REMOVE INDIVIDUALS MARKED FOR MORT
                ~~~~~~~~~~~~~~~~~~~~~~~~~~
                '''                
                ''' 
                Finally remove the individuals from the population 
                Also report the idividuals killed by life stage 
                '''
                if boolRemoveIndividuals:
                    odictKilled_Per_Age_Class = OrderedDict()
                    odictKilled_Per_Life_Stage = OrderedDict()
                    odictKilled_Per_Age_In_Months = OrderedDict()
                    
                    for key, value in odictIndividuals_ind_id_ToKillPerAgeClass.items():
                            for intListPos in range(0,len(value)):
                                floatIdividuals_ind_id = value[intListPos]
                                simupopIndividual = pop_In.indByID(floatIdividuals_ind_id) #Lookup individual by specific ind_id
                                
                                ''' for reporting: record the age class totals for killed and survivors '''
                                str_Stage_Info = int(simupopIndividual.info('age_class'))
                                if str_Stage_Info in odictKilled_Per_Age_Class.keys():
                                    odictKilled_Per_Age_Class[str_Stage_Info] += 1
                                else:
                                    odictKilled_Per_Age_Class[str_Stage_Info] = 1
                                pass
                                ''' for reporting: record the life stage totals for killed and survivors '''
                                str_Stage_Info = int(simupopIndividual.info('life_stage'))
                                if str_Stage_Info in odictKilled_Per_Life_Stage.keys():
                                    odictKilled_Per_Life_Stage[str_Stage_Info] += 1
                                else:
                                    odictKilled_Per_Life_Stage[str_Stage_Info] = 1
                                pass
                            
                                ''' for reporting: record the age in months totals for killed and survivors '''
                                str_Stage_Info = int(simupopIndividual.info('age_in_months'))
                                if str_Stage_Info in odictKilled_Per_Age_In_Months.keys():
                                    odictKilled_Per_Age_In_Months[str_Stage_Info] += 1
                                else:
                                    odictKilled_Per_Age_In_Months[str_Stage_Info] = 1
                                pass
                            
                                ''' flag individual as Died '''                                
                                simupopIndividual.setInfo(self.objSSParametersLocal.maxAge*12, 'age_in_months')
                                simupopIndividual.setInfo(globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Died, 'age_class')
                                simupopIndividual.setInfo(globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Died, 'life_stage')
                            
                                #Removing in this fashon  BREAKS the mating scheme
                                #bool_Delete_Individuals = True
                                #if bool_Delete_Individuals:
                                #    pop_In.removeIndividuals(IDs=[floatIdividuals_ind_id], idField='ind_id')
                                #pass
                            
                            pass
                    pass

                    #DEBUG_ON
                    #pop1 = pop_In.extractIndividuals(IDs=[2, 4], idField='age_in_months')
                    #DEBUG_OFF
                    '''
                    ~~~~~~~~~~~~
                    Mortality -  Reporting stats
                    ~~~~~~~~~~~~
                    '''                
                    self.method_Post_Mortality_Reporting(pop_In, intMortalityType, strSex, odictKilled_Per_Age_Class, odictKilled_Per_Life_Stage)
                pass

                #DEBUG_ON
                if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                    ''' Individuals per age cohort '''
                    #odict_Logging = odictIndividualCountPerAgeClass
                    odict_Logging = self.objSSParametersLocal.odictPreMortalityNumIndividualsPerAgeClass[strSex]
                    odict_Logging = OrderedDict(sorted(odictIndividualCountPerAgeClass.items(), key=lambda x: x[0]))
                    #str_Message = '>>> Survival Stat: odictIndividualCountPerAgeClass: '
                    str_Message = '>>> Survival Stat: odictPreMortalityNumIndividualsPerAgeClass: '
                    self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + strSex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                    str_Message += ':::Age;Num\t'
                    for int_Age, value in odict_Logging.items():
                        str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                    pass 
                    self.obj_Log_Debug_AgeNe.debug(str_Message)                    
                    
                    ''' Mortality '''
                    if self.objSSParametersLocal.boolAllowNATURALMortality:
                        odict_Logging = self.objSSParametersLocal.odictPostNATURALMortalityNumIndividualsKilledPerAgeClass[strSex]
                        odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                        str_Message = '>>> Survival Stat: odictPostNATURALMortalityNumIndividualsKilledPerAgeClass: '
                        self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + strSex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                        str_Message += ':::Age;Num\t'
                        for int_Age, value in odict_Logging.items():
                            str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                        pass 
                        self.obj_Log_Debug_AgeNe.debug(str_Message)
                    
                    if self.objSSParametersLocal.boolAllowUnNATURALMortality:
                        odict_Logging = self.objSSParametersLocal.odictPostUNNATURALMortalityNumIndividualsKilledPerAgeClass[strSex]
                        odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                        str_Message = '>>> Survival Stat: odictPostUNNATURALMortalityNumIndividualsKilledPerAgeClass: '
                        self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + strSex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                        str_Message += ':::Age;Num\t'
                        for int_Age, value in odict_Logging.items():
                            str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                        pass 
                        self.obj_Log_Debug_AgeNe.debug(str_Message)

                    if self.objSSParametersLocal.boolAllowNATURALMortality:
                        odict_Logging = self.objSSParametersLocal.odictPostCOMBINEDMortalityNumIndividualsKilledPerAgeClass[strSex]
                        odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                        str_Message = '>>> Survival Stat: odictPostCOMBINEDMortalityNumIndividualsKilledPerAgeClass: '
                        self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + strSex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                        str_Message += ':::Age;Num\t'
                        for int_Age, value in odict_Logging.items():
                            str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                        pass 
                        self.obj_Log_Debug_AgeNe.debug(str_Message)
                                                
                    ''' Survivors '''
                    if self.objSSParametersLocal.boolAllowNATURALMortality:
                        odict_Logging = self.objSSParametersLocal.odictPostNATURALMortalityNumIndividualsSurvivingPerAgeClass[strSex]
                        odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                        str_Message = '>>> Survival Stat: odictPostNATURALMortalityNumIndividualsSurvivingPerAgeClass: '
                        self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + strSex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                        str_Message += ':::Age;Num\t'
                        for int_Age, value in odict_Logging.items():
                            str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                        pass 
                        self.obj_Log_Debug_AgeNe.debug(str_Message)

                    if self.objSSParametersLocal.boolAllowUnNATURALMortality:
                        odict_Logging = self.objSSParametersLocal.odictPostUNNATURALMortalityNumIndividualsSurvivingPerAgeClass[strSex]
                        odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                        str_Message = '>>> Survival Stat: odictPostUNNATURALMortalityNumIndividualsSurvivingPerAgeClass: '
                        self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + strSex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                        str_Message += ':::Age;Num\t'
                        for int_Age, value in odict_Logging.items():
                            str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                        pass 
                        self.obj_Log_Debug_AgeNe.debug(str_Message)

                    if self.objSSParametersLocal.boolAllowNATURALMortality:
                        odict_Logging = self.objSSParametersLocal.odictPostCOMBINEDMortalityNumIndividualsSurvivingPerAgeClass[strSex]
                        odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                        str_Message = '>>> Survival Stat: odictPostCOMBINEDMortalityNumIndividualsSurvivingPerAgeClass: '
                        self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + strSex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                        str_Message += ':::Age;Num\t'
                        for int_Age, value in odict_Logging.items():
                            str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                        pass 
                        self.obj_Log_Debug_AgeNe.debug(str_Message)

                    ''' Total actually removed from pop '''
                    if self.objSSParametersLocal.boolAllowNATURALMortality:
                        odict_Logging = odictKilled_Per_Age_In_Months
                        odict_Logging = OrderedDict(sorted(odict_Logging.items(), key=lambda x: x[0]))
                        str_Message = '>>> Survival Stat: odictKilled_Per_Age_In_Months: '
                        self.obj_Log_Debug_AgeNe.debug(str_Message + 'Sex: ' + strSex + ' ; Total: ' + str(round(sum(collections__Counter(odict_Logging).values()),2)))
                        str_Message += ':::Age;Num\t'
                        for int_Age, value in odict_Logging.items():
                            str_Message += str(int(int_Age)) + ',' + str(value) + '\t'
                        pass 
                        self.obj_Log_Debug_AgeNe.debug(str_Message)
                    
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                        
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message='', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                #DEBUG_OFF

                pop_Out = pop_In
                
                return pop_Out
                

            '''
            -------------------------------------------------------------------------------------------------------
            # Stats Accumulation
            --------------------------------------------------------------------------------------------------------
            '''

            def method_Get_Birth_Rate_Stats_For_Sex(self, pop_In, strSex):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass
            
                                  
                odictBirthRatePerSex = OrderedDict()
                
                #Get scaled birth rate details to supply to AgeNe
                with SSAnalysisHandler() as objSSAnalysisOperation:

                    intAgeInMonths = 1
                    intVirtualSubPop = intAgeInMonths
                    dictParentOffspringCount = objSSAnalysisOperation.method_Count_Offspring_Per_Parent_Given_Sex_For_VirtualSubPop_Into_Dict(pop_In, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop, strSex)
                    
                    if (len(dictParentOffspringCount) > 0):
                        with AnalysisHandler() as objAnalysisOperation:
                            
                            #Construct a list of ACTUAL SIRE offspring counts
                            listOffspringCount = []
                            for i in dictParentOffspringCount[strSex]:
                                listOffspringCount.append(dictParentOffspringCount[strSex][i])
                            
                            intTotalOffspringCount = sum(listOffspringCount) 
                            floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listOffspringCount)
                            floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listOffspringCount)

                            dictNewValues = {
                                             globalsSS.StatisticsConstants.static_stringSampleSizeLabel:intTotalOffspringCount
                                             ,globalsSS.StatisticsConstants.static_stringMeanLabel:floatMean
                                             ,globalsSS.StatisticsConstants.static_stringVarianceLabel:floatVariance
                                             }
                            
                            if strSex in odictBirthRatePerSex:
                                odictBirthRatePerSex[strSex].update(dictNewValues)
                            else:
                                odictBirthRatePerSex[strSex] = dictNewValues


                ''' End of func DEBUG '''
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                        self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + 'AgeNe Stat: odictBirthRatePerSex')
                        for str_Sex, value in odictBirthRatePerSex.items():
                            self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(float(sum(collections__Counter(value).values())),2)) + ' ; Values: ' + str(value)) 
                        pass
                    pass                        
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
                return odictBirthRatePerSex

            def method_Pre_Fertilization_Stats_Gathering(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()     
                
                bool_Get_Potential_Parents_Before_Mating = True
                if bool_Get_Potential_Parents_Before_Mating:
                    listPotentialFemaleParents, listPotentialMaleParents = self.method_Pre_Mating_Potential_Parent_Determination(pop_In)
                    self.objSSParametersLocal.listPotentialFemaleParents = listPotentialFemaleParents
                    self.objSSParametersLocal.listPotentialMaleParents = listPotentialMaleParents
                pass

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message='', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass                 
                return True
                

            '''
            --------------------------------------------------------------------------------------------------------
            # Reporting
            --------------------------------------------------------------------------------------------------------
            '''

            def method_Post_Mortality_Reporting(self, pop_In, intMortalityType, strSex, odictKilled_Per_Age_Class, odictKilled_Per_Life_Stage):

                with SSAnalysisHandler() as objSSAnalysisOperation:
                    
                    ''' Determine survivors by stage for reporting '''
                    #pop_In = objSSAnalysisOperation.method_VSP_Split_Age_Class_By_Sex(pop_In)
                    #odictSurvived_Per_Age_Class = objSSAnalysisOperation.method_Get_VSP_Sizes(pop_In, True)
                    pop_In = objSSAnalysisOperation.method_VSP_Split_Pop_By_Sex(pop_In)
                    str_InfoField = 'age_class'
                    listExpectedKeyValues = [x for x in range(0, globalsSS.VSP_AgeClass.static_intVSP_AgeClass_NumberofVSPs)]
                    odictSurvived_Per_Age_Class = objSSAnalysisOperation.method_Get_VSP_Sizes_By_InfoField(pop_In, True, listExpectedKeyValues, str_InfoField, strSex)
                    
                   
                    #pop_In = objSSAnalysisOperation.method_VSP_Split_Life_Stage_By_Sex(pop_In)
                    #odictSurvived_Per_Life_Stage = objSSAnalysisOperation.method_Get_VSP_Sizes(pop_In, True)
                    pop_In = objSSAnalysisOperation.method_VSP_Split_Pop_By_Sex(pop_In)
                    str_InfoField = 'life_stage'
                    listExpectedKeyValues = [x for x in range(0, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_NumberofVSPs)]
                    odictSurvived_Per_Life_Stage = objSSAnalysisOperation.method_Get_VSP_Sizes_By_InfoField(pop_In, True, listExpectedKeyValues, str_InfoField, strSex)

                    ''' Report for each mortality type '''
#                     intMortalityType = globalsSS.MortalitySource.static_intMortalityType_NATURAL
#                     self.method_Post_Mortality_Update_Reporting_Vars(intMortalityType, strSex, odictKilled_Per_Age_Class, odictSurvived_Per_Age_Class, odictKilled_Per_Life_Stage, odictSurvived_Per_Life_Stage)
#                     intMortalityType = globalsSS.MortalitySource.static_intMortalityType_UnNATURAL
#                     self.method_Post_Mortality_Update_Reporting_Vars(intMortalityType, strSex, odictKilled_Per_Age_Class, odictSurvived_Per_Age_Class, odictKilled_Per_Life_Stage, odictSurvived_Per_Life_Stage)
                    intMortalityType = globalsSS.MortalitySource.static_intMortalityType_COMBINED
                    self.method_Post_Mortality_Update_Reporting_Vars(intMortalityType, strSex, odictKilled_Per_Age_Class, odictSurvived_Per_Age_Class, odictKilled_Per_Life_Stage, odictSurvived_Per_Life_Stage)
                    
                    return True

            def method_Post_Mortality_Update_Reporting_Vars(self, intMortalityType, strSex, odictKilled_Per_Age_Class, odictSurvived_Per_Age_Class, odictKilled_Per_Life_Stage, odictSurvived_Per_Life_Stage):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass 
                      
                                
                ''' update reporting variables after clearing them for every mortaility event '''
                #Determine what type of mortality we are dealing with here 
                if intMortalityType == globalsSS.MortalitySource.static_intMortalityType_NATURAL:

                    self.objSSParametersLocal.odictKilled_NATURAL_Per_Age_Class_By_Sex[strSex] = odictKilled_Per_Age_Class
                    self.objSSParametersLocal.odictKilled_NATURAL_Per_Life_Stage_By_Sex[strSex] = odictKilled_Per_Life_Stage
                        
                elif intMortalityType == globalsSS.MortalitySource.static_intMortalityType_UnNATURAL:

                    self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Age_Class_By_Sex[strSex] = odictKilled_Per_Age_Class
                    self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Life_Stage_By_Sex[strSex] = odictKilled_Per_Life_Stage
                
                elif intMortalityType == globalsSS.MortalitySource.static_intMortalityType_COMBINED:

                    self.objSSParametersLocal.odictKilled_COMBINED_Per_Age_Class_By_Sex[strSex] = odictKilled_Per_Age_Class
                    self.objSSParametersLocal.odictKilled_COMBINED_Per_Life_Stage_By_Sex[strSex] = odictKilled_Per_Life_Stage
                    self.objSSParametersLocal.odictSurvived_COMBINED_Per_Age_Class_By_Sex[strSex] = odictSurvived_Per_Age_Class
                    self.objSSParametersLocal.odictSurvived_COMBINED_Per_Life_Stage_By_Sex[strSex] = odictSurvived_Per_Life_Stage
                pass
                    
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                            
                return True
            
            def method_Post_Mortality_Reporting_RECENT(self, pop_In, intMortalityType, strSex, odictKilled_Per_Age_Class, odictKilled_Per_Life_Stage):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass 
            
                '''
                ***********************************************************************
                NOTE: This is expensive method due to simupop.Stat popSize inefficiancy
                in method_Get_VSP_Sizes for large numbers of VSPs
                ************************************************************************
                '''
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    
                    ''' Determine survivors by stage for reporting '''
                    #pop_In = objSSAnalysisOperation.method_VSP_Split_Age_Class_By_Sex(pop_In)
                    #odictSurvived_Per_Age_Class = objSSAnalysisOperation.method_Get_VSP_Sizes(pop_In, True)
                    pop_In = objSSAnalysisOperation.method_VSP_Split_Pop_By_Sex(pop_In)
                    str_InfoField = 'age_class'
                    listExpectedKeyValues = [x for x in range(0, globalsSS.VSP_AgeClass.static_intVSP_AgeClass_NumberofVSPs)]
                    odictSurvived_Per_Age_Class = objSSAnalysisOperation.method_Get_VSP_Sizes_By_InfoField(pop_In, True, listExpectedKeyValues, str_InfoField, strSex)
                    
                   
                    #pop_In = objSSAnalysisOperation.method_VSP_Split_Life_Stage_By_Sex(pop_In)
                    #odictSurvived_Per_Life_Stage = objSSAnalysisOperation.method_Get_VSP_Sizes(pop_In, True)
                    pop_In = objSSAnalysisOperation.method_VSP_Split_Pop_By_Sex(pop_In)
                    str_InfoField = 'life_stage'
                    listExpectedKeyValues = [x for x in range(0, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_NumberofVSPs)]
                    odictSurvived_Per_Life_Stage = objSSAnalysisOperation.method_Get_VSP_Sizes_By_InfoField(pop_In, True, listExpectedKeyValues, str_InfoField, strSex)

                    ''' update reporting variables after clearing them for every mortaility event '''
                    #Determine what type of mortality we are dealing with here 
                    if intMortalityType == globalsSS.MortalitySource.static_intMortalityType_NATURAL:
    
                        self.objSSParametersLocal.odictKilled_NATURAL_Per_Age_Class_By_Sex[strSex] = odictKilled_Per_Age_Class
                        self.objSSParametersLocal.odictKilled_NATURAL_Per_Life_Stage_By_Sex[strSex] = odictKilled_Per_Life_Stage
    
                        #odictSurvived_Per_Age_Class, odictSurvived_Per_Life_Stage = Get_Survived(strSex, odictSurvived_Per_Age_Class, odictSurvived_Per_Life_Stage)
                    
                        self.objSSParametersLocal.odictSurvived_NATURAL_Per_Age_Class_By_Sex[strSex] = odictSurvived_Per_Age_Class
                        self.objSSParametersLocal.odictSurvived_NATURAL_Per_Life_Stage_By_Sex[strSex] = odictSurvived_Per_Life_Stage
                            
                    elif intMortalityType == globalsSS.MortalitySource.static_intMortalityType_UnNATURAL:
    
                        self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Age_Class_By_Sex[strSex] = odictKilled_Per_Age_Class
                        self.objSSParametersLocal.odictKilled_UnNATURAL_Per_Life_Stage_By_Sex[strSex] = odictKilled_Per_Life_Stage
    
                        #odictSurvived_Per_Age_Class, odictSurvived_Per_Life_Stage = Get_Survived(strSex, odictSurvived_Per_Age_Class, odictSurvived_Per_Life_Stage)

                        self.objSSParametersLocal.odictSurvived_UnNATURAL_Per_Age_Class_By_Sex[strSex] = odictSurvived_Per_Age_Class
                        self.objSSParametersLocal.odictSurvived_UnNATURAL_Per_Life_Stage_By_Sex[strSex] = odictSurvived_Per_Life_Stage
                    
                    elif intMortalityType == globalsSS.MortalitySource.static_intMortalityType_COMBINED:
    
                        self.objSSParametersLocal.odictKilled_COMBINED_Per_Age_Class_By_Sex[strSex] = odictKilled_Per_Age_Class
                        self.objSSParametersLocal.odictKilled_COMBINED_Per_Life_Stage_By_Sex[strSex] = odictKilled_Per_Life_Stage
    
                        #odictSurvived_Per_Age_Class, odictSurvived_Per_Life_Stage = Get_Survived(strSex, odictSurvived_Per_Age_Class, odictSurvived_Per_Life_Stage)

                        self.objSSParametersLocal.odictSurvived_COMBINED_Per_Age_Class_By_Sex[strSex] = odictSurvived_Per_Age_Class
                        self.objSSParametersLocal.odictSurvived_COMBINED_Per_Life_Stage_By_Sex[strSex] = odictSurvived_Per_Life_Stage
                    pass
                    
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                            
                return True
            
            def method_Post_Fertilization_Reporting(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()     
                
                bool_Post_Fertilization_Reporting = True
                if bool_Post_Fertilization_Reporting:

                    bool_Save_Simupop_Pop_PF = True
                    if bool_Save_Simupop_Pop_PF:
                        with SSSamplingTest() as obj_Sampling:
                            #if self.objSSParametersLocal.int_MatingCount_Replicate_Total >= (self.objSSParametersLocal.intAgeNe_Data_Collection_Start__Replicate_Mating_Count + self.objSSParametersLocal.maxAge):
                            if self.objSSParametersLocal.int_MatingCount_Replicate_Total >= self.objSSParametersLocal.int_SimuPop_Saving_Starts__Replicate_Mating_Count:
                                ''' Only save pop every mating as specified by int_SimuPop_Save_Every__Replicate_Mating_Count '''
                                int_Replicate_Mating_Count_Div = float(self.objSSParametersLocal.int_MatingCount_Replicate_Total) / float(self.objSSParametersLocal.int_SimuPop_Save_Every__Replicate_Mating_Count) 
                                bool_Save_Pop = (int_Replicate_Mating_Count_Div).is_integer()
                                if bool_Save_Pop:
                                    #obj_Sampling.method_Initialise(self.obj_SSParams, self)
                                    str_Save_Path = self.objSSParametersLocal.str_Current_Run_Path + '\\' + globalsSS.SS_Per_Fert_PF_File_Output_Details.static_Output_Path_Folder__SimuPOP_Pop_PF 
                                    str_Save_FileName = self.objSSParametersLocal.strUniqueRunID + globalsSS.SS_Per_Fert_PF_File_Output_Details.static_Output_File_Prefix__SimuPOP_Pop_PF + self.str_Sim_Total_Mating_Batch_Replicate_Mating_Identifier_Short + globalsSS.SS_Per_Fert_PF_File_Output_Details.static_Output_File_Suffix__SimuPOP_Pop_PF  
                                    strSimuPop_Pop_FilePathAndName = str_Save_Path + str_Save_FileName
                                    bool_Success = False
                                    bool_Success = obj_Sampling.method_Save_SimuPop_Population(pop_In, strSimuPop_Pop_FilePathAndName)
                                pass
                            pass
                        pass
                    pass
                
                    bool_Log_Mortality_PF = True
                    if bool_Log_Mortality_PF:
                        if self.objSSParametersLocal.boolBurnIn == True and \
                           (self.objSSParametersLocal.intSimulationCurrentMonth / 12) < 1:
                            pass
                        else:
                            ''' Log NATURAL mortality '''
                            int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_NATURAL
                            bool_Success = False
                            bool_Success = self.method_Mortality_PF_Logging(int_Mortality_Type)

#                             ''' Log UnNATURAL mortality when it starts'''                            
#                             int_Current_Replicate_Mating_Count = self.objSSParametersLocal.int_MatingCount_Replicate_Total
#                             int_Mating_Mortality_Starts__UnNat = self.objSSParametersLocal.dict_Mortality_Application_Specs_By_Sex__UnNATURAL[globalsSS.MortalityApplication.static_str_Mating_Mortlity_Starts__UnNat]['Male']
#                             if int_Current_Replicate_Mating_Count >= int_Mating_Mortality_Starts__UnNat:
#                                 int_Mortality_Type = globalsSS.MortalitySource.static_intMortalityType_UnNATURAL
#                                 bool_Success = False
#                                 bool_Success = self.method_Mortality_PF_Logging(int_Mortality_Type)
#                                 pass
#                             pass
                        pass
                    pass

                    bool_Post_Sim_Ne2_LDNe_EXPERIMENT_2 = True
                    if bool_Post_Sim_Ne2_LDNe_EXPERIMENT_2:
                        ''' Start collecting results AFTER a lifespans worth of data has been collected as specified by intAgeNe_Data_Collection_Start__Replicate_Mating_Count'''
                        bool_First_Sample = False
                        bool_Next_Sample = False
                        bool_Header = False
                        if self.objSSParametersLocal.int_MatingCount_Replicate_Total == (self.objSSParametersLocal.intAgeNe_Data_Collection_Start__Replicate_Mating_Count + self.objSSParametersLocal.maxAge):
                            bool_First_Sample = True
                            bool_Header = True
                        elif self.objSSParametersLocal.int_MatingCount_Replicate_Total > (self.objSSParametersLocal.intAgeNe_Data_Collection_Start__Replicate_Mating_Count + self.objSSParametersLocal.maxAge):
                            bool_Next_Sample = True
                            bool_Header = False
                        else:
                            bool_First_Sample = False
                            bool_Next_Sample = False
                            bool_Header = False
                        pass
                        if bool_First_Sample or bool_Next_Sample:

                            bool_AgeNe_Reporting_2 = True
                            if bool_AgeNe_Reporting_2:
                                #self.method_SplitLifeStagesIntoVSPs_By_AgeClass(pop_In)
                                dict_Results = self.method_Log_Reporting_AgeNe_PF_Statistics(bool_Header)
                            pass   
                            
                        pass
                    pass 
                                
                    bool_Report_Offsping_Per_Parent = True
                    if bool_Report_Offsping_Per_Parent:
                        pop_In = self.method_SplitLifeStagesIntoVSPs_By_AgeClass(pop_In)
                        param=globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo
                        self.method_OutputPopulationOffspringTotalsByParent(pop_In, param)
                    pass
                
                    bool_Report_Summary_Parent_Offspring_Stats = True
                    if bool_Report_Summary_Parent_Offspring_Stats:
                        pop_In = self.method_SplitLifeStagesIntoVSPs_By_AgeClass(pop_In)
                        #pop_In = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop_In, False)
                        self.method_Summary_Parent_Offspring_Stats_Reporting(pop_In)
                    pass
                               
                    bool_Report_Effective_Parent_Summary_Stats = True
                    if bool_Report_Effective_Parent_Summary_Stats:
                        pop_In = self.method_SplitLifeStagesIntoVSPs_By_AgeClass(pop_In)
                        self.method_Effective_Parent_Summary_Stats_Reporting(pop_In)
                    pass               
    
                    bool_Report_Level_REPLICATE = True
                    if bool_Report_Level_REPLICATE:
                        pop_In = self.method_SplitLifeStagesIntoVSPs_By_AgeClass(pop_In)
                        str_Reporting_Interval = globalsSS.SS_Level_Details.static_Reporting_Interval__Level_REPLICATE_Post_Fertilization
                        self.method_REPLICATE_LEVEL_RLF_Reporting(pop_In, str_Reporting_Interval)
                    pass               
    
                    bool_Report_Level_Age_Class_VSP = True
                    if bool_Report_Level_Age_Class_VSP:    
                        #str_VSP_Group = globalsSS.VSP_Groups.static_VSP_Group_Age_Class
                        str_Reporting_Interval = globalsSS.SS_Level_Details.static_Reporting_Interval__Level_Age_Class_VSP_Post_Fertilization        
                        self.method_VSP_LEVEL_Age_Class_VLF_Reporting(pop_In, str_Reporting_Interval)
                    pass
                
                    bool_Report_Level_Life_Stage_VSP = True
                    if bool_Report_Level_Life_Stage_VSP:
                        #str_VSP_Group = globalsSS.VSP_Groups.static_VSP_Group_Life_Stage    
                        str_Reporting_Interval = globalsSS.SS_Level_Details.static_Reporting_Interval__Level_Life_Stage_VSP_Post_Fertilization        
                        self.method_VSP_LEVEL_Life_Stage_VLF_Reporting(pop_In, str_Reporting_Interval)
                    pass

                                
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass

                
                return True
                   
            '''@profile'''                                         
            def method_End_Of_SIM_REPLICATE_Reporting(self, pop_In):
                
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                        
                bool_End_Of_SIM_REPLICATE_reporting = True
                if bool_End_Of_SIM_REPLICATE_reporting:
                    
                    self.method_SplitLifeStagesIntoVSPs_By_AgeClass(pop_In)
                    
                    ''' End of SIM REPLICATE - LEVEL reporting '''
                    bool_Report_Level_SIM = True
                    if bool_Report_Level_SIM:
                        self.method_SIM_LEVEL_SLF_Reporting(pop_In)
                    pass
    
                    bool_Report_Level_BATCH = True
                    if bool_Report_Level_BATCH:
                        self.method_BATCH_LEVEL_BLF_Reporting(pop_In)
                    pass
    
                    bool_Report_Level_REPLICATE = True
                    if bool_Report_Level_REPLICATE:            
                        str_Reporting_Interval = globalsSS.SS_Level_Details.static_Reporting_Interval__Level_REPLICATE_End_Of_Replicate
                        self.method_REPLICATE_LEVEL_RLF_Reporting(pop_In, str_Reporting_Interval)
                    pass
    
                    bool_Report_Level_Age_Class_VSP = True
                    if bool_Report_Level_Age_Class_VSP:    
                        str_Reporting_Interval = globalsSS.SS_Level_Details.static_Reporting_Interval__Level_Age_Class_VSP_End_Of_Replicate        
                        self.method_VSP_LEVEL_Age_Class_VLF_Reporting(pop_In, str_Reporting_Interval)
                    pass
                
                    bool_Report_Level_Life_Stage_VSP = True
                    if bool_Report_Level_Life_Stage_VSP:    
                        str_Reporting_Interval = globalsSS.SS_Level_Details.static_Reporting_Interval__Level_Life_Stage_VSP_End_Of_Replicate        
                        self.method_VSP_LEVEL_Life_Stage_VLF_Reporting(pop_In, str_Reporting_Interval)
                    pass
                
                
                    ''' End of SIM REPLICATE - NE reporting '''

                    bool_Ne2_LDNe_EXPERIMENT_1 = False
                    if bool_Ne2_LDNe_EXPERIMENT_1:
                        self.method_SplitLifeStagesIntoVSPs_By_AgeClass(pop_In)
                        dict_Results = OrderedDict()
                        dict_Results = self.method_Ne2_LDNe_EXPERIMENT_1(pop_In, dict_Results)
                    pass          
                
                          
                    bool_AgeNe_Reporting_1 = True
                    if bool_AgeNe_Reporting_1:
                        #self.method_SplitLifeStagesIntoVSPs_By_AgeClass(pop_In)
                        dict_Results = self.method_Reporting_AgeNe_Statistics(pop_In)
                    pass   
                       
                    bool_AgeNe_Reporting_2 = True
                    if bool_AgeNe_Reporting_2:
                        #self.method_SplitLifeStagesIntoVSPs_By_AgeClass(pop_In)
                        dict_Results = self.method_Log_Reporting_AgeNe_EOR_Statistics()
                    pass          
                          
                    boolEnd_Of_SIM_REPLICATE_Reporting_NE_Stat = False
                    if boolEnd_Of_SIM_REPLICATE_Reporting_NE_Stat:
                        self.method_End_Of_SIM_REPLICATE_Reporting_NE_Stats([(0,2)])
                    pass

                '''
                ---------------------------
                Close log files
                ---------------------------
                '''
                list_tup_Logs = [
                                 #(self.obj_Logging__EPS, self.obj_Results_Log__EPS)
                                (self.obj_Logging__EPNS, self.obj_Results_Log__EPNS)
                                ,(self.obj_Logging__EOS_NE2_CATEGORISED, self.obj_Results_Log__EOS_NE2_CATEGORISED)
                                ,(self.obj_Logging__PF_NE2_CATEGORISED, self.obj_Results_Log__PF_NE2_CATEGORISED)
                                ,(self.obj_Logging__EOR_AgeNe_Man_D, self.obj_Results_Log__EOR_AgeNe_Man_D)
                                ,(self.obj_Logging__EOR_AgeNe_Man_LT, self.obj_Results_Log__EOR_AgeNe_Man_LT)
                                ,(self.obj_Logging__EOR_AgeNe_Man_DT, self.obj_Results_Log__EOR_AgeNe_Man_DT)
                                ,(self.obj_Logging__EOR_AgeNe_Man_FT, self.obj_Results_Log__EOR_AgeNe_Man_FT)
                                ,(self.obj_Logging__EOR_AgeNe_Sim_D, self.obj_Results_Log__EOR_AgeNe_Sim_D)
                                ,(self.obj_Logging__EOR_AgeNe_Sim_LT, self.obj_Results_Log__EOR_AgeNe_Sim_LT)
                                ,(self.obj_Logging__EOR_AgeNe_Sim_DT, self.obj_Results_Log__EOR_AgeNe_Sim_DT)
                                ,(self.obj_Logging__EOR_AgeNe_Sim_FT, self.obj_Results_Log__EOR_AgeNe_Sim_FT)
                                ,(self.obj_Logging__PF_AgeNe_Sim_D, self.obj_Results_Log__PF_AgeNe_Sim_D)
                                ,(self.obj_Logging__PF_AgeNe_Sim_LT, self.obj_Results_Log__PF_AgeNe_Sim_LT)
                                ,(self.obj_Logging__PF_AgeNe_Sim_DT, self.obj_Results_Log__PF_AgeNe_Sim_DT)
                                ,(self.obj_Logging__PF_AgeNe_Sim_FT, self.obj_Results_Log__PF_AgeNe_Sim_FT)
                                ,(self.obj_Logging__Mortality_PF, self.obj_Results_Log__Mortality_PF)
                                ]
                
                self.method_Close_Log_Files(list_tup_Logs)
                
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass  
                                        
                return True
            
            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            Gather Stats - Stats Gathering
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
           
            def method_Initialise_Stats_For_ILF_Individual_Dump(self, pop, listVSPs):
                
                #DEBUG_ON
                #self.methodOutput_outputPopulationDump(self.pop)
                #DEBUG_OFF
                
                # ------- Initialise all the stats required for a standard ILF individual dump
                ##############  REPORT: Pop size Statistics
                #######<---simupop.stat(pop, popSize=True, subPops=simupop.ALL_AVAIL, vars=['popSize']),
                #######<---simupop.stat(pop, popSize=True, subPops=listVSPs, vars=['popSize_sp']),
                
                ##############  REPORT: Info field Statistics
                # age_in_months
                #######<---simupop.stat(pop, maxOfInfo=['age_in_months'], subPops=simupop.ALL_AVAIL, vars=['maxOfInfo']),
                #simupop.Stat(maxOfInfo=['age_in_months'], subPops=[(0, simupop.simupop.ALL_AVAIL)], vars='maxOfInfo_sp'),
                                        
                ##############  REPORT: Allele Freq Statistics
                self.method_SimStat_AlleleFreq_Reporting(pop, listVSPs)
                #sim.Stat(pop, alleleFreq=simupop.ALL_AVAIL, subPops=[(0,0), (0,1), (0,2), (0,3)]),
                #simupop.stat(pop, alleleFreq=simupop.ALL_AVAIL, subPops=simupop.ALL_AVAIL, vars=['alleleFreq','alleleNum']),
                #simupop.stat(pop, alleleFreq=simupop.ALL_AVAIL, subPops=listVSPs, vars=['alleleFreq_sp','alleleNum_sp']),

                #############  REPORT: NE Statistics
                #######<---self.method_SimStat_DemographicNe_Reporting(pop, param=listVSPs),
                 
#                        simupop.PyOperator(func=self.method_SimStat_LDNe_Reporting, param=[(0,0), (0,1), (0,2), (0,3)]),
                
                #SubPops with 0 pop cause an error ie (0,3)
                #######<---self.method_SimStat_TemporalFS_P1_Ne_Reporting(pop, param=listVSPs),

                #######<---self.method_SimStat_TemporalFS_P2_Ne_Reporting(pop, param=listVSPs),
                
                #self.objSSParametersLocal.boolReportLDNe = True
                self.method_SimStat_LDNe_Reporting(pop, param=listVSPs)


                pass   
                   
                    
            def method_Initialise_Stats_For_VSP_LEVEL_Reporting(self, pop_In, listVSPs):
                
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()  
                
                #DEBUG_ON
                #self.methodOutput_outputPopulationDump(self.pop)
                #DEBUG_OFF
                
                # ------- Initialise all the stats required for a standard ILF individual dump
                ##############  REPORT: Pop size Statistics
                #######<---simupop.stat(pop, popSize=True, subPops=simupop.ALL_AVAIL, vars=['popSize']),
                #######<---simupop.stat(pop, popSize=True, subPops=listVSPs, vars=['popSize_sp']),
                
                ##############  REPORT: Info field Statistics
                # age_in_months
                #######<---simupop.stat(pop, maxOfInfo=['age_in_months'], subPops=simupop.ALL_AVAIL, vars=['maxOfInfo']),
                #simupop.Stat(maxOfInfo=['age_in_months'], subPops=[(0, simupop.simupop.ALL_AVAIL)], vars='maxOfInfo_sp'),
                                        
                ##############  REPORT: Allele Freq Statistics
                self.method_SimStat_AlleleFreq_Reporting(pop_In, listVSPs)
                #sim.Stat(pop, alleleFreq=simupop.ALL_AVAIL, subPops=[(0,0), (0,1), (0,2), (0,3)]),
                #simupop.stat(pop, alleleFreq=simupop.ALL_AVAIL, subPops=simupop.ALL_AVAIL, vars=['alleleFreq','alleleNum']),
                #simupop.stat(pop, alleleFreq=simupop.ALL_AVAIL, subPops=listVSPs, vars=['alleleFreq_sp','alleleNum_sp']),

                #############  REPORT: NE Statistics
                #simupop.stat(pop_In, effectiveSize=[0], subPops=simupop.ALL_AVAIL, vars=['Ne_demo'])
                #simupop.stat(pop_In, effectiveSize=[0], subPops=listVSPs, vars=['Ne_demo_sp'])
                #simupop.stat(pop_In, effectiveSize=[0], subPops=[(0,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult)], vars=['Ne_demo_sp'])
                
                #SubPops with 0 pop cause an error ie (0,3)
                #######<---self.method_SimStat_TemporalFS_P1_Ne_Reporting(pop, param=listVSPs),

                #######<---self.method_SimStat_TemporalFS_P2_Ne_Reporting(pop, param=listVSPs),
                
                #self.objSSParametersLocal.boolReportLDNe = True
                self.method_SimStat_LDNe_Reporting(pop_In, param=listVSPs)

                pop_Out = pop_In

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass

                
                return pop_Out   
                    

            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # LEVEL specific reporting
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''

            def method_SIM_LEVEL_SLF_Reporting(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()   
                                    
                self.method_Output_SIM_LEVEL_SLF_Reporting(pop_In)

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass  
                          
                return True
            
            
            def method_BATCH_LEVEL_BLF_Reporting(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()   
                                    
                self.method_Output_BATCH_LEVEL_BLF_Reporting(pop_In)

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass  
                
                return True
            
            
            def method_REPLICATE_LEVEL_RLF_Reporting(self, pop_In, str_Reporting_Interval):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()   
                    
                ''' Get simuPOP LDNe stats '''
                #listVirtualSubPop = [0, 0]
                #pop_In = self.pop_In.clone()
                
                listVSPsForStats = [0]
                pop_Out = self.method_Initialise_Stats_For_VSP_LEVEL_Reporting(pop_In, listVSPsForStats)
                
                listSPsForReporting = [globalsSS.SP_SubPops.static_intSP_SubPop_Primary]
                
                if str_Reporting_Interval == globalsSS.SS_Level_Details.static_Reporting_Interval__Level_REPLICATE_End_Of_Replicate:
                    self.objSSParametersLocal.listOutputSPs_SP_Level_RLF_End_Of_Replicate = listSPsForReporting
                pass
            
                if str_Reporting_Interval == globalsSS.SS_Level_Details.static_Reporting_Interval__Level_REPLICATE_Post_Fertilization:
                    self.objSSParametersLocal.listOutputSPs_SP_Level_RLF_Post_Fertilization = listSPsForReporting
                pass
            
                self.method_Output_REPLICATE_LEVEL_RLF_Reporting(pop_Out, str_Reporting_Interval)

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass

                
                return True
            
            
            def method_VSP_LEVEL_Age_Class_VLF_Reporting(self, pop_In, str_Reporting_Interval):
                
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()   
                    
                ''' Get simuPOP LDNe stats '''
                #listVirtualSubPop = [0, 0]
                #pop_In = self.pop.clone()
                
                
                pop_Out_1 =  self.method_SplitLifeStagesIntoVSPs_By_AgeClass(pop_In)
                str_VSP_Group = globalsSS.VSP_Groups.static_VSP_Group_Age_Class
                
                #Get a list of all the VSPs with individuals
                listVSPs = []
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    boolReportVSPIfEmpty = False
                    listVSPsForStats = objSSAnalysisOperation.method_Get_VSP_List(pop_Out_1, boolReportVSPIfEmpty)
                    boolReportVSPIfEmpty = True
                    listVSPsForReporting = objSSAnalysisOperation.method_Get_VSP_List(pop_Out_1, boolReportVSPIfEmpty)
                                     
#                 pop_Out_2 = self.method_SimStat_LDNe_Reporting_2(pop_Out_1, listVSPs )

              
                pop_Out_2 = self.method_Initialise_Stats_For_VSP_LEVEL_Reporting(pop_Out_1, listVSPsForStats)

                ''' Specify VSPs to output '''
                
                if str_Reporting_Interval == globalsSS.SS_Level_Details.static_Reporting_Interval__Level_Age_Class_VSP_End_Of_Replicate: 
                    self.objSSParametersLocal.listOutputVSPs_VSP_Level_Age_Class_VLF_EOR = listVSPsForReporting
                pass
            
                if str_Reporting_Interval == globalsSS.SS_Level_Details.static_Reporting_Interval__Level_Age_Class_VSP_Post_Fertilization:
                    self.objSSParametersLocal.listOutputVSPs_VSP_Level_Age_Class_VLF_PF = listVSPsForReporting
                pass
                
                ''' Start output '''
                self.method_Output_VSP_LEVEL_Age_Class_VLF_Reporting(pop_Out_2, str_Reporting_Interval, str_VSP_Group)

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass

                
                return True
            
            
            def method_VSP_LEVEL_Life_Stage_VLF_Reporting(self, pop_In, str_Reporting_Interval):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()   
                                    
                ''' Get simuPOP LDNe stats '''
                #listVirtualSubPop = [0, 0]
                #pop_In = self.pop.clone()
                
                
                pop_Out_1 =  self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop_In, False)
                str_VSP_Group = globalsSS.VSP_Groups.static_VSP_Group_Life_Stage
                
                #Get a list of all the VSPs with individuals
                listVSPs = []
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    boolReportVSPIfEmpty = False
                    listVSPsForStats = objSSAnalysisOperation.method_Get_VSP_List(pop_Out_1, boolReportVSPIfEmpty)
                    boolReportVSPIfEmpty = True
                    listVSPsForReporting = objSSAnalysisOperation.method_Get_VSP_List(pop_Out_1, boolReportVSPIfEmpty)
                                     
#                 pop_Out_2 = self.method_SimStat_LDNe_Reporting_2(pop_Out_1, listVSPs )

                #DEBUG_ON
                if self.objSSParametersLocal.intCurrentReplicate == 2:
                    self.obj_Log_Debug_Display.debug('Here')
                #DEBUG_OFF                  
                pop_Out_2 = self.method_Initialise_Stats_For_VSP_LEVEL_Reporting(pop_Out_1, listVSPsForStats)


                ''' Specify VSPs to output '''
                
                if str_Reporting_Interval == globalsSS.SS_Level_Details.static_Reporting_Interval__Level_Life_Stage_VSP_End_Of_Replicate: 
                    self.objSSParametersLocal.listOutputVSPs_VSP_Level_Life_Stage_VLF_EOR = listVSPsForReporting
                pass
            
                if str_Reporting_Interval == globalsSS.SS_Level_Details.static_Reporting_Interval__Level_Life_Stage_VSP_Post_Fertilization:
                    self.objSSParametersLocal.listOutputVSPs_VSP_Level_Life_Stage_VLF_PF = listVSPsForReporting
                pass
                
                ''' Start output '''
                self.method_Output_VSP_LEVEL_Life_Stage_VLF_Reporting(pop_Out_2, str_Reporting_Interval, str_VSP_Group)

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass

                
                return True

            '''
            ------------------------
            LEVEL Output
            ------------------------
            '''
            
            def method_Output_SIM_LEVEL_SLF_Reporting(self, pop_In):

                if self.objSSParametersLocal.boolBurnIn: # and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    #DEBUG_ON
                    #Stops run of this function
                    #return True
                    #DEBUG_OFF

                    #intSubPop=0
                    
                    #listOutputDestinations = list(self.objSSParametersLocal.listOutputDestinations_ILF_PopulationIndividualsDump)
                    listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Sim_Level_SLF
                    listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_ILF_PopulationIndividualsDump
                    
                    #Check if only specific VSPs are required.  None assumes that ALL ARE REQUIRED.
                    if listVirtSubPopsToOutput == []:
                      
                        intNumberVirtualSubPops = self.pop.numVirtualSubPop()
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            #All are required. Create list of all VSPs to process
                            listCurrentVSP =[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)]
                            listSingleVirtualSubPop = listCurrentVSP[0]
                            listVirtSubPopsToOutput.append(listSingleVirtualSubPop)
                            pass
                        pass
                    
                    with SSOutputHandler() as SSOutputOperation:
                        SSOutputOperation.method_Output_SIM_LEVEL_To_SLF_Files(self.objSSParametersLocal, pop_In, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
                
                return True


            def method_Output_BATCH_LEVEL_BLF_Reporting(self, pop_In):

                if self.objSSParametersLocal.boolBurnIn: # and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    #DEBUG_ON
                    #Stops run of this function
                    #return True
                    #DEBUG_OFF

                    #intSubPop=0
                    
                    #listOutputDestinations = list(self.objSSParametersLocal.listOutputDestinations_ILF_PopulationIndividualsDump)
                    listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Batch_Level_BLF
                    listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_ILF_PopulationIndividualsDump
                    
                    #Check if only specific VSPs are required.  None assumes that ALL ARE REQUIRED.
                    if listVirtSubPopsToOutput == []:
                      
                        intNumberVirtualSubPops = self.pop.numVirtualSubPop()
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            #All are required. Create list of all VSPs to process
                            listCurrentVSP =[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)]
                            listSingleVirtualSubPop = listCurrentVSP[0]
                            listVirtSubPopsToOutput.append(listSingleVirtualSubPop)
                            pass
                        pass
                    
                    with SSOutputHandler() as SSOutputOperation:
                        SSOutputOperation.method_Output_BATCH_LEVEL_To_BLF_Files(self.objSSParametersLocal, pop_In, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
                
                return True


            def method_Output_REPLICATE_LEVEL_RLF_Reporting(self, pop_In, str_Reporting_Interval):

                if self.objSSParametersLocal.boolBurnIn: # and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    #DEBUG_ON
                    #Stops run of this function
                    #return True
                    #DEBUG_OFF

                    #intSubPop=0
                    
                    #listOutputDestinations = list(self.objSSParametersLocal.listOutputDestinations_ILF_PopulationIndividualsDump)
                    if str_Reporting_Interval == globalsSS.SS_Level_Details.static_Reporting_Interval__Level_REPLICATE_End_Of_Replicate:
                        listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Replicate_Level_RLF_End_Of_Replicate
                        listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputSPs_SP_Level_RLF_End_Of_Replicate
                    pass
                
                    if str_Reporting_Interval == globalsSS.SS_Level_Details.static_Reporting_Interval__Level_REPLICATE_Post_Fertilization:
                        listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Replicate_Level_RLF_Post_Fertilization
                        listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputSPs_SP_Level_RLF_Post_Fertilization
                    pass
                    
                    with SSOutputHandler() as SSOutputOperation:
                        SSOutputOperation.method_Output_REPLICATE_LEVEL_To_RLF_Files(self.objSSParametersLocal, pop_In, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
                
                return True


            def method_Output_VSP_LEVEL_Age_Class_VLF_Reporting(self, pop_In, str_Reporting_Interval, str_VSP_Group):

                if self.objSSParametersLocal.boolBurnIn: # and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    #DEBUG_ON
                    #Stops run of this function
                    #return True
                    #DEBUG_OFF

                    #intSubPop=0
                    
                    #listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_VSP_Level_Age_Class_VLF
                    #listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_VSP_Level_Age_Class_VLF

                    if str_Reporting_Interval == globalsSS.SS_Level_Details.static_Reporting_Interval__Level_Age_Class_VSP_End_Of_Replicate: 
                        listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_VSP_Level_Age_Class_VLF_EOR
                        listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_VSP_Level_Age_Class_VLF_EOR
                    pass
                
                    if str_Reporting_Interval == globalsSS.SS_Level_Details.static_Reporting_Interval__Level_Age_Class_VSP_Post_Fertilization:
                        listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_VSP_Level_Age_Class_VLF_PF
                        listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_VSP_Level_Age_Class_VLF_PF
                    pass

#                     
#                     #Check if only specific VSPs are required.  None assumes that ALL ARE REQUIRED.
#                     if listVirtSubPopsToOutput == []:
#                       
#                         intNumberVirtualSubPops = self.pop_In.numVirtualSubPop()
#                         for intVirtualSubPop in range(0, intNumberVirtualSubPops):
#                             #All are required. Create list of all VSPs to process
#                             listCurrentVSP =[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)]
#                             listSingleVirtualSubPop = listCurrentVSP[0]
#                             listVirtSubPopsToOutput.append(listSingleVirtualSubPop)
#                             pass
#                         pass
                    
                    with SSOutputHandler() as SSOutputOperation:
                        SSOutputOperation.method_Output_VSP_LEVEL_To_VLF_Files(self.objSSParametersLocal, pop_In, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput, str_VSP_Group)
                
                return True


            def method_Output_VSP_LEVEL_Life_Stage_VLF_Reporting(self, pop_In, str_Reporting_Interval, str_VSP_Group):

                if self.objSSParametersLocal.boolBurnIn: # and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    #DEBUG_ON
                    #Stops run of this function
                    #return True
                    #DEBUG_OFF

                    #intSubPop=0
                    
                    #listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_VSP_Level_Life_Stage_VLF
                    #listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_VSP_Level_Life_Stage_VLF

                    if str_Reporting_Interval == globalsSS.SS_Level_Details.static_Reporting_Interval__Level_Life_Stage_VSP_End_Of_Replicate:
                        listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_VSP_Level_Life_Stage_VLF_EOR
                        listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_VSP_Level_Life_Stage_VLF_EOR
                    pass
                
                    if str_Reporting_Interval == globalsSS.SS_Level_Details.static_Reporting_Interval__Level_Life_Stage_VSP_Post_Fertilization:
                        listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_VSP_Level_Life_Stage_VLF_PF
                        listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_VSP_Level_Life_Stage_VLF_PF
                    pass
                    
#                     #Check if only specific VSPs are required.  None assumes that ALL ARE REQUIRED.
#                     if listVirtSubPopsToOutput == []:
#                        
#                         intNumberVirtualSubPops = self.pop_In.numVirtualSubPop()
#                         for intVirtualSubPop in range(0, intNumberVirtualSubPops):
#                             #All are required. Create list of all VSPs to process
#                             listCurrentVSP =[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)]
#                             listSingleVirtualSubPop = listCurrentVSP[0]
#                             listVirtSubPopsToOutput.append(listSingleVirtualSubPop)
#                             pass
#                         pass
                    
                    with SSOutputHandler() as SSOutputOperation:
                        SSOutputOperation.method_Output_VSP_LEVEL_To_VLF_Files(self.objSSParametersLocal, pop_In, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput, str_VSP_Group)
                
                return True

            
            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # Mortality Stats
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''

            def method_Mortality_PF_Logging(self, int_Mortality_Type):

                '''
                --------------------------
                Get the stats
                --------------------------
                '''
                dict_Results = OrderedDict()

                if self.objSSParametersLocal.bool_Overlapping_Gens_Simulation:
                    int_Sim_Pop_Size = self.objSSParametersLocal.popnSize
                else:
                    int_Sim_Pop_Size = self.objSSParametersLocal.popnSize / 2 #For Discrete gens only
                pass
            
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = self.objSSParametersLocal.strUniqueRunID 
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = self.objSSParametersLocal.strRunSpecificUserDefinedFolder
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = self.objSSParametersLocal.bool_Overlapping_Gens_Simulation
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = int_Sim_Pop_Size
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = self.objSSParametersLocal.bool_Allow_Mutation
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = self.objSSParametersLocal.float_Mutation_Rate
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = self.objSSParametersLocal.nLoci
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = self.objSSParametersLocal.intBatches
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = self.objSSParametersLocal.intReplicates
                
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = self.objSSParametersLocal.boolBurnIn
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = self.objSSParametersLocal.intCurrentBatch
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = self.objSSParametersLocal.intCurrentReplicate
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = self.objSSParametersLocal.intSimulationCurrentMonth//12
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = self.objSSParametersLocal.intYearCurrentMonth
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = self.objSSParametersLocal.int_MatingCount_Sim_Total
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = self.objSSParametersLocal.int_MatingCount_Replicate_Total


                int_Current_Replicate_Mating_Count = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                int_Mating_Mortality_Starts__UnNat = self.objSSParametersLocal.dict_Mortality_Application_Specs_By_Sex__UnNATURAL[globalsSS.MortalityApplication.static_str_Mating_Mortlity_Starts__UnNat]['Male']
                
                
                dict_Multiline_Results = OrderedDict()
#                 dict_Mortality_NATURAL = self.objSSParametersLocal.odictPostNATURALMortalityNumIndividualsKilledPerAgeClass
#                 dict_Survivorship_NATURAL = self.objSSParametersLocal.odictPostNATURALMortalityNumIndividualsSurvivingPerAgeClass
#                 dict_Mortality_UnNATURAL = self.objSSParametersLocal.odictPostUNNATURALMortalityNumIndividualsKilledPerAgeClass
#                 dict_Survivorship_UnNATURAL = self.objSSParametersLocal.odictPostUNNATURALMortalityNumIndividualsSurvivingPerAgeClass
                dict_Mortality_COMBINED = self.objSSParametersLocal.odictPostCOMBINEDMortalityNumIndividualsKilledPerAgeClass
                dict_Mortality_COMBINED = OrderedDict(sorted(dict_Mortality_COMBINED.items(), key=lambda x: x[0]))
                #dict_Survivorship_COMBINED = self.objSSParametersLocal.odictPostCOMBINEDMortalityNumIndividualsSurvivingPerAgeClass
                
                #int_Line = 0

#                 int_Line_Total = len(dict_Mortality_COMBINED['Male'])*2
#                 for int_Line in range(0, int_Line_Total):
#                     
#                     dict_Multiline_Results[int_Line] = {key:value for key,value in dict_Results.items()}
                int_Line = 0    
                for key_Sex, dict_Mortality_For_Sex in dict_Mortality_COMBINED.items():
                                   
                    for key_Age, value_Indiv_Count in dict_Mortality_For_Sex.items():
                        dict_Multiline_Results[int_Line] = {key:value for key,value in dict_Results.items()} 
                        dict_Multiline_Results[int_Line][globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = key_Sex
                        dict_Multiline_Results[int_Line]['Age_In_Months'] = int(key_Age)
                        dict_Multiline_Results[int_Line]['Pre_Mortality_Num_In_Age'] = self.objSSParametersLocal.odictPreMortalityNumIndividualsPerAgeClass[key_Sex][key_Age]
                        dict_Multiline_Results[int_Line]['NAT_Survival_Rate'] = self.objSSParametersLocal.odictRates_Of_Survival_NATURAL_BySex_ByAge[key_Sex][key_Age]
                        dict_Multiline_Results[int_Line]['NAT_Indivs_Died'] = self.objSSParametersLocal.odictPostNATURALMortalityNumIndividualsKilledPerAgeClass[key_Sex][key_Age]
                        dict_Multiline_Results[int_Line]['NAT_Indivs_Survived'] = self.objSSParametersLocal.odictPostNATURALMortalityNumIndividualsSurvivingPerAgeClass[key_Sex][key_Age]
                        dict_Multiline_Results[int_Line]['UNN_Survival_Rate'] = self.objSSParametersLocal.odictRates_Of_Survival_UnNATURAL_BySex_ByAge[key_Sex][key_Age]
                        if self.objSSParametersLocal.boolAllowUnNATURALMortality and int_Current_Replicate_Mating_Count >= int_Mating_Mortality_Starts__UnNat:
                            dict_Multiline_Results[int_Line]['UNN_Indivs_Died'] = self.objSSParametersLocal.odictPostUNNATURALMortalityNumIndividualsKilledPerAgeClass[key_Sex][key_Age]
                            dict_Multiline_Results[int_Line]['UNN_Indivs_Survived'] = self.objSSParametersLocal.odictPostUNNATURALMortalityNumIndividualsSurvivingPerAgeClass[key_Sex][key_Age]
                        else:
                            dict_Multiline_Results[int_Line]['UNN_Indivs_Died'] = 0
                            dict_Multiline_Results[int_Line]['UNN_Indivs_Survived'] = 0
                        pass
                        dict_Multiline_Results[int_Line]['COM_Survival_Rate'] = self.objSSParametersLocal.odictRates_Of_Survival_COMBINED_BySex_ByAge[key_Sex][key_Age]
                        dict_Multiline_Results[int_Line]['COM_Indivs_Died'] = value_Indiv_Count
                        dict_Multiline_Results[int_Line]['COM_Indivs_Survived'] = self.objSSParametersLocal.odictPostCOMBINEDMortalityNumIndividualsSurvivingPerAgeClass[key_Sex][key_Age]
                        int_Line += 1
                    pass
                    
                pass
                    #int_Line += 1
                pass
                pass

                '''
                --------------------------
                Log the results
                --------------------------
                '''
                str_Results_1 = self.objSSParametersLocal.strUniqueRunID
                if (self.objSSParametersLocal.intSimulationCurrentMonth / 12) == 1:
                    str_Heading_1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
                    str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Mortality_PF_Results

                    self.obj_Logging__Mortality_PF.func_Log_MultiLine_Results_Header(self.obj_Results_Log__Mortality_PF, str_Heading_1, str_Heading_Prefix_1, dict_Multiline_Results)
                    self.obj_Logging__Mortality_PF.func_Log_MultiLine_Results_Detail(str_Results_1, self.obj_Results_Log__Mortality_PF, dict_Multiline_Results)
                else:
                    self.obj_Logging__Mortality_PF.func_Log_MultiLine_Results_Detail(str_Results_1, self.obj_Results_Log__Mortality_PF, dict_Multiline_Results)
                pass
#                 str_Results_1 = self.objSSParametersLocal.strUniqueRunID
#                 
#                 if self.objSSParametersLocal.boolBurnIn == True and self.objSSParametersLocal.intSimulationCurrentMonth == self.objSSParametersLocal.intMatingCalenderMonth - 1:
#                     str_Heading_1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
#                     str_Heading_Prefix_1 = globalsSS.Embryo_Offspring_Parent_Ne_Stats.static_Label_Gen_File
#                     self.obj_Logging__EPNS.func_Log_Results_Header(self.obj_Results_Log__EPNS, str_Heading_1, str_Heading_Prefix_1, dict_Results)
#                     self.obj_Logging__EPNS.func_Log_Results_Detail(str_Results_1, self.obj_Results_Log__EPNS, dict_Results)
#                 else:
#                     self.obj_Logging__EPNS.func_Log_Results_Detail(str_Results_1, self.obj_Results_Log__EPNS, dict_Results)
#                 pass

                return True

            def method_Mortality_PF_Logging_OLD(self, int_Mortality_Type):

                '''
                --------------------------
                Get the stats
                --------------------------
                '''
                dict_Results = OrderedDict()

                if self.objSSParametersLocal.bool_Overlapping_Gens_Simulation:
                    int_Sim_Pop_Size = self.objSSParametersLocal.popnSize
                else:
                    int_Sim_Pop_Size = self.objSSParametersLocal.popnSize / 2 #For Discrete gens only
                pass
            
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = self.objSSParametersLocal.strUniqueRunID 
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = self.objSSParametersLocal.strRunSpecificUserDefinedFolder
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = self.objSSParametersLocal.bool_Overlapping_Gens_Simulation
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = int_Sim_Pop_Size
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = self.objSSParametersLocal.bool_Allow_Mutation
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = self.objSSParametersLocal.float_Mutation_Rate
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = self.objSSParametersLocal.nLoci
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = self.objSSParametersLocal.intBatches
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = self.objSSParametersLocal.intReplicates
                
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = self.objSSParametersLocal.boolBurnIn
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = self.objSSParametersLocal.intCurrentBatch
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = self.objSSParametersLocal.intCurrentReplicate
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = self.objSSParametersLocal.intSimulationCurrentMonth//12
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = self.objSSParametersLocal.intYearCurrentMonth
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = self.objSSParametersLocal.int_MatingCount_Sim_Total
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                
                dict_Multiline_Results = OrderedDict()
                #dict_Mortality = OrderedDict()
                #dict_Survivorship = OrderedDict()
#                 if int_Mortality_Type == globalsSS.MortalitySource.static_intMortalityType_NATURAL:
#                     str_Mortality_Type = globalsSS.MortalitySource.static_strMortalityType_NATURAL
#                     #dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mortality_Type] = globalsSS.MortalitySource.static_strMortalityType_NATURAL
#                     dict_Mortality = 
#                 elif int_Mortality_Type == globalsSS.MortalitySource.static_intMortalityType_UnNATURAL:
#                     str_Mortality_Type = globalsSS.MortalitySource.static_strMortalityType_UnNATURAL
#                     #dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mortality_Type] = globalsSS.MortalitySource.static_strMortalityType_UnNATURAL
#                 elif int_Mortality_Type == globalsSS.MortalitySource.static_intMortalityType_COMBINED:
#                     str_Mortality_Type = globalsSS.MortalitySource.static_strMortalityType_COMBINED
#                     #dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mortality_Type] = globalsSS.MortalitySource.static_strMortalityType_COMBINED
#                 pass
                
                int_Line = 0
                for str_Sex in self.objSSParametersLocal.listSexes:

                    if int_Mortality_Type == globalsSS.MortalitySource.static_intMortalityType_NATURAL:
                        str_Mortality_Type = globalsSS.MortalitySource.static_strMortalityType_NATURAL
                        #dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mortality_Type] = globalsSS.MortalitySource.static_strMortalityType_NATURAL
                        dict_Mortality = self.objSSParametersLocal.odictPostNATURALMortalityNumIndividualsKilledPerAgeClass[str_Sex]
                        dict_Mortality = OrderedDict(sorted(dict_Mortality.items(), key=lambda x: x[0]))
                        dict_Survivorship = self.objSSParametersLocal.odictPostNATURALMortalityNumIndividualsSurvivingPerAgeClass[str_Sex]
                        #dict_Survivorship = OrderedDict(sorted(dict_Survivorship.items(), key=lambda x: x[0]))
                    elif int_Mortality_Type == globalsSS.MortalitySource.static_intMortalityType_UnNATURAL:
                        str_Mortality_Type = globalsSS.MortalitySource.static_strMortalityType_UnNATURAL
                        #dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mortality_Type] = globalsSS.MortalitySource.static_strMortalityType_UnNATURAL
                        dict_Mortality = self.objSSParametersLocal.odictPostUNNATURALMortalityNumIndividualsKilledPerAgeClass[str_Sex]
                        dict_Mortality = OrderedDict(sorted(dict_Mortality.items(), key=lambda x: x[0]))
                        dict_Survivorship = self.objSSParametersLocal.odictPostUNNATURALMortalityNumIndividualsSurvivingPerAgeClass[str_Sex]
                        #dict_Survivorship = OrderedDict(sorted(dict_Survivorship.items(), key=lambda x: x[0]))
                    elif int_Mortality_Type == globalsSS.MortalitySource.static_intMortalityType_COMBINED:
                        str_Mortality_Type = globalsSS.MortalitySource.static_strMortalityType_COMBINED
                        #dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mortality_Type] = globalsSS.MortalitySource.static_strMortalityType_COMBINED
                        dict_Mortality = self.objSSParametersLocal.odictPostCOMBINEDMortalityNumIndividualsKilledPerAgeClass[str_Sex]
                        dict_Mortality = OrderedDict(sorted(dict_Mortality.items(), key=lambda x: x[0]))
                        dict_Survivorship = self.objSSParametersLocal.odictPostCOMBINEDMortalityNumIndividualsSurvivingPerAgeClass[str_Sex]
                        #dict_Survivorship = OrderedDict(sorted(dict_Survivorship.items(), key=lambda x: x[0]))                        
                    pass                    
                  
                    for key_Age, value_Indiv_Count in dict_Mortality.items():
                        dict_Multiline_Results[int_Line] = {key:value for key,value in dict_Results.items()}
                        dict_Multiline_Results[int_Line][globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sex] = str_Sex
                        dict_Multiline_Results[int_Line][globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mortality_Type] = str_Mortality_Type
                        dict_Multiline_Results[int_Line]['Age_In_Months'] = int(key_Age)
                        dict_Multiline_Results[int_Line]['Indivs_Died'] = value_Indiv_Count
                        dict_Multiline_Results[int_Line]['Indivs_Survived'] = dict_Survivorship[key_Age]
                        dict_Multiline_Results[int_Line]['Pre_Mortality_Num_In_Age'] = self.objSSParametersLocal.odictPreMortalityNumIndividualsPerAgeClass[str_Sex][key_Age]
                        int_Line += 1
                        pass
                    pass
                pass

                '''
                --------------------------
                Log the results
                --------------------------
                '''
                str_Results_1 = self.objSSParametersLocal.strUniqueRunID
                if (self.objSSParametersLocal.intSimulationCurrentMonth / 12) == 1:
                    str_Heading_1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
                    str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__Prefix__Mortality_PF_Results

                    self.obj_Logging__Mortality_PF.func_Log_MultiLine_Results_Header(self.obj_Results_Log__Mortality_PF, str_Heading_1, str_Heading_Prefix_1, dict_Multiline_Results)
                    self.obj_Logging__Mortality_PF.func_Log_MultiLine_Results_Detail(str_Results_1, self.obj_Results_Log__Mortality_PF, dict_Multiline_Results)
                else:
                    self.obj_Logging__Mortality_PF.func_Log_MultiLine_Results_Detail(str_Results_1, self.obj_Results_Log__Mortality_PF, dict_Multiline_Results)
                pass
#                 str_Results_1 = self.objSSParametersLocal.strUniqueRunID
#                 
#                 if self.objSSParametersLocal.boolBurnIn == True and self.objSSParametersLocal.intSimulationCurrentMonth == self.objSSParametersLocal.intMatingCalenderMonth - 1:
#                     str_Heading_1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
#                     str_Heading_Prefix_1 = globalsSS.Embryo_Offspring_Parent_Ne_Stats.static_Label_Gen_File
#                     self.obj_Logging__EPNS.func_Log_Results_Header(self.obj_Results_Log__EPNS, str_Heading_1, str_Heading_Prefix_1, dict_Results)
#                     self.obj_Logging__EPNS.func_Log_Results_Detail(str_Results_1, self.obj_Results_Log__EPNS, dict_Results)
#                 else:
#                     self.obj_Logging__EPNS.func_Log_Results_Detail(str_Results_1, self.obj_Results_Log__EPNS, dict_Results)
#                 pass

                return True

           
            
            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # Parent / Offspring Stats
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
           

            def method_Summary_Parent_Offspring_Stats_Reporting(self, pop_In):

                '''
                --------------------------
                Get the stats
                --------------------------
                '''
                dict_Results = OrderedDict()

                if self.objSSParametersLocal.bool_Overlapping_Gens_Simulation:
                    int_Sim_Pop_Size = self.objSSParametersLocal.popnSize
                else:
                    int_Sim_Pop_Size = self.objSSParametersLocal.popnSize / 2 #For Discrete gens only
                pass
            
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = self.objSSParametersLocal.strUniqueRunID 
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = self.objSSParametersLocal.strRunSpecificUserDefinedFolder
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = self.objSSParametersLocal.bool_Overlapping_Gens_Simulation
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = int_Sim_Pop_Size
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = self.objSSParametersLocal.bool_Allow_Mutation
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = self.objSSParametersLocal.float_Mutation_Rate
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = self.objSSParametersLocal.nLoci
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = self.objSSParametersLocal.intBatches
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = self.objSSParametersLocal.intReplicates
                
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = self.objSSParametersLocal.boolBurnIn
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = self.objSSParametersLocal.intCurrentBatch
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = self.objSSParametersLocal.intCurrentReplicate
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = self.objSSParametersLocal.intSimulationCurrentMonth//12
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = self.objSSParametersLocal.intYearCurrentMonth
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = self.objSSParametersLocal.int_MatingCount_Sim_Total
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                
                with SSAnalysisHandler() as obj_SSAnalysis:
#                     
#                                         
#                     intSubPop = globalsSS.SP_SubPops.static_intSP_SubPop_Primary
#                     intVSP = globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo
#                     
                    dict_Results = obj_SSAnalysis.method_Embryo_Offspring_Parent_Ne_Summary_Stats_METHOD_1(pop_In, dict_Results, self.objSSParametersLocal)

                    with SSAnalysisHandler() as objSSAnalysisOperation:
                        intSubPop = globalsSS.SP_SubPops.static_intSP_SubPop_Primary
                        #intVirtualSubPop = globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo
                        intVirtualSubPop = globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo
                                            
                        dictSireOffspringCount = objSSAnalysisOperation.method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(pop_In, intSubPop, intVirtualSubPop)
                        dictDameOffspringCount = objSSAnalysisOperation.method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(pop_In, intSubPop, intVirtualSubPop)
                        
                        listPotentialFemaleParents = self.objSSParametersLocal.listPotentialFemaleParents
                        listPotentialMaleParents = self.objSSParametersLocal.listPotentialMaleParents
                        dictOffspringCount = objSSAnalysisOperation.method_Count_Offspring_PerParent_For_VirtualSubPop(pop_In, dictSireOffspringCount, dictDameOffspringCount, listPotentialMaleParents, listPotentialFemaleParents, intSubPop, intVirtualSubPop)                    
                    
                    dict_Results = obj_SSAnalysis.method_Embryo_Offspring_Parent_Ne_Summary_Stats_METHOD_2(dictSireOffspringCount, dictDameOffspringCount, dictOffspringCount, dict_Results)
                pass
            
                '''
                --------------------------
                Log the results
                --------------------------
                '''
                str_Results_1 = self.objSSParametersLocal.strUniqueRunID
                
                if self.objSSParametersLocal.boolBurnIn == True and self.objSSParametersLocal.intSimulationCurrentMonth == self.objSSParametersLocal.intMatingCalenderMonth - 1:
                    str_Heading_1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
                    str_Heading_Prefix_1 = globalsSS.Embryo_Offspring_Parent_Ne_Stats.static_Label_Gen_File
                    self.obj_Logging__EPNS.func_Log_Results_Header(self.obj_Results_Log__EPNS, str_Heading_1, str_Heading_Prefix_1, dict_Results)
                    self.obj_Logging__EPNS.func_Log_Results_Detail(str_Results_1, self.obj_Results_Log__EPNS, dict_Results)
                else:
                    self.obj_Logging__EPNS.func_Log_Results_Detail(str_Results_1, self.obj_Results_Log__EPNS, dict_Results)
                pass
           
                return True
           
            
            def method_Effective_Parent_Summary_Stats_Reporting(self, pop_In):

                '''
                --------------------------
                Get the stats
                --------------------------
                '''
                dict_Results = OrderedDict()

                str_Source_Unique_Run_Batch_Rep_VSP_ID = self.objSSParametersLocal.strUniqueRunID   
                dict_Results[globalsSS.Ne2_Sampling_Stats.static_Label_Gen_Source_Unique_Run_Batch_Rep_VSP_ID] = str_Source_Unique_Run_Batch_Rep_VSP_ID
 
                
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label] = ''
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = self.objSSParametersLocal.strRunSpecificUserDefinedFolder
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = str(self.objSSParametersLocal.boolBurnIn)
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = self.objSSParametersLocal.intCurrentBatch
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = self.objSSParametersLocal.intCurrentReplicate
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = self.objSSParametersLocal.intSimulationCurrentMonth//12
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = self.objSSParametersLocal.intYearCurrentMonth
                
                with SSAnalysisHandler() as obj_SSAnalysis:
                    dict_Results = obj_SSAnalysis.method_Effective_Parent_Summary_Stats_1(pop_In, dict_Results)
                pass
            
                '''
                --------------------------
                Log the results
                --------------------------
                '''
                str_Results_1 = self.objSSParametersLocal.strUniqueRunID
                
                if self.objSSParametersLocal.boolBurnIn == True and self.objSSParametersLocal.intSimulationCurrentMonth == self.objSSParametersLocal.intMatingCalenderMonth - 1:
                    str_Heading_1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
                    str_Heading_Prefix_1 = globalsSS.Effective_Parents_Stats.static_Label_Gen_File
                    self.obj_Logging__EPS.func_Log_MultiLine_Results_Header(self.obj_Results_Log__EPS, str_Heading_1, str_Heading_Prefix_1, dict_Results)
                    self.obj_Logging__EPS.func_Log_MultiLine_Results_Detail(str_Results_1, self.obj_Results_Log__EPS, dict_Results)
                else:
                    self.obj_Logging__EPS.func_Log_MultiLine_Results_Detail(str_Results_1, self.obj_Results_Log__EPS, dict_Results)
                pass
           
                return True


            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # NE Stats
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
               
            def method_End_Of_SIM_REPLICATE_Reporting_NE_Stats(self, listVSPToReport):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()   
                    
                #self.method_EndOfSim_Reporting_NEStatistics()
                
                '''
                NE Custom 1 STATS
                '''
                '''
                Setup STATs for monitoring
                '''
                #Log finishing datetime and time for SIM run before NE experiments
                self.objSSParametersLocal.dateReplicateRunFinishTime = datetime.now()

                dateTimeRunTime1 = self.objSSParametersLocal.dateReplicateRunFinishTime - self.objSSParametersLocal.dateReplicateRunStartTime
                with SSOutputHandler() as SSOutputOperation:
                    #listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches, self.objSSParametersLocal.outputFileNameSummaryLogAllReps, self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
                    listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches, self.objSSParametersLocal.outputFileNameSummaryLogAllReps, self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
                    SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'SIM Replicate Run Finished: ' + self.objSSParametersLocal.dateReplicateRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
                    SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'SIM Replicate Run took: ' + str(dateTimeRunTime1))

                self.pop = self.method_SplitLifeStagesInto_AgeInMonths_VSPs_By_AgeInMonths(self.pop)
 
#                 dateTestRunStartTime = datetime.now()
#                 
#                 self.method_Reporting_AgeNe_Statistics() 
#                 
#                 dateTestRunFinishTime = datetime.now()
#                 dateTimeRunTime = timedelta()
#                 dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
#                 with SSOutputHandler() as SSOutputOperation:
#                     #listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
#                     SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'AgeNe Stats Reporting Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
#                     SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'AgeNe Stats Reporting took: ' + str(dateTimeRunTime))
#                 
                dateTestRunStartTime = datetime.now()
                
                #Get a list of all the VSPs with individuals
                listVSPsWithIndivs = []
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    listVSPsWithIndivs = objSSAnalysisOperation.method_Get_VSP_List(self.pop)
                
                listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches, self.objSSParametersLocal.outputFileNameSummaryLogAllReps, self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
                SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'EOS Ne Reporting - VSPs with indivs: ' + str(listVSPsWithIndivs))
                SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'EOS Ne Reporting - VSPs to report: ' + str(listVSPToReport))
   
                #Generate the SIMUPOP STATS for the required VSPs
                self.method_Initialise_Stats_For_ILF_Individual_Dump(self.pop, listVSPsWithIndivs)


                dateTestRunFinishTime = datetime.now()
                dateTimeRunTime = timedelta()
                dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
                with SSOutputHandler() as SSOutputOperation:
                    #listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
                    listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches, self.objSSParametersLocal.outputFileNameSummaryLogAllReps, self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
                    SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'ILF Stats Init Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
                    SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'ILF Stats Init took: ' + str(dateTimeRunTime))
                
                dateTestRunStartTime = datetime.now()
                
                #self.method_NEStatistics_Custom_1_Reporting(listVSPsWithIndivs)
                self.method_NEStatistics_Custom_3_Reporting()
                self.method_NEStatistics_Custom_1_Reporting_Manual_Experiments(listVSPsWithIndivs)
                self.method_NEStatistics_Custom_2_Reporting_Auto_Experiments(listVSPToReport)
                
                dateTestRunFinishTime = datetime.now()
                dateTimeRunTime = timedelta()
                dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
                with SSOutputHandler() as SSOutputOperation:
                    #listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
                    SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'NEStatistics Custom 2 Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
                    SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'NEStatistics Custom 2 took: ' + str(dateTimeRunTime))

                #with SSAnalysisHandler() as objSSAnalysisOperation:
                #    objSSAnalysisOperation.method_rpy2_test()


                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass  
            
            '''@profile''' 
            def method_In_Sim_Reporting_NEStatistics(self, listVSPsToExperimentOn):

                #self.method_EndOfSim_Reporting_NEStatistics()
                
                '''
                NE Custom 4 STATS
                '''
                '''
                Setup STATs for monitoring
                '''
                if self.objSSParametersLocal.boolReport_Custom_4 or self.objSSParametersLocal.boolReport_Custom_5:
                    with SSOutputHandler() as SSOutputOperation:
                        listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches, self.objSSParametersLocal.outputFileNameSummaryLogAllReps, self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
                        #
                        SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Gathering MORE Post-Fertilisation Ne Stats', boolIsHeader=True, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
             
                    self.pop = self.method_SplitLifeStagesInto_AgeInMonths_VSPs_By_AgeInMonths(self.pop)
                   
                    #Get a list of all the VSPs with individuals
                    listVSPsWithIndivs = []
                    with SSAnalysisHandler() as objSSAnalysisOperation:
                        listVSPsWithIndivs = objSSAnalysisOperation.method_Get_VSP_List(self.pop)
    
                    listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches, self.objSSParametersLocal.outputFileNameSummaryLogAllReps, self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
                    SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'In Sim Ne Reporting - VSPs with indivs: ' + str(listVSPsWithIndivs))
                    SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'In Sim Ne Reporting - VSPs to experement on: ' + str(listVSPsToExperimentOn))
                        
                    #Generate the SIMUPOP STATS for the required VSPs
                    #self.method_Initialise_Stats_For_ILF_Individual_Dump(self.pop, listVSPsWithIndivs)
                    self.method_SimStat_AlleleFreq_Reporting(self.pop, listVSPsWithIndivs)
                    #self.objSSParametersLocal.boolReportLDNe = True
                    #self.method_SimStat_LDNe_Reporting(self.pop, param=listVSPsWithIndivs),
    
    #                 with SSOutputHandler() as SSOutputOperation:
    #                     listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches, self.objSSParametersLocal.outputFileNameSummaryLogAllReps, self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
    #                     #
    #                     SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Running Post-Fertilisation Ne Experiments (Custom 4)', boolIsHeader=True, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
    
                    self.method_NEStatistics_Custom_4_Reporting_Auto_Experiments(listVSPsToExperimentOn, listVSPsWithIndivs)
    
    #                 with SSOutputHandler() as SSOutputOperation:
    #                     listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches, self.objSSParametersLocal.outputFileNameSummaryLogAllReps, self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
    #                     #
    #                     SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'Running Post-Fertilisation Ne Experiments (Custom 5)', boolIsHeader=True, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
    
                    self.method_NEStatistics_Custom_5_Reporting_Auto_Experiments(listVSPsToExperimentOn, listVSPsWithIndivs)
    
    
                    #dateTestRunFinishTime = datetime.now()
                    #dateTimeRunTime = timedelta()
                    #dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
                    #with SSOutputHandler() as SSOutputOperation:
                        #listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
                        #SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'NEStatistics Custom 4 Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
                        #SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'NEStatistics Custom 4 took: ' + str(dateTimeRunTime))
    
                    pass
                return True


            def method_Reporting_AgeNe_Statistics(self, pop_In):
                
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    #Use manually supplied demographic parameters to calc AgeNe
                    self.objSSParametersLocal.boolUseAgeNeSimParameters = False
                    self.objSSParametersLocal.listOfAgeNeManualObjects = objSSAnalysisOperation.method_AgeNeCalculation(self.objSSParametersLocal)
                    
                    self.methodOutput_outputAgeNeDetailInfo(pop_In, [True, False, self.objSSParametersLocal.listSexes])
                    self.methodOutput_outputAgeNeLifeTablesTotalsInfo(pop_In, [True, False, self.objSSParametersLocal.listSexes])
                    self.methodOutput_outputAgeNeDemographicTablesTotalsInfo(pop_In, [True, False, self.objSSParametersLocal.listSexes])
                    
                    self.methodOutput_outputAgeNeFinalTotalsInfo(pop_In, [True, False, self.objSSParametersLocal.listSexes])


                    #Use SIM supplied demographic parameters to calc AgeNe
                    self.objSSParametersLocal.boolUseAgeNeSimParameters = True
                    
                    self.objSSParametersLocal.listOfAgeNeSimObjects = objSSAnalysisOperation.method_AgeNeCalculation(self.objSSParametersLocal) 

                    self.methodOutput_outputAgeNeDetailInfo(pop_In, [True, False, self.objSSParametersLocal.listSexes])
                    self.methodOutput_outputAgeNeLifeTablesTotalsInfo(pop_In, [True, False, self.objSSParametersLocal.listSexes])
                    self.methodOutput_outputAgeNeDemographicTablesTotalsInfo(pop_In, [True, False, self.objSSParametersLocal.listSexes])
                    
                    self.methodOutput_outputAgeNeFinalTotalsInfo(pop_In, [True, False, self.objSSParametersLocal.listSexes])
                
                    #DEBUG_ON
                    #raw_input('pausing...')
                    #DEBUG_OFF
                pass

            def method_Log_Reporting_AgeNe_EOR_Statistics(self):

                dict_Results = OrderedDict()
                
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = self.objSSParametersLocal.strUniqueRunID 
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = self.objSSParametersLocal.strRunSpecificUserDefinedFolder
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = self.objSSParametersLocal.bool_Overlapping_Gens_Simulation
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = self.objSSParametersLocal.popnSize
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = self.objSSParametersLocal.bool_Allow_Mutation
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = self.objSSParametersLocal.float_Mutation_Rate
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = self.objSSParametersLocal.nLoci
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = self.objSSParametersLocal.intBatches
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = self.objSSParametersLocal.intReplicates
                
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = self.objSSParametersLocal.boolBurnIn
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = self.objSSParametersLocal.intCurrentBatch
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = self.objSSParametersLocal.intCurrentReplicate
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = self.objSSParametersLocal.intSimulationCurrentMonth//12
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = self.objSSParametersLocal.intYearCurrentMonth
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = self.objSSParametersLocal.int_MatingCount_Sim_Total
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    #Use manually supplied demographic parameters to calc AgeNe
                    self.objSSParametersLocal.boolUseAgeNeSimParameters = False
                    self.objSSParametersLocal.listOfAgeNeManualObjects = objSSAnalysisOperation.method_AgeNeCalculation(self.objSSParametersLocal)
                    
                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Man_Details_EOR_Results
                    str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Man_Details_EOR_Results
                    self.method_LogOutput_outputAgeNeDetailInfo(self.pop, [True, False, self.objSSParametersLocal.listSexes, self.obj_Logging__EOR_AgeNe_Man_D, self.obj_Results_Log__EOR_AgeNe_Man_D, str_Heading_Prefix_1, dict_Results])

                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Man_LifeTables_Total_EOR_Results
                    str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Man_LifeTables_Total_EOR_Results
                    self.method_LogOutput_outputAgeNeLifeTableTotals(self.pop, [True, False, self.objSSParametersLocal.listSexes, self.obj_Logging__EOR_AgeNe_Man_LT, self.obj_Results_Log__EOR_AgeNe_Man_LT, str_Heading_Prefix_1, dict_Results])

                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Man_DemographicTables_Total_EOR_Results
                    str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Man_DemographicTables_Total_EOR_Results
                    self.method_LogOutput_outputAgeNeDemographicTableTotals(self.pop, [True, False, self.objSSParametersLocal.listSexes, self.obj_Logging__EOR_AgeNe_Man_DT, self.obj_Results_Log__EOR_AgeNe_Man_DT, str_Heading_Prefix_1, dict_Results])

                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Man_Final_Totals_EOR_Results
                    str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Man_Final_Totals_EOR_Results
                    self.method_LogOutput_outputAgeNeFinalTotals(self.pop, [True, False, self.objSSParametersLocal.listSexes, self.obj_Logging__EOR_AgeNe_Man_FT, self.obj_Results_Log__EOR_AgeNe_Man_FT, str_Heading_Prefix_1, dict_Results])



                    #Use SIM supplied demographic parameters to calc AgeNe
                    self.objSSParametersLocal.boolUseAgeNeSimParameters = True
                    self.objSSParametersLocal.listOfAgeNeSimObjects = objSSAnalysisOperation.method_AgeNeCalculation(self.objSSParametersLocal) 

                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_Details_EOR_Results
                    str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_Details_EOR_Results
                    self.method_LogOutput_outputAgeNeDetailInfo(self.pop, [True, False, self.objSSParametersLocal.listSexes, self.obj_Logging__EOR_AgeNe_Sim_D, self.obj_Results_Log__EOR_AgeNe_Sim_D, str_Heading_Prefix_1, dict_Results])

                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_LifeTables_Total_EOR_Results
                    str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_LifeTables_Total_EOR_Results
                    self.method_LogOutput_outputAgeNeLifeTableTotals(self.pop, [True, False, self.objSSParametersLocal.listSexes, self.obj_Logging__EOR_AgeNe_Sim_LT, self.obj_Results_Log__EOR_AgeNe_Sim_LT, str_Heading_Prefix_1, dict_Results])

                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_DemographicTables_Total_EOR_Results
                    str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_DemographicTables_Total_EOR_Results
                    self.method_LogOutput_outputAgeNeDemographicTableTotals(self.pop, [True, False, self.objSSParametersLocal.listSexes, self.obj_Logging__EOR_AgeNe_Sim_DT, self.obj_Results_Log__EOR_AgeNe_Sim_DT, str_Heading_Prefix_1, dict_Results])

                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_Final_Totals_EOR_Results
                    str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_Final_Totals_EOR_Results
                    self.method_LogOutput_outputAgeNeFinalTotals(self.pop, [True, False, self.objSSParametersLocal.listSexes, self.obj_Logging__EOR_AgeNe_Sim_FT, self.obj_Results_Log__EOR_AgeNe_Sim_FT, str_Heading_Prefix_1, dict_Results])
              
                pass

            def method_Log_Reporting_AgeNe_PF_Statistics(self, bool_Header):

                dict_Results = OrderedDict()
                
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Unique_Run_ID] = self.objSSParametersLocal.strUniqueRunID 
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder] = self.objSSParametersLocal.strRunSpecificUserDefinedFolder
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp] = self.objSSParametersLocal.bool_Overlapping_Gens_Simulation
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size] = self.objSSParametersLocal.popnSize
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation] = self.objSSParametersLocal.bool_Allow_Mutation
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate] = self.objSSParametersLocal.float_Mutation_Rate
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci] = self.objSSParametersLocal.nLoci
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus] = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches] = self.objSSParametersLocal.intBatches
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates] = self.objSSParametersLocal.intReplicates
                
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In] = self.objSSParametersLocal.boolBurnIn
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch] = self.objSSParametersLocal.intCurrentBatch
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate] = self.objSSParametersLocal.intCurrentReplicate
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year] = self.objSSParametersLocal.intSimulationCurrentMonth//12
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month] = self.objSSParametersLocal.intYearCurrentMonth
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total] = self.objSSParametersLocal.int_MatingCount_Sim_Total
                dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total] = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                
                with SSAnalysisHandler() as objSSAnalysisOperation:

                    #Use SIM supplied demographic parameters to calc AgeNe
                    self.objSSParametersLocal.boolUseAgeNeSimParameters = True
                    self.objSSParametersLocal.listOfAgeNeSimObjects = objSSAnalysisOperation.method_AgeNeCalculation(self.objSSParametersLocal) 

                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_Details_PF_Results
                    str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_Details_PF_Results
                    self.method_LogOutput_outputAgeNeDetailInfo(self.pop, [bool_Header, False, self.objSSParametersLocal.listSexes, self.obj_Logging__PF_AgeNe_Sim_D, self.obj_Results_Log__PF_AgeNe_Sim_D, str_Heading_Prefix_1, dict_Results])

                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_LifeTables_Total_PF_Results
                    str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_LifeTables_Total_PF_Results
                    self.method_LogOutput_outputAgeNeLifeTableTotals(self.pop, [bool_Header, False, self.objSSParametersLocal.listSexes, self.obj_Logging__PF_AgeNe_Sim_LT, self.obj_Results_Log__PF_AgeNe_Sim_LT, str_Heading_Prefix_1, dict_Results])

                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_DemographicTables_Total_PF_Results
                    str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_DemographicTables_Total_PF_Results
                    self.method_LogOutput_outputAgeNeDemographicTableTotals(self.pop, [bool_Header, False, self.objSSParametersLocal.listSexes, self.obj_Logging__PF_AgeNe_Sim_DT, self.obj_Results_Log__PF_AgeNe_Sim_DT, str_Heading_Prefix_1, dict_Results])

                    dict_Results[globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category] = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_Final_Totals_PF_Results
                    str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname__AgeNe_Sim_Final_Totals_PF_Results
                    self.method_LogOutput_outputAgeNeFinalTotals(self.pop, [bool_Header, False, self.objSSParametersLocal.listSexes, self.obj_Logging__PF_AgeNe_Sim_FT, self.obj_Results_Log__PF_AgeNe_Sim_FT, str_Heading_Prefix_1, dict_Results])
              
                pass

            def method_Update_Sim_AgeNe_Survivors_Per_Age_Class_Stats(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass                
                    
                #DEBUG_ON
                int_Current_Replicate_Mating_Count = self.objSSParametersLocal.int_MatingCount_Replicate_Total
                if int_Current_Replicate_Mating_Count == 77:
                    self.obj_Log_Debug_Display.debug('int_Current_Replicate_Mating_Count == 77')
                pass
                #DEBUG_OF 

                self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year = OrderedDict()
                                                
                for strSex, dictAgeClassSurvivors in self.objSSParametersLocal.odictPostCOMBINEDMortalityNumIndividualsSurvivingPerAgeClass.items():
                    
                    for intAgeInMonths, intSurvivors in dictAgeClassSurvivors.iteritems():
#                         '''
#                         Add 12 monthes to each age class
#                         '''                             
#                         intAgeInMonths = intAgeInMonths + 12
                           
                        intAgeInYears = intAgeInMonths / 12
                        floatSurvivors = float(intSurvivors)
                        dictNewValues = {intAgeInYears:floatSurvivors}
                        if strSex in self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year:
                            self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year[strSex].update(dictNewValues)
                        else:
                            self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year[strSex] = dictNewValues
                    pass  
                    #Always attempt to add 1st value    
                    if 0 in self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year[strSex]:
                            pass
                    else:
                        floatN1NewbornsbySex = self.objSSParametersLocal.odictAgeNe_Sim_N1_Newborns_Per_Sex_Per_Year[strSex][1]
                        dictNewValues = {0:floatN1NewbornsbySex}
                        if strSex in self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year:
                            self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year[strSex].update(dictNewValues)
                        else:
                            self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year[strSex] = dictNewValues
                        pass
                    pass


                ''' End of func DEBUG '''
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                        self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + 'AgeNe Stat: odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year')
                        for str_Sex, value in self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year.iteritems():
                            self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(value).values()),2)) + ' ; Values: ' + str(value)) 
                        pass
                    pass
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
                 
                return True
            
            def method_Update_Sim_AgeNe_Survivors_Per_Age_Class_Stats_OLD(self):

                self.method_Combine_Survivor_Numbers()
                                
                #for strSex, dictAgeClassSurvivors in self.objSSParametersLocal.odictPostNATURALMortalityNumIndividualsSurvivingPerAgeClass.items():
                for strSex, dictAgeClassSurvivors in self.objSSParametersLocal.odictPostCOMBINEDMortalityNumIndividualsSurvivingPerAgeClass.items():
                    
                    for intAgeInMonths, intSurvivors in dictAgeClassSurvivors.iteritems():                             
                    
                        intAgeInYears = intAgeInMonths / 12
                        floatSurvivors = float(intSurvivors)
                        dictNewValues = {intAgeInYears:floatSurvivors}
                        if strSex in self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year:
                            self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year[strSex].update(dictNewValues)
                        else:
                            self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year[strSex] = dictNewValues
                    pass  
                    #Always attempt to add 1st value    
                    if 0 in self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year[strSex]:
                            pass
                    else:
                        #floatN1NewbornsbySex = self.objSSParametersLocal.intAgeNe_Sim_N1_Newborns_PREDICTED // 2
                        floatN1NewbornsbySex = self.objSSParametersLocal.intAgeNe_Sim_N1_Newborns // 2
                        dictNewValues = {0:floatN1NewbornsbySex}
                        if strSex in self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year:
                            self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year[strSex].update(dictNewValues)
                        else:
                            self.objSSParametersLocal.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year[strSex] = dictNewValues
                        pass
                    pass

                pass

            '''@profile'''
            def method_AgeNe_PF_Stats_Gathering(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass
                            
                '''
                ~~~~~~~~~~~~~~~
                Split the pop the right way
                ~~~~~~~~~~~~~~~
                '''                
                pop_In = self.method_SplitLifeStagesInto_AgeInMonths_VSPs_By_AgeInMonths(pop_In)
                
                '''
                ~~~~~~~~~~~~~~~
                Update Birth Rates - bx
                ~~~~~~~~~~~~~~~
                '''                
                self.method_Update_Sim_Birth_Rate_Stats(pop_In)

                '''
                ~~~~~~~~~~~~~~~
                Update Survivorship Rates - sx
                ~~~~~~~~~~~~~~~
                '''
                self.method_Update_AgeNe_Survival_Rates__sx()

                '''
                ~~~~~~~~~~~~~~~
                Update Newborns - N1
                ~~~~~~~~~~~~~~~
                '''
                #self.method_Update_VSP_Size_by_Sex_Stats(pop_In)
                #self.method_Update_AgeClass_Size_by_SexStats(self.objSSParametersLocal.odictVSP_Sizes_Per_Sex)
                self.method_Update_AgeNe_Newborns_Per_Age__N1(pop_In)
           
                '''
                ~~~~~~~~~~~~~~~
                Update Survivor Numbers - Nx
                ~~~~~~~~~~~~~~~
                '''                
                #Must be after N1 is assigned
                self.method_Update_Sim_AgeNe_Survivors_Per_Age_Class_Stats()


                ''' End of func DEBUG '''
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
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
                
                return True

            def method_Update_AgeNe_Newborns_Per_Age__N1(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  

                #DEBUG_ON
                #with SSAnalysisHandler() as obj_Analysis:
                #    odictVSPSizes = obj_Analysis.method_Get_VSP_Sizes(pop_In, False)
                #pass
                #DEBUG_OFF
                
                pop_sample_split = self.method_Split_By_Sex_Then_By_AgeInMonths_VSPs(pop_In)

                intMaxAgeInMonthsAdjusted = (self.objSSParametersLocal.maxAge*12+2)
                int_N1_Male = pop_sample_split.subPopSize((0,1))
                int_N1_Female = pop_sample_split.subPopSize((0,intMaxAgeInMonthsAdjusted))
                
                #DEBUG_ON
                #with SSAnalysisHandler() as obj_Analysis:
                #    odictVSPSizes = obj_Analysis.method_Get_VSP_Sizes(pop_sample_split, True)
                #pass
                #DEBUG_OFF
                ''' Define the Male Sex ratio '''
                #decAgeNe_N1_Male_Sex_Ratio = Decimal(int_N1_Male) / (Decimal(int_N1_Female) + Decimal(int_N1_Male))
                decAgeNe_N1_Male_Sex_Ratio = float(int_N1_Male) / (float(int_N1_Female) + float(int_N1_Male))
                self.objSSParametersLocal.floatAgeNe_Sim_N1_Male_Sex_Ratio = decAgeNe_N1_Male_Sex_Ratio
                self.objSSParametersLocal.floatAgeNe_Manual_N1_Male_Sex_Ratio = decAgeNe_N1_Male_Sex_Ratio

                '''
                ----------------------------
                AgeNe Sim N1 per Sex
                NOTE: This scheme uses the simulation last mating to set the N1 number of offspring
                ----------------------------
                '''
                
                self.objSSParametersLocal.intAgeNe_Sim_N1_Newborns = 0
                dictAgeValuesPerSex = OrderedDict()
                for str_Sex in self.objSSParametersLocal.listSexes:
                    dictAgeValuesPerSex[str_Sex] = OrderedDict()
                    intAgeNe_N1_Newborns_By_Sex = 0
                    for intAge in range(1, self.objSSParametersLocal.intAgeNe_Sim_Max_Age+2):
                        if str_Sex == globalsSS.SexConstants.static_stringSexMale:
                            intAgeNe_N1_Newborns_By_Sex = int_N1_Male
                        else:
                            intAgeNe_N1_Newborns_By_Sex = int_N1_Female
                        pass
                        dictAgeValuesPerSex[str_Sex][intAge] = intAgeNe_N1_Newborns_By_Sex
                    pass
                    self.objSSParametersLocal.intAgeNe_Sim_N1_Newborns += intAgeNe_N1_Newborns_By_Sex
                pass
                self.objSSParametersLocal.odictAgeNe_Sim_N1_Newborns_Per_Sex_Per_Year = dictAgeValuesPerSex

                '''
                ----------------------------
                AgeNe MANUAL N1 per Sex
                NOTE: This scheme uses the simulation last mating to set the N1 number of offspring
                ----------------------------
                '''
                self.objSSParametersLocal.intAgeNe_Manual_N1_Newborns = 0
                dictAgeValuesPerSex = OrderedDict()
                for str_Sex in self.objSSParametersLocal.listSexes:
                    dictAgeValuesPerSex[str_Sex] = OrderedDict()
                    intAgeNe_N1_Newborns_By_Sex = 0
                    for intAge in range(1, self.objSSParametersLocal.intAgeNe_Sim_Max_Age+2):
                        if str_Sex == globalsSS.SexConstants.static_stringSexMale:
                            intAgeNe_N1_Newborns_By_Sex = int_N1_Male
                        else:
                            intAgeNe_N1_Newborns_By_Sex = int_N1_Female
                        pass
                        dictAgeValuesPerSex[str_Sex][intAge] = intAgeNe_N1_Newborns_By_Sex
                    pass
                    self.objSSParametersLocal.intAgeNe_Manual_N1_Newborns += intAgeNe_N1_Newborns_By_Sex
                pass
                self.objSSParametersLocal.odictAgeNe_Manual_N1_Newborns_Per_Sex_Per_Year = dictAgeValuesPerSex


                ''' End of func DEBUG '''
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                        self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + 'AgeNe Stat: odictAgeNe_Sim_N1_Newborns_Per_Sex_Per_Year')
                        for str_Sex, value in self.objSSParametersLocal.odictAgeNe_Sim_N1_Newborns_Per_Sex_Per_Year.iteritems():
                            self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(value).values()),2)) + ' ; Values: ' + str(value)) 
                        pass    
                        self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + 'AgeNe Stat: odictAgeNe_Manual_N1_Newborns_Per_Sex_Per_Year')
                        for str_Sex, value in self.objSSParametersLocal.odictAgeNe_Manual_N1_Newborns_Per_Sex_Per_Year.iteritems():
                            self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(value).values()),2)) + ' ; Values: ' + str(value)) 
                        pass
                    pass    
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
                
                return True               


            def method_Update_AgeNe_Survival_Rates__sx(self):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
            
                #Survival rates
                for strSex, dictValues in self.objSSParametersLocal.odictRates_Of_Survival_COMBINED_BySex_ByAge.items():
                    for intAgeInMonths, value in dictValues.iteritems():
                        intAgeinYears = int(intAgeInMonths/12)
                        
                        dictNewValues = {intAgeinYears:value}
                        
                        if strSex in self.objSSParametersLocal.odictAgeNe_Sim_Age_Values_Survival_Rates:
                            self.objSSParametersLocal.odictAgeNe_Sim_Age_Values_Survival_Rates[strSex].update(dictNewValues)
                        else:
                            self.objSSParametersLocal.odictAgeNe_Sim_Age_Values_Survival_Rates[strSex] = dictNewValues
                    pass
                pass

            
                ''' End of func DEBUG '''
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                        self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + 'Survival Stat: odictAgeNe_Sim_Age_Values_Survival_Rates')
                        for str_Sex, value in self.objSSParametersLocal.odictAgeNe_Sim_Age_Values_Survival_Rates.iteritems():
                            self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + 'Sex: ' + str_Sex + ' ; Total: ' + str(round(sum(collections__Counter(value).values()),2)) + ' ; Values: ' + str(value)) 
                        pass
                    pass
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
            
                                        
                return True            
            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # NE experiments
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
            
            def method_Ne2_LDNe_EXPERIMENT_1(self, pop_In, dict_Results):

                '''
                --------------------------
                EXPERIMENT_1 - Define the experiment
                --------------------------
                '''

                #list_Stats_Categories = ['Full', 'Large_All', 'Large_Mature','Large_Embryo', 'Small_All', 'Small_Mature', 'Small_Embryo']
                list_Stats_Categories = ['Full', 'Large_Mature','Large_Embryo', 'Small_Mature', 'Small_Embryo']
                #list_Stats_Categories = ['Full', 'Large_Mature','Large_Embryo', 'Small_Mature', 'Small_Embryo']
                #list_Stats_Categories = ['All_Embryo', 'Large_Embryo', 'Small_Embryo']
                
                dict_SubSample_Replicates_By_Category = {
                                                         'Full':1
                                                         #'All_Embryo':1
                                                         #,'Large_All':1
                                                         ,'Large_Mature':1
                                                         ,'Large_Embryo':1
                                                         #,'Small_All':1
                                                         ,'Small_Mature':1
                                                         ,'Small_Embryo':1}
                if self.objSSParametersLocal.bool_Overlapping_Gens_Simulation:
                    int_Full_SubSample_Size = self.objSSParametersLocal.popnSize
                else:
                    int_Full_SubSample_Size = self.objSSParametersLocal.popnSize / 2 #For Discrete gens only
                pass
            
                int_Large_SubSample_Size = int_Full_SubSample_Size * 0.4
                int_Small_SubSample_Size = 500#int_Full_SubSample_Size * 0.1
                dict_SubSample_Sizes_By_Category = {
                                                    'Full':int(int_Full_SubSample_Size)
                                                    #'All_Embryo':int(int_Full_SubSample_Size)
                                                    #,'Large_All':int(int_Large_SubSample_Size)
                                                    ,'Large_Mature':int(int_Large_SubSample_Size)
                                                    ,'Large_Embryo':int(int_Large_SubSample_Size)
                                                    #,'Small_All':int(int_Small_SubSample_Size)
                                                    ,'Small_Mature':int(int_Small_SubSample_Size)
                                                    ,'Small_Embryo':int(int_Small_SubSample_Size)}
                
                dict_VSPs_To_SubSample_By_Category = {
                                                    'Full':0
                                                    #'All_Embryo':(0,globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)
                                                    #,'Large_All':0
                                                    ,'Large_Mature':(0,globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult)
                                                    ,'Large_Embryo':(0,globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)
                                                    ,'Small_Mature':(0,globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult)
                                                    ,'Small_Embryo':(0,globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)}
                
                list_LDNe_PCrits_To_Get = [0.1,0.05,0.02,0.01,0]
                
                str_Source_Unique_Run_Batch_Rep_VSP_ID = self.objSSParametersLocal.strUniqueRunID   
 
                for str_Stats_Category in list_Stats_Categories:
                    #if bool_Initialise_Stats:
                    if str_Stats_Category not in dict_Results:
                        dict_Results[str_Stats_Category] = OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label,str_Stats_Category)])
                    pass

                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder,self.objSSParametersLocal.strRunSpecificUserDefinedFolder)]))
                    #dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Ne2_Sampling_Stats.static_Label_Gen_Source_Unique_Run_Batch_Rep_VSP_ID,str_Source_Unique_Run_Batch_Rep_VSP_ID})
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories,list_Stats_Categories)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category,dict_SubSample_Sizes_By_Category[str_Stats_Category])]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category,dict_SubSample_Replicates_By_Category[str_Stats_Category])]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category,dict_VSPs_To_SubSample_By_Category[str_Stats_Category])]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get,list_LDNe_PCrits_To_Get)]))
                    
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp,self.objSSParametersLocal.bool_Overlapping_Gens_Simulation)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches,self.objSSParametersLocal.intBatches)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates,self.objSSParametersLocal.intReplicates)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size,int_Full_SubSample_Size)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation,self.objSSParametersLocal.bool_Allow_Mutation)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate,self.objSSParametersLocal.float_Mutation_Rate)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci,self.objSSParametersLocal.nLoci)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus,self.objSSParametersLocal.nAllelesPerLoci)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In,str(self.objSSParametersLocal.boolBurnIn))]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch,self.objSSParametersLocal.intCurrentBatch)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate,self.objSSParametersLocal.intCurrentReplicate)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year,self.objSSParametersLocal.intSimulationCurrentMonth//12)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month,self.objSSParametersLocal.intYearCurrentMonth)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total,self.objSSParametersLocal.int_MatingCount_Sim_Total)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total,self.objSSParametersLocal.int_MatingCount_Replicate_Total)]))
                    
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category,str_Stats_Category)]))

                    pass
                pass

                '''
                --------------------------
                Get the stats
                --------------------------
                '''
                
                with SSSamplingTest() as obj_SSSampling:
                    obj_SSSampling.method_Initialise(self.objSSParametersLocal)
                    bool_Use_Simupop_LDNe = False
                    bool_Use_Ne2_LDNe = True
                    for str_SubSampling_Category in dict_Results.keys():
                        dict_Results = obj_SSSampling.method_Population_SubSample_Ne2_Results(pop_In, str_SubSampling_Category, bool_Use_Simupop_LDNe, bool_Use_Ne2_LDNe, dict_Results)
                    pass


                '''
                --------------------------
                Flatten the dict for logging
                --------------------------
                '''
                dict_To_Flatten = dict_Results

                ''' First - determine how many levels down the nested dict goes '''

                with SSAnalysisHandler() as obj_SSAnalysis:
                    dict_Non_Dict_Key_Count_Per_Level = OrderedDict()
                    dict_Non_Dict_Key_Count_Per_Level = obj_SSAnalysis.method_Get_Nested_Dict__Non_Dict_Key_Count_Per_Nested_Level(dict_To_Flatten, 0, dict_Non_Dict_Key_Count_Per_Level)
                    #int_Lowest_Level = max(dict_Non_Dict_Key_Count_Per_Level, key=dict_Non_Dict_Key_Count_Per_Level.get) - 1
                    int_Lowest_Level = max(dict_Non_Dict_Key_Count_Per_Level.keys(), key=int) - 1
                
                ''' Second - Get the number fd dicts at that lowest level (-1)'''    
                int_Lowest_Level_Dict_Num_Keys = len(list_LDNe_PCrits_To_Get)
               
                ''' Third - Flattern the dict into a dcb multiline dict '''
                dict_To_Flatten = dict_Results
                dict_Final = OrderedDict()
                dict_MultiLine_Results = OrderedDict()
                int_Line_Initial = 0
                int_Line = 0
                int_Level = 0
                #int_Lowest_Level = 3
                #int_Lowest_Level_Dict_Num_Keys = 5
                
                with SSAnalysisHandler() as obj_SSAnalysis:
                    dict_MultiLine_Results = obj_SSAnalysis.method_Flatten_Nested_Dict_Into_Multiline_Dict__LDNe_Results(True, int_Line_Initial, int_Line, int_Level, int_Lowest_Level, int_Lowest_Level_Dict_Num_Keys, dict_To_Flatten, dict_Final)
                pass
                

                '''
                --------------------------
                Log the results
                --------------------------
                '''
                str_Results_1 = self.objSSParametersLocal.strUniqueRunID
                str_Heading_1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
                #str_Heading_Prefix_1 = globalsSS.Categorised_Ne2_Sampling_Stats.static_Label_Gen_File
                str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results
                self.obj_Logging__EOS_NE2_CATEGORISED.func_Log_MultiLine_Results_Header(self.obj_Results_Log__EOS_NE2_CATEGORISED, str_Heading_1, str_Heading_Prefix_1, dict_MultiLine_Results)
                self.obj_Logging__EOS_NE2_CATEGORISED.func_Log_MultiLine_Results_Detail(str_Results_1, self.obj_Results_Log__EOS_NE2_CATEGORISED, dict_MultiLine_Results)
                
                
                return dict_Results

               
            def method_Ne2_LDNe_EXPERIMENT_2(self, pop_In, dict_Results, bool_Header):

                '''
                --------------------------
                EXPERIMENT_2 - Define the experiment
                --------------------------
                '''

                #list_Stats_Categories = ['Full', 'Large_All', 'Large_Mature','Large_Embryo', 'Small_All', 'Small_Mature', 'Small_Embryo']
                list_Stats_Categories = ['Full', 'Large_Mature','Large_Embryo', 'Small_Mature', 'Small_Embryo']
                
                dict_SubSample_Replicates_By_Category = {'Full':1
                                                         #,'Large_All':1
                                                         ,'Large_Mature':1
                                                         ,'Large_Embryo':1
                                                         #,'Small_All':1
                                                         ,'Small_Mature':1
                                                         ,'Small_Embryo':2}
                
                if self.objSSParametersLocal.bool_Overlapping_Gens_Simulation:
                    int_Full_SubSample_Size = self.objSSParametersLocal.popnSize
                else:
                    int_Full_SubSample_Size = self.objSSParametersLocal.popnSize / 2 #For Discrete gens only
                pass
            
                int_Large_SubSample_Size = self.objSSParametersLocal.popnSize * 0.4
                int_Small_SubSample_Size = 500
                dict_SubSample_Sizes_By_Category = {'Full':int(int_Full_SubSample_Size)
                                                    #,'Large_All':int(int_Large_SubSample_Size)
                                                    ,'Large_Mature':int(int_Large_SubSample_Size)
                                                    ,'Large_Embryo':int(int_Large_SubSample_Size)
                                                    #,'Small_All':int(int_Small_SubSample_Size)
                                                    ,'Small_Mature':int(int_Small_SubSample_Size)
                                                    ,'Small_Embryo':int(int_Small_SubSample_Size)}
                
                dict_VSPs_To_SubSample_By_Category = {'Full':0
                                                    #,'Large_All':0
                                                    ,'Large_Mature':(0,2)
                                                    ,'Large_Embryo':(0,0)
                                                    #,'Small_All':0
                                                    ,'Small_Mature':(0,2)
                                                    ,'Small_Embryo':(0,0)}
                
                #list_LDNe_PCrits_To_Get = [0.05,0.02,0.01,0]
                #list_LDNe_PCrits_To_Get = [0.02,0]
                list_LDNe_PCrits_To_Get = [0.05,0]
                
                str_Source_Unique_Run_Batch_Rep_VSP_ID = self.objSSParametersLocal.strUniqueRunID   
 
                for str_Stats_Category in list_Stats_Categories:
                    #if bool_Initialise_Stats:
                    if str_Stats_Category not in dict_Results:
                        dict_Results[str_Stats_Category] = OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Experiment_Label,str_Stats_Category)])
                    pass

                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Run_User_Defined_Folder,self.objSSParametersLocal.strRunSpecificUserDefinedFolder)]))
                    #dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Ne2_Sampling_Stats.static_Label_Gen_Source_Unique_Run_Batch_Rep_VSP_ID,str_Source_Unique_Run_Batch_Rep_VSP_ID})
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_list_Stats_Categories,list_Stats_Categories)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Sizes_By_Category,dict_SubSample_Sizes_By_Category[str_Stats_Category])]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_SubSample_Replicates_By_Category,dict_SubSample_Replicates_By_Category[str_Stats_Category])]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_VSPs_To_SubSample_By_Category,dict_VSPs_To_SubSample_By_Category[str_Stats_Category])]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_EXPERIMENT_Parent_Offspring_Ne_1.static_Str_Colname_list_LDNe_PCrits_To_Get,list_LDNe_PCrits_To_Get)]))
                    
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Gens_Overlapp,self.objSSParametersLocal.bool_Overlapping_Gens_Simulation)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Batches,self.objSSParametersLocal.intBatches)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Replicates,self.objSSParametersLocal.intReplicates)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Pop_Size,int_Full_SubSample_Size)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Allow_Mutation,self.objSSParametersLocal.bool_Allow_Mutation)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mutation_Rate,self.objSSParametersLocal.float_Mutation_Rate)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Loci,self.objSSParametersLocal.nLoci)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Alleles_Per_Locus,self.objSSParametersLocal.nAllelesPerLoci)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Burn_In,str(self.objSSParametersLocal.boolBurnIn))]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Batch,self.objSSParametersLocal.intCurrentBatch)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Sim_Current_Replicate,self.objSSParametersLocal.intCurrentReplicate)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Year,self.objSSParametersLocal.intSimulationCurrentMonth//12)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Replicate_Current_Month,self.objSSParametersLocal.intYearCurrentMonth)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Sim_Total,self.objSSParametersLocal.int_MatingCount_Sim_Total)]))
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Mating_Count_Replicate_Total,self.objSSParametersLocal.int_MatingCount_Replicate_Total)]))
                    
                    dict_Results[str_Stats_Category].update(OrderedDict([(globalsSS.Colnames_COMMON_EXPERIMENT.static_Str_Colname_Stats_Category,str_Stats_Category)]))

                    pass
                pass

                '''
                --------------------------
                Get the stats
                --------------------------
                '''
                
                with SSSamplingTest() as obj_SSSampling:
                    obj_SSSampling.method_Initialise(self.objSSParametersLocal)
                    bool_Use_Simupop_LDNe = False
                    bool_Use_Ne2_LDNe = True
                    for str_SubSampling_Category in dict_Results.keys():
                        dict_Results = obj_SSSampling.method_Population_SubSample_Ne2_Results(pop_In, str_SubSampling_Category, bool_Use_Simupop_LDNe, bool_Use_Ne2_LDNe, dict_Results)
                    pass


                '''
                --------------------------
                Flatten the dict for logging
                --------------------------
                '''
                dict_To_Flatten = dict_Results

                ''' First - determine how many levels down the nested dict goes '''

                with SSAnalysisHandler() as obj_SSAnalysis:
                    dict_Non_Dict_Key_Count_Per_Level = OrderedDict()
                    dict_Non_Dict_Key_Count_Per_Level = obj_SSAnalysis.method_Get_Nested_Dict__Non_Dict_Key_Count_Per_Nested_Level(dict_To_Flatten, 0, dict_Non_Dict_Key_Count_Per_Level)
                    #int_Lowest_Level = max(dict_Non_Dict_Key_Count_Per_Level, key=dict_Non_Dict_Key_Count_Per_Level.get) - 1
                    int_Lowest_Level = max(dict_Non_Dict_Key_Count_Per_Level.keys(), key=int) - 1
                
                ''' Second - Get the number fd dicts at that lowest level (-1)'''    
                int_Lowest_Level_Dict_Num_Keys = len(list_LDNe_PCrits_To_Get)
               
                ''' Third - Flattern the dict into a dcb multiline dict '''
                dict_Final = OrderedDict()
                dict_MultiLine_Results = OrderedDict()
                int_Line_Initial = 0
                int_Line = 0
                int_Level = 0
                #int_Lowest_Level = 3
                #int_Lowest_Level_Dict_Num_Keys = 0 #5
                
                with SSAnalysisHandler() as obj_SSAnalysis:
                    dict_MultiLine_Results = obj_SSAnalysis.method_Flatten_Nested_Dict_Into_Multiline_Dict__LDNe_Results(True, int_Line_Initial, int_Line, int_Level, int_Lowest_Level, int_Lowest_Level_Dict_Num_Keys, dict_To_Flatten, dict_Final)
                pass
                

                '''
                --------------------------
                Log the results
                --------------------------
                '''
                str_Results_1 = self.objSSParametersLocal.strUniqueRunID
                str_Heading_1 = globalsSS.Logger_Results_File_Details.static_Logger_Label_Gen_UniqueID
                str_Heading_Prefix_1 = globalsSS.Logger_Results_File_Details.static_Logger_Colname_Prefix__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results
                #if (self.objSSParametersLocal.boolBurnIn) and (self.objSSParametersLocal.int_MatingCount_Replicate_BurnIn == self.objSSParametersLocal.intReplicateBurnInLengthInYears):
                if bool_Header:
                    self.obj_Logging__PF_NE2_CATEGORISED.func_Log_MultiLine_Results_Header(self.obj_Results_Log__PF_NE2_CATEGORISED, str_Heading_1, str_Heading_Prefix_1, dict_MultiLine_Results)
                    self.obj_Logging__PF_NE2_CATEGORISED.func_Log_MultiLine_Results_Detail(str_Results_1, self.obj_Results_Log__PF_NE2_CATEGORISED, dict_MultiLine_Results)
                else:
                    self.obj_Logging__PF_NE2_CATEGORISED.func_Log_MultiLine_Results_Detail(str_Results_1, self.obj_Results_Log__PF_NE2_CATEGORISED, dict_MultiLine_Results)
                pass
                
                return dict_Results

               
            def method_NEStatistics_Custom_1_Reporting_Manual_Experiments(self, pop_In, listVSPsWithIndivs):

                if self.objSSParametersLocal.boolReport_Custom_1:
                                   
                    with SSOutputHandler() as SSOutputOperation:
                        #listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        #
                        SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, '')
                        #
                        stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> Custom 1 Ne STATS Reporting - START   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                        boolNewline=True
                        SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)


                        dateTestRunStartTime = datetime.now()
                        self.method_Reporting_AgeNe_Statistics(pop_In) 
                        dateTestRunFinishTime = datetime.now()
                        dateTimeRunTime = timedelta()
                        dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
                        with SSOutputHandler() as SSOutputOperation:
                            #listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
                            SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'AgeNe Stats Reporting Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
                            SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'AgeNe Stats Reporting took: ' + str(dateTimeRunTime))
                        
                        
                        ####!!!!!!!!!!! Combination of Fertilization month, Gestation Length & Parturition month has to be exact for this to work
                        ####!!!!!!!!!!! The pop must have just been fertilized so that tupVSP(0,0) has individuals in it
                        
                        #DEBUG_ON
                        #self.methodOutput_outputPopulationDump(self.pop)
                        #Gather the NE stats required
                        #listVirtualSubPop = [(0, 61)]
                        #self.method_SimStat_LDNe_Reporting(self.pop, listVirtualSubPop )
                        #Send them to the output files as unstructured text
                        #listParams = [False,False,(0, 61)]
                        #self.method_Output_NE_Statistics(self.pop, listParams)
                        #DEBUG_OFF
    
                        
                        #Generate the SIMUPOP STATS for the required VSPs
                        #self.method_Initialise_Stats_For_ILF_Individual_Dump(self.pop, listVSPsWithIndivs)
                                            
                        listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_Custom_1_Reporting_Experiment_Dump
                        listNEStatisticsOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_1_Reporting_Experiment_Dump
    
                        intVSPProcessedCount = 0
                        for tupVSP in  listVSPsWithIndivs:
                            
                            self.objSSParametersLocal.listOutputVSPs_Custom_1_Reporting_Experiment_Dump = [tupVSP]     
                            
                        # ----------- Now perform the experimental sampleing with stat generation specific to the population sub-sample
                            '''
                            ENTER Number of replicates ---->
                            '''
                            intNumExperiments = self.objSSParametersLocal.intLDNe_Experiments_Custom_1_Replicates

                            '''
                            ENTER LDNe sample size ---->
                            '''

                            intSampleSize = self.objSSParametersLocal.intLDNe_Experiments_Custom_1_Sample_Size

                            '''
                            ENTER LDNe loci ---->
                            '''
                            
                            listReportLoci = self.objSSParametersLocal.listLDNe_Experiments_Custom_1_Loci_To_Report
                            #listReportLoci.append([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

                            '''
                            ENTER VSPs to sub-sample ---->
                            '''
                            tupVSPToSample = [0]
                                #listVSPsToSample.append(simupop.simupop.ALL_AVAIL)

                            dictExperiments = AutoVivificationHandler()
                            dictExperiments['Experiment_Label'] = ['1','2','3']
                            dictExperiments['Run_Experiment'] = [True,False,False]
                            dictExperiments['Experiment_Replicates'] = [intNumExperiments,1,1]
                            dictExperiments['Sample_Size'] = [intSampleSize,200,300]
                            #dictExperiments['Report_Loci'] = [[0,1,2,3,4,5],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]]
                            dictExperiments['Report_Loci'] = [listReportLoci,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]]
                            dictExperiments['VSPs_To_Sample'] = [tupVSPToSample, simupop.ALL_AVAIL, simupop.ALL_AVAIL]
                            #dictExperiments['VSPs_To_Sample'] = [simupop.ALL_AVAIL, simupop.ALL_AVAIL, listVSPsWithIndivs]
                            #dictExperiments['VSPs_To_Sample'] = [simupop.ALL_AVAIL, simupop.ALL_AVAIL, simupop.ALL_AVAIL]
                            
                            #Start experiments
                            intNumExperiments = len(dictExperiments['Experiment_Replicates'])
                            for intCurrentExperiment in range(0, intNumExperiments):
                                
                                boolRunMe = dictExperiments['Run_Experiment'][intCurrentExperiment]
                                if boolRunMe:
                                    listPopSubSamples = []
                                    listSubSampleVSPsToOutput = []
                                    
                                    strExperimentLabel = dictExperiments['Experiment_Label'][intCurrentExperiment]
                                    intNumRandomPopSubSamplesToDraw = dictExperiments['Experiment_Replicates'][intCurrentExperiment]
                                    intRandomSampleNumIndividuals = dictExperiments['Sample_Size'][intCurrentExperiment]
                                    self.objSSParametersLocal.listLociToReportNE = dictExperiments['Report_Loci'][intCurrentExperiment]
                                    listVSPToSample = dictExperiments['VSPs_To_Sample'][intCurrentExperiment]
                                    #stringMessage = '> ' +'intNumRandomPopSubSamplesToDraw = ' + str(intNumRandomPopSubSamplesToDraw) + ' > intRandomSampleNumIndividuals = ' + str(intRandomSampleNumIndividuals) + ' > #Loci = ' + str(len(self.objSSParametersLocal.listLociToReportNE)) +'\n'
                                    #boolNewline=True
                                    #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                                    
                                    #perform experiment for x replicates
                                    for intExperimentReplicate in range(0, intNumRandomPopSubSamplesToDraw):
            
                                        pop_SubSample = drawRandomSample(self.pop, sizes=intRandomSampleNumIndividuals, subPops=listVSPToSample)
                                        listRanges = [[0, intRandomSampleNumIndividuals]]
                                        listVirtualSubPop = [(0, 0)]
                                        listParams = [False,False,(0, 0)]
                                        
                                        #DEBUG_ON
                                        pop_SubSample = self.method_SplitLifeStagesInto_AgeInMonths_VSPs_By_AgeInMonths(pop_SubSample)
                                        with SSAnalysisHandler() as objSSAnalysisHandler:
                                            odictVSPSizes = objSSAnalysisHandler.method_Get_VSP_Sizes(pop_SubSample, False)
                                            print('#Indivs of each age_in_months: ' + str(odictVSPSizes))
                                            pass
                                        #self.methodOutput_outputPopulationDump(pop_SubSample)
                                        
                                        #DEBUG_OFF
                                        
                                        #Create just one VSP from the pop sub-sample
                                        pop_SubSample = self.method_SplitRandomSampleIntoVSP(pop_SubSample, listRanges)
                                        
                                        #Gather the NE stats required
                                        self.objSSParametersLocal.boolReportLDNe = True
                                        self.method_SimStat_LDNe_Reporting(pop_SubSample, listVirtualSubPop )
                                        #Send them to the output files as unstructured text
                                        #self.method_Output_NE_Statistics(pop_SubSample, listParams)
                                        
                                        ##############  REPORT: Allele Freq Statistics
                                        self.method_SimStat_AlleleFreq_Reporting(pop_SubSample, listVirtualSubPop)
    #                                     #sim.Stat(pop, alleleFreq=simupop.ALL_AVAIL, subPops=[(0,0), (0,1), (0,2), (0,3)]),
    #                                     simupop.stat(pop_SubSample, alleleFreq=simupop.ALL_AVAIL, subPops=simupop.ALL_AVAIL, vars=['alleleFreq','alleleNum']),
    #                                     simupop.stat(pop_SubSample, alleleFreq=simupop.ALL_AVAIL, subPops=listVirtualSubPop, vars=['alleleFreq_sp','alleleNum_sp']),
                                                                
                                        listPopSubSamples.append(pop_SubSample)
                                        listSubSampleVSPsToOutput = listVirtualSubPop
        
                                        #Write out a GENPOP file for corss validation of statistics
                                        listOutputParams= self.objSSParametersLocal.listOutputParams_PopulationGENEPOP_FSTAT_Pop_Dump_Per_Replicate
                                        #Define filename
                                        strOutfile = self.objSSParametersLocal.outfilePath + self.objSSParametersLocal.strFileNameProgramPrefix + 'EOR_EXP_' + str(strExperimentLabel) + '_REP_' + str(intExperimentReplicate) + '_' + self.objSSParametersLocal.strFilenameEmbeddedFields + '_rep_' + str(self.objSSParametersLocal.intCurrentReplicate).zfill(3) + '.genepop.gp_ssim'
                                        #Create file for entire SUB-SAMPLE
                                        with SSOutputHandler() as SSOutputOperation:
                                            boolOutputVSPs = False
                                            #SSOutputOperation.methodSaveFile_GENEPOP_FSTAT_By_Pop(pop_SubSample, listOutputParams[0], boolOutputVSPs, listVirtSubPopsToOutput, listOutputParams[1], listOutputParams[2], strOutfile, loci=self.objSSParametersLocal.listLociToReportNE)
                                            pass
                                    pass
                                
         
                                    #Write out the full population stats plus the experiment replicate stats to ILF file
                                    #Experiment replicates will be appended to the EOL after the full pop stats    
                                    
                                    if intVSPProcessedCount > 0:
                                        boolOutputHeader = False
                                    else:
                                        boolOutputHeader = True
                                        
                                    if intCurrentExperiment == 0:
                                        boolReusePrimedTopLevelOutputObject = False
                                    else:
                                        boolReusePrimedTopLevelOutputObject = True
    
                                        with SSOutputHandler() as SSOutputOperation:
                                            listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_1_Reporting_Experiment_Dump
                                            #
                                            stringMessage = 'E' + str(intCurrentExperiment) + ';'
                                            boolNewline=False
                                            SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                                        
                                        #print('E' + str(intCurrentExperiment)) + ':',
                                                
                                    boolReuseObjectPropertiesToReport = True
                                    self.objSSParametersLocal.boolReportSimAgeNe = True
                                    self.methodOutput_outputPopulationIndividuals_ILF_Custom_1_Reporting_Experiment(self.pop, listPopSubSamples, listSubSampleVSPsToOutput, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport)
                                    
                                    intVSPProcessedCount += 1
                                    #stringMessage = '> ' +'intNumRandomPopSubSamplesToDraw = ' + str(intNumRandomPopSubSamplesToDraw) + ' > intRandomSampleNumIndividuals = ' + str(intRandomSampleNumIndividuals) + ' > #Loci = ' + str(len(self.objSSParametersLocal.listLociToReportNE)) +'\n'
                                    #boolNewline=False
                                    #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listNEStatisticsOutputDestinations, stringMessage, boolNewline)
        
                                    #stringMessage = '\n' + '>>>>>>>>>>>>>>>>> ' +'Experiment ' + str(strExperimentLabel) + '- END ' +'\n'
                                    #boolNewline=False
                                    #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listNEStatisticsOutputDestinations, stringMessage, boolNewline)
            
                                    #Next experiment
    
                    with SSOutputHandler() as SSOutputOperation:
                        listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        #
                        stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> Custom 1 Ne STATS Reporting - END   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                        boolNewline=True
                        SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                        #
                        listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        SSOutputOperation.methodOutput_SimGeneralMessageFooter(listOutputDestinations, '')


            def method_NEStatistics_Custom_2_Reporting_Auto_Experiments(self, pop_In, listVSPsWithIndivs):

                if self.objSSParametersLocal.boolReport_Custom_2:
                   
                    with SSOutputHandler() as SSOutputOperation:
                        listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        #
                        SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, '')
                        #
                        stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> Custom 2 Ne STATS Reporting - START   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                        boolNewline=True
                        SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)


                        dateTestRunStartTime = datetime.now()
                        self.method_Reporting_AgeNe_Statistics(pop_In) 
                        dateTestRunFinishTime = datetime.now()
                        dateTimeRunTime = timedelta()
                        dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
                        with SSOutputHandler() as SSOutputOperation:
                            #listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
                            SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'AgeNe Stats Reporting Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
                            SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'AgeNe Stats Reporting took: ' + str(dateTimeRunTime))
                        
                        ####!!!!!!!!!!! Combination of Fertilization month, Gestation Length & Parturition month has to be exact for this to work
                        ####!!!!!!!!!!! The pop must have just been fertilized so that tupVSP(0,0) has individuals in it
                        
                        #DEBUG_ON
                        #self.methodOutput_outputPopulationDump(self.pop)
                        #Gather the NE stats required
                        #listVirtualSubPop = [(0, 61)]
                        #self.method_SimStat_LDNe_Reporting(self.pop, listVirtualSubPop )
                        #Send them to the output files as unstructured text
                        #listParams = [False,False,(0, 61)]
                        #self.method_Output_NE_Statistics(self.pop, listParams)
                        #DEBUG_OFF
                        
                        #Generate the SIMUPOP STATS for the required VSPs
                        #self.method_Initialise_Stats_For_ILF_Individual_Dump(self.pop, listVSPsWithIndivs)
                                            
                        listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_Custom_2_Reporting_Experiment_Dump
                        listNEStatisticsOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_2_Reporting_Experiment_Dump
    
                        intVSPProcessedCount = 0
                        for tupVSP in  listVSPsWithIndivs:
                            
                            self.objSSParametersLocal.listOutputVSPs_Custom_2_Reporting_Experiment_Dump = [tupVSP]     
                            
                        # ----------- Now perform the experimental sampleing with stat generation specific to the population sub-sample
                        
                            dictExperiments = AutoVivificationHandler()
                            #dictExperiments['Experiment_Label'] = ['1','2','3']
                            '''
                            ENTER Number of replicates ---->
                            '''
                            intNumExperiments = self.objSSParametersLocal.intLDNe_Experiments_Custom_2_Replicates
                        
                            
                            
                            listExperimentLabel = []
                            listRunExperiment = []
                            listExperimentReplicates = []
                            listSampleSize = []
                            listReportLoci = []
                            listVSPsToSample = []
    
                            for intExperiment in range(0, intNumExperiments):
                                listExperimentLabel.append(str(intExperiment+1))
                                listRunExperiment.append(True)
                                listExperimentReplicates.append(1)
                                '''
                                ENTER LDNe sample size ---->
                                '''
    
                                listSampleSize.append(self.objSSParametersLocal.intLDNe_Experiments_Custom_2_Sample_Size)
    
                                '''
                                ENTER LDNe loci ---->
                                '''
                                
                                listReportLoci.append(self.objSSParametersLocal.listLDNe_Experiments_Custom_2_Loci_To_Report)
                                #listReportLoci.append([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
    
                                '''
                                ENTER VSPs to sub-sample ---->
                                '''
                                listVSPsToSample.append(self.objSSParametersLocal.listLDNe_Experiments_Custom_2_VSP_List_To_Sample)
                                #listVSPsToSample.append([tupVSP])
                                #listVSPsToSample.append(simupop.simupop.ALL_AVAIL)
                            
                            pass
                            
                            dictExperiments['Experiment_Label'] = listExperimentLabel
                            dictExperiments['Run_Experiment'] = listRunExperiment
                            dictExperiments['Experiment_Replicates'] = listExperimentReplicates
                            dictExperiments['Sample_Size'] = listSampleSize
                            dictExperiments['Report_Loci'] = listReportLoci
                            dictExperiments['VSPs_To_Sample'] = listVSPsToSample
                            
                            
                            #dictExperiments['VSPs_To_Sample'] = [simupop.ALL_AVAIL, simupop.ALL_AVAIL, listVSPsWithIndivs]
                            #dictExperiments['VSPs_To_Sample'] = [simupop.ALL_AVAIL, simupop.ALL_AVAIL, simupop.ALL_AVAIL]
                            
                            #Start experiments
                            intNumExperiments = len(dictExperiments['Experiment_Label'])
                            for intCurrentExperiment in range(0, intNumExperiments):
                                
                                boolRunMe = dictExperiments['Run_Experiment'][intCurrentExperiment]
                                if boolRunMe:
                                    listPopSubSamples = []
                                    listSubSampleVSPsToOutput = []
                                    
                                    strExperimentLabel = dictExperiments['Experiment_Label'][intCurrentExperiment]
                                    intNumRandomPopSubSamplesToDraw = dictExperiments['Experiment_Replicates'][intCurrentExperiment]
                                    intRandomSampleNumIndividuals = dictExperiments['Sample_Size'][intCurrentExperiment]
                                    self.objSSParametersLocal.listLociToReportNE = dictExperiments['Report_Loci'][intCurrentExperiment]
                                    listVSPToSample = dictExperiments['VSPs_To_Sample'][intCurrentExperiment]
                                    #stringMessage = '> ' +'intNumRandomPopSubSamplesToDraw = ' + str(intNumRandomPopSubSamplesToDraw) + ' > intRandomSampleNumIndividuals = ' + str(intRandomSampleNumIndividuals) + ' > #Loci = ' + str(len(self.objSSParametersLocal.listLociToReportNE)) +'\n'
                                    #boolNewline=True
                                    #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                                    
                                    #perform experiment for x replicates
                                    for intExperimentReplicate in range(0, intNumRandomPopSubSamplesToDraw):
            
    #                                     dateTestRunStartTime = datetime.now()
                                         
                                        pop_SubSample = drawRandomSample(self.pop, sizes=intRandomSampleNumIndividuals, subPops=listVSPToSample)
                                        listRanges = [[0, intRandomSampleNumIndividuals]]
                                        listVirtualSubPop = [(0, 0)]
                                        listParams = [False,False,(0, 0)]
                                         
                                        #DEBUG_ON
#                                         pop_SubSample = self.method_SplitLifeStagesInto_AgeInMonths_VSPs_By_AgeInMonths(pop_SubSample)
#                                         with SSAnalysisHandler() as objSSAnalysisHandler:
#                                             odictVSPSizes = objSSAnalysisHandler.method_Get_VSP_Sizes(pop_SubSample, False)
#                                             print('#Indivs of each age_in_months: ' + str(odictVSPSizes))
#                                             pass
                                        #self.methodOutput_outputPopulationDump(pop_SubSample)
                                        
                                        #DEBUG_OFF
                                        #Create just one VSP from the pop sub-sample
                                        pop_SubSample = self.method_SplitRandomSampleIntoVSP(pop_SubSample, listRanges)
    
    #                                     dateTestRunFinishTime = datetime.now()
    #                                     dateTimeRunTime = timedelta()
    #                                     dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
    #                                     with SSOutputHandler() as SSOutputOperation:
    #                                         listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
    #                                         SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'LDNe Random Sample Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
    #                                         SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'LDNe Random Sample Run took: ' + str(dateTimeRunTime))
                                        
    #                                    dateTestRunStartTime = datetime.now()
                                        
                                        #Gather the NE stats required
                                        self.objSSParametersLocal.boolReportLDNe = True
                                        self.method_SimStat_LDNe_Reporting(pop_SubSample, listVirtualSubPop )
                                        #Send them to the output files as unstructured text
                                        #self.method_Output_NE_Statistics(pop_SubSample, listParams)
    
    #                                     dateTestRunFinishTime = datetime.now()
    #                                     dateTimeRunTime = timedelta()
    #                                     dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
    #                                     with SSOutputHandler() as SSOutputOperation:
    #                                         listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
    #                                         SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'LDNe  Stats Gathering Run Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
    #                                         SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'LDNe Stats Gathering Run took: ' + str(dateTimeRunTime))
    
    #                                     self.objSSParametersLocal.dateTestRunStartTime = datetime.now()
                                       
                                        ##############  REPORT: Allele Freq Statistics
                                        self.method_SimStat_AlleleFreq_Reporting(pop_SubSample, listVirtualSubPop)
    #                                     #sim.Stat(pop, alleleFreq=simupop.ALL_AVAIL, subPops=[(0,0), (0,1), (0,2), (0,3)]),
    #                                     simupop.stat(pop_SubSample, alleleFreq=simupop.ALL_AVAIL, subPops=simupop.ALL_AVAIL, vars=['alleleFreq','alleleNum']),
    #                                     simupop.stat(pop_SubSample, alleleFreq=simupop.ALL_AVAIL, subPops=listVirtualSubPop, vars=['alleleFreq_sp','alleleNum_sp']),
    
    #                                     dateTestRunFinishTime = datetime.now()
    #                                     dateTimeRunTime = timedelta()
    #                                     dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
    #                                     with SSOutputHandler() as SSOutputOperation:
    #                                         listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
    #                                         SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'LDNe AlleleFreq Stats Gathering Run Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
    #                                         SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'LDNe AlleleFreq Stats Gathering Run Finished: ' + str(dateTimeRunTime))
                                                                
                                        listPopSubSamples.append(pop_SubSample)
                                        listSubSampleVSPsToOutput = listVirtualSubPop
                                        
                                        
                                        #Write out a GENPOP file for corss validation of statistics
                                        listOutputParams= self.objSSParametersLocal.listOutputParams_PopulationGENEPOP_FSTAT_Pop_Dump_Per_Replicate
                                        #Define filename
                                        strOutfile = self.objSSParametersLocal.outfilePath + self.objSSParametersLocal.strFileNameProgramPrefix + 'EOR_EXP_' + str(strExperimentLabel) + '_REP_' + str(intExperimentReplicate) + '_' + self.objSSParametersLocal.strFilenameEmbeddedFields + '_rep_' + str(self.objSSParametersLocal.intCurrentReplicate).zfill(3) + '.genepop.gp_ssim'
                                        #Create file for entire SUB-SAMPLE
                                        with SSOutputHandler() as SSOutputOperation:
                                            boolOutputVSPs = False
                                            #SSOutputOperation.methodSaveFile_GENEPOP_FSTAT_By_Pop(pop_SubSample, listOutputParams[0], boolOutputVSPs, listVirtSubPopsToOutput, listOutputParams[1], listOutputParams[2], strOutfile, loci=self.objSSParametersLocal.listLociToReportNE)
                                            pass
                                        
                                    pass
                                
    #                                 dateTestRunStartTime = datetime.now()
                                    
                                    #Write out the full population stats plus the experiment replicate stats to ILF file
                                    #Experiment replicates will be appended to the EOL after the full pop stats    
                                    
                                    if intVSPProcessedCount > 0:
                                        boolOutputHeader = False
                                    else:
                                        boolOutputHeader = True
                                    
                                    if intCurrentExperiment == 0:
                                        boolReusePrimedTopLevelOutputObject = False
                                    else:
                                        boolReusePrimedTopLevelOutputObject = True
                                        with SSOutputHandler() as SSOutputOperation:
                                            listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_2_Reporting_Experiment_Dump
                                            #
                                            #stringMessage = 'E' + str(intCurrentExperiment) + ';'
                                            #boolNewline=False
                                            #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
    
                                        #print('E' + str(intCurrentExperiment)) + ':',
                                                
                                    boolReuseObjectPropertiesToReport = True
                                    self.objSSParametersLocal.boolReportSimAgeNe = True
                                    self.methodOutput_outputPopulationIndividuals_ILF_Custom_2_Reporting_Experiment(self.pop, listPopSubSamples, listSubSampleVSPsToOutput, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport)
    
    #                                 dateTestRunFinishTime = datetime.now()
    #                                 dateTimeRunTime = timedelta()
    #                                 dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
    #                                 with SSOutputHandler() as SSOutputOperation:
    #                                     listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
    #                                     SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'LDNe File Output Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
    #                                     SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'LDNe File Output Finished took: ' + str(dateTimeRunTime))
    
                                    
                                    intVSPProcessedCount += 1
                                    #stringMessage = '> ' +'intNumRandomPopSubSamplesToDraw = ' + str(intNumRandomPopSubSamplesToDraw) + ' > intRandomSampleNumIndividuals = ' + str(intRandomSampleNumIndividuals) + ' > #Loci = ' + str(len(self.objSSParametersLocal.listLociToReportNE)) +'\n'
                                    #boolNewline=False
                                    #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listNEStatisticsOutputDestinations, stringMessage, boolNewline)
        
                                    #stringMessage = '\n' + '>>>>>>>>>>>>>>>>> ' +'Experiment ' + str(strExperimentLabel) + '- END ' +'\n'
                                    #boolNewline=False
                                    #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listNEStatisticsOutputDestinations, stringMessage, boolNewline)
            
                                    #Next experiment
                    #print('\n')
                    with SSOutputHandler() as SSOutputOperation:
                        listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        #
                        stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> Custom 2 Ne STATS Reporting - END   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                        boolNewline=True
                        SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                        #
                        listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                        SSOutputOperation.methodOutput_SimGeneralMessageFooter(listOutputDestinations, '')
            
            
            def method_NEStatistics_Custom_3_Reporting(self):
               
                with SSOutputHandler() as SSOutputOperation:
                    listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, '')
                    #
                    stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> Custom 3 Reporting - START   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                    boolNewline=True
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                    
                    listSubPopsToOutput = []
                    listSubPopsToOutput.append(globalsSS.SP_SubPops.static_intSP_SubPop_Primary)
                    listNEStatisticsOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_3_Reporting_Experiment_Dump

                    intSPProcessedCount = 0
                    for intSubPop in  listSubPopsToOutput:
                        
                        self.objSSParametersLocal.listOutputVSPs_Custom_3_Reporting_Experiment_Dump = [intSubPop]     
                        
                        ##############  REPORT: Allele Freq Statistics
                        self.method_SimStat_AlleleFreq_Reporting(self.pop, listSubPopsToOutput)
                                                
                        if intSPProcessedCount > 0:
                            boolOutputHeader = False
                        else:
                            boolOutputHeader = True
                        
                        #self.objSSParametersLocal.boolReportLDNe = False        
                        self.methodOutput_outputPopulationIndividuals_ILF_Custom_3_Reporting_Experiment(self.pop, listSubPopsToOutput, boolOutputHeader)

                        intSPProcessedCount += 1

                    listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    #
                    stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> Custom 3 Reporting - END   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                    boolNewline=True
                    SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                    #
                    listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                    SSOutputOperation.methodOutput_SimGeneralMessageFooter(listOutputDestinations, '')


            def method_NEStatistics_Custom_4_Reporting_Auto_Experiments(self, listVSPsToExperimentOn, listVSPsWithIndivs):

                if self.objSSParametersLocal.boolReport_Custom_4:
                    
                    boolReport_Custom_4_Sample_Required = False
                    intSimulationCurrentYear = (self.objSSParametersLocal.intSimulationCurrentMonth // 12)
                    
                    if intSimulationCurrentYear in self.objSSParametersLocal.listReport_Custom_4_Sim_Year_Sample_Required:
                        boolReport_Custom_4_Sample_Required = True
                    pass
                
                    if boolReport_Custom_4_Sample_Required:
                         
                        with SSOutputHandler() as SSOutputOperation:
                            listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                            #
                            SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, '')
                            #
                            stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> Custom 4 Ne STATS Reporting - START   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                            boolNewline=True
                            SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                            #
                            #listOutputDestinations = [self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                            
                            ####!!!!!!!!!!! Combination of Fertilization month, Gestation Length & Parturition month has to be exact for this to work
                            ####!!!!!!!!!!! The pop must have just been fertilized so that tupVSP(0,0) has individuals in it
                            
                            #DEBUG_ON
                            #self.methodOutput_outputPopulationDump(self.pop)
                            #Gather the NE stats required
                            #listVirtualSubPop = [(0, 61)]
                            #self.method_SimStat_LDNe_Reporting(self.pop, listVirtualSubPop )
                            #Send them to the output files as unstructured text
                            #listParams = [False,False,(0, 61)]
                            #self.method_Output_NE_Statistics(self.pop, listParams)
                            #DEBUG_OFF
                            
                            #Generate the SIMUPOP STATS for the required VSPs
                            #self.method_Initialise_Stats_For_ILF_Individual_Dump(self.pop, listVSPsWithIndivs)
                                                
                            listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_Custom_4_Reporting_Experiment_Dump
                            listNEStatisticsOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_4_Reporting_Experiment_Dump
        
                            intVSPProcessedCount = 0
                            for tupVSP in  listVSPsToExperimentOn:
                                
                                self.objSSParametersLocal.listOutputVSPs_Custom_4_Reporting_Experiment_Dump = [tupVSP]     
                                
                            # ----------- Now perform the experimental sampleing with stat generation specific to the population sub-sample
                            
                                dictExperiments = AutoVivificationHandler()
                                #dictExperiments['Experiment_Label'] = ['1','2','3']
                                '''
                                ENTER Number of replicates ---->
                                '''
                                intNumExperiments = self.objSSParametersLocal.intLDNe_Experiments_Custom_4_Replicates
                                '''
                                ENTER Sizes of subsamples for each VSP with indivs ---->
                                '''
                                listVSPsToRandomSample = []
                                listRandomSampleSizePerVSP = []
                                for keyAgeInmonths, valueNumToSample in self.objSSParametersLocal.odictAgeCohortSampleNumbers.items():
                                    tupVSPToRandomSample = (globalsSS.SP_SubPops.static_intSP_SubPop_Primary, keyAgeInmonths+1)
                                    listVSPsToRandomSample.append(tupVSPToRandomSample)
                                    listRandomSampleSizePerVSP.append(valueNumToSample)
                                pass
                                
                                listExperimentLabel = []
                                listRunExperiment = []
                                listExperimentReplicates = []
                                listSampleSize = []
                                listReportLoci = []
                                listVSPsToSample = []
        
                                for intExperiment in range(0, intNumExperiments):
                                    listExperimentLabel.append(str(intExperiment+1))
                                    listRunExperiment.append(True)
                                    listExperimentReplicates.append(1)
                                    '''
                                    ENTER LDNe sample size ---->
                                    '''
        
                                    listSampleSize.append(self.objSSParametersLocal.intLDNe_Experiments_Custom_4_Sample_Size)
        
                                    '''
                                    ENTER LDNe loci ---->
                                    '''
                                    listReportLoci.append(self.objSSParametersLocal.listLDNe_Experiments_Custom_4_Loci_To_Report)
                                    #listReportLoci.append([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
        
                                    
                                    '''
                                    ENTER VSPs to sub-sample ---->
                                    '''
                                    listVSPsToSample.append(self.objSSParametersLocal.listLDNe_Experiments_Custom_4_VSP_List_To_Sample)
                                    #listVSPsToSample.append([(0,0)])
                                    #listVSPsToSample.append([tupVSP])
                                    #listVSPsToSample.append(simupop.simupop.ALL_AVAIL)
                                pass
                                                                
                                dictExperiments['Experiment_Label'] = listExperimentLabel
                                dictExperiments['Run_Experiment'] = listRunExperiment
                                dictExperiments['Experiment_Replicates'] = listExperimentReplicates
                                dictExperiments['Sample_Size'] = listSampleSize
                                dictExperiments['Report_Loci'] = listReportLoci
                                dictExperiments['VSPs_To_Sample'] = listVSPsToSample
                                
                                
                                #dictExperiments['VSPs_To_Sample'] = [simupop.ALL_AVAIL, simupop.ALL_AVAIL, listVSPsWithIndivs]
                                #dictExperiments['VSPs_To_Sample'] = [simupop.ALL_AVAIL, simupop.ALL_AVAIL, simupop.ALL_AVAIL]
                                
                                #Start experiments
                                intNumExperiments = len(dictExperiments['Experiment_Label'])
                                for intCurrentExperiment in range(0, intNumExperiments):
                                    
                                    boolRunMe = dictExperiments['Run_Experiment'][intCurrentExperiment]
                                    if boolRunMe:
                                        listPopSubSamples = []
                                        listSubSampleVSPsToOutput = []
                                        
                                        strExperimentLabel = dictExperiments['Experiment_Label'][intCurrentExperiment]
                                        intNumRandomPopSubSamplesToDraw = dictExperiments['Experiment_Replicates'][intCurrentExperiment]
                                        intRandomSampleNumIndividuals = dictExperiments['Sample_Size'][intCurrentExperiment]
                                        self.objSSParametersLocal.listLociToReportNE = dictExperiments['Report_Loci'][intCurrentExperiment]
                                        listVSPToSample = dictExperiments['VSPs_To_Sample'][intCurrentExperiment]
                                        #stringMessage = '> ' +'intNumRandomPopSubSamplesToDraw = ' + str(intNumRandomPopSubSamplesToDraw) + ' > intRandomSampleNumIndividuals = ' + str(intRandomSampleNumIndividuals) + ' > #Loci = ' + str(len(self.objSSParametersLocal.listLociToReportNE)) +'\n'
                                        #boolNewline=True
                                        #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                                        
                                        #perform experiment for x replicates
                                        for intExperimentReplicate in range(0, intNumRandomPopSubSamplesToDraw):
                
        #                                     dateTestRunStartTime = datetime.now()
                                            
                                                 
                                            pop_SubSample = drawRandomSample(self.pop, sizes=listRandomSampleSizePerVSP, subPops=listVSPsToRandomSample)
                                            #simupop.mergeSubPops(pop_SubSample)
                                            pop_SubSample.mergeSubPops()
                                            #pop_SubSample = drawRandomSample(self.pop, sizes=intRandomSampleNumIndividuals, subPops=listVSPToSample)
                                            listRanges = [[0, intRandomSampleNumIndividuals]]
                                            listVirtualSubPop = [(0, 0)]
                                            listParams = [False,False,(0, 0)]
                                             
                                            #DEBUG_ON
                                            pop_SubSample = self.method_SplitLifeStagesInto_AgeInMonths_VSPs_By_AgeInMonths(pop_SubSample)
                                            with SSAnalysisHandler() as objSSAnalysisHandler:
                                                #odictVSPSizes = objSSAnalysisHandler.method_Get_VSP_Sizes(pop_SubSample, False)
                                                odictVSPSizes = objSSAnalysisHandler.method_Get_VSP_Sizes(pop_SubSample, False)
                                                print('Pop sub-sample size: ' + str(int(pop_SubSample.subPopSize())))
                                                print('Pop sub-sample sizes: ' + str(pop_SubSample.subPopSizes()))
                                                print('#Indivs of each age_in_months: ' + str(odictVSPSizes))
                                                pass
                                                #self.methodOutput_outputPopulationDump(pop_SubSample)
                                            #with SSOutputHandler() as objSSOutputOperation:
                                            #    objSSOutputOperation.method_Pause_Console()
                                            #DEBUG_OFF
                                            
                                            #Create just one VSP from the pop sub-sample
                                            pop_SubSample = self.method_SplitRandomSampleIntoVSP(pop_SubSample, listRanges)
        
        #                                     dateTestRunFinishTime = datetime.now()
        #                                     dateTimeRunTime = timedelta()
        #                                     dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
        #                                     with SSOutputHandler() as SSOutputOperation:
        #                                         listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
        #                                         SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'LDNe Random Sample Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
        #                                         SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'LDNe Random Sample Run took: ' + str(dateTimeRunTime))
                                            
        #                                    dateTestRunStartTime = datetime.now()
                                            
                                            
                                            #Gather the NE stats required
                                            self.objSSParametersLocal.boolReportLDNe = True
                                            self.method_SimStat_LDNe_Reporting(pop_SubSample, listVirtualSubPop)
                                            #Send them to the output files as unstructured text
                                            self.objSSParametersLocal.boolReportLDNe = True
                                            listLDNePCritOutput=[0.0,0.05,0.02,0.01]
                                            #listParams = [False,False,[(0,0)], listLDNePCritOutput, False]
                                            #self.method_Output_NE_Statistics(pop_SubSample, listParams)
                                            listVSPsToReport = listVirtualSubPop
                                            strPrefixMessage = 'Sub-sample ' + str(intCurrentExperiment+1) + ' of ' + str(intNumExperiments) + ' : '
                                            self.method_Calculate_And_Output_LDNE_To_Console(pop_SubSample, listVSPsToReport, listLDNePCritOutput, listOutputDestinations, strPrefixMessage)
                                            
        
        #                                     dateTestRunFinishTime = datetime.now()
        #                                     dateTimeRunTime = timedelta()
        #                                     dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
        #                                     with SSOutputHandler() as SSOutputOperation:
        #                                         listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
        #                                         SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'LDNe  Stats Gathering Run Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
        #                                         SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'LDNe Stats Gathering Run took: ' + str(dateTimeRunTime))
        
        #                                     self.objSSParametersLocal.dateTestRunStartTime = datetime.now()
                                           
                                            ##############  REPORT: Allele Freq Statistics
                                            self.method_SimStat_AlleleFreq_Reporting(pop_SubSample, listVirtualSubPop)
        #                                     #sim.Stat(pop, alleleFreq=simupop.ALL_AVAIL, subPops=[(0,0), (0,1), (0,2), (0,3)]),
        #                                     simupop.stat(pop_SubSample, alleleFreq=simupop.ALL_AVAIL, subPops=simupop.ALL_AVAIL, vars=['alleleFreq','alleleNum']),
        #                                     simupop.stat(pop_SubSample, alleleFreq=simupop.ALL_AVAIL, subPops=listVirtualSubPop, vars=['alleleFreq_sp','alleleNum_sp']),
        
        #                                     dateTestRunFinishTime = datetime.now()
        #                                     dateTimeRunTime = timedelta()
        #                                     dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
        #                                     with SSOutputHandler() as SSOutputOperation:
        #                                         listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
        #                                         SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'LDNe AlleleFreq Stats Gathering Run Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
        #                                         SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'LDNe AlleleFreq Stats Gathering Run Finished: ' + str(dateTimeRunTime))
                                                                    
                                            listPopSubSamples.append(pop_SubSample)
                                            listSubSampleVSPsToOutput = listVirtualSubPop
                                            
                                            
                                            #Write out a GENPOP file for corss validation of statistics
                                            listOutputParams= self.objSSParametersLocal.listOutputParams_PopulationGENEPOP_FSTAT_Pop_Dump_Per_Replicate
                                            #Define filename
                                            strOutfile = self.objSSParametersLocal.outfilePath + self.objSSParametersLocal.strFileNameProgramPrefix + 'EOR_EXP_' + str(strExperimentLabel) + '_REP_' + str(intExperimentReplicate) + '_' + self.objSSParametersLocal.strFilenameEmbeddedFields + '_rep_' + str(self.objSSParametersLocal.intCurrentReplicate).zfill(3) + '.genepop.gp_ssim'
                                            #Create file for entire SUB-SAMPLE
                                            with SSOutputHandler() as SSOutputOperation:
                                                boolOutputVSPs = False
                                                #SSOutputOperation.methodSaveFile_GENEPOP_FSTAT_By_Pop(pop_SubSample, listOutputParams[0], boolOutputVSPs, listVirtSubPopsToOutput, listOutputParams[1], listOutputParams[2], strOutfile, loci=self.objSSParametersLocal.listLociToReportNE)
                                                pass
                                            
                                        pass
                                    
        #                                 dateTestRunStartTime = datetime.now()
                                        
                                        #Write out the full population stats plus the experiment replicate stats to ILF file
                                        #Experiment replicates will be appended to the EOL after the full pop stats    
                                        
                                        if intVSPProcessedCount > 0:
                                            boolOutputHeader = False
                                        else:
                                            boolOutputHeader = True
                                        
                                        if intCurrentExperiment == 0:
                                            boolReusePrimedTopLevelOutputObject = False
                                        else:
                                            boolReusePrimedTopLevelOutputObject = True
                                            with SSOutputHandler() as SSOutputOperation:
                                                listNEStatisticsOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_4_Reporting_Experiment_Dump
                                                #
                                                #stringMessage = 'E' + str(intCurrentExperiment) + ';'
                                                #boolNewline=False
                                                #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
        
                                            #print('E' + str(intCurrentExperiment)) + ':',
                                                    
                                        boolReuseObjectPropertiesToReport = True
                                        self.objSSParametersLocal.boolReportSimAgeNe = False
                                        self.methodOutput_outputPopulationIndividuals_ILF_Custom_4_Reporting_Experiment(self.pop, listPopSubSamples, listSubSampleVSPsToOutput, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport)
        
        #                                 dateTestRunFinishTime = datetime.now()
        #                                 dateTimeRunTime = timedelta()
        #                                 dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
        #                                 with SSOutputHandler() as SSOutputOperation:
        #                                     listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
        #                                     SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'LDNe File Output Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
        #                                     SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'LDNe File Output Finished took: ' + str(dateTimeRunTime))
        
                                        
                                        intVSPProcessedCount += 1
                                        #stringMessage = '> ' +'intNumRandomPopSubSamplesToDraw = ' + str(intNumRandomPopSubSamplesToDraw) + ' > intRandomSampleNumIndividuals = ' + str(intRandomSampleNumIndividuals) + ' > #Loci = ' + str(len(self.objSSParametersLocal.listLociToReportNE)) +'\n'
                                        #boolNewline=False
                                        #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listNEStatisticsOutputDestinations, stringMessage, boolNewline)
            
                                        #stringMessage = '\n' + '>>>>>>>>>>>>>>>>> ' +'Experiment ' + str(strExperimentLabel) + '- END ' +'\n'
                                        #boolNewline=False
                                        #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listNEStatisticsOutputDestinations, stringMessage, boolNewline)
                
                                        #Next experiment
                        #print('\n')
                        with SSOutputHandler() as SSOutputOperation:
                            listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                            #
                            stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> Custom 4 Ne STATS Reporting - END   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                            boolNewline=True
                            SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                            #
                            SSOutputOperation.methodOutput_SimGeneralMessageFooter(listOutputDestinations, '')
            

            def method_NEStatistics_Custom_5_Reporting_Auto_Experiments(self, listVSPsToExperimentOn, listVSPsWithIndivs):

                if self.objSSParametersLocal.boolReport_Custom_5:
                    
                    boolReport_Custom_5_Sample_Required = False
                    intSimulationCurrentYear = (self.objSSParametersLocal.intSimulationCurrentMonth // 12)
                    
                    if intSimulationCurrentYear in self.objSSParametersLocal.listReport_Custom_5_Sim_Year_Sample_Required:
                        boolReport_Custom_5_Sample_Required = True
                    pass
                
                    if boolReport_Custom_5_Sample_Required:
                         
                        with SSOutputHandler() as SSOutputOperation:
                            listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                            #
                            SSOutputOperation.methodOutput_SimGeneralMessageHeader(listOutputDestinations, '')
                            #
                            stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> Custom 5 Ne STATS Reporting - START   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                            boolNewline=True
                            SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)

                            
                            ####!!!!!!!!!!! Combination of Fertilization month, Gestation Length & Parturition month has to be exact for this to work
                            ####!!!!!!!!!!! The pop must have just been fertilized so that tupVSP(0,0) has individuals in it
                            
                            #DEBUG_ON
                            #self.methodOutput_outputPopulationDump(self.pop)
                            #Gather the NE stats required
                            #listVirtualSubPop = [(0, 61)]
                            #self.method_SimStat_LDNe_Reporting(self.pop, listVirtualSubPop )
                            #Send them to the output files as unstructured text
                            #listParams = [False,False,(0, 61)]
                            #self.method_Output_NE_Statistics(self.pop, listParams)
                            #DEBUG_OFF
        
                            #Generate the SIMUPOP STATS for the required VSPs
                            #self.method_Initialise_Stats_For_ILF_Individual_Dump(self.pop, listVSPsWithIndivs)
                                                
                            listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_Custom_5_Reporting_Experiment_Dump
                            listNEStatisticsOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_5_Reporting_Experiment_Dump
        
                            intVSPProcessedCount = 0
                            for tupVSP in  listVSPsToExperimentOn:
                                
                                self.objSSParametersLocal.listOutputVSPs_Custom_5_Reporting_Experiment_Dump = [tupVSP]     
                                
                            # ----------- Now perform the experimental sampleing with stat generation specific to the population sub-sample
                            
                                dictExperiments = AutoVivificationHandler()
                                #dictExperiments['Experiment_Label'] = ['1','2','3']
                                '''
                                ENTER Number of replicates ---->
                                '''
                                intNumExperiments = self.objSSParametersLocal.intLDNe_Experiments_Custom_5_Replicates
                            
                                
                                
                                listExperimentLabel = []
                                listRunExperiment = []
                                listExperimentReplicates = []
                                listSampleSize = []
                                listReportLoci = []
                                listVSPsToSample = []
        
                                for intExperiment in range(0, intNumExperiments):
                                    listExperimentLabel.append(str(intExperiment+1))
                                    listRunExperiment.append(True)
                                    listExperimentReplicates.append(1)
                                    '''
                                    ENTER LDNe sample size ---->
                                    '''
        
                                    listSampleSize.append(self.objSSParametersLocal.intLDNe_Experiments_Custom_5_Sample_Size)
        
                                    '''
                                    ENTER LDNe loci ---->
                                    '''
                                    listReportLoci.append(self.objSSParametersLocal.listLDNe_Experiments_Custom_5_Loci_To_Report)
                                    #listReportLoci.append([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
        
                                    
                                    '''
                                    ENTER VSPs to sub-sample ---->
                                    '''
                                    listVSPsToSample.append(self.objSSParametersLocal.listLDNe_Experiments_Custom_5_VSP_List_To_Sample)
                                    #listVSPsToSample.append([(0,0)])
                                    #listVSPsToSample.append([0])
                                    #listVSPsToSample.append([tupVSP])
                                    #listVSPsToSample.append(simupop.simupop.ALL_AVAIL)

                                pass
                                                                
                                dictExperiments['Experiment_Label'] = listExperimentLabel
                                dictExperiments['Run_Experiment'] = listRunExperiment
                                dictExperiments['Experiment_Replicates'] = listExperimentReplicates
                                dictExperiments['Sample_Size'] = listSampleSize
                                dictExperiments['Report_Loci'] = listReportLoci
                                dictExperiments['VSPs_To_Sample'] = listVSPsToSample
                                
                                
                                #dictExperiments['VSPs_To_Sample'] = [simupop.ALL_AVAIL, simupop.ALL_AVAIL, listVSPsWithIndivs]
                                #dictExperiments['VSPs_To_Sample'] = [simupop.ALL_AVAIL, simupop.ALL_AVAIL, simupop.ALL_AVAIL]
                                
                                #Start experiments
                                intNumExperiments = len(dictExperiments['Experiment_Label'])
                                for intCurrentExperiment in range(0, intNumExperiments):
                                    
                                    boolRunMe = dictExperiments['Run_Experiment'][intCurrentExperiment]
                                    if boolRunMe:
                                        listPopSubSamples = []
                                        listSubSampleVSPsToOutput = []
                                        
                                        strExperimentLabel = dictExperiments['Experiment_Label'][intCurrentExperiment]
                                        intNumRandomPopSubSamplesToDraw = dictExperiments['Experiment_Replicates'][intCurrentExperiment]
                                        intRandomSampleNumIndividuals = dictExperiments['Sample_Size'][intCurrentExperiment]
                                        self.objSSParametersLocal.listLociToReportNE = dictExperiments['Report_Loci'][intCurrentExperiment]
                                        listVSPToSample = dictExperiments['VSPs_To_Sample'][intCurrentExperiment]
                                        #stringMessage = '> ' +'intNumRandomPopSubSamplesToDraw = ' + str(intNumRandomPopSubSamplesToDraw) + ' > intRandomSampleNumIndividuals = ' + str(intRandomSampleNumIndividuals) + ' > #Loci = ' + str(len(self.objSSParametersLocal.listLociToReportNE)) +'\n'
                                        #boolNewline=True
                                        #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                                        
                                        #perform experiment for x replicates
                                        for intExperimentReplicate in range(0, intNumRandomPopSubSamplesToDraw):
                
        #                                     dateTestRunStartTime = datetime.now()
                                             
                                            pop_SubSample = drawRandomSample(self.pop, sizes=intRandomSampleNumIndividuals, subPops=listVSPToSample)
                                            listRanges = [[0, intRandomSampleNumIndividuals]]
                                            listVirtualSubPop = [(0, 0)]
                                            listParams = [False,False,(0, 0)]
                                             
                                            #DEBUG_ON
                                            pop_SubSample = self.method_SplitLifeStagesInto_AgeInMonths_VSPs_By_AgeInMonths(pop_SubSample)
                                            with SSAnalysisHandler() as objSSAnalysisHandler:
                                                odictVSPSizes = objSSAnalysisHandler.method_Get_VSP_Sizes(pop_SubSample, False)
                                                print('Pop sub-sample size: ' + str(int(pop_SubSample.subPopSize())))
                                                print('#Indivs of each age_in_months: ' + str(odictVSPSizes))
                                                pass
                                            #self.methodOutput_outputPopulationDump(pop_SubSample)
                                            
                                            #DEBUG_OFF
                                            #Create just one VSP from the pop sub-sample
                                            pop_SubSample = self.method_SplitRandomSampleIntoVSP(pop_SubSample, listRanges)
        
        #                                     dateTestRunFinishTime = datetime.now()
        #                                     dateTimeRunTime = timedelta()
        #                                     dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
        #                                     with SSOutputHandler() as SSOutputOperation:
        #                                         listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
        #                                         SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'LDNe Random Sample Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
        #                                         SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'LDNe Random Sample Run took: ' + str(dateTimeRunTime))
                                            
        #                                    dateTestRunStartTime = datetime.now()
                                            
                                            
                                            #Gather the NE stats required
                                            self.objSSParametersLocal.boolReportLDNe = True
                                            self.method_SimStat_LDNe_Reporting(pop_SubSample, listVirtualSubPop)
                                            #Send them to the output files as unstructured text
                                            self.objSSParametersLocal.boolReportLDNe = True
                                            listLDNePCritOutput=[0.0,0.05,0.02,0.01]
                                            #listParams = [False,False,[(0,0)], listLDNePCritOutput, False]
                                            #self.method_Output_NE_Statistics(pop_SubSample, listParams)
                                            listVSPsToReport = listVirtualSubPop
                                            strPrefixMessage = 'Sub-sample ' + str(intCurrentExperiment+1) + ' of ' + str(intNumExperiments) + ' : '
                                            self.method_Calculate_And_Output_LDNE_To_Console(pop_SubSample, listVSPsToReport, listLDNePCritOutput, listOutputDestinations, strPrefixMessage)
                                                                        
        
        #                                     dateTestRunFinishTime = datetime.now()
        #                                     dateTimeRunTime = timedelta()
        #                                     dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
        #                                     with SSOutputHandler() as SSOutputOperation:
        #                                         listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
        #                                         SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'LDNe  Stats Gathering Run Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
        #                                         SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'LDNe Stats Gathering Run took: ' + str(dateTimeRunTime))
        
        #                                     self.objSSParametersLocal.dateTestRunStartTime = datetime.now()
                                           
                                            ##############  REPORT: Allele Freq Statistics
                                            self.method_SimStat_AlleleFreq_Reporting(pop_SubSample, listVirtualSubPop)
        #                                     #sim.Stat(pop, alleleFreq=simupop.ALL_AVAIL, subPops=[(0,0), (0,1), (0,2), (0,3)]),
        #                                     simupop.stat(pop_SubSample, alleleFreq=simupop.ALL_AVAIL, subPops=simupop.ALL_AVAIL, vars=['alleleFreq','alleleNum']),
        #                                     simupop.stat(pop_SubSample, alleleFreq=simupop.ALL_AVAIL, subPops=listVirtualSubPop, vars=['alleleFreq_sp','alleleNum_sp']),
        
        #                                     dateTestRunFinishTime = datetime.now()
        #                                     dateTimeRunTime = timedelta()
        #                                     dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
        #                                     with SSOutputHandler() as SSOutputOperation:
        #                                         listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
        #                                         SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'LDNe AlleleFreq Stats Gathering Run Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
        #                                         SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'LDNe AlleleFreq Stats Gathering Run Finished: ' + str(dateTimeRunTime))
                                                                    
                                            listPopSubSamples.append(pop_SubSample)
                                            listSubSampleVSPsToOutput = listVirtualSubPop
                                            
                                            
                                            #Write out a GENPOP file for corss validation of statistics
                                            listOutputParams= self.objSSParametersLocal.listOutputParams_PopulationGENEPOP_FSTAT_Pop_Dump_Per_Replicate
                                            #Define filename
                                            strOutfile = self.objSSParametersLocal.outfilePath + self.objSSParametersLocal.strFileNameProgramPrefix + 'EOR_EXP_' + str(strExperimentLabel) + '_REP_' + str(intExperimentReplicate) + '_' + self.objSSParametersLocal.strFilenameEmbeddedFields + '_rep_' + str(self.objSSParametersLocal.intCurrentReplicate).zfill(3) + '.genepop.gp_ssim'
                                            #Create file for entire SUB-SAMPLE
                                            with SSOutputHandler() as SSOutputOperation:
                                                boolOutputVSPs = False
                                                #SSOutputOperation.methodSaveFile_GENEPOP_FSTAT_By_Pop(pop_SubSample, listOutputParams[0], boolOutputVSPs, listVirtSubPopsToOutput, listOutputParams[1], listOutputParams[2], strOutfile, loci=self.objSSParametersLocal.listLociToReportNE)
                                                pass
                                            
                                        pass
                                    
        #                                 dateTestRunStartTime = datetime.now()
                                        
                                        #Write out the full population stats plus the experiment replicate stats to ILF file
                                        #Experiment replicates will be appended to the EOL after the full pop stats    
                                        
                                        if intVSPProcessedCount > 0:
                                            boolOutputHeader = False
                                        else:
                                            boolOutputHeader = True
                                        
                                        if intCurrentExperiment == 0:
                                            boolReusePrimedTopLevelOutputObject = False
                                        else:
                                            boolReusePrimedTopLevelOutputObject = True
                                            with SSOutputHandler() as SSOutputOperation:
                                                listNEStatisticsOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_5_Reporting_Experiment_Dump
                                                #listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_5_Reporting_Experiment_Dump
                                                #
                                                #stringMessage = 'E' + str(intCurrentExperiment) + ';'
                                                #boolNewline=False
                                                #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
        
                                            #print('E' + str(intCurrentExperiment)) + ':',
                                                    
                                        boolReuseObjectPropertiesToReport = True
                                        self.objSSParametersLocal.boolReportSimAgeNe = False
                                        self.methodOutput_outputPopulationIndividuals_ILF_Custom_5_Reporting_Experiment(self.pop, listPopSubSamples, listSubSampleVSPsToOutput, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport)
        
        #                                 dateTestRunFinishTime = datetime.now()
        #                                 dateTimeRunTime = timedelta()
        #                                 dateTimeRunTime = dateTestRunFinishTime - dateTestRunStartTime
        #                                 with SSOutputHandler() as SSOutputOperation:
        #                                     listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameTimingSummaryLogAllBatches]
        #                                     SSOutputOperation.methodOutput_SimGeneralMessage(True, False, listOutputDestinations, 'LDNe File Output Finished: ' + dateTestRunFinishTime.strftime("%Y-%m-%d %H:%M:%S"))
        #                                     SSOutputOperation.methodOutput_SimGeneralMessage(False, False, listOutputDestinations, 'LDNe File Output Finished took: ' + str(dateTimeRunTime))
        
                                        
                                        intVSPProcessedCount += 1
                                        #stringMessage = '> ' +'intNumRandomPopSubSamplesToDraw = ' + str(intNumRandomPopSubSamplesToDraw) + ' > intRandomSampleNumIndividuals = ' + str(intRandomSampleNumIndividuals) + ' > #Loci = ' + str(len(self.objSSParametersLocal.listLociToReportNE)) +'\n'
                                        #boolNewline=False
                                        #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listNEStatisticsOutputDestinations, stringMessage, boolNewline)
            
                                        #stringMessage = '\n' + '>>>>>>>>>>>>>>>>> ' +'Experiment ' + str(strExperimentLabel) + '- END ' +'\n'
                                        #boolNewline=False
                                        #SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listNEStatisticsOutputDestinations, stringMessage, boolNewline)
                
                                        #Next experiment
                        #print('\n')
                        with SSOutputHandler() as SSOutputOperation:
                            listOutputDestinations = ['console', self.objSSParametersLocal.outputFileNameSummaryLogAllBatches]
                            #
                            stringMessage = '>>>>>>>>>>>>>>>>>>>>>>>>>>> Custom 4 Ne STATS Reporting - END   >>>>>>>>>>>>>>>>>>>>>>>>>>>'  +'\n'
                            boolNewline=True
                            SSOutputOperation.methodOutput_SimGeneralMessageWithoutHeaderAndFooter(listOutputDestinations, stringMessage, boolNewline)
                            #
                            SSOutputOperation.methodOutput_SimGeneralMessageFooter(listOutputDestinations, '')
                            #
                            #SSOutputOperation.method_Pause_Console()

                pass
            
                return True


            def method_Update_Sim_Birth_Rate_Stats(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass
                            
                for strSex in self.objSSParametersLocal.listSexes:                                
                    odictBirthRatePerSex = self.method_Get_Birth_Rate_Stats_For_Sex(pop_In, strSex)
                    
                    #Check if any offspring were produced
                    if len(odictBirthRatePerSex) > 0:
                        
                        #intYearAsAProxyForAge = self.objSSParametersLocal.intSimulationCurrentMonth // 12
                        intYearAsAProxyForAge = self.objSSParametersLocal.int_MatingCount_LifeSpan
                        
                        if (intYearAsAProxyForAge < self.objSSParametersLocal.minMatingAge+1) or (intYearAsAProxyForAge > self.objSSParametersLocal.maxMatingAge):
                            dictNewValues = {intYearAsAProxyForAge:0}
                        else:
                            dictNewValues = {intYearAsAProxyForAge:odictBirthRatePerSex[strSex][globalsSS.StatisticsConstants.static_stringMeanLabel]}
    #                     dictNewValues = {intYearAsAProxyForAge:odictBirthRatePerSex[strSex][globalsSS.StatisticsConstants.static_stringMeanLabel]}
                        pass
                    
                        if strSex in self.objSSParametersLocal.odictAgeNe_Sim_b_x_Odict_Scaled_Birth_Rate_Per_Age_x:
                            self.objSSParametersLocal.odictAgeNe_Sim_b_x_Odict_Scaled_Birth_Rate_Per_Age_x[strSex].update(dictNewValues)
                        else:
                            self.objSSParametersLocal.odictAgeNe_Sim_b_x_Odict_Scaled_Birth_Rate_Per_Age_x[strSex] = dictNewValues
                        pass
                    pass
                pass
            
                if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                    #DEBUG_ON
                    self.obj_Log_Debug_AgeNe.debug('>>> AgeNe Stat: AgeNe_Sim_b_x_Odict_Scaled_Birth_Rate_Per_Age_x')
                    for str_Sex, value in self.objSSParametersLocal.odictAgeNe_Sim_b_x_Odict_Scaled_Birth_Rate_Per_Age_x.iteritems():
                        self.obj_Log_Debug_AgeNe.debug('Sex: ' + str_Sex + ' ; Total: ' + str(round(float(sum(collections__Counter(value).values())),2)) + ' ; Values: ' + str(value)) 
                    pass    
                    #DEBUG_OFF
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console()
                    #pass
                pass
            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message='', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                            
                return True
            '''
            --------------------------------------------------------------------------------------------------------
            #  Manage log files
            --------------------------------------------------------------------------------------------------------
            '''
            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # Open log files
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
            def method_Open_Log_Files_PF_Per_Fertilization(self):

                '''
                -------------------------
                Get Per Fertilization - PF - Duration Results Loggers
                -------------------------
                '''
                
                

                return True


            def method_Open_Log_Files_For_End_Of_Replicate_EOR_Reporting(self):

                ''' Get logger - Embryo Parents Ne Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__Embryo_Parent_Ne_Stats_Post_Fertilization + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__Embryo_Parent_Ne_Stats_Post_Fertilization
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__EPNS, self.obj_Results_Log__EPNS = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                ''' Get logger - Effective Parents Stats '''

                bool_Report_Effective_Parent_Summary_Stats = True
                if bool_Report_Effective_Parent_Summary_Stats:                
                    bool_LogToConsole = False
                    str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                    str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__Effective_Parents_Stats_Post_Fertilization + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                    str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__Effective_Parents_Stats_Post_Fertilization
                    strFileName_Experiment_Label = ''
                    str_Experiment = ''
                    self.obj_Logging__EPS, self.obj_Results_Log__EPS = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)
                pass
            
                ''' Get logger - Categorised Ne2 Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__EXPERIMENT_Parent_Offspring_Ne_1__Categorised_Ne2_EOR_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__EOS_NE2_CATEGORISED, self.obj_Results_Log__EOS_NE2_CATEGORISED = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                ''' Get logger - Exp 2 - Categorised Ne2 Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__EXPERIMENT_Parent_Offspring_Ne_2__Categorised_Ne2_PF_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__PF_NE2_CATEGORISED, self.obj_Results_Log__PF_NE2_CATEGORISED = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                '''
                ~~~~~~~~~~~~~~~~~~
                AgeNe EOR Loggers
                ~~~~~~~~~~~~~~~~~~
                '''
                ''' Get logger - AgeNe Man Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Man_Details_EOR_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Man_Details_EOR_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__EOR_AgeNe_Man_D, self.obj_Results_Log__EOR_AgeNe_Man_D = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                ''' Get logger - AgeNe Man Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Man_LifeTables_Total_EOR_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Man_LifeTables_Total_EOR_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__EOR_AgeNe_Man_LT, self.obj_Results_Log__EOR_AgeNe_Man_LT = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                ''' Get logger - AgeNe Man Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Man_DemographicTables_Total_EOR_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Man_DemographicTables_Total_EOR_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__EOR_AgeNe_Man_DT, self.obj_Results_Log__EOR_AgeNe_Man_DT = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                ''' Get logger - AgeNe Man Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Man_Final_Totals_EOR_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Man_Final_Totals_EOR_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__EOR_AgeNe_Man_FT, self.obj_Results_Log__EOR_AgeNe_Man_FT = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                ''' Get logger - AgeNe Sim Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_Details_EOR_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_Details_EOR_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__EOR_AgeNe_Sim_D, self.obj_Results_Log__EOR_AgeNe_Sim_D = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                ''' Get logger - AgeNe Sim Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_LifeTables_Total_EOR_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_LifeTables_Total_EOR_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__EOR_AgeNe_Sim_LT, self.obj_Results_Log__EOR_AgeNe_Sim_LT = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                ''' Get logger - AgeNe Sim Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_DemographicTables_Total_EOR_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_DemographicTables_Total_EOR_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__EOR_AgeNe_Sim_DT, self.obj_Results_Log__EOR_AgeNe_Sim_DT = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                ''' Get logger - AgeNe Sim Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_Final_Totals_EOR_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_Final_Totals_EOR_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__EOR_AgeNe_Sim_FT, self.obj_Results_Log__EOR_AgeNe_Sim_FT = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)
                
                '''
                ~~~~~~~~~~~~~~~~~~
                AgeNe PF Loggers
                ~~~~~~~~~~~~~~~~~~
                '''
                ''' Get logger - AgeNe Sim Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_Details_PF_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_Details_PF_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__PF_AgeNe_Sim_D, self.obj_Results_Log__PF_AgeNe_Sim_D = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                ''' Get logger - AgeNe Sim Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_LifeTables_Total_PF_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_LifeTables_Total_PF_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__PF_AgeNe_Sim_LT, self.obj_Results_Log__PF_AgeNe_Sim_LT = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                ''' Get logger - AgeNe Sim Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_DemographicTables_Total_PF_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_DemographicTables_Total_PF_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__PF_AgeNe_Sim_DT, self.obj_Results_Log__PF_AgeNe_Sim_DT = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                ''' Get logger - AgeNe Sim Stats '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__AgeNe_Sim_Final_Totals_PF_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__AgeNe_Sim_Final_Totals_PF_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__PF_AgeNe_Sim_FT, self.obj_Results_Log__PF_AgeNe_Sim_FT = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                
                '''
                ~~~~~~~~~~~~~~~~~~
                Mortality PF Loggers
                ~~~~~~~~~~~~~~~~~~
                '''
                ''' Get logger '''
                bool_LogToConsole = False
                str_Logger_Path = self.objSSParametersLocal.str_Current_Run_Path__Logs
                str_Logger_Name = globalsSS.Logger_Results_File_Details.static_Logger_Name__Mortality_PF_Results + '_' + self.objSSParametersLocal.str_Sim_Batch_Replicate_Identifier_Short
                str_Logger_FileName_Suffix = globalsSS.Logger_Results_File_Details.static_Logger_File_Suffix__Mortality_PF_Results
                strFileName_Experiment_Label = ''
                str_Experiment = ''
                self.obj_Logging__Mortality_PF, self.obj_Results_Log__Mortality_PF = self.method_Get_Results_Logger(bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment)

                return True             

            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            Logger initilisation
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
            def method_Get_Results_Logger(self, bool_LogToConsole, str_Logger_Path, str_Logger_Name, str_Logger_FileName_Suffix, strFileName_Experiment_Label, str_Experiment):

                with FileHandler() as obj_File_Op:
                    obj_File_Op.method_Create_Path(str_Logger_Path)
                    
                str_Logger_Name = self.objSSParametersLocal.strUniqueRunID + '_' + str_Logger_Name + '_' + strFileName_Experiment_Label + '_' + str_Experiment + str_Logger_FileName_Suffix
                                
                obj_Logging = Logging()
                obj_Logging.str_Logger_Name = str_Logger_Name
                obj_Logging.str_Logger_Level = 'info'
                obj_Logging.bool_ClearLogFileAtStart = True
                obj_Logging.bool_LogToConsole = bool_LogToConsole
                obj_Logging.bool_LogToFile = True
                obj_Logging.strLogPath = str_Logger_Path
                obj_Logging.strLogFile = str_Logger_Name
                #obj_Logging = self.func_Get_Func_Specific_Logger_Name(str_Logger_Path, str_Logger_Name)

                ''' Create logger to record results '''
                int_Level = 1
                str_Logger_Name = obj_Logging.strLogFile
                obj_Logging.func_Initialise_New_Logger()
                obj_Log_Results = logging__getLogger(obj_Logging.str_Logger_Name)
                    
                ''' Check if logger already exists'''
                with FileHandler() as objFileOperation:
                    boolFileExistsAtDestination = objFileOperation.fileExists(obj_Logging.strLogPath + '\\' + obj_Logging.strLogFile)

                return obj_Logging, obj_Log_Results
            
            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # Close log files
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
            def method_Close_Log_Files(self, list_tup_Logs):

                for tup_Log_obj in list_tup_Logs:
                    ''' Clear the log handlers'''
                    tup_Log_obj[1].handlers = []
                    ''' None the log object '''
                    #obj_Logger = tup_Log_obj[0]
                    #obj_Logger = None
                pass

                return True


            def method_Close_Log_Files_EOR_End_Of_replicate(self):



                return True                

            '''
            --------------------------------------------------------------------------------------------------------
            Output routines
            --------------------------------------------------------------------------------------------------------
            '''

            def method_Output_Genpop_File_PF_Per_Fertilization(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass           

                ''' Format general filename '''
                str_Current_Mating_Out = self.str_Sim_Batch_Replicate_Mating_Identifier_Short + '_Z'
                
                if self.objSSParametersLocal.boolBurnIn:
                    str_File_Name_BurnIn_Flag = '_' + globalsSS.Sim_Status.static_str_Sim_Status__BurnIn + '_'
                else:
                    str_File_Name_BurnIn_Flag = '_' + globalsSS.Sim_Status.static_str_Sim_Status__InSim + '_'
                pass
                str_File_Name_Suffix = str_File_Name_BurnIn_Flag + str_Current_Mating_Out
                #strFilePath = self.objSSParametersLocal.outfilePath + '\\BioP\\'
                strFilePath = self.objSSParametersLocal.str_Current_Run_Path + '\\' + globalsSS.Processing_Path.static_str_Processing_Path__Genepop_PF_Pop_Sample
                strFilePathAndNameFull_Export_Prefix = strFilePath + '\\' + self.objSSParametersLocal.strUniqueRunID  + '_'
               
                with SSSamplingTest() as obj_Sampling:
                    '''
                    Create GENEPOP file
                    IMPORTANT - Allele adjust means the difference between an allele and missing data
                    if your data has zeros as missing data - set this to zero
                    if your data is simulated - set this to 1 to avoid external programs assuming Allele 0 is missing data
                    '''
                    intAlleleAdjust = 1
                    bool_Prevent_Internal_Function_Console_Output = True
                    bool_Prevent_External_Function_Console_Output = True
                    
                    #bool_Genepop_Export_PF_Embryo_VSP = False
                    if self.objSSParametersLocal.bool_Genepop_Export_PF_Embryo_VSP:
                        list_VSPs = [(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo)]
                        ''' Get random sub-sample of the population if required
                            set to 0 if all required
                        '''
                        float_SubSample_Percent_Of_SP = self.objSSParametersLocal.float_SubSample_Percent_Of_PF_Embryo_VSP
                        int_Pop_Size = pop_In.subPopSize(list_VSPs[0])
                        if float_SubSample_Percent_Of_SP > 0:
                            intSubSample_Size = int(float_SubSample_Percent_Of_SP * int_Pop_Size)
                        else:
                            intSubSample_Size = int_Pop_Size
                        pass
                        pop_SubSample = obj_Sampling.method_Draw_Random_Pop_SubSample(pop_In, intSubSample_Size, list_VSPs)
                        ''' Export for Embryonic VSP '''
                        strFilePathAndNameFull_Export = strFilePathAndNameFull_Export_Prefix + globalsSS.Genepop_Results_File_Details.static_Genepop_File_Name__Embryo_VSP_Post_Fertilization + str_File_Name_Suffix + globalsSS.Genepop_Results_File_Details.static_Genepop_File_Suffix__Embryo_VSP_Post_Fertilization
                        ''' Prep File system path for save '''
                        with FileHandler() as obj_FileOp:
                            bool_Success = obj_FileOp.method_FileSystem_Prep_For_File_Save(strFilePathAndNameFull_Export, bool_Delete=True)
                        pass                        
                        
                        boolSuccess = obj_Sampling.method_Export_Genotypes(pop_SubSample, intAlleleAdjust, strFilePathAndNameFull_Export, bool_Prevent_Internal_Function_Console_Output, bool_Prevent_External_Function_Console_Output, (True, False, True), list_VSPs)
                    pass
                
                    #bool_Genepop_Export_PF_Mature_VSP = True
                    if self.objSSParametersLocal.bool_Genepop_Export_PF_Mature_VSP:
                        list_VSPs = [(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult)]
                        ''' Get random sub-sample of the population if required
                            set to 0 if all required
                        '''
                        float_SubSample_Percent_Of_SP = self.objSSParametersLocal.float_SubSample_Percent_Of_PF_Mature_VSP
                        int_Pop_Size = pop_In.subPopSize(list_VSPs[0])
                        if float_SubSample_Percent_Of_SP > 0:
                            intSubSample_Size = int(float_SubSample_Percent_Of_SP * int_Pop_Size)
                        else:
                            intSubSample_Size = int_Pop_Size
                        pass
                        pop_SubSample = obj_Sampling.method_Draw_Random_Pop_SubSample(pop_In, intSubSample_Size, list_VSPs)
                        ''' Export for Mature VSP '''
                        strFilePathAndNameFull_Export = strFilePathAndNameFull_Export_Prefix + globalsSS.Genepop_Results_File_Details.static_Genepop_File_Name__Mature_VSP_Post_Fertilization + str_File_Name_Suffix + globalsSS.Genepop_Results_File_Details.static_Genepop_File_Suffix__Mature_VSP_Post_Fertilization
                        ''' Prep File system path for save '''
                        with FileHandler() as obj_FileOp:
                            bool_Success = obj_FileOp.method_FileSystem_Prep_For_File_Save(strFilePathAndNameFull_Export, bool_Delete=True)
                        pass   
                        
                        boolSuccess = obj_Sampling.method_Export_Genotypes(pop_SubSample, intAlleleAdjust, strFilePathAndNameFull_Export, bool_Prevent_Internal_Function_Console_Output, bool_Prevent_External_Function_Console_Output, (True, False, True), list_VSPs)
                    pass
                
                    #bool_Genepop_Export_PF_Full_SP = False
                    if self.objSSParametersLocal.bool_Genepop_Export_PF_Full_SP:                    
                        ''' Get random sub-sample of the population if required
                            set to 0 if all required
                        '''
                        float_SubSample_Percent_Of_SP = self.objSSParametersLocal.float_SubSample_Percent_Of_PF_Full_SP
                        int_Pop_Size = pop_In.subPopSize()
                        if float_SubSample_Percent_Of_SP > 0:
                            intSubSample_Size = int(float_SubSample_Percent_Of_SP * int_Pop_Size)
                        else:
                            intSubSample_Size = int_Pop_Size
                        pass
                        pop_SubSample = obj_Sampling.method_Draw_Random_Pop_SubSample(pop_In, intSubSample_Size)
                        ''' Export for full pop '''
                        strFilePathAndNameFull_Export = strFilePathAndNameFull_Export_Prefix + globalsSS.Genepop_Results_File_Details.static_Genepop_File_Name__Full_SP_Post_Fertilization + str_File_Name_Suffix + globalsSS.Genepop_Results_File_Details.static_Genepop_File_Suffix__Full_SP_Post_Fertilization
                        ''' Prep File system path for save '''
                        with FileHandler() as obj_FileOp:
                            bool_Success = obj_FileOp.method_FileSystem_Prep_For_File_Save(strFilePathAndNameFull_Export, bool_Delete=True)
                        pass   
                        boolSuccess = obj_Sampling.method_Export_Genotypes(pop_SubSample, intAlleleAdjust, strFilePathAndNameFull_Export, bool_Prevent_Internal_Function_Console_Output, bool_Prevent_External_Function_Console_Output, (True, False, True))
                    pass

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    self.obj_Log_Debug_Display.debug('>>> ' + str_Message_Location)
                    pass                     
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
                #DEBUG_OFF
                                                        
                return True
            
            def methodOutput_VSP_To_GENEPOP_By_Gen(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    if self.objSSParametersLocal.listOutputReplicates_PopulationGENEPOP_FSTAT_Pop_Dump != []:
    
                        for intOutputReplicate in self.objSSParametersLocal.listOutputReplicates_PopulationGENEPOP_FSTAT_Pop_Dump:
                            if intOutputReplicate == self.objSSParametersLocal.intCurrentReplicate: 
                   
    
                                boolOutputVSPs = param
                                listOutputParams= self.objSSParametersLocal.listOutputParams_PopulationGENEPOP_FSTAT_Pop_Dump
    
                                for intOutputFertilisation in self.objSSParametersLocal.listOutputGenerations_PopulationGENEPOP_FSTAT_Pop_Dump:
                                        if intOutputFertilisation == self.objSSParametersLocal.intCurrentTemporalFertilisation: 
                                           with SSOutputHandler() as SSOutputOperation:
                                                #DEBUG ON
                                                #listOutputDestinations = ['console', outputFileName]
                                                #DEBUG OFF
                        
                                                #boolGenepopFormat = True
                                                #boolSaveAsOnePop = True
                                                #intAlleleLengthFormat = 3
                                                #listVirtSubPopsToOutput = [0]
    
                                                listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_PopulationGENEPOP_FSTAT_Pop_Dump
               
                                    
                                                if boolOutputVSPs:
                                                    for intVirtSubPopToOutput in listVirtSubPopsToOutput:
                                                        #Define filename
                                                        strOutfile = self.objSSParametersLocal.outfilePath + self.objSSParametersLocal.strFileNameProgramPrefix + 'gen_' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation) + '_VSP_' + str(intVirtSubPopToOutput) + "_" + self.objSSParametersLocal.strFilenameEmbeddedFields + '_rep_' + str(self.objSSParametersLocal.intCurrentReplicate).zfill(3) + '.genepop.gp_ssim'
                                                        listVirtSubPopsToOutput = [intVirtSubPopToOutput]
                                        
                                                        #Create file
                                                        with SSOutputHandler() as SSOutputOperation:
                                                            SSOutputOperation.methodSaveFile_GENEPOP_FSTAT_By_Pop(pop, listOutputParams[0], boolOutputVSPs, listVirtSubPopsToOutput, listOutputParams[1], listOutputParams[2], strOutfile)
                                                            pass
                                                else:
                                                    #Define filename
                                                    strOutfile = self.objSSParametersLocal.outfilePath + self.objSSParametersLocal.strFileNameProgramPrefix + 'gen_' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation) + '_POP_' + self.objSSParametersLocal.strFilenameEmbeddedFields + '_rep_' + str(self.objSSParametersLocal.intCurrentReplicate).zfill(3) + '.genepop.gp_ssim'
                                                    listVirtSubPopsToOutput = [globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo]
                                        
                                                    #Create file
                                                    SSOutputOperation.methodSaveFile_GENEPOP_FSTAT_By_Pop(pop, listOutputParams[0], boolOutputVSPs, listVirtSubPopsToOutput, listOutputParams[1], listOutputParams[2], strOutfile)
                                                    pass
            
                return True

            def methodOutput_outputAgeNeFinalTotalsInfo(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
                    
                    listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_AgeNe_Reporting
                    if listOutputDestinations != []:
                        
                        #TESTING_ON
                        objSSReporting = object_SSReportingObject()
                        #TESTING_OFF
                        
                        with SSOutputHandler() as SSOutputOperation:
                            #DEBUG ON
                            #listOutputDestinations = ['console', outputFileName]
                            #DEBUG OFF
                        
                            #intSubPop=0
                            boolHeader= param[0]
                            boolFooter = param[1]
                            listSexes = param[2]
                            SSOutputOperation.methodOutput_Sim_AgeNe_Final_Total_Info_Reporting(self, pop, boolHeader, boolFooter, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, self.objSSParametersLocal.boolBurnIn, objSSReporting, listSexes)
                
                return True
            
            def methodOutput_outputAgeNeLifeTablesTotalsInfo(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
                    
                    listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_AgeNe_Reporting
                    if listOutputDestinations != []:
                        
                        #TESTING_ON
                        objSSReporting = object_SSReportingObject()
                        #TESTING_OFF
                        
                        with SSOutputHandler() as SSOutputOperation:
                            #DEBUG ON
                            #listOutputDestinations = ['console', outputFileName]
                            #DEBUG OFF
                        
                            #intSubPop=0
                            boolHeader= param[0]
                            boolFooter = param[1]
                            listSexes = param[2]
                            SSOutputOperation.methodOutput_Sim_AgeNe_LifeTables_Total_Info_Reporting(self, pop, boolHeader, boolFooter, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, self.objSSParametersLocal.boolBurnIn, objSSReporting, listSexes)
                
                return True

            def methodOutput_outputAgeNeDemographicTablesTotalsInfo(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
                    
                    listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_AgeNe_Reporting
                    if listOutputDestinations != []:
                        
                        #TESTING_ON
                        objSSReporting = object_SSReportingObject()
                        #TESTING_OFF
                        
                        with SSOutputHandler() as SSOutputOperation:
                            #DEBUG ON
                            #listOutputDestinations = ['console', outputFileName]
                            #DEBUG OFF
                        
                            #intSubPop=0
                            boolHeader= param[0]
                            boolFooter = param[1]
                            listSexes = param[2]
                            SSOutputOperation.methodOutput_Sim_AgeNe_DemographicTables_Total_Info_Reporting(self, pop, boolHeader, boolFooter, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, self.objSSParametersLocal.boolBurnIn, objSSReporting, listSexes)
                
                return True
         
            def methodOutput_outputAgeNeDetailInfo(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
                    
                    listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_AgeNe_Reporting
                    if listOutputDestinations != []:
                        
                        #TESTING_ON
                        objSSReporting = object_SSReportingObject()
                        #TESTING_OFF
                        
                        with SSOutputHandler() as SSOutputOperation:
                            #DEBUG ON
                            #listOutputDestinations = ['console', outputFileName]
                            #DEBUG OFF
                        
                            #intSubPop=0
                            boolHeader= param[0]
                            boolFooter = param[1]
                            listSexes = param[2]
                            
                            SSOutputOperation.methodOutput_Sim_AgeNe_Detail_Info_Reporting(self, pop, boolHeader, boolFooter, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, self.objSSParametersLocal.boolBurnIn, objSSReporting, listSexes)
                return True
 
            def method_LogOutput_outputAgeNeDetailInfo(self, pop, param):
                    
                #TESTING_ON
                objSSReporting = object_SSReportingObject()
                #TESTING_OFF
                
                with SSOutputHandler() as SSOutputOperation:
                    #DEBUG ON
                    #listOutputDestinations = ['console', outputFileName]
                    #DEBUG OFF
                
                    #intSubPop=0
                    boolHeader= param[0]
                    boolFooter = param[1]
                    listSexes = param[2]
                    obj_Logging = param[3]
                    obj_Results_Log = param[4]
                    str_Heading_Prefix_1 = param[5]
                    dict_Results = param[6]
                    
                    SSOutputOperation.method_LogOutput_Sim_AgeNe_Detail_Info_Reporting(obj_Logging, obj_Results_Log, str_Heading_Prefix_1, boolHeader, boolFooter, self, pop, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, self.objSSParametersLocal.boolBurnIn, objSSReporting, listSexes, dict_Results)
                return True
 
            def method_LogOutput_outputAgeNeLifeTableTotals(self, pop, param):
                    
                #TESTING_ON
                objSSReporting = object_SSReportingObject()
                #TESTING_OFF
                
                with SSOutputHandler() as SSOutputOperation:
                    #DEBUG ON
                    #listOutputDestinations = ['console', outputFileName]
                    #DEBUG OFF
                
                    #intSubPop=0
                    boolHeader= param[0]
                    boolFooter = param[1]
                    listSexes = param[2]
                    obj_Logging = param[3]
                    obj_Results_Log = param[4]
                    str_Heading_Prefix_1 = param[5]
                    dict_Results = param[6]
                    
                    SSOutputOperation.method_LogOutput_Sim_AgeNe_LifeTables_Total_Info_Reporting(obj_Logging, obj_Results_Log, str_Heading_Prefix_1, boolHeader, boolFooter, self, pop, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, self.objSSParametersLocal.boolBurnIn, objSSReporting, listSexes, dict_Results)
                return True
 
            def method_LogOutput_outputAgeNeDemographicTableTotals(self, pop, param):

                #TESTING_ON
                objSSReporting = object_SSReportingObject()
                #TESTING_OFF
                
                with SSOutputHandler() as SSOutputOperation:
                    #DEBUG ON
                    #listOutputDestinations = ['console', outputFileName]
                    #DEBUG OFF
                
                    #intSubPop=0
                    boolHeader= param[0]
                    boolFooter = param[1]
                    listSexes = param[2]
                    obj_Logging = param[3]
                    obj_Results_Log = param[4]
                    str_Heading_Prefix_1 = param[5]
                    dict_Results = param[6]
                    
                    SSOutputOperation.method_LogOutput_Sim_AgeNe_DemographicTables_Total_Info_Reporting(obj_Logging, obj_Results_Log, str_Heading_Prefix_1, boolHeader, boolFooter, self, pop, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, self.objSSParametersLocal.boolBurnIn, objSSReporting, listSexes, dict_Results)
                return True
 
            def method_LogOutput_outputAgeNeFinalTotals(self, pop, param):
                    
                #TESTING_ON
                objSSReporting = object_SSReportingObject()
                #TESTING_OFF
                
                with SSOutputHandler() as SSOutputOperation:
                    #DEBUG ON
                    #listOutputDestinations = ['console', outputFileName]
                    #DEBUG OFF
                
                    #intSubPop=0
                    boolHeader= param[0]
                    boolFooter = param[1]
                    listSexes = param[2]
                    obj_Logging = param[3]
                    obj_Results_Log = param[4]
                    str_Heading_Prefix_1 = param[5]
                    dict_Results = param[6]
                    
                    SSOutputOperation.method_LogOutput_Sim_AgeNe_Final_Total_Info_Reporting(obj_Logging, obj_Results_Log, str_Heading_Prefix_1, boolHeader, boolFooter, self, pop, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, self.objSSParametersLocal.boolBurnIn, objSSReporting, listSexes, dict_Results)
                return True
 
            '''@profile'''
            def methodOutput_outputPopulationTemporalProcessingSummaryInfo(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
                    
                    listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_PopulationTemporalProcessingSummaryInfo
                    
                    if self.objSSParametersLocal.listOutputDestinations_PopulationTemporalProcessingSummaryInfo != []:
                        
                        with SSOutputHandler() as SSOutputOperation:
                            #DEBUG ON
                            #listOutputDestinations = ['console', outputFileName]
                            #DEBUG OFF
                        
                            SSOutputOperation.method_Output_Sim_General_Message_With_Time(listOutputDestinations, 'SimTemporalProcessingSummaryInfo', boolIsHeader=True, boolReportDateTime=True, boolTimeSinceLastGeneralMessage=True)
                            boolHeader= param[0]
                            boolFooter = param[1]
                            SSOutputOperation.methodOutput_SimTemporalProcessingSummaryInfo(self, pop, boolHeader, boolFooter, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, self.objSSParametersLocal.boolBurnIn)
                            
                return True
                
            
            def methodOutput_outputPopulationLifeStageTotals(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
                
                    if self.objSSParametersLocal.listOutputDestinations_PopulationLifeStageTotals != []:
                        
                        pop = self.method_SplitLifeStagesIntoVSPs_By_LifeStage(pop, boolUpdate=True)
                        
                        ##############  REPORT: Info field Statistics
                        # age_in_months
                        with SSAnalysisHandler() as objSSAnalysisOperation:
                            listVSPs = objSSAnalysisOperation.method_Get_VSP_List(pop)
                            
#                         simupop.stat(pop, minOfInfo=['age_in_months'], subPops=simupop.ALL_AVAIL, vars=['minOfInfo']),
#                         simupop.stat(pop, meanOfInfo=['age_in_months'], subPops=simupop.ALL_AVAIL, vars=['meanOfInfo']),
#                         simupop.stat(pop, maxOfInfo=['age_in_months'], subPops=simupop.ALL_AVAIL, vars=['maxOfInfo']),
                        simupop.stat(pop, minOfInfo=['age_in_months'], subPops=listVSPs, vars=['minOfInfo_sp']),
                        simupop.stat(pop, meanOfInfo=['age_in_months'], subPops=listVSPs, vars=['meanOfInfo_sp']),
                        simupop.stat(pop, maxOfInfo=['age_in_months'], subPops=listVSPs, vars=['maxOfInfo_sp']),

                        with SSOutputHandler() as SSOutputOperation:
                            #DEBUG ON
                            #listOutputDestinations = ['console', outputFileName]
                            #DEBUG OFF
                        
                            #intSubPop=0
                            
                            SSOutputOperation.methodOutput_SimLifeStageSummaryInfo(self, pop, param[0], param[1], self.objSSParametersLocal.listOutputDestinations_PopulationLifeStageTotals, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation)
                
                return True

            
            def methodOutput_outputPopulationAgeClassTotals(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
                
                    if self.objSSParametersLocal.listOutputDestinations_PopulationAgeClassTotals != []:
                        
                        pop = self.method_SplitLifeStagesIntoVSPs_By_AgeClass(pop)

                        ##############  REPORT: Info field Statistics
                        # age_in_months
                        with SSAnalysisHandler() as objSSAnalysisOperation:
                            listVSPs = objSSAnalysisOperation.method_Get_VSP_List(pop)
                            
#                         simupop.stat(pop, minOfInfo=['age_in_months'], subPops=simupop.ALL_AVAIL, vars=['minOfInfo']),
#                         simupop.stat(pop, meanOfInfo=['age_in_months'], subPops=simupop.ALL_AVAIL, vars=['meanOfInfo']),
#                         simupop.stat(pop, maxOfInfo=['age_in_months'], subPops=simupop.ALL_AVAIL, vars=['maxOfInfo']),
                        simupop.stat(pop, minOfInfo=['age_in_months'], subPops=listVSPs, vars=['minOfInfo_sp']),
                        simupop.stat(pop, meanOfInfo=['age_in_months'], subPops=listVSPs, vars=['meanOfInfo_sp']),
                        simupop.stat(pop, maxOfInfo=['age_in_months'], subPops=listVSPs, vars=['maxOfInfo_sp']),
                        
                        with SSOutputHandler() as SSOutputOperation:
                            #DEBUG ON
                            #listOutputDestinations = ['console', outputFileName]
                            #DEBUG OFF
                        
                            #intSubPop=0
                            SSOutputOperation.methodOutput_SimAgeClassSummaryInfo(self, pop, param[0], param[1], self.objSSParametersLocal.listOutputDestinations_PopulationAgeClassTotals, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation)
                
                return True

            def methodOutput_outputPopulationDump(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
                 
                    if self.objSSParametersLocal.listOutputDestinations_PopulationDump != []:
    
                        with SSOutputHandler() as SSOutputOperation:
                            #DEBUG ON
                            #listOutputDestinations = ['console', outputFileName]
                            #DEBUG OFF
        
                            #listInfoFields=['age', 'ind_id', 'father_id', 'mother_id', 'fertilisation', 'birth_generation']
                            #listInfoFields=['age', 'ind_id', 'father_id', 'mother_id', 'birth_generation']
                            listInfoFields=['age', 'ind_id', 'father_id', 'mother_id']
                            #intSubPop=0
                            strMethod_Call_Origin = param[0]
                            listDumpParameters = [globalsSS.SP_SubPops.static_intSP_SubPop_Primary, 2, 30, True, True, listInfoFields, strMethod_Call_Origin]
                                    
                            SSOutputOperation.methodOutput_SimPopDump(pop, self.objSSParametersLocal.listOutputDestinations_PopulationDump, listDumpParameters)
                
                return True

            def methodOutput_Population_Individuals_For_Initial_Pedigree(self, pop):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    #Check if file is required.  No filenames listed assumes that it is NOT required.
                    if self.objSSParametersLocal.listOutputDestinations_PopulationIndividualsInitialPedigree != []:
    
                        #intSubPop=0
    
                        listOutputDestinations = list(self.objSSParametersLocal.listOutputDestinations_PopulationIndividualsInitialPedigree)
                        #Output all VSPs
                        listVirtSubPopsToOutput= []
                        intNumberVirtualSubPops = self.pop.numVirtualSubPop()
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            #All are required. Create list of all VSPs to process
                            listCurrentVSP =[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)]
                            listSingleVirtualSubPop = listCurrentVSP[0]
                            listVirtSubPopsToOutput.append(listSingleVirtualSubPop)
                            pass
                        
                        with SSOutputHandler() as SSOutputOperation:
                            SSOutputOperation.methodOutput_Population_Individuals_For_Pedigree(self.objSSParametersLocal, pop, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput)

                return True

            def methodOutput_Population_Individuals_For_Pedigree(self, pop):

                #DEBUG_ON
                #Stops run of this function
                #self.objSSParametersLocal.listOutputDestinations_PopulationIndividualsPedigree = []
                #DEBUG_OFF
                
                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    #Check if file is required.  No filenames listed assumes that it is NOT required.
                    if self.objSSParametersLocal.listOutputDestinations_PopulationIndividualsPedigree != []:
    
                        #intSubPop=0
    
                        listOutputDestinations = list(self.objSSParametersLocal.listOutputDestinations_PopulationIndividualsPedigree)
                        #Only capture the offspring generation (0,0) to produce pedigree without duplicates
                        listVirtSubPopsToOutput= [(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)]
    
                        with SSOutputHandler() as SSOutputOperation:
                            SSOutputOperation.methodOutput_Population_Individuals_For_Pedigree(self.objSSParametersLocal, pop, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput)

                return True

            def methodOutput_outputPopulationIndividuals_ILF_Custom_1_Reporting_Experiment(self, pop, listPopSubSamples, listSubSampleVSPsToOutput, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    #DEBUG_ON
                    #Stops run of this function
                    #return True
                    #DEBUG_OFF

                    #intSubPop=0
                    
                    listFullPopVSPsToOutput= self.objSSParametersLocal.listOutputVSPs_Custom_1_Reporting_Experiment_Dump
                    listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_1_Reporting_Experiment_Dump
                    
                    #Check if only specific VSPs are required.  None assumes that ALL ARE REQUIRED.
                    if listFullPopVSPsToOutput == []:
                      
                        #Get a list of all the VSPs
                        listFullPopVSPsToOutput = []
                        with SSAnalysisHandler() as objSSAnalysisOperation:
                            listVSPs = objSSAnalysisOperation.method_Get_VSP_List(self.pop, boolReportVSPIfEmpty=True)
                            for intVirtualSubPop in range(0, len(listVSPs)):
                                #All are required. Create list of all VSPs to process
                                listCurrentVSP =[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)]
                                listSingleVirtualSubPop = listCurrentVSP[0]
                                listFullPopVSPsToOutput.append(listSingleVirtualSubPop)

                    
                    dictPropertiesNotSuppressed = self.objSSParametersLocal.dictCustom_1_PropertiesNotSuppressed
                    dictOfObjectPropertiesToReport = self.objSSParametersLocal.dictCustom_1_OfObjectPropertiesToReport
                    with SSOutputHandler() as SSOutputOperation:
                        SSOutputOperation.method_Output_Population_Individuals_To_ILF_Files_With_Custom_1_Reporting(self.objSSParametersLocal, pop, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listFullPopVSPsToOutput, listPopSubSamples, listSubSampleVSPsToOutput, dictPropertiesNotSuppressed, dictOfObjectPropertiesToReport, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport)
                
                return True

            
            def methodOutput_outputPopulationIndividuals_ILF_Custom_2_Reporting_Experiment(self, pop, listPopSubSamples, listSubSampleVSPsToOutput, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    #DEBUG_ON
                    #Stops run of this function
                    #return True
                    #DEBUG_OFF

                    #intSubPop=0
                    
                    listFullPopVSPsToOutput= self.objSSParametersLocal.listOutputVSPs_Custom_2_Reporting_Experiment_Dump
                    listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_2_Reporting_Experiment_Dump
                    
                    #Check if only specific VSPs are required.  None assumes that ALL ARE REQUIRED.
                    if listFullPopVSPsToOutput == []:
                      
                        #Get a list of all the VSPs
                        listFullPopVSPsToOutput = []
                        with SSAnalysisHandler() as objSSAnalysisOperation:
                            listVSPs = objSSAnalysisOperation.method_Get_VSP_List(self.pop, boolReportVSPIfEmpty=True)
                            for intVirtualSubPop in range(0, len(listVSPs)):
                                #All are required. Create list of all VSPs to process
                                listCurrentVSP =[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)]
                                listSingleVirtualSubPop = listCurrentVSP[0]
                                listFullPopVSPsToOutput.append(listSingleVirtualSubPop)

                    
                    dictPropertiesNotSuppressed = self.objSSParametersLocal.dictCustom_2_PropertiesNotSuppressed
                    dictOfObjectPropertiesToReport = self.objSSParametersLocal.dictCustom_2_OfObjectPropertiesToReport
                    with SSOutputHandler() as SSOutputOperation:
                        SSOutputOperation.method_Output_Population_Individuals_To_ILF_Files_With_Custom_2_Reporting(self.objSSParametersLocal, pop, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listFullPopVSPsToOutput, listPopSubSamples, listSubSampleVSPsToOutput, dictPropertiesNotSuppressed, dictOfObjectPropertiesToReport, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport)
                
                return True
            
            def methodOutput_outputPopulationIndividuals_ILF_Custom_3_Reporting_Experiment(self, pop, listSPsToOutput, boolOutputHeader):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    #DEBUG_ON
                    #Stops run of this function
                    #return True
                    #DEBUG_OFF

                    #intSubPop=0
                    
                    #listFullPopVSPsToOutput= self.objSSParametersLocal.listOutputVSPs_Custom_3_Reporting_Experiment_Dump
                    listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_3_Reporting_Experiment_Dump
                    
                    
                    dictPropertiesNotSuppressed = self.objSSParametersLocal.dictCustom_3_PropertiesNotSuppressed
                    dictOfObjectPropertiesToReport = self.objSSParametersLocal.dictCustom_3_OfObjectPropertiesToReport
                    with SSOutputHandler() as SSOutputOperation:
                        SSOutputOperation.method_Output_Population_Individuals_To_ILF_Files_With_Custom_3_Reporting(self.objSSParametersLocal, pop, listOutputDestinations, self.objSSParametersLocal.intCurrentTemporalFertilisation, listSPsToOutput, dictPropertiesNotSuppressed, dictOfObjectPropertiesToReport, boolOutputHeader)
                
                return True

            def methodOutput_outputPopulationIndividuals_ILF_Custom_4_Reporting_Experiment(self, pop, listPopSubSamples, listSubSampleVSPsToOutput, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    #DEBUG_ON
                    #Stops run of this function
                    #return True
                    #DEBUG_OFF

                    #intSubPop=0
                    
                    listFullPopVSPsToOutput= self.objSSParametersLocal.listOutputVSPs_Custom_4_Reporting_Experiment_Dump
                    listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_4_Reporting_Experiment_Dump
                    
                    #Check if only specific VSPs are required.  None assumes that ALL ARE REQUIRED.
                    if listFullPopVSPsToOutput == []:
                      
                        #Get a list of all the VSPs
                        listFullPopVSPsToOutput = []
                        with SSAnalysisHandler() as objSSAnalysisOperation:
                            listVSPs = objSSAnalysisOperation.method_Get_VSP_List(self.pop, boolReportVSPIfEmpty=True)
                            for intVirtualSubPop in range(0, len(listVSPs)):
                                #All are required. Create list of all VSPs to process
                                listCurrentVSP =[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)]
                                listSingleVirtualSubPop = listCurrentVSP[0]
                                listFullPopVSPsToOutput.append(listSingleVirtualSubPop)

                    
                    dictPropertiesNotSuppressed = self.objSSParametersLocal.dictCustom_4_PropertiesNotSuppressed
                    dictOfObjectPropertiesToReport = self.objSSParametersLocal.dictCustom_4_OfObjectPropertiesToReport
                    with SSOutputHandler() as SSOutputOperation:
                        SSOutputOperation.method_Output_Population_Individuals_To_ILF_Files_With_Custom_4_Reporting(self.objSSParametersLocal, pop, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listFullPopVSPsToOutput, listPopSubSamples, listSubSampleVSPsToOutput, dictPropertiesNotSuppressed, dictOfObjectPropertiesToReport, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport)
                
                return True
            
            
            def methodOutput_outputPopulationIndividuals_ILF_Custom_5_Reporting_Experiment(self, pop, listPopSubSamples, listSubSampleVSPsToOutput, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    #DEBUG_ON
                    #Stops run of this function
                    #return True
                    #DEBUG_OFF

                    #intSubPop=0
                    
                    listFullPopVSPsToOutput= self.objSSParametersLocal.listOutputVSPs_Custom_5_Reporting_Experiment_Dump
                    listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_Custom_5_Reporting_Experiment_Dump
                    
                    #Check if only specific VSPs are required.  None assumes that ALL ARE REQUIRED.
                    if listFullPopVSPsToOutput == []:
                      
                        #Get a list of all the VSPs
                        listFullPopVSPsToOutput = []
                        with SSAnalysisHandler() as objSSAnalysisOperation:
                            listVSPs = objSSAnalysisOperation.method_Get_VSP_List(self.pop, boolReportVSPIfEmpty=True)
                            for intVirtualSubPop in range(0, len(listVSPs)):
                                #All are required. Create list of all VSPs to process
                                listCurrentVSP =[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)]
                                listSingleVirtualSubPop = listCurrentVSP[0]
                                listFullPopVSPsToOutput.append(listSingleVirtualSubPop)

                    
                    dictPropertiesNotSuppressed = self.objSSParametersLocal.dictCustom_5_PropertiesNotSuppressed
                    dictOfObjectPropertiesToReport = self.objSSParametersLocal.dictCustom_5_OfObjectPropertiesToReport
                    with SSOutputHandler() as SSOutputOperation:
                        SSOutputOperation.method_Output_Population_Individuals_To_ILF_Files_With_Custom_5_Reporting(self.objSSParametersLocal, pop, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listFullPopVSPsToOutput, listPopSubSamples, listSubSampleVSPsToOutput, dictPropertiesNotSuppressed, dictOfObjectPropertiesToReport, boolOutputHeader, boolReusePrimedTopLevelOutputObject, boolReuseObjectPropertiesToReport)
                
                return True
            
            
            def method_Output_Population_Individuals_To_ILF_Files_With_AgeNe_Reporting(self, pop, boolOutputHeader):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    #DEBUG_ON
                    #Stops run of this function
                    #return True
                    #DEBUG_OFF

                    #intSubPop=0
                    
                    listFullPopVSPsToOutput= self.objSSParametersLocal.listOutputVSPs_AgeNe_Reporting
                    listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_AgeNe_Reporting
                    
                    #Check if only specific VSPs are required.  None assumes that ALL ARE REQUIRED.
                    if listFullPopVSPsToOutput == []:
                      
                        intNumberVirtualSubPops = self.pop.numVirtualSubPop()
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            #All are required. Create list of all VSPs to process
                            listCurrentVSP =[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)]
                            listSingleVirtualSubPop = listCurrentVSP[0]
                            listFullPopVSPsToOutput.append(listSingleVirtualSubPop)
                            pass
                        pass
                    
                    #dictPropertiesNotSuppressed = self.objSSParametersLocal.dictPropertiesNotSuppressed
                    #dictOfObjectPropertiesToReport = self.objSSParametersLocal.dictOfObjectPropertiesToReport
                    with SSOutputHandler() as SSOutputOperation:
                        SSOutputOperation.method_Output_Population_Individuals_To_ILF_Files_With_AgeNe_Reporting(self.objSSParametersLocal, pop, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, boolOutputHeader)
                
                return True

            def methodOutput_outputPopulationIndividuals_ILF_Dump(self, pop):

                if self.objSSParametersLocal.boolBurnIn:# and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    #DEBUG_ON
                    #Stops run of this function
                    #return True
                    #DEBUG_OFF

                    #intSubPop=0
                    
                    #listOutputDestinations = list(self.objSSParametersLocal.listOutputDestinations_ILF_PopulationIndividualsDump)
                    listOutputDestinations = self.objSSParametersLocal.listOutputDestinations_ILF_PopulationIndividualsDump
                    listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_ILF_PopulationIndividualsDump
                    
                    #Check if only specific VSPs are required.  None assumes that ALL ARE REQUIRED.
                    if listVirtSubPopsToOutput == []:
                      
                        intNumberVirtualSubPops = self.pop.numVirtualSubPop()
                        for intVirtualSubPop in range(0, intNumberVirtualSubPops):
                            #All are required. Create list of all VSPs to process
                            listCurrentVSP =[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)]
                            listSingleVirtualSubPop = listCurrentVSP[0]
                            listVirtSubPopsToOutput.append(listSingleVirtualSubPop)
                            pass
                        pass
                    
                    with SSOutputHandler() as SSOutputOperation:
                        SSOutputOperation.method_Output_Population_Individuals_To_ILF_Files(self.objSSParametersLocal, pop, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
                
                return True

#             def methodOutput_outputPopulationIndividuals_ILF_Dump_NEW(self, pop):
# 
#                 #intSubPop=0
#                 
#                 listOutputDestinations = list(self.objSSParametersLocal.listOutputDestinations_ILF_PopulationIndividualsDump)
#                 listVirtSubPopsToOutput= self.objSSParametersLocal.listOutputVSPs_ILF_PopulationIndividualsDump
#                 
#                 #Check if only specific VSPs are required.  None assumes that ALL ARE REQUIRED.
#                 if listVirtSubPopsToOutput != []:
#                   
#                     intNumberVirtualSubPops = self.pop.numVirtualSubPop()
#                     for intVirtualSubPop in range(0, intNumberVirtualSubPops):
#                         #All are required. Create list of all VSPs to process
#                         listCurrentVSP =[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)]
#                         listSingleVirtualSubPop = listCurrentVSP[0]
#                         listVirtSubPopsToOutput.append(listSingleVirtualSubPop)
#                     
#                     with SSOutputHandler() as SSOutputOperation:
#                       
#                         #Check if file is required.  No filenames listed assumes that it is NOT required.
#                         if self.objSSParametersLocal.listOutputDestinations_ILF_PopulationIndividualsDump != []:
#                         
#                             #Check if only specific REPLICATES are required.  None assumes that ALL ARE REQUIRED.
#                             if self.objSSParametersLocal.listOutputReplicates_ILF_PopulationIndividualsDump != []:
#                         
#                                 #Process a required REPLICATE if it is the CURRENT REPLICATE
#                                 for intOutputReplicate in self.objSSParametersLocal.listOutputReplicates_ILF_PopulationIndividualsDump:
#                                     if intOutputReplicate == self.objSSParametersLocal.intCurrentReplicate: 
#                         
#                                         #Check if only specific GENERATIONS are required.  None assumes that ALL ARE REQUIRED. 
#                                         if self.objSSParametersLocal.listOutputGenerations_ILF_PopulationIndividualsDump !=[]:
#                                             
#                                             #Process a required GENERATION if it is the CURRENT GENERATION
#                                             listOutputDestinationsPerGen = []
#                                             for intOutputFertilisation in self.objSSParametersLocal.listOutputGenerations_ILF_PopulationIndividualsDump:
#                                                 if intOutputFertilisation == self.objSSParametersLocal.intCurrentTemporalFertilisation: 
#                                                        
#                                                     #Check if only specific VSPs are required.  None assumes that ALL ARE REQUIRED. 
#                                                     if self.objSSParametersLocal.listOutputVSPs_ILF_PopulationIndividualsDump !=[]:
#                                                         #Write out only the specified VSPs
#                                                                 
#                                                         intCount = len(listOutputDestinations)
#                                                         if (listOutputDestinations[0] == 'console') & (intCount == 1):
#                                                                 # If the list length is <= 1 then only console output is required and the filenames should not be added to the list
#                                                                 pass
#                                                         else:
#                                                             #Add output files for specified VSPS for a specified GENERATION for a specified REPLICATE
#                                                             outputFileName = self.objSSParametersLocal.outfilePath + self.objSSParametersLocal.strFileNameProgramPrefix + 'individ_log_gen_' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation) + '_' + self.objSSParametersLocal.strFilenameEmbeddedFields + '_rep_' + str(self.objSSParametersLocal.intCurrentReplicate).zfill(3) + '.il_ssim'
#                                                             list.append(listOutputDestinationsPerGen, outputFileName) #NOTE: Special output destinations list, not the general output generations list
#                         
#                                                             #Write ALL VSPs for specified GENERATIONS for a specified REPLICATE to....
#                                                             #SPECIAL CASE: Writes to a separate file for each GENERATION and no output is written to central ILF file   
#                                                             SSOutputOperation.methodOutput_SimPopIndividulsDump(self.objSSParametersLocal, pop, listOutputDestinationsPerGen, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
#                                                             pass                                                        
#                                                     else:
#                                                         intCount = len(listOutputDestinations)
#                                                         if (listOutputDestinations[0] == 'console') & (intCount == 1):
#                                                                 # If the list lenght is <= 1 then only console output is required and the filenames should not be added to the list
#                                                                 pass
#                                                         else:
#                                                             #Write ALL VSPs for a specified GENERATION for a specified REPLICATE to central ILF file    
#                                                             SSOutputOperation.methodOutput_SimPopIndividulsDump(self.objSSParametersLocal, pop, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
#                                                             pass
#                                                 else:
#                                                     #CURRENT GENERATION is NOT required.
#                                                     pass
#                                             #End of GENERATION FOR Loop
#                                         else:
#                                             #Write specified VSPs for ALL GENERATIONS for a specified REPLICATE to central ILF file
#                                             SSOutputOperation.methodOutput_SimPopIndividulsDump(self.objSSParametersLocal, pop, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
#                                             pass
#                                     else:
#                                         #CURRENT REPLICATE is NOT required.
#                                         pass
#                                 #End of REPLICATE FOR Loop
#                             else:
#                                 #Write specified VSPs for ALL GENERATIONS for ALL REPLICATES to central ILF file
#                                 SSOutputOperation.methodOutput_SimPopIndividulsDump(self.objSSParametersLocal, pop, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation, listVirtSubPopsToOutput)
#                                 pass
#                         else:
#                             #Output is NOT Required
#                             pass
#                 return True

#             def methodOutput_outputPopulationIndividuals_ILF_Dump_ORIG(self, pop):
# 
#                 if self.objSSParametersLocal.listOutputDestinations_ILF_PopulationIndividualsDump !=[]:
# 
#                     with SSOutputHandler() as SSOutputOperation:
#                         #DEBUG ON
#                         #listOutputDestinations = ['console', outputFileName]
#                         #DEBUG OFF
# 
#                         listOutputDestinations = list(self.objSSParametersLocal.listOutputDestinations_ILF_PopulationIndividualsDump)
#                         intCount = len(listOutputDestinations)
#                         if (listOutputDestinations[0] == 'console') & (intCount == 1):
#                                 # If the list lenght is <= 1 then only console output is required and the filenames should not be added to the list
#                                 pass
#                         else:
#                             for intOutputFertilisation in self.objSSParametersLocal.listOutputGenerations_PopulationIndividualsDump:
#                                 if intOutputFertilisation == self.objSSParametersLocal.intCurrentTemporalFertilisation:
#                                     outputFileName = self.objSSParametersLocal.outfilePath + self.objSSParametersLocal.strFileNameProgramPrefix + 'individ_log_gen_' + str(self.objSSParametersLocal.intCurrentTemporalFertilisation) + '_' + self.objSSParametersLocal.strFilenameEmbeddedFields + '_rep_' + str(self.objSSParametersLocal.intCurrentReplicate).zfill(3) + '.il_ssim'
#                                     list.append(listOutputDestinations, outputFileName)
#                                     break
#                     
#                         #intSubPop=0
#                                 
#                         SSOutputOperation.methodOutput_SimPopIndividulsDump(self.objSSParametersLocal, pop, listOutputDestinations, globalsSS.SP_SubPops.static_intSP_SubPop_Primary, self.objSSParametersLocal.intCurrentTemporalFertilisation)
# 
#                 return True

            def method_OutputPopulationOffspringTotalsByParent(self, pop, param):
                
                #DEBUG_ON
                #Stops run of this function
                #self.objSSParametersLocal.listOutputDestinations_PopulationOffspringTotalsByParent = []
                #DEBUG_OFF

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:
                
                    if self.objSSParametersLocal.listOutputDestinations_PopulationOffspringTotalsByParent != []:
                        
                        
                        with SSOutputHandler() as SSOutputOperation:
                            #DEBUG ON
                            #listOutputDestinations_PopulationOffspringTotalsByParent = ['console', outputFileName]
                            #listOutputDestinations_PopulationOffspringTotalsByParent = ['console']
                            #param = 0
                            #DEBUG OFF
    
                            #intSubPop = 0
                            intVirtualSubPop = param
                            
                            SSOutputOperation.method_Output_Population_Offspring_Totals_By_Parent(pop, self.objSSParametersLocal.listOutputDestinations_PopulationOffspringTotalsByParent, self.objSSParametersLocal.listOffspringNumberParameters,  globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVirtualSubPop)
                    
                return True
            
            def method_Output_Population_Allele_Frequencies(self, pop, param):

                if self.objSSParametersLocal.boolBurnIn and self.objSSParametersLocal.boolSuppressBurnInOutput:
                    pass
                else:

                    if self.objSSParametersLocal.listOutputDestinations_PopulationAlleleStatistics != []:
    
                        with SSOutputHandler() as SSOutputOperation:
                            #DEBUG ON
                            #listOutputDestinations_PopulationAlleleStatistics = ['console', outputFileName]
                            #listOutputDestinations_PopulationAlleleStatistics = ['console']
                            #param = 2
                            #DEBUG OFF
    
                            #intSubPop = 0
                            listVirtualSubPop = param
                            
                            SSOutputOperation.method_Output_Population_Allele_Frequencies(pop, self.objSSParametersLocal.listOutputDestinations_PopulationAlleleStatistics, listVirtualSubPop)
                
                return True


            '''
            --------------------------------------------------------------------------------------------------------
            # CLASS FINALISATION
            --------------------------------------------------------------------------------------------------------
            '''

            def __del__(self):

                #print('!!!!!!!!!!!!!!!!SharkSimOperation died!!!!!!!!!!!!!!!!')
                
                return None
            
            
            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful


        self.SharkSimOperation_obj = SharkSimOperation() 
        return self.SharkSimOperation_obj
 
    def __exit__(self, type, value, traceback): 
        self.SharkSimOperation_obj.classCleanUp()