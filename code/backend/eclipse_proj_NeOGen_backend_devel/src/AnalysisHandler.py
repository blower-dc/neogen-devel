#------------------< Import python modules
# DEBUG Imports
from logging import getLogger as logging__getLogger
from handler_Debug import Timer
from handler_Debug import Timer2
from handler_Debug import Debug_Location
# Imports
from numpy import random as numpy__random
from numpy import array as numpy__array
from scipy import stats as scipy__stats
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import SharkSim modules
from globals_SharkSim import globalsSS


gstringModuleName='AnalysisHandler.py'
gstringClassName='AnalysisOperation'
gint_Large_Undefined_Number = 999999999999999.99 #Pandas aggregate from Excel file fails if this is > 15 digits
#gint_Large_Undefined_Number = float('NaN')

class AnalysisHandler:
    """Handle AnalysisOperation objects"""

    def __enter__(self):
         
        class AnalysisOperation: 
            """Explicitly control all fundemental file operations"""

            def __init__(self):

                '''
                ------------------
                Initialise class specific variables
                ------------------
                '''                        
                
                ''' Get all the loggers required for monitoring this object '''
                self.method_Initialise_Monitor_Loggers()

                return None         

            def method_Initialise_Monitor_Loggers(self):
                
                ''' 
                ~~~~~~~~~~~~~~~~~~~~~~~~~~
                Get all the loggers required for monitoring this object
                ~~~~~~~~~~~~~~~~~~~~~~~~~~
                '''
                ''' Get Run Display Logger '''
                self.obj_Log_Run_Display = logging__getLogger(globalsSS.Logger_Run_Display.static_Logger_Name__Run_Display)
                           
                ''' Get Default Logger '''
                self.obj_Log_Default_Display = logging__getLogger(globalsSS.Logger_Default_Display.static_Logger_Name__Default_Display)
        
                ''' Get Debug Logger '''
                self.obj_Log_Debug_Display = logging__getLogger(globalsSS.Logger_Debug_Display.static_Logger_Name__Debug_Display)
        
                ''' Get Debug Timer '''
                #self.obj_Log_Debug_Timing = None
                #if globalsSS.Logger_Debug_Timing.bool_Debug_Timing:
                self.obj_Log_Debug_Timing = logging__getLogger(globalsSS.Logger_Debug_Timing.static_Logger_Name__Debug_Timing)
                #pass

                ''' Get Debug AgeNe Logger '''
                self.obj_Log_Debug_AgeNe = None
                if globalsSS.Logger_Debug_AgeNe.bool_Debug_AgeNe:
                    self.obj_Log_Debug_AgeNe = logging__getLogger(globalsSS.Logger_Debug_AgeNe.static_Logger_Name__Debug_AgeNe)
                pass
                                        
                return True


            def method_Get_Mean_From_A_List(self, listValues):

                floatMean = 0
                
                floatMean = float(sum(listValues)) / len(listValues)

                return floatMean

            def method_Get_Population_Variance_From_A_List(self, listValues):

                floatVariance = 0
                floatDiff = 0
                floatSqrdDiff = 0
                floatSqrdDiffSum = 0

                #DEBUG ON
                #listfloatDiff = []
                #listfloatSqrdDiff = []
                #listfloatSqrdDiffSum =[]
                #DEBUG OFF
                 
                floatMean = self.method_Get_Mean_From_A_List(listValues)

                intListSize = 0
                intListSize = len(listValues)

                for i in range(0, intListSize):

                    floatDiff =  listValues[i] - floatMean
                    #listfloatDiff.append(floatDiff)
                                       
                    floatSqrdDiff =  floatDiff ** 2
                    #listfloatSqrdDiff.append(floatSqrdDiff)
                    
                    floatSqrdDiffSum = floatSqrdDiffSum + floatSqrdDiff
                    #listfloatSqrdDiffSum.append(floatSqrdDiffSum)
                pass

                floatVariance = floatSqrdDiffSum / len(listValues)

                return floatVariance

            def method_Get_Sample_Variance_From_A_List(self, listValues):

                floatVariance = 0
                floatDiff = 0
                floatSqrdDiff = 0
                floatSqrdDiffSum = 0

                #DEBUG ON
                #listfloatDiff = []
                #listfloatSqrdDiff = []
                #listfloatSqrdDiffSum =[]
                #DEBUG OFF
                 
                floatMean = self.method_Get_Mean_From_A_List(listValues)

                intListSize = 0
                intListSize = len(listValues)

                for i in range(0, intListSize):

                    floatDiff =  listValues[i] - floatMean
                    #listfloatDiff.append(floatDiff)
                                       
                    floatSqrdDiff =  floatDiff ** 2
                    #listfloatSqrdDiff.append(floatSqrdDiff)
                    
                    floatSqrdDiffSum = floatSqrdDiffSum + floatSqrdDiff
                    #listfloatSqrdDiffSum.append(floatSqrdDiffSum)
                pass
                
                intDenominator = len(listValues) - 1
                if intDenominator > 0:
                    floatVariance = floatSqrdDiffSum / intDenominator
                else:
                    #Produce error without causing a division by zero crash
                    floatVariance = gint_Large_Undefined_Number #99999999999999999999999999.99

                return floatVariance

            def method_Get_Demographic_Ne_By_Parental_Sex_Given_Known_Offspring(self, integerNumberofParentsForSex_Nsex, floatMeanLitterSizeForSex_MeanKsex, floatMeanVarianceLitterSizeForSex_VarKsex):

                '''
                Calculate Demographic Ne from the offspring known to be from parents of a particular sex.
                E.G. for Female parents:

                Nf = Number of female parents
                Mean(Kf) = Mean litter size for Females after a specific breeding event 
                Var(Kf) = Variance in litter size (reproductive success) for Females after a specific breeding event 

                Nef = ((Nf.Mean(Kf))-1)/((Mean(Kf)-1)+(Var(Kf)/mean(Kf))
                '''
                #Part 1: ((Nf.Mean(Kf))-1)
                floatPart1 = (integerNumberofParentsForSex_Nsex * floatMeanLitterSizeForSex_MeanKsex) - 1

                #Part 2: ((Mean(Kf)-1)+(Var(Kf)/mean(Kf))
                floatPart2 =  (floatMeanLitterSizeForSex_MeanKsex - 1) + (floatMeanVarianceLitterSizeForSex_VarKsex / floatMeanLitterSizeForSex_MeanKsex)

                #Part 3: Part1 / Part 2
                if floatPart2 > 0:
                    floatNeDemographicBySexFromKnownOffspring =  floatPart1 / floatPart2
                else:
                    #Produce error without causing a division by zero crash
                    floatNeDemographicBySexFromKnownOffspring = gint_Large_Undefined_Number #999999999999999.99 #99999999999999999999999999.99
                    
                return floatNeDemographicBySexFromKnownOffspring

            def method_Get_Demographic_Ne_From_Known_Offspring_Given_Parental_Sex_Ne(self, floatNeBySex_Male_Nem, floatNeBySex_Female_Nef):

                '''
                Calculate Demographic Ne from the Parental Ne for each sex
                E.G. :

                Nf = Number of female parents
                Mean(Kf) = Mean litter size for Females after a specific breeding event 
                Var(Kf) = Variance in litter size (reproductive success) for Females after a specific breeding event 

                Ne = (4.Nef.Nem) / (Nef + Nem)

                '''
                #Part 1: (4.Nef.Nem)
                floatPart1 = 4 * floatNeBySex_Male_Nem * floatNeBySex_Female_Nef

                #Part 2: (Nef + Nem)
                floatPart2 =  floatNeBySex_Male_Nem + floatNeBySex_Female_Nef

                #Part 3: Part1 / Part 2
                if floatPart2 > 0:
                    floatNeDemographicFromKnownOffspring =  floatPart1 / floatPart2
                else:
                    #Produce error without causing a division by zero crash
                    floatNeDemographicFromKnownOffspring = gint_Large_Undefined_Number #99999999999999999999999999.99

                return floatNeDemographicFromKnownOffspring

            def method_Get_Distribution__NORMAL(self, float_Mean, float_Standard_Deviation, int_Samples):
                
                mu, sigma = float_Mean, float_Standard_Deviation
                
                #mu, sigma = 0, 0.1 # mean and standard deviation
                s = numpy__random.normal(float_Mean, float_Standard_Deviation, int_Samples)

                #DEBUG_ON
                import matplotlib.pyplot as plt
                import numpy as np
                count, bins, ignored = plt.hist(s, 30, normed=True) 
                plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                         np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
                         linewidth=2, color='r')
                plt.show()                
                #DEBUG_OFF
                               
                return s

            def method_Get_Distribution__BINOMIAL(self, float_Probability, int_Trials, int_Tests, bool_Allow_Zeros):
                
                p, n, t = float_Probability, int_Trials, int_Tests # probability of each trial, number of trials, number of tests per trial
                
                if bool_Allow_Zeros:
                    #DEBUG_ON
                    #t = 10000
                    #DEBUG_OFF
                    numpy_array_Draws = numpy__random.binomial(n, p, t)
                else:
                    #numpy_array_Draws = numpy__array([])
                    list_Draws = []
                    #DEBUG_ON
                    #t = 10000
                    #DEBUG_OFF
                    int_Trial_Count = 0
                    int_Zero_Count = 0
                    while True:
                    #for int_Trial in range(1, t+1):
                        numpy_array_Draws = numpy__random.binomial(n, p, 1)
                        int_Draw = numpy_array_Draws[0]
                        if int_Draw > 0:
                            int_Trial_Count += 1 
                            list_Draws.append(numpy_array_Draws[0])
                            if int_Trial_Count == t:
                                break
                            pass
                        else:
                            int_Zero_Count += 1
                        pass
                    pass
                    numpy_array_Draws = numpy__array(list_Draws)
                    #DEBUG_ON
                    #self.obj_Log_Default_Display.info('method_Get_Distribution__BINOMIAL - ' + '; Total trials: ' + str(len(numpy_array_Draws)) + '; after Zeros excluded and resampled: ' + str(int_Zero_Count)) 
                    self.obj_Log_Debug_Display.debug('method_Get_Distribution__BINOMIAL - ' + '; Total trials: ' + str(len(numpy_array_Draws)) + '; after Zeros excluded and resampled: ' + str(int_Zero_Count))
                    #DEBUG_OFF

                pass
            
                #DEBUG_ON
                #s = numpy_array_Draws
                #import matplotlib.pyplot as plt
                #import numpy as np
                #count, bins, ignored = plt.hist(s, 30, normed=True) 
                #plt.show()
                #DEBUG_OFF
                
                if bool_Allow_Zeros == False:                
                    list_Zeros = [x for x in numpy_array_Draws if x == 0 ]
                    if len(list_Zeros) > 0:
                        with Debug_Location() as obj_DebugLoc:
                            str_Message_Location = obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                        pass
                        str_Message = str_Message_Location + ' >> BINOMIAL Distribution has Zeros: ' + str(len(list_Zeros))
                        self.obj_Log_Default_Display.error(str_Message)
                        raise ValueError(str_Message)
                    pass                  
                pass
                               
                return numpy_array_Draws
            
            def method_Get_Distribution__TRUNCATED_NORMAL(self, float_Mean, float_Standard_Deviation, float_Minimum, float_Maximum, int_Samples):

                mu, sigma, lower, upper = float_Mean, float_Standard_Deviation, float_Minimum, float_Maximum
                X = scipy__stats.truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)                
                
                s=None
                return s


            def func_Get_Float_Reciprocal_With_Same_Decimal_Places(self, float_Orig):
                
                str_Float_Decimals = str(float_Orig).split('.')[1]
                int_Len_Float_Decimals = len(str_Float_Decimals)
                float_Reciprocal = round(float(1) - float_Orig, int_Len_Float_Decimals)
                               
                return float_Reciprocal
                         
            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.analysisOperation_obj = AnalysisOperation() 
        return self.analysisOperation_obj
 
    def __exit__(self, type, value, traceback): 
        self.analysisOperation_obj.classCleanUp()
