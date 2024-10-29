#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
#from simuPOP
#import simuPOP as sim
from AutoVivificationHandler import AutoVivificationHandler
#from OutputHandler

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
#from collections import defaultdict

class object_SSReplicate:
    """Contains SS Simulation level properties and methods"""
    def __enter__(self):

        class obj_SSReplicate():

# -------------- Class specific routines

            __slots__ = ('stringDelimiter'
                         ,'stringDelimiter2'
                         ,'objSSParametersLocal'
                         ,'intLevel'
                         ,'dictDataSectionNotesLevels'
                         ,'dict_Replicates'
                         ,'dict_CurrentReplicate'
                        )

            def __init__(self):
                
                self.stringDelimiter = ';'
                self.stringDelimiter2 = ','

                self.objSSParametersLocal = None

                self.intLevel = 3
                
                self.dictDataSectionNotesLevels = AutoVivificationHandler()

                self.dict_Replicates = {}

                self.dict_CurrentReplicate = {}

            def method_PopulateProperties(self):
                    
                
                self.dictDataSectionNotesLevels[self.intLevel]['Data_Section_Note_' + str(self.intLevel)] = 'Rep_Level_Params'
                
                self.dict_Replicates['Replicates'] = self.objSSParametersLocal.intReplicates
                    
                self.dict_CurrentReplicate['Current_Replicate'] = self.objSSParametersLocal.intCurrentReplicate
                                    
                pass


# -------------- Class specific routines

            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.class_obj_SSReplicate = obj_SSReplicate() 
        return self.class_obj_SSReplicate
 
    def __exit__(self, type, value, traceback): 
        self.class_obj_SSReplicate.classCleanUp()