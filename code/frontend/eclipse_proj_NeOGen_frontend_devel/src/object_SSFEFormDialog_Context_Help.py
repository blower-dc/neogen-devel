'''
Created on 29 Jan 2015

@author: dblowe
'''
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS
#
#------------------< Import python modules
# DEBUG Imports
from logging import getLogger as logging__getLogger
from handler_Debug import Timer2
from handler_Debug import Debug_Location as dcb_Debug_Location
#
import traceback
#
import sys
#
from datetime import datetime
#
from PyQt4 import QtCore, QtGui, uic
#from __builtin__ import True
#from PyQt4.QtGui import QApplication
qtDesigner_Dialog_Context_Help = uic.loadUiType("SharkSimFE_CURRENT_HELP_NONMODAL_DIALOG_WV.ui")[0]  

from os import path as os__path
from collections import OrderedDict
 
#------------------< Import DCB_General modules
from FileHandler import FileHandler
from handler_Logging import Logging
#------------------< Import SharkSimFE modules
from globals_SharkSimFE import globalsSSFE
from SSConfigHandler import SSConfigOperation
from object_SSConfigFiles import object_SSConfigFiles
from object_SSConfigSettings import object_SSConfigSettings
from object_SSConfigProjects import object_SSConfigProjects
from object_SSConfigProject import object_SSConfigProject
from object_SSConfigBatchScenario import object_SSConfigBatchScenario
from object_SSConfigBatchSettings import object_SSConfigBatchSettings
from object_SSConfigSamplingStrategy import object_SSConfigSamplingStrategy
from object_SSFEWidget_Slider_Sample_Proportions import Ui_QWidget_Slider_Sample_Proportions
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION


#class object_SSFEFormMain(QWidget):
#self.setWindowTitle("NeSharkSim")
#return None

class Ui_Dialog_Context_Help(QtGui.QDialog, qtDesigner_Dialog_Context_Help):

    
    '''
    -------------------------------------------------------------------------------
        Initialse
    -------------------------------------------------------------------------------
    '''
    def __init__(self, parent = None):
                
        ''' Flag that INIT has STARTED '''
        self.bool_Init_Finished = False

        '''
        -------------------------------------------
        Get PARENT FORM Details
        -------------------------------------------
        '''      
        self.qForm_Main = parent
        #self.qForm_Controlling = self.qForm_Main_Main_Form
        '''
        -------------------------------------------
        Initialise LOGGERS
        -------------------------------------------
        '''
        ''' Get all the loggers required for monitoring this object '''
        #self.func_Initialise_Monitor_Loggers()
        
        '''
        -------------------------------------------
        Initialise ERROR HANDLING
        -------------------------------------------
        '''        
        ''' Indercept and handle uncaught exceptions '''
        #sys.excepthook = self.func_Error_Handler__UNCaught_Exceptions
        
        '''
        -------------------------------------------
        Initialise VARIABLES
        -------------------------------------------
        '''
        self.func_Initialise_Variables__Pre_Settings_Load()
                       
        '''
        -------------------------------------------
        Initialise DIALOG FORM WINDOW
        -------------------------------------------
        '''
        super(Ui_Dialog_Context_Help, self).__init__(self.qForm_Main)
        self.setupUi(self)
        

        
        '''
        -------------------------------------------
        Initialise EVENT FILTERS
        -------------------------------------------
        '''        
        self.func_Bind_Event_Filters()
        self.func_Bind_Event_Handlers()

        '''
        -------------------------------------------
        Initialise VALIDATORS & WIDGETS
        -------------------------------------------
        '''        
        #self.func_Initialise_Validators__Post_Settings_Load()
        self.func_Initialise_Widgets__Post_Settings_Load()

        '''
        -------------------------------------------
        Add Dialog WIDGETS
        -------------------------------------------
        '''        
        self.func_Add_Widgets__Post_Settings_Load()
        

        #self.func_Populate_Widgits_With_Config_Data()      
                  
                  
        #self.func_Enable_Apply_Values_Widgets()
        
        ''' Flag that INIT has finished '''
        self.bool_Init_Finished = True
        return None

    def func_Initialise_Variables__Pre_Settings_Load(self):

        self.func_Initialise_Variables__Dialog_Form()
        return True

    def func_Initialise_Variables__Dialog_Form(self):
        
        self.bool_SliderMouseButtonReleased = False
               
        return True
    
    def func_Initialise_Validators__Post_Settings_Load(self):
    
        ''' reg exs '''
        qregexp_Alpha = QtCore.QRegExp("[a-z-A-Z]+")        
        qregexp_Alphanumeric_0 = QtCore.QRegExp("[a-zA-Z0-9]+")        
        qregexp_Alphanumeric_1 = QtCore.QRegExp("[a-zA-Z0-9_-\s]+")        
        qregexp_Numeric_1 = QtCore.QRegExp("[0-9.]+")        
        
        ''' Apply single value'''
