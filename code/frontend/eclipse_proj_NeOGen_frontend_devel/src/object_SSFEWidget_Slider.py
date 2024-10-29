'''
Created on 12 Feb 2016

@author: Dean Blower
'''
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS
#
#------------------< Import python modules

from PyQt4 import QtCore, QtGui, uic
qtDesigner_QWidget_Slider = uic.loadUiType("SharkSimFE_CUSTOM_WIDGET_DOUBLE_SPINBOX_SLIDER.ui")[0]  
#------------------< Import DCB_General modules
# DEBUG Imports
from logging import getLogger as logging__getLogger
from handler_Debug import Timer2
from handler_Debug import Debug_Location as dcb_Debug_Location
#
#from FileHandler import FileHandler
from handler_Logging import Logging
#------------------< Import SharkSimFE modules
from globals_SharkSimFE import globalsSSFE
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION


class Ui_QWidget_Slider(QtGui.QWidget, qtDesigner_QWidget_Slider):
    '''
    classdocs
    '''
    __slots__ = (
               #PROPERTIES
               'prop_int_Slider_Value_Step_Divisor'
               ,'prop_int_Slider__Default_Value'
               ,'prop_int_Slider__Min'
               ,'prop_int_Slider__Max'
               ,'prop_int_DoubleSpinBox__Decimals'
               ,'prop_float_DoubleSpinBox__Min'
               ,'prop_float_DoubleSpinBox__Max'
               )
    

    def __init__(self, parent = None):

        ''' Flag that INIT has STARTED '''
        self.bool_Init_Finished = False

        '''
        -------------------------------------------
        Get PARENT FORM Details
        -------------------------------------------
        '''      
        self.qForm_Main = parent
        
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
        Initialise CUSTOM QWIDGET
        -------------------------------------------
        '''        
        super(QtGui.QWidget,self).__init__(self.qForm_Main)
        self.setupUi(self)

        '''
        -------------------------------------------
        Add WIDGETS
        -------------------------------------------
        '''        
        #self.func_Add_Widgets__Post_Settings_Load()
        
        '''
        -------------------------------------------
        Initialise EVENT FILTERS
        -------------------------------------------
        '''        
        self.func_Bind_Event_Filters()
        self.func_Bind_Event_Handlers()

        return None

    def func_Initialise_Class(self):
        
        #VARIABLES
        self.int_Slider_Value_Step_Divisor = 0
        self.float_Widget_Value__Default = 0
        
        #PROPERTIES -> VARIABLES
        self.int_Slider_Value_Step_Divisor = self.prop_int_Slider_Value_Step_Divisor
        self.int_Slider__Default_Value = self.prop_int_Slider__Default_Value
        self.int_Slider__Min = self.prop_int_Slider__Min
        self.int_Slider__Max = self.prop_int_Slider__Max
        self.int_DoubleSpinBox__Decimals = self.prop_int_DoubleSpinBox__Decimals
        self.float_DoubleSpinBox__Min = self.prop_float_DoubleSpinBox__Min
        self.float_DoubleSpinBox__Max = self.prop_float_DoubleSpinBox__Max
        
        '''
        -------------------------------------------
        Initialise VALIDATORS & WIDGETS
        -------------------------------------------
        '''        
        self.func_Initialise_Widgets__Post_Settings_Load()
        
        ''' Flag that INIT has finished '''
        self.bool_Init_Finished = True        
        
        return True
    
    def func_Initialise_Monitor_Loggers(self):
        
        ''' 
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Get all the loggers required for monitoring this object
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        ''' Get Run Display Logger '''
        self.obj_Log_Run_Display = logging__getLogger(globalsSSFE.Logger_Run_Display.static_Logger_Name__Run_Display)
                    
        ''' Get Default Logger '''
        self.obj_Log_Default_Display = logging__getLogger(globalsSSFE.Logger_Default_Display.static_Logger_Name__Default_Display)
 
        ''' Get Debug Logger '''
        self.obj_Log_Debug_Display = logging__getLogger(globalsSSFE.Logger_Debug_Display.static_Logger_Name__Debug_Display)
 
        ''' Get Debug Timer '''
        self.obj_Log_Debug_Timing = None
        if globalsSSFE.Logger_Debug_Timing.bool_Debug_Timing:
            self.obj_Log_Debug_Timing = logging__getLogger(globalsSSFE.Logger_Debug_Timing.static_Logger_Name__Debug_Timing)
        pass

        ''' Get Debug Events Logger '''
        self.obj_Log_Debug_Events = None
        if globalsSSFE.Logger_Debug_Events.bool_Debug_Events:
            self.obj_Log_Debug_Events = logging__getLogger(globalsSSFE.Logger_Debug_Events.static_Logger_Name__Debug_Events)
        pass
                                 
        return True

    
    def func_Initialise_Variables__Pre_Settings_Load(self):

        self.func_Initialise_Variables__Custom_Widget()
        return True

    def func_Initialise_Variables__Custom_Widget(self):

        ''' Check if Slider is being interacted with '''
        self.bool_Slider_Engaged = False
        ''' Check if Slider has had its mouse button released thereby setting its value '''
        self.bool_SliderMouseButtonReleased = False
        
        return True
    
    def func_Initialise_Widgets__Post_Settings_Load(self):
        
        self.func_Initialise_Widgets__Custom_Widget()
        return True

    def func_Initialise_Widgets__Custom_Widget(self):

        ''' Linked slider and spinbox - Settings'''
        self.verticalSlider.setRange(self.int_Slider_Value_Step_Divisor*self.int_Slider__Min
                                          ,self.int_Slider_Value_Step_Divisor*self.int_Slider__Max)
        self.verticalSlider.setSingleStep(1)
        self.doubleSpinBox.setDecimals(self.int_DoubleSpinBox__Decimals)
        self.doubleSpinBox.setRange(self.float_DoubleSpinBox__Min
                                      ,self.float_DoubleSpinBox__Max)
        self.doubleSpinBox.setSingleStep(float(1)/float(self.int_Slider_Value_Step_Divisor))
        self.verticalSlider.setValue(self.int_Slider_Value_Step_Divisor*self.int_Slider__Default_Value)


        return True

       
        '''
    -------------------------------------------------------------------------------
        Event filters
    -------------------------------------------------------------------------------
    '''

    def func_Bind_Event_Filters(self):
        
        self.func_Bind_Event_Filters__QSliders()
        
        return True

    def func_Bind_Event_Filters__QSliders(self):

        self.verticalSlider.installEventFilter(self)    
   
        return True
        
    def eventFilter(self, object, event):
 
        if isinstance(object, QtGui.QSlider):
            self.eventFilter__QSlider(object, event)
            #return True #NOTE: uncommenting this return True or removing any above makes the control disappear!?
        else:
            pass
        pass
        return False

    def eventFilter__QSlider(self, object, event):
 
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
            bool_Save = True
            #self.func_Update__Sampling_Strategy_Run_Parameters(object.objectName(), int_Object_Value, bool_Save)
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
            ''' Get the mouse cursor y pos relative to the widget '''
            y = event.pos().y()
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; HoverMove Y pos:"  + str(y) + '; object max: ' + str(object.maximum()) + '; object in: ' + str(object.minimum()))
            ''' Get the value of the slider to the value calculated from the mouse x pos '''
            int_Object_Value = QtGui.QStyle.sliderValueFromPosition (object.minimum(), object.maximum(), y, object.height(), upsideDown = True)
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; HoverMove sliderValueFromPosition:"  + str(int_Object_Value))
            ''' Set the value of the slider to the value calculated from the mouse x pos '''
            ''' Set the slider and spinbox values '''
            object.setValue(int_Object_Value)
            ''' Dont update config but set the ranges for related sliders '''
            bool_Save = False
            #self.func_Update__Sampling_Strategy_Run_Parameters(object.objectName(), int_Object_Value, bool_Save)
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
            return True
        elif event.type() == QtCore.QEvent.Enter :
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; Enter:"  + str(event.type()))
            #self.bool_Slider_Engaged = True
            return True
        elif event.type() == QtCore.QEvent.Leave :
            self.qForm_Main.func_Debug_Logging(True, 2, str(object.staticMetaObject.className()) + '; ' + str(object.objectName()) + "; Leave:"  + str(event.type()))
            #self.bool_Slider_Engaged = False
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
        
        self.func_Bind_Event_Handlers__Joined_QSliders_And_QSpinBoxes()
        
        return True
    
    def func_Bind_Event_Handlers__Joined_QSliders_And_QSpinBoxes(self):
        
        self.verticalSlider.valueChanged["int"].connect(self.func_QVerticalSlider__SetValue)
        self.doubleSpinBox.valueChanged["double"].connect(self.func_QDoubleSpinBox__SetValue)


        return True

    '''
    -------------------------------------------------------------------------------
        Signal specific functions
    -------------------------------------------------------------------------------
    '''

    '''
    ----------------------------
    Base Form Widgets
    ----------------------------
    '''    


    def func_QDoubleSpinBox__SetValue(self, float_Value):
    
        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF
        
        intScaled_Value = int(round(float_Value*self.int_Slider_Value_Step_Divisor,0))
        self.verticalSlider.setValue(intScaled_Value)

#         if self.bool_Init_Finished:
#             if self.bool_Reload_Widgets_Finished__Batch_Scenario:
#                 #self.func_Debug_Logging(False, 2, '; self.bool_Slider_Engaged: ' + str(self.bool_Slider_Engaged))
#                 if not self.bool_Slider_Engaged:
#                     ''' Update widgets and config with changes '''
#                     bool_Save = True
#                     self.func_Update__Genome_Alleles_Per_Locus_Distribution_BINOMIAL_StdDev_Alleles_Per_Locus(float_Value, bool_Save)
#                 pass
#             pass
#         pass             
        return float_Value
    
    def func_QVerticalSlider__SetValue(self, int_Value):
    
        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF
        
        floatScaled_Value = float(int_Value)/float(self.int_Slider_Value_Step_Divisor)
        self.doubleSpinBox.setValue(floatScaled_Value)
        
        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '; int_Value:' + str(int_Value) + '; floatScaled_Value: ' + str(floatScaled_Value))
        #DEBUG_OFF        
        '''
        NOTE: use eventFilter for the majority of the logic for this widget.
        It cant seem to cope with extended logic here.
        '''
        return int_Value 
       