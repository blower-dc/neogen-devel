#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS
#
#------------------< Import python modules
import re
from sys import platform as sys__platform
import tempfile
import os, glob, fnmatch
from itertools import islice
import ntpath
#import shutil, errno
import errno
from shutil import copystat as shutil__copystat
from shutil import copyfile as shutil__copyfile
from shutil import copytree as shutil__copytree
from shutil import copy as shutil__copy
from shutil import copy2 as shutil__copy2
from shutil import rmtree as shutil__rmtree
from time import sleep as time__sleep
#------------------< Import DCB_General modules
from ErrorHandler import ErrorHandler
from logging import getLogger as logging__getLogger

gstringModuleName='FileHandler.py'
gstringClassName='FileOperation'


class FileHandler:
    """Handle FileOperation objects"""

    static_str_FileStat_FileSize_st_size = 'st_size'
    
    def __enter__(self):
        
        
        
        class FileOperation: 
            """Explicitly control all fundemental file operations"""

            def __init__(self):
                '''
                Constructor
                '''
                self.obj_Log_Default = logging__getLogger(__name__)
                self.obj_Log_Debug = logging__getLogger('app_debug')           
                     
                return None
            
            
            def method_Get_File_Stats(self, strPathAndFileName, strFileStatRequired=''):
                
                if strFileStatRequired == FileHandler.static_str_FileStat_FileSize_st_size:
                    longFileSize = os.stat(strPathAndFileName).st_size
                    tupReturn = (0, longFileSize)
                else:
                    tupReturn = os.stat(strPathAndFileName)
                pass
                    
                return tupReturn
            
            def method_Get_FileName_From_PathAndFileName(self, strPathAndFileName):
            
                strFilePathAndName, strFileName = ntpath.split(strPathAndFileName)
                
                return strFileName or ntpath.basename(strFilePathAndName)

            def method_Separate_Path_And_FileName_From_PathAndFileName(self, strPathAndFileName):
            
                strFilePath, strFileName = ntpath.split(strPathAndFileName)
                
                return strFilePath, strFileName

            def method_Get_FileNameAndExtension_From_FileName(self, strPathAndFileNameWithExtension):
            
                strFilePathAndName, strFileExtension = os.path.splitext(strPathAndFileNameWithExtension)
                
                return (strFilePathAndName, strFileExtension)
            
            def method_Path_Exists(self, strPath):

                boolSuccessful = False
                
                #DEBUG_ON
