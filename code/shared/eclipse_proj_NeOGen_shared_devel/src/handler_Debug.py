'''
Created on 20 Jan 2015

@author: Darwin
'''

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
#
from timeit import default_timer
import timeit
import inspect
import traceback
import ntpath
import sys
#
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
gstringModuleName='handler_Debug.py'
gstringClassName='Timer'

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = timeit.default_timer()
        return self

    def __exit__(self, *args):
        self.end = timeit.default_timer()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print('???????? DEBUG - Elapsed time: ' + str(self.msecs))  
            
class Timer2(object):

    def __init__(self, verbose=False):
        self.verbose = verbose
        

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass
 
    
    def Start(self):
        self.start = timeit.default_timer()
        
    def Stop(self, logger=None, str_Message='', bool_Pause_Run=False):
        self.end = timeit.default_timer()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if logger != None:
            if self.verbose:
                obj_Debug_Info = Debug_Location()
                str_Message += ' ' + obj_Debug_Info.Get_Debug_Location()
                logger.debug('Func took: %f ms. ' % self.msecs + str_Message)     
            pass
        pass
        if bool_Pause_Run:
            obj_Pause =  Pause_Console() 
            obj_Pause.method_Pause_Console()
        pass
    
class Pause_Console(object): 
                   
    def method_Pause_Console(self):
        raw_input('\n Pausing for output review - Press return to continue... \n')
        return True
                
class Debug_Location(object):

    def __init__(self):
        pass

    def __enter__(self):
        
        return self

     
    def Get_Debug_Location(string, bool_Short=False, int_Stack_Trace_Level_Override=0):

        def Get_Debug_Location__LINE( int_Stack_Trace_Level_Override = 0 ):
            return sys._getframe( int_Stack_Trace_Level_Override + 1 ).f_lineno
        def Get_Debug_Location__FILE( int_Stack_Trace_Level_Override = 0 ):
           return sys._getframe( int_Stack_Trace_Level_Override + 1 ).f_code.co_filename
        def Get_Debug_Location__FUNC( int_Stack_Trace_Level_Override = 0):
            return sys._getframe( int_Stack_Trace_Level_Override + 1 ).f_code.co_name
        def Get_Debug_Location__WHERE( int_Stack_Trace_Level_Override = 0 ):
           frame = sys._getframe( int_Stack_Trace_Level_Override + 1 )
           return "%s/%s %s()" % ( os.path.basename( frame.f_code.co_filename ), 
                                   frame.f_lineno, frame.f_code.co_name )
  
        if int_Stack_Trace_Level_Override > 0:
            frame_LineNo = Get_Debug_Location__LINE( int_Stack_Trace_Level_Override)
            frame_File = Get_Debug_Location__FILE( int_Stack_Trace_Level_Override)
            frame_Func = Get_Debug_Location__FUNC( int_Stack_Trace_Level_Override)
            str_Origin_Func = str(frame_Func)
            str_Origin_Class_PathAndFileName = str(frame_File)
            str_Origin_Class_Path, str_Origin_Class_FileName = ntpath.split(str_Origin_Class_PathAndFileName)
            str_Location = '; ' + str_Origin_Class_FileName + '.' + str_Origin_Func + ' ;' + 'line: ' + str(frame_LineNo)
        
        else:
            frame = inspect.currentframe()
            str_Origin_Func = str(frame.f_back.f_back.f_code.co_name)
            str_Origin_Class_PathAndFileName = str(frame.f_back.f_back.f_code.co_filename)
            str_Origin_Class_Path, str_Origin_Class_FileName = ntpath.split(str_Origin_Class_PathAndFileName)
            str_Location = '; ' + str_Origin_Class_FileName + '.' + str_Origin_Func
        pass
    
        if bool_Short:
            return str_Location
        else: 
            stack_trace = traceback.format_stack(frame)
            if int_Stack_Trace_Level_Override > 0:
                str_Trace_Location = str(stack_trace[len(stack_trace)-int_Stack_Trace_Level_Override])
            else:
                str_Trace_Location = str(stack_trace[len(stack_trace)-3])
            pass
            str_Trace_Location = str_Trace_Location.split('t2.Stop')[0]
            str_Location += '; >> ' + str_Trace_Location
        pass
    
        return str_Location

  
    def __exit__(self, *args):
        pass    