#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
#from simuPOP
import simuPOP as sim
from AutoVivificationHandler import AutoVivificationHandler
from SSOutputHandler import SSOutputHandler
from SSAnalysisHandler import SSAnalysisHandler
from AnalysisHandler import AnalysisHandler
from globals_SharkSim import globalsSS
from object_SSRepProperty import object_SSPropertyHandler
from object_SSReportingProperty import object_SSReportingProperty
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
import re

class object_SSReportingCustom_2(object):
    """Contains SS Simulation level properties and methods"""
    def __enter__(self):

        class obj_SSReportingCustom_1():

# -------------- Class specific routines

            __slots__ = (
                         'static_stringNotSuppressed'
                         ,'dictPropertiesNotSuppressed'
                         ,'stringNotApplicable'
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

                        ,'dictReportingPropertyObjects'
                        )

            def __init__(self):
                
                globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed = 'NSUP'
                globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed = 'SUP'
                self.static_stringNotSpecified = 'NSP'
                globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed = 'SUPNOUT'
                
                self.dictPropertiesNotSuppressed = {}
                self.stringNotApplicable = 'NA'
                #globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed = 'SUP'
                
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
                dictSireOffspringCount = AutoVivificationHandler()
                dictDameOffspringCount = AutoVivificationHandler()
                dictOffspringCount = AutoVivificationHandler()

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
                
                self.dictReportingPropertyObjects = AutoVivificationHandler()
                self.boolAtleastTwoSubPops = False
                
            def method_PopulateProperties(self, boolIncludeParentOffspringProperties):

                #Reporting variables

#                 dictDataSectionNotesLevels = AutoVivificationHandler()
#                 dict_SubPop_VSP = AutoVivificationHandler()
#                 dict_SubPopSize_VSP = AutoVivificationHandler()
#                 dict_NeDemographic_VSP = AutoVivificationHandler()
#                 dict_temporal_JR_P1_ne_VSP = AutoVivificationHandler()
#                 dict_temporal_JR_P1_ne_2_5_CI_VSP = AutoVivificationHandler()
#                 dict_temporal_JR_P1_ne_97_5_CI_VSP = AutoVivificationHandler()
#                 dict_temporal_JR_P2_ne_VSP = AutoVivificationHandler()
#                 dict_temporal_JR_P2_ne_2_5_CI_VSP = AutoVivificationHandler()
#                 dict_temporal_JR_P2_ne_97_5_CI_VSP = AutoVivificationHandler()
#                 dict_ld_ne_pcrit_0_VSP = AutoVivificationHandler()
#                 dict_ld_ne_pcrit_0_lwr_ci_VSP = AutoVivificationHandler()
#                 dict_ld_ne_pcrit_0_upr_ci_VSP = AutoVivificationHandler()
#                 dict_ld_ne_pcrit_0_05_VSP = AutoVivificationHandler()
#                 dict_ld_ne_pcrit_0_05_lwr_ci_VSP = AutoVivificationHandler()
#                 dict_ld_ne_pcrit_0_05_upr_ci_VSP = AutoVivificationHandler()
#                 dict_ld_ne_pcrit_0_02_VSP = AutoVivificationHandler()
#                 dict_ld_ne_pcrit_0_02_lwr_ci_VSP = AutoVivificationHandler()
#                 dict_ld_ne_pcrit_0_02_upr_ci_VSP = AutoVivificationHandler()
#                 dict_ld_ne_pcrit_0_01_VSP = AutoVivificationHandler()
#                 dict_ld_ne_pcrit_0_01_lwr_ci_VSP = AutoVivificationHandler()
#                 dict_ld_ne_pcrit_0_01_upr_ci_VSP = AutoVivificationHandler()
                dict_AlleleTotalPerLocus_VSP = AutoVivificationHandler()
                dict_dictAlleleInstanceCountPerLocus_VSP = AutoVivificationHandler()
                dict_dictAlleleFreqs_VSP = AutoVivificationHandler()
#                 dict_Num_Sire_Parent  = AutoVivificationHandler()
#                 dict_Mean_Offspring_Per_Sire_Parent  = AutoVivificationHandler()
#                 dict_Mean_Variance_Per_Sire_Parent  = AutoVivificationHandler()
#                 dict_Num_Dame_Parent  = AutoVivificationHandler()
#                 dict_Mean_Offspring_Per_Dame_Parent  = AutoVivificationHandler()
#                 dict_Mean_Variance_Per_Dame_Parent  = AutoVivificationHandler()
#                 dict_Num_Male_Potential_Parent  = AutoVivificationHandler()
#                 dict_Mean_Offspring_Per_Male_Potential_Parent  = AutoVivificationHandler()
#                 dict_Mean_Variance_Per_Male_Potential_Parent  = AutoVivificationHandler()
#                 dict_Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents = AutoVivificationHandler()
#                 dict_Num_Female_Potential_Parent  = AutoVivificationHandler()
#                 dict_Mean_Offspring_Per_Female_Potential_Parent  = AutoVivificationHandler()
#                 dict_Mean_Variance_Per_Female_Potential_Parent  = AutoVivificationHandler()
#                 dict_Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents = AutoVivificationHandler()
#                 dict_Num_Actual_Parent  = AutoVivificationHandler()
#                 dict_Mean_Offspring_Per_Actual_Parent  = AutoVivificationHandler()
#                 dict_Mean_Variance_Per_Actual_Parent  = AutoVivificationHandler()
#                 dict_Num_Potential_Parent  = AutoVivificationHandler()
#                 dict_Mean_Offspring_Per_Potential_Parent  = AutoVivificationHandler()
#                 dict_Mean_Variance_Per_Potential_Parent  = AutoVivificationHandler()
#                 dict_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne  = AutoVivificationHandler()
#                 dict_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents   = AutoVivificationHandler()
                
