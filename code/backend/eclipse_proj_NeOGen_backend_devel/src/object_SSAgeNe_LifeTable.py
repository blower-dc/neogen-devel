#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
from globals_SharkSim import globalsSS
from AutoVivificationHandler import AutoVivificationHandler 
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
from collections import OrderedDict
from logging import getLogger as logging__getLogger
from collections import Counter as collections__Counter
from handler_Debug import Debug_Location as dcb_Debug_Location

gstringModuleName='object_SSAgeNe_LifeTable.py'
gstringClassName='object_SSAgeNe_LifeTable'

class object_SSAgeNe_LifeTable(object):
    """Handle SS Age Ne Life Table Operations"""

# -------------- Class specific routines

    __slots__ = (
                 #PROPERTIES
                 'Max_Age'
                 ,'Min_Mating_Age'
                 ,'Max_Mating_Age'
                 ,'List_Sexes'
                 ,'Initial_Male_Sex_Ratio'
                 ,'N1_Newborns'
                 ,'N1_Newborns_Per_Sex_Per_Age'
                 ,'Calculated_Totals'
                 ,'sx_Odict_Survival_Rate_Per_Age_x'
                 ,'bx_Odict_Birth_Rate_Per_Age_x'
                 ,'lx_Odict_Fraction_Newborn_Still_Alive_Per_Age_x'
                 ,'bxlx_Odict_Per_Age_x'
                 ,'Nx_Odict_Newborns_Per_Age_x'
                 ,'b_x_Odict_Scaled_Birth_Rate_Per_Age_x'
                 ,'Bx_Per_Age_x'
                 ,'AgexBx_Div_N1_Per_Age_x'
                 ,'Use_Sim_Parameters'
                 #VARIABLES
                 ,'intMinAge'
                 ,'intMinMatingAge'
                 ,'intMaxMatingAge'
                 ,'intMaxAge'
                 ,'intMaxAgeAdjusted'
                 ,'intMaxAgeAdjustedForRange'
                 ,'listSexes'
                 ,'floatInitialMaleSexRatio'
                 ,'dict_floatInitialSexRatio'
                 ,'intN1_intNewborns'
                 ,'intN1_intNewbornsBySex'
                 ,'N1_Odict'
                 ,'odictSexAgeInMonths'
                 ,'odictSexAgeInYears'
                 ,'dictCalcTotals'
                 ,'sx_Odict'
                 ,'bx_Odict'
                 ,'lx_Odict'
                 ,'bxlx_Odict'
                 ,'Nx_Odict'
                 ,'bxNx_Odict'
                 ,'b_x_Odict'
                 ,'Bx_Odict'
                 ,'xBx_Div_N1_Odict'
                 ,'boolUseAgeNeSimParameters'
                 ,'obj_Log_Debug_AgeNe'
                 #CONSTANTS
                 ,'static_stringDictKey_CalcTotals_Nx_N_Adults'
                 ,'static_stringDictKey_CalcTotals_Nx_Nc_Adults'
                 ,'static_stringDictKey_CalcTotals_Nx_All'
                 ,'static_stringDictKey_CalcTotals_bxNx_All'
                 ,'static_stringDictKey_CalcTotals_L_All'
                )
    
    static_stringDictKey_CalcTotals_Nx_N_Adults = 'Nx_N_Adults'
    static_stringDictKey_CalcTotals_Nx_Nc_Adults = 'Nx_Nc_Adults'
    static_stringDictKey_CalcTotals_Nx_All = 'Nx_All'
    static_stringDictKey_CalcTotals_bxNx_All = 'bxNx_Sum_All'  
    static_stringDictKey_CalcTotals_L_All = 'L_All'  
       
    def __init__(self):
        
        #Initialize  PROPERTIES
        self.Max_Age = 0
        self.Min_Mating_Age = 0
        self.List_Sexes = []
        self.N1_Newborns = 0
        self.N1_Newborns_Per_Sex_Per_Age = 0
        self.Calculated_Totals = AutoVivificationHandler()
        self.sx_Odict_Survival_Rate_Per_Age_x = OrderedDict([])
        self.bx_Odict_Birth_Rate_Per_Age_x = OrderedDict([])
        self.lx_Odict_Fraction_Newborn_Still_Alive_Per_Age_x = OrderedDict([])
        self.bxlx_Odict_Per_Age_x = OrderedDict([])
        self.Nx_Odict_Newborns_Per_Age_x = OrderedDict([])
        self.b_x_Odict_Scaled_Birth_Rate_Per_Age_x = OrderedDict([])
        self.Bx_Per_Age_x = OrderedDict([])
        self.Use_Sim_Parameters = False
        
        #Initialize VARIALBLES
        self.intMinAge = 1
        self.intMaxAge = 0
        self.intMinMatingAge = 0
        self.intMaxMatingAge = 0
        self.intMaxAgeAdjusted = 0
        self.intMaxAgeAdjustedForRange = 0
        self.listSexes = []
        self.floatInitialMaleSexRatio = 0
        self.dict_floatInitialSexRatio = OrderedDict([])
        self.intN1_intNewborns = 0
        self.N1_Odict = OrderedDict([])
        self.intN1_intNewbornsBySex = 0
        self.odictSexAgeInMonths = OrderedDict([])
        self.odictSexAgeInYears = OrderedDict([])
        self.dictCalcTotals = AutoVivificationHandler()
        self.sx_Odict = OrderedDict([])
        self.bx_Odict = OrderedDict([])
        self.lx_Odict = OrderedDict([])
        self.bxlx_Odict = OrderedDict([])
        self.Nx_Odict = OrderedDict([])
        self.bxNx_Odict = OrderedDict([])
        self.b_x_Odict = OrderedDict([])
        self.Bx_Odict = OrderedDict([])
        self.xBx_Div_N1_Odict = OrderedDict([])
        self.boolUseAgeNeSimParameters = False
        pass

        ''' Get all the loggers required for monitoring this object '''
        self.method_Initialise_Monitor_Loggers()

        return None         

    def method_Initialise_Monitor_Loggers(self):
        
        ''' 
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get all the loggers required for monitoring this object
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
#         ''' Get Run Display Logger '''
#         self.obj_Log_Run_Display = logging__getLogger(globalsSS.Logger_Run_Display.static_Logger_Name__Run_Display)
#                    
#         ''' Get Default Logger '''
#         self.obj_Log_Default_Display = logging__getLogger(globalsSS.Logger_Default_Display.static_Logger_Name__Default_Display)
# 
#         ''' Get Debug Logger '''
#         self.obj_Log_Debug_Display = logging__getLogger(globalsSS.Logger_Debug_Display.static_Logger_Name__Debug_Display)
# 
#         ''' Get Debug Timer '''
#         #self.obj_Log_Debug_Timing = None
#         #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
#         self.obj_Log_Debug_Timing = logging__getLogger(globalsSS.Logger_Debug_Timing.static_Logger_Name__Debug_Timing)
#         #pass

        ''' Get Debug AgeNe Logger '''
        self.obj_Log_Debug_AgeNe = None
        if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
            self.obj_Log_Debug_AgeNe = logging__getLogger(globalsSS.Logger_Debug_AgeNe.static_Logger_Name__Debug_AgeNe)
        pass
                                
        return True
        
           
    def method_Initialise(self):
         
        #PROPERTIES -> VARIABLES
        self.intMaxAge = self.Max_Age
        self.intMinMatingAge = self.Min_Mating_Age
        self.intMaxMatingAge = self.Max_Mating_Age
        self.listSexes = self.List_Sexes
        self.floatInitialMaleSexRatio = self.Initial_Male_Sex_Ratio
        self.dict_floatInitialSexRatio[globalsSS.SexConstants.static_stringSexMale] = self.floatInitialMaleSexRatio
        self.dict_floatInitialSexRatio[globalsSS.SexConstants.static_stringSexFemale] = 1 - self.floatInitialMaleSexRatio
        self.intN1_intNewborns = self.N1_Newborns
        #self.Calculated_Totals = self.dictCalcTotals 
        self.sx_Odict = self.sx_Odict_Survival_Rate_Per_Age_x
        self.bx_Odict = self.bx_Odict_Birth_Rate_Per_Age_x
        self.boolUseAgeNeSimParameters = self.Use_Sim_Parameters
        if self.boolUseAgeNeSimParameters: 
            self.Nx_Odict = self.Nx_Odict_Newborns_Per_Age_x
            self.b_x_Odict = self.b_x_Odict_Scaled_Birth_Rate_Per_Age_x 
            self.N1_Odict = self.N1_Newborns_Per_Sex_Per_Age
            
            odictCalcAgeValues = OrderedDict([])
            odictCalcAgeValuesInYears = OrderedDict([])
            
            self.intMaxAgeAdjusted = self.intMaxAge
            self.intMaxAgeAdjustedForRange = self.intMaxAge+1
            for stringSex in self.listSexes:
                for intAge in range(1, self.intMaxAgeAdjustedForRange):
                    intAgeInMonths = intAge * 12
                    odictCalcAgeValues[intAge] = intAgeInMonths
                    self.odictSexAgeInMonths[stringSex] = odictCalcAgeValues
                    odictCalcAgeValuesInYears[intAge] = intAge
                    self.odictSexAgeInYears[stringSex] = odictCalcAgeValuesInYears
                pass
            
        else:
            #This is purely for DIPLAY PURPOSES ONLY
            self.N1_Odict = self.N1_Newborns_Per_Sex_Per_Age
            
            odictCalcAgeValues = OrderedDict([])
            odictCalcAgeValuesInYears = OrderedDict([])
            
            self.intMaxAgeAdjusted = self.intMaxAge
            self.intMaxAgeAdjustedForRange = self.intMaxAge+1
            for stringSex in self.listSexes:
                for intAge in range(1, self.intMaxAgeAdjustedForRange):
                    intAgeInMonths = intAge * 12
                    odictCalcAgeValues[intAge] = intAgeInMonths
                    self.odictSexAgeInMonths[stringSex] = odictCalcAgeValues
                    odictCalcAgeValuesInYears[intAge] = intAge
                    self.odictSexAgeInYears[stringSex] = odictCalcAgeValuesInYears
                pass
        
        self.intN1_intNewbornsBySex = self.intN1_intNewborns / len(self.odictSexAgeInMonths)

        self.dictCalcTotals = {
                               globalsSS.SexConstants.static_stringSexMale:
                                   {
                                    self.static_stringDictKey_CalcTotals_Nx_N_Adults: 0
                                    ,self.static_stringDictKey_CalcTotals_Nx_Nc_Adults: 0
                                    ,self.static_stringDictKey_CalcTotals_Nx_All: 0
                                    ,self.static_stringDictKey_CalcTotals_bxNx_All: 0
                                    ,self.static_stringDictKey_CalcTotals_L_All: 0
                                    }
                               ,globalsSS.SexConstants.static_stringSexFemale:
                                    {
                                    self.static_stringDictKey_CalcTotals_Nx_N_Adults: 0
                                    ,self.static_stringDictKey_CalcTotals_Nx_Nc_Adults: 0
                                    ,self.static_stringDictKey_CalcTotals_Nx_All: 0
                                    ,self.static_stringDictKey_CalcTotals_bxNx_All: 0
                                    ,self.static_stringDictKey_CalcTotals_L_All: 0
                                    }
                               }
        
        
        
        pass
    
    def method_Calc_lx_Fraction_Newborn_Still_Alive_Per_Age_x(self):
        
        for stringSex, odictAgeValues in self.sx_Odict.items():
            
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                
                if intAge == self.intMinAge:
                    odictCalcAgeValues[intAge] = 1
                    self.lx_Odict[stringSex] = odictCalcAgeValues
                else:
                    #Perform calculations
                    '''
                    lx = s(x-1)*l(x-1)
                    '''
                    str_Working_Msg = 's(x-1)*l(x-1)'
                    
                    
                    num_lx = self.sx_Odict[stringSex][intAge-1] * self.lx_Odict[stringSex][intAge-1]
                    
                    #Assign calculated values
                    odictCalcAgeValues[intAge] = float(num_lx)
                    self.lx_Odict[stringSex] = odictCalcAgeValues
                    
                    pass
            pass
        
        #self.bxlx_Odict_Per_Age_x = self.bxlx_Odict
        self.lx_Odict_Fraction_Newborn_Still_Alive_Per_Age_x = self.lx_Odict
        self.method_Debug_Logging_Dict_List(False, [self.sx_Odict, self.lx_Odict], ['sx','lx'], str_Working_Msg)
        
        return True

    def method_Calc_bxlx_Per_Age_x(self):
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                'bx.lx'
                '''
                str_Working_Msg = 'bx.lx'
                
                
                num_bxlx = self.bx_Odict[stringSex][intAge] * self.lx_Odict[stringSex][intAge]
                
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_bxlx)
                self.bxlx_Odict[stringSex] = odictCalcAgeValues
                
                pass
            
        self.bxlx_Odict_Per_Age_x = self.bxlx_Odict
        self.method_Debug_Logging_Dict_List(False, [self.bx_Odict, self.lx_Odict, self.bxlx_Odict], ['bx','lx', 'bxlx'], str_Working_Msg)
        
        return True

    def method_Calc_Nx_Newborns_Per_Age_x(self):
        
        intN1 = 0
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            num_Nx_Sum_All = float(0)
            num_Nx_Sum_N_Adults = float(0)
            num_Nx_Sum_Nc_Adults = float(0)
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                Nx = N1_Sex.lx
                NOTE: Waples AgeNe V1 rounds this value down for display purposes (but not for calculation)
                NOTE: Waples AgeNe V1 totals the rounded Nx value to get the total adults
                '''
                
                '''
                Nx = N1.lx
                '''
                str_Working_Msg = 'Nx = N1.lx'
                
                
#                 if self.boolUseAgeNeSimParameters:
#                     intN1 = self.N1_Odict[stringSex][intAge]
#                 else:
#                     intN1 = self.intN1_intNewbornsBySex
                
                intN1 = self.N1_Odict[stringSex][intAge]
                                
                num_Nx = intN1 * self.lx_Odict[stringSex][intAge]
                
                #if (intAge > self.intMinMatingAge) and intAge < self.intMaxAgeAdjusted:
                #if (intAge > self.intMinMatingAge) and intAge <= self.intMaxAgeAdjusted:
                if (intAge > self.intMinMatingAge) and intAge <= self.intMaxAgeAdjusted:
                    ''' Includes NON-fertile or NON-reproductively competent animals i.e. senescent '''
                    num_Nx_Sum_N_Adults += num_Nx
                pass
                if (intAge > self.intMinMatingAge) and intAge <= self.intMaxMatingAge:
                    ''' ONLY fertile or reproductively competent animals i.e. not senescent '''
                    num_Nx_Sum_Nc_Adults += num_Nx
                pass
                
                num_Nx_Sum_All += float(num_Nx)
                
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_Nx)
                self.Nx_Odict[stringSex] = odictCalcAgeValues
                pass
            
            self.dictCalcTotals[stringSex][self.static_stringDictKey_CalcTotals_Nx_N_Adults] = num_Nx_Sum_N_Adults
            self.dictCalcTotals[stringSex][self.static_stringDictKey_CalcTotals_Nx_Nc_Adults] = num_Nx_Sum_Nc_Adults
            self.dictCalcTotals[stringSex][self.static_stringDictKey_CalcTotals_Nx_All] = num_Nx_Sum_All
        pass
        self.Nx_Odict_Newborns_Per_Age_x = self.Nx_Odict
        self.method_Debug_Logging_Dict_List(False, [self.N1_Odict, self.lx_Odict, self.Nx_Odict], ['N1','lx', 'Nx'], str_Working_Msg)

        return True

    def method_Calc_Nx_Newborns_Per_Age_x_Totals(self):
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            num_Nx_Sum_All = float(0)
            num_Nx_Sum_N_Adults = float(0)
            num_Nx_Sum_Nc_Adults = float(0)
            #odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Values supplied by SIM
                '''
                ONLY REQUIRED WHEN Nx IS SUPPLIED BY SIM
                '''
                '''
                Nx = Nx from Sim
                '''
                str_Working_Msg = 'Nx = Nx from Sim'
                
                
                num_Nx = self.Nx_Odict[stringSex][intAge]
                
                #if (intAge > self.intMinMatingAge) and intAge < (self.intMaxAgeAdjusted - 1):  #Minus 1 ensures we exclude the MaxAge+1 (Died) age class from the parent count
                #if (intAge > self.intMinMatingAge) and intAge < (self.intMaxAgeAdjusted):
                if (intAge > self.intMinMatingAge) and intAge <= self.intMaxAgeAdjusted:
                    ''' Includes NON-fertile or NON-reproductively competent animals i.e. senescent '''
                    num_Nx_Sum_N_Adults += num_Nx
                pass
                if (intAge > self.intMinMatingAge) and intAge <= self.intMaxMatingAge:
                    ''' ONLY fertile or reproductively competent animals i.e. not senescent '''
                    num_Nx_Sum_Nc_Adults += num_Nx
                pass                
                num_Nx_Sum_All += float(num_Nx)
                
                #Assign calculated values
                #odictCalcAgeValues[intAge] = float(num_Nx)
                #self.Nx_Odict[stringSex] = odictCalcAgeValues
                pass
            
            self.dictCalcTotals[stringSex][self.static_stringDictKey_CalcTotals_Nx_N_Adults] = num_Nx_Sum_N_Adults
            self.dictCalcTotals[stringSex][self.static_stringDictKey_CalcTotals_Nx_Nc_Adults] = num_Nx_Sum_Nc_Adults
            self.dictCalcTotals[stringSex][self.static_stringDictKey_CalcTotals_Nx_All] = num_Nx_Sum_All
        pass
        self.Nx_Odict_Newborns_Per_Age_x = self.Nx_Odict
        self.method_Debug_Logging_Dict_List(False, [self.N1_Odict, self.lx_Odict, self.Nx_Odict], ['N1','lx', 'Nx'], str_Working_Msg)

        return True
    
    def method_Calc_bxNx_Per_Age_x(self):
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            num_bxNx_Sum_All = float(0)
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                bx.Nx
                '''
                str_Working_Msg = 'bx.Nx'
                
                
                num_bxNx = self.bx_Odict[stringSex][intAge] * self.Nx_Odict[stringSex][intAge]
                    
                num_bxNx_Sum_All += float(num_bxNx)
                
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_bxNx)
                self.bxNx_Odict[stringSex] = odictCalcAgeValues
            pass
            
            self.dictCalcTotals[stringSex][self.static_stringDictKey_CalcTotals_bxNx_All] = num_bxNx_Sum_All
        pass
        self.method_Debug_Logging_Dict_List(False, [self.bx_Odict, self.Nx_Odict, self.bxNx_Odict], ['bx','Nx', 'bxNx'], str_Working_Msg)
        
        return True

    def method_Calc_b_x_Scaled_Birth_Rate_Per_Age_x(self):
        
        intN1 = 0
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            odictCalcAgeValues = OrderedDict([])
            numbxNxSum = self.dictCalcTotals[stringSex][self.static_stringDictKey_CalcTotals_bxNx_All]
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                b_x = N1_All.bx/(SUM(bx.Nx).MaleOrFemale_Ratio)
                '''
                str_Working_Msg = 'b_x = N1_All.bx/(SUM(bx.Nx).MaleOrFemale_Ratio)'
                

#                 if self.boolUseAgeNeSimParameters:
#                     intN1 = (self.N1_Odict[stringSex][intAge]*2)
#                 else:
#                     intN1= self.intN1_intNewborns
                
                #intN1 = self.N1_Odict[stringSex][intAge]*2
                intN1 = self.N1_Odict[stringSex][intAge]
                
                if numbxNxSum > 0:
                    num_b_x = (intN1 * self.bx_Odict[stringSex][intAge]) / (numbxNxSum*self.dict_floatInitialSexRatio[stringSex])
                else:
                    num_b_x = 0
                    
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_b_x)
                self.b_x_Odict[stringSex] = odictCalcAgeValues
                self.method_Debug_Logging_Variable_List(False, [('Age','intAge',intAge),('intN1*2','intN1',intN1),('intN1*2','bx',self.bx_Odict[stringSex][intAge]),('SUM(bxNx)','numbxNxSum',numbxNxSum), ('SUM(bxNx)','numbxNxSum',numbxNxSum)], str_Working_Msg)
                self.method_Debug_Logging_Variable_List(False, [(str_Working_Msg,'num_b_x',num_b_x)], str_Working_Msg)
            pass
        pass
        self.b_x_Odict_Scaled_Birth_Rate_Per_Age_x = self.b_x_Odict
        self.method_Debug_Logging_Dict_List(False, [self.b_x_Odict, self.bx_Odict], ['b_x','bx'], str_Working_Msg)
        
        return True

    def method_Calc_Bx_Per_Age_x(self):
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                Bx = b_x.Nx
                '''
                str_Working_Msg = 'Bx = b_x.Nx'
                
                
                num_Bx = self.b_x_Odict[stringSex][intAge] * self.Nx_Odict[stringSex][intAge]
                
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_Bx)
                self.Bx_Odict[stringSex] = odictCalcAgeValues
                pass
            
            pass
        
        self.Bx_Per_Age_x = self.Bx_Odict
        self.method_Debug_Logging_Dict_List(False, [self.b_x_Odict, self.Nx_Odict, self.Bx_Odict], ['b_x','Nx','Bx'], str_Working_Msg)
        
        return True

    def method_Calc_AgexBx_Div_N1_Per_Age_x(self):
        
        intN1 = 0
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            num_xBx_Div_N1_Sum_All = float(0)
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                xBx/N1
                '''
                str_Working_Msg = 'xBx/N1'
                
                
#                 if self.boolUseAgeNeSimParameters:
#                     intN1 = (self.N1_Odict[stringSex][intAge]*2)
#                 else:
#                     intN1= self.intN1_intNewborns
                
                #intN1 = self.N1_Odict[stringSex][intAge]*2
                intN1 = self.N1_Odict[globalsSS.SexConstants.static_stringSexMale][intAge]+self.N1_Odict[globalsSS.SexConstants.static_stringSexFemale][intAge]

                num_xBx_Div_N1 = (intAge * self.Bx_Odict[stringSex][intAge]) / intN1
                
                num_xBx_Div_N1_Sum_All += float(num_xBx_Div_N1)
                
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_xBx_Div_N1)
                self.xBx_Div_N1_Odict[stringSex] = odictCalcAgeValues

                self.method_Debug_Logging_Variable_List(False, [('Age','intAge',intAge),('Bx','Bx',self.Bx_Odict[stringSex][intAge]),('intN1*2','intN1',intN1)], str_Working_Msg)
                self.method_Debug_Logging_Variable_List(False, [(str_Working_Msg,'num_xBx_Div_N1',num_xBx_Div_N1)], str_Working_Msg)

            self.dictCalcTotals[stringSex][self.static_stringDictKey_CalcTotals_L_All] = num_xBx_Div_N1_Sum_All
            self.method_Debug_Logging_Variable_List(False, [('SUM(num_xBx_Div_N1)','num_xBx_Div_N1_Sum_All',num_xBx_Div_N1_Sum_All)], str_Working_Msg)
            pass
        pass
        self.AgexBx_Div_N1_Per_Age_x = self.xBx_Div_N1_Odict
        self.method_Debug_Logging_Dict_List(False, [self.Bx_Odict, self.N1_Odict, self.xBx_Div_N1_Odict], ['Bx','N1,','xBx_Div_N1_Odict'], str_Working_Msg)
        
        self.method_Finalise()
        return True
    
    def method_AgeNe_LifeTable_Final_Calculations(self):
        
        self.method_Calc_lx_Fraction_Newborn_Still_Alive_Per_Age_x()
        self.method_Calc_bxlx_Per_Age_x()
        
        if self.boolUseAgeNeSimParameters:
            #Nx is supplied but totals must be calculated
            self.method_Calc_Nx_Newborns_Per_Age_x_Totals()
            pass
        else:
            self.method_Calc_Nx_Newborns_Per_Age_x()
        pass
    
        self.method_Calc_bxNx_Per_Age_x()
        
#         if self.boolUseAgeNeSimParameters:
#             #b_x is supplied
#             pass
#         else:
#             self.method_Calc_b_x_Scaled_Birth_Rate_Per_Age_x()
        self.method_Calc_b_x_Scaled_Birth_Rate_Per_Age_x()
            
        self.method_Calc_Bx_Per_Age_x()
        self.method_Calc_AgexBx_Div_N1_Per_Age_x()
        
        #DEBUG_ON
#         if self.boolUseAgeNeSimParameters:
#                 pass
#         else:
#             with globalsSS.Pause_Console() as obj_Pause:
#                 obj_Pause.method_Pause_Console()
#             pass
#         pass   
        #DEBUG_OFF
        
        return True
    
    def method_Finalise(self):
        
        self.Calculated_Totals = self.dictCalcTotals
        pass


    def method_Debug_Logging_Variable_List(self, bool_Pause, list_Tup_Variables, str_Message):

        #DEBUG_ON
        if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
            with dcb_Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
            self.obj_Log_Debug_AgeNe.debug(globalsSS.Output_Display_Constants.static_str_Message_Separator)
            self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + str_Message_Location)
            self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + str_Message)
            for tup_Op_Var_Value in list_Tup_Variables:
                self.method_Debug_Logging_Variables(tup_Op_Var_Value) 
            pass    
            if bool_Pause:
                with globalsSS.Pause_Console() as obj_Pause:
                    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
            pass
        pass
                    
#         if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
#             t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
#             #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
#             #    t2 = Timer2(True)
#             #    t2.Start()
#             #pass                    
#         pass

        return True
     
    def method_Debug_Logging_Variables(self, tup_Op_Var_Value):

        #DEBUG_ON
        if globalsSS.Logger_Debug_Display.bool_Debug_Display:
            str_Msg_Prefix = globalsSS.Logger_Debug_AgeNe.static_str_Logger_Message_Prefix
            if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                str_Operation, str_Var_Name, num_Value = tup_Op_Var_Value
                self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + ' Op: ' + str_Operation + ' ; Var: ' + str_Var_Name + ' ; Value: ' + str(num_Value)) 
            pass
        pass
                    
#         if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
#             t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
#             #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
#             #    t2 = Timer2(True)
#             #    t2.Start()
#             #pass                    
#         pass

        return True 

    def method_Debug_Logging_Dict_List(self, bool_Pause, list_Dicts_To_Log, list_Dicts_To_Log_Names, str_Message):

        #DEBUG_ON
        if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
            with dcb_Debug_Location() as obj_DebugLoc:
                str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
            pass
            str_Msg_Prefix = globalsSS.Logger_Debug_Display.static_str_Logger_Message_Prefix
            self.obj_Log_Debug_AgeNe.debug(globalsSS.Output_Display_Constants.static_str_Message_Separator)
            self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + str_Message_Location)
            self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + str_Message)
            int_Dict_Count = 0
            for dict_To_Log in list_Dicts_To_Log:
                dict_To_Log_Name = list_Dicts_To_Log_Names[int_Dict_Count]
                self.method_Debug_Logging_Dict(dict_To_Log, dict_To_Log_Name) 
                int_Dict_Count += 1
            pass    
            if bool_Pause:
                with globalsSS.Pause_Console() as obj_Pause:
                    obj_Pause.method_Pause_Console(str_Message_Location)
                pass
            pass
        pass
                    
#         if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
#             t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
#             #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
#             #    t2 = Timer2(True)
#             #    t2.Start()
#             #pass                    
#         pass

        return True
    
        
    def method_Debug_Logging_Dict(self, dict_To_Log, str_Dict_To_Log_Name):

        #DEBUG_ON
        if globalsSS.Logger_Debug_Display.bool_Debug_Display:
            str_Msg_Prefix = globalsSS.Logger_Debug_AgeNe.static_str_Logger_Message_Prefix
            if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                for str_Sex, value in dict_To_Log.items():
                    self.obj_Log_Debug_AgeNe.debug(str_Msg_Prefix + ' ' + str_Dict_To_Log_Name.ljust(6) + ' ; Sex: ' + str_Sex.ljust(6) + ' ; Total: ' + str(round(sum(collections__Counter(value).values()),2)) + ' ; Values: ' + str(value)) 
                pass    
            pass
        pass
                    
#         if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
#             t2.Stop(self.obj_Log_Debug_Timing, '', bool_Pause_Run=globalsSS.Logger_Debug_Timing.bool_Debug_Timing__Pause)
#             #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
#             #    t2 = Timer2(True)
#             #    t2.Start()
#             #pass                    
#         pass

        return True 
        