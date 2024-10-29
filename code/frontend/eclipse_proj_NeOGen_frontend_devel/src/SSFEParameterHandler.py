'''
-----------------------------------------------
                FUTURE PYTHON COMPATIBILITY
-----------------------------------------------
'''
#------------------< Import future python modules
#from __future__ import print_function

'''
-----------------------------------------------
                MODULE NOTES
-----------------------------------------------
'''
'''
Created on 25/01/2016

@author: Dean
'''
'''
-----------------------------------------------
                RELEASE INFO
-----------------------------------------------
'''
#------------------------------------< Import app details modules
from version import version as app_details
''' Display app version details '''
print('\nProject: '+ str(app_details.__project__))
print('Author: '+ str(app_details.__author__))
print('Version: '+ str(app_details.__version__))
print('Date: '+ str(app_details.__date__))
print('Copyright: '+ str(app_details.__copyright__))
print('License: '+ str(app_details.__license__))

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS
#
#------------------< Import python modules
from os import path as os__path
#
#------------------< Import DCB_General modules
from FileHandler import FileHandler
#------------------< Import SharkSimFE modules
#


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
class SSFEParameters(object) :

    def __enter__(self):
        
        return self

    def __init__(self):

        self.func_Class_Variable_Specification()

        return None         

    def func_Class_Variable_Specification(self):
        
        self.str_App_Run_Path = ''
        self.str_App_Run_File = ''
        self.str_App_Arg_Working_Base_Path = ''
        self.bool_App_Arg_Debug_Logging = False
        self.bool_App_Arg_Devel_Mode = False
        self.str_App_Arg_Devel_Folder = ''
        self.bool_App_Arg_Devel_Uses_Sync_Folders = False
        
        self.str_Application_Settings_Path_And_File = ''   
             
        return True
    
    '''
    --------------------------------------------------------------------------------------------------------
    Pre-run processing
    --------------------------------------------------------------------------------------------------------
    '''
    
    def func_Run_Pre_Processing__Application_Specs(self):

        ''' Application Version '''
        self.str_App_Version = '_'.join(app_details.__version__.split('.'))

        ''' Program Short Prefix '''
        self.strFileNameProgramPrefix = app_details.str_Project__Prefix + '_' + self.str_App_Version + '_'
        
        ''' Unique Run ID '''
        self.str_INI_UID_DateTime_Stamp = str(self.dateSimRunStartTime.strftime("%Y%m%d%H%M%S"))
            
        ''' APPLICATION Base path '''
        self.str_App_Base_Path = self.str_App_Run_Path
        
        ''' APPLICATION SETTINGS Path & File '''
        self.str_App_Base_Path_And_File = os__path.join(self.str_App_Base_Path, 'Settings.ini')
        
        ''' APPLICATION Working Path '''
#         str_Run_Folder = app_details.str_Run_Folder
     
#         #str_Root_Drive = 'Q:'
#         str_Root_Folder = 'CODE'
#         str_Sync_Folder = 'RS_SRC' + '__' + app_details.str_Project_Short_Name + '_' + self.str_App_Version + '_' + str_Run_Folder
#         str_Project_Folder = 'proj'
#         str_Project_Language_Code = 'Py'
#         str_Project_Language_Version = '2'
#         str_Project_App_Name = '_'.join(app_details.__project__.split(' '))
#         str_Project_App_Name_And_Version = str_Project_App_Name + '_' + self.str_App_Version  + '_' + str_Run_Folder
#         str_Project_App_Folder = str_Project_Folder + '_' + str_Project_Language_Code + str_Project_Language_Version + '_' + str_Project_App_Name_And_Version
#          
#         #str_Project_Path = os__path.join(str_Root_Folder, app_details.str_Project_Short_Name, self.str_Project_Version, str_Run_Folder, str_Sync_Folder, str_Project_App_Folder)
#         #str_Project_Full_Path = os__path.join(str_Root_Drive, str_Project_Path)
#         

        str_Usr_Path_Root = 'usr'
#         if self.str_App_Arg_Working_Base_Path == '': #Working path was not passed as a command line arg...which is allowed
#             #self.str_Application_Working_Path = self.str_App_Base_Path + '\\' + 'v' + self.str_App_Version
#                         
#             if str_Run_Folder == '':
#                 str_Working_Path_Root = str_Usr_Path_Root
#             else:
#                 str_Working_Path_Root = os__path.join(str_Run_Folder, str_Usr_Path_Root)
#             pass
#         
#             self.str_Application_Working_Path = os__path.join(self.str_App_Base_Path, str_Working_Path_Root)            
#             
#         else:
#             #self.str_Application_Working_Path = self.str_App_Arg_Working_Base_Path + '\\' + 'v' + self.str_App_Version
#             #self.str_Application_Working_Path = os__path.join(self.str_App_Arg_Working_Base_Path, 'usr')
# 
#             self.str_Application_Working_Path = os__path.join(self.str_App_Arg_Working_Base_Path, str_Usr_Path_Root)
#         pass

        if self.str_App_Arg_Working_Base_Path == '': #Working path was not passed as a command line arg...which is allowed
            self.str_Application_Working_Path = os__path.join(self.str_App_Base_Path, str_Usr_Path_Root)
        else:
            self.str_Application_Working_Path = os__path.join(self.str_App_Arg_Working_Base_Path, str_Usr_Path_Root)
        pass
       
        return True
        
    def func_Run_Pre_Processing__Environment_Specs(self):

        ''' Unique Run ID '''
        strSimDateTimeStamp = str(self.dateSimRunStartTime.strftime("%Y_%m_%d_%H_%M_%S"))
        self.strUniqueRunID = self.strFileNameProgramPrefix + 'Run_' + strSimDateTimeStamp

        ''' Current App Run Log path '''
        str_Log_Path = 'logs'
        self.str_Current_App_Run_Log_Path = os__path.join(self.str_Application_Working_Path, str_Log_Path, self.strUniqueRunID)
        
        '''Create Run Folders, if they dont already exist '''
        with FileHandler() as obj_FileHandler:
            #obj_FileHandler.func_Create_Path(self.str_Current_App_Run_Path)
            obj_FileHandler.method_Create_Path(self.str_Current_App_Run_Log_Path)
        pass

#         ''' Set the CPU affinity for the process'''
#         bool_Use_Affinity = False
#         if bool_Use_Affinity:
#             pidLastSpawnedProcess = os__getpid()
#             int_CPUs = multiprocessing__cpu_count()
#             int_CPUs_To_Keep_Free = 2
#             if int_CPUs > int_CPUs_To_Keep_Free: 
#                 int_CPUs_To_Use = int_CPUs - int_CPUs_To_Keep_Free
#                 list_CPUs = [x for x in range(0,int_CPUs_To_Use)]                    
#                 
#                 psutil_Process = psutil__Process(pidLastSpawnedProcess)    
#                 psutil_Process.cpu_affinity(list_CPUs)
#             pass
#         pass
                    
        return True 

    '''
    --------------------------------------------------------------------------------------------------------
    # <<<<<<<<<<<<<<<<<< CLASS FINALIZATION
    --------------------------------------------------------------------------------------------------------
    '''       
    def __exit__(self, type, value, traceback):
         
        pass