#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS
#
#------------------< Import python modules


# PROCESSING Imports
from copy import deepcopy as copy__deepcopy
from collections import OrderedDict
#from collections import Counter
from collections import Counter as collections__Counter
#import rpy2.robjects as robjects
from math import log
import sys, traceback
from math import sqrt as math__sqrt
from decimal import *
from numpy import sum as numpy__sum
# DEBUG Imports
from logging import getLogger as logging__getLogger

#import objgraph
import pdb
from memory_profiler import profile
#------------------< Import simupop modules
from simuPOP import *
import simuPOP as simupop
#------------------< Import DCB_General modules
from AutoVivificationHandler import AutoVivificationHandler
# DEBUG Imports
from handler_Debug import Timer
from handler_Debug import Timer2
from handler_Debug import Debug_Location
from handler_Debug import Debug_Location as dcb_Debug_Location
#------------------< Import SharkSim modules
from globals_SharkSim import globalsSS
from object_SSAgeNe_LifeTable import object_SSAgeNe_LifeTable
from object_SSAgeNe_DemographicTable import object_SSAgeNe_DemographicTable
from object_SSAgeNe import object_SSAgeNe
from AnalysisHandler import AnalysisHandler

#from SSOutputHandler import SSOutputHandler
#
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
gstringModuleName='SSAnalysisHandler.py'
gstringClassName='SSAnalysisOperation'

class SSAnalysisHandler:
    """Handle SS Analysis Operations"""
    
    def __init__(self):
        
        pass    


    def __enter__(self):


        
        class SSAnalysisOperation:


            def __init__(self):
                
                
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
            
            def method_Pause_Console(self):
                
                #objOutput.write('\n')
                raw_input('\n Pausing for output review - Press return to continue... \n')
                #objOutput.write('\n') 
                                     
            '''
            --------------------------------------------------------------------------------------------------------
            # Parent / Offspring Processing
            --------------------------------------------------------------------------------------------------------
            '''

            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # METHOD 2 Parent / Offspring Stats
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
            def method_Count_Offspring_PerParent_For_VirtualSubPop(self, pop, dictMaleFamSize, dictFemaleFamSize, listPotentialMaleParents, listPotentialFemaleParents, intSubPop, intVirtualSubPop=-1):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass   
            
                try:
                    intVirtualSubPop = int(intVirtualSubPop)
                except:
                    self.obj_Log_Default_Display.error('intVirtualSubPop is not an integer: ' + str(intVirtualSubPop))
                    raise
                pass
                                      
                '''
                Count the number of offspring per parent in any VSP
                '''

                #Get Sires and count offspring into a dictionary
                
                if dictMaleFamSize == {}:
                    dictMaleFamSize = AutoVivificationHandler()  
                    if intVirtualSubPop == -1:
                        dictMaleFamSize = self.method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(pop, intSubPop)
                    else:
                        dictMaleFamSize = self.method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(pop, intSubPop, intVirtualSubPop)
                
                #Get Dames and count offspring into a dictionary
                
                if dictFemaleFamSize == {}:
                    dictFemaleFamSize = AutoVivificationHandler()
                    if intVirtualSubPop == -1:
                        dictFemaleFamSize = self.method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(pop, intSubPop)
                    else:
                        dictFemaleFamSize = self.method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(pop, intSubPop, intVirtualSubPop)
                    pass
                pass

                #Get all individuals for the parent generation and if they are not in the Sire/Dame Dict
                #...they were not parent, so add them to the dict with zero offspring

            
                dictfamSize = OrderedDict()
                for key_Outer, value_Dict in dictMaleFamSize.iteritems():
                    dictfamSize[simupop.MALE] = {key:valuelist for key,valuelist in value_Dict.iteritems()}
                pass
                for key_Outer, value_Dict in dictFemaleFamSize.iteritems():
                    dictfamSize[simupop.FEMALE] = {key:valuelist for key,valuelist in value_Dict.iteritems()}
                pass

                int_Effective_Male_Total = len(dictfamSize[simupop.MALE])
                int_Male_Count = 0
                for ind_id in listPotentialMaleParents:
                    parent = int(ind_id)
                    int_Male_Count += 1
                    if parent in dictfamSize[simupop.MALE]:
                        pass
                    else:
                        dictfamSize[simupop.MALE][parent] = 0
                    pass
                pass
            
                int_Effective_Female_Total = len(dictfamSize[simupop.FEMALE])
                int_Female_Count = 0
                for ind_id in listPotentialFemaleParents:
                    parent = int(ind_id)
                    int_Female_Count += 1
                    if parent in dictfamSize[simupop.FEMALE]:
                        pass
                    else:
                        dictfamSize[simupop.FEMALE][parent] = 0
                    pass
                pass

                int_Count = len(listPotentialMaleParents) + len(listPotentialFemaleParents)
                
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    self.obj_Log_Debug_Display.debug('Total Male Effective Parents: ' + str(int_Effective_Male_Total))
                    self.obj_Log_Debug_Display.debug('Total Female Effective Parents: ' + str(int_Effective_Female_Total))                
                    self.obj_Log_Debug_Display.debug('Total Male INEffective Parents: ' + str(int_Male_Count - int_Effective_Male_Total))
                    self.obj_Log_Debug_Display.debug('Total Female INEffective Parents: ' + str(int_Female_Count - int_Effective_Female_Total))                
                    self.obj_Log_Debug_Display.debug('Total Male Potential Parents: ' + str(int_Male_Count))
                    self.obj_Log_Debug_Display.debug('Total Female Potential Parents: ' + str(int_Female_Count))
                    self.obj_Log_Debug_Display.debug('Total Potential Parents: ' + str(int_Count))
                    #simupop.dump(pop)
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
                            
                return dictfamSize

            def method_Count_Offspring_PerParent_For_VirtualSubPop_OLD(self, pop, dictMaleFamSize, dictFemaleFamSize, intSubPop, intVirtualSubPop=-1):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass   
            
                          
                '''
                Count the number of offspring per parent in any VSP
                '''

                #Get Sires and count offspring into a dictionary
                
                if dictMaleFamSize == {}:
                    dictMaleFamSize = AutoVivificationHandler()  
                    if intVirtualSubPop == -1:
                        dictMaleFamSize = self.method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(pop, intSubPop)
                    else:
                        dictMaleFamSize = self.method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(pop, intSubPop, intVirtualSubPop)
                
                #Get Dames and count offspring into a dictionary
                
                if dictFemaleFamSize == {}:
                    dictFemaleFamSize = AutoVivificationHandler()
                    if intVirtualSubPop == -1:
                        dictFemaleFamSize = self.method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(pop, intSubPop)
                    else:
                        dictFemaleFamSize = self.method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(pop, intSubPop, intVirtualSubPop)
                    pass
                pass

                #Get all individuals for the parent generation and if they are not in the Sire/Dame Dict
                #...they were not parent, so add them to the dict with zero offspring
                try:
                    intVirtualSubPop = int(intVirtualSubPop)
                    simupopIndivPotentialParents = None
                    if intVirtualSubPop == -1:
                        simupopIndivPotentialParents = pop.individuals([intSubPop])
                    else:
                        simupopIndivPotentialParents = pop.individuals([intSubPop, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult])
                    pass
                except:
                    self.obj_Log_Default_Display.error('intVirtualSubPop is not an integer: ' + str(intVirtualSubPop))
                    raise
                pass
            
#                 dictMaleFamSizeDCopy = AutoVivificationHandler()
#                 dictMaleFamSizeDCopy = copy__deepcopy(dictMaleFamSize)
#                 dictFemaleFamSizeDCopy = AutoVivificationHandler()
#                 dictFemaleFamSizeDCopy = copy__deepcopy(dictFemaleFamSize)
#                 dictfamSize = AutoVivificationHandler()
#                 dictfamSize = dict(list(dictMaleFamSizeDCopy.items()) + list(dictFemaleFamSizeDCopy.items())) 


                #copied = {key:valuelist[:] for (key,valuelist) in original.iteritems()}                

                dictfamSize = OrderedDict()
                for key_Outer, value_Dict in dictMaleFamSize.iteritems():
                    dictfamSize[simupop.MALE] = {key:valuelist for key,valuelist in value_Dict.iteritems()}
                pass
                for key_Outer, value_Dict in dictFemaleFamSize.iteritems():
                    dictfamSize[simupop.FEMALE] = {key:valuelist for key,valuelist in value_Dict.iteritems()}
                pass

                int_Count = 0
