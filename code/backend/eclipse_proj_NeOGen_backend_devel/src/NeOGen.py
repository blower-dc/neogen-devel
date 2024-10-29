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
            #str_Project_Version = 'v' + '_'.join(app_details.__version__.split('.'))
            
#             bool_Test = False
#             if bool_Test:
#                 str_Run_Folder = 'test'
#             else:
#                 str_Run_Folder = 'devel'
#             pass
#         
#             str_Root_Drive = 'Q:'
#             str_Root_Folder = 'CODE'
#             str_Sync_Folder = 'RS_SRC' + '__' + app_details.str_Project_Short_Name + '_' + str_Project_Version + '_' + str_Run_Folder
#             str_Project_Folder = 'proj'
#             str_Project_Language_Code = 'Py'
#             str_Project_Language_Version = '2'
#             str_Project_App_Name = '_'.join(app_details.__project__.split(' '))
#             str_Project_App_Name_And_Version = str_Project_App_Name + '_' + str_Project_Version  + '_' + str_Run_Folder
#             str_Project_App_Folder = str_Project_Folder + '_' + str_Project_Language_Code + str_Project_Language_Version + '_' + str_Project_App_Name_And_Version
#             
#             str_Project_Path = os__path.join(str_Root_Folder, app_details.str_Project_Short_Name, str_Project_Version, str_Run_Folder, str_Sync_Folder, str_Project_App_Folder)
#             str_Project_Full_Path = os__path.join(str_Root_Drive, str_Project_Path)
            
            #list_HC_Paths.append('Q:CODE\\GEN\\v1_0_0_0_a1\\devel\\RS_SRC__GEN_v1_0_0_0_a1_devel\\proj_Py2_DCB_General_Resources_v1_0_0_0_a1\\src')
            #list_HC_Paths.append(str_Project_Full_Path)
            
#             list_HC_Paths.append(str_Referenced_Project_1)
#             sys__path.insert(0, str_Referenced_Project_1)
            '''
            PATH ORDER IS IMPORTANT:
            Referenced projects must be inserted into the sys.path.list BEFORE
            the project that calls its modules or else a command line run of .py or .exe
            will result in a fal and a 'ImportError: No module named...' error
            '''
            str_Runtime_Referenced_Project_1 = app_details.str_Runtime_Referenced_Project_1
            list_HC_Paths.insert(0, str_Runtime_Referenced_Project_1) #equivalent to... sys__path.insert(0, str_Runtime_Referenced_Project_1)
            
            #str_Referenced_Project_1 = 'Q:\\CODE\\GEN\\v1_0_0_0_a1\\devel\\RS_SRC__GEN_v1_0_0_0_a1_devel\\proj_Py2_DCB_General_Resources_v1_0_0_0_a1\\src'
            #list_HC_Paths.insert(0, str_Referenced_Project_1) #equivalent to... sys__path.insert(0, str_Referenced_Project_1)
            
            #list_HC_Paths.append('M:\\dcb_projects\\dcb_general_resources')
            
            pass                
        elif str_OS_Platform.startswith('darwin'):
            # OS X
            pass
        pass
    
        for str_Path in list_HC_Paths:
            sys__path.append(str_Path)
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
#DEBUG_ON
#Py3 from builtins import input as builtins__input
#DEBUG_OFF

#------------------< Import DCB_General modules
from globals_DCB_General import globalsDCBGen as globals_GEN
from FileHandler import FileHandler as cls_GEN_File_IO
from handler_Logging import Logging as cls_Logging
#

