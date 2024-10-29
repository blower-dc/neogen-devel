#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
from globals_SharkSim import globalsSS
from object_SSReportingProperty import object_SSReportingProperty
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules

gstringModuleName='object_SSReportingObject.py'
gstringClassName='object_SSReportingObject'

class object_SSReportingObject(object):
    """Handle SS Reporting Property Operations"""

# -------------- Class specific routines

    __slots__ = (
                 #PROPERTIES
                'Dict_Of_Objects_To_Report'
                ,'Dict_Of_Object_Properties_To_Report'
                ,'Ordered_Dict_Of_Object_Properties_To_Report'
                ,'List_Of_Object_Properties_To_Output'
                #VARIABLES
                ,'dictOfObjectsToReport'
                ,'dictOfObjectPropertiesToReport'
                ,'oDictOfObjectPropertiesToReport'
                ,'listOfObjectPropertiesToOutput'
                #CONSTANTS
                )
    
    #CONSTAMT Declarations here
    
    
    def __init__(self):
        
        #PROPERTIES
        self.Dict_Of_Objects_To_Report = {}
        self.Dict_Of_Object_Properties_To_Report = {}
        self.Ordered_Dict_Of_Object_Properties_To_Report = {}
        self.List_Of_Object_Properties_To_Output = {}
        
        #VARIABLES
        self.dictOfObjectsToReport = {}
        self.dictOfObjectPropertiesToReport = {}
        self.oDictOfObjectPropertiesToReport = {}
        self.listOfObjectPropertiesToOutput = []
        
        pass
        
    def method_Initialse(self, dictOfObjectsToReport, dictOfObjectPropertiesToReport, oDictOfObjectPropertiesToReport):
        
        #PROPERTIES <-- ARGS
        self.Dict_Of_Objects_To_Report = dictOfObjectsToReport
        self.Dict_Of_Object_Properties_To_Report = dictOfObjectPropertiesToReport
        self.Ordered_Dict_Of_Object_Properties_To_Report = oDictOfObjectPropertiesToReport
        
        #VARIABLES <-- PROPERTIES
        self.dictOfObjectsToReport = self.Dict_Of_Objects_To_Report 
        self.dictOfObjectPropertiesToReport = self.Dict_Of_Object_Properties_To_Report
        self.oDictOfObjectPropertiesToReport = self.Ordered_Dict_Of_Object_Properties_To_Report
        pass
    
    def method_GetListOfReportingPropertys_From_OrderedDict(self):
        
        #Get the Max Reporting Order Key
        #intLastReportingOrderKey = int(max(self.dictOfObjectPropertiesToReport.iterkeys(), key=(lambda key: self.dictOfObjectPropertiesToReport[key])))
        
        for keyIntReportingOrderKey, valueDictReportingProperties in self.oDictOfObjectPropertiesToReport.items():
        #    dictOfObjectPropertiesToReportByReportingOrder = self.dictOfObjectPropertiesToReport[str(intReportingOrderKey)]
        #for keyObjectName, valueListOfObjectProperties in dictOfObjectPropertiesToReportByReportingOrder.iteritems():
            for keyObjectName, valueListOfObjectProperties in valueDictReportingProperties.iteritems():
                
                objObjectToReport = self.dictOfObjectsToReport[keyObjectName]
                intReportingPropertyCount = 0
                
                for strObjectPropertyName in valueListOfObjectProperties:
                    intReportingPropertyCount += 1
                    #Get property from object by property name
                    propertyValue = getattr(objObjectToReport, strObjectPropertyName, globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyNameNotFound)
                    if propertyValue != globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyNameNotFound:
                        #Create the property object and assign it values
                        objObjectPropertiesToReport = self.method_CreateReportingPropertyObject(intReportingPropertyCount, keyObjectName, strObjectPropertyName, propertyValue)
                    else:
                        #Create an ERROR object as property cannot be found
                        objObjectPropertiesToReport = self.method_MissingReportingPropertyObject(strObjectPropertyName)
                    
                    self.listOfObjectPropertiesToOutput.append(objObjectPropertiesToReport)
                
        self.List_Of_Object_Properties_To_Output = self.listOfObjectPropertiesToOutput
        pass

        
        pass
    
    def method_GetListOfReportingPropertys_From_Dict_RETIRED(self):
        
        #Get the Max Reporting Order Key
        #intLastReportingOrderKey = int(max(self.dictOfObjectPropertiesToReport.iterkeys(), key=(lambda key: self.dictOfObjectPropertiesToReport[key])))
        intLastReportingOrderKey = int(max(self.dictOfObjectPropertiesToReport.keys(), key=int))
        
        for intReportingOrderKey in range(0, intLastReportingOrderKey+1):
            dictOfObjectPropertiesToReportByReportingOrder = self.dictOfObjectPropertiesToReport[str(intReportingOrderKey)]
            for keyObjectName, valueListOfObjectProperties in dictOfObjectPropertiesToReportByReportingOrder.iteritems():
                for keyObjectName, valueListOfObjectProperties in dictOfObjectPropertiesToReportByReportingOrder.iteritems():
                    
                    objObjectToReport = self.dictOfObjectsToReport[keyObjectName]
                    intReportingPropertyCount = 0
                    
                    for strObjectPropertyName in valueListOfObjectProperties:
                        intReportingPropertyCount += 1
                        #Get property from object by property name
                        propertyValue = getattr(objObjectToReport, strObjectPropertyName, globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyNameNotFound)
                        if propertyValue != globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyNameNotFound:
                            #Create the property object and assign it values
                            objObjectPropertiesToReport = self.method_CreateReportingPropertyObject(intReportingPropertyCount, keyObjectName, strObjectPropertyName, propertyValue)
                        else:
                            #Create an ERROR object as property cannot be found
                            objObjectPropertiesToReport = self.method_MissingReportingPropertyObject(strObjectPropertyName)
                        
                        self.listOfObjectPropertiesToOutput.append(objObjectPropertiesToReport)
                
        self.List_Of_Object_Properties_To_Output = self.listOfObjectPropertiesToOutput
        pass

        
        pass

    def method_GetListOfReportingPropertys_From_Dict(self):
        
        #Get the Max Reporting Order Key
        #intLastReportingOrderKey = int(max(self.dictOfObjectPropertiesToReport.iterkeys(), key=(lambda key: self.dictOfObjectPropertiesToReport[key])))
        intLastReportingOrderKey = int(max(self.dictOfObjectPropertiesToReport.keys(), key=int))
        
        for intReportingOrderKey in range(0, intLastReportingOrderKey+1):
            dictOfObjectPropertiesToReportByReportingOrder = self.dictOfObjectPropertiesToReport[str(intReportingOrderKey)]
            for keyObjectName, valueListOfObjectProperties in dictOfObjectPropertiesToReportByReportingOrder.iteritems():
                for keyObjectName, valueListOfObjectProperties in dictOfObjectPropertiesToReportByReportingOrder.iteritems():
                    
                    objObjectToReport = self.dictOfObjectsToReport[keyObjectName]
                    intReportingPropertyCount = 0
                    
                    for strObjectPropertyName in valueListOfObjectProperties:
                        intReportingPropertyCount += 1
                        #Get property from object by property name
                        propertyValue = getattr(objObjectToReport, strObjectPropertyName, globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyNameNotFound)
                        if propertyValue != globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyNameNotFound:
                            strPropertyNotSuppressed = objObjectToReport.dictPropertiesNotSuppressed[strObjectPropertyName]
                            if strPropertyNotSuppressed == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                                #Create the property object and assign it values
                                objObjectPropertiesToReport = self.method_CreateReportingPropertyObject(intReportingPropertyCount, keyObjectName, strObjectPropertyName, propertyValue)
                            else:
                                #Create an ERROR object as property cannot be found
                                objObjectPropertiesToReport = self.method_MissingReportingPropertyObject(strObjectPropertyName, strPropertyNotSuppressed)
                        
