#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
#from simuPOP
#import simuPOP as sim
from AutoVivificationHandler import AutoVivificationHandler
#from OutputHandler

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
#from collections import defaultdict

class object_SSBatch:
    """Contains SS Batc level properties and methods"""
    def __enter__(self):

        class obj_SSBatch():

# -------------- Class specific routines

            __slots__ = ('stringDelimiter'
                         ,'stringDelimiter2'
                         ,'objSSParametersLocal'
                         ,'intLevel'
                         ,'dictDataSectionNotesLevels'
                         ,'dict_ReplicateBatches'
                         ,'dict_CurrentReplicateBatch'
                        )

            def __init__(self):
                
                self.stringDelimiter = ';'
                self.stringDelimiter2 = ','

                self.objSSParametersLocal = None

                self.intLevel = 2
                
                self.dictDataSectionNotesLevels = AutoVivificationHandler()

                self.dict_ReplicateBatches = {}

                self.dict_CurrentReplicateBatch = {}

            def method_PopulateProperties(self):
                    
                
                self.dictDataSectionNotesLevels[self.intLevel]['Data_Section_Note_' + str(self.intLevel)] = 'Batch_Level_Params'
                
                self.dict_ReplicateBatches['Replicate_Batches'] = self.objSSParametersLocal.intReplicateBatches
                    
                self.dict_CurrentReplicateBatch['Current_Replicate_Batch'] = self.objSSParametersLocal.intCurrentReplicateBatch
                                    
                pass


# -------------- Class specific routines

            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.class_obj_SSBatch = obj_SSBatch() 
        return self.class_obj_SSBatch
 
    def __exit__(self, type, value, traceback): 
        self.class_obj_SSBatch.classCleanUp()