def func_Initialise(str_App_Arg_Output_Base_Path):
    
    bool_Success = True
    
    '''
    Initialise logging
    '''
    str_File__Log = 'logging.txt'
    str_Path__Log = str_App_Arg_Output_Base_Path
    str_Path_And_File__Log = os__path.join(str_Path__Log, str_File__Log)
    
    try:
        obj_Logging = cls_Logging()
        if globals_GEN.Debug.static_global_Debug:
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
            raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Caught_Error)
        pass
    except Exception as error:
        str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
        print(str_Message_Header)
        print('>> UNCAUGHT EXCEPTION. Logging could not be initiated: ' + str_Path_And_File__Log)
        print('>> Command Line Error >> UNEXPECTED ERROR: ' + error.__doc__)
        print('>> Command Line Error >> UNEXPECTED ERROR: ' +  error.message) 
        print('>> Run Terminated.')
        str_Message_Footer = '-'*(len(str_Message_Header)-1)
        print(str_Message_Footer)
        raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)
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
#
#    cProfile.run('main_run()', app_details.str_Project__Prefix + '_CProfile.profile')
    #DEBUG_OFF
    
    bool_Success = False
    '''
    Enable python automatic garbage collection
    '''
    bool_Enable_Garbage_Collection_Manually = False
    if bool_Enable_Garbage_Collection_Manually:
        try:
            gc__enable()
            bool_Success = True
        except Exception as error:
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> UNCAUGHT EXCEPTION. Garbage collection could not be initiated')
            print('>> Command Line Error >> UNEXPECTED ERROR: ' + error.__doc__)
            print('>> Command Line Error >> UNEXPECTED ERROR: ' +  error.message) 
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)
        pass              
    else:
        bool_Success = True
    pass

    obj_Log.info("Garbage collection thresholds: " + str(gc__get_threshold()))
    obj_Log.info("Garbage collection is enabled: " + str(gc__isenabled()))

    return bool_Success
def func_Initalise_Simupop(list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use):
    
    import simuOpt as simupop_Opt
    
    int_Simupop_Threads = len(list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use)
    # -------------------------- Initialise debug parameters
    # simuOpt DEBUG options
    # debug: DBG_WARNING - show all warning messages.
    # numThreads: threads or cores available for host computer
    # optimised: True - when code is in PROD and runtime is important.  False allows verbose error messages.
    # alleleType: controls the memory usage of allele eg 'short' can only represent 256 states (8 bits per allele: enough for most simulations)
    #               Set alleleType to 'long' for infinate-alleles mutation model.  use 'binary' for SNPs
    # quiet: Suppress banner messages
     
    simupop_Opt.setOptions(debug=[
    #'DBG_ALL'
    ##'DBG_BATCHTESTING',
    ##'DBG_COMPATIBILITY',
    #'DBG_DEVEL',
    ##'DBG_GENERAL',
    #'DBG_INDIVIDUAL',
    ##'DBG_INITIALIZER',
    ##'DBG_INTEROPERABILITY',
    #'DBG_MATING',
    ##'DBG_MIGRATOR',
    ##'DBG_MUTATOR',
    ##'DBG_OPERATOR',
    #'DBG_POPULATION',
    ##'DBG_PROFILE',
    ##'DBG_SELECTOR',
    #'DBG_SIMULATOR',
    ##'DBG_STATOR',
    #'DBG_TAGGER',
    ##'DBG_TRANSMITTER',
    ##'DBG_UTILITY',
    #'DBG_WARNING'
    ]
    ,numThreads=int_Simupop_Threads
    ,optimized=True
    #,alleleType='mutant'
    #,alleleType='binary' 
    ,alleleType='short' 
    #,alleleType='long' 
    #,alleleType='lineage' #Required to get Demographic NE.  alleleType='short' is sufficiant for LDNe
    #, quiet=True
    )  

    pass
    