#                         if strPropertyNotSuppressed == globalsSS.ILFOutputSuppressionFlags.static_stringNotSuppressed:
                        self.listOfObjectPropertiesToOutput.append(objObjectPropertiesToReport)
                
        self.List_Of_Object_Properties_To_Output = self.listOfObjectPropertiesToOutput
        pass

        
        pass

    def method_GetListOfReportingPropertysFromAProperty(self):
        
        #Get the Max Reporting Order Key
        #intLastReportingOrderKey = int(max(self.dictOfObjectPropertiesToReport.iterkeys(), key=(lambda key: self.dictOfObjectPropertiesToReport[key])))
        
        for keyIntReportingOrderKey, valueDictReportingProperties in self.oDictOfObjectPropertiesToReport.items():
        #    dictOfObjectPropertiesToReportByReportingOrder = self.dictOfObjectPropertiesToReport[str(intReportingOrderKey)]
        #for keyObjectName, valueListOfObjectProperties in dictOfObjectPropertiesToReportByReportingOrder.iteritems():
            for keyObjectName, valueListOfObjectProperties in valueDictReportingProperties.iteritems():
                
                objObjectToReport = self.dictOfObjectsToReport[keyObjectName]
                intReportingPropertyCount = 0
                
                for strObjectPropertyName in valueListOfObjectProperties:
                    intReportingPropertyCount += 1
                    #Get property from object by property name
                    if isinstance(objObjectToReport, dict):
                        propertyValue = objObjectToReport[strObjectPropertyName]
                    else:
                        propertyValue = getattr(objObjectToReport, strObjectPropertyName, globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyNameNotFound)
                    #propertyValue = objObjectToReport
                    if propertyValue != globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyNameNotFound:
                        #Create the property object and assign it values
                        objObjectPropertiesToReport = self.method_CreateReportingPropertyObject(intReportingPropertyCount, keyObjectName, strObjectPropertyName, propertyValue)
                    else:
                        #Create an ERROR object as property cannot be found
                        objObjectPropertiesToReport = self.method_MissingReportingPropertyObject(strObjectPropertyName)
                    
                    self.listOfObjectPropertiesToOutput.append(objObjectPropertiesToReport)
                
        self.List_Of_Object_Properties_To_Output = self.listOfObjectPropertiesToOutput
        pass

        
        pass
            
    def method_GetListOfReportingPropertys_Using_ExistingReportingPropertys(self):
        
        #e.g. dictOfObjectsToReport = {'object1name': 'object1', 'object2name':'object2'}
        
        #e.g. dictOfObjectPropertiesToReport = {'object1': ['property2'], 'object2':['property3']}
        
        #Get the Max Reporting Order Key
        #intLastReportingOrderKey = max(self.dictOfObjectPropertiesToReport.iterkeys(), key=(lambda key: self.dictOfObjectPropertiesToReport[key]))
        intLastReportingOrderKey = int(max(self.dictOfObjectPropertiesToReport.keys(), key=int))
        
        for intReportingOrderKey in range(0, intLastReportingOrderKey+1):
            dictOfObjectPropertiesToReportByReportingOrder = self.dictOfObjectPropertiesToReport[str(intReportingOrderKey)]
            for keyObjectName, valueListOfObjectProperties in dictOfObjectPropertiesToReportByReportingOrder.iteritems():
                
                objObjectToReport = self.dictOfObjectsToReport[keyObjectName]
                for strObjectPropertyName in valueListOfObjectProperties:
                    if strObjectPropertyName in objObjectToReport.dictReportingPropertyObjects:
                        objObjectPropertiesToReport = objObjectToReport.dictReportingPropertyObjects[strObjectPropertyName]
                    else:
