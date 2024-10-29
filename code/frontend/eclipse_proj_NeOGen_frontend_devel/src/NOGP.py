'''
-----------------------------------------------
                FUTURE PYTHON COMPATIBILITY
-----------------------------------------------
'''
#------------------< Import future python modules
from __future__ import print_function

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
    
'''
-----------------------------------------------
                CPU AFFINITY
-----------------------------------------------
'''
#------------------< Import external modules
from psutil import Process as psutil__Process
from multiprocessing import cpu_count as multiprocessing__cpu_count
from os import getpid as os__getpid

'''
-----------------------------------------------
                PATH INFO
-----------------------------------------------
'''
#------------------< Import external modules
import sys, getopt
from sys import path as sys__path

''' Display the CPUs '''
int_CPUs_Available_Count = multiprocessing__cpu_count()
print('\nAvailable CPUs: ' + str(int_CPUs_Available_Count))
'''
-----------------------------------------------
                PLATFORM
-----------------------------------------------
'''
from sys import platform as sys__platform
import platform
from os import name as os__name
from os import path as os__path

str_OS_Platform = sys__platform
str_OS_Dist_Name, str_OS_Dist_Ver_Desc_1, str_OS_Dist_Ver_Desc_2 = platform.dist()
str_OS_Dist_Release = platform.release()
''' Display the platform '''
print('\nOS Platform:'+ str_OS_Platform)
print('OS System:'+ str(platform.system()))
print('OS Release:'+ str(platform.release()))
print('OS Distribution:'+ str(platform.dist()))
print('OS Name:'+ str(os__name))

''' Display the python version '''
str_Py_Ver = '.'.join(str(sys.version_info[x]) for x in range(0, len(sys.version_info)-1))
print('\nPython Version: ' + str_Py_Ver)

''' Set the environment paths '''
bool_Paths_Display = True
if bool_Paths_Display:
    print('-------------------------------------------------')
    print('System Paths')
    print('-------------------------------------------------')
    for strPath in sys__path:
        print(strPath)
    pass

    bool_Add_HC_Paths = True
    if bool_Add_HC_Paths:
        list_HC_Paths = []
        if str_OS_Platform.startswith('linux') and str_OS_Dist_Name.startswith('centos'):
            # linux
#             list_HC_Paths.append('/home/uqdblowe/TremlLab/CRAmodel/RS_CODE/devel/proj/proj_Py3_Coral_Adaptive_Migrator/proj_Py3_Coral_Adaptive_Migrator_v1_0_0_Py27')
#             list_HC_Paths.append('/home/uqdblowe/TremlLab/CRAmodel/RS_CODE/devel/proj/proj_Py3_Lib_General/proj_Py3_Lib_General_v1_0_0')
#             list_HC_Paths.append('/home/uqdblowe/TremlLab/CRAmodel/RS_CODE/devel/proj/proj_Py3_Lib_Simupop/proj_Py3_Lib_Simupop_v1_0_0')
            pass
        if str_OS_Platform.startswith('linux') and str_OS_Dist_Name.startswith('debian'):
            # linux
#             list_HC_Paths.append('/home/ubuntu/coding/devel/eclipse/proj/proj_Py3_Coral_Adaptive_Migrator/proj_Py3_Coral_Adaptive_Migrator_v1_0_0_Py27')
#             list_HC_Paths.append('/home/ubuntu/coding/devel/eclipse/proj/proj_Py3_Lib_General/proj_Py3_Lib_General_v1_0_0')
#             list_HC_Paths.append('/home/ubuntu/coding/devel/eclipse/proj/proj_Py3_Lib_Simupop/proj_Py3_Lib_Simupop_v1_0_0')
            pass
        elif str_OS_Platform.startswith('win') and str_OS_Dist_Release.startswith('2012ServerR2'):
            # Windows...