#         qregexpvalidator_lineEdit = QtGui.QRegExpValidator(qregexp_Numeric_1, self.lineEdit)
#         self.lineEdit.setValidator(qregexpvalidator_lineEdit)

        return True
    
    def func_Initialise_Widgets__Post_Settings_Load(self):
        
        self.func_Initialise_Widgets__Form()
        return True
    
    def func_Initialise_Widgets__Form(self):

        #self.textBrowser.setHtml('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/strict.dtd">')
        #self.textBrowser.setHtml('<p><big><big><big><big><big>This is a ANOTHER test</big></big></big></big></big></p>')
        #self.textBrowser.acceptRichText()
        
        if self.qForm_Main.bool_Settings_Context_Help_Display_At_Start__Default_Value:
            self.checkBox.blockSignals(True)
            self.checkBox.setChecked(True)
            self.checkBox.blockSignals(False)
        pass

        self.checkBox_2.setChecked(self.qForm_Main.bool_Context_Help__Follow_Context)
        
        ''' int_Genome_Alleles_Per_Locus_Distribution_BINOMIAL_StdDev_Alleles_Per_Locus - Settings'''
        self.int_Zoom_Factor__Step_Divisor = 100
        int_Zoom_Factor__Min = 75
        int_Zoom_Factor__Max = 175
        float_Zoom_Factor__Step = 0.05
        
        bool_Block_Signals = True
        self.horizontalSlider.blockSignals(bool_Block_Signals)
        self.horizontalSlider.setRange(int_Zoom_Factor__Min, int_Zoom_Factor__Max)
        self.horizontalSlider.setSingleStep(int(self.int_Zoom_Factor__Step_Divisor*float_Zoom_Factor__Step))
        
        int_Zoom_Factor = int(self.qForm_Main.float_Settings_Context_Help_Zoom_Factor__Default_Value * self.int_Zoom_Factor__Step_Divisor)

        
        self.horizontalSlider.setValue(int_Zoom_Factor)
        self.webView.setZoomFactor(self.qForm_Main.float_Settings_Context_Help_Zoom_Factor__Default_Value)
        bool_Block_Signals = False
        self.horizontalSlider.blockSignals(bool_Block_Signals)
                
        #self.webView.setZoomFactor(self.qForm_Main.float_Settings_Context_Help_Zoom_Factor__Default_Value)
        
        return True
    

    def func_Add_Widgets__Post_Settings_Load(self):
        
        self.func_Add_Custom_Slider_Widgets_To_QScrollArea()
        
        return True
    
    def func_Add_Custom_Slider_Widgets_To_QScrollArea(self):


        return True
        

    '''
    -------------------------------------------------------------------------------
        Native Events 
    -------------------------------------------------------------------------------
    '''
    def closeEvent(self, event):
        
        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, 'User has clicked cancel or the red x on the window')
        #DEBUG_OFF        

