#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import dcb_general_resource modules
from ErrorHandler import ErrorHandler
from FileHandler import FileHandler
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
# import os
# import sys
# import re
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import pymysql modules
# import json
# import pymysql

class SSDatabaseHandler:
    """Handle all general database operations"""
    def __enter__(self):
         
        class SSDatabaseOperation: 
            """Explicitly control all GenscapePy database operations"""
            
            gstringModuleName="SSDatabaseHandler.py"
            gstringClassName="SSDatabaseOperation"

            static_stringSQLEndChar = ';'
            static_stringSQLQuote1 = '`'
            static_stringSQLQuote2 = "'"

            static_stringSQLCommit = ' commit;'
            static_stringSQLDefault = 'DEFAULT' #Eg use for key fields with autoincrement
            
            static_stringSQLSelectStart = 'SELECT '
            static_stringSQLSelectMiddle = ' FROM '
            
            static_stringSQLSelectLIMIT = ' LIMIT '
            
            static_stringSQLInsertStart = 'INSERT INTO '
            static_stringSQLInsertMiddle = ' VALUES '

            '''Class-specific properties'''
            
            propertyString_ErrorOriginModule = ''
            propertyString_ErrorOriginClass = ''
            propertyString_ErrorMessage = ''
            
            #property_intCommitEveryNRecords = 0
            
            property_stringSQLDBName = ''
            property_stringSQLTableName = ''
            property_SQLStatementType = ''
            property_stringSQLSelectLIMITRows = 0
            
            property_listFieldNames = []
            
            property_listInsertData = []
            
            property_intSkipFirst_N_CSVRows = 0
            property_intProcessFirst_N_CSVRows = 0
            property_ListCSVColumns =[]
            
            property_intConnection = 0 #Default to the first DB connection object
            
# ----- General routines
            
#             def method_GenerateSQLStatement(self):
#          
#                 stringSQL = ''
#                 stringSQLStart = ''
#                 stringSQLMiddle = ''
#                 
#                 if self.property_SQLStatementType == 'INSERT':
#                     stringSQLStart = self.static_stringSQLInsertStart
#                     stringSQLMiddle = self.static_stringSQLInsertMiddle
#                     stringSQL = stringSQLStart + self.static_stringSQLQuote1 + self.property_stringSQLDBName + self.static_stringSQLQuote1 + '.' + self.static_stringSQLQuote1 + self.property_stringSQLTableName + self.static_stringSQLQuote1 + ' (' 
#                     
#                 stringSQLFieldNames = ''
#                 
#                 intFieldListLength = len(self.property_listFieldNames)
#                 intFieldNameCount = 0
#                 
#                 for stringFieldName in self.property_listFieldNames:
#                     stringSQLFieldNames = stringSQLFieldNames + self.static_stringSQLQuote1 + stringFieldName + self.static_stringSQLQuote1
#                     intFieldNameCount += 1
#                     
#                     if intFieldNameCount < intFieldListLength:
#                         stringSQLFieldNames = stringSQLFieldNames + ','
#                     
#                             
#                     stringSQL = stringSQL + stringSQLFieldNames
#         
#                 stringSQL = stringSQL + ')' + stringSQLMiddle
#                 
#                 return stringSQL

            def method_GenerateSQLSELECTStatementWithWHERE(self):
          
                stringSQL = ''
                stringSQLStart = ''
                stringSQLMiddle = ''
                 
                if self.property_SQLStatementType == 'SELECT':
                    stringSQLStart = self.static_stringSQLSelectStart
                    stringSQLMiddle = self.static_stringSQLSelectMiddle
                    stringSQLDBAndTable = self.static_stringSQLQuote1 + self.property_stringSQLDBName + self.static_stringSQLQuote1 + '.' + self.static_stringSQLQuote1 + self.property_stringSQLTableName + self.static_stringSQLQuote1 
                     
                stringSQLFieldNames = ''
                 
                intFieldListLength = len(self.property_listFieldNames)
                if intFieldListLength == 0:
                    #SELECT * is assumed
                    stringSQLStart = stringSQLStart + "*"
                    stringSQL = stringSQLStart + stringSQLMiddle + stringSQLDBAndTable
                else:    
                    intFieldNameCount = 0
                     
                    for stringFieldName in self.property_listFieldNames:
                        stringSQLFieldName = self.static_stringSQLQuote1 + stringFieldName + self.static_stringSQLQuote1
                        intFieldNameCount += 1
                         
                        if intFieldNameCount < intFieldListLength:
                            stringSQLFieldNames = stringSQLFieldNames + stringSQLFieldName + ','
                                 
                        stringSQL = stringSQL + stringSQLFieldNames
             
                    stringSQL = stringSQLStart + stringSQLFieldNames + stringSQLMiddle + stringSQLDBAndTable
                    
                if self.property_stringSQLSelectLIMITRows > 0:
                    stringSQL = stringSQL + self.static_stringSQLSelectLIMIT + str(self.property_stringSQLSelectLIMITRows)
                
                #Add final semi-colon
                stringSQL = stringSQL + self.static_stringSQLEndChar
                     
                return stringSQL

            def method_GenerateSQLSELECTStatementForFieldNamesInitilization(self):
          
                stringSQL = ''
                stringSQLStart = ''
                stringSQLMiddle = ''
                 
                if self.property_SQLStatementType == 'SELECT':
                    stringSQLStart = self.static_stringSQLSelectStart
                    stringSQLMiddle = self.static_stringSQLSelectMiddle
                    stringSQLDBAndTable = self.static_stringSQLQuote1 + self.property_stringSQLDBName + self.static_stringSQLQuote1 + '.' + self.static_stringSQLQuote1 + self.property_stringSQLTableName + self.static_stringSQLQuote1 
                     