#                 dictProperty = {}
                
                #End of local variable declaration
                              
                #dictDataSectionNotesLevels[self.intLevel]['Data_Section_Note_' + str(self.intLevel)] = 'Virtual_Pop_Level_Params'
                '''#>>>>> PROPERTY -Initialize property values'''
                listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Data_Section_Note
                listPropertyLabelPrefixes = ['', '','','','','']
                propertySuppressedValue, propertyValue = '',''
                #Determine if property required
                if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                    if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                        #Get the property reporting value
                        propertyValue = 'Data_Section_Note_' + str(self.intLevel)
                    else:
                        propertySuppressedValue = self.dictPropertiesNotSuppressed[listPropertyLabels[0]]
                else:
                        propertySuppressedValue = self.static_stringNotSpecified
                #Assign property values        
                dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

                #Specify the number of VSP being reported 
                self.intNumberVirtualSubPops = self.pop.numVirtualSubPop()
                self.boolAtleastTwoSubPops = False
                if self.intNumberVirtualSubPops > 1:
                    self.boolAtleastTwoSubPops = True 
                #Report of each VSP in turn
                for itemVirtualSubPop in self.listVirtSubPopsToOutput:
                    
                    #VSP has individuals so continue
                    self.listCurrentVSP.append(itemVirtualSubPop)
                    self.listSingleVirtualSubPop = self.listCurrentVSP[0]
                    self.intVirtualSubPop = int(re.findall( r'\,(.*?)\)', str(self.listSingleVirtualSubPop))[0])
                    '''
                    >>>>>>> Assign Properties <<<<<<<<
                    '''
                                        
                    '''#>>>>> PROPERTY -Initialize property values'''
                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Sub_Pop_VSP
                    listPropertyLabelPrefixes = ['', '','','','','']
                    propertySuppressedValue, propertyValue = '',''
                    #Determine if property required
                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                            #Get the property reporting value
                            propertyValue = self.listCurrentVSP
                        else:
                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                    else:
                            propertySuppressedValue = self.static_stringNotSpecified
                    #Assign property values        
                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
                    
                    
                    #This flag has to be set here and control operations as well as being areported property
                    intVSPSize = self.pop.subPopSize(self.listSingleVirtualSubPop)
                    '''#>>>>> PROPERTY -Initialize property values'''
                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Sub_Pop_Size_VSP
                    listPropertyLabelPrefixes = ['', '','','','','']
                    propertySuppressedValue, propertyValue = '',''
                    #Determine if property required
                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                            #Get the property reporting value
                            propertyValue = intVSPSize
                        else:
                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                    else:
                            propertySuppressedValue = self.static_stringNotSpecified
                    #Assign property values        
                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
                    
#                     stringPropertyKey = 'Sub_Pop_Size_VSP'
#                     if stringPropertyKey in self.dictPropertiesNotSuppressed:
#                         if self.dictPropertiesNotSuppressed[stringPropertyKey] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
#                             intVSPSize = self.pop.subPopSize(self.listSingleVirtualSubPop)
#                             dict_SubPopSize_VSP[self.listSingleVirtualSubPop][stringPropertyKey] = intVSPSize
#                     dictProperty = dict_SubPopSize_VSP 
#                     self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
                    
                    boolVSPHasIndivs = False
                    if intVSPSize > 0:
                        boolVSPHasIndivs = True

                    with SSAnalysisHandler() as objSSAnalysisOperation:
                        if self.objSSParametersLocal.boolReportDemographicNe:
                            #Demographic Ne for entire pop
                            dictNeDemographic = objSSAnalysisOperation.method_Statistics_On_NE_Demographic_Population_Size_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                            value = dictNeDemographic[0] #Only take the value for the first locus as they should all be the same
                        else:
                            value = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed

                        ''''''#>>>>> PROPERTY -Initialize property values''''''
                        listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_demographic_ne_loci_1_VSP
                        listPropertyLabelPrefixes = ['', '','','','','']
                        propertySuppressedValue, propertyValue = '',''
                        #Determine if property required
                        if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                            if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                #Get the property reporting value
                                propertyValue = value
                            else:
                                propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                        else:
                                propertySuppressedValue = self.static_stringNotSpecified
                        #Assign property values        
                        dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                        self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
                        
#                         stringPropertyKey = 'demographic_ne_loci_1_VSP'
#                         if self.dictPropertiesNotSuppressed[stringPropertyKey] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
#                             dict_NeDemographic_VSP[self.listSingleVirtualSubPop][stringPropertyKey] = value
#                         dictProperty = dict_NeDemographic_VSP 
#                         self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

                        listNeTemporal_JR_P1 = []
                        listNeTemporal_JR_P2 = []
                        if boolVSPHasIndivs:
                            
                            if self.objSSParametersLocal.boolReportTemporalFS_P1_Ne:
                                #Temporal JR P1 Ne for entire pop
                                listNeTemporal_JR_P1 = objSSAnalysisOperation.method_Statistics_On_NE_Temporal_JordeRyman_P1_Population_Size_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                            else:
                                #Output has been suppressed
                                for i in range(0, 3):
                                    listNeTemporal_JR_P1.append(globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed)
                                    
                            listNeTemporal_JR_P2 = []
                            if self.objSSParametersLocal.boolReportTemporalFS_P2_Ne:
                                #Temporal JR P2 Ne for entire pop
                                listNeTemporal_JR_P2 = objSSAnalysisOperation.method_Statistics_On_NE_Temporal_JordeRyman_P2_Population_Size_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                            else:
                                #Output has been suppressed
                                for i in range(0, 3):
                                    listNeTemporal_JR_P2.append(globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed)
                        else:
                            #Output is not applicable
                            for i in range(0, 3):
                                listNeTemporal_JR_P1.append(self.stringNotApplicable)
                                listNeTemporal_JR_P2.append(self.stringNotApplicable)
                        
                        '''#>>>>> PROPERTY -Initialize property values'''
                        listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_temporal_JR_P1_ne_VSP
                        listPropertyLabelPrefixes = ['', '','','','','']
                        propertySuppressedValue, propertyValue = '',''
                        #Determine if property required
                        if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                            if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                #Get the property reporting value
                                propertyValue = listNeTemporal_JR_P1[0]
                            else:
                                propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                        else:
                                propertySuppressedValue = self.static_stringNotSpecified
                        #Assign property values        
                        dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                        self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

                        '''#>>>>> PROPERTY -Initialize property values'''
                        listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_temporal_JR_P1_ne_2_5_CI_VSP
                        listPropertyLabelPrefixes = ['', '','','','','']
                        propertySuppressedValue, propertyValue = '',''
                        #Determine if property required
                        if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                            if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                #Get the property reporting value
                                propertyValue = listNeTemporal_JR_P1[1]
                            else:
                                propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                        else:
                                propertySuppressedValue = self.static_stringNotSpecified
                        #Assign property values        
                        dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                        self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
                        
                        '''#>>>>> PROPERTY -Initialize property values'''
                        listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_temporal_JR_P1_ne_97_5_CI_VSP
                        listPropertyLabelPrefixes = ['', '','','','','']
                        propertySuppressedValue, propertyValue = '',''
                        #Determine if property required
                        if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                            if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                #Get the property reporting value
                                propertyValue = listNeTemporal_JR_P1[2]
                            else:
                                propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                        else:
                                propertySuppressedValue = self.static_stringNotSpecified
                        #Assign property values        
                        dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                        self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
                        