#         self.bool_Unsaved_Changes = self.func_UnSaved_Changes_Check()
#         
#         if self.bool_Unsaved_Changes:
#             str_MessageBox_Text = 'Changes have not been saved. Are you sure you wish to exit?'
#             messageBox_Reponse = QtGui.QMessageBox.question(self, 'Close window?', str_MessageBox_Text, buttons=QtGui.QMessageBox.Yes, defaultButton=QtGui.QMessageBox.No)
#          
#             if messageBox_Reponse == QtGui.QMessageBox.Yes:
#                 ''' End as gracefully as possible'''
#                 event.accept()
#             else:
#                 event.ignore()
#             pass
#         else:
#             event.accept()
#         pass
        self.qForm_Main.dialog_Context_Help = None
        
        return None

    '''
    -------------------------------------------------------------------------------
        Event filters
    -------------------------------------------------------------------------------
    '''

    def func_Bind_Event_Filters(self):
        
        self.func_Bind_Event_Filters__QSliders()
        
        return True

    def func_Bind_Event_Filters__QSliders(self):

        self.horizontalSlider.installEventFilter(self)

    def eventFilter(self, object, event):
 
        if object.objectName() == 'horizontalSlider':
            self.eventFilter__horizontalSlider(object, event)
            #return True #NOTE: uncommenting this return True or removing any above makes the control disappear!?
        else:
            pass
        pass
        return False

    def eventFilter__horizontalSlider(self, object, event):
 
        if event.type() == QtCore.QEvent.MouseButtonPress :
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; MouseButtonPress:"  + str(event.type()))
            return True
        elif event.type() == QtCore.QEvent.MouseButtonRelease :
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; MouseButtonRelease:"  + str(event.type()))
            '''set the mouse button pressed flag'''
            self.bool_SliderMouseButtonReleased = True
            ''' Get the slider value'''
            int_Object_Value = object.value()
            ''' Set the slider value '''         
            object.setValue(int_Object_Value)
            ''' Update config but dont Save file...yet'''
            self.bool_Slider_Engaged = False
            bool_Save = True
            self.func_Update__Zoom(object.objectName(), int_Object_Value, bool_Save)
            ''' Get the slider value to remember'''
            self.int_Slider_Orig_Value = int_Object_Value
            '''reset the mouse button pressed flag'''
            self.bool_SliderMouseButtonReleased = False
            return True
        elif event.type() == QtCore.QEvent.MouseMove :
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; MouseMove:"  + str(event.type()))
            return True
        elif event.type() == QtCore.QEvent.MouseTrackingChange :
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; MouseTrackingChange:"  + str(event.type()))
            return True
        elif event.type() == QtCore.QEvent.HoverEnter :
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; HoverEnter:"  + str(event.type()))
            '''Get slider value '''
            self.int_Slider_Orig_Value = object.value()
            self.bool_Slider_Engaged = True
            object.setFocus() #Set the focus so that the spinBox cannot be edited whilst slider is engaged
            return True
        elif event.type() == QtCore.QEvent.HoverMove :
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; HoverMove:"  + str(event.type()))
            ''' Get the mouse cursor x pos relative to the widget '''
            x = event.pos().x()
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; HoverMove X pos:"  + str(x))
            ''' Get the value of the slider to the value calculated from the mouse x pos '''
            int_Object_Value = QtGui.QStyle.sliderValueFromPosition (object.minimum(), object.maximum(), x, object.width())
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; HoverMove sliderValueFromPosition:"  + str(int_Object_Value))
            ''' Set the value of the slider to the value calculated from the mouse x pos '''
            ''' Set the slider and spinbox values '''
            object.setValue(int_Object_Value)
            ''' Dont update config but set the ranges for related sliders '''
            bool_Save = False
            self.func_Update__Zoom(object.objectName(), int_Object_Value, bool_Save)
            return True
        elif event.type() == QtCore.QEvent.HoverLeave :
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; HoverLeave:"  + str(event.type()))
            ''' Leaving the slider - if the mouse button hasnt been pressed reset the slider to its orig value'''
            if self.bool_SliderMouseButtonReleased == False:
                ''' Reset slider to original value '''
                ''' Get the slider value '''
                int_Slider_Value = self.int_Slider_Orig_Value
                ''' Set the slider and spinbox values '''
                object.setValue(int_Slider_Value)
            else:
                self.bool_SliderMouseButtonReleased = False
            pass
            self.bool_Slider_Engaged = False
            #self.func_Validate_Sampling_Strategy__Display_Combinations()
            return True
        elif event.type() == QtCore.QEvent.Enter :
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; Enter:"  + str(event.type()))
            return True
        elif event.type() == QtCore.QEvent.Leave :
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; Leave:"  + str(event.type()))
            return True
        elif event.type() == QtCore.QEvent.ToolTip :
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; ToolTip:"  + str(event.type()))
            return True
        else:
            #self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; Untrapped Event:"  + str(event.type()))
            pass
            #return True #NOTE: uncommenting this return True or removing any above makes the control disappear!?
        pass
        return False
    '''
    -------------------------------------------------------------------------------
        Bind signal handlers
    -------------------------------------------------------------------------------
    '''    
    def func_Bind_Event_Handlers(self):
        
        #self.func_Bind_Event_Handlers__QPushButton()
        self.func_Bind_Event_Handlers__QCheckBox()
        self.func_Bind_Event_Handlers__QSliders()
        
        return True

    def func_Bind_Event_Handlers__QPushButton(self):
        
        '''QPushButton - Apply Distribution to SEX'''
        #self.pushButton.clicked.connect(self.func_QPushButton_Clicked__Apply_Distribution) 
        
        
        return True

    def func_Bind_Event_Handlers__QCheckBox(self):
        
        '''QCheckBox - Select Show Help At Start '''
        self.checkBox.stateChanged["int"].connect(self.func_QCheckBox_SHOW_DIALOG_AT_STARTUP__StateChanged)
        '''QCheckBox - Select Follow Context'''
        self.checkBox_2.stateChanged["int"].connect(self.func_QCheckBox_FOLLOW_CONTEXT__StateChanged)
        
        return True
    
        '''
    -------------------------------------------------------------------------------
        Signal specific functions
    -------------------------------------------------------------------------------
    '''

    def func_Bind_Event_Handlers__QSliders(self):
        
        self.horizontalSlider.valueChanged["int"].connect(self.func_QHorizontalSlider__Zoom_Factor__SetValue)
        
        return True
    
    '''
    ----------------------------
    Base Form Widgets
    ----------------------------
    '''    
    def func_QCheckBox_SHOW_DIALOG_AT_STARTUP__StateChanged(self, int_State):
        
        if self.checkBox.isChecked():
            self.qForm_Main.bool_Settings_Context_Help_Display_At_Start__Default_Value = True
        else:
            self.qForm_Main.bool_Settings_Context_Help_Display_At_Start__Default_Value = False
        pass
    
        self.qForm_Main.func_Update_Config__Settings_Context_Help_Display_At_Start()
        
        return int_State

    def func_QCheckBox_FOLLOW_CONTEXT__StateChanged(self, int_State):
        
        if self.checkBox_2.isChecked():
            self.qForm_Main.bool_Context_Help__Follow_Context = True
        else:
            self.qForm_Main.bool_Context_Help__Follow_Context = False
        pass
    
        #self.qForm_Main.func_Update_Config__Settings_Context_Help_Display_At_Start()
        
        return int_State

    def func_QHorizontalSlider__Zoom_Factor__SetValue(self, int_Value):
    
        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF
        
        floatScaled_Value = float(int_Value)/float(self.int_Zoom_Factor__Step_Divisor)
        self.webView.setZoomFactor(floatScaled_Value)
        
        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '; int_Value:' + str(int_Value) + '; floatScaled_Value: ' + str(floatScaled_Value))
        #DEBUG_OFF        
        '''
        NOTE: use eventFilter for the majority of the logic for this widget.
        It cant seem to cope with extended logic here.
        '''
        return int_Value

    '''
    -------------------------------------------------------------------------------
    Save buttons
    -------------------------------------------------------------------------------
    '''

    def func_QPushButton_Clicked__Cancel_And_Exit(self):   
        
        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF        
    
        self.close()
        
        return True
    '''
    -------------------------------------------------------------------------------
        Signal downstream functions 
    -------------------------------------------------------------------------------
    ''' 

    def func_Update__Zoom(self, str_Object_Name, value_Object, bool_Save):
        
        if str_Object_Name == 'horizontalSlider':
            self.func_Update__Zoom_Factor(value_Object, bool_Save)
        pass
    
        return True

    def func_Update__Zoom_Factor(self, int_Value, bool_Save):

        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF
                
        if bool_Save:
            ''' Update config but dont Save file...yet'''
            float_Value_Scaled = float(int_Value)/float(self.int_Zoom_Factor__Step_Divisor)
            self.qForm_Main.float_Settings_Context_Help_Zoom_Factor__Default_Value = float_Value_Scaled
            #DEBUG_ON
            self.qForm_Main.func_Debug_Logging(False, 2, '; SAVE ; self.qForm_Main.float_Settings_Context_Help_Zoom_Factor__Default_Value: ' + str(float_Value_Scaled))
            #DEBUG_OFF                
            self.qForm_Main.func_Update_Config__Settings_Context_Help_Zoom_Factor()
            pass
        pass
    
        return True

    
    
    '''
    -------------------------------------------------------------------------------
        Messages & Logging
    -------------------------------------------------------------------------------
    '''           



                  
    '''
    --------------------------------------------------------------------------------------------------------
    # <<<<<<<<<<<<<<<<<< CLASS FINALIZATION
    --------------------------------------------------------------------------------------------------------
    '''       
    #def __exit__(self, type, value, traceback):
    def __exit__(self):
        
        return True
        