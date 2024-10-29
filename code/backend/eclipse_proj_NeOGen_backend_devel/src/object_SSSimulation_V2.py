#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
from collections import OrderedDict

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
from globals_SharkSim import globalsSS
from AutoVivificationHandler import AutoVivificationHandler
from OutputHandler import OutputHandler
from SSAnalysisHandler import SSAnalysisHandler


class object_SSSimulation_V2:
    """Contains SS Simulation level properties and methods"""
    def __enter__(self):

        class obj_SSSimulation_V2():

# -------------- Class specific routines

            __slots__ =('stringDelimiter'
                        ,'stringDelimiter2'
                        ,'objSSParametersLocal'
                        ,'intNum_DICT_PROPERTIES_ToReport'                        
                        ,'intLevel'
                        ,'str_Current_Col_Index'
                        
                        #Reporting vars
                        ,'dict_Rep_1_DataSectionNotesLevels'
                        
                        ,'dict_Rep_20_FilenameEmbeddedFields'
                        ,'dict_Rep_30_SingleRun'
                        ,'dict_Rep_40_BatchRunStart'
                        ,'dict_Rep_45_ReplicateRunStart'
                        ,'dict_Rep_50_strUniqueRunID'
                        ,'dict_Rep_60_SimCurrentBatch'
                        ,'dict_Rep_70_SimCurrentReplicate'
                        
                        ,'dict_ReportingPropertyObjects'
                       )

            def __init__(self):
                
                self.stringDelimiter = globalsSS.StringDelimiters.static_stringDelimiter_SEMI_COLON
                self.stringDelimiter2 = globalsSS.StringDelimiters.static_stringDelimiter_COMMA
                self.str_ID_Suf = globalsSS.StringDelimiters.static_stringDelimiter_SPACE

                self.objSSParametersLocal = None
                self.intLevel = 1

                self.str_Current_Col_Index = str(
                                                 str(self.intLevel) +
                                                 globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                                 '0' +
                                                 globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                                 '0' +
                                                 globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                                 '0')
                                                
                #self.dict_Rep_1_DataSectionNotesLevels = AutoVivificationHandler()
                self.dict_Rep_1_DataSectionNotesLevels = {}
                
                self.dict_Rep_20_FilenameEmbeddedFields = {}
                self.dict_Rep_30_SingleRun = {}
                self.dict_Rep_40_BatchRunStart = {}
                self.dict_Rep_45_ReplicateRunStart = {}
                self.dict_Rep_50_strUniqueRunID = {}
                self.dict_Rep_60_SimCurrentBatch = {}
                self.dict_Rep_70_SimCurrentReplicate = {}

                self.dict_ReportingPropertyObjects = OrderedDict()

                return None
            
            def method_PopulateProperties(self):

                ''' DICT PROPERTIES
                    these are defined by:
                    _Rep_ in the property name
                    _Rep_x where x is an integer describing the order the property is reported
                '''
                #self.dict_Rep_1_DataSectionNotesLevels[self.intLevel]['Data_Section_Note_' + str(self.intLevel)] = 'Sim_Level_Params'
                self.dict_Rep_1_DataSectionNotesLevels[self.Get_Log_Current_Column_Index(True, True, self.str_ID_Suf) + 'Data_Section_Note_' + str(self.intLevel)] = 'Sim_Level_Params'
                self.dict_Rep_20_FilenameEmbeddedFields[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Filename_Embedded_Fields'] = self.objSSParametersLocal.strFilenameEmbeddedFields
                self.dict_Rep_30_SingleRun[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Single_Run'] = self.objSSParametersLocal.boolSingleRun
                self.dict_Rep_40_BatchRunStart[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Batch_Run_Started_Y_m_d_H_M_S'] = self.objSSParametersLocal.dateBatchRunStartTime.strftime("%Y_%m_%d_%H_%M_%S")
                self.dict_Rep_45_ReplicateRunStart[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Replicate_Run_Started_Y_m_d_H_M_S'] = self.objSSParametersLocal.dateReplicateRunStartTime.strftime("%Y_%m_%d_%H_%M_%S")
                self.dict_Rep_50_strUniqueRunID[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Unique_Run_ID'] = self.objSSParametersLocal.strUniqueRunID
                self.dict_Rep_60_SimCurrentBatch[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Sim_Current_Batch'] = self.objSSParametersLocal.intCurrentBatch
                self.dict_Rep_70_SimCurrentReplicate[self.Get_Log_Current_Column_Index(False, True, self.str_ID_Suf) + 'Sim_Current_Replicate'] = self.objSSParametersLocal.intCurrentReplicate
                   
                return True

            def Get_Log_Current_Column_Index(self, bool_Reset, bool_Add_Suffix = False, str_Suffix = ''):
                
                if bool_Reset:
                    self.str_Current_Col_Index = str(
                                                     str(self.intLevel) +
                                                     globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                                     '0' +
                                                     globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                                     '0' +
                                                     globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                                     '0')
                else:
                    L, h, i, j = self.str_Current_Col_Index.split(globalsSS.StringDelimiters.static_stringDelimiter_DOT)
                    
                    h = int(h)
                    i = int(i)
                    j = int(j)
                    
                    j += 1
                    
                    '''Get column numbering'''
                    if j == 10:
                        j = 0
                        i += 1
                        if i == 10:
                            i = 0
                            h += 1
                            if h == 10:
                                self.obj_Log_Default.warn('Column index number has exceeded its max number 9.9.9. Dataframes will not be in the correct column order')
                        pass
                    pass
                    
                    self.str_Current_Col_Index = str(
                                        str(self.intLevel) +
                                        globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                        str(h) +
                                        globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                        str(i) +
                                        globalsSS.StringDelimiters.static_stringDelimiter_DOT +
                                        str(j))
                    
                pass

                if bool_Add_Suffix:
                    self.str_Current_Col_Index = self.str_Current_Col_Index + str(str_Suffix)
                pass
            
                return self.str_Current_Col_Index
        

# -------------- Class specific routines

            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.class_obj_SSSimulation_V2 = obj_SSSimulation_V2() 
        return self.class_obj_SSSimulation_V2
 
    def __exit__(self, type, value, traceback): 
        self.class_obj_SSSimulation_V2.classCleanUp()