#                 os.path.isdir(strPath)
#                 os.path.islink(strPath)
#                 os.path.exists(strPath)
                #DEBUG_OFF

                if os.path.exists(strPath):
                        boolSuccessful = True
                
                return boolSuccessful

            def method_Create_Path(self, strPath):

                boolSuccessful = False

                if not self.method_Path_Exists(strPath):
                    try:
                        os.makedirs(strPath)
                        
                        boolSuccessful = True

                    except (OSError, IOError) as exception:
                        
                        with ErrorHandler() as objectErrorOperation:
                            objectErrorOperation.propertyString_ErrorOriginModule= gstringModuleName
                            objectErrorOperation.propertyString_ErrorOriginClass= gstringClassName
                            objectErrorOperation.propertyString_ErrorMessage= 'Path cannot be created (strPath): ' + strPath + ')'
                            stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                        
                            raise OSError(stringErrorMessageWithDetail)
                else:
                    #Path already exists
                    boolSuccessful = True
                    pass
                     
                return boolSuccessful
                
            def method_Delete_Path(self, str_Path):
                
                bool_Success = False
                
                bool_Path_Exists = self.method_Path_Exists(str_Path)
                if bool_Path_Exists:
                    bool_Success = False
                    
                    try:
                        shutil__rmtree(str_Path) #removes all the subdirectories!
                        bool_Success = True
                    except (OSError, IOError): 
                        bool_Success = False
                    pass
                else:
                    bool_Success = True
                pass
            
                return bool_Success
                
            def methodDelete_MultipleFilesByWildcard(self, strFilenames):
                
                bool_Success = False
                
                try:
                    for strFileName in glob.glob(strFilenames) :
                        os.remove(strFileName)
                    pass
                    bool_Success = True
                    
                except (OSError, IOError): 
                    bool_Success = False
                pass
                
                return bool_Success
            
            def fileDelete(self,fileName):

                boolSuccessful = False

                try:
                    os.remove(fileName)
                    boolSuccessful = True

                except (OSError, IOError):
                    boolSuccessful = False
                    pass

                return boolSuccessful
            
            
            def fileExists(self,fileName):

                bool_Success = False
                
                fileHandle = None
                
                try:
                    fileHandle = open(fileName, 'r')
                    bool_Success = True
                except (OSError, IOError):
                     boolSuccessful = False
                finally:
                    if fileHandle is not None:
                       fileHandle.close()
                    pass
                pass

                return bool_Success

            def method_FileSystem_Prep_For_File_Save(self, strFile_PathAndFileName, bool_Delete=False):
            
                boolSuccess = False

                ''' Check if filename length is excessive '''
                strFilePath, strFileName = self.method_Separate_Path_And_FileName_From_PathAndFileName(strFile_PathAndFileName)
                boolSuccess = self.func_Windows_Check_Filename_Length(strFilePath, strFileName)
                if not boolSuccess:
                    return boolSuccess
                pass
            
                ''' Create path if not exists '''
                boolSuccess = self.method_Create_Path(strFilePath)
                if not boolSuccess:
                    return boolSuccess
                pass
            
                ''' Check if file exists and delete if required '''
                bool_File_Exists = self.fileExists(strFile_PathAndFileName)
                if bool_File_Exists and bool_Delete:
                    boolSuccess = self.fileDelete(strFile_PathAndFileName)
                pass
                if not boolSuccess:
                    return boolSuccess
                pass
                        
                return boolSuccess
                
            def fileOpen(self, fileName, stringFileOpenModeVerbose):
                
                stringMethodName= "FileOpen"
                fileHandle = None
                
                # Open file with appropriate open mode (enclose code in double quotes):
                # "r" - read (default if not specified)
                # "w" - write
                # "a" - append
                # "r+" - read & write
                
                boolContinue = False
                if stringFileOpenModeVerbose == 'read':
                    boolContinue = self.fileExists(fileName)
                    stringFileOpenModeConcise = 'r'
                elif stringFileOpenModeVerbose == 'write':
                    #File will be created if it doesnt exist
                    boolContinue = True
                    stringFileOpenModeConcise = 'w'
                elif stringFileOpenModeVerbose == 'read_write':
                    #File will be created if it doesnt exist
                    boolContinue = True
                    stringFileOpenModeConcise = 'r+'
                elif stringFileOpenModeVerbose == 'append':
                    boolContinue = self.fileExists(fileName)
                    stringFileOpenModeConcise = 'a'
                else:
                    # stringFileOpenModeVerbose contains an invalid value
                    boolContinue = False
                    with ErrorHandler() as objectErrorOperation:
                        objectErrorOperation.propertyString_ErrorOriginModule= gstringModuleName
                        objectErrorOperation.propertyString_ErrorOriginClass= gstringClassName
                        objectErrorOperation.propertyString_ErrorMessage= 'Invalid stringFileOpenModeVerbose (stringFileOpenModeVerbose=' + stringFileOpenModeVerbose + ')'
                        stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                    return

                if boolContinue == True:
                    try:       
                        fileHandle = open(fileName, stringFileOpenModeConcise)

                    except (OSError, IOError):
                        with ErrorHandler() as objectErrorOperation:
                            objectErrorOperation.propertyString_ErrorOriginModule= gstringModuleName
                            objectErrorOperation.propertyString_ErrorOriginClass= gstringClassName
                            objectErrorOperation.propertyString_ErrorMessage= 'File: ' + fileName + ' cannot be opened (stringFileOpenModeConcise: ' + stringFileOpenModeConcise + ')'
                            stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                        raise IOError(stringErrorMessageWithDetail)
                else:
                    with ErrorHandler() as objectErrorOperation:
                        objectErrorOperation.propertyString_ErrorOriginModule= gstringModuleName
                        objectErrorOperation.propertyString_ErrorOriginClass= gstringClassName
                        objectErrorOperation.propertyString_ErrorMessage= 'File: ' + fileName + ' cannot be opened (stringFileOpenModeConcise: ' + stringFileOpenModeConcise + ')'
                        stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                        print(stringErrorMessageWithDetail)
                    return

                return fileHandle
             
            def fileClose(self, fileHandle):
                
                boolSuccessful = False

                try:       
                    fileHandle.close()
                    boolSuccessful = True
                    
                    #DEBUG
                    #print('Closed:' + fileHandle.name)
                    #DEBUG
                    
                except (OSError, IOError):
                    with ErrorHandler() as objectErrorOperation:
                        objectErrorOperation.propertyString_ErrorOriginModule= gstringModuleName
                        objectErrorOperation.propertyString_ErrorOriginClass= gstringClassName
                        objectErrorOperation.propertyString_ErrorMessage= 'File: ' + fileHandle.name + ' cannot be closed.'
                        stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
                    raise IOError(stringErrorMessageWithDetail)
                
                return boolSuccessful            


            def method_Copy_Folder_Or_All_Files(self, strFolderFileSource, strFolderFileDestination):
                
                boolSuccessful = False
            
                try:
                    shutil__copytree(strFolderFileSource, strFolderFileDestination)
                    boolSuccessful = True
                except (OSError, IOError) as exc: # python >2.5
                    if exc.errno == errno.EEXIST:
                        #shutil__copy(strFolderFileSource, strFolderFileDestination)
                        strFileCopyPattern = '*'
                        boolSuccessful = self.method_Copy_Files_By_Pattern(strFolderFileSource, strFolderFileDestination, strFileCopyPattern, bool_Search_SubFolders=True)
                        #boolSuccessful = True
                    else: 
                        boolSuccessful = False
                        raise
                
                return boolSuccessful
            
            def method_Copy_Files(self, strFilePathAndNameSource, strFilePathAndNameDestination):
                
                boolSuccessful = False
            
                try:
                    shutil__copyfile(strFilePathAndNameSource, strFilePathAndNameDestination)
                    boolSuccessful = True
                except (OSError, IOError) as exc: # python >2.5
                        boolSuccessful = False
                        raise
                
                return boolSuccessful
 
            def method_Copy_Files_By_Search_Pattern(self, strFilePathSource, strFilePathDestination, strFileCopyPattern, bool_Search_SubFolders=False):  
                
                boolSuccessful = False
                int_Attempts = 3
                int_Attempt = 0
                