#             list_HC_Paths.append('C:\\TremlLab\\CRAmodel\\RS_CODE\\devel\\proj\\proj_Py3_Coral_Adaptive_Migrator\\proj_Py3_Coral_Adaptive_Migrator_v1_0_0_Py27')
#             list_HC_Paths.append('C:\\TremlLab\\CRAmodel\\RS_CODE\\devel\\proj\\proj_Py3_Lib_General\\proj_Py3_Lib_General_v1_0_0')
#             list_HC_Paths.append('C:\\TremlLab\\CRAmodel\\RS_CODE\\devel\\proj\\proj_Py3_Lib_Simupop\\proj_Py3_Lib_Simupop_v1_0_0')
            pass                        
        elif str_OS_Platform.startswith('win'):
            # Windows...

            bool_Insert = False
            if bool_Insert:
                list_HC_Paths.insert(0, app_details.str_Runtime_Referenced_Project_1) #equivalent to... sys__path.insert(0, str_Runtime_Referenced_Project_1)
                list_HC_Paths.insert(1, app_details.str_Runtime_Referenced_Project_2) #equivalent to... sys__path.insert(0, str_Runtime_Referenced_Project_1)
                pass
            else:
                list_HC_Paths.append(app_details.str_Runtime_Referenced_Project_1) #equivalent to... sys__path.append(str_Runtime_Referenced_Project_1)
                list_HC_Paths.append(app_details.str_Runtime_Referenced_Project_2) #equivalent to... sys__path.append(str_Runtime_Referenced_Project_1)
                pass
            pass
            
            pass                
        elif str_OS_Platform.startswith('darwin'):
            # OS X
            pass
        pass
    
        for str_Path in list_HC_Paths:
            bool_Insert = False
            if bool_Insert:
                sys__path.insert(0,str_Path)
            else:
                sys__path.append(str_Path)
            pass 
        pass
    
        if len(list_HC_Paths) > 0: 
            print('-------------------------------------------------')
            print('SYSTEM PATHS UPDATED')
            print('-------------------------------------------------')
            for strPath in sys__path:
                print(strPath)
            pass        
            print('-------------------------------------------------!')
        pass
    
        if len(list_HC_Paths) > 0: 
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('REMOVE FOLLOWING HARCODED PATHS for final installation')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            for str_HC_Path in list_HC_Paths:
                print(str(str_HC_Path))
            pass
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        pass
    pass
pass

#------------------< Import python modules
import cProfile
from gc import enable as gc__enable
from gc import get_threshold as gc__get_threshold
from gc import isenabled as gc__isenabled
from os import path as os__path
from os import makedirs as os__makedirs
from os import extsep as os__extsep
from shutil import rmtree as shutil__rmtree
from logging import getLogger as logging__getLogger

#------------------< Import DCB_General modules
from globals_DCB_General import globalsDCBGen
from handler_Logging import Logging

#------------------< Import SharkSim modules
from globals_SharkSimFE import globalsSSFE
from SSFERunHandler import SSFERunOperation

static_str_App_Started_From_IDE = 'IDE'

def func_Initialise(str_App_Arg_Working_Base_Path):
    
    bool_Success = True
    
    '''
    Initialise logging
    '''
    str_File__Log = 'logging.txt'
    str_Path__Log = str_App_Arg_Working_Base_Path
    str_Path_And_File__Log = os__path.join(str_Path__Log, str_File__Log)
    
    try:
        obj_Logging = Logging()
        if globalsDCBGen.Debug.static_global_Debug:
            dict_Default_Logger_Specs = {'':{'Level':'','LogToConsole':True,'LogToFile':True}
                                     ,'app_debug':{'Level':'debug','LogToConsole':True,'LogToFile':True}}
        else:
            dict_Default_Logger_Specs = {'':{'Level':'','LogToConsole':True,'LogToFile':False}
                                     ,'app_debug':{'Level':'debug','LogToConsole':False,'LogToFile':False}}
        pass
        obj_Logging.strLogFile = str_File__Log
        obj_Logging.strLogPath = str_Path__Log
        obj_Logging.dict_Default_Logger_Specs = dict_Default_Logger_Specs
        obj_Logging.func_Initialise_Default_Loggers()
        obj_Log = logging__getLogger(__name__)
        if obj_Log != None:
            bool_Success = True
        else:
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> Unexpected Error. Logging could not be initiated: ' + str_Path_And_File__Log)
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__Caught_Error)
        pass
    except Exception, error:
        str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
        print(str_Message_Header)
        print('>> UNCAUGHT EXCEPTION. Logging could not be initiated: ' + str_Path_And_File__Log)
        print('>> Command Line Error >> UNEXPECTED ERROR: ' + error.__doc__)
        print('>> Command Line Error >> UNEXPECTED ERROR: ' +  error.message) 
        print('>> Run Terminated.')
        str_Message_Footer = '-'*(len(str_Message_Header)-1)
        print(str_Message_Footer)
        raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)
    pass              

    #DEBUG_ON
    #import cProfile