#                         dict_temporal_JR_P2_ne_VSP[self.listSingleVirtualSubPop]['temporal_JR_P2_ne_VSP'] = listNeTemporal_JR_P2[0]
#                         dict_temporal_JR_P2_ne_2_5_CI_VSP[self.listSingleVirtualSubPop]['temporal_JR_P2_ne_2.5_CI_VSP'] = listNeTemporal_JR_P2[1]
#                         dict_temporal_JR_P2_ne_97_5_CI_VSP[self.listSingleVirtualSubPop]['temporal_JR_P2_ne_97.5_CI_VSP'] = listNeTemporal_JR_P2[2]

                        '''#>>>>> PROPERTY -Initialize property values'''
                        listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_temporal_JR_P2_ne_VSP
                        listPropertyLabelPrefixes = ['', '','','','','']
                        propertySuppressedValue, propertyValue = '',''
                        #Determine if property required
                        if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                            if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                #Get the property reporting value
                                propertyValue = listNeTemporal_JR_P2[0]
                            else:
                                propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                        else:
                                propertySuppressedValue = self.static_stringNotSpecified
                        #Assign property values        
                        dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                        self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

                        '''#>>>>> PROPERTY -Initialize property values'''
                        listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_temporal_JR_P2_ne_2_5_CI_VSP
                        listPropertyLabelPrefixes = ['', '','','','','']
                        propertySuppressedValue, propertyValue = '',''
                        #Determine if property required
                        if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                            if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                #Get the property reporting value
                                propertyValue = listNeTemporal_JR_P2[1]
                            else:
                                propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                        else:
                                propertySuppressedValue = self.static_stringNotSpecified
                        #Assign property values        
                        dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                        self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
                        
                        '''#>>>>> PROPERTY -Initialize property values'''
                        listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_temporal_JR_P2_ne_97_5_CI_VSP
                        listPropertyLabelPrefixes = ['', '','','','','']
                        propertySuppressedValue, propertyValue = '',''
                        #Determine if property required
                        if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                            if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                #Get the property reporting value
                                propertyValue = listNeTemporal_JR_P2[2]
                            else:
                                propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                        else:
                                propertySuppressedValue = self.static_stringNotSpecified
                        #Assign property values        
                        dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                        self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

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
                            
#                                 dict_ld_ne_pcrit_0_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0_VSP'] = round(dictNeLD[0.0][0],4)
#                                 dict_ld_ne_pcrit_0_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0_lwr_ci_VSP'] = round(dictNeLD[0.0][1],4)
#                                 dict_ld_ne_pcrit_0_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0_upr_ci_VSP'] = round(dictNeLD[0.0][2],4)

                            '''#>>>>> PROPERTY -Initialize property values'''
                            listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_ld_ne_pcrit_0_VSP
                            listPropertyLabelPrefixes = ['', '','','','','']
                            propertySuppressedValue, propertyValue = '',''
                            #Determine if property required
                            if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                    #Get the property reporting value
                                    propertyValue = round(dictNeLD[0.0][0],4)
                                else:
                                    propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                            else:
                                    propertySuppressedValue = self.static_stringNotSpecified
                            #Assign property values        
                            dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                            self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

                            '''#>>>>> PROPERTY -Initialize property values'''
                            listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_ld_ne_pcrit_0_lwr_ci_VSP
                            listPropertyLabelPrefixes = ['', '','','','','']
                            propertySuppressedValue, propertyValue = '',''
                            #Determine if property required
                            if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                    #Get the property reporting value
                                    propertyValue = round(dictNeLD[0.0][1],4)
                                else:
                                    propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                            else:
                                    propertySuppressedValue = self.static_stringNotSpecified
                            #Assign property values        
                            dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                            self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

                            '''#>>>>> PROPERTY -Initialize property values'''
                            listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_ld_ne_pcrit_0_upr_ci_VSP
                            listPropertyLabelPrefixes = ['', '','','','','']
                            propertySuppressedValue, propertyValue = '',''
                            #Determine if property required
                            if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                    #Get the property reporting value
                                    propertyValue = round(dictNeLD[0.0][2],4)
                                else:
                                    propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                            else:
                                    propertySuppressedValue = self.static_stringNotSpecified
                            #Assign property values        
                            dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                            self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty


#                                 dict_ld_ne_pcrit_0_05_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.05_VSP'] = round(dictNeLD[0.05][0],4)
#                                 dict_ld_ne_pcrit_0_05_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.05_lwr_ci_VSP'] = round(dictNeLD[0.05][1],4)
#                                 dict_ld_ne_pcrit_0_05_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.05_upr_ci_VSP'] = round(dictNeLD[0.05][2],4)

                            '''#>>>>> PROPERTY -Initialize property values'''
                            listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_ld_ne_pcrit_0_05_VSP
                            listPropertyLabelPrefixes = ['', '','','','','']
                            propertySuppressedValue, propertyValue = '',''
                            #Determine if property required
                            if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                    #Get the property reporting value
                                    propertyValue = round(dictNeLD[0.05][0],4)
                                else:
                                    propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                            else:
                                    propertySuppressedValue = self.static_stringNotSpecified
                            #Assign property values        
                            dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                            self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

                            '''#>>>>> PROPERTY -Initialize property values'''
                            listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_ld_ne_pcrit_0_05_lwr_ci_VSP
                            listPropertyLabelPrefixes = ['', '','','','','']
                            propertySuppressedValue, propertyValue = '',''
                            #Determine if property required
                            if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                    #Get the property reporting value
                                    propertyValue = round(dictNeLD[0.05][1],4)
                                else:
                                    propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                            else:
                                    propertySuppressedValue = self.static_stringNotSpecified
                            #Assign property values        
                            dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                            self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

                            '''#>>>>> PROPERTY -Initialize property values'''
                            listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_ld_ne_pcrit_0_05_upr_ci_VSP
                            listPropertyLabelPrefixes = ['', '','','','','']
                            propertySuppressedValue, propertyValue = '',''
                            #Determine if property required
                            if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                    #Get the property reporting value
                                    propertyValue = round(dictNeLD[0.05][2],4)
                                else:
                                    propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                            else:
                                    propertySuppressedValue = self.static_stringNotSpecified
                            #Assign property values        
                            dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                            self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

