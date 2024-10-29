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
                PATH INFO
-----------------------------------------------
'''
#------------------< Import external modules
import sys, getopt
from sys import path as sys__path

# ''' Display the CPUs '''
# int_CPUs_Available_Count = multiprocessing__cpu_count()
# print('\nAvailable CPUs: ' + str(int_CPUs_Available_Count))

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

bool_Platform_Check = True
if bool_Platform_Check:
    if str_OS_Platform.startswith('win'):
        if not str_OS_Dist_Release.startswith('7'):
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print(' You are building on the wrong version of Windows.')
            print(' It must be built on Win 7 to ensure the program runs on later versions of Windows.\n')
            print(' Terminating build...')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            str_Exit_Code = 999
            sys.exit(str_Exit_Code)
        pass
    pass
pass

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
#             str_Project_Version = 'v' + '_'.join(app_details.__version__.split('.'))
#             
#             str_Run_Folder = app_details.str_Run_Folder
#         
#             str_Root_Drive = 'Q:'
#             str_Root_Folder = 'CODE'
#             str_Sync_Folder = 'RS_SRC' + '__' + app_details.str_Project_Short_Name + '_' + str_Project_Version + '_' + str_Run_Folder
#             str_Project_Folder = 'proj'
#             str_Project_Language_Code = 'Py'
#             str_Project_Language_Version = '2'
#             str_Project_App_Name = '_'.join(app_details.app_details.__project__.split(' '))
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
import sys, getopt, os
from sys import path as sys__path
from __builtin__ import True
from distutils.core import setup
import py2exe

'''
-----------------------
Prevent directory recursion error
-----------------------
'''
sys.setrecursionlimit(5000)


'''
-----------------------
Specify the build folder
-----------------------
'''
build_base = "./py2exe/build"
dist_dir = "./py2exe/dist"
'''
-----------------------
Remove the build folder, a bit slower but ensures that build contains the latest
-----------------------
'''
import shutil
 
shutil.rmtree(dist_dir, ignore_errors=True)
shutil.rmtree(build_base, ignore_errors=True)

'''
-----------------------
modules missing
-----------------------
'''
includes_biopython = ['Bio.Application','Bio.PopGen', 'Bio.PopGen.GenePop']
includes_timeit = ['timeit']
includes_pymysql = ['pymysql']

includes = includes_pymysql + includes_timeit + includes_biopython


'''
-----------------------
libmmd.dll & libzmq.dll issues
-----------------------
'''

import os
import numpy
import zmq

# libzmq.dll is in same directory as zmq's __init__.py

os.environ["PATH"] = \
    os.environ["PATH"] + \
    os.path.pathsep + os.path.split(zmq.__file__)[0]

includes_zmq = ["zmq.utils", "zmq.utils.jsonapi", "zmq.utils.strtypes"]

'''
-----------------------
Sypy issues
-----------------------
'''
includes_scipy = ['scipy', 'scipy.integrate', 'scipy.special.*','scipy.linalg.*','scipy.sparse.csgraph._validation']

'''
-----------------------
Matplotlib issues
-----------------------
'''

# add the mpl mpl-data folder and rc file
import matplotlib as mpl
data_files = []
data_files += mpl.get_py2exe_datafiles()

from distutils.filelist import findall
import matplotlib
matplotlibdatadir = matplotlib.get_data_path()
matplotlibdata = findall(matplotlibdatadir)
matplotlibdata_files = []
for f in matplotlibdata:
    dirname = os.path.join('matplotlibdata', f[len(matplotlibdatadir)+1:])
    matplotlibdata_files.append((os.path.split(dirname)[0], [f]))
pass

'''
-----------------------
Combine includes
-----------------------
'''  
includes = includes + includes_scipy + includes_zmq


'''
---------------------------------------------------------
Build on Win 7 to run on Win 10 -  NEED TO EXCLUDE THESE DLLS
---------------------------------------------------------
'''
list_Dll_Excludes = ["IPHLPAPI.DLL", "NSI.dll",  "WINNSI.DLL",  "WTSAPI32.dll"] #Works on Win 10
list_Dll_Excludes = ["WTSAPI32.dll"]
''' Fails on Win 10
  File "psutil\_psutil_windows.pyo", line 10, in __load
ImportError: DLL load failed: The specified module could not be found.
'''
list_Dll_Excludes = ["IPHLPAPI.DLL", "NSI.dll",  "WINNSI.DLL"] #Works on Win 10
list_Dll_Excludes = ["NSI.dll",  "WINNSI.DLL"] 
''' Fails on Win 10
  File "psutil\_psutil_windows.pyo", line 10, in __load
ImportError: DLL load failed: The specified module could not be found.
'''
list_Dll_Excludes = ["IPHLPAPI.DLL", "NSI.dll"] #Works on Win 10

list_Dll_Excludes = ["IPHLPAPI.DLL"]

''' Not used '''
list_Dll_Includes = []


# setup( console=[{"script": "Main.py"}],
#        options={ 
#            "py2exe": {
#                     # compressed and optimize reduce the size
#                     "compressed": 2 
#                     ,"optimize": 2,
#                     "includes": includes
#                     #,'excludes': ['_gtkagg', '_tkagg']
#                     ,'packages' : ['matplotlib', 'pytz']}} 
#         #using zipfile to reduce number of files in dist
#         ,zipfile = r'lib\library.zip'    
#         ,data_files=data_files  
#         )

str_Main_Py_And_Exe_Name = app_details.str_Project_MainPy_Name

# setup( console=[{"script": "NeOGen.py"}] # Runs with a console widow showing log out put
setup( console=[{"script": str_Main_Py_And_Exe_Name+".py"}] # Runs with a console widow showing log out put
       #windows=['Main.py'] #Runs without console window but output saved to log file in dist foldeer
       ,options={'build': {
                          'build_base': build_base
                          } 
                ,"py2exe": {
                            'dist_dir': dist_dir
                            ,"compressed": 2 # compress and optimize to reduce the size
                            ,"optimize": 2,
                            #,'bundle_files': 1 #Not supported on Win64
                            "includes": includes
                            #,'excludes': ['_gtkagg', '_tkagg']
                            ,'packages' : ['matplotlib', 'pytz']
                            ,'dll_excludes': list_Dll_Excludes
                            #,'dll_includes': list_Dll_Includes                            
                            }
                } 
        #using zipfile to reduce number of files in dist
        ,zipfile = r'lib\library.zip'    
        ,data_files=data_files  
        )

pass