#     turnOnDebug(code="")
# 
#     Details:
# 
#         Set debug code code. More than one code could be specified using a
#         comma separated string. Name of available codes are available from
#         moduleInfo()['debug'].keys().    

    #cProfile.run('main_run()','SharkSim_CProfile.profile')
    #DEBUG_OFF
    
    bool_Success = False
    '''
    Enable python automatic garbage collection
    '''
    try:
        gc__enable()
        bool_Success = True
    except Exception, error:
        str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
        print(str_Message_Header)
        print('>> UNCAUGHT EXCEPTION. Garbage collection could not be initiated')
        print('>> Command Line Error >> UNEXPECTED ERROR: ' + error.__doc__)
        print('>> Command Line Error >> UNEXPECTED ERROR: ' +  error.message) 
        print('>> Run Terminated.')
        str_Message_Footer = '-'*(len(str_Message_Header)-1)
        print(str_Message_Footer)
        raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)
    pass              

    obj_Log.info("Garbage collection thresholds: " + str(gc__get_threshold()))
    obj_Log.info("Garbage collection is enabled: " + str(gc__isenabled()))

    return bool_Success

def func_Get_Command_Line_Arguments(list_Command_Line_Arguments):
    
    str_App_Run_Path_And_File = ''
    str_App_Run_Path = ''
    str_App_Run_File = ''
    str_App_Arg_Working_Base_Path = ''
    bool_App_Arg_Debug_Logging = False
    str_App_Arg_Devel_Folder = ''
    bool_App_Arg_Devel_Mode = False
    bool_App_Arg_Devel_Uses_Sync_Folders = False
    list_int_App_Arg_Run_Processing_Steps = []

    try:
        str_App_Main_Path_And_File = os__path.abspath(__file__)
    except NameError:  # We are the main py2exe script, not a module
        str_App_Main_Path_And_File = os__path.abspath(sys.argv[0])    
    pass
 
    str_App_Main_Path, str_App_Main_File = os__path.split(str_App_Main_Path_And_File)
    
    try:
        opts, args = getopt.getopt(list_Command_Line_Arguments,'s:w:h:v:dl:dmf:dus',['settings_path=','work_path=', 'help', 'version', 'debug_logging', 'devel_mode_and_folder=', 'devel_uses_sync_folders'])
    except getopt.GetoptError:
        str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
        print(str_Message_Header)
        print('>> Command Line Error >> Unexpected Option and/or Arguments --> ' + str(list_Command_Line_Arguments))
        print('>> Please use the following -options and <arguments>:')
        print(str_App_Run_File + ' --help --version --work_path=<projects_config_files_path>')
        print('>> or... ')
        print(str_App_Run_File + ' -h -v -w <projects_config_files_path>')
        print('>> Run Terminated.')
        str_Message_Footer = '-'*(len(str_Message_Header)-1)
        print(str_Message_Footer)
        raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)
    pass

    if ("-s", "--settings_path") in opts:
        ''' Get the arg along with the other args '''
        pass
    else:
        ''' Assume the settings.ini is in the same folder as this file (either .py or .exe) '''
        str_App_Run_Path_And_File  = os__path.join(str_App_Main_Path, 'settings.ini')
    pass

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> Please use the following -options and <arguments>:')
            print(str_App_Run_File + ' --help --version --work_path=<projects_config_files_path>')
            print('>> or... ')
            print(str_App_Run_File + ' -h -v -w <projects_config_files_path>')
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Completion__Premature)
        elif opt in ('-v', '--version'):
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> PROGRAM: ' + str(app_details.__project__)) 
            print('>> VERSION: ' + str(app_details.__version__)) 
            print('>> DATE RELEASED: ' + str(app_details.__date__)) 
            print('>> AUTHOR: ' + str(app_details.__author__))
            print('>> COPYRIGHT: ' + str(app_details.__copyright__)) 
            print('>> LICENSE: ' + str(app_details.__license__))
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Completion__Premature)
        elif opt in ('-dl', '--debug_logging'):
            bool_App_Arg_Debug_Logging = True
        elif opt in ("-s", "--settings_path"):
            
            ''' Check if arg is empty '''
            if not arg == "": 
                str_App_Run_Path_And_File = arg
            else:
                ''' Otherwise assume that the path where the app was executed is also the settings path '''
                try:
                    str_App_Run_Path_And_File = os__path.abspath(__file__)
                except NameError:  # We are the main py2exe script, not a module
                    str_App_Run_Path_And_File = os__path.abspath(sys.argv[0])    
                pass
        
            str_App_Run_Path, str_App_Run_File = os__path.split(str_App_Run_Path_And_File)            
            
            if ':' not in str_App_Run_Path:
                str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                print(str_Message_Header)
                print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                print('>> Command Line Error >> Invalid path.  No drive specified.  Please check. Invalid argument --> ' + str(opt) + ' ' + str(arg))
                print('>> Run Terminated.')
                str_Message_Footer = '-'*(len(str_Message_Header)-1)
                print(str_Message_Footer)
                raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)
            else:
                try:
                    if not os__path.exists(str_App_Run_Path):
                        str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                        print(str_Message_Header)
                        print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                        print('>> Command Line Error >> Path does not exist.  Please check. Invalid argument --> ' + str(opt) + ' ' + str(arg))
                        print('>> Run Terminated.')
                        str_Message_Footer = '-'*(len(str_Message_Header)-1)
                        print(str_Message_Footer)
                        raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)
                    pass
                except Exception, error:
                    str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                    print(str_Message_Header)
                    print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                    print('>> Command Line Error >> UNEXPECTED ERROR: ' + error.__doc__)
                    print('>> Command Line Error >> UNEXPECTED ERROR: ' +  error.message) 
                    print('>> Run Terminated.')
                    str_Message_Footer = '-'*(len(str_Message_Header)-1)
                    print(str_Message_Footer)
                    raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)
                pass
            pass                
        elif opt in ("-w", "--work_path"):
            str_App_Arg_Working_Base_Path = arg
            if ':' not in str_App_Arg_Working_Base_Path:
                str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                print(str_Message_Header)
                print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                print('>> Command Line Error >> Invalid path.  No drive specified.  Please check. Invalid argument --> ' + str(opt) + ' ' + str(arg))
                print('>> Run Terminated.')
                str_Message_Footer = '-'*(len(str_Message_Header)-1)
                print(str_Message_Footer)
                raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)
            else:
                try:
                    if not os__path.exists(str_App_Arg_Working_Base_Path):
                        str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                        print(str_Message_Header)
                        print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                        print('>> Command Line Error >> Path does not exist.  Please check. Invalid argument --> ' + str(opt) + ' ' + str(arg))
                        print('>> Run Terminated.')
                        str_Message_Footer = '-'*(len(str_Message_Header)-1)
                        print(str_Message_Footer)
                        raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)
                    pass
                except Exception, error:
                    str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                    print(str_Message_Header)
                    print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                    print('>> Command Line Error >> UNEXPECTED ERROR: ' + error.__doc__)
                    print('>> Command Line Error >> UNEXPECTED ERROR: ' +  error.message) 
                    print('>> Run Terminated.')
                    str_Message_Footer = '-'*(len(str_Message_Header)-1)
                    print(str_Message_Footer)
                    raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)
                pass
            pass                
        elif opt in ("-dmf", "--devel_mode_and_folder"):
            
            str_App_Arg_Devel_Folder = arg
            
            if not str_App_Arg_Devel_Folder == '':
                bool_App_Arg_Devel_Mode = True
            pass
        elif opt in ("-dus", "--devel_uses_sync_folders"):
            
            bool_App_Arg_Devel_Uses_Sync_Folders = True
            
            ''' NOTE: Also need the devel_run_folder for this option'''
            pass                
        else:
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
            print('>> Command Line Error >> Unexpected Option and/or Arguments --> ' + str(opts) + ' ' + str(args))
            print('>> Please use the following -options and <arguments>:')
            print(str_App_Run_File + ' --help --version --work_path=<projects_config_files_path>')
            print('>> or... ')
            print(str_App_Run_File + ' -h -v -w <projects_config_files_path>')
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globalsDCBGen.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)
        pass
    pass
    
    str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
    print(str_Message_Header)
    print('>> Me: ' + str_App_Main_Path_And_File)
    print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
    print('>> Settings_Path: ' + str_App_Run_Path_And_File)
    print('>> Working_Path: ' + str_App_Arg_Working_Base_Path)
    print('>> Debug_Logging: ' + str(bool_App_Arg_Debug_Logging))
    print('>> Devel_Mode: ' + str(bool_App_Arg_Devel_Mode))
    if bool_App_Arg_Devel_Mode:
        print('>> Devel_Folder: ' + str(str_App_Arg_Devel_Folder))
        print('>> Devel_Uses_Sync_Folders: ' + str(bool_App_Arg_Devel_Uses_Sync_Folders))
    pass
    print('>> Run proceeding...')
    str_Message_Footer = '-'*(len(str_Message_Header)-1)
    print(str_Message_Footer)
    
    return str_App_Run_Path_And_File, str_App_Arg_Working_Base_Path, bool_App_Arg_Debug_Logging, bool_App_Arg_Devel_Mode, str_App_Arg_Devel_Folder, bool_App_Arg_Devel_Uses_Sync_Folders
  
