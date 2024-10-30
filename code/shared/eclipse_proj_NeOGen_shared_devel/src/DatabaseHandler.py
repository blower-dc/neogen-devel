#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import dcb_general_resource modules
from ErrorHandler import ErrorHandler
from FileHandler import FileHandler
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
import os
import sys
import re
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import pymysql modules
import json
import pymysql

class DatabaseHandler:
    """Handle all general database operations"""
    def __enter__(self):
         
        class DatabaseOperation: 
            """Explicitly control all fundamental database operations"""
            
            gstringModuleName="DatabaseHandler.py"
            gstringClassName="DatabaseOperation"

            '''Class-specific properties'''
            
            propertyString_ErrorOriginModule = ''
            propertyString_ErrorOriginClass = ''
            propertyString_ErrorMessage = ''
            
# ----- General routines
            def method_DBGetJSONDatabaseInfo(self):
                
                boolSuccessful = False
                
                stringInputFilename = os.path.join(os.path.dirname(__file__), "databases.json")
                
                with FileHandler() as objectFileHandler:
                    boolFileExists = objectFileHandler.fileExists(stringInputFilename)
                    if boolFileExists:
                        fileHandle = objectFileHandler.fileOpen(stringInputFilename, 'read')
                    else:
                        # stringFileOpenModeVerbose contains an invalid value
                        boolContinue = False
                        with ErrorHandler() as objectErrorOperation:
                            objectErrorOperation.propertyString_ErrorOriginModule= self.gstringModuleName
                            objectErrorOperation.propertyString_ErrorOriginClass= self.gstringClassName
                            objectErrorOperation.propertyString_ErrorMessage= 'Database info file not found: ' + stringInputFilename
                            stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                        return

                    #objInput=fileHandle
                    
                    #self.databases = json.load(fileHandle)
                    
                    try:       
                        self.databases = json.load(fileHandle)
                        boolSuccessful = True

                    except IOError:
                        with ErrorHandler() as objectErrorOperation:
                            objectErrorOperation.propertyString_ErrorOriginModule= self.gstringModuleName
                            objectErrorOperation.propertyString_ErrorOriginClass= self.gstringClassName
                            objectErrorOperation.propertyString_ErrorMessage= 'Databases could not be loaded from JSON file: ' + stringInputFilename
                            stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                        raise IOError(stringErrorMessageWithDetail)
                    
                return boolSuccessful  
           
            def method_DBOpenConections(self):
                
                '''Opens all the DBs specified by the .json file
                   & and adds them to a list of connections '''
                
                self.connections = []
                for params in self.databases:
                    self.connections.append(pymysql.connect(**params))    
  
                pass
 
            def method_DBCloseConection(self):
                
                '''Closes all connection objects in the connections list '''
                
                for connection in self.connections:
                    connection.close()
                    
                pass
           
           
            def method_DBSQLSELECTOperation(self, intConnection, stringSQL):
                
                '''Executes an SQL SELECT command against the connection object
                specified by the list index & returns a cursor object holding
                the results '''
                
                boolSuccessful = False
                dbCursor = None
                    
                #Try to obtain cursor for specified connection object    
                try:       
                    dbCursor = self.connections[intConnection].cursor()
                    boolSuccessful = True
                #Except if index is invalid for connections list
                except IndexError as e:
                    with ErrorHandler() as objectErrorOperation:
                        objectErrorOperation.propertyString_ErrorOriginModule= self.gstringModuleName
                        objectErrorOperation.propertyString_ErrorOriginClass= self.gstringClassName
                        objectErrorOperation.propertyString_ErrorMessage= 'Index for connection:' +  str(intConnection) + ' was invalid for list of connections when using command: ' + stringSQL
                        stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                        print (stringErrorMessageWithDetail)
                    raise  
                #Except if cursor cant be obtained for some reason
                except pymysql.err.Error as e:
                    with ErrorHandler() as objectErrorOperation:
                        objectErrorOperation.propertyString_ErrorOriginModule= self.gstringModuleName
                        objectErrorOperation.propertyString_ErrorOriginClass= self.gstringClassName
                        objectErrorOperation.propertyString_ErrorMessage= 'Cursor for connection:' +  str(intConnection) + ' could not be obtained for command: ' + stringSQL
                        stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                        print (stringErrorMessageWithDetail)
                    raise
    
                #If cursor obtained, try to execute SQL statement and return results in a cursor object
                if boolSuccessful:
                    try:       
                        dbCursor.execute(stringSQL)
                        boolSuccessful = True
                    #Except if something is wrong with the SQL statement
                    except pymysql.err.Error as e:
                        with ErrorHandler() as objectErrorOperation:
                            objectErrorOperation.propertyString_ErrorOriginModule= self.gstringModuleName
                            objectErrorOperation.propertyString_ErrorOriginClass= self.gstringClassName
                            objectErrorOperation.propertyString_ErrorMessage= 'Database operation on connection:' +  str(intConnection) + ' was unsuccessful with command: ' + stringSQL
                            stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                            print (stringErrorMessageWithDetail)
                        raise
             
                return dbCursor

            def method_DBSQLINSERTOperation(self, intConnection, stringSQL):
                
                '''Executes an SQL INSERY command against the connection object
                specified by the list index & returns a boolean success variable '''
                
                boolSuccessful = False
                dbCursor = None
                    
                #Try to obtain cursor for specified connection object    
                try:       
                    dbCursor = self.connections[intConnection].cursor()
                    boolSuccessful = True
                #Except if index is invalid for connections list
                except IndexError as e:
                    with ErrorHandler() as objectErrorOperation:
                        objectErrorOperation.propertyString_ErrorOriginModule= self.gstringModuleName
                        objectErrorOperation.propertyString_ErrorOriginClass= self.gstringClassName
                        objectErrorOperation.propertyString_ErrorMessage= 'Index for connection:' +  str(intConnection) + ' was invalid for list of connections when using command: ' + stringSQL
                        stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                        print (stringErrorMessageWithDetail)
                    raise  
                #Except if cursor cant be obtained for some reason
                except pymysql.err.Error as e:
                    with ErrorHandler() as objectErrorOperation:
                        objectErrorOperation.propertyString_ErrorOriginModule= self.gstringModuleName
                        objectErrorOperation.propertyString_ErrorOriginClass= self.gstringClassName
                        objectErrorOperation.propertyString_ErrorMessage= 'Cursor for connection:' +  str(intConnection) + ' could not be obtained for command: ' + stringSQL
                        stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                        print (stringErrorMessageWithDetail)
                    raise
    
                #If cursor obtained, try to execute SQL statement and return results in a cursor object
                if boolSuccessful:
                    try:       
                        dbCursor.execute(stringSQL)
                        boolSuccessful = True
                    except pymysql.err.IntegrityError as e:
                        boolSuccessful = False
                    #Except if something is wrong with the SQL statement
                    except pymysql.err.Error as e:
                        with ErrorHandler() as objectErrorOperation:
                            objectErrorOperation.propertyString_ErrorOriginModule= self.gstringModuleName
                            objectErrorOperation.propertyString_ErrorOriginClass= self.gstringClassName
                            objectErrorOperation.propertyString_ErrorMessage= 'Database operation on connection:' +  str(intConnection) + ' was unsuccessful with command: ' + stringSQL
                            stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                            print (stringErrorMessageWithDetail)
                        raise
             
                return boolSuccessful 
                      
            def method_GetFieldDescriptionInfoListForCursor(self, dbCursor, intFieldDescriptionListIndex):
                
                listFieldDescriptionInfo = []
                
                for i in dbCursor.description:
                    try:       
                        listFieldDescriptionInfo.append(i[intFieldDescriptionListIndex])
                        #boolSuccessful = True
                        #Except if index is invalid for list
                    except IndexError as e:
                        with ErrorHandler() as objectErrorOperation:
                            objectErrorOperation.propertyString_ErrorOriginModule= self.gstringModuleName
                            objectErrorOperation.propertyString_ErrorOriginClass= self.gstringClassName
                            objectErrorOperation.propertyString_ErrorMessage= 'Index for fields.description:' +  str(intFieldDescriptionListIndex) + ' was invalid'
                            stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                            print (stringErrorMessageWithDetail)
                        raise  

               
                return listFieldDescriptionInfo
            
            def method_PerformSQLCommitWithCursor(self, dbCursor):
                
                boolSuccessful = False
                
                stringSQL = 'commit;'
                
                try:       
                    dbCursor.execute(stringSQL)
                    boolSuccessful = True
#                 except pymysql.err.IntegrityError as e:
#                     boolSuccessful = False
                #Except if something is wrong with the SQL statement
                except pymysql.err.Error as e:
                    with ErrorHandler() as objectErrorOperation:
                        objectErrorOperation.propertyString_ErrorOriginModule= self.gstringModuleName
                        objectErrorOperation.propertyString_ErrorOriginClass= self.gstringClassName
                        objectErrorOperation.propertyString_ErrorMessage= 'Commit failed'
                        stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                        print (stringErrorMessageWithDetail)
                    raise
         
                return boolSuccessful 
            
            
            
# -------------- Class specific routines
                        
            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.DatabaseOperation_obj = DatabaseOperation() 
        return self.DatabaseOperation_obj
 
    def __exit__(self, type, value, traceback): 
        self.DatabaseOperation_obj.classCleanUp()