def func_Set_CPU_Affinity(list_Command_Line_Arguments, list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use):

    if list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use[0] == -1:
        list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use = [] 
        str_App_Arg_Run_CPU_Affinity_CPUs_To_Use = raw_input("\n Enter list of CPUs to use: ")
        #Py3 str_App_Arg_Run_CPU_Affinity_CPUs_To_Use = builtins__input("\n Enter list of CPUs to use: ")
        list_str_App_Arg_Run_CPU_Affinity_CPUs_To_Use = str_App_Arg_Run_CPU_Affinity_CPUs_To_Use.split(',')
        list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use = [int(str_CPU) for str_CPU in list_str_App_Arg_Run_CPU_Affinity_CPUs_To_Use]
    pass

    if list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use[0] == -2:
        ''' If affinity is set to -2 then set the affinity to the available number of cores '''
        int_CPUs_Available_Count = multiprocessing__cpu_count()
        list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use = [x for x in range(0,int_CPUs_Available_Count)] 
    pass

    ''' Set the CPU affinity for the process'''
    if len(list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use) > 0:
        int_CPUs_Requested_Count = len(list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use)
        int_CPUs_Available_Count = multiprocessing__cpu_count()
        
        ''' Check if the number of CPUs requested is valid '''
        if int_CPUs_Requested_Count > int_CPUs_Available_Count:
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
            print('>> Command Line Error >> System CPUs available: ' + str(int_CPUs_Available_Count) + ' Too many CPUs requested: ' + str(int_CPUs_Requested_Count) + ', Revise CPUs requested argument list.')
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)                    
        pass
    
        ''' Check if the CPUs requested are valid '''
        list_CPUs_Available = [x for x in range(0,int_CPUs_Available_Count)]
        bool_CPU_Numbers_Are_Valid = set(list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use).issubset(list_CPUs_Available)
        if not bool_CPU_Numbers_Are_Valid:
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
            print('>> Command Line Error >> System CPUs available: ' + str(list_CPUs_Available) + ' Invalid CPUs requested: ' + str(list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use) + ', Revise CPUs requested argument list.')
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)                    
        pass
    
        ''' Validation passed. Assign CPUs to process '''
        try:
            pidLastSpawnedProcess = os__getpid()
            psutil_Process = psutil__Process(pidLastSpawnedProcess)    
            psutil_Process.cpu_affinity(list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use)
        except Exception as error:
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
            print('>> Command Line Error >> UNEXPECTED ERROR: ' + error.__doc__)
            print('>> Command Line Error >> UNEXPECTED ERROR: ' +  error.message) 
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)
        pass
    pass

    return True, list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use
                
def func_Is_Path_Valid_For_OS_Platform(str_Path):
    
    bool_Success = True
    
    with cls_GEN_File_IO() as obj_GEN_File_IO:
        bool_Success = obj_GEN_File_IO.is_path_exists_or_creatable(str_Path)
    pass

    return bool_Success
    
