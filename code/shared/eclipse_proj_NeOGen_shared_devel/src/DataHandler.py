#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import dcb_general_resource modules
from ErrorHandler import ErrorHandler
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
# import os
# import sys
# import re

class DataHandler:
    """Handle all general Data operations"""
    def __enter__(self):
         
        class DataOperation: 
            """Explicitly control all fundamental Data operations"""
            
            gstringModuleName="DataHandler.py"
            gstringClassName="DataOperation"

            '''Class-specific properties'''
            
            propertyString_ErrorOriginModule = ''
            propertyString_ErrorOriginClass = ''
            propertyString_ErrorMessage = ''
            
# ----- General routines
    
            def method_ParseCSVLineIntoList(self, line):
            
                
            
            
# -------------- Class specific routines
                        
            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.DataOperation_obj = DataOperation() 
        return self.DataOperation_obj
 
    def __exit__(self, type, value, traceback): 
        self.DataOperation_obj.classCleanUp()