def func_Main(list_Command_Line_Arguments): 

    str_App_Run_Path_And_File = ''
    str_App_Arg_Working_Base_Path = ''
    bool_App_Arg_Debug_Logging = False
    bool_App_Arg_Devel_Mode = False
    str_App_Arg_Devel_Folder = ''
    bool_App_Arg_Devel_Uses_Sync_Folders = False
    
    ''' Validate and retrieve the arguments '''
    str_App_Run_Path_And_File \
    , str_App_Arg_Working_Base_Path \
    , bool_App_Arg_Debug_Logging \
    , bool_App_Arg_Devel_Mode \
    , str_App_Arg_Devel_Folder \
    , bool_App_Arg_Devel_Uses_Sync_Folders \
    = func_Get_Command_Line_Arguments(list_Command_Line_Arguments)
    
    ''' 
    Start Run processing
    '''
    with SSFERunOperation(str_App_Run_Path_And_File, str_App_Arg_Working_Base_Path, bool_App_Arg_Debug_Logging, bool_App_Arg_Devel_Mode, str_App_Arg_Devel_Folder, bool_App_Arg_Devel_Uses_Sync_Folders) as obj_SSRun:
        obj_SSRun.func_Run_Start()
    pass

    #DEBUG_ON
    #input("\n Press return to close this window... \n")
    #DEBUG_OFF
    
    return True    
'''
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
MAIN       
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
'''
if __name__ == '__main__':

    func_Main(sys.argv[1:])    
