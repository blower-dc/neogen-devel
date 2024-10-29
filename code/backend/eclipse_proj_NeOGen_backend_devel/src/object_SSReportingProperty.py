#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
#from globals_SharkSim import globalsSS
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules

gstringModuleName='object_SSReportingProperty.py'
gstringClassName='object_SSReportingProperty'

class object_SSReportingProperty:
    """Handle SS Reporting Property Operations"""

# -------------- Class specific routines

    __slots__ = (
                 #PROPERTIES
                'Property_Name'
                ,'Property_Label_Long'
                ,'Property_Label_Short'
                ,'Property_Label_Abreviation'
                ,'Property_Label_Units'
                ,'Property_Label_Default_Label_Key'
                ,'Property_Value_Suppressed'
                ,'Property_Value'
                #VARIABLES
                #CONSTANTS
                'static_stringProperty_Name'
                ,'static_stringProperty_Label_Long'
                ,'static_stringProperty_Label_Short'
                ,'static_stringProperty_Label_Abreviation'
                ,'static_stringProperty_Label_Units'
                ,'static_stringProperty_Label_Default_Label_Key'
                ,'static_stringProperty_Value_Suppressed'
                )

    static_stringProperty_Name = 'Property_Name'
    static_stringProperty_Label_Long = 'Property_Label_Long'
    static_stringProperty_Label_Short = 'Property_Label_Short'
    static_stringProperty_Label_Abreviation = 'Property_Label_Abreviation'
    static_stringProperty_Label_Units = 'Property_Label_Units'
    static_stringProperty_Label_Default_Label_Key = 'Property_Label_Default_Label_Key'
    static_stringProperty_Value_Suppressed = 'Property_Value_Suppressed'
    
    def __init__(self):
        
        self.Property_Name = 'Property_Name'
        self.Property_Label_Long = 'Property_Label_Long'
        self.Property_Label_Short = 'Property_Label_Short'
        self.Property_Label_Abreviation = 'Property_Label_Abreviation'
        self.Property_Label_Units = 'Property_Label_Units'
        self.Property_Label_Default_Label_Key = 'Property_Label_Default_Label_Key'
        self.Property_Value_Suppressed = 'Property_Value_Suppressed'
        self.Property_Value = ''