def func_Get_Command_Line_Arguments(list_Command_Line_Arguments):
    
    str_App_Run_Path_And_File = ''
    str_App_Arg_Output_Base_Path = ''
    str_App_Arg_Config_Path_And_File = ''
    list_int_App_Arg_Run_Processing_Steps = []
    list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use = []

    try:
        str_App_Run_Path_And_File = os__path.abspath(__file__)
    except NameError:  # We are the main py2exe script, not a module
        str_App_Run_Path_And_File = os__path.abspath(sys.argv[0])    
    pass
    
    try:
        opts, args = getopt.getopt(list_Command_Line_Arguments,'i:o:p:c:h:v',['infile=', 'outpath=', 'procstep=', 'cpu_affinity=', 'help','version'])
    except getopt.GetoptError:
        str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
        print(str_Message_Header)
        print('>> Command Line Error >> Unexpected Option and/or Arguments --> ' + str(list_Command_Line_Arguments))
        print('>> Please use the following -options and <arguments>:')
        print('neogen.exe --infile=<batch_scenario_file> --outpath=<output_path> --procstep=<processing_steps_comma_separated>')
        print('>> or... ')
        print('neogen.exe -i <batch_scenario_file> -o <output_path> -p <processing_steps_comma_separated>')
        print('>> Run Terminated.')
        str_Message_Footer = '-'*(len(str_Message_Header)-1)
        print(str_Message_Footer)
        raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)
    pass

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> Please use the following -options and <arguments>:')
            print('neogen.exe --infile=<batch_scenario_file> --outpath=<output_path> --procstep=<processing_steps_comma_separated>')
            print('or... ')
            print('neogen.exe -i <batch_scenario_file> -o <output_path> -p <processing_steps_comma_separated>')
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Completion__Premature)
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
            raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Completion__Premature)
        elif opt in ("-i", "--infile"):
            str_App_Arg_Config_Path_And_File = arg
            if str_OS_Platform.startswith('win') and str_OS_Dist_Release.startswith('2012ServerR2'):
                ''' Valid path check fails on WS2012 ''' 
                bool_Success = True
            else:
                bool_Success = func_Is_Path_Valid_For_OS_Platform(str_App_Arg_Config_Path_And_File)
            pass
        
            if not bool_Success:
                str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                print(str_Message_Header)
                print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                print('>> Command Line Error >> File path invalid for OS platform (' + str_OS_Platform + '). Invalid argument --> ' + str(opt) + ' ' + str(arg))
                print('>> Run Terminated.')
                str_Message_Footer = '-'*(len(str_Message_Header)-1)
                print(str_Message_Footer)
                raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)
                pass                  
            pass
        
            fileHandle = None
            try:
                fileHandle = open(str_App_Arg_Config_Path_And_File)
            except (OSError, IOError):
                str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                print(str_Message_Header)
                print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                print('>> Command Line Error >> Non-existent file. Invalid argument --> ' + str(opt) + ' ' + str(arg))
                print('>> Run Terminated.')
                str_Message_Footer = '-'*(len(str_Message_Header)-1)
                print(str_Message_Footer)
                raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)
                pass  
            except Exception as error:
                str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                print(str_Message_Header)
                print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                print('>> Command Line Error >> UNEXPECTED ERROR: ' + error.__doc__)
                print('>> Command Line Error >> UNEXPECTED ERROR: ' + error.message)
                print('>> Run Terminated.')
                str_Message_Footer = '-'*(len(str_Message_Header)-1)
                print(str_Message_Footer)
                raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)                              
            finally:
                if fileHandle is not None:
                    fileHandle.close()
                pass
            pass    
            pass
        elif opt in ("-o", "--outpath"):
            str_App_Arg_Output_Base_Path = arg
            if str_OS_Platform.startswith('win') and (':' not in str_App_Arg_Output_Base_Path):
                str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                print(str_Message_Header)
                print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                print('>> Command Line Error >> Invalid path.  No drive specified.  Please check. Invalid argument --> ' + str(opt) + ' ' + str(arg))
                print('>> Run Terminated.')
                str_Message_Footer = '-'*(len(str_Message_Header)-1)
                print(str_Message_Footer)
                raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)
            else:
                try:
                    if not os__path.exists(str_App_Arg_Output_Base_Path):
                        try:
                            os__makedirs(str_App_Arg_Output_Base_Path)
                        except (OSError, IOError):
                            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                            print(str_Message_Header)
                            print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                            print('>> Command Line Error >> Path could not be created.  Please check. Invalid argument --> ' + str(opt) + ' ' + str(arg))
                            print('>> Run Terminated.')
                            str_Message_Footer = '-'*(len(str_Message_Header)-1)
                            print(str_Message_Footer)
                            raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)
                        pass
                    pass
                except Exception as error:
                    str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                    print(str_Message_Header)
                    print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                    print('>> Command Line Error >> UNEXPECTED ERROR: ' + error.__doc__)
                    print('>> Command Line Error >> UNEXPECTED ERROR: ' +  error.message) 
                    print('>> Run Terminated.')
                    str_Message_Footer = '-'*(len(str_Message_Header)-1)
                    print(str_Message_Footer)
                    raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)
                pass
            pass                
        elif opt in ("-p", "--procstep"):
            try:
                list_int_App_Arg_Run_Processing_Steps = [int(x.strip()) for x in arg.split(",")]
            except ValueError:
                str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                print(str_Message_Header)
                print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                print('>> Command Line Error >> Invalid comma-separated integer list (no spaces allowed, only valid integers and commas i.e. 0,1). Invalid argument --> ' + str(opt) + ' ' + str(arg))
                print('>> Run Terminated.')
                str_Message_Footer = '-'*(len(str_Message_Header)-1)
                print(str_Message_Footer)
                raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)                    
            except Exception as error:
                str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                print(str_Message_Header)
                print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                print('>> Command Line Error >> UNEXPECTED ERROR: ' + error.__doc__)
                print('>> Command Line Error >> UNEXPECTED ERROR: ' +  error.message) 
                print('>> Run Terminated.')
                str_Message_Footer = '-'*(len(str_Message_Header)-1)
                print(str_Message_Footer)
                raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)
            pass              
        elif opt in ("-c", "--cpu_affinity"):
            try:
                list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use = [int(x.strip()) for x in arg.split(",")]
            except ValueError:
                str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                print(str_Message_Header)
                print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                print('>> Command Line Error >> Invalid comma-separated integer list (no spaces allowed, only valid integers and commas i.e. 0,1). Invalid argument --> ' + str(opt) + ' ' + str(arg))
                print('>> Run Terminated.')
                str_Message_Footer = '-'*(len(str_Message_Header)-1)
                print(str_Message_Footer)
                raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)                    
            except Exception as error:
                str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                print(str_Message_Header)
                print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
                print('>> Command Line Error >> UNEXPECTED ERROR: ' + error.__doc__)
                print('>> Command Line Error >> UNEXPECTED ERROR: ' +  error.message) 
                print('>> Run Terminated.')
                str_Message_Footer = '-'*(len(str_Message_Header)-1)
                print(str_Message_Footer)
                raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)
            pass              
        else:
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
            print('>> Command Line Error >> Unexpected Option and/or Arguments --> ' + str(opts) + ' ' + str(args))
            print('>> Please use the following -options and <arguments>:')
            print('neogen.exe --infile=<batch_scenario_file> --outpath=<output_path> --procstep=<processing_steps_comma_separated>')
            print('>> or... ')
            print('neogen.exe -i <batch_scenario_file> -o <output_path> -p <processing_steps_comma_separated>')
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)
        pass
    pass
    
    str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
    print(str_Message_Header)
    print('>> Me: ' + str_App_Run_Path_And_File)
    print('>> Command line arguments entered: ' + ' '.join(list_Command_Line_Arguments))
    print('>> Batch_Scenario_Path_And_File: ' + str_App_Arg_Config_Path_And_File)
    print('>> Output_Path: ' + str_App_Arg_Output_Base_Path)
    print('>> Processing_Step: ' + str(list_int_App_Arg_Run_Processing_Steps))
    print('>> Run proceeding...')
    str_Message_Footer = '-'*(len(str_Message_Header)-1)
    print(str_Message_Footer)
            
    #tup_Command_Line_Args = str_App_Run_Path_And_File, str_App_Arg_Output_Base_Path, str_App_Arg_Config_Path_And_File, list_int_App_Arg_Run_Processing_Steps
    
    return str_App_Run_Path_And_File, str_App_Arg_Output_Base_Path, str_App_Arg_Config_Path_And_File, list_int_App_Arg_Run_Processing_Steps, list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use