#                                 dict_ld_ne_pcrit_0_02_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.02_VSP'] = round(dictNeLD[0.02][0],4)
#                                 dict_ld_ne_pcrit_0_02_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.02_lwr_ci_VSP'] = round(dictNeLD[0.02][1],4)
#                                 dict_ld_ne_pcrit_0_02_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.02_upr_ci_VSP'] = round(dictNeLD[0.02][2],4)

                            '''#>>>>> PROPERTY -Initialize property values'''
                            listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_ld_ne_pcrit_0_02_VSP
                            listPropertyLabelPrefixes = ['', '','','','','']
                            propertySuppressedValue, propertyValue = '',''
                            #Determine if property required
                            if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                    #Get the property reporting value
                                    propertyValue = round(dictNeLD[0.02][0],4)
                                else:
                                    propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                            else:
                                    propertySuppressedValue = self.static_stringNotSpecified
                            #Assign property values        
                            dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                            self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

                            '''#>>>>> PROPERTY -Initialize property values'''
                            listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_ld_ne_pcrit_0_02_lwr_ci_VSP
                            listPropertyLabelPrefixes = ['', '','','','','']
                            propertySuppressedValue, propertyValue = '',''
                            #Determine if property required
                            if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                    #Get the property reporting value
                                    propertyValue = round(dictNeLD[0.02][1],4)
                                else:
                                    propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                            else:
                                    propertySuppressedValue = self.static_stringNotSpecified
                            #Assign property values        
                            dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                            self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

                            '''#>>>>> PROPERTY -Initialize property values'''
                            listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_ld_ne_pcrit_0_02_upr_ci_VSP
                            listPropertyLabelPrefixes = ['', '','','','','']
                            propertySuppressedValue, propertyValue = '',''
                            #Determine if property required
                            if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                    #Get the property reporting value
                                    propertyValue = round(dictNeLD[0.02][2],4)
                                else:
                                    propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                            else:
                                    propertySuppressedValue = self.static_stringNotSpecified
                            #Assign property values        
                            dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                            self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty


#                                 dict_ld_ne_pcrit_0_01_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.01_VSP'] = round(dictNeLD[0.01][0],4)
#                                 dict_ld_ne_pcrit_0_01_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.01_lwr_ci_VSP'] = round(dictNeLD[0.01][1],4)
#                                 dict_ld_ne_pcrit_0_01_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.01_upr_ci_VSP'] = round(dictNeLD[0.01][2],4)

                            '''#>>>>> PROPERTY -Initialize property values'''
                            listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_ld_ne_pcrit_0_01_VSP
                            listPropertyLabelPrefixes = ['', '','','','','']
                            propertySuppressedValue, propertyValue = '',''
                            #Determine if property required
                            if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                    #Get the property reporting value
                                    propertyValue = round(dictNeLD[0.01][0],4)
                                else:
                                    propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                            else:
                                    propertySuppressedValue = self.static_stringNotSpecified
                            #Assign property values        
                            dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                            self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

                            '''#>>>>> PROPERTY -Initialize property values'''
                            listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_ld_ne_pcrit_0_01_lwr_ci_VSP
                            listPropertyLabelPrefixes = ['', '','','','','']
                            propertySuppressedValue, propertyValue = '',''
                            #Determine if property required
                            if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                    #Get the property reporting value
                                    propertyValue = round(dictNeLD[0.01][1],4)
                                else:
                                    propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                            else:
                                    propertySuppressedValue = self.static_stringNotSpecified
                            #Assign property values        
                            dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                            self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

                            '''#>>>>> PROPERTY -Initialize property values'''
                            listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_ld_ne_pcrit_0_01_upr_ci_VSP
                            listPropertyLabelPrefixes = ['', '','','','','']
                            propertySuppressedValue, propertyValue = '',''
                            #Determine if property required
                            if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                    #Get the property reporting value
                                    propertyValue = round(dictNeLD[0.01][2],4)
                                else:
                                    propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                            else:
                                    propertySuppressedValue = self.static_stringNotSpecified
                            #Assign property values        
                            dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                            self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

#                            else:
#                                #Output has been suppressed
#                                 dict_ld_ne_pcrit_0_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0_VSP'] = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
#                                 dict_ld_ne_pcrit_0_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0_lwr_ci_VSP'] = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
#                                 dict_ld_ne_pcrit_0_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0_upr_ci_VSP'] = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
#                                 dict_ld_ne_pcrit_0_05_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.05_VSP'] = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
#                                 dict_ld_ne_pcrit_0_05_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.05_lwr_ci_VSP'] = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
#                                 dict_ld_ne_pcrit_0_05_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.05_upr_ci_VSP'] = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
#                                 dict_ld_ne_pcrit_0_02_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.02_VSP'] = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
#                                 dict_ld_ne_pcrit_0_02_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.02_lwr_ci_VSP'] = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
#                                 dict_ld_ne_pcrit_0_02_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.02_upr_ci_VSP'] = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
#                                 dict_ld_ne_pcrit_0_01_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.01_VSP'] = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
#                                 dict_ld_ne_pcrit_0_01_lwr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.01_lwr_ci_VSP'] = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
#                                 dict_ld_ne_pcrit_0_01_upr_ci_VSP[self.listSingleVirtualSubPop]['ld_ne_pcrit_0.01_upr_ci_VSP'] = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
#                                pass
                            

                        '''#>>>>> PROPERTY -Initialize property values'''
                        listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Loci_Allele_Totals_Per_Locus_List_VSP
                        propertySuppressedValue, propertyValue = '',''
                        #Determine if property required
                        if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                            if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                #Get the property reporting value

                                #Construct dict of Allele totals per locus
                                dictAlleleTotalPerLocus = objSSAnalysisOperation.method_Statistics_On_Allele_TotalPerLocus_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                                #Write dict of Allele Totals Per Locus
                                dict_AlleleTotalPerLocus_VSP[self.listSingleVirtualSubPop]['Loci_Allele_Totals_Per_Locus_List_VSP'] = dictAlleleTotalPerLocus

                                propertyValue = dict_AlleleTotalPerLocus_VSP
                            else:
                                propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                        else:
                                propertySuppressedValue = self.static_stringNotSpecified
                        #Assign property values        
                        dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                        self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

