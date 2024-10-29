#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
from globals_SharkSim import globalsSS
from AutoVivificationHandler import AutoVivificationHandler 
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
from collections import OrderedDict
#from numpy import mean

gstringModuleName='object_SSAgeNe.py'
gstringClassName='object_SSAgeNe'

class object_SSAgeNe(object):
    """Handle SS Age Ne Operations"""

# -------------- Class specific routines

    __slots__ = (
                 #PROPERTIES
                 'Initial_Male_Sex_Ratio'
                 ,'List_Sexes'
                 ,'N1_Newborns'
                 ,'N1_Newborns_Per_Sex_Per_Age'
                 ,'Calculated_Totals'
                 ,'Calculated_Totals_Life_Tables'
                 ,'Calculated_Totals_Demographic_Tables'
                 ,'Use_Sim_Parameters'
                 #VARIABLES
                 ,'floatInitialMaleSexRatio'
                 ,'listSexes'
                 ,'intN1_intNewborns'
                 #,'intN1_intNewbornsBySex'
                 ,'N1_Odict'
                 ,'dictCalcTotals'
                 ,'dictCalcTotalsLifeTables'
                 ,'dictCalcTotalsDemographicTables'
                 ,'boolUseAgeNeSimParameters'
                 #CONSTANTS
                 ,'static_stringDictKey_CalcTotals_kbar_Overall'
                 ,'static_stringDictKey_CalcTotals_kbar_All'
                 ,'static_stringDictKey_CalcTotals_Vk_Overall'
                 ,'static_stringDictKey_CalcTotals_Vk_All'
                 ,'static_stringDictKey_CalcTotals_L_All'
                 ,'static_stringDictKey_CalcTotals_L_Overall'
                 ,'static_stringDictKey_CalcTotals_Nx_N_Adults'
                 ,'static_stringDictKey_CalcTotals_Nx_Nc_Adults'
                 ,'static_stringDictKey_CalcTotals_N_Adults_Overall'
                 ,'static_stringDictKey_CalcTotals_Nc_Adults_Overall'
                 ,'static_stringDictKey_CalcTotals_Nx_All'
                 ,'static_stringDictKey_CalcTotals_N_Overall'
                 ,'static_stringDictKey_CalcTotals_NeDemo'
                 #,'static_stringDictKey_CalcTotals_NeDemo_Div_NAdultsOverall'
                 ,'static_stringDictKey_CalcTotals_NeDemo_Div_NcAdultsOverall'
                 ,'static_stringDictKey_CalcTotals_NeDemo_Div_NOverall'
                 ,'static_stringDictKey_CalcTotals_Nb_Vx_All_Sexes'
                 ,'static_stringDictKey_CalcTotals_Nb_Vx_All_Sexes_Overall'
                 ,'static_stringDictKey_CalcTotals_Nb_kbar_All_Sexes'
                 ,'static_stringDictKey_CalcTotals_NbDemo'
                 ,'static_stringDictKey_CalcTotals_Male_N1_Ratio'
                )
    
    static_stringDictKey_CalcTotals_kbar_Overall = 'kbar_Overall'
    static_stringDictKey_CalcTotals_kbar_All = 'kbar_All'
    static_stringDictKey_CalcTotals_Vk_Overall = 'Vk_Overall' 
    static_stringDictKey_CalcTotals_Vk_All = 'Vk_All' 
    static_stringDictKey_CalcTotals_L_All = 'L_All' 
    static_stringDictKey_CalcTotals_L_Overall = 'L_Overall' 
    static_stringDictKey_CalcTotals_Nx_N_Adults = 'Nx_N_Adults' 
    static_stringDictKey_CalcTotals_Nx_Nc_Adults = 'Nx_Nc_Adults' 
    static_stringDictKey_CalcTotals_N_Adults_Overall = 'N_Adults_Overall' 
    static_stringDictKey_CalcTotals_Nc_Adults_Overall = 'Nc_Adults_Overall' 
    static_stringDictKey_CalcTotals_Nx_All = 'Nx_All' 
    static_stringDictKey_CalcTotals_N_Overall = 'N_Overall' 
    static_stringDictKey_CalcTotals_NeDemo = 'NeDemo' 
    #static_stringDictKey_CalcTotals_NeDemo_Div_NAdultsOverall = 'NeDemoDivNAdultsOverall' 
    static_stringDictKey_CalcTotals_NeDemo_Div_NcAdultsOverall = 'NeDemoDivNcAdultsOverall' 
    static_stringDictKey_CalcTotals_NeDemo_Div_NOverall = 'NeDemoDivNOverall'
    static_stringDictKey_CalcTotals_Nb_Vx_All_Sexes = 'Nb_Vx_All_Sexes' 
    static_stringDictKey_CalcTotals_Nb_Vx_All_Sexes_Overall = 'Nb_Vx_All_Sexes_Overall'
    static_stringDictKey_CalcTotals_Nb_kbar_All_Sexes = 'Nb_kbar_All_Sexes'  
    static_stringDictKey_CalcTotals_NbDemo = 'NbDemo'  
    static_stringDictKey_CalcTotals_Male_N1_Ratio = 'Male_N1_Ratio'  
       
       
    def __init__(self):
        
        #Initialize  PROPERTIES
        self.Initial_Male_Sex_Ratio = 0
        self.List_Sexes = []
        self.N1_Newborns = 0
        self.N1_Newborns_Per_Sex_Per_Age = 0
        self.Calculated_Totals = AutoVivificationHandler() 
        self.dictCalcTotalsLifeTables = AutoVivificationHandler()
        self.dictCalcTotalsDemographicTables = AutoVivificationHandler()
        self.Use_Sim_Parameters = False
        
        #Initialize VARIALBLES
        self.listSexes = []
        self.floatInitialMaleSexRatio = 0
        self.intN1_intNewborns = 0
        self.N1_Odict = OrderedDict([])
        #self.intN1_intNewbornsBySex = 0
        self.dictCalcTotals = AutoVivificationHandler()
        self.boolUseAgeNeSimParameters = False
        pass
        
           
    def method_Initialise(self):
         
        #PROPERTIES -> VARIABLES
        self.listSexes = self.List_Sexes
        self.floatInitialMaleSexRatio = self.Initial_Male_Sex_Ratio 
        self.intN1_intNewborns = self.N1_Newborns
        self.Calculated_Totals = self.dictCalcTotals  
        self.dictCalcTotalsLifeTables = self.Calculated_Totals_Life_Tables
        self.dictCalcTotalsDemographicTables = self.Calculated_Totals_Demographic_Tables
        self.boolUseAgeNeSimParameters = self.Use_Sim_Parameters
        if self.boolUseAgeNeSimParameters: 
            self.N1_Odict = self.N1_Newborns_Per_Sex_Per_Age
            #self.method_Calc_mean_N1()
        
        self.dictCalcTotals = {
                               self.static_stringDictKey_CalcTotals_kbar_Overall: 0
                              ,self.static_stringDictKey_CalcTotals_Vk_Overall: 0
                              ,self.static_stringDictKey_CalcTotals_L_Overall: 0
                              ,self.static_stringDictKey_CalcTotals_N_Adults_Overall: 0
                              ,self.static_stringDictKey_CalcTotals_Nc_Adults_Overall: 0
                              ,self.static_stringDictKey_CalcTotals_N_Overall: 0
                              ,self.static_stringDictKey_CalcTotals_NeDemo: 0
                              #,self.static_stringDictKey_CalcTotals_NeDemo_Div_NAdultsOverall: 0
                              ,self.static_stringDictKey_CalcTotals_NeDemo_Div_NcAdultsOverall: 0
                              ,self.static_stringDictKey_CalcTotals_NeDemo_Div_NOverall: 0
                              ,self.static_stringDictKey_CalcTotals_NbDemo: 0
                              ,self.static_stringDictKey_CalcTotals_Male_N1_Ratio: 0
                              }
        
        pass
    
    def method_Calc_mean_N1(self):
        