#                stringSQLFieldNames = ''
                 
                    #SELECT * is assumed
                    stringSQLStart = stringSQLStart + "*"
                    stringSQL = stringSQLStart + stringSQLMiddle + stringSQLDBAndTable
                
                    stringSQL = stringSQL + self.static_stringSQLSelectLIMIT + str(self.property_stringSQLSelectLIMITRows)
                
                #Add final semi-colon
                stringSQL = stringSQL + self.static_stringSQLEndChar
                     
                return stringSQL

            def method_GenerateSQLInsertStatementFieldsPrefix(self):
         
                stringSQL = ''
                stringSQLStart = ''
                stringSQLMiddle = ''
                
                if self.property_SQLStatementType == 'INSERT':
                    stringSQLStart = self.static_stringSQLInsertStart
                    stringSQLMiddle = self.static_stringSQLInsertMiddle
                    stringSQL = stringSQLStart + self.static_stringSQLQuote1 + self.property_stringSQLDBName + self.static_stringSQLQuote1 + '.' + self.static_stringSQLQuote1 + self.property_stringSQLTableName + self.static_stringSQLQuote1 + ' (' 
                    
                stringSQLFieldName = ''
                
                intFieldListLength = len(self.property_listFieldNames)
                intFieldNameCount = 0
                
                for stringFieldName in self.property_listFieldNames:
                    stringSQLFieldName = self.static_stringSQLQuote1 + stringFieldName + self.static_stringSQLQuote1
                    intFieldNameCount += 1
                    
                    if intFieldNameCount < intFieldListLength:
                        stringSQLFieldName = stringSQLFieldName + ','
                    
                            
                    stringSQL = stringSQL + stringSQLFieldName
        
                stringSQL = stringSQL + ')' + stringSQLMiddle
                
                return stringSQL

            def method_GenerateSQLInsertStatementAddDataSuffixFromList(self, stringSQL, boolAddCommit):
                
                intDataFieldCount = 0
                
                #We assume any tables first field is the primary key with autoincrement turned on
                #That means the very first data element must be "DEFAULT,"  
                #stringSQLDataFields = self.static_stringSQLDefault + ','
                stringSQLDataFields = ''
                
                intDataFieldListLength = len(self.property_listInsertData)
                
                for stringDataField in self.property_listInsertData:
                    stringSQLDataField = self.static_stringSQLQuote2 + stringDataField + self.static_stringSQLQuote2
                
                    intDataFieldCount += 1
                    
                    if intDataFieldCount < intDataFieldListLength:
                        stringSQLDataField = stringSQLDataField + ','
                        
                    stringSQLDataFields = stringSQLDataFields + stringSQLDataField
        
                stringSQL = stringSQL + '(' + stringSQLDataFields + ')' 
                
                #Add final semi-colon
                stringSQL = stringSQL + self.static_stringSQLEndChar
                
                if boolAddCommit:
                    stringSQL = stringSQL + self.static_stringSQLCommit
                
                return stringSQL
            
            def method_GenerateSQLInsertStatementAddDataSuffixFromGenerator(self, stringSQL, generatorLines):
                
                intDataFieldCount = 0
                
                stringSQLDataFields = '('
                
                for line in generatorLines:
                    stringSQLDataFields = stringSQLDataFields + self.static_stringSQLQuote2 + line + self.static_stringSQLQuote2
                
                    intDataFieldCount += 1
                    
                    intDataFieldListLength = None
                    if intDataFieldCount < intDataFieldListLength:
                        stringSQLDataFields = stringSQLDataFields + ','
                        
                stringSQLData = stringSQLDataFields + ')'
                
                stringSQL = stringSQL + stringSQLData
                
                return stringSQL
            
            
# -------------- Class specific routines
                        
            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.SSDatabaseOperation_obj = SSDatabaseOperation() 
        return self.SSDatabaseOperation_obj
 
    def __exit__(self, type, value, traceback): 
        self.SSDatabaseOperation_obj.classCleanUp()