#                         #Construct dict of Allele instance count per locus
#                         dictAlleleInstanceCountPerLocus = objSSAnalysisOperation.method_Statistics_On_Allele_InstanceCountPerLocus_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
#                         #Write dict of Allele Instance Counts
#                         dict_dictAlleleInstanceCountPerLocus_VSP[self.listSingleVirtualSubPop]['Loci_Allele_Instance_Count_List_VSP'] = dictAlleleInstanceCountPerLocus

                        '''#>>>>> PROPERTY -Initialize property values'''
                        listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Loci_Allele_Instance_Count_List_VSP
                        listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                        propertySuppressedValue, propertyValue = '',''
                        #Determine if property required
                        if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                            if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                #Get the property reporting value

                                #Construct dict of Allele instance count per locus
                                dictAlleleInstanceCountPerLocus = objSSAnalysisOperation.method_Statistics_On_Allele_InstanceCountPerLocus_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                                #Write dict of Allele Instance Counts
                                dict_dictAlleleInstanceCountPerLocus_VSP[self.listSingleVirtualSubPop]['Loci_Allele_Instance_Count_List_VSP'] = dictAlleleInstanceCountPerLocus

                                propertyValue = dict_dictAlleleInstanceCountPerLocus_VSP
                            else:
                                propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                        else:
                                propertySuppressedValue = self.static_stringNotSpecified
                        #Assign property values        
                        dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                        self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