#         listAllN1s = []
#         for stringSex, odictAgeValues in self.N1_Odict.items():
#             
#             for intAge, value in odictAgeValues.items():
#                 listAllN1s.append(value)
#         
#         self.intN1_intNewborns = mean(listAllN1s)    
        pass
    
    def method_Calc_kbar_Overall(self):
            
        #Perform calculations
        '''
        kbar_Overall = (Male_Sex_Ratio * kbar_All_Male) + ((1-Male_Sex_Ratio)*kbar_All_Female))
        '''
        num_kbar_Overall = (self.floatInitialMaleSexRatio * self.dictCalcTotalsDemographicTables[self.listSexes[0]][self.static_stringDictKey_CalcTotals_kbar_All]) + ((1-self.floatInitialMaleSexRatio) * self.dictCalcTotalsDemographicTables[self.listSexes[1]][self.static_stringDictKey_CalcTotals_kbar_All])
        
        self.dictCalcTotals[self.static_stringDictKey_CalcTotals_kbar_Overall] = num_kbar_Overall
        self.dictCalcTotals[self.static_stringDictKey_CalcTotals_Male_N1_Ratio] = self.floatInitialMaleSexRatio
        pass

    def method_Calc_Vk_Overall(self):
        
        #Perform calculations
        '''
        Vk_Overall = ((Male_Sex_Ratio * Vk_All_Male) + ((1-Male_Sex_Ratio)*Vk_All_Female))) +
                     (Male_Sex_Ratio*(1-Male_Sex_Ratio)*Vk_All_Female) + SQR(kbar_All_Male - kbar_All_Female))
        '''
        #num_Vk_Overall = ((self.floatInitialMaleSexRatio * self.dictCalcTotalsDemographicTables[self.listSexes[0]][self.static_stringDictKey_CalcTotals_Vk_All]) + ((1-self.floatInitialMaleSexRatio) * self.dictCalcTotalsDemographicTables[self.listSexes[1]][self.static_stringDictKey_CalcTotals_Vk_All])) + (self.floatInitialMaleSexRatio*(1-self.floatInitialMaleSexRatio)*((self.dictCalcTotalsDemographicTables[self.listSexes[0]][self.static_stringDictKey_CalcTotals_kbar_All]-self.dictCalcTotalsDemographicTables[self.listSexes[0]][self.static_stringDictKey_CalcTotals_kbar_All])*(self.dictCalcTotalsDemographicTables[self.listSexes[0]][self.static_stringDictKey_CalcTotals_kbar_All]-self.dictCalcTotalsDemographicTables[self.listSexes[1]][self.static_stringDictKey_CalcTotals_kbar_All])))
        ''' (Male_Sex_Ratio * Vk_All_Male) '''
        num_Vk_Overall__M_Part_1 = self.floatInitialMaleSexRatio * self.dictCalcTotalsDemographicTables[self.listSexes[0]][self.static_stringDictKey_CalcTotals_Vk_All]
        ''' ((1-Male_Sex_Ratio)*Vk_All_Female))) '''
        num_Vk_Overall__F_Part_1 = (1-self.floatInitialMaleSexRatio) * self.dictCalcTotalsDemographicTables[self.listSexes[1]][self.static_stringDictKey_CalcTotals_Vk_All]
        ''' (Male_Sex_Ratio*(1-Male_Sex_Ratio)) '''
        num_Vk_Overall__Part_2 = self.floatInitialMaleSexRatio * (1-self.floatInitialMaleSexRatio)
        ''' kbar_All_Male - kbar_All_Female '''
        num_Vk_Overall__Part_3a = (self.dictCalcTotalsDemographicTables[self.listSexes[0]][self.static_stringDictKey_CalcTotals_kbar_All] - self.dictCalcTotalsDemographicTables[self.listSexes[1]][self.static_stringDictKey_CalcTotals_kbar_All])
        ''' SQR(kbar_All_Male - kbar_All_Female) '''
        num_Vk_Overall__Part_3b = num_Vk_Overall__Part_3a * num_Vk_Overall__Part_3a
        
        ''' Vk_Overall '''
        num_Vk_Overall = (num_Vk_Overall__M_Part_1 + num_Vk_Overall__F_Part_1) + (num_Vk_Overall__Part_2 * num_Vk_Overall__Part_3b)
            
        self.dictCalcTotals[self.static_stringDictKey_CalcTotals_Vk_Overall] = num_Vk_Overall
        pass

    def method_Calc_L_Generation_Length_Overall(self):
        
        #Perform calculations
        '''
        L_Overall = (L_Male + L_Female) / 2
        '''
        num_L_Overall = (self.dictCalcTotalsLifeTables[self.listSexes[0]][self.static_stringDictKey_CalcTotals_L_All] + self.dictCalcTotalsLifeTables[self.listSexes[1]][self.static_stringDictKey_CalcTotals_L_All]) / 2
            
        self.dictCalcTotals[self.static_stringDictKey_CalcTotals_L_Overall] = num_L_Overall
        pass

    def method_Calc_N_N_Adults_Overall_Total_Adults(self):
        
        #Perform calculations
        '''
        N_Adults_Overall = Nx_Adults_Male + Nx_Adults_Female
        '''
        num_N_Adults_Overall = self.dictCalcTotalsLifeTables[self.listSexes[0]][self.static_stringDictKey_CalcTotals_Nx_N_Adults] + self.dictCalcTotalsLifeTables[self.listSexes[1]][self.static_stringDictKey_CalcTotals_Nx_N_Adults]
            
        self.dictCalcTotals[self.static_stringDictKey_CalcTotals_N_Adults_Overall] = num_N_Adults_Overall
        pass
    
    def method_Calc_N_Nc_Adults_Overall_Total_Adults_Reproductivly_Competant(self):
        
        #Perform calculations
        '''
        N_Nc_Adults_Overall = Nx_Nc_Adults_Male + Nx_Nc_Adults_Female
        '''
        num_Nc_Adults_Overall = self.dictCalcTotalsLifeTables[self.listSexes[0]][self.static_stringDictKey_CalcTotals_Nx_Nc_Adults] + self.dictCalcTotalsLifeTables[self.listSexes[1]][self.static_stringDictKey_CalcTotals_Nx_Nc_Adults]
            
        self.dictCalcTotals[self.static_stringDictKey_CalcTotals_Nc_Adults_Overall] = num_Nc_Adults_Overall
        pass

    def method_Calc_N_Overall_Total_Individuals(self):
        
        #Perform calculations
        '''
        N_Overall = Nx_All_Male + Nx_All_Female
        '''
        num_N_Overall = self.dictCalcTotalsLifeTables[self.listSexes[0]][self.static_stringDictKey_CalcTotals_Nx_All] + self.dictCalcTotalsLifeTables[self.listSexes[1]][self.static_stringDictKey_CalcTotals_Nx_All]
            
        self.dictCalcTotals[self.static_stringDictKey_CalcTotals_N_Overall] = num_N_Overall
        pass
    
    def method_Calc_NeDemographic_Eqn2(self):
            
        #Perform calculations
        '''
        NeDemographic = (4*(N1*L_Overall))/ (Vk_Overall + 2)
        '''
        num_NeDemo = (4*(self.intN1_intNewborns * self.dictCalcTotals[self.static_stringDictKey_CalcTotals_L_Overall])) / (self.dictCalcTotals[self.static_stringDictKey_CalcTotals_Vk_Overall] + 2)
        
        self.dictCalcTotals[self.static_stringDictKey_CalcTotals_NeDemo] = num_NeDemo
        
        pass

    def method_Calc_NeDemographic_Eqn2_Ratio_To_N_Adults_Overall(self):
            
        #Perform calculations
        '''
        NeDemo_Div_NAdultsOverall = NeDemo/Nc_Adults_Overall
        '''
