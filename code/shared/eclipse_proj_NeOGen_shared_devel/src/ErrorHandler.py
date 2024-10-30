#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
#from pprint import pprint
import pprint
import datetime

class ErrorHandler:
    '''Handle errors'''
    def __enter__(self):

        class ErrorOperation:

            gstringFile="ErrorHandler.py"
            gstringClassName="ErrorOperation"
            

            '''Class-specific properties'''
            
            propertyString_ErrorOriginModule = ''
            propertyString_ErrorOriginClass = ''
            propertyString_ErrorMessage = ''
            
            def methodConstructErrorMessageWithDetail(self):

                #Construct a meaningful error message with properties provided

                dateTime = datetime.datetime.now()

                stringErrorMessageWithDetail = '>'
                stringErrorMessageWithDetail = stringErrorMessageWithDetail + dateTime.strftime("%Y-%m-%d %H:%M")
                stringErrorMessageWithDetail = stringErrorMessageWithDetail + '>Error'
                stringErrorMessageWithDetail = stringErrorMessageWithDetail + '>OriginModule:' + self.propertyString_ErrorOriginModule
                stringErrorMessageWithDetail = stringErrorMessageWithDetail + '>ClassName:' + self.propertyString_ErrorOriginClass
                stringErrorMessageWithDetail = stringErrorMessageWithDetail + '>Message:' + self.propertyString_ErrorMessage
                stringErrorMessageWithDetail = stringErrorMessageWithDetail + '<'

                return stringErrorMessageWithDetail
            
            def outputErrorMessageWithDetail(self, listOutputDestinations):

                # Output message to the destinations provided
                # "0" - console
                # "1" - standard error log file
                # <fileHandle> - Handle for an open file
                # "<fileName> - Full path and name of the destination file

                return boolSuccessful

            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.errorOperation_obj = ErrorOperation() 
        return self.errorOperation_obj
 
    def __exit__(self, type, value, traceback): 
        self.errorOperation_obj.classCleanUp()