def func_Run_Status(str_Run_Status_Base_Path, bool_Delete_Run_Status_Path):
    
    bool_Success = False
    
    try:
        str_Run_Status_Path_And_File = ''
        str_Run_Status_Path = os__path.join(str_Run_Status_Base_Path, globals_GEN.Run_Status.static_str_Run_Status__Path)
        str_Run_Status_Path_And_File = os__path.join(str_Run_Status_Path, app_details.str_Project__Prefix + '_Run' + os__extsep + globals_GEN.Run_Status.static_str_Run_Status__INITIATED)
        
        if bool_Delete_Run_Status_Path:
            if os__path.exists(str_Run_Status_Path):
                shutil__rmtree(str_Run_Status_Path) #removes all the subdirectories!
                print('Deleted path: ' + str_Run_Status_Path)
            pass
        pass
    
        if not os__path.exists(str_Run_Status_Path):
            try:
                os__makedirs(str_Run_Status_Path)
                print('Created path: ' + str_Run_Status_Path)
            except (OSError, IOError):
                str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
                print(str_Message_Header)
                print('>> Command Line Error >> Run status path could not be created.  Invalid outpath.  Please check. Invalid argument --> --outpath=' + str_Run_Status_Path)
                print('>> Run Terminated.')
                str_Message_Footer = '-'*(len(str_Message_Header)-1)
                print(str_Message_Footer)
                raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)
            pass
        elif bool_Delete_Run_Status_Path:
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> Command Line Error >> Run status path could not be removed: ' + str_Run_Status_Path)
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Caught_Error)
        pass
    
        try:
            fileHandle = open(str_Run_Status_Path_And_File, 'w')
            print('Created file: ' + str_Run_Status_Path_And_File)
        except (OSError, IOError):
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> Unexpected Error. Run status file could not be created & opened for writing: ' + str_Run_Status_Path_And_File)
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Caught_Error)
        finally:
            if fileHandle is not None:
                fileHandle.close()
            pass
        pass
    
        bool_Success = True
