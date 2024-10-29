'''
Created on 29 Jan 2015

@author: dblowe
'''
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS
#
#------------------< Import python modules
# DEBUG Imports
# from logging import getLogger as logging__getLogger
# from handler_Debug import Timer2
# from handler_Debug import Debug_Location
#
from collections import OrderedDict
 
#------------------< Import DCB_General modules
# from FileHandler import FileHandler
# from handler_Logging import Logging
#------------------< Import SharkSim modules
#from globals_SharkSim import globalsSS
from object_SSConfigFiles import object_SSConfigFiles
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
class object_SSConfigProjects(object_SSConfigFiles):

    '''
    --------------------------------------------------------------------------------------------------------
    # <<<<<<<<<<<<<<<<<< CLASS INIT
    --------------------------------------------------------------------------------------------------------
    '''   

    __slots__ = (
                #PROPERTIES
                #'obj_SSParams'                
                #VARIABLES
                #,'str_Project_Name'
                )

    static_str_Section__INI_File = 'INI_File'
    static_str_Option__INI_Filename = 'INI_Filename'
    static_str_Value__INI_Filename = 'PROJECTS'
    static_str_Option__INI_Creation_Run_ID = 'INI_Creation_Run_ID'
    static_str_Option__INI_UID = 'INI_UID'
    
#     static_str_Section__Projects_Details = 'Projects_Details'
#     static_str_Option__Projects_Name = 'Projects_Name'
#     
    static_str_Section__Project_File_List = 'Project_File_List'
    static_str_Option__Project_File = 'Project_File'

    static_str_Section__Project_Name_List = 'Project_Name_List'
    static_str_Option__Project_Name = 'Project_Name'


    def __enter__(self):
        
        return self 
    
    def __init__(self):

        return None         

    '''
    --------------------------------------------------------------------------------------------------------
    # <<<<<<<<<<<<<<<<<< CLASS FINALIZATION
    --------------------------------------------------------------------------------------------------------
    '''       
    def __exit__(self, type, value, traceback):
         
        pass
        