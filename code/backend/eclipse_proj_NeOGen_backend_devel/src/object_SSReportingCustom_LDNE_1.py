#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
#from simuPOP
import simuPOP as sim
from AutoVivificationHandler import AutoVivificationHandler
#from SSOutputHandler import SSOutputHandler
from SSAnalysisHandler import SSAnalysisHandler
from AnalysisHandler import AnalysisHandler
from globals_SharkSim import globalsSS
from object_SSRepProperty import object_SSPropertyHandler
from object_SSReportingProperty import object_SSReportingProperty
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
import re

class object_SSReportingCustom_LDNE_1(object):
    """Contains SS Simulation level properties and methods"""
    def __enter__(self):

        class obj_SSReportingCustom_LDNE_1():

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
                self.listLDNeVSPToReport = []
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
                
            def method_PopulateProperties(self):

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

                with SSAnalysisHandler() as objSSAnalysisOperation:
                    #LD Ne - Dict for each PCrit (0.0, 0.05, 0.02, 0.01) listing NE, lower CI, upper CI    
                    #dictNeLD = objSSAnalysisOperation.method_Statistics_On_NE_LD_Population_Size_For_VirtualSubPop(self.pop, [0])
                    dictNeLD = objSSAnalysisOperation.method_Statistics_On_NE_LD_Population_Size_For_VirtualSubPop(self.pop, self.listVirtSubPopsToOutput)
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

        self.class_obj_SSReportingCustom_LDNE_1 = obj_SSReportingCustom_LDNE_1() 
        return self.class_obj_SSReportingCustom_LDNE_1
 
    def __exit__(self, type, value, traceback): 
        self.class_obj_SSReportingCustom_LDNE_1.classCleanUp()