#     except (OSError, IOError):
#         str_Message_Header = '\n---------------------------------------------- ' + str(__project__) + ' ' + str(__version__) + ' Command Line ----------------------------------------------'
#         print(str_Message_Header
#         print('>> Command Line Error >> Run status path could not be removed: ' + str_Run_Status_Path
#         print('>> Run Terminated.'
#         str_Message_Footer = '-'*(len(str_Message_Header)-1)
#         print(str_Message_Footer
#         raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Caught_Error)
#             
    except Exception as error:
        str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
        print(str_Message_Header)
        print('>> UNCAUGHT EXCEPTION Creating Run Status File: ' + str_Run_Status_Path_And_File)
        print('>> Command Line Error >> UNEXPECTED ERROR: ' + error.__doc__)
        print('>> Command Line Error >> UNEXPECTED ERROR: ' +  error.message) 
        print('>> Run Terminated.')
        str_Message_Footer = '-'*(len(str_Message_Header)-1)
        print(str_Message_Footer)
        raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)
    pass
    
    return bool_Success   

def func_Get_Run_Status_File__REQUESTED(str_Run_Status_Base_Path):
    
    bool_App_Started_From_Command_Line = True
    str_Run_Status_Path_And_File = ''
    fileHandle = None
    
    str_Run_Status_Path = os__path.join(str_Run_Status_Base_Path, globals_GEN.Run_Status.static_str_Run_Status__Path)
    str_Run_Status_Path_And_File = os__path.join(str_Run_Status_Path, app_details.str_Project__Prefix + '_Run' + os__extsep + globals_GEN.Run_Status.static_str_Run_Status__REQUESTED)

    if os__path.exists(str_Run_Status_Path):
        try:
            fileHandle = open(str_Run_Status_Path_And_File, 'r')
            if fileHandle is not None:
                bool_App_Started_From_Command_Line = False
                print('Found file: ' + str_Run_Status_Path_And_File)
            else:
                bool_App_Started_From_Command_Line = True
                print('App started from command line. File NOT Found: ' + str_Run_Status_Path_And_File)
            pass
        except IOError:
            bool_App_Started_From_Command_Line = True
            print('App started from command line. File NOT Found: ' + str_Run_Status_Path_And_File)
        except OSError:
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> Unexpected Error. Run status file could not be found & opened for read, to check its existence: ' + str_Run_Status_Path_And_File)
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Caught_Error)
        except Exception as error:
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> UNCAUGHT EXCEPTION Checking if Run Status File exists: ' + str_Run_Status_Path_And_File)
            print('>> Command Line Error >> UNEXPECTED ERROR: ' + error.__doc__)
            print('>> Command Line Error >> UNEXPECTED ERROR: ' +  error.message) 
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__UNCaught_Error)
        finally:
            if fileHandle is not None:
                fileHandle.close()
            pass
        pass
    pass

    return bool_App_Started_From_Command_Line
   