#                 for simupopIndiv in simupopIndivPotentialParents:
#                     parent = int(simupopIndiv.ind_id)
#                     if parent in dictfamSize[simupop.MALE]:
#                         pass
#                     else:
#                         if parent in dictfamSize[simupop.FEMALE]:
#                             pass
#                         else:
#                             dictfamSize[simupopIndiv.sex()][parent] = 0
#                         pass
#                     pass
#                     int_Count += 1

                int_Effective_Male_Total = len(dictfamSize[simupop.MALE])
                int_Effective_Female_Total = len(dictfamSize[simupop.FEMALE])
                
                int_Male_Count = 0
                int_Female_Count = 0
                for simupopIndiv in simupopIndivPotentialParents:
                    parent = int(simupopIndiv.ind_id)
                    int_Sex = simupopIndiv.sex()
                    if int_Sex == simupop.MALE:
                        int_Male_Count += 1
                        if parent in dictfamSize[simupop.MALE]:
                            pass
                        else:
                            dictfamSize[simupop.MALE][parent] = 0
                        pass
                    else:
                        int_Female_Count += 1
                        if parent in dictfamSize[simupop.FEMALE]:
                            pass
                        else:
                            dictfamSize[simupop.FEMALE][parent] = 0
                        pass
                    pass
                    int_Count += 1
                pass



                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    self.obj_Log_Debug_Display.debug('Total Male Effective Parents: ' + str(int_Effective_Male_Total))
                    self.obj_Log_Debug_Display.debug('Total Female Effective Parents: ' + str(int_Effective_Female_Total))                
                    self.obj_Log_Debug_Display.debug('Total Male INEffective Parents: ' + str(int_Male_Count - int_Effective_Male_Total))
                    self.obj_Log_Debug_Display.debug('Total Female INEffective Parents: ' + str(int_Female_Count - int_Effective_Female_Total))                
                    self.obj_Log_Debug_Display.debug('Total Male Potential Parents: ' + str(int_Male_Count))
                    self.obj_Log_Debug_Display.debug('Total Female Potential Parents: ' + str(int_Female_Count))
                    self.obj_Log_Debug_Display.debug('Total Potential Parents: ' + str(int_Count))
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    str_Message = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message, bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
                            
                return dictfamSize


            def method_Count_Offspring_Per_ParentPair_For_Pop(self, pop):
                '''
                Count the number of offspring per parent in any pop
                '''
                # get the parents of each offspring
                parents = [(x, y) for x, y in zip(pop.indInfo('mother_id'),
                    pop.indInfo('father_id'))]
                # Individuals with identical parents are considered as siblings.
                famSize = []
                lastParent = (-1, -1)
                for parent in parents:
                    if parent == lastParent:
                        famSize[-1] += 1
                    else:
                        lastParent = parent
                        famSize.append(1)

                return famSize


            def method_Count_Offspring_Per_Sorted_ParentPair_For_VirtualSubPop(self, pop, intSubPop, intVirtualSubPop):
                '''
                Count the number of offspring per parent in any pop
                '''     
                
                # get the parents of each offspring
                parents = [(x, y) for x, y in zip(pop.indInfo('mother_id',  subPop=[intSubPop, intVirtualSubPop]),
                    pop.indInfo('father_id', subPop=[intSubPop, intVirtualSubPop]))]
                
                parents = sorted(parents)

                # Individuals with identical parents are considered as siblings.
                famSize = []
                lastParentPair = (-1, -1)
                for parentPair in parents:
                    if parentPair == lastParentPair:
                        famSize[-1] += 1
                    else:
                        lastParentPair = parentPair
                        famSize.append(1)

                return famSize


            def method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(self, pop, intSubPop, intVirtualSubPop=-1):

                try:
                    intVirtualSubPop = int(intVirtualSubPop)
                except:
                    self.obj_Log_Default_Display.error('intVirtualSubPop is not an integer: ' + str(intVirtualSubPop))
                    raise
                pass
                            
                #Get Dames and count offspring into a dictionary
                if intVirtualSubPop == -1:
                    listDamesSorted = sorted(pop.indInfo('mother_id', subPop=[intSubPop]))
                else:
                    listDamesSorted = sorted(pop.indInfo('mother_id', subPop=[intSubPop, intVirtualSubPop]))

                dictfamSize = AutoVivificationHandler()
                lastParent = -1
                for parent in listDamesSorted:
                    if parent == lastParent:
                        dictfamSize[simupop.FEMALE][int(parent)] += 1
                    else:
                       lastParent = parent
                       dictfamSize[simupop.FEMALE][int(parent)] = 1
                pass
                        
                return dictfamSize


            def method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(self, pop, intSubPop, intVirtualSubPop=-1):
                '''
                Count the number of offspring per SIRE in any pop
                '''
                
                try:
                    intVirtualSubPop = int(intVirtualSubPop)
                except:
                    self.obj_Log_Default_Display.error('intVirtualSubPop is not an integer: ' + str(intVirtualSubPop))
                    raise
                pass                
                    
                #Get Sires and count offspring into a dictionary
                if intVirtualSubPop == -1:
                    listSiresSorted = sorted(pop.indInfo('father_id', subPop=[intSubPop]))
                else:
                    listSiresSorted = sorted(pop.indInfo('father_id', subPop=[intSubPop, intVirtualSubPop]))
                
                dictfamSize = AutoVivificationHandler()
                lastParent = -1
                for parent in listSiresSorted:
                    if parent == lastParent:
                        dictfamSize[simupop.MALE][int(parent)] += 1
                    else:
                       lastParent = parent
                       dictfamSize[simupop.MALE][int(parent)] = 1
                pass

                return dictfamSize


            def method_Count_Offspring_Per_Parent_Given_Sex_For_VirtualSubPop_Into_Dict(self, pop, intSubPop, intVirtualSubPop, strSex):
                '''
                Count the number of offspring per parents of a given sex in any pop
                '''
                if strSex == globalsSS.SexConstants.static_stringSexMale:
                    static_simupop_Sex = globalsSS.SexConstants.static_simupop_Sex_MALE
                    #Get parents and count offspring into a dictionary
                    listParentsSorted = sorted(pop.indInfo('father_id', subPop=[intSubPop, intVirtualSubPop]))
                elif strSex == globalsSS.SexConstants.static_stringSexFemale: 
                    static_simupop_Sex = globalsSS.SexConstants.static_simupop_Sex_FEMALE
                    #Get parents and count offspring into a dictionary
                    listParentsSorted = sorted(pop.indInfo('mother_id', subPop=[intSubPop, intVirtualSubPop]))
                
                dictfamSize = AutoVivificationHandler()
                lastParent = -1
                for parent in listParentsSorted:
                    if parent == lastParent:
                        dictfamSize[strSex][int(parent)] += 1
                    else:
                        lastParent = parent
                        dictfamSize[strSex][int(parent)] = 1
                pass

                return dictfamSize


            def method_Count_Offspring_Per_Sire_For_VirtualSubPop(self, pop, intSubPop, intVirtualSubPop=1):
                '''
                Count the number of offspring per SIRE in any pop
                '''     
                try:
                    intVirtualSubPop = int(intVirtualSubPop)
                except:
                    self.obj_Log_Default_Display.error('intVirtualSubPop is not an integer: ' + str(intVirtualSubPop))
                    raise
                pass
                            
                # get the parents of each offspring
                if intVirtualSubPop == -1:
                    listSiresSorted = sorted(pop.indInfo('father_id', subPop=[intSubPop, intVirtualSubPop]))
                else:
                    listSiresSorted = sorted(pop.indInfo('father_id', subPop=[intSubPop, intVirtualSubPop]))

                famSize = []
                lastParent = -1
                for parent in listSiresSorted:
                    if parent == lastParent:
                        famSize[-1] += 1
                    else:
                        lastParent = parent
                        famSize.append(1)

                return famSize


            def method_Count_Offspring_Per_Sorted_Parent_For_VirtualSubPop(self, pop, intSubPop, intVirtualSubPop, stringParentInfoField):
                '''
                Count the number of offspring per parent as defined by the PARENT Info Field in any pop
                '''     
                
                # get the parents of each offspring
                
                listParentsSorted = sorted(pop.indInfo(stringParentInfoField, subPop=[intSubPop, intVirtualSubPop]))

                famSize = []
                lastParent = -1
                for parent in listParentsSorted:
                    if parent == lastParent:
                        famSize[-1] += 1
                    else:
                        lastParent = parent
                        famSize.append(1)

                return famSize


            def method_List_ParentID_Per_Offspring_For_VirtualSubPop(self, pop, intSubPop, intVirtualSubPop, stringParentInfoField, boolSorted):
                '''
                List Parent ID per offspring as defined by the PARENT Info Field in any pop
                '''     
                
                # get the parents of each offspring
                
                listParents = pop.indInfo(stringParentInfoField, subPop=[intSubPop, intVirtualSubPop])
                
                # Return all parentIDs as integers
                listParents = list(map(int, listParents))

                # Remove duplicates
                listParents = list(set(listParents))

                if boolSorted:
                    listParents = sorted(listParents)
                
                return listParents
            
            '''@profile'''
            def method_PutativeParentListFromVSP(self, pop_In, intSubPop):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass                     
            
                '''
                This is FASTER than the previous versions
                '''

                pop_Life_Stage_Mature_By_Sex = self.method_Split_Reproductively_Mature_VSP_By_Sex(pop_In)
                    
                listPutativeFemaleParents = list(pop_Life_Stage_Mature_By_Sex.indInfo('ind_id',  subPop=[globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult_Female]))
                
                listPutativeMaleParents = list(pop_Life_Stage_Mature_By_Sex.indInfo('ind_id',  subPop=[globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult_Male]))
                
                
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    self.obj_Log_Debug_Display.debug('listPutativeFemaleParents Count: ' + str(len(listPutativeFemaleParents)))
                    self.obj_Log_Debug_Display.debug('listPutativeFemaleParents: ' + str(listPutativeFemaleParents))
                    self.obj_Log_Debug_Display.debug('listPutativeMaleParents Count: ' + str(len(listPutativeMaleParents)))
                    self.obj_Log_Debug_Display.debug('listPutativeMaleParents: ' + str(listPutativeMaleParents))
                    #simupop.dump(pop)
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
            
                return listPutativeFemaleParents, listPutativeMaleParents

            
            #def method_Embryo_Offspring_Parent_Ne_Summary_Stats_METHOD_2(self, dictSireOffspringCount, dictDameOffspringCount, dictOffspringCount, dict_Results, intSubPop, intVSP):


            def method_Embryo_Offspring_Parent_Ne_Summary_Stats_METHOD_2(self, dictSireOffspringCount, dictDameOffspringCount, dictOffspringCount, dict_Results):
                
    
                if (len(dictOffspringCount[simupop.MALE]) > 0) | (len(dictOffspringCount[simupop.FEMALE]) > 0):
                    
                    with AnalysisHandler() as objAnalysisOperation:

                        #Construct a list of POTENTIAL MALE PARENT offspring counts
                        listMaleOffspringCount = []
                        listMaleOffspringCount = dictOffspringCount[simupop.MALE].values()
                        
                        floatMeanLitterSizeForMaleParents_MeanKsex = objAnalysisOperation.method_Get_Mean_From_A_List(listMaleOffspringCount)
                        floatMeanVarianceLitterSizeForMaleParents_VarKsex = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listMaleOffspringCount)
                        integerNumberofParentsForMaleParents_Nsex = len(listMaleOffspringCount)
                        floatNeDemographicByMaleParentsFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_By_Parental_Sex_Given_Known_Offspring(integerNumberofParentsForMaleParents_Nsex, floatMeanLitterSizeForMaleParents_MeanKsex, floatMeanVarianceLitterSizeForMaleParents_VarKsex)
                        
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Male_Potential_Parent] = integerNumberofParentsForMaleParents_Nsex
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Offspring_Per_Male_Potential_Parent] = round(floatMeanLitterSizeForMaleParents_MeanKsex,4)
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Variance_Offspring_Per_Male_Potential_Parent] = round( floatMeanVarianceLitterSizeForMaleParents_VarKsex,4)
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeMale_Potential_Parents_NeM] = round( floatNeDemographicByMaleParentsFromKnownOffspring,4)

                        #Construct a list of ACTUAL SIRE offspring counts
                        listSireOffspringCount = []
                        listSireOffspringCount = dictSireOffspringCount[simupop.MALE].values()
                        
                        floatMeanLitterSizeForSireParents_MeanKsex = objAnalysisOperation.method_Get_Mean_From_A_List(listSireOffspringCount)
                        floatMeanVarianceLitterSizeForSireParents_VarKsex = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listSireOffspringCount)
                        integerNumberofParentsForSireParents_Nsex = len(listSireOffspringCount)
                        floatNeDemographicBySireParentsFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_By_Parental_Sex_Given_Known_Offspring(integerNumberofParentsForSireParents_Nsex, floatMeanLitterSizeForSireParents_MeanKsex, floatMeanVarianceLitterSizeForSireParents_VarKsex)
                        
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Sires] = integerNumberofParentsForSireParents_Nsex
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Offspring_Per_Sire] = round(floatMeanLitterSizeForSireParents_MeanKsex,4)
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Variance_Offspring_Per_Sire] = round( floatMeanVarianceLitterSizeForSireParents_VarKsex,4)
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeSires_NeS] = round( floatNeDemographicBySireParentsFromKnownOffspring,4)
                        
                        #Construct a list of POTENTIAL FEMALE PARENT offspring counts
                        listFemaleOffspringCount = []
                        listFemaleOffspringCount = dictOffspringCount[simupop.FEMALE].values()
                        
                        floatMeanLitterSizeForFemaleParents_MeanKsex = objAnalysisOperation.method_Get_Mean_From_A_List(listFemaleOffspringCount)
                        floatMeanVarianceLitterSizeForFemaleParents_VarKsex = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listFemaleOffspringCount)
                        integerNumberofParentsForFemaleParents_Nsex = len(listFemaleOffspringCount)
                        floatNeDemographicByFemaleParentsFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_By_Parental_Sex_Given_Known_Offspring(integerNumberofParentsForFemaleParents_Nsex, floatMeanLitterSizeForFemaleParents_MeanKsex, floatMeanVarianceLitterSizeForFemaleParents_VarKsex)
                        
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Female_Potential_Parent] = integerNumberofParentsForFemaleParents_Nsex
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Offspring_Per_Female_Potential_Parent] = round(floatMeanLitterSizeForFemaleParents_MeanKsex,4)
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Variance_Offspring_Per_Female_Potential_Parent] = round(floatMeanVarianceLitterSizeForFemaleParents_VarKsex,4)
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Ne_DemoFemale_Potential_Parents_NeF] = round(floatNeDemographicByFemaleParentsFromKnownOffspring,4)
                        
                        #Construct a list of ACTUAL DAME offspring counts
                        listDameOffspringCount = []
                        listDameOffspringCount = dictDameOffspringCount[simupop.FEMALE].values()
                        
                        floatMeanLitterSizeForDameParents_MeanKsex = objAnalysisOperation.method_Get_Mean_From_A_List(listDameOffspringCount)
                        floatMeanVarianceLitterSizeForDameParents_VarKsex = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listDameOffspringCount)
                        integerNumberofParentsForDameParents_Nsex = len(listDameOffspringCount)
                        floatNeDemographicByDameParentsFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_By_Parental_Sex_Given_Known_Offspring(integerNumberofParentsForDameParents_Nsex, floatMeanLitterSizeForDameParents_MeanKsex, floatMeanVarianceLitterSizeForDameParents_VarKsex)
                        
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Dames] = integerNumberofParentsForDameParents_Nsex
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Offspring_Per_Dame] = round(floatMeanLitterSizeForDameParents_MeanKsex,4)
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Variance_Offspring_Per_Dame] = round(floatMeanVarianceLitterSizeForDameParents_VarKsex,4)
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeDames_NeD] = round(floatNeDemographicByDameParentsFromKnownOffspring,4)
                        
                        listBothSexesPotentialParentsOffspringCount = []
                        for intCount in listMaleOffspringCount:
                            listBothSexesPotentialParentsOffspringCount.append(intCount)
                        for intCount in listFemaleOffspringCount:
                            listBothSexesPotentialParentsOffspringCount.append(intCount)
                        
                        floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listBothSexesPotentialParentsOffspringCount)
                        floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listBothSexesPotentialParentsOffspringCount)
                        integerNumberofParentsForBothSexesPotentialParents_Nsex = len(listBothSexesPotentialParentsOffspringCount)
                        floatNeDemographicGivenBothSexesPotentialParentsNeFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_From_Known_Offspring_Given_Parental_Sex_Ne(floatNeDemographicByMaleParentsFromKnownOffspring, floatNeDemographicByFemaleParentsFromKnownOffspring)
                        
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Potential_Parents_PP] = integerNumberofParentsForBothSexesPotentialParents_Nsex
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Offspring_Per_PP] = round(floatMean,4)
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Variance_Offspring_Per_PP] = round( floatVariance,4)
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP] = round( floatNeDemographicGivenBothSexesPotentialParentsNeFromKnownOffspring,4)
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NePP_Rato_Nc] = round((floatNeDemographicGivenBothSexesPotentialParentsNeFromKnownOffspring / integerNumberofParentsForBothSexesPotentialParents_Nsex),4)
                        
                        listBothSexesEffectiveParentsOffspringCount = []
                        for intCount in listSireOffspringCount:
                            listBothSexesEffectiveParentsOffspringCount.append(intCount)
                        for intCount in listDameOffspringCount:
                            listBothSexesEffectiveParentsOffspringCount.append(intCount)
                        
                        floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listBothSexesEffectiveParentsOffspringCount)
                        floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listBothSexesEffectiveParentsOffspringCount)
                        integerNumberofParentsForBothSexesEffectiveParents_Nsex = len(listBothSexesEffectiveParentsOffspringCount)
                        floatNeDemographicGivenBothSexesEffectiveParentsNeFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_From_Known_Offspring_Given_Parental_Sex_Ne(floatNeDemographicBySireParentsFromKnownOffspring, floatNeDemographicByDameParentsFromKnownOffspring)
                        
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Effective_Parents_EP] = integerNumberofParentsForBothSexesEffectiveParents_Nsex
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Offspring_Per_EP] = round(floatMean,4)
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Mean_Variance_Offspring_Per_EP] = round( floatVariance,4)
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeEP] = round( floatNeDemographicGivenBothSexesEffectiveParentsNeFromKnownOffspring,4)
                        dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_2.static_Str_Colname_Demo_NeEP_Rato_Nc] = round((floatNeDemographicGivenBothSexesEffectiveParentsNeFromKnownOffspring / integerNumberofParentsForBothSexesPotentialParents_Nsex),4) #NOTE: Division by Nc
                        
                    pass
                pass
                
                return dict_Results

            
            '''@profile'''
            def method_Embryo_Offspring_Parent_Ne_Summary_Stats_METHOD_1(self, pop_In, dict_Results, objSSParametersLocal):
                
                ''' get potential & effective parent per mating from Embryo VSP '''
                listEffectiveFemaleParents = self.method_Effective_Female_List_From_Embryo_VSP(pop_In)
                listEffectiveMaleParents = self.method_Effective_Male_List_From_Embryo_VSP(pop_In)
                listTupEffectiveDameSirePairs = self.method_Effective_Dame_Sire_Parent_Pair_List(listEffectiveFemaleParents, listEffectiveMaleParents)
                
                counterEffectiveFemaleParents = self.method_Get_Effective_Female_Counter(listEffectiveFemaleParents)
                counterEffectiveMaleParents = self.method_Get_Effective_Male_Counter(listEffectiveMaleParents)
                counterTupEffectiveDameSirePairs = self.method_Get_Effective_Dame_Sire_Pair_Counter(listTupEffectiveDameSirePairs)

                int_NonUnique_Female_Effective_Gametes = self.method_Get_NonUnique_Effective_Female_Count(counterEffectiveFemaleParents)
                dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_NonUnique_Female_Effective_Gametes] = int_NonUnique_Female_Effective_Gametes
                int_NonUnique_Male_Effective_Gametes = self.method_Get_NonUnique_Effective_Male_Count(counterEffectiveMaleParents)
                dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_NonUnique_Male_Effective_Gametes] = int_NonUnique_Male_Effective_Gametes
                int_NonUnique_Effective_Dame_Sire_Gamete_Pair_Count = self.method_Get_NonUnique_Effective_Dame_Sire_Parent_Pair_Count(counterTupEffectiveDameSirePairs)
                dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_NonUnique_Effective_Dame_Sire_Gamete_Pair_Count] = int_NonUnique_Effective_Dame_Sire_Gamete_Pair_Count
                
                int_Unique_Female_Effective_Gametes = self.method_Get_Unique_Effective_Female_Count(counterEffectiveFemaleParents)
                dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_Unique_Female_Effective_Gametes] = int_Unique_Female_Effective_Gametes
                int_Unique_Male_Effective_Gametes = self.method_Get_Unique_Effective_Male_Count(counterEffectiveMaleParents)
                dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_Unique_Male_Effective_Gametes] = int_Unique_Male_Effective_Gametes
                int_Unique_Effective_Dame_Sire_Gamete_Pair_Count = self.method_Get_Unique_Effective_Dame_Sire_Parent_Pair_Count(counterTupEffectiveDameSirePairs)
                dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_Unique_Effective_Dame_Sire_Gamete_Pair_Count] = int_Unique_Effective_Dame_Sire_Gamete_Pair_Count
                
                int_Total_NonUnique_Gametes = int_NonUnique_Female_Effective_Gametes + int_NonUnique_Male_Effective_Gametes
                dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_Total_NonUnique_Gametes] = int_Total_NonUnique_Gametes                                  
                int_Total_Unique_Gametes = int_Unique_Female_Effective_Gametes + int_Unique_Male_Effective_Gametes                                  
                dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_int_Total_Unique_Gametes] = int_Total_Unique_Gametes
           
                #float_Ne_By_Sex = self.method_Calculate_Demographic_Ne_By_Sex(int_Unique_Female_Effective_Gametes, int_Unique_Male_Effective_Gametes)
                dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_Demo_Ne_By_Sex] = int_Total_Unique_Gametes

                dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating] = objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating
                dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn] = objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn
                dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn] = objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn
                dict_Results[globalsSS.Colnames_Parent_Offspring_Stats_METHOD_1.static_Str_Colname_float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate] = objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate
                
                return dict_Results 

            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # METHOD 1 Parent / Offspring Stats
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
           
            def method_Effective_Female_List_From_Embryo_VSP(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass                  
            
                '''
                This is FASTER than the previous versions
                '''
                listEffectiveFemaleParents = []
                listEffectiveFemaleParents = list(pop_In.indInfo('mother_id',  subPop=[0, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo]))
                
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    self.obj_Log_Debug_Display.debug('listEffectiveFemaleParents: ' + str(listEffectiveFemaleParents))
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    str_Message = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message, bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
            
                return listEffectiveFemaleParents


            def method_Effective_Male_List_From_Embryo_VSP(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass                        
            
                '''
                This is FASTER than the previous versions
                '''
                listEffectiveMaleParents = []
                listEffectiveMaleParents = list(pop_In.indInfo('father_id',  subPop=[0, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo]))
                
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    self.obj_Log_Debug_Display.debug('listEffectiveMaleParents: ' + str(listEffectiveMaleParents))
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    str_Message = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message, bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
            
                return listEffectiveMaleParents


            def method_Effective_Dame_Sire_Parent_Pair_List(self, listEffectiveFemaleParents, listEffectiveMaleParents):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass         
                                    
                '''
                This is FASTER than the previous versions
                '''

                listTupEffectiveDameSirePairs = zip(listEffectiveFemaleParents, listEffectiveMaleParents)
                
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    self.obj_Log_Debug_Display.debug('listTupEffectiveDameSirePairs: ' + str(listTupEffectiveDameSirePairs))
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    str_Message = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message, bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
            
                return listTupEffectiveDameSirePairs


            def method_Get_Effective_Dame_Sire_Pair_Counter(self,listTupEffectiveDameSirePairs):

                counterTupEffectiveDameSirePairs=collections__Counter(listTupEffectiveDameSirePairs)
                
                return counterTupEffectiveDameSirePairs


            def method_Get_NonUnique_Effective_Dame_Sire_Parent_Pair_Count(self, counterTupEffectiveDameSirePairs):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass 
            
             
                int_NonUnique_Effective_Dame_Sire_Parent_Pair_Count = len(counterTupEffectiveDameSirePairs.values())

 
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    self.obj_Log_Debug_Display.debug('int_NonUnique_Effective_Dame_Sire_Parent_Pair_Count :' + str(int_NonUnique_Effective_Dame_Sire_Parent_Pair_Count))
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    str_Message = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message, bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
             
                return int_NonUnique_Effective_Dame_Sire_Parent_Pair_Count
       
            
            def method_Get_Unique_Effective_Dame_Sire_Parent_Pair_Count(self, counterTupEffectiveDameSirePairs):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass 
            
                            
                int_Unique_Effective_Dame_Sire_Parent_Pair_Count = len(counterTupEffectiveDameSirePairs.values())


                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    self.obj_Log_Debug_Display.debug('int_Unique_Effective_Dame_Sire_Parent_Pair_Count :' + str(int_Unique_Effective_Dame_Sire_Parent_Pair_Count))
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    str_Message = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message, bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                                            
                return int_Unique_Effective_Dame_Sire_Parent_Pair_Count


            def method_Get_Effective_Female_Counter(self,listEffectiveFemaleParents):
                
                #listEffectiveFemaleParents = self.method_Effective_Female_List_From_Embryo_VSP(self.pop)

                counterFemaleEffectiveParents=collections__Counter(listEffectiveFemaleParents)
                
                return counterFemaleEffectiveParents


            def method_Get_Effective_Male_Counter(self,listEffectiveMaleParents):
                
                #listEffectiveMaleParents = self.method_Effective_Male_List_From_Embryo_VSP(self.pop)

                counterMaleEffectiveParents=collections__Counter(listEffectiveMaleParents)
        
                return counterMaleEffectiveParents


            def method_Get_NonUnique_Effective_Female_Count(self, counterFemaleEffectiveParents):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
                    
                                    
                int_NonUnique_Female_Effective_Parents = sum(counterFemaleEffectiveParents.values())


                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    self.obj_Log_Debug_Display.debug('int_NonUnique_Female_Effective_Parents :' + str(int_NonUnique_Female_Effective_Parents))
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    str_Message = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message, bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                            
                return int_NonUnique_Female_Effective_Parents


            def method_Get_NonUnique_Effective_Male_Count(self, counterMaleEffectiveParents):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
                    
                    
                int_NonUnique_Male_Effective_Parents = sum(counterMaleEffectiveParents.values())


                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    self.obj_Log_Debug_Display.debug('int_NonUnique_Male_Effective_Parents :' + str(int_NonUnique_Male_Effective_Parents))
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    str_Message = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message, bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
            
                return int_NonUnique_Male_Effective_Parents
      
            
            def method_Get_Unique_Effective_Female_Count(self, counterFemaleEffectiveParents):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
                    
                                    
                int_Unique_Female_Effective_Parents = len(counterFemaleEffectiveParents.values())
                

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    self.obj_Log_Debug_Display.debug('int_Unique_Female_Effective_Parents :' + str(int_Unique_Female_Effective_Parents))
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    str_Message = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message, bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                            
                return int_Unique_Female_Effective_Parents


            def method_Get_Unique_Effective_Male_Count(self, counterMaleEffectiveParents):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
                    
                    
                int_Unique_Male_Effective_Parents = len(counterMaleEffectiveParents.values())
                

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    self.obj_Log_Debug_Display.debug('int_Unique_Male_Effective_Parents :' + str(int_Unique_Male_Effective_Parents))
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    str_Message = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message, bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                            
                return int_Unique_Male_Effective_Parents


            def method_Get_Parent_Offspring_Summary_Stats(self, pop_In, bool_Initialise_Stats, list_Stats_Categories, dict_Results):

                for str_Stats_Category in list_Stats_Categories:                
                    ''' get potential & effective parent per mating from Embryo VSP '''
                    listEffectiveFemaleParents = self.method_Effective_Female_List_From_Embryo_VSP(pop_In)
                    listEffectiveMaleParents = self.method_Effective_Male_List_From_Embryo_VSP(pop_In)
                    listTupEffectiveDameSirePairs = self.method_Effective_Dame_Sire_Parent_Pair_List(listEffectiveFemaleParents, listEffectiveMaleParents)
                    
                    counterEffectiveFemaleParents = self.method_Get_Effective_Female_Counter(listEffectiveFemaleParents)
                    counterEffectiveMaleParents = self.method_Get_Effective_Male_Counter(listEffectiveMaleParents)
                    counterTupEffectiveDameSirePairs = self.method_Get_Effective_Dame_Sire_Pair_Counter(listTupEffectiveDameSirePairs)
    
                    '''assign results to dict keys'''
                    int_NonUnique_Female_Effective_Parents = self.method_Get_NonUnique_Effective_Female_Count(counterEffectiveFemaleParents)
                    dict_Results[str_Stats_Category].update({'int_NonUnique_Female_Effective_Parents':int_NonUnique_Female_Effective_Parents})
                    int_NonUnique_Male_Effective_Parents = self.method_Get_NonUnique_Effective_Male_Count(counterEffectiveMaleParents)
                    dict_Results[str_Stats_Category].update({'int_NonUnique_Male_Effective_Parents':int_NonUnique_Male_Effective_Parents})
                    int_NonUnique_Effective_Dame_Sire_Parent_Pair_Count = self.method_Get_NonUnique_Effective_Dame_Sire_Parent_Pair_Count(counterTupEffectiveDameSirePairs)
                    dict_Results[str_Stats_Category].update({'int_NonUnique_Effective_Dame_Sire_Parent_Pair_Count':int_NonUnique_Effective_Dame_Sire_Parent_Pair_Count})
                    
                    int_Unique_Female_Effective_Parents = self.method_Get_Unique_Effective_Female_Count(counterEffectiveFemaleParents)
                    dict_Results[str_Stats_Category].update({'int_Unique_Female_Effective_Parents':int_Unique_Female_Effective_Parents})
                    int_Unique_Male_Effective_Parents = self.method_Get_Unique_Effective_Male_Count(counterEffectiveMaleParents)
                    dict_Results[str_Stats_Category].update({'int_Unique_Male_Effective_Parents':int_Unique_Male_Effective_Parents})
                    int_Unique_Effective_Dame_Sire_Parent_Pair_Count = self.method_Get_Unique_Effective_Dame_Sire_Parent_Pair_Count(counterTupEffectiveDameSirePairs)
                    dict_Results[str_Stats_Category].update({'int_Unique_Effective_Dame_Sire_Parent_Pair_Count':int_Unique_Effective_Dame_Sire_Parent_Pair_Count})
                    
                    int_Total_NonUnique_Parents = int_NonUnique_Female_Effective_Parents + int_NonUnique_Male_Effective_Parents
                    dict_Results[str_Stats_Category].update({'int_Total_NonUnique_Effective_Parents':int_Total_NonUnique_Parents})                                  
                    int_Total_Unique_Parents = int_Unique_Female_Effective_Parents + int_Unique_Male_Effective_Parents                                  
                    dict_Results[str_Stats_Category].update({'int_Total_Unique_Effective_Parents':int_Total_Unique_Parents})
               
    #                 float_Ne_By_Sex = self.method_Calculate_Demographic_Ne_By_Sex(int_Unique_Female_Effective_Parents, int_Unique_Male_Effective_Parents)
    #                 dict_Results['Demo_Ne_By_Sex_=_4(Nf.Nm)/(Nf+Nm)'] = int_Total_Unique_Parents
    # 
    #                 dict_Results['float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating'] = objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_From_Last_Mating
    #                 dict_Results['float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn'] = objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_BurnIn
    #                 dict_Results['float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn'] = objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_PostBurnIn
    #                 dict_Results['float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate'] = objSSParametersLocal.float_Crow_And_Denniston_1988_DemoNe_Mean_From_Matings_Over_Replicate
    #                 
                return dict_Results 


            def method_Effective_Parent_Summary_Stats_1(self, pop_In, dict_Results_Per_Result_Line):

                ''' get potential & effective parent per mating from Embryo VSP '''
                
                ''' Method 1'''
                listEffectiveFemaleParents = self.method_Effective_Female_List_From_Embryo_VSP(pop_In)
                listEffectiveMaleParents = self.method_Effective_Male_List_From_Embryo_VSP(pop_In)
                #listTupEffectiveDameSirePairs = self.method_Effective_Dame_Sire_Parent_Pair_List(listEffectiveFemaleParents, listEffectiveMaleParents)

                counterEffectiveFemaleParents = self.method_Get_Effective_Female_Counter(listEffectiveFemaleParents)
                counterEffectiveMaleParents = self.method_Get_Effective_Male_Counter(listEffectiveMaleParents)
                #counterTupEffectiveDameSirePairs = self.method_Get_Effective_Dame_Sire_Pair_Counter(listTupEffectiveDameSirePairs)
                
                '''Method 2'''
                with SSAnalysisHandler() as objSSAnalysisOperation:
                    
                    intSubPop = globalsSS.SP_SubPops.static_intSP_SubPop_Primary
                    
                    dictSireOffspringCount = objSSAnalysisOperation.method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(pop_In, intSubPop, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)
                    dictSireOffspringCount = dictSireOffspringCount[simupop.MALE]
                    dictDameOffspringCount = objSSAnalysisOperation.method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(pop_In, intSubPop, globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo)
                    dictDameOffspringCount = dictDameOffspringCount[simupop.FEMALE]
                
                '''Preliminary validity check'''
                int_Method1_Dame_Count = len(counterEffectiveFemaleParents)
                int_Method2_Dame_Count = len(dictDameOffspringCount)
                int_Method1_Sire_Count = len(counterEffectiveMaleParents)
                int_Method2_Sire_Count = len(dictSireOffspringCount)
                
                if int_Method1_Dame_Count != int_Method2_Dame_Count:
                    self.obj_Log_Default_Display.error('int_Method1_Dame_Count: ' + str(int_Method1_Dame_Count) + ' != ' + 'int_Method2_Dame_Count: ' + str(int_Method2_Dame_Count))
                    bool_Dame_Count_Valid = False
                else:
                    bool_Dame_Count_Valid = True
                pass
                if int_Method1_Sire_Count != int_Method2_Sire_Count:
                    self.obj_Log_Default_Display.error('int_Method1_Sire_Count: ' + str(int_Method1_Sire_Count) + ' != ' + 'int_Method2_Sire_Count: ' + str(int_Method2_Sire_Count))
                    bool_Sire_Count_Valid = False
                else:
                    bool_Sire_Count_Valid = True
                pass

                dict_MultiLine_Results = OrderedDict()
                int_MultiLine_Result = 0                
                
                '''Report error or go on to produce results'''
                if bool_Dame_Count_Valid == False or bool_Sire_Count_Valid == False:
                    dict_Results_Per_Result_Line['Dame_Count_Meth1=Meth2'] = str(bool_Dame_Count_Valid)
                    dict_Results_Per_Result_Line['Method_1_Dame_Count'] = str(int_Method1_Dame_Count)
                    dict_Results_Per_Result_Line['Method_2_Dame_Count'] = str(int_Method2_Dame_Count)
                    
                    dict_Results_Per_Result_Line['Sire_Count_Meth1=Meth2'] = str(bool_Sire_Count_Valid)
                    dict_Results_Per_Result_Line['Method_1_Sire_Count'] = str(int_Method1_Sire_Count)
                    dict_Results_Per_Result_Line['Method_2_Sire_Count'] = str(int_Method2_Sire_Count)
                    
                    dict_MultiLine_Results[int_MultiLine_Result] = dict_Results_Per_Result_Line
                else:
                    ''' Extract and Merge results for both Methods'''
                    for keyParent_Ind_ID, valueOffspring_Count in counterEffectiveFemaleParents.items():
    
                        dict_Results = OrderedDict()
                        for key, value in dict_Results_Per_Result_Line.items():
                            dict_Results[key] = value
                        pass
                    
                        dict_Results['Sex'] = globalsSS.SexConstants.static_stringSexFemale
                        dict_Results['Method_1_Effective_Parent_Count'] = str(int_Method1_Dame_Count)
                        dict_Results['Method_2_Effective_Parent_Count'] = str(int_Method2_Dame_Count)
                        dict_Results['Effective_Parent_ID'] = str(int(keyParent_Ind_ID))
                        dict_Results['Effective_Parent_Offspring_Count_Method_1'] = str(valueOffspring_Count)
                        if keyParent_Ind_ID in dictDameOffspringCount:
                            dict_Results['Effective_Parent_Offspring_Count_Method_2'] = str(dictDameOffspringCount[keyParent_Ind_ID])
                        else:
                            dict_Results['Effective_Parent_Offspring_Count_Method_2'] = globalsSS.StringUnexpectedResults.static_stringError_Reporting_IDNotFound
                        pass    
                            
                        dict_MultiLine_Results[int_MultiLine_Result] = dict_Results
                        int_MultiLine_Result += 1
                    pass
                    
                    for keyParent_Ind_ID, valueOffspring_Count in counterEffectiveMaleParents.items():
                        
                        dict_Results = OrderedDict()
                        for key, value in dict_Results_Per_Result_Line.items():
                            dict_Results[key] = value
                        pass
                       
                        dict_Results['Sex'] = globalsSS.SexConstants.static_stringSexMale
                        dict_Results['Method_1_Effective_Parent_Count'] = str(int_Method1_Sire_Count)
                        dict_Results['Method_2_Effective_Parent_Count'] = str(int_Method2_Sire_Count)
                        dict_Results['Effective_Parent_ID'] = str(int(keyParent_Ind_ID))
                        dict_Results['Effective_Parent_Offspring_Count_Method_1'] = str(valueOffspring_Count)
                        if keyParent_Ind_ID in dictSireOffspringCount:
                            dict_Results['Effective_Parent_Offspring_Count_Method_2'] = str(dictSireOffspringCount[keyParent_Ind_ID])
                        else:
                            dict_Results['Effective_Parent_Offspring_Count_Method_2'] = globalsSS.StringUnexpectedResults.static_stringError_Reporting_IDNotFound
                        pass    

                        dict_MultiLine_Results[int_MultiLine_Result] = dict_Results
                        int_MultiLine_Result += 1
                    pass
                pass
            
                return dict_MultiLine_Results
            
            
            def method_List_ParentID_Per_Sorted_ParentPair_For_VirtualSubPop(self, pop, intSubPop, intVirtualSubPop):
                '''
                List Parent ID per mated parent pair in any pop
                '''     
                
                # get the parents of each offspring
                listParents = [(int(x), int(y)) for x, y in zip(pop.indInfo('mother_id',  subPop=[intSubPop, intVirtualSubPop]),
                    pop.indInfo('father_id', subPop=[intSubPop, intVirtualSubPop]))]
                
                # Remove duplicates
                listParents = list(set(listParents))

                # Sort List
                listParents = sorted(listParents)

                return listParents

            '''
            --------------------------------------------------------------------------------------------------------
            # Locus / Allele Processing
            --------------------------------------------------------------------------------------------------------
            '''            
            def method_Statistics_On_Allele_TotalPerLocus_For_VirtualSubPop(self, pop, listSingleVirtualSubPop):

                '''
                Provide statitics on  Allele totals for all loci in any pop
                '''     
                dictVSPAlleleTotals = {}

                dictVSPAlleleInstanceCounts = self.method_Statistics_On_Allele_InstanceCountPerLocus_For_VirtualSubPop(pop, listSingleVirtualSubPop)
                for key, values in dictVSPAlleleInstanceCounts.items():
                    dictVSPAlleleTotals[key] = int(len(values))

                return dictVSPAlleleTotals


            def method_Statistics_On_Allele_InstanceCountPerLocus_For_VirtualSubPop(self, pop, listSingleVirtualSubPop):

                '''
                Provide statitics on  Allele counts for all loci in any pop
                '''     
                
                #simupop.stat(pop, alleleFreq=ALL_AVAIL, subPops=[(intSubPop,intVirtualSubPop)])
                #dictVSPAlleleInstanceCounts = pop.dvars().alleleNum
                #return dictVSPAlleleInstanceCounts

                dictStatistics=[]
                if listSingleVirtualSubPop == 0:
                    dictStatistics = pop.dvars().alleleNum
                else:
                    dictStatistics = pop.dvars(listSingleVirtualSubPop).alleleNum
                
                return dictStatistics


            def method_Statistics_On_Allele_Frequencies_For_VirtualSubPop(self, pop, listSingleVirtualSubPop):

                '''
                Provide statitics on  Allele Frequencies for all loci in any pop
                '''     
                
                #simupop.stat(pop, alleleFreq=ALL_AVAIL, subPops=[(intSubPop,intVirtualSubPop)])
                #dictVSPAlleleFreqs = pop.dvars().alleleFreq
                #return dictVSPAlleleFreqs

                dictStatistics=[]
                if listSingleVirtualSubPop == 0:
                    dictStatistics = pop.dvars().alleleFreq
                else:
                    dictStatistics = pop.dvars(listSingleVirtualSubPop).alleleFreq
                
                return dictStatistics


            '''
            --------------------------------------------------------------------------------------------------------
            # Individual Processing
            --------------------------------------------------------------------------------------------------------
            '''
            def method_List_IndividualID_For_VirtualSubPop_ORIG(self, pop, intSubPop, intVirtualSubPop, stringSortInfoField, boolSorted, ):
                '''
                List Individual IDs for any pop
                '''     
                
                if boolSorted:
                    pop.sortIndividuals(stringSortInfoField)

                iterIndividuals = pop.individuals([intSubPop,intVirtualSubPop])

                listIDs=[]
#                 for intIndividual in listIndividuals:
#                     
#                     listIDs.append(int(intIndividual.ind_id))
                
                listIDs = [indiv.ind_id for indiv in iterIndividuals]
                
                return listIDs
  
            
            def method_List_IndividualID_For_VirtualSubPop(self, pop_In, intSubPop, intVirtualSubPop, stringSortInfoField, boolSorted, ):
                '''
                List Individual IDs for any pop
                '''     
                
                listIDs = list(pop_In.indInfo('ind_id',  subPop=[globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult]))
                
                if boolSorted:
                    listIDs.sort()

                return listIDs


            def method_Count_Individuals_By_InfoField_RETIRED(self, pop, strSimupopInfoField):
                '''
                Count the number of individuals by InfoField in any passed pop
                ''' 
                #odictCountIndividualsWithInfoField = AutoVivificationHandler()
                odictCountIndividualsWithInfoField = OrderedDict()
                    
                #Get list of all indInfo values (each from a unique individual in the pop) = the one specified
                listIndInfoValuesSorted = sorted(pop.indInfo(strSimupopInfoField))

                intCount = 0
                strLastIndInfoValue = listIndInfoValuesSorted[0]
                for strCurrentIndInfoValue in listIndInfoValuesSorted:
                    
                    
                    if strCurrentIndInfoValue == strLastIndInfoValue:
                        intCount += 1
                    else:
                        odictCountIndividualsWithInfoField[strLastIndInfoValue] = intCount
                        intCount = 1
                        strLastIndInfoValue = strCurrentIndInfoValue
                        

                return odictCountIndividualsWithInfoField


            def method_Count_Individuals_By_Sex_By_InfoField_RETIRED(self, pop, strSimupopInfoField, static_simupop_SEX):
                '''
                Count the number of individuals by InfoField in any passed pop for any sex
                ''' 
                #odictCountIndividualsWithInfoField = AutoVivificationHandler()
                odictCountIndividualsWithInfoField = OrderedDict()
                
                pop_sample = pop.extractIndividuals(filter=lambda ind: ind.sex() == static_simupop_SEX)
                    
                #Get list of all indInfo values (each from a unique individual in the pop) = the one specified
                listIndInfoValuesSorted = sorted(pop_sample.indInfo(strSimupopInfoField))

                intCount = 0
                strLastIndInfoValue = listIndInfoValuesSorted[0]
                for strCurrentIndInfoValue in listIndInfoValuesSorted:
                    
                    
                    if strCurrentIndInfoValue == strLastIndInfoValue:
                        intCount += 1
                    else:
                        odictCountIndividualsWithInfoField[strLastIndInfoValue] = intCount
                        intCount = 1
                        strLastIndInfoValue = strCurrentIndInfoValue
                pass
                #Count last item also
                if strCurrentIndInfoValue == strLastIndInfoValue:
                    intCount += 1
                else:
                    odictCountIndividualsWithInfoField[strLastIndInfoValue] = intCount
                    intCount = 1
                    strLastIndInfoValue = strCurrentIndInfoValue
                        

                return odictCountIndividualsWithInfoField
     
            
            def method_Count_Individuals_By_InfoField(self, pop, strSimupopInfoField):
                '''
                Count the number of individuals by InfoField in any passed pop
                ''' 
                
                #Get list of all indInfo values (each from a unique individual in the pop) = the one specified
                #listIndInfoValuesSorted = sorted(pop.indInfo(strSimupopInfoField, subPop=tupVSP))
                listIndInfoValuesSorted = sorted(pop.indInfo(strSimupopInfoField))

                dictCountedIndInfoValues = collections__Counter(listIndInfoValuesSorted)
                odictCountIndividualsWithInfoField = OrderedDict(sorted(dictCountedIndInfoValues.items()))
#                 for key, value in odictCountedIndInfoValues.items(): 
#                     odictCountIndividualsWithInfoField[key] = value

                return odictCountIndividualsWithInfoField


            def method_Get_Index_Of_Individuals_By_InfoField(self, pop, strSimupopInfoField):
                '''
                Get all the indexes of individuals by InfoField in any passed pop
                ''' 
                #odictIndexsofIndividualsByInfoField = AutoVivificationHandler()
                odictIndexsofIndividualsByInfoField = OrderedDict()
                    
                #Get list of all indInfo values (each from a unique individual in the pop) = the one specified
                listIndInfoValuesSorted = sorted(pop.indInfo(strSimupopInfoField))
                
                strLastIndInfoValue = listIndInfoValuesSorted[0]
                
                #pop1 = pop.sortIndividuals(strSimupopInfoField)
                pop.sortIndividuals(strSimupopInfoField)
                for  individual in pop.individuals():
                    strCurrentIndInfoValue = individual.info(strSimupopInfoField)
                    if strCurrentIndInfoValue == strLastIndInfoValue:
                        if not strCurrentIndInfoValue in odictIndexsofIndividualsByInfoField:
                            
                            odictIndexsofIndividualsByInfoField[strCurrentIndInfoValue] = [individual.info('ind_id')] #Or could us individuals absolute index - pop.individual(idx).index = idx
                        else:
                            odictIndexsofIndividualsByInfoField[strCurrentIndInfoValue].append(individual.info('ind_id'))
                    else:
                        strLastIndInfoValue = strCurrentIndInfoValue
                        odictIndexsofIndividualsByInfoField[strCurrentIndInfoValue] = [individual.info('ind_id')] #Or could us individuals absolute index - pop.individual(idx).index = idx

                return odictIndexsofIndividualsByInfoField


            def method_Get_InfoField_For_Pop_By_InfoField(self, pop, tupVSP, strSimupopInfoFieldToFind, infoFieldValueToFind, strSimupopInfoFieldToReturn):
                '''
                Count the sexes in a pop
                '''
                odictInfoFieldofIndividualsByInfoField = OrderedDict()
                
                for individual in pop.individuals([tupVSP]):
                    #if individual.sex() == simupop.MALE:
                    if individual.info(strSimupopInfoFieldToFind) == infoFieldValueToFind:
                        infoReturned = individual.info(strSimupopInfoFieldToReturn)
                        if infoFieldValueToFind in odictInfoFieldofIndividualsByInfoField:
                            
                            odictInfoFieldofIndividualsByInfoField[infoFieldValueToFind].update(infoReturned)
                        else:
                            odictInfoFieldofIndividualsByInfoField[infoFieldValueToFind] = infoReturned

                return odictInfoFieldofIndividualsByInfoField

 
            def method_Extract_Imported_Allele_Info_To_List(self, odictAlleleFreqs_Orig, strInfoLabel):
                
                listAlleleInfo_All = []
                
                for keyLocus, valueDictLocusAlleleFreqs in odictAlleleFreqs_Orig.items():
                    
                    listAlleleInfo = []
                    
                    for keyAllele in valueDictLocusAlleleFreqs.keys():
                        
                        strAlleleName = valueDictLocusAlleleFreqs[keyAllele][strInfoLabel]
                    
                        listAlleleInfo.append(strAlleleName)
                    pass
                
                    listAlleleInfo_All.append(listAlleleInfo)
                    
                return listAlleleInfo_All

            '''
            --------------------------------------------------------------------------------------------------------
            # By Sex Processing
            --------------------------------------------------------------------------------------------------------
            '''

            def method_Get_InfoField_For_Pop_By_Sex(self, pop, tupVSP, strSex, simupopInfoFieldToReturn):
                '''
                Count the sexes in a pop
                '''
                
                objSexConstants = globalsSS.SexConstants()
                static_simupopSex = objSexConstants.method_Get_Simupop_Sex_Constant(strSex)
                
                listfInfoReturned = []
                odictInfoFieldofIndividualsBySex = OrderedDict([])
                
                simupopIndividuals = pop.individuals([tupVSP])
                
                for individual in simupopIndividuals:
                    if individual.sex() == static_simupopSex:

                        infoReturned = individual.info(simupopInfoFieldToReturn)
                        
                        listfInfoReturned.append(infoReturned)
#                         
#                         if strSex in odictInfoFieldofIndividualsBySex:
#                             #odictInfoFieldofIndividualsBySex[strSex].append(infoReturned)
#                             odictInfoFieldofIndividualsBySex[strSex] = infoReturned
#                         else:
                            
                
                odictInfoFieldofIndividualsBySex[strSex] = listfInfoReturned
                
                return odictInfoFieldofIndividualsBySex
   
            
            def method_Get_InfoField_For_Pop_By_Sex_by_VSP_Split(self, pop, tupVSP, strSex, simupopInfoFieldToReturn):
                '''
                Count the sexes in a pop
                '''
                
                
                objSexConstants = globalsSS.SexConstants()
                static_simupopSex = objSexConstants.method_Get_Simupop_Sex_Constant(strSex)
                
                listfInfoReturned = []
                odictInfoFieldofIndividualsBySex = OrderedDict([])
                
                simupopIndividuals = pop.individuals([tupVSP])
                
                for individual in simupopIndividuals:
                    if individual.sex() == static_simupopSex:

                        infoReturned = individual.info(simupopInfoFieldToReturn)
                        
                        listfInfoReturned.append(infoReturned)
#                         
#                         if strSex in odictInfoFieldofIndividualsBySex:
#                             #odictInfoFieldofIndividualsBySex[strSex].append(infoReturned)
#                             odictInfoFieldofIndividualsBySex[strSex] = infoReturned
#                         else:
                            
                
                odictInfoFieldofIndividualsBySex[strSex] = listfInfoReturned
                
                return odictInfoFieldofIndividualsBySex

            '''@profile'''
            def method_Get_InfoFields_For_Pop_By_Sex_OLD(self, pop, tupVSP, strSex, listSimupopInfoFieldsToReturn):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass 
                 
                '''
                Count the sexes in a pop
                '''
                
                objSexConstants = globalsSS.SexConstants()
                static_simupopSex = objSexConstants.method_Get_Simupop_Sex_Constant(strSex)
                
                odictInfoFieldsofIndividualsBySex = OrderedDict([])
                
                simupopIndividuals = pop.individuals([tupVSP])
                
                for individual in simupopIndividuals:
                    if individual.sex() == static_simupopSex:
                        
                        intIndividualID = individual.ind_id
                        odictNewValues = OrderedDict()
                        
                        for strInfoField in listSimupopInfoFieldsToReturn:
                        
                            infoReturned = individual.info(strInfoField)
                            dictNewValue = {strInfoField:infoReturned}
                            if intIndividualID in odictNewValues:
                                odictNewValues[intIndividualID].update(dictNewValue)
                            else:
                                odictNewValues[intIndividualID] = dictNewValue
                        pass
                        if intIndividualID in odictInfoFieldsofIndividualsBySex:
                            print('??? WARNING - Duplicate key updated' + str(odictNewValues) + ' - WARNING ???')
                            odictInfoFieldsofIndividualsBySex.update(odictNewValues)
                        else:
                            odictInfoFieldsofIndividualsBySex.update(odictNewValues)
                    pass
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
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
                                        
                
                return odictInfoFieldsofIndividualsBySex

            def method_Get_InfoFields_For_Pop_By_Sex_New(self, pop_In, tupVSP, strSex, listSimupopInfoFieldsToReturn, boolReportVSPIfEmpty, listExpectedKeyValues):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass    
                
                '''
                Count the sexes in a pop
                '''
                
                objSexConstants = globalsSS.SexConstants()
                static_simupop_Sex = objSexConstants.method_Get_Simupop_Sex_Constant(strSex)
                
                odictInfoFieldsofIndividualsBySex = OrderedDict()

                pop = self.method_VSP_Split_Pop_By_Sex(pop_In)

                #simupopIndividuals = pop.individuals([globalsSS.SP_SubPops.static_intSP_SubPop_Primary, strSex])
                #listIDs = list(simupopIndividuals)
                
                list1 = list(pop.indInfo(listSimupopInfoFieldsToReturn[0],  subPop=[globalsSS.SP_SubPops.static_intSP_SubPop_Primary, strSex]))
                list2 = list(pop.indInfo(listSimupopInfoFieldsToReturn[1],  subPop=[globalsSS.SP_SubPops.static_intSP_SubPop_Primary, strSex]))
                
                odictInfoFieldsofIndividualsBySex_Start = OrderedDict(zip(list1,list2))
                
                for float_IndivID, float_IndivAgeInMonths in odictInfoFieldsofIndividualsBySex_Start.items():
                
                    if float_IndivAgeInMonths in odictInfoFieldsofIndividualsBySex:
                        odictInfoFieldsofIndividualsBySex[float_IndivAgeInMonths].append(float_IndivID)
                    else:
                        odictInfoFieldsofIndividualsBySex[float_IndivAgeInMonths] = [float_IndivID]
                    pass
                pass
            
                if boolReportVSPIfEmpty and len(listExpectedKeyValues) > 0:

                    #list_tup_VSP_Sizes_New = [x for x in list_tup_VSP_Sizes]
                    for intExpectedVSP in listExpectedKeyValues:
                        float_ExpectedVSP = float(intExpectedVSP)
                        if float_ExpectedVSP not in odictInfoFieldsofIndividualsBySex.keys():
                            odictInfoFieldsofIndividualsBySex[float_ExpectedVSP] = []
                        pass
                    pass
                pass
            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #pdb.set_trace()
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                                        
                return odictInfoFieldsofIndividualsBySex

            def method_Get_InfoFields_For_Pop_By_Sex_New_OLD(self, pop_In, tupVSP, strSex, listSimupopInfoFieldsToReturn):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass    
                
                '''
                Count the sexes in a pop
                '''
                
                objSexConstants = globalsSS.SexConstants()
                static_simupop_Sex = objSexConstants.method_Get_Simupop_Sex_Constant(strSex)
                
                odictInfoFieldsofIndividualsBySex = OrderedDict()

                pop = self.method_VSP_Split_Pop_By_Sex(pop_In)

                #simupopIndividuals = pop.individuals([globalsSS.SP_SubPops.static_intSP_SubPop_Primary, strSex])
                #listIDs = list(simupopIndividuals)
                
                list1 = list(pop.indInfo(listSimupopInfoFieldsToReturn[0],  subPop=[globalsSS.SP_SubPops.static_intSP_SubPop_Primary, strSex]))
                list2 = list(pop.indInfo(listSimupopInfoFieldsToReturn[1],  subPop=[globalsSS.SP_SubPops.static_intSP_SubPop_Primary, strSex]))
                
                odictInfoFieldsofIndividualsBySex_Start = OrderedDict(zip(list1,list2))
                
                for float_IndivID, float_IndivAgeInMonths in odictInfoFieldsofIndividualsBySex_Start.items():
                
                    if float_IndivAgeInMonths in odictInfoFieldsofIndividualsBySex:
                        odictInfoFieldsofIndividualsBySex[float_IndivAgeInMonths].append(float_IndivID)
                    else:
                        odictInfoFieldsofIndividualsBySex[float_IndivAgeInMonths] = [float_IndivID]
                    pass
                pass
            
            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #pdb.set_trace()
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                                        
                return odictInfoFieldsofIndividualsBySex

            def method_Get_InfoFields_For_Pop_By_Sex(self, pop_In, tupVSP, strSex, listSimupopInfoFieldsToReturn):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass    
                
                '''
                Count the sexes in a pop
                '''
                
                objSexConstants = globalsSS.SexConstants()
                static_simupop_Sex = objSexConstants.method_Get_Simupop_Sex_Constant(strSex)
                
                odictInfoFieldsofIndividualsBySex = OrderedDict([])

                pop = self.method_VSP_Split_Pop_By_Sex(pop_In)

                #simupopIndividuals = pop.individuals([globalsSS.SP_SubPops.static_intSP_SubPop_Primary, strSex])
                #listIDs = list(simupopIndividuals)
                
                list1 = list(pop.indInfo(listSimupopInfoFieldsToReturn[0],  subPop=[globalsSS.SP_SubPops.static_intSP_SubPop_Primary, strSex]))
                list2 = list(pop.indInfo(listSimupopInfoFieldsToReturn[1],  subPop=[globalsSS.SP_SubPops.static_intSP_SubPop_Primary, strSex]))
                
                odictInfoFieldsofIndividualsBySex = OrderedDict(zip(list1,list2))
                
                
                #simupopIndividuals = pop.individuals([tupVSP])
                
#                 for individual in simupopIndividuals:
#                     if individual.sex() == static_simupopSex:
#                         
#                         intIndividualID = individual.ind_id
#                         odictNewValues = OrderedDict()
#                         
#                         for strInfoField in listSimupopInfoFieldsToReturn:
#                         
#                             infoReturned = individual.info(strInfoField)
#                             dictNewValue = {strInfoField:infoReturned}
#                             if intIndividualID in odictNewValues:
#                                  odictNewValues[intIndividualID].update(dictNewValue)
#                             else:
#                                 odictNewValues[intIndividualID] = dictNewValue
#                         pass
#                         if intIndividualID in odictInfoFieldsofIndividualsBySex:
#                             print('??? WARNING - Duplicate key updated' + str(odictNewValues) + ' - WARNING ???')
#                             odictInfoFieldsofIndividualsBySex.update(odictNewValues)
#                         else:
#                             odictInfoFieldsofIndividualsBySex.update(odictNewValues)
#                     pass
#                 pass
            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #pdb.set_trace()
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                                        
                return odictInfoFieldsofIndividualsBySex


            def method_List_Sexes_For_VirtualSubPop(self, pop, intSubPop, intVirtualSubPop, stringSortInfoField, boolSorted):
                '''
                List sex values for any pop
                '''     

                if boolSorted:
                    pop.sortIndividuals(stringSortInfoField)
                    
                iterIndividuals = pop.individuals([intSubPop,intVirtualSubPop])

                listSexes=[]

                for intIndividual in iterIndividuals:
                    if intIndividual.sex() == 1:
                            stringSex = 'M'
                    elif intIndividual.sex() == 2:
                        stringSex = 'F'
                    else:
                        stringSex = 'U'
                    
                    listSexes.append(stringSex)

                return listSexes


            def methodCount_SexesInAPop(self, pop_In, intSubPop, intVirtualSubPop=-1):
                '''
                Count the sexes in a pop
                '''
                intMale=0
                intFemale=0
                
                try:
                    intVirtualSubPop = int(intVirtualSubPop)
                    if intVirtualSubPop == -1:
                        simupop_Indivs = pop_In.individuals(intSubPop)
                    else:
                        simupop_Indivs = pop_In.individuals([intSubPop, intVirtualSubPop])
                    pass
                except:
                    self.obj_Log_Default_Display.error('intVirtualSubPop is not an integer: ' + str(intVirtualSubPop))
                    sys.stderr.flush()
                    raise
                pass
            
                for individual in simupop_Indivs:
                    if individual.sex() == simupop.MALE:
                        intMale+=1
                    else:
                        if individual.sex() == simupop.FEMALE:
                            intFemale+=1

                listCountofMaleFemale = [intMale, intFemale]

                return listCountofMaleFemale


            '''
            --------------------------------------------------------------------------------------------------------
            # Utility Processing
            --------------------------------------------------------------------------------------------------------
            '''
           
            def method_Flatten_Nested_Dict_Into_Multiline_Dict__LDNe_Results(self, bool_Top_Level, int_Line_Initial, int_Line, int_Level, int_Lowest_Level, int_Lowest_Level_Dict_Num_Keys, dict_To_Flatten, dict_Final):
                '''
                Flatten an OrderedDict object
                '''
                int_Level += 1

                dict_Discard = OrderedDict()
                for k, v in dict_To_Flatten.items():
                    if isinstance(v, dict):

                        dict_Discard = self.method_Flatten_Nested_Dict_Into_Multiline_Dict__LDNe_Results(False, int_Line_Initial, int_Line, int_Level, int_Lowest_Level, int_Lowest_Level_Dict_Num_Keys, v, dict_Final)

                        if int_Level == int_Lowest_Level:
                            int_Line += 1
                        pass
                    else:
                        if int_Level == int_Lowest_Level+1:
                            if int_Line in dict_Final:
                                    
                                dict_Final[int_Line].update(OrderedDict([(k, v)]))
                                    
                            else:
                                dict_Final[int_Line] = OrderedDict([(k, v)])
                            pass
                        else:
                            for int_Line_Count in range(int_Line_Initial, int_Line_Initial+int_Lowest_Level_Dict_Num_Keys):
                                if int_Line_Count in dict_Final:
                                    
                                    dict_Final[int_Line_Count].update(OrderedDict([(k, v)]))
                                    
                                else:
                                    dict_Final[int_Line_Count] = OrderedDict([(k, v)])
                                pass
                            pass
                        pass
                    pass
                
                    if bool_Top_Level:
                        int_Line_Initial = len(dict_Final)
                        int_Line = int_Line_Initial
                    pass
                pass
                
                    
                return dict_Final

            def method_Get_Nested_Dict__Non_Dict_Key_Count_Per_Nested_Level(self, dict_To_Analyse, int_Level, dict_Non_Dict_Key_Count_Per_Level):
                
                int_Level += 1
                int_Non_Dict_Key_Count_This_Level = 0
                
                ''' Get the number of keys for the lowest level dict '''
                for v in dict_To_Analyse.values(): 
                    if isinstance(v, dict):
                        dict_Non_Dict_Key_Count_Per_Level = self.method_Get_Nested_Dict__Non_Dict_Key_Count_Per_Nested_Level(v, int_Level, dict_Non_Dict_Key_Count_Per_Level)
                    else:
                        int_Non_Dict_Key_Count_This_Level += 1
                    pass
                    dict_Non_Dict_Key_Count_Per_Level[int_Level] = int_Non_Dict_Key_Count_This_Level
                pass
            
                return dict_Non_Dict_Key_Count_Per_Level

            def method_Flatten_Nested_Dict_Into_Multiline_Dict__BioP_Allele_Freqs(self, bool_Top_Level, int_Line_Initial, int_Line, int_Level, int_Lowest_Level, int_Lowest_Level_Dict_Num_Keys, dict_To_Flatten, dict_Final):
                '''
                Flatten an OrderedDict object
                '''
                int_Level += 1
                
                if int_Level == 2:
                    dict_Non_Dict_Key_Count_Per_Level = OrderedDict()
                    dict_Non_Dict_Key_Count_Per_Level = self.method_Get_Nested_Dict__Non_Dict_Key_Count_Per_Nested_Level(dict_To_Flatten, 0, dict_Non_Dict_Key_Count_Per_Level)
                    int_Lowest_Level_Dict_Num_Keys = max(value for value in dict_Non_Dict_Key_Count_Per_Level.values())
#                 else:
#                     int_Lowest_Level_Dict_Num_Keys = 0
                pass
                
                dict_Discard = OrderedDict()
                for k, v in dict_To_Flatten.items():
                    if isinstance(v, dict):

                        dict_Discard = self.method_Flatten_Nested_Dict_Into_Multiline_Dict__BioP_Allele_Freqs(False, int_Line_Initial, int_Line, int_Level, int_Lowest_Level, int_Lowest_Level_Dict_Num_Keys, v, dict_Final)

                        if int_Level == int_Lowest_Level:
                            int_Line += 1
                        pass
                    else:
                        if int_Level == int_Lowest_Level+1:
                            if int_Line in dict_Final:
                                    
#                                 dict_Final[int_Line].update(OrderedDict([(k, v)]))
                                dict_Final[int_Line][globalsSS.Colnames_Genepop_Allele_Freqs_By_Allele_Results.static_str_Colname_Allele_Name] = k
                                dict_Final[int_Line][globalsSS.Colnames_Genepop_Allele_Freqs_By_Allele_Results.static_str_Colname_Allele_Freq] = v
                                int_Line += 1    
                            else:
                                dict_Final[int_Line] = OrderedDict([(k, v)])
                            pass
                        else:
                            for int_Line_Count in range(int_Line_Initial, int_Line_Initial+int_Lowest_Level_Dict_Num_Keys):
                                if int_Line_Count in dict_Final:
                                    
                                    dict_Final[int_Line_Count].update(OrderedDict([(k, v)]))
                                    
                                else:
                                    dict_Final[int_Line_Count] = OrderedDict([(k, v)])
                                pass
                            pass
                        pass
                    pass
                
                    if bool_Top_Level:
                        int_Line_Initial = len(dict_Final)
                        int_Line = int_Line_Initial
                    pass
                pass
                
                    
                return dict_Final

            def method_Flatten_Nested_Dict_Into_Multiline_Dict_OLD(self, bool_Top_Level, int_Line_Initial, int_Line, int_Level, int_Lowest_Level, int_Lowest_Level_Dict_Num_Keys, dict_To_Flatten, dict_Final):
                '''
                Flatten an OrderedDict object
                '''
                int_Level += 1
                 
                dict_Discard = OrderedDict()
                for k, v in dict_To_Flatten.items():
                    if isinstance(v, dict):

                        dict_Discard = self.method_Flatten_Nested_Dict_Into_Multiline_Dict(False, int_Line_Initial, int_Line, int_Level, int_Lowest_Level, int_Lowest_Level_Dict_Num_Keys, v, dict_Final)

                        if int_Level == int_Lowest_Level:
                            int_Line += 1
                        pass
                    else:
                        if int_Level == int_Lowest_Level+1:
                            if int_Line in dict_Final:
                                    
                                dict_Final[int_Line].update({k: v})
                                    
                            else:
                                dict_Final[int_Line] = {k: v}
                            pass
                        else:
                            for int_Line_Count in range(int_Line_Initial, int_Line_Initial+int_Lowest_Level_Dict_Num_Keys):
                                if int_Line_Count in dict_Final:
                                    
                                    dict_Final[int_Line_Count].update({k: v})
                                    
                                else:
                                    dict_Final[int_Line_Count] = {k: v}
                                pass
                            pass
                        pass
                    pass
                
                    if bool_Top_Level:
                        int_Line_Initial = len(dict_Final)
                        int_Line = int_Line_Initial
                    pass
                pass
                
                    
                return dict_Final


            def method_Count_OrderedDict_Values_By_Key(self, odictSource, keyToCountValues):
                '''
                ''' 
                listValues = []
                
                for odictValues in odictSource.values():
                    
                    listValues.append(odictValues[keyToCountValues])
                pass
            
                listValuesSorted = sorted(listValues) 
                    
                dictCountedValues = collections__Counter(listValuesSorted)
                
                odictCountValuesByKey = OrderedDict(sorted(dictCountedValues.items()))

                return odictCountValuesByKey


            def method_Count_OrderedDict_Values_By_Key_NEW(self, odictSource, keyToCountValues):
                    
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass
                      
                listValues = []
                
                for values in odictSource.values():
                    
                    listValues.append(values)
                pass
            
                listValuesSorted = sorted(listValues) 
                    
                dictCountedValues = collections__Counter(listValuesSorted)
                
                odictCountValuesByKey = OrderedDict(sorted(dictCountedValues.items()))

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    #simupop.dump(pop)
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
            
                return odictCountValuesByKey
  
            
            def method_Get_OrderedDict_Values_List_By_Key(self, odictSource, keyOfValues):
                '''
                ''' 
                listValues = []
                
                for odictValues in odictSource.values():
                    
                    listValues.append(odictValues[keyOfValues])
                pass

                return listValues


            def method_Get_OrderedDict_Values_List_By_Key_And_Value(self, odictSource, keyOfValues, valueToMatch, keyOfValueToReturn):
                '''
                ''' 
                listValues = []
                
                for odictValues in odictSource.values():
                    
                    value = odictValues[keyOfValues]
                    
                    if value == valueToMatch:
                        listValues.append(odictValues[keyOfValueToReturn])
                pass

                return listValues
   
            
            def method_Get_OrderedDict_Values_List_By_Key_And_Value_NEW(self, odictSource, keyOfValues, valueToMatch, keyOfValueToReturn):
                    
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
                    
#                     
#                 listValues = []
#                 
#                 for key, value in odictSource.items():
#                     
#                     #value = odictValues[keyOfValues]
#                     
#                     if value == valueToMatch:
#                         listValues.append(key)
#                 pass
                    
                listValues = [item[0] for item in odictSource.items() if item[1] == valueToMatch]

                #pdb.set_trace()
                
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    #str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    obj_Debug_Loc = Debug_Location()
                    str_Message_Location = obj_Debug_Loc.Get_Debug_Location()
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #pdb.set_trace()
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
            
                return listValues


            def method_Validate_Rate_Distribution(self, dictRateDist): 
                
                boolSuccess = False
                
                #Check that rate distibution totals 1
                floatTotalRate = 0
                for keyRate, valueRate in dictRateDist.items():
                    floatTotalRate += valueRate
                pass
                
                #Apply a rounding as this will often not be precise
                floatTotalRate = round(floatTotalRate,2)
                
                if floatTotalRate != 1:
                    #LOGGING
                    #print('!!! ERROR - method_Apply_Rate_Distribution_To_Number_Distribution - Rate total not equal to 1: ' + str(floatTotalRate) + ' ERROR!!!')
                    self.obj_Log_Default_Display.error('!!! ERROR - method_Apply_Rate_Distribution_To_Number_Distribution - Rate total not equal to 1: ' + str(floatTotalRate) + ' ERROR!!!')
                    #LOGGING
                    boolSuccess = False
                else:
                    boolSuccess = True
                pass        
                
                return boolSuccess


            def method_Apply_Absolute_Rate_To_Number_Distribution(self, floatRate, dictNumberDist, boolRoundResult, intRoundToDecimalPlaces):    
                
                dictResultingNumberDistribution = OrderedDict()
                
                #Get the total of the number dist
                intTotalNumber = 0
                for valueNumber in dictNumberDist.values():
                    intTotalNumber += valueNumber
                
                floatRate = Decimal(floatRate)
                #intTotalSamplesToTake = int(round(intTotalNumber * floatRate,0))
                intTotalSamplesToTake = int(round(intTotalNumber * floatRate))
                
                #Generate dict with the absolute rate applied to the supplied numbers
                for keyNumber, valueNumber in dictNumberDist.items():
                    
                    floatCohortProportionOfTotalPop = valueNumber / intTotalNumber
                    floatResult = intTotalSamplesToTake * floatCohortProportionOfTotalPop
                    if boolRoundResult:
                        floatResult = round(floatResult, intRoundToDecimalPlaces)
                    pass
                    dictResultingNumberDistribution[keyNumber] = floatResult
                pass   
                
                return dictResultingNumberDistribution   
    
                          
            def method_Apply_Rate_Distribution_To_Number_Distribution(self, dictRateDist, dictNumberDist, boolRoundResult, intRoundToDecimalPlaces):
                
                #Check that rate distibution totals 1
                boolSuccess = self.method_Validate_Rate_Distribution(dictRateDist)
                
                dictResultingNumberDistribution = OrderedDict()
                if boolSuccess:
                    #Generate dict with the resulting rates applied to the supplied numbers
                    for keyNumber, valueNumber in dictNumberDist.items():
                        
                        floatRate = dictRateDist[keyNumber]
                        floatRate = Decimal(floatRate)
                        floatResult = valueNumber * floatRate
                        if boolRoundResult:
                            floatResult = round(floatResult, intRoundToDecimalPlaces)
                        pass
                        dictResultingNumberDistribution[keyNumber] = floatResult
                    pass   
                
                return dictResultingNumberDistribution
    
                                              
            def method_Apply_Proportion_Distribution_To_Number_Distribution(self, dictProportionDist, dictNumberDist, boolRoundResult, intRoundToDecimalPlaces):
                
                #Check that rate distibution totals 1
                #boolSuccess = self.method_Validate_Rate_Distribution(dictRateDist)
                
                boolSuccess = True
                dictResultingNumberDistribution = OrderedDict()
                if boolSuccess:
                    #Generate dict with the resulting rates applied to the supplied numbers
                    for keyNumber, valueNumber in dictNumberDist.items():
                        
                        floatProportion = dictProportionDist[keyNumber]
                        floatResult = valueNumber * floatProportion
                        if boolRoundResult:
                            floatResult = round(floatResult, intRoundToDecimalPlaces)
                        pass
                        dictResultingNumberDistribution[keyNumber] = floatResult
                    pass   
                
                return dictResultingNumberDistribution
    
                                              
            def method_rpy2_test(self):   
                
                #pi = robjects.r['pi']
                #print('rpy2 test')
                #print(pi[0])
                pass


            def method_Accumulate_Generic_Stat(self, list_Stats_Categories, str_Stat_Name, value_Stat, dict_Results):


                for str_Stats_Category in list_Stats_Categories:
                    
                    dict_Results[str_Stats_Category].update({str_Stat_Name : value_Stat})                    
                pass
                
                return dict_Results 


            def method_Get_Ratio_Stat(self, float_Numerator, float_Denominatior):
                
                float_Ratio = float(float_Numerator) / float(float_Denominatior)
                
                return float_Ratio
                
                
            '''
            --------------------------------------------------------------------------------------------------------
            # VSP Processing
            --------------------------------------------------------------------------------------------------------
            '''

            def method_Get_VSP_Sizes_RETIRE(self, pop_In, boolReportVSPIfEmpty):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass 
                
   



#                         simupop.Stat(popSize=True, subPops=[(0,0), (0,1), (0,2), (0,3), (0,4),(0,5), (0,6), (0,7), (0,8)]),
#                         # print virtual subpopulation sizes (there is no individual with age > maxAge after mating)
#                         simupop.PyEval(r"'Size of age groups: %s\n' % (','.join(['%d' % x for x in subPopSize]))"),
                                            
                intNumVSPS = pop_In.numVirtualSubPop()
                odictVSPSizes = OrderedDict()
                for intVSP in range(0, intNumVSPS):
                    intVSPSize = int(pop_In.subPopSize([globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVSP]))
                    #Convert to float to ensure accurate AgeNe calculations
                    floatVSPSize = float(intVSPSize)
                    #Check if any individuals in VSP
                    if intVSPSize == 0:
                        #Report if required otherwise dont
                         
                        if boolReportVSPIfEmpty:
                            if intVSP in odictVSPSizes:
                                odictVSPSizes[intVSP].update(floatVSPSize)
                            else:
                                odictVSPSizes[intVSP] = float(floatVSPSize)
                    else:
                        #Always report if VSP has individuals
                        if intVSP in odictVSPSizes:
                            odictVSPSizes[intVSP].update(floatVSPSize)
                        else:
                            odictVSPSizes[intVSP] = floatVSPSize

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    #str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    obj_Debug_Loc = Debug_Location()
                    str_Message_Location = obj_Debug_Loc.Get_Debug_Location()
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #pdb.set_trace()
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
            
                pdb.set_trace()
                                
                return odictVSPSizes
            
            
            def method_Get_VSP_Sizes_By_InfoField(self, pop_In, boolReportVSPIfEmpty, listExpectedKeyValues, str_InfoField, str_VSP_Name=''):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass 
            
                if str_VSP_Name <> '':
                    listIndivsPerInfoField = list(pop_In.indInfo(str_InfoField,  subPop=[globalsSS.SP_SubPops.static_intSP_SubPop_Primary, str_VSP_Name]))
                else:  
                    listIndivsPerInfoField = list(pop_In.indInfo(str_InfoField,  subPop=[globalsSS.SP_SubPops.static_intSP_SubPop_Primary]))
                pass

                counterIndivsPerInfoField = collections__Counter(listIndivsPerInfoField)
                #list_tup_VSP_Sizes = sorted(counterIndivsPerInfoField.items(), key=itemgetter(0))
                list_tup_VSP_Sizes = [(key, value) for key, value in counterIndivsPerInfoField.iteritems()]
                    
                if boolReportVSPIfEmpty and len(listExpectedKeyValues) > 0:

                    
                    list_tup_VSP_Sizes_New = [x for x in list_tup_VSP_Sizes]
                    for intExpectedVSP in listExpectedKeyValues:
                        if len([item for item in list_tup_VSP_Sizes if item[0] == intExpectedVSP]) == 0:
                            list_tup_VSP_Sizes_New.append((intExpectedVSP, 0))
                        pass
                    pass
                    list_tup_VSP_Sizes_New = sorted(list_tup_VSP_Sizes_New, key=lambda tup: tup[0])
                    odictVSPSizes = OrderedDict(list_tup_VSP_Sizes_New)
                else:
                    odictVSPSizes = OrderedDict(list_tup_VSP_Sizes_New)
                pass
            
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    #str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    obj_Debug_Loc = Debug_Location()
                    str_Message_Location = obj_Debug_Loc.Get_Debug_Location()
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #pdb.set_trace()
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
            
                return odictVSPSizes
  
            def method_Get_VSP_Sizes(self, pop_In, boolReportVSPIfEmpty):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass 
                intNumVSPS = pop_In.numVirtualSubPop()
                list_VSPS = [x for x in range (0, intNumVSPS)]
                list_tup_VSPS = [(0,x) for x in range (0, intNumVSPS)]

                '''
                ***********************************************
                NOTE: This simupop.Stat function for popSize 
                is very expensive for lots of VSPs. Use sparingly.
                ***********************************************
                '''
                simupop.stat(pop_In, popSize=True, subPops=list_tup_VSPS , vars=['subPopSize'])
                list_VSP_Sizes = pop_In.dvars().subPopSize
                
                list_VSP_Sizes = [float(i) for i in list_VSP_Sizes]
                list_tup_VSP_Sizes = zip(list_VSPS, list_VSP_Sizes)
                 
                if boolReportVSPIfEmpty:
                    odictVSPSizes = OrderedDict(list_tup_VSP_Sizes)
                else:
                    filter_list = [0]
                    list_tup_VSP_Sizes_With_Indivs = [tup for tup in list_tup_VSP_Sizes if any(i not in [tup[1]] for i in filter_list)]
                    odictVSPSizes = OrderedDict(list_tup_VSP_Sizes_With_Indivs)
                pass
                                   

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    #str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    obj_Debug_Loc = Debug_Location()
                    str_Message_Location = obj_Debug_Loc.Get_Debug_Location()
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #pdb.set_trace()
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
            
                return odictVSPSizes
  
            def method_Get_VSP_Sizes_OLD(self, pop_In, boolReportVSPIfEmpty):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass 
                    
                    
                intNumVSPS = pop_In.numVirtualSubPop()
                odictVSPSizes = OrderedDict()
                for intVSP in range(0, intNumVSPS):
                    intVSPSize = int(pop_In.subPopSize([globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVSP]))
                    #Convert to float to ensure accurate AgeNe calculations
                    floatVSPSize = float(intVSPSize)
                    #Check if any individuals in VSP
                    if intVSPSize == 0:
                        #Report if required otherwise dont
                        
                        if boolReportVSPIfEmpty:
                            if intVSP in odictVSPSizes:
                                odictVSPSizes[intVSP].update(floatVSPSize)
                            else:
                                odictVSPSizes[intVSP] = float(floatVSPSize)
                    else:
                        #Always report if VSP has individuals
                        if intVSP in odictVSPSizes:
                            odictVSPSizes[intVSP].update(floatVSPSize)
                        else:
                            odictVSPSizes[intVSP] = floatVSPSize

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    #str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    obj_Debug_Loc = Debug_Location()
                    str_Message_Location = obj_Debug_Loc.Get_Debug_Location()
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
                                    
                return odictVSPSizes
  
            
            def method_Get_SP_Sizes(self, pop, boolReportSPIfEmpty):

                intNumSPS = pop.numSubPop()
                odictSPSizes = OrderedDict()
                for intSP in range(0, intNumSPS):
                    intSPSize = int(pop.subPopSize([globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intSP]))
                    #Convert to float to ensure accurate AgeNe calculations
                    floatSPSize = float(intSPSize)
                    #Check if any individuals in SP
                    if intSPSize == 0:
                        #Report if required otherwise dont
                        
                        if boolReportSPIfEmpty:
                            if intSP in odictSPSizes:
                                odictSPSizes[intSP].update(floatSPSize)
                            else:
                                odictSPSizes[intSP] = float(floatSPSize)
                    else:
                        #Always report if SP has individuals
                        if intSP in odictSPSizes:
                            odictSPSizes[intSP].update(floatSPSize)
                        else:
                            odictSPSizes[intSP] = floatSPSize
                        
                return odictSPSizes
  
            
            def method_Get_VSP_List(self, pop, boolReportVSPIfEmpty=False):
                
                listVSPs = []
                intNumVSPS = pop.numVirtualSubPop()
                for intVSP in range(0, intNumVSPS):
                    tupVSP = (globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVSP)
                    if boolReportVSPIfEmpty:
                        listVSPs.append(tupVSP)
                    #elif self.pop.subPopSize(subPop=[intSubPop, intSubpopIndex]) > 0:
                    elif pop.subPopSize(subPop=[globalsSS.SP_SubPops.static_intSP_SubPop_Primary, intVSP]) > 0:
                        listVSPs.append(tupVSP)
                        
                return listVSPs


            def method_Convert_AgeInMonths_To_AgeInYears(self, dictToConvert):
                
                if isinstance(dictToConvert, dict):
                    dictConverted = AutoVivificationHandler()
                    for intAge, value in dictToConvert.iteritems():
                        intAge = (intAge / 12)
                        #if intAge in dictConverted:
                        #    dictConverted[intAge]..append(value)
                        #else:
                        #    dictConverted[intAge] = value
                        dictConverted[intAge] = value
                    pass
                elif isinstance(dictToConvert, OrderedDict()):
                    dictConverted = OrderedDict()
                    for intAge, value in dictToConvert.items():
                        intAge = intAge / 12
                        if intAge in dictConverted:
                            dictConverted[intAge].update(value)
                        else:
                            dictConverted[intAge] = value
                    pass
                
                return dictConverted


            def method_Convert_Allele_Freqs_To_List(self, odictAlleleFreqs_Orig, odictAlleleFreqs_New):
                '''
                #Convert odict of allele freqs into list ensuring that the results reflect
                the original allele frequencies
                '''
                listAlleleFreqs = []
                dictAlleleFreqs = {}
                listAlleleFreqs_All = []
                
                for keyLocus, valueDictLocusAlleleFreqs in odictAlleleFreqs_Orig.items():
                    
                    dictAlleleFreqs = odictAlleleFreqs_New[keyLocus]
                    
                    listAlleleFreqs = []
                    for keyAllele in valueDictLocusAlleleFreqs.keys():
                        if keyAllele in dictAlleleFreqs:
                            floatAlleleFreq = dictAlleleFreqs[keyAllele]
                        else:
                            floatAlleleFreq = 0
                    
                        listAlleleFreqs.append(floatAlleleFreq)
                    pass
                
                    listAlleleFreqs_All.append(listAlleleFreqs)
                
                return listAlleleFreqs_All

            '''
            --------------------------------------------------------------------------------------------------------
            # Ne Stats Processing
            --------------------------------------------------------------------------------------------------------
            '''

            def method_Calculate_Nb_Adj1_From_Nb_Ne_Ratio(self, floatLD_Nb_Raw_From_Single_Cohort, floatNb_Ne_Ratio):
                
                floatNb_Adj1_From_True_Nb_Ne_Ratio = float(floatLD_Nb_Raw_From_Single_Cohort) / float(1.26 - float(0.323 * float(floatNb_Ne_Ratio)))
                   
                return floatNb_Adj1_From_True_Nb_Ne_Ratio
   
            
            def method_Calculate_Nb_Adj2_From_Two_Traits(self, floatLD_Nb_Raw_From_Single_Cohort, floatMaxAge, floatMinReproductiveAge):
                
                floatNb_Adj2_From_Two_Traits = float(floatLD_Nb_Raw_From_Single_Cohort) / float(1.103 - float(0.245 * float(log(float(floatMaxAge/floatMinReproductiveAge)))))
                   
                return floatNb_Adj2_From_Two_Traits
   
            
            def method_Calculate_Ne_Adj1_From_Nb_Ne_Ratio(self, floatNb_Adj1_From_True_Nb_Ne_Ratio, floatNb_Ne_Ratio):
                
                floatNe_Adj1_From_True_Nb_Ne_Ratio = float(floatNb_Adj1_From_True_Nb_Ne_Ratio) / float(floatNb_Ne_Ratio)
                   
                return floatNe_Adj1_From_True_Nb_Ne_Ratio
   
            
            def method_Calculate_Ne_Adj2_From_Two_Traits(self, floatNb_Adj2_From_Two_Traits, floatMaxAge, floatMinReproductiveAge):
                
                floatNe_Adj2_From_Two_Traits = float(floatNb_Adj2_From_Two_Traits) / float(0.485 - float(0.758 * float(log(float(floatMaxAge/floatMinReproductiveAge)))))
                   
                return floatNe_Adj2_From_Two_Traits
   
            '''
            ^^^^^^^^^^^^^^^^^^^^^^^^
            AgeNe Calc
            ^^^^^^^^^^^^^^^^^^^^^^^^
            '''             
            def method_AgeNeCalculation(self, objSSParameters):
                
                odictAgeValues = OrderedDict()
                
                boolUseAgeNeSimParameters = objSSParameters.boolUseAgeNeSimParameters
                
                if boolUseAgeNeSimParameters:
                    listSexes = objSSParameters.listAgeNe_Sim_ListSexes
                    intMaxAgeInYears = objSSParameters.intAgeNe_Sim_Max_Age
                    intMinMatingAgeInYears = objSSParameters.intAgeNe_Sim_Min_Mating_Age
                    intMaxMatingAgeInYears = objSSParameters.intAgeNe_Sim_Max_Mating_Age
                    #intAgeNe_N1_Newborns_Per_Age = objSSParameters.intAgeNe_Sim_N1_Newborns_Per_Age
                    intAgeNe_N1_Newborns_Per_Age = objSSParameters.intAgeNe_Sim_N1_Newborns
                    #intAgeNe_N1_Newborns_Per_Age = objSSParameters.intAgeNe_Manual_N1_Newborns_PREDICTED
                    #floatAgeNe_Initial_Male_Sex_Ratio  = objSSParameters.floatAgeNe_Sim_Initial_Male_Sex_Ratio
                    floatAgeNe_N1_Male_Sex_Ratio  = objSSParameters.floatAgeNe_Sim_N1_Male_Sex_Ratio
                    odictAgeNe_Age_Values_Survival_Rates = objSSParameters.odictAgeNe_Sim_Age_Values_Survival_Rates
                    #dictAgeNe_Age_Values_Birth_Rates = objSSParameters.odictAgeNe_Sim_Age_Values_Birth_Rates
                    odictAgeNe_Alpha_Value_Scaling_Poisson_Variance_In_Reproductive_Success = objSSParameters.odictAgeNe_Sim_Alpha_Value_Scaling_Poisson_Variance_In_Reproductive_Success
                    
                    #odictAgeNe_Sim_AgeClass_Sizes_Per_Sex starts at year 0 to (maxAge-1) with 0 holding the predicted SIM N1
                    #Need to convert it to ages from 1 to maxAge
                    
                    #odictAgeNe_Nx_Odict_Newborns_Per_Age_x = objSSParameters.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year
                    odictAgeNe_Nx_Odict_Newborns_Per_Age_x = OrderedDict()
#                     for strSex, dictYearValues in objSSParameters.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year.items(): 
#                         for intYear, value in dictYearValues.iteritems():
#                             #intAge = intYear+1
#                             intAge = intYear+2
#                             dictNewValues = {intAge: value}
#                             if strSex in odictAgeNe_Nx_Odict_Newborns_Per_Age_x:
#                                 odictAgeNe_Nx_Odict_Newborns_Per_Age_x[strSex].update(dictNewValues)
#                             else:
#                                 odictAgeNe_Nx_Odict_Newborns_Per_Age_x[strSex] = dictNewValues
#                         pass
#                         #floatN1NewbornsbySex = objSSParameters.intAgeNe_Sim_N1_Newborns // 2
#                         #floatN1NewbornsbySex = objSSParameters.dict_AgeNe_Manual_N1_Newborns_By_Sex_PREDICTED[strSex]
#                         floatN1NewbornsbySex = objSSParameters.odictAgeNe_Sim_N1_Newborns_Per_Sex_Per_Year[strSex][1]
#                         dictNewValues = {1: floatN1NewbornsbySex}
#                         #dictNewValues = {objSSParameters.maxAge+1: 0}
#                         odictAgeNe_Nx_Odict_Newborns_Per_Age_x[strSex].update(dictNewValues)
#                     pass
                    for strSex, dictYearValues in objSSParameters.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year.items(): 
                        for intYear, value in dictYearValues.iteritems():
                            intAge = intYear+1
                            dictNewValues = {intAge: value}
                            if strSex in odictAgeNe_Nx_Odict_Newborns_Per_Age_x:
                                odictAgeNe_Nx_Odict_Newborns_Per_Age_x[strSex].update(dictNewValues)
                            else:
                                odictAgeNe_Nx_Odict_Newborns_Per_Age_x[strSex] = dictNewValues
                        pass

                    pass
                    
                    odictAgeNe_Age_Values_Birth_Rates = objSSParameters.odictAgeNe_Sim_b_x_Odict_Scaled_Birth_Rate_Per_Age_x #TEMP_FIX
                    for strSex in listSexes:
                        #Providing a (maxAge + 1) value to the SIM AgeNe calcs is required as the sim starts at 0 and so Age 0-1 represents Age 1 in AgeNe and maxAge to maxAge+1 is maxAge 
                        odictAgeNe_Age_Values_Birth_Rates[strSex].update({(objSSParameters.maxAge)+1:0})
                        
                    #odictAgeNe_Age_Values_Birth_Rates
                    #odictAgeNe_b_x_Odict_Scaled_Birth_Rate_Per_Age_x = objSSParameters.odictAgeNe_Sim_b_x_Odict_Scaled_Birth_Rate_Per_Age_x
                    #odictAgeNe_N1_Newborns_Per_Sex_Per_Year = objSSParameters.odictAgeNe_Sim_Nx_Newborns_After_Mortality_Per_Sex_Per_Year
                    odictAgeNe_N1_Newborns_Per_Sex_Per_Year = objSSParameters.odictAgeNe_Sim_N1_Newborns_Per_Sex_Per_Year
                    pass
                else:
                    listSexes = objSSParameters.listAgeNe_Manual_ListSexes
                    intMaxAgeInYears = objSSParameters.intAgeNe_Manual_Max_Age
                    intMinMatingAgeInYears = objSSParameters.intAgeNe_Manual_Min_Mating_Age
                    intMaxMatingAgeInYears = objSSParameters.intAgeNe_Manual_Max_Mating_Age
                    #intAgeNe_N1_Newborns_Per_Age = objSSParameters.intAgeNe_Manual_N1_Newborns
                    intAgeNe_N1_Newborns_Per_Age = objSSParameters.intAgeNe_Manual_N1_Newborns
                    #intAgeNe_N1_Newborns_Per_Age = objSSParameters.intAgeNe_Manual_N1_Newborns_PREDICTED
                    #floatAgeNe_Initial_Male_Sex_Ratio  = objSSParameters.floatAgeNe_Manual_Initial_Male_Sex_Ratio 
                    floatAgeNe_N1_Male_Sex_Ratio  = objSSParameters.floatAgeNe_Manual_N1_Male_Sex_Ratio 
                    odictAgeNe_Age_Values_Survival_Rates = objSSParameters.odictAgeNe_Manual_Age_Values_Survival_Rates
                    if objSSParameters.boolAgeNeParmMatchManual_bx_genertated_in_Sim:
                        odictAgeNe_Age_Values_Birth_Rates = objSSParameters.odictAgeNe_Sim_b_x_Odict_Scaled_Birth_Rate_Per_Age_x #TEMP_FIX
                    #elif objSSParameters.boolAgeNeParmMatchManualToSim:
                    #    odictAgeNe_Age_Values_Birth_Rates = objSSParameters.odictAgeNe_Sim_Age_Values_Birth_Rates
                    #else:
                    odictAgeNe_Age_Values_Birth_Rates = objSSParameters.odictAgeNe_Manual_Age_Values_Birth_Rates
                    odictAgeNe_Alpha_Value_Scaling_Poisson_Variance_In_Reproductive_Success = objSSParameters.odictAgeNe_Manual_Alpha_Value_Scaling_Poisson_Variance_In_Reproductive_Success
                    #This is purely for DISPLAY PURPOSES ONLY
                    odictAgeNe_N1_Newborns_Per_Sex_Per_Year = objSSParameters.odictAgeNe_Manual_N1_Newborns_Per_Sex_Per_Year
                    
                #Initialize AgeNeDemographicTable values
                objAgeNeLifeTable = object_SSAgeNe_LifeTable()
                
                objAgeNeLifeTable.Use_Sim_Parameters = boolUseAgeNeSimParameters
                objAgeNeLifeTable.Max_Age = intMaxAgeInYears
                objAgeNeLifeTable.Min_Mating_Age = intMinMatingAgeInYears
                objAgeNeLifeTable.Max_Mating_Age = intMaxMatingAgeInYears
                objAgeNeLifeTable.List_Sexes = listSexes
                objAgeNeLifeTable.N1_Newborns = intAgeNe_N1_Newborns_Per_Age
                objAgeNeLifeTable.Initial_Male_Sex_Ratio = floatAgeNe_N1_Male_Sex_Ratio
                if boolUseAgeNeSimParameters:
                    #The scaled birth rate (b_x) is supplied
                    objAgeNeLifeTable.Nx_Odict_Newborns_Per_Age_x = odictAgeNe_Nx_Odict_Newborns_Per_Age_x
                    #objAgeNeLifeTable.b_x_Odict_Scaled_Birth_Rate_Per_Age_x = odictAgeNe_b_x_Odict_Scaled_Birth_Rate_Per_Age_x
                    objAgeNeLifeTable.N1_Newborns_Per_Sex_Per_Age = odictAgeNe_N1_Newborns_Per_Sex_Per_Year
                else:
                    #This is purely for DISPLAY PURPOSES ONLY
                    objAgeNeLifeTable.N1_Newborns_Per_Sex_Per_Age = odictAgeNe_N1_Newborns_Per_Sex_Per_Year
                    pass
#                 objAgeNeLifeTable.method_Initialise()
                pass
            
                for strSex in listSexes:
                    #Supply survival rates to AgeNe calculation
                    dictAgeValues = odictAgeNe_Age_Values_Survival_Rates[strSex]
                    odictAgeValues[strSex] = OrderedDict(sorted(dictAgeValues.items()))
                    objAgeNeLifeTable.sx_Odict_Survival_Rate_Per_Age_x[strSex] = odictAgeValues[strSex] 
                    
                    #Supply birth rates to AgeNe calculation
                    dictAgeValues = odictAgeNe_Age_Values_Birth_Rates[strSex]
                    odictAgeValues[strSex] = OrderedDict(sorted(dictAgeValues.items()))
                    objAgeNeLifeTable.bx_Odict_Birth_Rate_Per_Age_x[strSex] = odictAgeValues[strSex] 
                pass
                
                objAgeNeLifeTable.method_Initialise()
                #Perform AgeNe LifeTable calculations
                #DEBUG_ON
                int_Current_Replicate_Mating_Count = objSSParameters.int_MatingCount_Replicate_Total
                if int_Current_Replicate_Mating_Count == 77:
                    self.obj_Log_Debug_Display.debug('int_Current_Replicate_Mating_Count == 77')
                pass
                #DEBUG_OFF
                objAgeNeLifeTable.method_AgeNe_LifeTable_Final_Calculations()

                #Initialize Age NeDemographicTable values
                objAgeNeDemographicTable = object_SSAgeNe_DemographicTable()
                
                objAgeNeDemographicTable.Max_Age = objAgeNeLifeTable.Max_Age
                objAgeNeDemographicTable.List_Sexes = objAgeNeLifeTable.List_Sexes
                #objAgeNeDemographicTable.Initial_Male_Sex_Ratio = floatAgeNe_Initial_Male_Sex_Ratio
                objAgeNeDemographicTable.Initial_Male_Sex_Ratio = floatAgeNe_N1_Male_Sex_Ratio
                objAgeNeDemographicTable.Use_Sim_Parameters = objAgeNeLifeTable.Use_Sim_Parameters
#                 if boolUseAgeNeSimParameters:
#                     objAgeNeDemographicTable.N1_Newborns_Per_Sex_Per_Age = objAgeNeLifeTable.N1_Newborns_Per_Sex_Per_Age
#                 else:
#                     objAgeNeDemographicTable.N1_Newborns = objAgeNeLifeTable.N1_Newborns
                objAgeNeDemographicTable.N1_Newborns_Per_Sex_Per_Age = objAgeNeLifeTable.N1_Newborns_Per_Sex_Per_Age
                objAgeNeDemographicTable.N1_Newborns = objAgeNeLifeTable.N1_Newborns
                objAgeNeDemographicTable.b_x_Odict_Scaled_Birth_Rate_Per_Age_x = objAgeNeLifeTable.b_x_Odict_Scaled_Birth_Rate_Per_Age_x
                objAgeNeDemographicTable.lx_Odict_Fraction_Newborn_Still_Alive_Per_Age_x = objAgeNeLifeTable.lx_Odict_Fraction_Newborn_Still_Alive_Per_Age_x
                objAgeNeDemographicTable.Nx_Odict_Newborns_Per_Age_x = objAgeNeLifeTable.Nx_Odict_Newborns_Per_Age_x
                objAgeNeDemographicTable.Calculated_Totals_Life_Tables = objAgeNeLifeTable.Calculated_Totals
                objAgeNeDemographicTable.alpha_Value_Scaling_Poisson_Variance_In_Reproductive_Success = odictAgeNe_Alpha_Value_Scaling_Poisson_Variance_In_Reproductive_Success
#                 for strSex in listSexes:
#                     #Supply Poisson scaling factor (alpha) to AgeNe calculation
#                     dictAgeValues = odictAgeNe_Alpha_Value_Scaling_Poisson_Variance_In_Reproductive_Success[strSex]
#                     odictAgeValues[strSex] = OrderedDict(sorted(dictAgeValues.items()))
#                     objAgeNeDemographicTable.alpha_Value_Scaling_Poisson_Variance_In_Reproductive_Success[strSex] = odictAgeValues[strSex] 
               
                objAgeNeDemographicTable.method_Initialise()
                #Perform AgeNe DemographicTable calculations
                objAgeNeDemographicTable.method_AgeNe_DemographicTable_Final_Calculations()
                
                
                #Initialize AgeNe Calculation values
                objAgeNe = object_SSAgeNe()
                
                #objAgeNe.Initial_Male_Sex_Ratio = floatAgeNe_Initial_Male_Sex_Ratio
                objAgeNe.Initial_Male_Sex_Ratio = floatAgeNe_N1_Male_Sex_Ratio

                objAgeNe.List_Sexes = objAgeNeLifeTable.List_Sexes
                objAgeNe.Use_Sim_Parameters = objAgeNeLifeTable.Use_Sim_Parameters
                objAgeNe.N1_Newborns_Per_Sex_Per_Age = objAgeNeLifeTable.N1_Newborns_Per_Sex_Per_Age
                objAgeNe.N1_Newborns = objAgeNeLifeTable.N1_Newborns
                objAgeNe.Calculated_Totals_Life_Tables = objAgeNeLifeTable.Calculated_Totals
                objAgeNe.Calculated_Totals_Demographic_Tables = objAgeNeDemographicTable.Calculated_Totals
                objAgeNe.method_Initialise()
                
                #Perform AgeNe calculations
                objAgeNe.method_AgeNe_Final_Calculations()
                
                listOfAgeNeObjects= []
                listOfAgeNeObjects.append(objAgeNeLifeTable)
                listOfAgeNeObjects.append(objAgeNeDemographicTable)
                listOfAgeNeObjects.append(objAgeNe)
                
                return listOfAgeNeObjects


            def method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(self, float_Mean_Burrows_r_Squared__Observed, float_Mean_Burrows_r_Squared__Expected):
                
                float_Mean_Burrows_r_Squared_Diff = float_Mean_Burrows_r_Squared__Observed - float_Mean_Burrows_r_Squared__Expected
                
                return float_Mean_Burrows_r_Squared_Diff


            def method_Get_LDNe_From_Burrows_r_Squared_Results(self, float_Mean_Burrows_r_Squared__Observed, float_Mean_Burrows_r_Squared__Expected):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass 
                    
                float_Mean_Burrows_r_Squared_Diff = self.method_Get_Burrows_r_Squared_Observed_Minus_Expected_Results(float_Mean_Burrows_r_Squared__Observed, float_Mean_Burrows_r_Squared__Expected)

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    str_Message = 'float_Mean_Burrows_r_Squared__Observed: ' + str(float_Mean_Burrows_r_Squared__Observed)
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    str_Message = 'float_Mean_Burrows_r_Squared__Expected: ' + str(float_Mean_Burrows_r_Squared__Expected)
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    str_Message = 'float_Mean_Burrows_r_Squared_Diff: ' + str(float_Mean_Burrows_r_Squared_Diff)
                    self.obj_Log_Debug_Display.debug(str_Message)
                pass
                #DEBUG_OFF

                ''' LDNe is Inf by default '''
                float_LDNe = float('Inf')
                ''' Check that calc can proceed - If the Observed r^2 - Expected r^2 < 0 then LDNe cannot be calculated and LDNe = float('Inf') '''               
                if float_Mean_Burrows_r_Squared_Diff != 0:

                    #DEBUG_ON
                    if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                        str_Message = 'Trying Calc: LDNe = (((float(1)/float(3)) + math__sqrt((float(1)/float(9))-(float(2.76)*(' + str(float_Mean_Burrows_r_Squared_Diff) + ')))) / (float(2)*(' + str(float_Mean_Burrows_r_Squared_Diff) + ')))'
                        self.obj_Log_Debug_Display.debug(str_Message)
                    pass
                    #DEBUG_OFF
                                    
                    ''' Check that Sqrt is not presented with a negative number '''
                    
                    float_Sqrt_Subject = ((float(1)/float(9))-(float(2.76)*(float_Mean_Burrows_r_Squared_Diff)))

                    #DEBUG_ON
                    if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                        str_Message = 'float_Sqrt_Subject: ' + str(float_Sqrt_Subject)
                        self.obj_Log_Debug_Display.debug(str_Message)
                    pass
                    #DEBUG_OFF
                                    
                    if float_Sqrt_Subject >= 0:
                        
                        ''' Perform the LDNe calculation '''
                        float_LDNe = (((float(1)/float(3)) + math__sqrt((float(1)/float(9))-(float(2.76)*(float_Mean_Burrows_r_Squared_Diff))))
                                        /
                                        (float(2)*(float_Mean_Burrows_r_Squared_Diff)))
                    
                    else:
                        #DEBUG_ON
                        if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                            str_Message = 'LDNe = Inf because Sqrt subject is < 0 (Negative) and cannot be Square rooted'
                            self.obj_Log_Debug_Display.debug(str_Message)
                        pass           
                        #DEBUG_OFF             
                    pass
                else:
                    #DEBUG_ON
                    if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                        str_Message = 'LDNe = Inf because the Observed r^2 - Expected r^2 < 0'
                        self.obj_Log_Debug_Display.debug(str_Message)
                    pass
                    #DEBUG_OFF
                pass
            
                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    str_Message = 'float_LDNe: ' + str(float_LDNe)
                    self.obj_Log_Debug_Display.debug(str_Message)
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass 
                                       
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    str_Message = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message, bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
                #DEBUG_OFF
                    
                return float_LDNe


            def func_Get_Pandas_Dataframe_Harmonic_Mean_Including_Negatives_PREV(self, float_Value):    

                ''' Perform calculation '''
                try:
                    float_Harmonic_Mean = len(float_Value) / (numpy__sum(1.0 / float_Value))
                    return float_Harmonic_Mean
                 
                except ZeroDivisionError:
                    float_Harmonic_Mean = len(float_Value) / numpy__sum(1.0)
                    return float_Harmonic_Mean

                pass
             
            def func_Get_Pandas_Dataframe_Harmonic_Mean_Including_Negatives(self, float_Value):    

                ''' Perform calculation '''
                try:
                
                    float_Harmonic_Mean = len(float_Value) / (numpy__sum(1.0 / float_Value))
                    return float_Harmonic_Mean
                 
                except ZeroDivisionError:
                    float_Harmonic_Mean = len(float_Value) / numpy__sum(1.0)
                    return float_Harmonic_Mean

                pass
             
                   
            def method_Calculate_Demographic_Ne_By_Sex(self, int_Unique_Female_Effective_Parents, int_Unique_Male_Effective_Parents):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass
                                 
                '''
                Demo Ne Eqn 1 = 4(Nf.Nm) / (Nf + Nm)
                '''
                
                float_Ne_By_Sex = ((4*int_Unique_Female_Effective_Parents*int_Unique_Male_Effective_Parents) / (int_Unique_Female_Effective_Parents + int_Unique_Male_Effective_Parents))
                

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    self.obj_Log_Debug_Display.debug('float_Ne_By_Sex :' + str(float_Ne_By_Sex))
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    str_Message = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message, bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
                           
                return float_Ne_By_Sex


            def method_Get_SimupopStat_Demographic_Ne_Crow_And_Denniston_1988(self, pop_In):
                
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass       
                
                simupop.stat(pop_In, effectiveSize=[0], subPops=[(globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult)], vars=['Ne_demo_sp'])
                dictCD_DemoNeStats = pop_In.dvars((globalsSS.SP_SubPops.static_intSP_SubPop_Primary, globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult)).Ne_demo
                float_Crow_And_Denniston_1988_DemoNe = dictCD_DemoNeStats[0]

                #DEBUG_ON
                if globalsSS.Logger_Debug_Display.bool_Debug_Display:
                    str_Message_Location = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
                    self.obj_Log_Debug_Display.debug(str_Msg_Prefix + str_Message_Location)
                    self.obj_Log_Debug_Display.debug('float_Crow_And_Denniston_1988_DemoNe :' + str(float_Crow_And_Denniston_1988_DemoNe))
                    #simupop.dump(pop)
                    #with globalsSS.Pause_Console() as obj_Pause:
                    #    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
                            
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    str_Message = str(self.__class__.__name__) + '.' +  str(sys._getframe().f_code.co_name)
                    t2.Stop(self.obj_Log_Debug_Timing, str_Message, bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass 
                            
                return float_Crow_And_Denniston_1988_DemoNe


            def method_Get_C_And_D_1988_Demographic_Ne_Summary_Stats_For_Overlapping_Gens(self, pop_PostMating, intSP, intVSP, dict_Results):

                dictSireOffspringCount = self.method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(pop_PostMating, intSP, intVSP)
                dictDameOffspringCount = self.method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(pop_PostMating, intSP, intVSP)
                dictOffspringCount = self.method_Count_Offspring_PerParent_For_VirtualSubPop(pop_PostMating, dictSireOffspringCount, dictDameOffspringCount, intSP, intVSP)                    
                            
                dict_Results = self.method_Embryo_Offspring_Parent_Ne_Summary_Stats_Method_2(dictSireOffspringCount, dictDameOffspringCount, dictOffspringCount, dict_Results, intSP, intVSP)
            
                float_Last_Gen_DCB_CD_DemoNe_By_Sex = dict_Results['Demo_NePP_=_(4.NeF.NeM)/(NeF+NeM)']
                
                return dict_Results, float_Last_Gen_DCB_CD_DemoNe_By_Sex
    
            
            def method_Get_C_And_D_1988_Demographic_Ne_Summary_Stats_For_Discrete_Gens(self, pop_PreMating, pop_PostMating, dict_Results):
             
                intSP = 0
                intVSP = -1
        
                dictSireOffspringCount = self.method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(pop_PostMating, intSP, intVSP)
                dictDameOffspringCount = self.method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(pop_PostMating, intSP, intVSP)
                dictOffspringCount = self.method_Count_Offspring_PerParent_For_VirtualSubPop(pop_PreMating, dictSireOffspringCount, dictDameOffspringCount, intSP, intVSP)                    
                            
                dict_Results = self.method_Embryo_Offspring_Parent_Ne_Summary_Stats_Method_2(dictSireOffspringCount, dictDameOffspringCount, dictOffspringCount, dict_Results, intSP, intVSP)
            
                return dict_Results
  
            
            def method_Statistics_On_NE_Demographic_Population_Size_For_VirtualSubPop(self, pop, listSingleVirtualSubPop):

                '''
                Provide statitics on  NE Demographic population size in any pop
                
                A dictionary of locus-specific demographic effective population size, 
                calculated using number of gametes each parent transmits to the
                offspring population.
                The method is based on Crow & Denniston 1988
                (Ne = KN-1/k-1+Vk/k) and need variable Ne_demo_base
                set before mating.
                Effective size estimated from this formula is model dependent
                and might not be applicable to your mating schemes.
                '''     
                
                listStatistics=[]
                if listSingleVirtualSubPop == 0:
                    listStatistics = pop.dvars().Ne_demo
                else:
                    #listStatistics = pop.dvars(listSingleVirtualSubPop).Ne_demo_sp

                    try:
                        listStatistics = pop.dvars(listSingleVirtualSubPop).Ne_demo_sp
                    except AttributeError, e:
                        self.obj_Log_Default_Display.error('Module: ' + gstringModuleName + '; Class: ' + gstringClassName + '; Message: Error getting simuPOP Stat Demo Ne for VSP: ' + str(listSingleVirtualSubPop) + '; Error is :' + str(e))

                return listStatistics


            def method_Statistics_On_NE_LD_Population_Size_For_VirtualSubPop(self, pop, listSingleVirtualSubPop):

                '''
                Provide statitics on  NE LD population size in any pop

                Lists of length three for effective population size,
                2.5% and 97.% confidence interval for cutoff allele frequency
                0., 0.01, 0.02 and 0.05 (as dictionary keys), using a
                parametric method, estimated from linkage disequilibrim
                information of one sample, using LD method developed by Waples
                & Do 2006 (LDNe). This method assumes unlinked loci and uses
                LD measured from genotypes at loci. Because this is a sample
                based method, it should better be applied to a random sample
                of the population. 95% CI is calculated using a Jackknife
                estimated effective number of independent alleles. Please
                refer to relevant papers and the LDNe user's guide for
                details.

                '''
                     
                if type(listSingleVirtualSubPop[0]) == tuple:
                    listSingleVirtualSubPop = [listSingleVirtualSubPop[0][0],listSingleVirtualSubPop[0][1]]
                pass
                
                listStatistics=[]
#                 if listSingleVirtualSubPop == 0:
#                     listStatistics = pop.dvars().Ne_LD
#                 else:
#                     #This a temporary fix to cut down on LDNe calculations which slow the sim down.
#                     #I only process VSPs 0-2 but when the final output is to be written all the VSP ie. 0-3 are passed and the pop.dvars([0,3)] fails as NE_LD was not recorded
#                     if listSingleVirtualSubPop[1] != 3:  
#                         listStatistics = pop.dvars(listSingleVirtualSubPop).Ne_LD
#                     else:
#                         listStatistics = 0
                
                try:
                    listStatistics = pop.dvars(listSingleVirtualSubPop).Ne_LD
                except AttributeError, e:
                    #DEBUG_ON
                    #LOGGING
#                     print('!!!ERROR')
#                     print('!!!ERROR - ' + str(e))
#                     print('!!!ERROR - Module: ' + gstringModuleName + ' Class: ' + gstringClassName + ' Message: method_Statistics_On_NE_LD_Population_Size_For_VirtualSubPop - VSPs to Report:' + str(listSingleVirtualSubPop) + '\n')
#                     print('!!!ERROR')
                    self.obj_Log_Default_Display.error('Module: ' + gstringModuleName + '; Class: ' + gstringClassName + '; Message: Error getting simuPOP Stat LDNe for VSP: ' + str(listSingleVirtualSubPop) + '; Error is :' + str(e))
                    #LOGGING
                    #DEBUG_OFF
                    #traceback.print_exc()
                    #exit(3)
                
                return listStatistics


            def method_Statistics_On_NE_Temporal_JordeRyman_P1_Population_Size_For_VirtualSubPop(self, pop, listSingleVirtualSubPop):

                '''
                Provide statitics on  NE Temporal Jorde & Ryman (sampling plan 1) population size in any pop

                Effective population size, 2.5% and 97.5%
                confidence interval for sampling plan 1 as a list of size 3,
                estimated using a temporal method as described in Jorde &amp;
                Ryman (2007), and as implemented by software tempoFS
                (http://www.zoologi.su.se/~ryman/). This variable is set to
                census population size if no baseline has been set, and to the
                temporal effective size between the present and the baseline
                generation otherwise. This method uses population size or sum
                of subpopulation sizes of specified (virtual) subpopulations
                as census population size for the calculation based on plan 1.

                '''     
                
                listStatistics=[]
                if listSingleVirtualSubPop == 0:
                    listStatistics = pop.dvars().Ne_tempoFS_P1
                else:
                    listStatistics = pop.dvars(listSingleVirtualSubPop).Ne_tempoFS_P1

                return listStatistics


            def method_Statistics_On_NE_Temporal_JordeRyman_P2_Population_Size_For_VirtualSubPop(self, pop, listSingleVirtualSubPop):

                '''
                Provide statitics on  NE Temporal Jorde & Ryman (sampling plan 1) population size in any pop

                Effective population size, 2.5% and 97.5%
                confidence interval for sampling plan 2 as a list of size 6,
                estimated using a temporal method as described in Jorde &amp;
                Ryman (2007). This variable is set to census population size
                no baseline has been set, and to the temporal effective size
                between the present and the baseline generation otherwise.
                This method assumes that the sample is drawn from an
                infinitely-sized population.
                '''     
                
                listStatistics=[]
                if listSingleVirtualSubPop == 0:
                    listStatistics = pop.dvars().Ne_tempoFS_P2
                else:
                    listStatistics = pop.dvars(listSingleVirtualSubPop).Ne_tempoFS_P2

                return listStatistics


            '''
            --------------------------------------------------------------------------------------------------------
            # Simupop - SPLIT functions
            --------------------------------------------------------------------------------------------------------
            '''


            def method_VSP_Split_Pop_By_Sex(self, pop_In):

                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2 = Timer2(True)
                    t2.Start()
                pass  
            
                '''
                VSP Splits - SEX
                '''

                               
                pop_In.setVirtualSplitter(
                                          simupop.SexSplitter(
                                              names=[
                                                    globalsSS.SexConstants.static_stringSexMale
                                                    ,globalsSS.SexConstants.static_stringSexFemale
                                                    ]))


                pop_Out = pop_In
                
                if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
                    #pdb.set_trace()
                    #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                    #    t2 = Timer2(True)
                    #    t2.Start()
                    #pass                    
                pass
               
                return pop_Out


            def method_Split_Reproductively_Mature_VSP_By_Sex(self, pop_In):
                
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
    
            
            def method_Split_Embryo_VSP_By_Sex(self, pop_In):
                
                pop_In.setVirtualSplitter(
                              simupop.ProductSplitter([
                                         simupop.InfoSplitter('life_stage',
                                         values=[globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo],
                                         names=[globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo]),
                                         simupop.SexSplitter()
                                         ], 
                                         names=[
                                                globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo_Male
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo_Female
                                                ]))
                
                pop_Out = pop_In    
                
                return pop_Out   


            def method_VSP_Split_Age_Class_By_Sex(self, pop_In):
                
                pop_In.setVirtualSplitter(
                              simupop.ProductSplitter([
                                         simupop.SexSplitter(
                                         names=[
                                                globalsSS.SexConstants.static_stringSexMale
                                                ,globalsSS.SexConstants.static_stringSexFemale
                                                ]),
                                         simupop.InfoSplitter('age_class',
                                         values = [ 
                                                    globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Embryo
                                                    #,globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Neonate
                                                    ,globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Juvenile
                                                    ,globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Reproductivly_available_adult
                                                    ,globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Senescent_adult
                                                    ,globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Died
                                                    ],
                                         names = [
                                                    globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Embryo
                                                    #,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Neonate
                                                    ,globalsSS.VSP_AgeClass.static_intVSP_AgeClass_Juvenile
                                                    ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult
                                                    ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Senescent_adult
                                                    ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Died
                                                    ])],
                                                          
                                         names=[
                                                    globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Embryo_Male
                                                    #,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Neonate_Male
                                                    ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Juvenile_Male
                                                    ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult_Male
                                                    ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Senescent_adult_Male
                                                    ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Died_Male
                                                    ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Embryo_Female
                                                    #,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Neonate_Female
                                                    ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Juvenile_Female
                                                    ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Reproductivly_available_adult_Female
                                                    ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Senescent_adult_Female
                                                    ,globalsSS.VSP_AgeClass.static_string_Age_Class_VSP_Name_Died_Female
                                                    ])
                                        )
                
                pop_Out = pop_In    
                
                return pop_Out   
   
                                   
            def method_VSP_Split_Life_Stage_By_Sex(self, pop_In):
                
                pop_In.setVirtualSplitter(
                              simupop.ProductSplitter([
                                         simupop.SexSplitter(
                                         names=[
                                                globalsSS.SexConstants.static_stringSexMale
                                                ,globalsSS.SexConstants.static_stringSexFemale
                                                ]),
                                         simupop.InfoSplitter('life_stage',
                                         values = [ 
                                                    globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Embryo
                                                    #,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Neonate
                                                    ,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Juvenile
                                                    #,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Sub_adult
                                                    ,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Reproductivly_available_adult
                                                    ,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Gestating_adult_female
                                                    ,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Resting_adult_female
                                                    ,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Senescent_adult
                                                    ,globalsSS.VSP_LifeStage.static_intVSP_LifeStage_Died
                                                    ],
                                         names = [
                                                    globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo
                                                    #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Neonate
                                                    ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Juvenile
                                                    #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Sub_adult
                                                    ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult
                                                    ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Gestating_adult_female
                                                    ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Resting_adult_female
                                                    ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Senescent_adult
                                                    ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Died
                                                    ])],
                                                          
                                         names=[
                                                globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo_Male
                                                #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Neonate_Male
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Juvenile_Male
                                                #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Sub_adult_Male
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult_Male
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Gestating_adult_female_Male
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Resting_adult_female_Male
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Senescent_adult_Male
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Died_Male
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Embryo_Female
                                                #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Neonate_Female
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Juvenile_Female
                                                #,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Sub_adult_Female
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Reproductivly_available_adult_Female
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Gestating_adult_female_Female
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Resting_adult_female_Female
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Senescent_adult_Female
                                                ,globalsSS.VSP_LifeStage.static_string_Life_Stage_VSP_Name_Died_Female
                                                    ])
                                        )
                
                pop_Out = pop_In    
                
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
    
                                   
            def method_SplitPopIntoTemporaryVSPs_ByValue_ToUpdateInfoFields(self, pop_In, intSubPop, boolUpdateInfoField, stringVSPSplitOperator, stringInfoFieldToSplitBy, listVSPSplitValues, listVSPSplitNames, stringInfoFieldToUpdate='', listVSPsToUpdate=[], listUpdateValues=[]):
                
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
               
                pop_Out = pop_In
                
                return pop_Out


           
 
            '''            
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS FINALIZATION
            '''            
            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.SSAnalysisOperation_obj = SSAnalysisOperation() 
        return self.SSAnalysisOperation_obj
 
    def __exit__(self, type, value, traceback): 
        self.SSAnalysisOperation_obj.classCleanUp()