#                         #Get Allele frequencies in list per population per loci per allele
#                         #[Locus#]{Allele#1:Allele#1_Freq,Allele#2:Allele#2_Freq,...Allele#n:Allele#n_Freq}
#                         dictAlleleFreqs = objSSAnalysisOperation.method_Statistics_On_Allele_Frequencies_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
#                         #Write dict of Allele Frequenecies
#                         dict_dictAlleleFreqs_VSP[self.listSingleVirtualSubPop]['Loci_Allele_Frequencies_List_VSP'] = dictAlleleFreqs

                        '''#>>>>> PROPERTY -Initialize property values'''
                        listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Loci_Allele_Frequencies_List_VSP
                        listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                        propertySuppressedValue, propertyValue = '',''
                        #Determine if property required
                        if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                            if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                #Get the property reporting value

                                #Get Allele frequencies in list per population per loci per allele
                                #[Locus#]{Allele#1:Allele#1_Freq,Allele#2:Allele#2_Freq,...Allele#n:Allele#n_Freq}
                                dictAlleleFreqs = objSSAnalysisOperation.method_Statistics_On_Allele_Frequencies_For_VirtualSubPop(self.pop, self.listSingleVirtualSubPop)
                                #Write dict of Allele Frequenecies
                                dict_dictAlleleFreqs_VSP[self.listSingleVirtualSubPop]['Loci_Allele_Frequencies_List_VSP'] = dictAlleleFreqs

                                propertyValue = dict_dictAlleleFreqs_VSP
                            else:
                                propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                        else:
                                propertySuppressedValue = self.static_stringNotSpecified
                        #Assign property values        
                        dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                        self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

                        ''' AgeNe Reporting '''
                        if self.objSSParametersLocal.boolReportSimAgeNe:
                            
                            listSexes = self.objSSParametersLocal.listSexes

                            with SSOutputHandler() as objSSOutputOperation:
                                 
                                listOfAgeNeObjects = self.objSSParametersLocal.listOfAgeNeManualObjects
                                strSex = globalsSS.SexConstants.static_stringSexAll
                                
                                objSSReporting = objSSOutputOperation.method_AgeNe_Final_Totals_Reporting(listOfAgeNeObjects, strSex)
                                
                                strPropertyNamePrefix = globalsSS.ObjectCustom1ReportingPropertyLabels.static_AgeNe_Manual_CalculatedTotals_Label_Prefix1
                                strPropertyLabelPrefix = globalsSS.ObjectCustom1ReportingPropertyLabels.static_AgeNe_Manual_CalculatedTotals_Label_Prefix2
                                for objSSReportingProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                                    strDefaultLabelKey = objSSReportingProperty.Property_Label_Default_Label_Key
                                    strPropertyLabel = strPropertyLabelPrefix + getattr(objSSReportingProperty, strDefaultLabelKey)
                                    setattr(objSSReportingProperty, strDefaultLabelKey, strPropertyLabel)
                                    setattr(objSSReportingProperty, 'Property_Name', strPropertyNamePrefix + objSSReportingProperty.Property_Name)
                                    self.dictReportingPropertyObjects[objSSReportingProperty.Property_Name] = objSSReportingProperty
                                    #self.dictReportingPropertyObjects[strPropertyNamePrefix + objSSReportingProperty.Property_Name] = objSSReportingProperty
                                    pass
                                pass
                                 
                                listOfAgeNeObjects = self.objSSParametersLocal.listOfAgeNeSimObjects
                                strSex = globalsSS.SexConstants.static_stringSexAll
                                 
                                objSSReporting = objSSOutputOperation.method_AgeNe_Final_Totals_Reporting(listOfAgeNeObjects, strSex)
                                 
                                strPropertyNamePrefix = globalsSS.ObjectCustom1ReportingPropertyLabels.static_AgeNe_Sim_CalculatedTotals_Label_Prefix1
                                strPropertyLabelPrefix = globalsSS.ObjectCustom1ReportingPropertyLabels.static_AgeNe_Sim_CalculatedTotals_Label_Prefix2
                                for objSSReportingProperty in objSSReporting.List_Of_Object_Properties_To_Output:
                                    strDefaultLabelKey = objSSReportingProperty.Property_Label_Default_Label_Key
                                    strPropertyLabel = strPropertyLabelPrefix + getattr(objSSReportingProperty, strDefaultLabelKey)
                                    setattr(objSSReportingProperty, strDefaultLabelKey, strPropertyLabel)
                                    setattr(objSSReportingProperty, 'Property_Name', strPropertyNamePrefix + objSSReportingProperty.Property_Name)
                                    self.dictReportingPropertyObjects[objSSReportingProperty.Property_Name] = objSSReportingProperty
                                    pass
                                pass
                            
                                #self.listOfAgeNeObjects = self.listOfAgeNeSimObjects
                            pass
                        pass
                    
                        if boolIncludeParentOffspringProperties:
                            if boolVSPHasIndivs:
                                #Output Mean and Variance of the cumulative number of offspring per each parent for VSP (0,0)
                                #Keep results from VSP (0,0) and display on all subsequent VSPs until next offspring batch is created
                                
                                #if self.listSingleVirtualSubPop == (0,0):
                                    self.listCurrentVSP
                                    with SSAnalysisHandler() as objSSAnalysisOperation:
        
                                        dictSireOffspringCount = objSSAnalysisOperation.method_Count_Offspring_Per_Sire_For_VirtualSubPop_Into_Dict(self.pop, self.intSubPop, self.intVirtualSubPop)
                                        dictDameOffspringCount = objSSAnalysisOperation.method_Count_Offspring_Per_Dame_For_VirtualSubPop_Into_Dict(self.pop, self.intSubPop, self.intVirtualSubPop)
                                        
                                        #intSireCount = len(dictSireOffspringCount[sim.MALE])
                                        #intDameCount = len(dictDameOffspringCount[sim.FEMALE])
        
                                        #intSireCount = 0
                                        #for intID, intOffspringCount in dictSireOffspringCount[sim.MALE].iteritems():
                                        #    if intOffspringCount > 0:
                                        #        intSireCount += 1
        
                                        #WITHOUT DEEPCOPY in this function the passed dict objects will be updated by reference
                                        boolAllow = False
                                        if boolAllow:
                                            if self.boolAtleastTwoSubPops: 
                                                dictOffspringCount = objSSAnalysisOperation.method_Count_Offspring_PerParent_For_VirtualSubPop(self.pop, self.intSubPop, self.intVirtualSubPop, dictSireOffspringCount, dictDameOffspringCount)
                                            else:
                                                dictOffspringCount = {}
                                                
                                            if (len(dictOffspringCount[sim.MALE]) > 0) | (len(dictOffspringCount[sim.FEMALE]) > 0):
                                                with AnalysisHandler() as objAnalysisOperation:
                                                    
                                                    #Construct a list of ACTUAL SIRE offspring counts
                                                    listSireOffspringCount = []
                                                    for i in dictSireOffspringCount[sim.MALE]:
                                                        listSireOffspringCount.append(dictSireOffspringCount[sim.MALE][i])
            
                                                    self.floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listSireOffspringCount)
                                                    self.floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listSireOffspringCount)
                                                    
    #                                                 dict_Num_Sire_Parent[self.listSingleVirtualSubPop]['Num_Sire_Parent'] = len(listSireOffspringCount)
    #                                                 dict_Mean_Offspring_Per_Sire_Parent[self.listSingleVirtualSubPop]['Mean_Offspring_Per_Sire_Parent'] = round(self.floatMean,4)
    #                                                 dict_Mean_Variance_Per_Sire_Parent[self.listSingleVirtualSubPop]['Mean_Variance_Offspring_Per_Sire_Parent'] = round( self.floatVariance,4)
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Num_Sire_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = len(listSireOffspringCount)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Mean_Offspring_Per_Sire_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round(self.floatMean,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Mean_Variance_Offspring_Per_Sire_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round( self.floatVariance,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
            
                                                    #Construct a list of POTENTIAL SIRE offspring counts
                                                    listMaleOffspringCount = []
                                                    for i in dictOffspringCount[sim.MALE]:
                                                        listMaleOffspringCount.append(dictOffspringCount[sim.MALE][i])
            
                                                    self.floatMeanLitterSizeForMaleParents_MeanKsex = objAnalysisOperation.method_Get_Mean_From_A_List(listMaleOffspringCount)
                                                    self.floatMeanVarianceLitterSizeForMaleParents_VarKsex = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listMaleOffspringCount)
                                                    self.integerNumberofParentsForMaleParents_Nsex = len(listMaleOffspringCount)
                                                    self.floatNeDemographicByMaleParentsFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_By_Parental_Sex_Given_Known_Offspring(self.integerNumberofParentsForMaleParents_Nsex, self.floatMeanLitterSizeForMaleParents_MeanKsex, self.floatMeanVarianceLitterSizeForMaleParents_VarKsex)
    
    
    #                                                 dict_Num_Male_Potential_Parent[self.listSingleVirtualSubPop]['Num_Male_Potential_Parent'] = self.integerNumberofParentsForMaleParents_Nsex
    #                                                 dict_Mean_Offspring_Per_Male_Potential_Parent[self.listSingleVirtualSubPop]['Mean_Offspring_Per_Male_Potential_Parent'] = round(self.floatMeanLitterSizeForMaleParents_MeanKsex,4)
    #                                                 dict_Mean_Variance_Per_Male_Potential_Parent[self.listSingleVirtualSubPop]['Mean_Variance_Offspring_Per_Male_Potential_Parent'] = round( self.floatMeanVarianceLitterSizeForMaleParents_VarKsex,4)
    #                                                 dict_Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents[self.listSingleVirtualSubPop]['Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents'] = round( self.floatNeDemographicByMaleParentsFromKnownOffspring,4)
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Num_Male_Potential_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = self.integerNumberofParentsForMaleParents_Nsex
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Mean_Offspring_Per_Male_Potential_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round(self.floatMeanLitterSizeForMaleParents_MeanKsex,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Variance_Offspring_Per_Male_Potential_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round(self.floatMeanLitterSizeForMaleParents_MeanKsex,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Ne_Demographic_From_Known_Offspring_Given_Male_Potential_Parents
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round( self.floatNeDemographicByMaleParentsFromKnownOffspring,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
            
                                                    #Construct a list of ACTUAL DAME offspring counts
                                                    listDameOffspringCount = []
                                                    for i in dictDameOffspringCount[sim.FEMALE]:
                                                        listDameOffspringCount.append(dictDameOffspringCount[sim.FEMALE][i])
            
                                                    self.floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listDameOffspringCount)
                                                    self.floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listDameOffspringCount)
                                                    
    #                                                 dict_Num_Dame_Parent[self.listSingleVirtualSubPop]['Num_Dame_Parent'] = len(listDameOffspringCount)
    #                                                 dict_Mean_Offspring_Per_Dame_Parent[self.listSingleVirtualSubPop]['Mean_Offspring_Per_Dame_Parent'] = round(self.floatMean,4)
    #                                                 dict_Mean_Variance_Per_Dame_Parent[self.listSingleVirtualSubPop]['Mean_Variance_Offspring_Per_Dame_Parent'] = round( self.floatVariance,4)
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Num_Dame_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = len(listDameOffspringCount)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Mean_Offspring_Per_Dame_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round(self.floatMean,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Mean_Variance_Offspring_Per_Dame_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round( self.floatVariance,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
            
                                                    #Construct a list of POTENTIAL DAME offspring counts
                                                    listFemaleOffspringCount = []
                                                    for i in dictOffspringCount[sim.FEMALE]:
                                                        listFemaleOffspringCount.append(dictOffspringCount[sim.FEMALE][i])
                                                    
                                                    self.floatMeanLitterSizeForFemaleParents_MeanKsex = objAnalysisOperation.method_Get_Mean_From_A_List(listFemaleOffspringCount)
                                                    self.floatMeanVarianceLitterSizeForFemaleParents_VarKsex = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listFemaleOffspringCount)
                                                    self.integerNumberofParentsForFemaleParents_Nsex = len(listFemaleOffspringCount)
                                                    self.floatNeDemographicByFemaleParentsFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_By_Parental_Sex_Given_Known_Offspring(self.integerNumberofParentsForFemaleParents_Nsex, self.floatMeanLitterSizeForFemaleParents_MeanKsex, self.floatMeanVarianceLitterSizeForFemaleParents_VarKsex)
                                                    
            
    #                                                 dict_Num_Female_Potential_Parent[self.listSingleVirtualSubPop]['Num_Female_Potential_Parent'] = self.integerNumberofParentsForFemaleParents_Nsex
    #                                                 dict_Mean_Offspring_Per_Female_Potential_Parent[self.listSingleVirtualSubPop]['Mean_Offspring_Per_Female_Potential_Parent'] = round(self.floatMeanLitterSizeForFemaleParents_MeanKsex,4)
    #                                                 dict_Mean_Variance_Per_Female_Potential_Parent[self.listSingleVirtualSubPop]['Mean_Variance_Offspring_Per_Female_Potential_Parent'] = round(self.floatMeanVarianceLitterSizeForFemaleParents_VarKsex,4)
    #                                                 dict_Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents[self.listSingleVirtualSubPop]['Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents'] = round(self.floatNeDemographicByFemaleParentsFromKnownOffspring,4)
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Num_Female_Potential_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = self.integerNumberofParentsForFemaleParents_Nsex
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Mean_Offspring_Per_Female_Potential_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round(self.floatMeanLitterSizeForFemaleParents_MeanKsex,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Variance_Offspring_Per_Female_Potential_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round(self.floatMeanLitterSizeForFemaleParents_MeanKsex,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Ne_Demographic_From_Known_Offspring_Given_Female_Potential_Parents
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round( self.floatNeDemographicByFemaleParentsFromKnownOffspring,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
                                                            
                                                    listActualParentCount = []
                                                    listActualParentCount = listSireOffspringCount + listDameOffspringCount
            
                                                    self.floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listActualParentCount)
                                                    self.floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listActualParentCount)
            
    #                                                 dict_Num_Actual_Parent[self.listSingleVirtualSubPop]['Num_Actual_Parent'] = len(listActualParentCount)
    #                                                 dict_Mean_Offspring_Per_Actual_Parent[self.listSingleVirtualSubPop]['Mean_Offspring_Per_Actual_Parent'] = round(self.floatMean,4)
    #                                                 dict_Mean_Variance_Per_Actual_Parent[self.listSingleVirtualSubPop]['Mean_Variance_Offspring_Per_Actual_Parent'] = round( self.floatVariance,4)
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Num_Actual_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = len(listActualParentCount)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Mean_Offspring_Per_Actual_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round(self.floatMean,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Mean_Variance_Offspring_Per_Actual_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round( self.floatVariance,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
            
            
                                                    listBothSexesOffspringCount = []
                                                    for intCount in listMaleOffspringCount:
                                                        listBothSexesOffspringCount.append(intCount)
                                                    for intCount in listFemaleOffspringCount:
                                                        listBothSexesOffspringCount.append(intCount)
            
                                                    self.floatMean = objAnalysisOperation.method_Get_Mean_From_A_List(listBothSexesOffspringCount)
                                                    self.floatVariance = objAnalysisOperation.method_Get_Sample_Variance_From_A_List(listBothSexesOffspringCount)
                                                    self.integerNumberofParentsForBothSexesParents_Nsex = len(listBothSexesOffspringCount)
                                                    self.floatNeDemographicGivenBothSexesNeFromKnownOffspring = objAnalysisOperation.method_Get_Demographic_Ne_From_Known_Offspring_Given_Parental_Sex_Ne(self.floatNeDemographicByMaleParentsFromKnownOffspring, self.floatNeDemographicByFemaleParentsFromKnownOffspring)
              
    #                                                 dict_Num_Potential_Parent[self.listSingleVirtualSubPop]['Num_Potential_Parent'] = self.integerNumberofParentsForBothSexesParents_Nsex
    #                                                 dict_Mean_Offspring_Per_Potential_Parent[self.listSingleVirtualSubPop]['Mean_Offspring_Per_Potential_Parent'] = round(self.floatMean,4)
    #                                                 dict_Mean_Variance_Per_Potential_Parent[self.listSingleVirtualSubPop]['Mean_Variance_Offspring_Per_Potential_Parent'] = round( self.floatVariance,4)
    #                                                 dict_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne[self.listSingleVirtualSubPop]['Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne'] = round( self.floatNeDemographicGivenBothSexesNeFromKnownOffspring,4)
    #                                                 dict_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents[self.listSingleVirtualSubPop]['Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents'] = round((self.floatNeDemographicGivenBothSexesNeFromKnownOffspring / self.integerNumberofParentsForBothSexesParents_Nsex),4)
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Num_Actual_Potential_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = self.integerNumberofParentsForBothSexesParents_Nsex
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Mean_Offspring_Per_Actual_Potential_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round(self.floatMean,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Variance_Offspring_Per_Actual_Potential_Parent
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round( self.floatVariance,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Ne_Demographic_From_Known_Offspring_Given_Actual_Potential_Parents
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round( self.floatNeDemographicGivenBothSexesNeFromKnownOffspring,4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty
    
                                                    '''#>>>>> PROPERTY -Initialize property values'''
                                                    listPropertyLabels = globalsSS.ObjectCustom1ReportingPropertyLabels.static_listProperties_Ne_Demographic_From_Known_Offspring_Given_Both_Sexes_Potential_Parents_Ne_Rato_Nc_Potential_Parents
                                                    listPropertyLabelPrefixes = [str(self.listSingleVirtualSubPop) + ' ', str(self.listSingleVirtualSubPop) + ' ','','','','']
                                                    propertySuppressedValue, propertyValue = '',''
                                                    #Determine if property required
                                                    if listPropertyLabels[0] in self.dictPropertiesNotSuppressed:
                                                        if self.dictPropertiesNotSuppressed[listPropertyLabels[0]] == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                                            #Get the property reporting value
                                                            propertyValue = round((self.floatNeDemographicGivenBothSexesNeFromKnownOffspring / self.integerNumberofParentsForBothSexesParents_Nsex),4)
                                                        else:
                                                            propertySuppressedValue = globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed
                                                    else:
                                                            propertySuppressedValue = self.static_stringNotSpecified
                                                    #Assign property values        
                                                    dictProperty = self.AssignReportingPropertyObjectValues(listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue)
                                                    self.dictReportingPropertyObjects[listPropertyLabels[0]] = dictProperty

                pass

            def AssignPropertyValues(self, listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue):
                
                
                dictProperty = AutoVivificationHandler()

                #Initialse property values
                stringPropertyName = listPropertyLabelPrefixes[0] + listPropertyLabels[0]
                stringPropertyLabelLong = listPropertyLabelPrefixes[1] + listPropertyLabels[1]
                stringPropertyLabelShort = listPropertyLabelPrefixes[2] + listPropertyLabels[2]
                stringPropertyLabelAbreviation = listPropertyLabelPrefixes[3] + listPropertyLabels[3]
                stringPropertyLabelUnits = listPropertyLabelPrefixes[4] + listPropertyLabels[4]
                stringPropertyLabelDefaultLabelNum = listPropertyLabelPrefixes[5] + listPropertyLabels[5]

                #Assign property values        
                with object_SSPropertyHandler() as objSSPropertyOperation:
                    dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Name] = stringPropertyName
                    dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Long] = stringPropertyLabelLong
                    dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Short] = stringPropertyLabelShort
                    dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Abreviation] = stringPropertyLabelAbreviation
                    dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Units] = stringPropertyLabelUnits
                    dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Label_Default_Label_Key] = stringPropertyLabelDefaultLabelNum 
                    dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Value_Suppressed] = propertySuppressedValue
                    if propertySuppressedValue != '':
                        dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Value] = propertySuppressedValue
                    else:
                        dictProperty[objSSPropertyOperation.static_stringDictProperty_Key_Property_Value] = propertyValue
                
                return dictProperty

            def AssignReportingPropertyObjectValues(self, listPropertyLabels, listPropertyLabelPrefixes, propertySuppressedValue, propertyValue):
                
                objSSReportingProperty = object_SSReportingProperty()

                #Initialse property values
                stringPropertyName = listPropertyLabelPrefixes[0] + listPropertyLabels[0]
                stringPropertyLabelLong = listPropertyLabelPrefixes[1] + listPropertyLabels[1]
                stringPropertyLabelShort = listPropertyLabelPrefixes[2] + listPropertyLabels[2]
                stringPropertyLabelAbreviation = listPropertyLabelPrefixes[3] + listPropertyLabels[3]
                stringPropertyLabelUnits = listPropertyLabelPrefixes[4] + listPropertyLabels[4]
                stringPropertyLabelDefaultLabelNum = listPropertyLabelPrefixes[5] + listPropertyLabels[5]

                #Assign property values        
                objSSReportingProperty.Property_Name = stringPropertyName
                objSSReportingProperty.Property_Label_Long = stringPropertyLabelLong
                objSSReportingProperty.Property_Label_Short = stringPropertyLabelShort
                objSSReportingProperty.Property_Label_Abreviation = stringPropertyLabelAbreviation
                objSSReportingProperty.Property_Label_Units = stringPropertyLabelUnits
                objSSReportingProperty.Property_Label_Default_Label_Key = stringPropertyLabelDefaultLabelNum 
                objSSReportingProperty.Property_Value_Suppressed = propertySuppressedValue
                if propertySuppressedValue != '':
                    objSSReportingProperty.Property_Value = propertySuppressedValue
                else:
                    objSSReportingProperty.Property_Value = propertyValue
                
                return objSSReportingProperty
               
# -------------- Class specific routines

            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.class_obj_SSReportingCustom_1 = obj_SSReportingCustom_1() 
        return self.class_obj_SSReportingCustom_1
 
    def __exit__(self, type, value, traceback): 
        self.class_obj_SSReportingCustom_1.classCleanUp()