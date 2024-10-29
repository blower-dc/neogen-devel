#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
from globals_SharkSim import globalsSS
from AutoVivificationHandler import AutoVivificationHandler 
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
from collections import OrderedDict
from decimal import *

gstringModuleName='object_SSAgeNe_DemographicTable.py'
gstringClassName='object_SSAgeNe_DemographicTable'

class object_SSAgeNe_DemographicTable(object):
    """Handle SS Age Ne Demographic Table Operations"""

# -------------- Class specific routines

    __slots__ = (
                 #PROPERTIES
                 'Max_Age'
                 ,'List_Sexes'
                 ,'Initial_Male_Sex_Ratio'
                 ,'N1_Newborns'
                 ,'N1_Newborns_Per_Sex_Per_Age'
                 ,'Calculated_Totals'
                 ,'Calculated_Totals_Life_Tables'
                 ,'lx_Odict_Fraction_Newborn_Still_Alive_Per_Age_x'                 
                 ,'Nx_Odict_Newborns_Per_Age_x'
                 ,'b_x_Odict_Scaled_Birth_Rate_Per_Age_x'
                 ,'Nx_Odict_Newborns_Per_Age_x'
                 ,'kbarx_Odict_Mean_Reproductive_Success_Per_Age_x'
                 ,'alpha_Value_Scaling_Poisson_Variance_In_Reproductive_Success'
                 ,'Use_Sim_Parameters'
                 #VARIABLES
                 #,'object_SSAgeNe_LifeTable'
                 ,'intMinAge'
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
                 ,'dictCalcTotals'
                 ,'dictCalcTotalsLifeTables'
                 ,'lx_Odict'
                 ,'Nx_Odict'
                 ,'b_x_Odict'
                 ,'kbarx_Odict'
                 ,'alphaPoisson_Odict'
                 ,'Vx_Odict'
                 ,'Dx_Odict'
                 ,'kbarDx_Odict'
                 ,'kbarAll_Odict'
                 ,'delta_kbar_Odict'
                 ,'SSDIx_Odict'
                 ,'SSDGx_Odict'
                 ,'SSDx_Odict'
                 ,'Yx_Odict'
                 ,'Nb_Vx_All_Odict'
                 ,'Nb_Vx_All_Sexes_Odict'
                 ,'boolUseAgeNeSimParameters' 
                 #CONSTANTS
                 ,'static_stringDictKey_CalcTotals_kbarx_Dx_All'
                 ,'static_stringDictKey_CalcTotals_SSD_T'
                 ,'static_stringDictKey_CalcTotals_Vk_All'
                 ,'static_stringDictKey_CalcTotals_kbar_All'
                 ,'static_stringDictKey_CalcTotals_Nx_All'
                 ,'static_stringDictKey_CalcTotals_Nb_kbar_All_Sexes'
                 ,'static_stringDictKey_CalcTotals_Nb_Vx_All_Sexes'
                 )
    
    static_stringDictKey_CalcTotals_kbarx_Dx_All = 'kbarx_Dx_All'  
    static_stringDictKey_CalcTotals_SSD_T = 'SSD_T'  
    static_stringDictKey_CalcTotals_Vk_All = 'Vk_All'
    static_stringDictKey_CalcTotals_Nx_All = 'Nx_All'  
    static_stringDictKey_CalcTotals_kbar_All = 'kbar_All'
    static_stringDictKey_CalcTotals_Nb_kbar_All_Sexes = 'Nb_kbar_All_Sexes'  
    static_stringDictKey_CalcTotals_Nb_Vx_All_Sexes = 'Nb_Vx_All_Sexes'  
       
    def __init__(self):
        
        #Initialize  PROPERTIES
        self.Max_Age = 0
        self.List_Sexes = []
        self.Initial_Male_Sex_Ratio = 0
        self.Calculated_Totals = AutoVivificationHandler()
        self.Calculated_Totals_Life_Tables = AutoVivificationHandler()
        self.N1_Newborns = 0
        self.N1_Newborns_Per_Sex_Per_Age = 0
        self.lx_Odict_Fraction_Newborn_Still_Alive_Per_Age_x = OrderedDict([])
        self.Nx_Odict_Newborns_Per_Age_x = OrderedDict([])
        self.b_x_Odict_Scaled_Birth_Rate_Per_Age_x = OrderedDict([])
        self.kbarx_Odict_Mean_Reproductive_Success_Per_Age_x = OrderedDict([])
        self.alpha_Value_Scaling_Poisson_Variance_In_Reproductive_Success = OrderedDict([])
        self.Use_Sim_Parameters = False
        
        #Initialize VARIALBLES
        self.intMinAge = 1
        self.intMaxAge = 0
        self.intMaxAgeAdjusted = 0
        self.intMaxAgeAdjustedForRange = 0
        self.listSexes = []
        self.floatInitialMaleSexRatio = 0
        self.dict_floatInitialSexRatio = OrderedDict([])
        self.intN1_intNewborns = 0
        self.N1_Odict = OrderedDict([])
        self.intN1_intNewbornsBySex = 0
        self.odictSexAgeInMonths = OrderedDict([])
        self.dictCalcTotals = AutoVivificationHandler()
        self.dictCalcTotalsLifeTables = AutoVivificationHandler()
        self.lx_Odict = OrderedDict([])
        self.Nx_Odict = OrderedDict([])
        self.b_x_Odict = OrderedDict([])
        self.kbarx_Odict = OrderedDict([])
        self.alphaPoisson_Odict = OrderedDict([])
        self.Vx_Odict = OrderedDict([])
        self.Dx_Odict = OrderedDict([])
        self.kbarDx_Odict = OrderedDict([])
        self.kbarAll_Odict = OrderedDict([])
        self.delta_kbar_Odict = OrderedDict([])
        self.SSDIx_Odict = OrderedDict([])
        self.SSDGx_Odict = OrderedDict([])
        self.SSDx_Odict = OrderedDict([])
        self.Yx_Odict = OrderedDict([])
        self.Nb_Vx_All_Odict = OrderedDict([])
        self.Nb_Vx_All_Sexes_Odict = OrderedDict([])
        self.boolUseAgeNeSimParameters = False

        pass
        
           
    def method_Initialise(self):
         
        #PROPERTIES -> VARIABLES
        self.intMaxAge = self.Max_Age
        self.listSexes = self.List_Sexes
        self.floatInitialMaleSexRatio = self.Initial_Male_Sex_Ratio
        self.dict_floatInitialSexRatio[globalsSS.SexConstants.static_stringSexMale] = self.floatInitialMaleSexRatio
        self.dict_floatInitialSexRatio[globalsSS.SexConstants.static_stringSexFemale] = 1 - self.floatInitialMaleSexRatio
        self.intN1_intNewborns = self.N1_Newborns
        self.dictCalcTotalsLifeTables = self.Calculated_Totals_Life_Tables
        self.b_x_Odict = self.b_x_Odict_Scaled_Birth_Rate_Per_Age_x
        self.alphaPoisson_Odict = self.alpha_Value_Scaling_Poisson_Variance_In_Reproductive_Success
        self.lx_Odict = self.lx_Odict_Fraction_Newborn_Still_Alive_Per_Age_x
        self.Nx_Odict = self.Nx_Odict_Newborns_Per_Age_x
        self.boolUseAgeNeSimParameters = self.Use_Sim_Parameters
        if self.boolUseAgeNeSimParameters: 
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
#                     odictCalcAgeValuesInYears[intAge] = intAge
#                     self.odictSexAgeInYears[stringSex] = odictCalcAgeValuesInYears
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
#                     odictCalcAgeValuesInYears[intAge] = intAge
#                     self.odictSexAgeInYears[stringSex] = odictCalcAgeValuesInYears
                pass
       
