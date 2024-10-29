#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
#from globals_SharkSim import globalsSS
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules

gstringModuleName='object_SSPropertyHandler.py'
gstringClassName='SSPropertyOperation'

class object_SSPropertyHandler:
    """Handle SS Input Operations"""
    def __enter__(self):

        class SSPropertyOperation:

# -------------- Class specific routines

            __slots__ = (
            'static_stringDictProperty_Key_Property_Name'
            ,'static_stringDictProperty_Key_Property_Label_Long'
            ,'static_stringDictProperty_Key_Property_Label_Short'
            ,'static_stringDictProperty_Key_Property_Label_Abreviation'
            ,'static_stringDictProperty_Key_Property_Label_Units'
            ,'static_stringDictProperty_Key_Property_Label_Default_Label_Key'
            ,'static_stringDictProperty_Key_Property_Value_Suppressed'
            ,'static_stringDictProperty_Key_Property_Value'
                        )

            dictProperty = {}
            static_stringDictProperty_Key_Property_Name = 'Property_Name'
            static_stringDictProperty_Key_Property_Label_Long = 'Property_Label_Long'
            static_stringDictProperty_Key_Property_Label_Short = 'Property_Label_Short'
            static_stringDictProperty_Key_Property_Label_Abreviation = 'Property_Label_Abreviation'
            static_stringDictProperty_Key_Property_Label_Units = 'Property_Label_Units'
            static_stringDictProperty_Key_Property_Label_Default_Label_Key = 'Property_Label_Default_Label_Key'
            static_stringDictProperty_Key_Property_Value_Suppressed = 'Property_Value_Suppressed'
            static_stringDictProperty_Key_Property_Value = 'Property_Value'

            def __init__(self):
                
                #Need GET and SET for this object to work
                self.dictProperty = {
                                self.static_stringDictProperty_Key_Property_Name
                                ,self.static_stringDictProperty_Key_Property_Label_Long
                                ,self.static_stringDictProperty_Key_Property_Label_Short
                                ,self.static_stringDictProperty_Key_Property_Label_Abreviation
                                ,self.static_stringDictProperty_Key_Property_Label_Units
                                ,self.static_stringDictProperty_Key_Property_Value_Suppressed
                                ,self.static_stringDictProperty_Key_Property_Value
                                }


            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.SSPropertyOperation_obj = SSPropertyOperation() 
        return self.SSPropertyOperation_obj
 
    def __exit__(self, type, value, traceback): 
        self.SSPropertyOperation_obj.classCleanUp()