#                         strPropertySuppressed = objObjectToReport.dictPropertiesNotSuppressed[strObjectPropertyName]
#                         if strPropertySuppressed == globalsSS.ILFOutputSuppressionFlags.static_stringSuppressed:
#                             #We dont want it
#                             pass
#                         else:
                        #Create an ERROR object to replace missing one
                        objObjectPropertiesToReport = self.method_MissingReportingPropertyObject(strObjectPropertyName)
                    
                    self.listOfObjectPropertiesToOutput.append(objObjectPropertiesToReport)
                
        self.List_Of_Object_Properties_To_Output = self.listOfObjectPropertiesToOutput
        pass

    def method_CreateReportingPropertyObject(self, intReportingPropertyCount, keyObjectName, strObjectPropertyName, propertyValue):
        
        objSSReportingProperty = object_SSReportingProperty()

        '''#>>>>> PROPERTY -Initialize property values'''
        #Get Reporting Property Labels using property name
        
        strObjectPropertyLabelsPropertyName = 'static_' + keyObjectName[3:] + '_listProperties_' + str(intReportingPropertyCount)
        listPropertyLabels = getattr(globalsSS.ObjectReportingPropertyLabels, strObjectPropertyLabelsPropertyName, globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyLabelsNotFound)
        #listPropertyLabels = getattr(globalsSS.ObjectReportingPropertyLabels, strObjectPropertyName, globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyLabelsNotFound)
        listPropertyLabelPrefixes = ['','','','','','']

        #Get the property reporting value
        #propertyValue = strObjectPropertyValue
        propertySuppressedValue = ''
        #Assign property values        
        
        #Initialse property values
        intNumPropertyValues = len(listPropertyLabels)
        stringPropertyName = listPropertyLabelPrefixes[0] + listPropertyLabels[0]
        stringPropertyLabelLong = listPropertyLabelPrefixes[1] + listPropertyLabels[1]
        stringPropertyLabelShort = listPropertyLabelPrefixes[2] + listPropertyLabels[2]
        stringPropertyLabelAbreviation = listPropertyLabelPrefixes[3] + listPropertyLabels[3]
        stringPropertyLabelUnits = listPropertyLabelPrefixes[4] + listPropertyLabels[4]
        stringPropertyLabelDefaultLabelNum = listPropertyLabelPrefixes[5] + listPropertyLabels[5]
        if intNumPropertyValues == 7:
            stringPropertySingleValueDictKey = listPropertyLabels[6]
            
            
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
            #If a 6th Property Label value uxists then the property is a dict with only one value where the 6th label is the dict key
            if intNumPropertyValues == 7:
                objSSReportingProperty.Property_Value = propertyValue[stringPropertySingleValueDictKey]
                                                                       
        return objSSReportingProperty

    def method_CreateReportingPropertyObject_TEST(self, intReportingPropertyCount, keyObjectName, strObjectPropertyName, propertyValue):
        
        objSSReportingProperty = object_SSReportingProperty()

        '''#>>>>> PROPERTY -Initialize property values'''
        #Get Reporting Property Labels using property name
        
        strObjectPropertyLabelsPropertyName = 'static_' + keyObjectName[3:] + '_listProperties_' + str(intReportingPropertyCount)
        listPropertyLabels = getattr(globalsSS.ObjectReportingPropertyLabels, strObjectPropertyLabelsPropertyName, globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyLabelsNotFound)
        #listPropertyLabels = getattr(globalsSS.ObjectReportingPropertyLabels, strObjectPropertyName, globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyLabelsNotFound)
        listPropertyLabelPrefixes = ['','','','','','']

        #Get the property reporting value
        #propertyValue = strObjectPropertyValue
        propertySuppressedValue = ''
        #Assign property values        
        
        #Initialse property values
        intNumPropertyValues = len(listPropertyLabels)
        stringPropertyName = listPropertyLabelPrefixes[0] + listPropertyLabels[0]
        stringPropertyLabelLong = listPropertyLabelPrefixes[1] + listPropertyLabels[1]
        stringPropertyLabelShort = listPropertyLabelPrefixes[2] + listPropertyLabels[2]
        stringPropertyLabelAbreviation = listPropertyLabelPrefixes[3] + listPropertyLabels[3]
        stringPropertyLabelUnits = listPropertyLabelPrefixes[4] + listPropertyLabels[4]
        stringPropertyLabelDefaultLabelNum = listPropertyLabelPrefixes[5] + listPropertyLabels[5]
        if intNumPropertyValues == 7:
            stringPropertySingleValueDictKey = listPropertyLabels[6]
            
            
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
            #If a 6th Property Label value uxists then the property is a dict with only one value where the 6th label is the dict key
            if intNumPropertyValues == 7:
                objSSReportingProperty.Property_Value = propertyValue[stringPropertySingleValueDictKey]
                                                                       
        return objSSReportingProperty

    def method_MissingReportingPropertyObject(self, strObjectPropertyName, stringPropertySuppressedValue='' ):
        
        '''
        Create an ERROR object to replace missing one
        '''
        
        objSSReportingProperty = object_SSReportingProperty()

        #Initialse property values
        stringPropertyName = strObjectPropertyName
        stringPropertyLabelLong = globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyObjectNotFound
        stringPropertyLabelShort = globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyObjectNotFound
        stringPropertyLabelAbreviation = globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyObjectNotFound
        stringPropertyLabelUnits = globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyObjectNotFound
        #Leave this so that the correct label will be displayed
        stringPropertyLabelDefaultLabelNum = objSSReportingProperty.Property_Label_Abreviation
        if stringPropertySuppressedValue == '': 
            stringPropertySuppressedValue = globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyObjectNotFound
        stringPropertyValue = globalsSS.StringUnexpectedResults.static_stringError_ReportingPropertyObjectNotFound
        
        #Assign property values        
        objSSReportingProperty.Property_Name = stringPropertyName
        objSSReportingProperty.Property_Label_Long = stringPropertyLabelLong
        objSSReportingProperty.Property_Label_Short = stringPropertyLabelShort
        objSSReportingProperty.Property_Label_Abreviation = stringPropertyLabelAbreviation
        objSSReportingProperty.Property_Label_Units = stringPropertyLabelUnits
        objSSReportingProperty.Property_Label_Default_Label_Key = stringPropertyLabelDefaultLabelNum 
        objSSReportingProperty.Property_Value_Suppressed = stringPropertySuppressedValue
        objSSReportingProperty.Property_Value = stringPropertyValue
        
        return objSSReportingProperty
    
    def method_Finalise(self):
        
        #self.List_Of_Object_Properties_To_Output = self.listOfObjectPropertiesToOutput
        pass