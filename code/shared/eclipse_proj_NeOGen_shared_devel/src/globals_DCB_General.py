'''
Created on 25/01/2016

@author: Dean
'''
#------------------< Import python modules
from datetime import datetime, timedelta
from collections import OrderedDict
#------------------< Import DCB_General modules
from handler_Debug import Debug_Location as dcb_Debug_Location
import globals_DCB_General


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< GLOBALS DEFINITION
global_dateTimeLastGeneralMessage = datetime

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
class globalsDCBGen(object):


    class System_Exit_Code(object):
        
        static_int_System_Exit_Code__Completion__Normal = 0
        static_int_System_Exit_Code__Completion__Premature = 4
        
        static_int_System_Exit_Code__Failed__UNCaught_Error = 1
        static_int_System_Exit_Code__Failed__Command_Line_Error = 2
        static_int_System_Exit_Code__Failed__Caught_Error = 3

    class Run_Status(object):
        
        static_str_Run_Status__Path = 'job_status'
        
        static_int_Run_Status__NO_JOB = 0
        static_int_Run_Status__NOMINAL = 1
        static_int_Run_Status__REQUESTED = 2
        static_int_Run_Status__INITIATED = 3
        static_int_Run_Status__STARTED = 4
        static_int_Run_Status__ENDED = 5
        static_int_Run_Status__COMPLETED = 6
        static_int_Run_Status__USER_EDITS_FORCE_RERUN = 7
        static_int_Run_Status__FAILED = 99

        
        static_str_Run_Status__NO_JOB = 'NO_JOB'
        static_str_Run_Status__NOMINAL = 'NOMINAL'
        static_str_Run_Status__REQUESTED = 'REQUESTED'
        static_str_Run_Status__INITIATED = 'INITIATED'
        static_str_Run_Status__STARTED = 'STARTED'
        static_str_Run_Status__FAILED_CAUGHT = 'FAILED_CAUGHT'
        static_str_Run_Status__FAILED_UNCAUGHT = 'FAILED_UNCAUGHT'
        static_str_Run_Status__ENDED = 'ENDED'
        static_str_Run_Status__COMPLETED = 'COMPLETED'
        static_str_Run_Status__USER_EDITS_FORCE_RERUN = 'USER_EDITS_FORCE_RERUN'

    class Job_Status_Flag(object):
        
        static_str_Job_Status_Flags__NOMINAL = 'NOMINAL'
        static_str_Job_Status_Flags__JOB_STATUS_REQUESTED = 'JOB_STATUS_REQUESTED'
        static_str_Job_Status_Flags__NOT_TERMINATED = 'NOT_TERMINATED'
        static_str_Job_Status_Flags__REQUESTED = 'REQUESTED'
        static_str_Job_Status_Flags__INITIATED = 'INITIATED'
        static_str_Job_Status_Flags__STARTED = 'STARTED'
        static_str_Job_Status_Flags__IN_PROGRESS = 'IN_PROGRESS'
        static_str_Job_Status_Flags__ENDED = 'ENDED'        
        static_str_Job_Status_Flags__COMPLETED = 'COMPLETED'        
        static_str_Job_Status_Flags__USER_EDITS_FORCE_RERUN = 'USER_EDITS_FORCE_RERUN'
        
        static_str_Job_Status_Flags__TERMINATED = 'TERMINATED'
        static_str_Job_Status_Flags__STATUS_PATH_NOT_FOUND = 'STATUS_PATH_NOT_FOUND'
        static_str_Job_Status_Flags__FAILED_CAUGHT = 'FAILED_CAUGHT'
        static_str_Job_Status_Flags__FAILED_UNCAUGHT = 'FAILED_UNCAUGHT'
        static_str_Job_Status_Flags__JOB_SHELL_PID_NOT_FOUND = 'JOB_SHELL_PID_NOT_FOUND'
        static_str_Job_Status_Flags__JOB_PID_NOT_FOUND = 'JOB_PID_NOT_FOUND'

         
    class Run_Origin(object):
        
        static_str_Run_Started_From_IDE = 'IDE'
        
    class Debug(object):
        
        static_global_Debug = False
                
    class Pause_Console(object): 
        
        def __init__(self):
            return None
        
        def __enter__(self):
            return self
                       
        def method_Pause_Console(self, str_Message='', bool_Location=True):
            bool_Kill_Switch_Off = True
            
            if bool_Kill_Switch_Off:
                
                str_Message += '>> '
                
                if bool_Location:
                    with dcb_Debug_Location() as obj_DebugLoc:
                        str_Message += obj_DebugLoc.Get_Debug_Location(bool_Short=True)
                    pass
                pass
                if str_Message == '':
                    str_Message += ' << Pausing for output review -'
                pass
                
                
                raw_input('\n' + str_Message + ' << Press return to continue... \n')
            pass
        
            return True

        def __exit__(self, *args):
            return None

    class DateTimeVariables(object):
        
        dateTimeSinceLastGeneralMessage = timedelta
        
        def method_Get_DateTime_General_Message(self):
            
            dateTimeLastGeneralMessage = globals_SharkSim.global_dateTimeLastGeneralMessage
            
            globals_SharkSim.global_dateTimeLastGeneralMessage = datetime.now()
            
            return dateTimeLastGeneralMessage
        
        def method_Get_Time_Since_Last_General_Message(self):
            
            dateTimeLastGeneralMessage = self.method_Get_DateTime_General_Message()
            
            dateTimeNow = datetime.now()
            
            dateTimeSinceLastGeneralMessage = dateTimeNow - dateTimeLastGeneralMessage
            
            return dateTimeSinceLastGeneralMessage
    
        
    class Output_Display_Constants(object):
        
        static_str_Message_Separator = '-------------------------------------------------------------------------------------'        
        static_str_Message_Header = 'MH-------------------------------------------------------------------------------------MH'        
        static_str_Message_Footer = 'MF-------------------------------------------------------------------------------------MF'        

    class StringDelimiters(object):
        
        static_stringDelimiter = ';'
        static_stringDelimiter1 = '_'
        static_stringDelimiter2 = ','
        static_stringDelimiter3 = '|'
        static_stringDelimiterTAB = '\t'
        static_stringDelimiterSPACE = ' '
        static_stringDelimiter_SPACE = ' '
        static_stringDelimiter_RESULTS_START = '<>'
        static_stringDelimiter_DOT = '.'
        static_stringDelimiter_UNDERSCORE = '_'
        static_stringDelimiter_HYPHEN = '-'
        static_stringDelimiter_SEMI_COLON = ';'
        static_stringDelimiter_COMMA = ','
        
    class StringUnexpectedResults(object):
        
        static_stringError_Reporting_IDNotFound = 'ID_NOT_FOUND'
        static_stringNotApplicable = 'NA'
        static_stringSuppressed = 'SUP'
        static_stringError_ReportingPropertyNameNotFound = 'PROP NAME NOT FOUND'
        static_stringError_ReportingPropertyObjectNotFound = 'PROP NOT FOUND'
        static_stringError_ReportingPropertyLabelsNotFound = 'PROP LABELS NOT FOUND'

    class Logger_Run_Display(object):
        
        bool_Run_Display = True #You will not want to turn this off.
        
        static_Logger_File_Name__Run_Display = 'Run_Display_Log'
        static_Logger_Name__Run_Display = 'log_Run_Display'
        static_Logger_File_Suffix__Run_Display = '.log_Run_Display_ssim'
        
    class Logger_Default_Display(object):
        
        bool_Default_Display = True #You will not want to turn this off.
        
        static_Logger_File_Name__Default_Display = 'Default_Display_Log'
        static_Logger_Name__Default_Display = 'log_Default_Display'
        static_Logger_File_Suffix__Default_Display = '.log_Default_Display_ssim'
        
        static_Logger_bool_LogToConsole = True
        static_Logger_bool_LogToFile = True #You will not want to turn this off.
        
    class Logger_Error_Display(object):
        
        bool_Error_Display = True #You will not want to turn this off.
        
        static_Logger_File_Name__Error_Display = 'Error_Display_Log'
        static_Logger_Name__Error_Display = 'log_Error_Display'
        static_Logger_File_Suffix__Error_Display = '.log_Error_Display_ssim'

        static_Logger_bool_LogToConsole = False
        static_Logger_bool_LogToFile = False
        
        static_str_Logger_Message_Prefix = '!!ERR!!; '
        
    class Logger_Debug_Display(object):
        
        bool_Debug_Display = True #You will not want to turn this off.
        
        static_Logger_File_Name__Debug_Display = 'Debug_Display_Log'
        static_Logger_Name__Debug_Display = 'log_Debug_Display'
        static_Logger_File_Suffix__Debug_Display = '.log_Debug_Display_ssim'

        static_Logger_bool_LogToConsole = False
        static_Logger_bool_LogToFile = True #You will not want to turn this off.
        
        static_str_Logger_Message_Prefix = '>>; '
        
    class Logger_Debug_AgeNe(object):
        
        bool_Debug_AgeNe = True
        
        static_Logger_File_Name__Debug_AgeNe = 'Debug__AgeNe_Log'
        static_Logger_Name__Debug_AgeNe = 'log_Debug__AgeNe'
        static_Logger_File_Suffix__Debug_AgeNe = '.log_Debug__AgeNe_ssim'

        static_Logger_bool_LogToConsole = False
        static_Logger_bool_LogToFile = True

        static_str_Logger_Message_Prefix = '>>; '

    class Logger_Debug_Timing(object):
        
        bool_Debug_Timing_Override = False #Use this to just create the logger and use manually placed timers in the code
        
        bool_Debug_Timing = False #Use this to display timings on all functions that has this standard debug timer
        
        bool_Debug_Timing__Pause = False
        
        static_Logger_File_Name__Debug_Timing = 'Debug_Timing_Log'
        static_Logger_Name__Debug_Timing = 'log_Debug_Timing'
        static_Logger_File_Suffix__Debug_Timing = '.log_Debug_Timing_ssim'

    class PyQT4_QEvent_Type(object):
        
        static_dict_PyQT4_QEvent_Type = OrderedDict()
        static_dict_PyQT4_QEvent_Type[0] = 'QEvent.None'
        static_dict_PyQT4_QEvent_Type[1] = 'QEvent.Timer'
        static_dict_PyQT4_QEvent_Type[2] = 'QEvent.MouseButtonPress'
        static_dict_PyQT4_QEvent_Type[3] = 'QEvent.MouseButtonRelease'
        static_dict_PyQT4_QEvent_Type[4] = 'QEvent.MouseButtonDblClick'
        static_dict_PyQT4_QEvent_Type[5] = 'QEvent.MouseMove'
        static_dict_PyQT4_QEvent_Type[6] = 'QEvent.KeyPress'
        static_dict_PyQT4_QEvent_Type[7] = 'QEvent.KeyRelease'
        static_dict_PyQT4_QEvent_Type[8] = 'QEvent.FocusIn'
        static_dict_PyQT4_QEvent_Type[9] = 'QEvent.FocusOut'
        static_dict_PyQT4_QEvent_Type[10] = 'QEvent.Enter'
        static_dict_PyQT4_QEvent_Type[11] = 'QEvent.Leave'
        static_dict_PyQT4_QEvent_Type[12] = 'QEvent.Paint'
        static_dict_PyQT4_QEvent_Type[13] = 'QEvent.Move'
        static_dict_PyQT4_QEvent_Type[14] = 'QEvent.Resize'
        static_dict_PyQT4_QEvent_Type[17] = 'QEvent.Show'
        static_dict_PyQT4_QEvent_Type[18] = 'QEvent.Hide'
        static_dict_PyQT4_QEvent_Type[19] = 'QEvent.Close'
        static_dict_PyQT4_QEvent_Type[21] = 'QEvent.ParentChange'
        static_dict_PyQT4_QEvent_Type[24] = 'QEvent.WindowActivate'
        static_dict_PyQT4_QEvent_Type[25] = 'QEvent.WindowDeactivate'
        static_dict_PyQT4_QEvent_Type[26] = 'QEvent.ShowToParent'
        static_dict_PyQT4_QEvent_Type[27] = 'QEvent.HideToParent'
        static_dict_PyQT4_QEvent_Type[31] = 'QEvent.Wheel'
        static_dict_PyQT4_QEvent_Type[33] = 'QEvent.WindowTitleChange'
        static_dict_PyQT4_QEvent_Type[34] = 'QEvent.WindowIconChange'
        static_dict_PyQT4_QEvent_Type[35] = 'QEvent.ApplicationWindowIconChange'
        static_dict_PyQT4_QEvent_Type[36] = 'QEvent.ApplicationFontChange'
        static_dict_PyQT4_QEvent_Type[37] = 'QEvent.ApplicationLayoutDirectionChange'
        static_dict_PyQT4_QEvent_Type[38] = 'QEvent.ApplicationPaletteChange'
        static_dict_PyQT4_QEvent_Type[39] = 'QEvent.PaletteChange'
        static_dict_PyQT4_QEvent_Type[40] = 'QEvent.Clipboard'
        static_dict_PyQT4_QEvent_Type[43] = 'QEvent.MetaCall'
        static_dict_PyQT4_QEvent_Type[50] = 'QEvent.SockAct'
        static_dict_PyQT4_QEvent_Type[51] = 'QEvent.ShortcutOverride'
        static_dict_PyQT4_QEvent_Type[52] = 'QEvent.DeferredDelete'
        static_dict_PyQT4_QEvent_Type[60] = 'QEvent.DragEnter'
        static_dict_PyQT4_QEvent_Type[61] = 'QEvent.DragMove'
        static_dict_PyQT4_QEvent_Type[62] = 'QEvent.DragLeave'
        static_dict_PyQT4_QEvent_Type[63] = 'QEvent.Drop'
        static_dict_PyQT4_QEvent_Type[68] = 'QEvent.ChildAdded'
        static_dict_PyQT4_QEvent_Type[69] = 'QEvent.ChildPolished'
        static_dict_PyQT4_QEvent_Type[70] = 'QEvent.ChildInserted'
        static_dict_PyQT4_QEvent_Type[71] = 'QEvent.ChildRemoved'
        static_dict_PyQT4_QEvent_Type[74] = 'QEvent.PolishRequest'
        static_dict_PyQT4_QEvent_Type[75] = 'QEvent.Polish'
        static_dict_PyQT4_QEvent_Type[76] = 'QEvent.LayoutRequest'
        static_dict_PyQT4_QEvent_Type[77] = 'QEvent.UpdateRequest'
        static_dict_PyQT4_QEvent_Type[78] = 'QEvent.UpdateLater'
        static_dict_PyQT4_QEvent_Type[82] = 'QEvent.ContextMenu'
        static_dict_PyQT4_QEvent_Type[83] = 'QEvent.InputMethod'
        static_dict_PyQT4_QEvent_Type[86] = 'QEvent.AccessibilityPrepare'
        static_dict_PyQT4_QEvent_Type[87] = 'QEvent.TabletMove'
        static_dict_PyQT4_QEvent_Type[88] = 'QEvent.LocaleChange'
        static_dict_PyQT4_QEvent_Type[89] = 'QEvent.LanguageChange'
        static_dict_PyQT4_QEvent_Type[90] = 'QEvent.LayoutDirectionChange'
        static_dict_PyQT4_QEvent_Type[92] = 'QEvent.TabletPress'
        static_dict_PyQT4_QEvent_Type[93] = 'QEvent.TabletRelease'
        static_dict_PyQT4_QEvent_Type[94] = 'QEvent.OkRequest'
        static_dict_PyQT4_QEvent_Type[96] = 'QEvent.IconDrag'
        static_dict_PyQT4_QEvent_Type[97] = 'QEvent.FontChange'
        static_dict_PyQT4_QEvent_Type[98] = 'QEvent.EnabledChange'
        static_dict_PyQT4_QEvent_Type[99] = 'QEvent.ActivationChange'
        static_dict_PyQT4_QEvent_Type[100] = 'QEvent.StyleChange'
        static_dict_PyQT4_QEvent_Type[101] = 'QEvent.IconTextChange'
        static_dict_PyQT4_QEvent_Type[102] = 'QEvent.ModifiedChange'
        static_dict_PyQT4_QEvent_Type[103] = 'QEvent.WindowBlocked'
        static_dict_PyQT4_QEvent_Type[104] = 'QEvent.WindowUnblocked'
        static_dict_PyQT4_QEvent_Type[105] = 'QEvent.WindowStateChange'
        static_dict_PyQT4_QEvent_Type[109] = 'QEvent.MouseTrackingChange'
        static_dict_PyQT4_QEvent_Type[110] = 'QEvent.ToolTip'
        static_dict_PyQT4_QEvent_Type[111] = 'QEvent.WhatsThis'
        static_dict_PyQT4_QEvent_Type[112] = 'QEvent.StatusTip'
        static_dict_PyQT4_QEvent_Type[113] = 'QEvent.ActionChanged'
        static_dict_PyQT4_QEvent_Type[114] = 'QEvent.ActionAdded'
        static_dict_PyQT4_QEvent_Type[115] = 'QEvent.ActionRemoved'
        static_dict_PyQT4_QEvent_Type[116] = 'QEvent.FileOpen'
        static_dict_PyQT4_QEvent_Type[117] = 'QEvent.Shortcut'
        static_dict_PyQT4_QEvent_Type[118] = 'QEvent.WhatsThisClicked'
        static_dict_PyQT4_QEvent_Type[119] = 'QEvent.AccessibilityHelp'
        static_dict_PyQT4_QEvent_Type[120] = 'QEvent.ToolBarChange'
        static_dict_PyQT4_QEvent_Type[121] = 'QEvent.ApplicationActivate'
        static_dict_PyQT4_QEvent_Type[122] = 'QEvent.ApplicationDeactivate'
        static_dict_PyQT4_QEvent_Type[123] = 'QEvent.QueryWhatsThis'
        static_dict_PyQT4_QEvent_Type[124] = 'QEvent.EnterWhatsThisMode'
        static_dict_PyQT4_QEvent_Type[125] = 'QEvent.LeaveWhatsThisMode'
        static_dict_PyQT4_QEvent_Type[126] = 'QEvent.ZOrderChange'
        static_dict_PyQT4_QEvent_Type[127] = 'QEvent.HoverEnter'
        static_dict_PyQT4_QEvent_Type[128] = 'QEvent.HoverLeave'
        static_dict_PyQT4_QEvent_Type[129] = 'QEvent.HoverMove'
        static_dict_PyQT4_QEvent_Type[130] = 'QEvent.AccessibilityDescription'
        static_dict_PyQT4_QEvent_Type[131] = 'QEvent.ParentAboutToChange'
        static_dict_PyQT4_QEvent_Type[132] = 'QEvent.WinEventAct'
        static_dict_PyQT4_QEvent_Type[150] = 'QEvent.EnterEditFocus'
        static_dict_PyQT4_QEvent_Type[151] = 'QEvent.LeaveEditFocus'
        static_dict_PyQT4_QEvent_Type[153] = 'QEvent.MenubarUpdated'
        static_dict_PyQT4_QEvent_Type[155] = 'QEvent.GraphicsSceneMouseMove'
        static_dict_PyQT4_QEvent_Type[156] = 'QEvent.GraphicsSceneMousePress'
        static_dict_PyQT4_QEvent_Type[157] = 'QEvent.GraphicsSceneMouseRelease'
        static_dict_PyQT4_QEvent_Type[158] = 'QEvent.GraphicsSceneMouseDoubleClick'
        static_dict_PyQT4_QEvent_Type[159] = 'QEvent.GraphicsSceneContextMenu'
        static_dict_PyQT4_QEvent_Type[160] = 'QEvent.GraphicsSceneHoverEnter'
        static_dict_PyQT4_QEvent_Type[161] = 'QEvent.GraphicsSceneHoverMove'
        static_dict_PyQT4_QEvent_Type[162] = 'QEvent.GraphicsSceneHoverLeave'
        static_dict_PyQT4_QEvent_Type[163] = 'QEvent.GraphicsSceneHelp'
        static_dict_PyQT4_QEvent_Type[164] = 'QEvent.GraphicsSceneDragEnter'
        static_dict_PyQT4_QEvent_Type[165] = 'QEvent.GraphicsSceneDragMove'
        static_dict_PyQT4_QEvent_Type[166] = 'QEvent.GraphicsSceneDragLeave'
        static_dict_PyQT4_QEvent_Type[167] = 'QEvent.GraphicsSceneDrop'
        static_dict_PyQT4_QEvent_Type[168] = 'QEvent.GraphicsSceneWheel'
        static_dict_PyQT4_QEvent_Type[169] = 'QEvent.KeyboardLayoutChange'
        static_dict_PyQT4_QEvent_Type[170] = 'QEvent.DynamicPropertyChange'
        static_dict_PyQT4_QEvent_Type[171] = 'QEvent.TabletEnterProximity'
        static_dict_PyQT4_QEvent_Type[172] = 'QEvent.TabletLeaveProximity'
        static_dict_PyQT4_QEvent_Type[173] = 'QEvent.NonClientAreaMouseMove'
        static_dict_PyQT4_QEvent_Type[174] = 'QEvent.NonClientAreaMouseButtonPress'
        static_dict_PyQT4_QEvent_Type[175] = 'QEvent.NonClientAreaMouseButtonRelease'
        static_dict_PyQT4_QEvent_Type[176] = 'QEvent.NonClientAreaMouseButtonDblClick'
        static_dict_PyQT4_QEvent_Type[177] = 'QEvent.MacSizeChange'
        static_dict_PyQT4_QEvent_Type[178] = 'QEvent.ContentsRectChange'
        static_dict_PyQT4_QEvent_Type[181] = 'QEvent.GraphicsSceneResize'
        static_dict_PyQT4_QEvent_Type[182] = 'QEvent.GraphicsSceneMove'
        static_dict_PyQT4_QEvent_Type[183] = 'QEvent.CursorChange'
        static_dict_PyQT4_QEvent_Type[184] = 'QEvent.ToolTipChange'
        static_dict_PyQT4_QEvent_Type[186] = 'QEvent.GrabMouse'
        static_dict_PyQT4_QEvent_Type[187] = 'QEvent.UngrabMouse'
        static_dict_PyQT4_QEvent_Type[188] = 'QEvent.GrabKeyboard'
        static_dict_PyQT4_QEvent_Type[189] = 'QEvent.UngrabKeyboard'
        static_dict_PyQT4_QEvent_Type[192] = 'QEvent.StateMachineSignal'
        static_dict_PyQT4_QEvent_Type[193] = 'QEvent.StateMachineWrapped'
        static_dict_PyQT4_QEvent_Type[194] = 'QEvent.TouchBegin'
        static_dict_PyQT4_QEvent_Type[195] = 'QEvent.TouchUpdate'
        static_dict_PyQT4_QEvent_Type[196] = 'QEvent.TouchEnd'
        static_dict_PyQT4_QEvent_Type[198] = 'QEvent.Gesture'
        static_dict_PyQT4_QEvent_Type[199] = 'QEvent.RequestSoftwareInputPanel'
        static_dict_PyQT4_QEvent_Type[200] = 'QEvent.CloseSoftwareInputPanel'
        static_dict_PyQT4_QEvent_Type[202] = 'QEvent.GestureOverride'
        static_dict_PyQT4_QEvent_Type[203] = 'QEvent.WinIdChange'
        static_dict_PyQT4_QEvent_Type[212] = 'QEvent.PlatformPanel'
 
        
        
        
        