#                 def failed(exc):
#                     if int_Attempt <= int_Attempts:
#                         int_Attempt += 1
#                         time__sleep(1) # delays for 1 seconds
#                         pass
#                     else:
#                         boolSuccessful = False
#                         raise exc
#                         #return boolSuccessful
#                     pass
#                 pass
            
                def failed(exc):
                    boolSuccessful = False
                    raise exc
                    return boolSuccessful
                    pass
                pass
            
                for dirpath, dirs, files in os.walk(strFilePathSource, topdown=True, onerror=failed):
                    for file in fnmatch.filter(files, strFileCopyPattern):
                        try:
                            shutil__copy2(os.path.join(dirpath, file), strFilePathDestination)
                            boolSuccessful = True
                        except (OSError, IOError):
                            failed()
                        pass
                    pass
                    if not bool_Search_SubFolders:
                        boolSuccessful = True
                        break # no recursion
                    else:
                        boolSuccessful = True
                    pass                
                pass
                            
                return boolSuccessful
            
            def method_Copy_Files_By_Pattern(self, strFilePathSource, strFilePathDestination, strFileCopyPattern, bool_Search_SubFolders=False):  
                
                boolSuccessful = False
                int_Attempts = 3
                int_Attempt = 0
                
#                 def failed(exc):
#                     if int_Attempt <= int_Attempts:
#                         int_Attempt += 1
#                         time__sleep(1) # delays for 1 seconds
#                         pass
#                     else:
#                         boolSuccessful = False
#                         raise exc
#                         #return boolSuccessful
#                     pass
#                 pass
            
                def failed(exc):
                    boolSuccessful = False
                    raise exc
                    return boolSuccessful
                    pass
                pass
            
                for dirpath, dirs, files in os.walk(strFilePathSource, topdown=True, onerror=failed):
                    for file in fnmatch.filter(files, strFileCopyPattern):
                        try:
                            shutil__copy2(os.path.join(dirpath, file), strFilePathDestination)
                            boolSuccessful = True
                        except (OSError, IOError) as exc: # python >2.5
                            boolSuccessful = False
                        pass
                    pass
                    if not bool_Search_SubFolders:
                        boolSuccessful = True
                        break # no recursion
                    pass                
                pass
                            
                return boolSuccessful
                                                 
            def method_ReadSliceOfNLinesFromOpenFile(self, fileHandle, intLinesToRead):
                
                generatorLines = islice(fileHandle, intLinesToRead)
                
                return generatorLines

            def func_Locate_Files(self, str_Search_Path, str_File_Search_Pattern, bool_Print_Search_Result = False, bool_Search_Sub_Folders = True):
                
                bool_Files_Located = False
                
                def failed(exc):
                    bool_Files_Located = False
                    raise exc

                list_Path_And_Files = []
                
                if self.func_Windows_Check_Filename_Length(str_Search_Path, str_File_Search_Pattern):
                    boolSuccessful = False
                    bool_File_Located = False
                    
                    if bool_Search_Sub_Folders:
                        for dirpath, dirs, files in os.walk(str_Search_Path, topdown=True, onerror=failed):
                            str_Path_And_File = ''
                            for str_File_Name in fnmatch.filter(files, str_File_Search_Pattern):
                                bool_Files_Located = True
                                str_Path_And_File = os.path.join(dirpath, str_File_Name)
                                list_Path_And_Files.append(str_Path_And_File)
                                pass
                            pass
                        pass
                    else:
                        bool_Files_Found = False
                        list_Files_Found = []
                        for str_Path_And_File in os.listdir(str_Search_Path):
                            if os.path.isfile(os.path.join(str_Search_Path, str_Path_And_File)):
                                list_Files_Found.append(str_Path_And_File)
                                bool_Files_Found = True
                            pass
                        pass
                    
                        if bool_Files_Found:
                            for str_File_Name in fnmatch.filter(list_Files_Found, str_File_Search_Pattern):
                                bool_Files_Located = True
                                str_Path_And_File = os.path.join(str_Search_Path, str_File_Name)
                                list_Path_And_Files.append(str_Path_And_File)
                                pass
                            pass
                        pass
                    pass
                pass
            
                if bool_Print_Search_Result:
                    if len(list_Path_And_Files) == 0:
                        bool_Files_Located = False
                        print('No files found. Expecting files on search path; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
                    pass
                pass
                            
                return bool_Files_Located, list_Path_And_Files
        
            def func_Locate_Folders(self, str_Search_Path, str_Folder_Search_Pattern, bool_Print_Search_Result = False, bool_Search_Sub_Folders = True):
                
                bool_Folders_Located = False
                
                def failed(exc):
                    bool_Folders_Located = False
                    raise exc

                list_Folders = []
                
                if self.func_Windows_Check_Filename_Length(str_Search_Path, str_Folder_Search_Pattern):
                    boolSuccessful = False
                    bool_Folder_Located = False
                    
                    if bool_Search_Sub_Folders:
                        for dirpath, dirs, files in os.walk(str_Search_Path, topdown=True, onerror=failed):
                            #str_Path = ''
                            for str_Folder_Found in fnmatch.filter(dirs, str_Folder_Search_Pattern):
                                bool_Folders_Located = True
                                #str_Path = os.path.join(dirpath, str_Path_Name)
                                list_Folders.append(str_Folder_Found)
                                pass
                            pass
                        pass
                    else:
                        bool_Folders_Found = False
                        list_Folders_Found = []
                        for str_Folder_Found in os.listdir(str_Search_Path):
                            if os.path.isdir(os.path.join(str_Search_Path, str_Folder_Found)):
                                list_Folders_Found.append(str_Folder_Found)
                                bool_Folders_Found = True
                            pass
                        pass
                    
                        if bool_Folders_Found:
                            for str_Folder_Found in fnmatch.filter(list_Folders_Found, str_Folder_Search_Pattern):
                                bool_Folders_Located = True
                                #str_Path = os.path.join(str_Search_Path, str_Path_Name)
                                list_Folders.append(str_Folder_Found)
                                pass
                            pass
                        pass
                    pass
                pass
            
                if bool_Print_Search_Result:
                    if len(list_Folders) == 0:
                        bool_Folders_Located = False
                        print('No Folders found. Expecting Folders for search pattern: ' + str_Folder_Search_Pattern + '; on search path: ' + str_Search_Path)
                    pass
                pass
                            
                return bool_Folders_Located, list_Folders
        
            
            def func_Locate_Specific_File(self, str_Search_Path, str_File_Search_Pattern):
                
                def failed(exc):
                    boolSuccessful = False
                    raise exc
                
                bool_File_Located = False
                if not self.func_Windows_Check_Filename_Length(str_Search_Path, str_File_Search_Pattern):
                    boolSuccessful = False
                    
                    for dirpath, dirs, files in os.walk(str_Search_Path, topdown=True, onerror=failed):
                        bool_File_Located = False
                        intCount = 0
                        for str_File_Name in fnmatch.filter(files, str_File_Search_Pattern):
                            bool_File_Located = True
                            intCount += 1
                            if intCount > 1:
                                print('More than one file found. Expecting only one on search path; str_Search_Path = ' + str_Search_Path + '; strFileSearchPattern = ' + str_File_Search_Pattern)
                            pass
                        pass
                    pass
                pass
            
                str_Path_And_File = ''
                if bool_File_Located:
                    str_Path_And_File = dirpath + '\\' + str_File_Name
                    
                return bool_File_Located, str_Path_And_File

            def func_Windows_Check_Filename_Length(self, str_File_Path, str_File_Name):
                
                boolSuccess = False
                
                str_Path_And_File = str_File_Path + '\\' + str_File_Name
                int_Max_Length = 256
                int_Len_str_Path_And_File = len(str_Path_And_File)
                if int_Len_str_Path_And_File >= 256:
                    #self.obj_Log_Default.error('Filename exceeds ' + str(int_Max_Length) + ' by ' + str(int_Len_str_Path_And_File - int_Max_Length) + 'chars ; File: ' + str_Path_And_File)
                    #self.obj_Log_Default.error('Filename cannot be used.')
                    print('Filename exceeds ' + str(int_Max_Length) + ' by ' + str(int_Len_str_Path_And_File - int_Max_Length) + 'chars ; File: ' + str_Path_And_File)
                    print('Filename cannot be used.')
                    boolSuccess = False
                else:
                    boolSuccess = True
                pass
            
                return boolSuccess
                            
            def func_File_AndOr_Name_Length_Is_Valid(self, str_File_Path_And_Name, int_Max_Length):
                
                boolSuccess = False
                
                if int_Max_Length > 0:
                    int_Length = len(str_File_Path_And_Name)
                    
                    int_Length_Difference = int_Length - int_Max_Length
                    
                    if int_Length > int_Max_Length:
                        boolSuccess = False
                    else:
                        boolSuccess = True
                    pass
                pass
            
                return boolSuccess, int_Length_Difference

            def is_pathname_valid(self, pathname):
                
        
                bool_Success = False
                
                # Sadly, Python fails to provide the following magic number for us.
                ERROR_INVALID_NAME = 123
                '''
                Windows-specific error code indicating an invalid pathname.
                
                See Also
                ----------
                https://msdn.microsoft.com/en-us/library/windows/desktop/ms681382%28v=vs.85%29.aspx
                    Official listing of all such codes.
                '''
            
                '''
                `True` if the passed pathname is a valid pathname for the current OS;
                `False` otherwise.
                '''
                # If this pathname is either not a string or is but is empty, this pathname
                # is invalid.
                try:
                    if not isinstance(pathname, str) or not pathname:
                        return False
            
                    # Strip this pathname's Windows-specific drive specifier (e.g., `C:\`)
                    # if any. Since Windows prohibits path components from containing `:`
                    # characters, failing to strip this `:`-suffixed prefix would
                    # erroneously invalidate all valid absolute Windows pathnames.
                    _, pathname = os.path.splitdrive(pathname)
            
                    # Directory guaranteed to exist. If the current OS is Windows, this is
                    # the drive to which Windows was installed (e.g., the "%HOMEDRIVE%"
                    # environment variable); else, the typical root directory.
                    root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
                        if sys__platform == 'win32' else os.path.sep
                    assert os.path.isdir(root_dirname)   # ...Murphy and her ironclad Law
            
                    # Append a path separator to this directory if needed.
                    root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep
            
                    # Test whether each path component split from this pathname is valid or
                    # not, ignoring non-existent and non-readable path components.
                    for pathname_part in pathname.split(os.path.sep):
                        try:
                            os.lstat(root_dirname + pathname_part)
                        # If an OS-specific exception is raised, its error code
                        # indicates whether this pathname is valid or not. Unless this
                        # is the case, this exception implies an ignorable kernel or
                        # filesystem complaint (e.g., path not found or inaccessible).
                        #
                        # Only the following exceptions indicate invalid pathnames:
                        #
                        # * Instances of the Windows-specific "WindowsError" class
                        #   defining the "winerror" attribute whose value is
                        #   "ERROR_INVALID_NAME". Under Windows, "winerror" is more
                        #   fine-grained and hence useful than the generic "errno"
                        #   attribute. When a too-long pathname is passed, for example,
                        #   "errno" is "ENOENT" (i.e., no such file or directory) rather
                        #   than "ENAMETOOLONG" (i.e., file name too long).
                        # * Instances of the cross-platform "OSError" class defining the
                        #   generic "errno" attribute whose value is either:
                        #   * Under most POSIX-compatible OSes, "ENAMETOOLONG".
                        #   * Under some edge-case OSes (e.g., SunOS, *BSD), "ERANGE".
                        except OSError as exc:
                            if hasattr(exc, 'winerror'):
                                if exc.winerror == ERROR_INVALID_NAME:
                                    return False
                            elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                                return False
                # If a "TypeError" exception was raised, it almost certainly has the
                # error message "embedded NUL character" indicating an invalid pathname.
                except TypeError as exc:
                    return False
                # If no exception was raised, all path components and hence this
                # pathname itself are valid. (Praise be to the curmudgeonly python.)
                else:
                    return True
                # If any other exception was raised, this is an unrelated fatal issue
                # (e.g., a bug). Permit this exception to unwind the call stack.
                #
                # Did we mention this should be shipped with Python already?
                
                return bool_Success
        
            def is_path_creatable(self, pathname):
                '''
                `True` if the current user has sufficient permissions to create the passed
                pathname; `False` otherwise.
                '''
                bool_Success = False
                
                # Parent directory of the passed path.
                dirname = os.path.dirname(pathname) #or os.getcwd()
                
                bool_Success = os.access(dirname, os.W_OK)
                
                return bool_Success
            
            def is_path_exists_or_creatable(self, pathname):
                '''
                `True` if the passed pathname is a valid pathname for the current OS _and_
                either currently exists or is hypothetically creatable; `False` otherwise.
            
                This function is guaranteed to _never_ raise exceptions.
                '''
                
                bool_Success = False
                 
                try:
                    # To prevent "os" module calls from raising undesirable exceptions on
                    # invalid pathnames, is_pathname_valid() is explicitly called first.
                    bool_Success = self.is_pathname_valid(pathname) and (os.path.exists(pathname) or self.is_path_creatable(pathname))
                # Report failure on non-fatal filesystem complaints (e.g., connection
                # timeouts, permissions issues) implying this path to be inaccessible. All
                # other exceptions are unrelated fatal issues and should not be caught here.
                except OSError:
                    bool_Success = False 
                pass
                
                return bool_Success
            
            def is_path_sibling_creatable(self, pathname):
                '''
                `True` if the current user has sufficient permissions to create **siblings**
                (i.e., arbitrary files in the parent directory) of the passed pathname;
                `False` otherwise.
                '''
                
                bool_Success = False
                
                # Parent directory of the passed path. If empty, we substitute the current
                # working directory (CWD) instead.
                dirname = os.path.dirname(pathname) or os.getcwd()
            
                try:
                    # For safety, explicitly close and hence delete this temporary file
                    # immediately after creating it in the passed path's parent directory.
                    with tempfile.TemporaryFile(dir=dirname): pass
                    bool_Success = True
                # While the exact type of exception raised by the above function depends on
                # the current version of the Python interpreter, all such types subclass the
                # following exception superclass.
                except EnvironmentError:
                    bool_Success = False
                pass
            
                return bool_Success
            
            def is_path_exists_or_creatable_portable(self, pathname):
                '''
                `True` if the passed pathname is a valid pathname on the current OS _and_
                either currently exists or is hypothetically creatable in a cross-platform
                manner optimized for POSIX-unfriendly filesystems; `False` otherwise.
            
                This function is guaranteed to _never_ raise exceptions.
                '''
                try:
                    # To prevent "os" module calls from raising undesirable exceptions on
                    # invalid pathnames, is_pathname_valid() is explicitly called first.
                    return self.is_pathname_valid(pathname) and (
                        os.path.exists(pathname) or self.is_path_sibling_creatable(pathname))
                # Report failure on non-fatal filesystem complaints (e.g., connection
                # timeouts, permissions issues) implying this path to be inaccessible. All
                # other exceptions are unrelated fatal issues and should not be caught here.
                except OSError:
                    return False 
                
                                            
            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.fileOperation_obj = FileOperation() 
        return self.fileOperation_obj
 
    def __exit__(self, type, value, traceback): 
        self.fileOperation_obj.classCleanUp()