#         odictCalcAgeValues = OrderedDict([])
#         
#         for stringSex in self.listSexes:
#             for intAge in range(1, self.intMaxAge+1):
#                 intAgeInMonths = intAge * 12
#                 odictCalcAgeValues[intAge] = intAgeInMonths
#                 self.odictSexAgeInMonths[stringSex] = odictCalcAgeValues
#             pass
        
        self.intN1_intNewbornsBySex = self.intN1_intNewborns / len(self.odictSexAgeInMonths)

        self.dictCalcTotals = {
                               globalsSS.SexConstants.static_stringSexAll:
                                   {
                                    self.static_stringDictKey_CalcTotals_Nb_kbar_All_Sexes: 0
                                    ,self.static_stringDictKey_CalcTotals_Nb_Vx_All_Sexes: 0
                                    }
                               ,globalsSS.SexConstants.static_stringSexMale:
                                   {
                                    self.static_stringDictKey_CalcTotals_kbarx_Dx_All: 0
                                    ,self.static_stringDictKey_CalcTotals_SSD_T: 0
                                    ,self.static_stringDictKey_CalcTotals_Vk_All: 0
                                    }
                               ,globalsSS.SexConstants.static_stringSexFemale:
                                    {
                                    self.static_stringDictKey_CalcTotals_kbarx_Dx_All: 0
                                    ,self.static_stringDictKey_CalcTotals_SSD_T: 0
                                    ,self.static_stringDictKey_CalcTotals_Vk_All: 0
                                    }
                               }
        
        pass
    
    def method_Calc_kbarx_Odict_Mean_Reproductive_Success_Per_Age_x(self):
        
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                kbarx = kbar0 =, kbar1 = b_1, when x > 1 kbarx = kbar(x-1) + b_x
                '''
                if intAge == 0:
                    num_kbarx = 0
                elif intAge == 1:
                    num_kbarx = self.b_x_Odict[stringSex][intAge]
                elif intAge > 1:
                    num_kbarx = self.kbarx_Odict[stringSex][intAge-1] + self.b_x_Odict[stringSex][intAge]
                
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_kbarx)
                self.kbarx_Odict[stringSex] = odictCalcAgeValues
                pass
            
            pass
        
        self.kbarx_Odict_Mean_Reproductive_Success_Per_Age_x = self.kbarx_Odict
        pass
    
    def method_Calc_Vx_Odict_Varience_Reproductive_Success_Per_Age_x(self):
        
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                Vx = alphaPoissonVarianveInReproductiveSuccessScalingFactor * kbarx
                '''
                num_varx = self.alphaPoisson_Odict[stringSex][intAge] * self.kbarx_Odict[stringSex][intAge]
                
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_varx)
                self.Vx_Odict[stringSex] = odictCalcAgeValues
                pass
            
            pass
        
        #self.varx_Odict_Variance_Reproductive_Success_Per_Age_x = self.Vx_Odict
        pass

    def method_Calc_Dx_Odict_Deaths_After_Reaching_Age_x(self):
        
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                Dx = Nx - N(x+1)
                '''
                if intAge < self.intMaxAgeAdjusted:
                    num_Dx = self.Nx_Odict[stringSex][intAge] - self.Nx_Odict[stringSex][intAge+1]
                    '''
                    Sometimes (when cohorts have very low numbers of individuals) the number of survivors Nx...
                    in the next age cohort it larger than the previous cohort...
                    this leads to a negative number of deaths (-Dx) which is incorrect so change it to zero
                    ''' 
                    if num_Dx < 0:
                        num_Dx = 0
                    pass
                else:
                    num_Dx = self.Nx_Odict[stringSex][intAge] - 0
                    
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_Dx)
                self.Dx_Odict[stringSex] = odictCalcAgeValues
                pass
            
            pass
        
        pass

    def method_Calc_kbarx_Dx_Odict_Per_Age_x(self):
        
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            num_kbarx_Dx_Sum_All = float(0)
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                kbarx.Dx
                '''
                num_kbarx_Dx = self.kbarx_Odict[stringSex][intAge] * self.Dx_Odict[stringSex][intAge]
                
                num_kbarx_Dx_Sum_All += num_kbarx_Dx    
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_kbarx_Dx)
                self.kbarDx_Odict[stringSex] = odictCalcAgeValues
                pass
            
            self.dictCalcTotals[stringSex][self.static_stringDictKey_CalcTotals_kbarx_Dx_All] = num_kbarx_Dx_Sum_All
            pass
        
        pass

    def method_Calc_kbarAll_Per_Age_x(self):
        
        intN1 = 0
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                kbarAll = kbarx_Dx_Sum_All / N1_Sex
                '''
#                 if self.boolUseAgeNeSimParameters:
#                     intN1 = self.N1_Odict[stringSex][intAge]
#                 else:
#                     intN1 = self.intN1_intNewbornsBySex
                
                intN1 = self.N1_Odict[stringSex][intAge]

                num_kbarAll =  self.dictCalcTotals[stringSex][self.static_stringDictKey_CalcTotals_kbarx_Dx_All] / intN1
                
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_kbarAll)
                self.kbarAll_Odict[stringSex] = odictCalcAgeValues
                pass
            
            self.dictCalcTotals[stringSex][self.static_stringDictKey_CalcTotals_kbar_All] = num_kbarAll
            pass
        
        pass

    def method_Calc_Delta_kbar_Per_Age_x(self):
        
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                Delta_kbar = kbarx - kbarAll
                '''
                num_delta_kbar =  self.kbarx_Odict[stringSex][intAge] - self.kbarAll_Odict[stringSex][intAge]
                
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_delta_kbar)
                self.delta_kbar_Odict[stringSex] = odictCalcAgeValues
                pass
            
            pass
        
        pass

    def method_Calc_SSD_Ix_Per_Age_x(self):
        
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                SSD_Ix = Dx.Vx
                '''
                num_ssdix =  self.Dx_Odict[stringSex][intAge] * self.Vx_Odict[stringSex][intAge]
                
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_ssdix)
                self.SSDIx_Odict[stringSex] = odictCalcAgeValues
                pass
            
            pass
        
        pass

    def method_Calc_SSD_Gx_Per_Age_x(self):
        
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                SSD_Gx = Dx.SQR(Delta_kbar)
                '''
                num_ssdgx =  self.Dx_Odict[stringSex][intAge] * (self.delta_kbar_Odict[stringSex][intAge]*self.delta_kbar_Odict[stringSex][intAge])
                
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_ssdgx)
                self.SSDGx_Odict[stringSex] = odictCalcAgeValues
                pass
            
            pass
        
        pass

    def method_Calc_SSDx_Per_Age_x(self):
        
        intN1 = 0
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            num_ssdx_Sum_all = float(0)
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                SSDx = SSD_I + SSD_G
                '''
                num_ssdx =  self.SSDIx_Odict[stringSex][intAge] + self.SSDGx_Odict[stringSex][intAge]
                
                num_ssdx_Sum_all += num_ssdx
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_ssdx)
                self.SSDx_Odict[stringSex] = odictCalcAgeValues
                pass
            
            self.dictCalcTotals[stringSex][self.static_stringDictKey_CalcTotals_SSD_T] = num_ssdx_Sum_all
            '''
            Vk_All = SSD_T / Vx_All
            '''
#             if self.boolUseAgeNeSimParameters:
#                 intN1 = self.N1_Odict[stringSex][intAge]
#             else:
#                 intN1 = self.intN1_intNewbornsBySex
            
            intN1 = self.N1_Odict[stringSex][intAge]

            self.dictCalcTotals[stringSex][self.static_stringDictKey_CalcTotals_Vk_All] = num_ssdx_Sum_all / intN1
            
        # self.method_Finalise()
        pass

    def method_Calc_Nb_kbar_All_Sexes(self):
        
        #Perform calculations
        '''
        #### WRONG  Nb_kbar_All_Sexes = ((2*#Sexes)/(N_tot_Females + N_tot_Males))*1000  #Not sure why this is divided by 1000 but it is required to produce the correct Nb
        Nb_kbar_All_Sexes = (2*#Sexes)/ ((N_tot_Females + N_tot_Males)/ N1)    #Not sure why this is divided by N1 but it is required to produce the correct Nb
        '''
        intN1 = self.intN1_intNewborns
        #num_Nb_kbar_All_Sexes = 1000*((2 * len(self.listSexes)) / (self.dictCalcTotalsLifeTables[self.listSexes[0]][self.static_stringDictKey_CalcTotals_Nx_All] + self.dictCalcTotalsLifeTables[self.listSexes[0]][self.static_stringDictKey_CalcTotals_Nx_All]))
        num_Nb_kbar_All_Sexes = (2 * len(self.listSexes)) / ((self.dictCalcTotalsLifeTables[self.listSexes[0]][self.static_stringDictKey_CalcTotals_Nx_All] + self.dictCalcTotalsLifeTables[self.listSexes[1]][self.static_stringDictKey_CalcTotals_Nx_All]) / intN1) 
        
        #Assign calculated values
        self.dictCalcTotals[globalsSS.SexConstants.static_stringSexAll][self.static_stringDictKey_CalcTotals_Nb_kbar_All_Sexes] = num_Nb_kbar_All_Sexes
        pass

    def method_Calc_Yx_Per_Age_x(self):
        
        
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            odictCalcAgeValues = OrderedDict([])
            
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                Yx = (2 * b_x)- Nb_kbar_All_Sexes
                '''
                num_Yx = (2 * self.b_x_Odict[stringSex][intAge]) - self.dictCalcTotals[globalsSS.SexConstants.static_stringSexAll][self.static_stringDictKey_CalcTotals_Nb_kbar_All_Sexes]
                
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_Yx)
                self.Yx_Odict[stringSex] = odictCalcAgeValues
                pass
            
            pass
        pass

    def method_Calc_Nb_Vx_All_Per_Age_x(self):
         
         
        for stringSex, odictAgeValues in self.odictSexAgeInMonths.items():
            
            num_Nb_Vx_All_Sum = float(0)
            odictCalcAgeValues = OrderedDict([])
             
            for intAge, value in odictAgeValues.items():
                #Perform calculations
                '''
                ### WRONG  Nb_Vx_All = ((Nx/1000)*((2*b_x*alphaPoisson)+SQR(Yx)) #Not sure why Nx is divided by 1000 but it is required to calculate correct Nb
                Nb_Vx_All = ((lx*InitialMaleSexRatio)*((2*b_x*alphaPoisson)+SQR(Yx)) #Not sure why Nx is divided by 1000 but it is required to calculate correct Nb
                '''
                num_lx = self.lx_Odict[stringSex][intAge]
                
                #num_Nb_Vx_All = (self.Nx_Odict[stringSex][intAge]/1000)*((2*self.b_x_Odict[stringSex][intAge]*self.alphaPoisson_Odict[stringSex][intAge])+(self.Yx_Odict[stringSex][intAge]*self.Yx_Odict[stringSex][intAge]))
                #num_Nb_Vx_All = (num_lx*self.floatInitialMaleSexRatio)*((2*self.b_x_Odict[stringSex][intAge]*self.alphaPoisson_Odict[stringSex][intAge])+(self.Yx_Odict[stringSex][intAge]*self.Yx_Odict[stringSex][intAge]))
                num_Nb_Vx_All = (num_lx*self.dict_floatInitialSexRatio[stringSex])*((2*self.b_x_Odict[stringSex][intAge]*self.alphaPoisson_Odict[stringSex][intAge])+(self.Yx_Odict[stringSex][intAge]*self.Yx_Odict[stringSex][intAge]))
                #num_Nb_Vx_All = Decimal(num_lx*self.dict_floatInitialSexRatio[stringSex])*Decimal((2*self.b_x_Odict[stringSex][intAge]*self.alphaPoisson_Odict[stringSex][intAge])+(self.Yx_Odict[stringSex][intAge]*self.Yx_Odict[stringSex][intAge]))
                
                num_Nb_Vx_All_Sum += num_Nb_Vx_All
                #Assign calculated values
                odictCalcAgeValues[intAge] = float(num_Nb_Vx_All)
                self.Nb_Vx_All_Odict[stringSex] = odictCalcAgeValues
                pass
             
            pass
        
        pass
 
    def method_Calc_Nb_Vx_Per_Age_All_Sexes(self):

        num_Nb_Vx_All_Sexes_Sum = float(0)
        odictCalcAgeValues = OrderedDict([])
        
        for intAge in range(self.intMinAge, self.intMaxAgeAdjustedForRange):
            
            #Perform calculations
            '''
            Nb_Vx_All_Sexes = (Nb_Vx_All_Male + Nb_Vx_All_Female)
            '''
            num_Nb_Vx_All_Sexes = self.Nb_Vx_All_Odict[self.listSexes[0]][intAge] + self.Nb_Vx_All_Odict[self.listSexes[1]][intAge]
            
            num_Nb_Vx_All_Sexes_Sum += num_Nb_Vx_All_Sexes
            #Assign calculated values
            odictCalcAgeValues[intAge] = float(num_Nb_Vx_All_Sexes)
            pass
        
        self.Nb_Vx_All_Sexes_Odict[intAge] = odictCalcAgeValues
        self.dictCalcTotals[globalsSS.SexConstants.static_stringSexAll][self.static_stringDictKey_CalcTotals_Nb_Vx_All_Sexes] = num_Nb_Vx_All_Sexes_Sum
        
        self.method_Finalise()
        pass
 
    def method_AgeNe_DemographicTable_Final_Calculations(self):
    
        self.method_Calc_kbarx_Odict_Mean_Reproductive_Success_Per_Age_x()
        self.method_Calc_Vx_Odict_Varience_Reproductive_Success_Per_Age_x()
        self.method_Calc_Dx_Odict_Deaths_After_Reaching_Age_x()
        self.method_Calc_kbarx_Dx_Odict_Per_Age_x()
        self.method_Calc_kbarAll_Per_Age_x()
        self.method_Calc_Delta_kbar_Per_Age_x()
        self.method_Calc_SSD_Ix_Per_Age_x()
        self.method_Calc_SSD_Gx_Per_Age_x()
        self.method_Calc_SSDx_Per_Age_x()
        self.method_Calc_Nb_kbar_All_Sexes()
        self.method_Calc_Yx_Per_Age_x()
        self.method_Calc_Nb_Vx_All_Per_Age_x()
        self.method_Calc_Nb_Vx_Per_Age_All_Sexes()
        pass
    
    def method_Finalise(self):
        
        self.Calculated_Totals = self.dictCalcTotals
        pass