#         if self.dictCalcTotals[self.static_stringDictKey_CalcTotals_N_Adults_Overall] > 0:
#             NeDemo_Div_NAdultsOverall = self.dictCalcTotals[self.static_stringDictKey_CalcTotals_NeDemo] / self.dictCalcTotals[self.static_stringDictKey_CalcTotals_N_Adults_Overall]
#         else:
#             NeDemo_Div_NAdultsOverall = 0
        if self.dictCalcTotals[self.static_stringDictKey_CalcTotals_Nc_Adults_Overall] > 0:
            NeDemo_Div_NcAdultsOverall = self.dictCalcTotals[self.static_stringDictKey_CalcTotals_NeDemo] / self.dictCalcTotals[self.static_stringDictKey_CalcTotals_Nc_Adults_Overall]
        else:
            NeDemo_Div_NcAdultsOverall = 0
            
        self.dictCalcTotals[self.static_stringDictKey_CalcTotals_NeDemo_Div_NcAdultsOverall] = NeDemo_Div_NcAdultsOverall
        
        pass

    def method_Calc_NeDemographic_Eqn2_Ratio_To_N_Overall(self):
            
        #Perform calculations
        '''
        NeDemo_Div_NOverall = NeDemo/N_Overall
        '''
        NeDemo_Div_NOverall = self.dictCalcTotals[self.static_stringDictKey_CalcTotals_NeDemo] / self.dictCalcTotals[self.static_stringDictKey_CalcTotals_N_Overall]
        
        self.dictCalcTotals[self.static_stringDictKey_CalcTotals_NeDemo_Div_NOverall] = NeDemo_Div_NOverall
        
        pass

    def method_Calc_Vk_All_Sexes_Overall(self):
            
        #Perform calculations
        '''
        #WRONG   Vk_All_Sexes_Overall = Vk_All_Sexes / (N_Overall/1000)
        Vk_All_Sexes_Overall = Vk_All_Sexes
        
        but in Waples AgeNe it is Vk_All_Sexes_Overall = Vk_All_Sexes / (N_Tot_Indivs_Overall/N1)
        however, I do that in the final Nb calc.  Leaving this code in case I need to revert.
        '''
        num_Vk_All_Sexes_Overall = self.dictCalcTotalsDemographicTables[globalsSS.SexConstants.static_stringSexAll][self.static_stringDictKey_CalcTotals_Nb_Vx_All_Sexes]
        
        self.dictCalcTotals[self.static_stringDictKey_CalcTotals_Nb_Vx_All_Sexes_Overall] = num_Vk_All_Sexes_Overall
        
        pass

    def method_Calc_NbDemographic(self):
            
        #Perform calculations
        '''
        #### WRING NbDemo =(N1*N_Overall*1*Nb_kbar_All)-2)/(Nb_kbar_All-1 + ((Vk_All_Sexes_Overall/(N_Tot_Indivs_Overall/N1))/Nb_kbar_All))
        NbDemo =(N_Overall*1*Nb_kbar_All)-2)/(Nb_kbar_All-1 + ((Vk_All_Sexes_Overall/(N_Tot/N1))/Nb_kbar_All))
        '''
        intN1 = self.N1_Newborns
        intN_Tot_Indivs_Overall = self.dictCalcTotals[self.static_stringDictKey_CalcTotals_N_Overall]
        float_Nb_kbar_All_Sexes = self.dictCalcTotalsDemographicTables[globalsSS.SexConstants.static_stringSexAll][self.static_stringDictKey_CalcTotals_Nb_kbar_All_Sexes]
        float_Nb_Vx_All_Sexes_Overall = self.dictCalcTotals[self.static_stringDictKey_CalcTotals_Nb_Vx_All_Sexes_Overall]
        
        num_NbDemo = ((intN_Tot_Indivs_Overall*1*float_Nb_kbar_All_Sexes)-2) / ((float_Nb_kbar_All_Sexes-1) + ((float_Nb_Vx_All_Sexes_Overall/(intN_Tot_Indivs_Overall/intN1)) / float_Nb_kbar_All_Sexes))
        
        self.dictCalcTotals[self.static_stringDictKey_CalcTotals_NbDemo] = num_NbDemo
        
        self.method_Finalise()
        pass
    
    def method_AgeNe_Final_Calculations(self):
        
        self.method_Calc_kbar_Overall()
        self.method_Calc_Vk_Overall()
        self.method_Calc_L_Generation_Length_Overall()
        self.method_Calc_N_N_Adults_Overall_Total_Adults()
        self.method_Calc_N_Nc_Adults_Overall_Total_Adults_Reproductivly_Competant()
        self.method_Calc_N_Overall_Total_Individuals()
        self.method_Calc_NeDemographic_Eqn2()
        self.method_Calc_NeDemographic_Eqn2_Ratio_To_N_Adults_Overall()
        self.method_Calc_NeDemographic_Eqn2_Ratio_To_N_Overall()
        self.method_Calc_Vk_All_Sexes_Overall()
        self.method_Calc_NbDemographic()
        pass
    
    def method_Finalise(self):
        
        self.Calculated_Totals = self.dictCalcTotals
        pass