def func_Main(list_Command_Line_Arguments): 

    bool_Success = False
    
    str_App_Run_Path_And_File \
    , str_App_Arg_Output_Base_Path \
    , str_App_Arg_Config_Path_And_File \
    , list_int_App_Arg_Run_Processing_Steps \
    , list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use \
    = func_Get_Command_Line_Arguments(list_Command_Line_Arguments)
    
    ##print('Run scenario path:' + str_App_Arg_Output_Base_Path
    bool_App_Started_From_Command_Line = func_Get_Run_Status_File__REQUESTED(str_App_Arg_Output_Base_Path)
       
    tup_Command_Line_Args = (bool_App_Started_From_Command_Line, str_App_Run_Path_And_File, str_App_Arg_Output_Base_Path, str_App_Arg_Config_Path_And_File, list_int_App_Arg_Run_Processing_Steps, list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use) 
    #tup_Command_Line_Args = (True, '', '', '', [])
    
    ''' Set the CPU affinity for the process'''
    ''' If no affinity args we specified let the system / simupop work out what it wants '''
    if len(list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use) > 0:
        bool_Success, list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use = func_Set_CPU_Affinity(list_Command_Line_Arguments, list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use)
    pass

    ''' Initialise simupop OPTIONS '''
    bool_App_Uses_Simupop = True
    if bool_App_Uses_Simupop:
        func_Initalise_Simupop(list_int_App_Arg_Run_CPU_Affinity_CPUs_To_Use)
    pass

    bool_Delete_Run_Status_Path = bool_App_Started_From_Command_Line
    bool_Success = func_Run_Status(str_App_Arg_Output_Base_Path, bool_Delete_Run_Status_Path)
    bool_Success = True
    
    if bool_Success:
        bool_Success = False
        bool_Success = func_Initialise(str_App_Arg_Output_Base_Path)
    pass
    ''' 
    Start Run processing
    '''    
    if bool_Success:
        ''' This is imported here as it cannot be imported before simupop OPTIONS (simuOpt)
        are set (and the number of CPUs/Threads specified), as this class imports simupop and the options can then no longer be set
        '''
        from SSRunHandler import SSRunOperation as cls_Run
        
        with cls_Run(tup_Command_Line_Args) as obj_NOG_Run:
            obj_NOG_Run.func_Run_Start()
        pass
    pass

    #DEBUG_ON
    #builtins__input("\n Press return to close this window... \n")
    #DEBUG_OFF
    
    return True  

'''
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
MAIN       
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
'''
if __name__ == '__main__':

    try:
        list_Args = []
        list_Args = sys.argv[1:]
        if list_Args == []:
    
            str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
            print(str_Message_Header)
            print('>> Please use the following -options and <arguments>:')
            print('neogen.exe --infile=<batch_scenario_file> --outpath=<output_path> --procstep=<processing_steps_comma_separated>')
            print('>> or... ')
            print('neogen.exe -i <batch_scenario_file> -o <output_path> -p <processing_steps_comma_separated>')
            print('>> Run Terminated.')
            str_Message_Footer = '-'*(len(str_Message_Header)-1)
            print(str_Message_Footer)
            raise SystemExit(globals_GEN.System_Exit_Code.static_int_System_Exit_Code__Failed__Command_Line_Error)
         
        else:
            func_Main(list_Args)
        pass   
    
    finally:
        str_Message_Header = '\n---------------------------------------------- ' + str(app_details.__project__) + ' ' + str(app_details.__version__) + ' Command Line ----------------------------------------------'
        print(str_Message_Header)
        print('>>>> End program.')
        str_Message_Footer = '-'*(len(str_Message_Header)-1)
        print(str_Message_Footer)
        ''' test '''
    pass
