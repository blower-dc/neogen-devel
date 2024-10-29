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
# from handler_Debug import Debug_Location as dcb_Debug_Location
# #
# import traceback
# #
# import sys
# #
# from datetime import datetime
#
from PyQt4 import QtCore, QtGui, uic
#from __builtin__ import True
#from PyQt4.QtGui import QApplication
qtDesigner_Dialog_Age_Cohort_Mortality_Rates = uic.loadUiType("SharkSimFE_CURRENT_DIALOG_AGE_COHORT_BY_SEX_MORTALITY.ui")[0]  

# from os import path as os__path
from collections import OrderedDict
from Tkinter import Tk as tkinter__Tk
import re 
#------------------< Import DCB_General modules
# from FileHandler import FileHandler
# from handler_Logging import Logging
# #------------------< Import SharkSimFE modules
from globals_SharkSimFE import globalsSSFE
# from SSConfigHandler import SSConfigOperation
# from object_SSConfigFiles import object_SSConfigFiles
# from object_SSConfigSettings import object_SSConfigSettings
# from object_SSConfigProjects import object_SSConfigProjects
# from object_SSConfigProject import object_SSConfigProject
# from object_SSConfigBatchScenario import object_SSConfigBatchScenario
# from object_SSConfigBatchSettings import object_SSConfigBatchSettings
# from object_SSConfigSamplingStrategy import object_SSConfigSamplingStrategy
from object_SSFEWidget_Slider import Ui_QWidget_Slider
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION


#class object_SSFEFormMain(QWidget):
#self.setWindowTitle("NeSharkSim")
#return None

class Ui_Dialog_Age_Cohort_Mortality_Rates(QtGui.QDialog, qtDesigner_Dialog_Age_Cohort_Mortality_Rates):

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
        super(Ui_Dialog_Age_Cohort_Mortality_Rates, self).__init__(self.qForm_Main)
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
        self.func_Initialise_Validators__Post_Settings_Load()
        self.func_Initialise_Widgets__Post_Settings_Load()

        '''
        -------------------------------------------
        Add Dialog WIDGETS
        -------------------------------------------
        '''        
        self.func_Add_Widgets__Post_Settings_Load()
        

        self.func_Populate_Widgits_With_Config_Data()      
                  
        ''' Check if the user want to allow changes '''
        self.bool_Allow_Save = self.func_Verify_Change()
        if self.bool_Allow_Save:
            self.pushButton.setEnabled(True) 
        else:
            self.pushButton.setEnabled(False)
        pass
    
        self.func_Enable_Apply_Values_Widgets()
        
        ''' Flag that INIT has finished '''
        self.bool_Init_Finished = True
        return None

    def func_Initialise_Variables__Pre_Settings_Load(self):

        self.func_Initialise_Variables__Dialog_Form()
        return True

    def func_Initialise_Variables__Dialog_Form(self):

        self.bool_Allow_Save = False
                
        ''' Check if Slider is being interacted with '''
        self.bool_Slider_Engaged = False
        self.bool_SpinBox_Engaged = False
        ''' Check if Slider has had its mouse button released thereby setting its value '''
        self.bool_SliderMouseButtonReleased = False
        self.bool_SpinBoxMouseButtonReleased = False

        self.dict_Species_Demographic_Natural_MORTALITY_CSV_Age_And_MORTALITY_Rate__MALE = OrderedDict()
        self.dict_Species_Demographic_Natural_MORTALITY_CSV_Age_And_MORTALITY_Rate__FEMALE = OrderedDict()

        self.int_Slider_Value_Step_Divisor = 1000
        self.int_Slider__Default_Value = 0
                        
        return True
    
    def func_Initialise_Validators__Post_Settings_Load(self):
    
        ''' reg exs '''
#         qregexp_Alpha = QtCore.QRegExp("[a-z-A-Z]+")        
#         qregexp_Alphanumeric_0 = QtCore.QRegExp("[a-zA-Z0-9]+")        
#         qregexp_Alphanumeric_1 = QtCore.QRegExp("[a-zA-Z0-9_-\s]+")        
#         qregexp_Numeric_1 = QtCore.QRegExp("[0-9.]+")        
#         
#         ''' Apply single value'''
#         qregexpvalidator_lineEdit = QtGui.QRegExpValidator(qregexp_Numeric_1, self.lineEdit)
#         self.lineEdit.setValidator(qregexpvalidator_lineEdit)

        return True
    
    def func_Initialise_Widgets__Post_Settings_Load(self):
        
        self.func_Initialise_Widgets__Form()
        return True
    
    def func_Initialise_Widgets__Form(self):

        self.setWindowTitle(self.qForm_Main.str_App_Name_And_Version + ' - ' + 'Edit Age Cohort Mortality Rates')
        
        ''' Age cohort custom widgets container Widget ''' 
        self.widget_Cohorts__MALE = QtGui.QWidget()
        self.widget_Cohorts__FEMALE = QtGui.QWidget()
        
        bool_Block_Signals = True
        self.checkBox.blockSignals(bool_Block_Signals)
        self.checkBox_2.blockSignals(bool_Block_Signals)
        #self.checkBox_3.blockSignals(bool_Block_Signals)
        self.checkBox_4.blockSignals(bool_Block_Signals)
        self.checkBox_5.blockSignals(bool_Block_Signals)
        
        
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        #self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        
#         self.checkBox.setEnabled(False)
#         self.checkBox_2.setEnabled(False)
#         #self.checkBox_3.setEnabled(False)
#         self.checkBox_4.setEnabled(True)
#         self.checkBox_5.setEnabled(True)

        bool_Block_Signals = False
        self.checkBox.blockSignals(bool_Block_Signals)
        self.checkBox_2.blockSignals(bool_Block_Signals)
        #self.checkBox_3.blockSignals(bool_Block_Signals)
        self.checkBox_4.blockSignals(bool_Block_Signals)
        self.checkBox_5.blockSignals(bool_Block_Signals)


        ''' Linked slider and spinbox - Settings'''
        #self.int_Slider_Value_Step_Divisor = 10
        self.int_DoubleSpinBox__Decimals = 3
        self.float_DoubleSpinBox__Min = 0
        self.float_DoubleSpinBox__Max = 1.000
        self.doubleSpinBox.setDecimals(self.int_DoubleSpinBox__Decimals)
        self.doubleSpinBox.setRange(self.float_DoubleSpinBox__Min
                                      ,self.float_DoubleSpinBox__Max)
        self.doubleSpinBox.setSingleStep(float(1)/float(self.int_Slider_Value_Step_Divisor))

        #QtGui.QGroupBox.isCheckable()
        self.groupBox_4.setCheckable(True)
        self.groupBox_4.setChecked(False)
        self.groupBox_5.setCheckable(True)
        self.groupBox_5.setChecked(False)
        
        #self.func_Enable_Apply_Values_Widgets()
        
        return True
    

    def func_Add_Widgets__Post_Settings_Load(self):
        
        self.func_Add_Custom_Slider_Widgets_To_QScrollArea()
        
        return True
    
    def func_Add_Custom_Slider_Widgets_To_QScrollArea(self):

        ''' Layout of Container Widget '''
        layout_Sliders__MALE = self.horizontalLayout_4
        layout_Sliders__FEMALE = self.horizontalLayout_6
        
        ''' Add custom widgets to layout '''
        for int_Age_Cohort in range(0, self.qForm_Main.int_Species_Life_History_Max_Age):
            qCustom_Widget__MALE = Ui_QWidget_Slider(self.qForm_Main)
            qCustom_Widget__FEMALE = Ui_QWidget_Slider(self.qForm_Main)
                
            ''' Set label colours '''
            if int_Age_Cohort == self.qForm_Main.int_Species_Life_History_Max_Age-1:
                qPalette = QtGui.QPalette()
                qPalette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
                qCustom_Widget__MALE.label.setPalette(qPalette)
                qCustom_Widget__FEMALE.label.setPalette(qPalette)
                ''' set font '''   
                qFont = QtGui.QFont()
                qFont.setPointSize(11);
                qFont.setBold(True)
                qCustom_Widget__MALE.label.setFont(qFont)  
                qCustom_Widget__FEMALE.label.setFont(qFont)             
            elif int_Age_Cohort >= self.qForm_Main.int_Species_Life_History_Min_Mating_Age and int_Age_Cohort <= self.qForm_Main.int_Species_Life_History_Max_Mating_Age-1:
                qPalette = QtGui.QPalette()
                qPalette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.gray)
                #qPalette.setColor(QtGui.QPalette.Background,QtCore.Qt.white)
                #qCustom_Widget__MALE.setAutoFillBackground(True)
                qCustom_Widget__MALE.label.setPalette(qPalette)
                qCustom_Widget__FEMALE.label.setPalette(qPalette)
                ''' set font '''   
                qFont = QtGui.QFont()
                qFont.setPointSize(11);
                qFont.setBold(True)
                qCustom_Widget__MALE.label.setFont(qFont) 
                qCustom_Widget__FEMALE.label.setFont(qFont)                              
            pass
                              
            ''' Initialise MALE custom widgets '''
            qCustom_Widget__MALE.prop_int_Slider_Value_Step_Divisor = self.int_Slider_Value_Step_Divisor
            qCustom_Widget__MALE.prop_int_Slider__Default_Value = self.int_Slider__Default_Value
            qCustom_Widget__MALE.prop_int_Slider__Min = 0
            qCustom_Widget__MALE.prop_int_Slider__Max = 1
            qCustom_Widget__MALE.prop_int_DoubleSpinBox__Decimals = 3
            qCustom_Widget__MALE.prop_float_DoubleSpinBox__Min = 0.00
            qCustom_Widget__MALE.prop_float_DoubleSpinBox__Max = 1.00            
            qCustom_Widget__MALE.func_Initialise_Class()

            qCustom_Widget__MALE.doubleSpinBox.setKeyboardTracking(False)          
            qCustom_Widget__MALE.label.setText(str(int_Age_Cohort) + ' - '+ str(int_Age_Cohort+1)) #Minus 1 to start at Zero and match the Demographic profile plot
            
            layout_Sliders__MALE.addWidget(qCustom_Widget__MALE)
            qCustom_Widget__MALE.setFixedWidth(70)
            
            ''' Initialise FEMALE custom widgets '''
            qCustom_Widget__FEMALE.prop_int_Slider_Value_Step_Divisor = self.int_Slider_Value_Step_Divisor
            qCustom_Widget__FEMALE.prop_int_Slider__Default_Value = self.int_Slider__Default_Value
            qCustom_Widget__FEMALE.prop_int_Slider__Min = 0
            qCustom_Widget__FEMALE.prop_int_Slider__Max = 1
            qCustom_Widget__FEMALE.prop_int_DoubleSpinBox__Decimals = 3
            qCustom_Widget__FEMALE.prop_float_DoubleSpinBox__Min = 0.00
            qCustom_Widget__FEMALE.prop_float_DoubleSpinBox__Max = 1.00            
            qCustom_Widget__FEMALE.func_Initialise_Class()

            qCustom_Widget__FEMALE.doubleSpinBox.setKeyboardTracking(False)
            qCustom_Widget__FEMALE.label.setText(str(int_Age_Cohort) + ' - '+ str(int_Age_Cohort+1)) #Minus 1 to start at Zero and match the Demographic profile plot
            
            layout_Sliders__FEMALE.addWidget(qCustom_Widget__FEMALE)
            qCustom_Widget__FEMALE.setFixedWidth(70)
            
        pass
           
        self.widget_Cohorts__MALE.setLayout(layout_Sliders__MALE)
        self.widget_Cohorts__FEMALE.setLayout(layout_Sliders__FEMALE)

        ''' Scroll Area Properties '''
        qScrollArea__MALE = self.scrollArea
        #scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        qScrollArea__MALE.setWidgetResizable(True)
        qScrollArea__MALE.setWidget(self.widget_Cohorts__MALE)
        ''' Scroll Area Properties '''
        qScrollArea__FEMALE = self.scrollArea_2
        #scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        qScrollArea__FEMALE.setWidgetResizable(True)
        qScrollArea__FEMALE.setWidget(self.widget_Cohorts__FEMALE)

        return True
        
    def add_new_slider(self):
        #slider = QtGui.QSlider()
        slider = Ui_QWidget_Slider(self.qForm_Main)
        self.widget_Cohorts__MALE.layout().addWidget(slider)
        #slider.installEventFilter(self)
        slider.setFixedWidth(60)

    def add_new_label_ALT(self):
        label = QtGui.QSlider()
        layout = self.widget.layout()
        layout.insertWidget(layout.count() - 1, label)
        label.installEventFilter(self)

    def func_Verify_Change(self):
        
        bool_Continue = False
        str_Object_Name = 'pushButton_6'
        qWidget_Engaged = self.qForm_Main.findChild(QtGui.QPushButton, str_Object_Name)
         
        ''' Verify if the change can proceed '''
        if self.qForm_Main.bool_Reload_Widgets_Finished__Batch_Scenario:
            list_Parameter_Groups = [globalsSSFE.Parameter_Group.static_str__Parameter_Group__BATCH_SCENARIO_PARAM]
            ''' Verify if the change can proceed '''
            int_Verify_Change__Warning_Count = self.qForm_Main.func_Verify_Change__Get_Warning_Count__Bind_Event_Filter_Downstream_Actions(str_Object_Name, list_Parameter_Groups)
            if int_Verify_Change__Warning_Count < 1:
                ''' Block signals to ensure editingChanged SIGNAL does not fire when MessageBox shown '''
                qWidget_Engaged.blockSignals(True)
                ''' Warn that other parameters that are dependent will have to be changed '''
                bool_Continue = self.qForm_Main.func_Verify_Change__Can_Change_Proceed__ANY_Scenario_PARAMETER()
                qWidget_Engaged.blockSignals(False)
            else:
                bool_Continue = True
            pass
        else:
            bool_Continue = True
        pass

        return bool_Continue
    
    '''
    -------------------------------------------------------------------------------
        Native Events 
    -------------------------------------------------------------------------------
    '''
    def closeEvent(self, event):
        
        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, 'User has clicked cancel or the red x on the window')
        #DEBUG_OFF        

        self.bool_Unsaved_Changes = self.func_UnSaved_Changes_Check()
        
        if self.bool_Allow_Save:
            self.bool_Unsaved_Changes = False
        pass
    
        if self.bool_Unsaved_Changes:
            str_MessageBox_Text = 'Changes have not been saved. Are you sure you wish to exit?'
            messageBox_Reponse = QtGui.QMessageBox.question(self, 'Close window?', str_MessageBox_Text, buttons=QtGui.QMessageBox.Yes, defaultButton=QtGui.QMessageBox.No)
         
            if messageBox_Reponse == QtGui.QMessageBox.Yes:
                ''' End as gracefully as possible'''
                event.accept()
            else:
                event.ignore()
            pass
        else:
            event.accept()
        pass
    
        return None
    '''
    -------------------------------------------------------------------------------
        Event filters
    -------------------------------------------------------------------------------
    '''

    def func_Bind_Event_Filters(self):
        
        #self.func_Bind_Event_Filters__QSliders()
        
        return True

    def func_Bind_Event_Filters__QSliders(self):

        '''Run Sampling Strategy Page - Tab - Sampling Strategy run Parameters'''        
        #self.horizontalSlider_54.installEventFilter(self)
        
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
        
        self.func_Bind_Event_Handlers__QPushButton()
        self.func_Bind_Event_Handlers__QCheckBox()
        self.func_Bind_Event_Handlers__QGroupBox()

        return True

    def func_Bind_Event_Handlers__QPushButton(self):
        
#         '''QPushButton - Apply Distribution MALE'''
#         self.pushButton_2.clicked.connect(self.func_QPushButton_Clicked__Apply_Distribution__MALE) 
#         '''QPushButton - Apply Distribution FEMALE'''
#         self.pushButton_3.clicked.connect(self.func_QPushButton_Clicked__Apply_Distribution__FEMALE) 
#         
        '''QPushButton - Apply Distribution to SEX'''
        self.pushButton_2.clicked.connect(self.func_QPushButton_Clicked__Apply_Distribution) 
        
        '''QPushButton - Copy Distribution'''
        self.pushButton_3.clicked.connect(self.func_QPushButton_Clicked__Copy_Distribution) 
        
        '''QPushButton - Save Distribution '''
        self.pushButton.clicked.connect(self.func_QPushButton_Clicked__Save_Distribution) 

        '''QPushButton - Cancel '''
        self.pushButton_4.clicked.connect(self.func_QPushButton_Clicked__Cancel_And_Exit) 
        
        return True

    def func_Bind_Event_Handlers__QCheckBox(self):
        
        '''QCheckBox - Select MALES '''
        self.checkBox.stateChanged["int"].connect(self.func_QCheckBox_SELECT_MALES__StateChanged)
        
        '''QCheckBox - Select FEMALES '''
        self.checkBox_2.stateChanged["int"].connect(self.func_QCheckBox_SELECT_FEMALES__StateChanged)
        
        
        '''QCheckBox - Select JUVENILES '''
        self.checkBox_4.stateChanged["int"].connect(self.func_QCheckBox_SELECT_JUVENILES__StateChanged)
        
        '''QCheckBox - Select ADULTS '''
        self.checkBox_5.stateChanged["int"].connect(self.func_QCheckBox_SELECT_ADULTS__StateChanged)
        
        
        return True
    
    def func_Bind_Event_Handlers__QGroupBox(self):
        
        '''QGroupBox - Select Apply Single Value '''
        self.groupBox_4.toggled["bool"].connect(self.func_QGroupBox_SELECT_APPLY_SINGLE_VALUE__StateChanged)
        
        '''QGroupBox - Select Apply CSV Values '''
        self.groupBox_5.toggled["bool"].connect(self.func_QGroupBox_SELECT_APPLY_CSV_VALUES__StateChanged)
        
        
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
    def func_QCheckBox_SELECT_MALES__StateChanged(self, int_State):
        
        if self.groupBox_5.isChecked():
            pass
        else:
            self.func_QCheckBox_SELECT_JUVENILES__StateChanged(int_State)
            self.func_QCheckBox_SELECT_ADULTS__StateChanged(int_State)
        pass
    
        return int_State
    
    def func_QCheckBox_SELECT_FEMALES__StateChanged(self, int_State):
 
        if self.groupBox_5.isChecked():
            pass
        else:
            self.func_QCheckBox_SELECT_JUVENILES__StateChanged(int_State)
            self.func_QCheckBox_SELECT_ADULTS__StateChanged(int_State)
        pass
        
        return int_State
    
    def func_QCheckBox_SELECT_JUVENILES__StateChanged(self, int_State):
        
        list_Age_Cohorts = [x for x in range(0,self.qForm_Main.int_Species_Life_History_Min_Mating_Age)] 
        
        ''' Check for MALES '''
        if self.checkBox_4.isChecked():
            if self.checkBox.isChecked():
                bool_Tick = True
            else:
                bool_Tick = False
            pass
        else:
            bool_Tick = False
        pass
    
        list_Custom_Widgets = self.widget_Cohorts__MALE.findChildren(Ui_QWidget_Slider)
        self.func_CheckBox_Tick_Custom_Slider_Widget_Age_Cohorts(list_Custom_Widgets, list_Age_Cohorts, bool_Tick)
        
        ''' Check for FEMALES '''
        if self.checkBox_4.isChecked():
            if self.checkBox_2.isChecked():
                bool_Tick = True
            else:
                bool_Tick = False
            pass
        else:
            bool_Tick = False
        pass
        list_Custom_Widgets = self.widget_Cohorts__FEMALE.findChildren(Ui_QWidget_Slider)
        self.func_CheckBox_Tick_Custom_Slider_Widget_Age_Cohorts(list_Custom_Widgets, list_Age_Cohorts, bool_Tick)
        
        self.func_Enable_Apply_Values_Widgets()
        
        return int_State
    
    def func_QCheckBox_SELECT_ADULTS__StateChanged(self, int_State):
        
        list_Age_Cohorts = [x for x in range(self.qForm_Main.int_Species_Life_History_Min_Mating_Age, self.qForm_Main.int_Species_Life_History_Max_Age)] 
        
        ''' Check for MALES '''
        if self.checkBox_5.isChecked():
            if self.checkBox.isChecked():
                bool_Tick = True
            else:
                bool_Tick = False
            pass
        else:
            bool_Tick = False
        pass
    
        list_Custom_Widgets = self.widget_Cohorts__MALE.findChildren(Ui_QWidget_Slider)
        self.func_CheckBox_Tick_Custom_Slider_Widget_Age_Cohorts(list_Custom_Widgets, list_Age_Cohorts, bool_Tick)
        
        ''' Check for FEMALES '''
        if self.checkBox_5.isChecked():
            if self.checkBox_2.isChecked():
                bool_Tick = True
            else:
                bool_Tick = False
            pass
        else:
            bool_Tick = False
        pass
        list_Custom_Widgets = self.widget_Cohorts__FEMALE.findChildren(Ui_QWidget_Slider)
        self.func_CheckBox_Tick_Custom_Slider_Widget_Age_Cohorts(list_Custom_Widgets, list_Age_Cohorts, bool_Tick)
        
        self.func_Enable_Apply_Values_Widgets()
        
        return int_State
    
    def func_CheckBox_Tick_Custom_Slider_Widget_Age_Cohorts(self, list_Custom_Widgets, list_Age_Cohorts, bool_Tick):
        
        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF
                   
        for int_Age in list_Age_Cohorts:
            #widget_Custom = list_Custom_Widgets[int_Age - 1]
            widget_Custom = list_Custom_Widgets[int_Age]
            for widget_Custom_Child in widget_Custom.findChildren(QtGui.QCheckBox):
                widget_Custom_Child.setChecked(bool_Tick)
            pass
        pass   
                     
    
        return True
    
    def func_CheckBox_Enable_Custom_Slider_Widget_Age_Cohorts(self, list_Custom_Widgets, list_Age_Cohorts, bool_Enable):
        
        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF
                   
        for int_Age in list_Age_Cohorts:
            widget_Custom = list_Custom_Widgets[int_Age - 1]
            for widget_Custom_Child in widget_Custom.findChildren(QtGui.QCheckBox):
                widget_Custom_Child.setEnabled(bool_Enable)
            pass
        pass   
                     
    
        return True


    def func_QGroupBox_SELECT_APPLY_SINGLE_VALUE__StateChanged(self, bool_State):
        
        if self.groupBox_4.isChecked():
            if self.groupBox_5.isChecked():
                self.groupBox_5.setChecked(False)
            pass
        pass
    
        return bool_State
    
    def func_QGroupBox_SELECT_APPLY_CSV_VALUES__StateChanged(self, bool_State):

        bool_Block_Signals = True
        self.checkBox_4.blockSignals(bool_Block_Signals)
        self.checkBox_5.blockSignals(bool_Block_Signals)
                
        if self.groupBox_5.isChecked():
            self.pushButton_2.setEnabled(True)
            
            if self.groupBox_4.isChecked():
                self.groupBox_4.setChecked(False)
            pass

            self.checkBox_4.setChecked(False)
            self.checkBox_5.setChecked(False)
            self.checkBox_4.setEnabled(False)
            self.checkBox_5.setEnabled(False)
        else:
            self.pushButton_2.setEnabled(False)
            self.checkBox_4.setEnabled(True)
            self.checkBox_5.setEnabled(True)
        pass

        bool_Block_Signals = False
        self.checkBox_4.blockSignals(bool_Block_Signals)
        self.checkBox_5.blockSignals(bool_Block_Signals) 
            
        return bool_State
    
    def func_Enable_Apply_Values_Widgets(self):
        
#         if self.checkBox_4.isChecked() or self.checkBox_5.isChecked():
#             self.checkBox.setEnabled(True)
#             self.checkBox_2.setEnabled(True)
#             self.checkBox.setChecked(True)
#             self.checkBox_2.setChecked(True)
#         else:
#             self.checkBox.setEnabled(False)
#             self.checkBox_2.setEnabled(False)
#             self.checkBox.setChecked(False)
#             self.checkBox_2.setChecked(False)            
#         pass
         
        if self.checkBox.isChecked() or self.checkBox_2.isChecked():
            self.checkBox_4.setEnabled(True)
            self.checkBox_5.setEnabled(True)
        else:
            self.checkBox_4.setEnabled(False)
            self.checkBox_5.setEnabled(False)
            self.checkBox_4.setChecked(False)
            self.checkBox_5.setChecked(False)                
        pass
         
        if self.checkBox.isChecked():
            list_Age_Cohorts = [x for x in range(1,self.qForm_Main.int_Species_Life_History_Max_Age+1)]
            list_Custom_Widgets = self.widget_Cohorts__MALE.findChildren(Ui_QWidget_Slider)
            bool_Enable = True
            self.func_CheckBox_Enable_Custom_Slider_Widget_Age_Cohorts(list_Custom_Widgets, list_Age_Cohorts, bool_Enable)
            pass
        else:
            list_Age_Cohorts = [x for x in range(1,self.qForm_Main.int_Species_Life_History_Max_Age+1)]
            list_Custom_Widgets = self.widget_Cohorts__MALE.findChildren(Ui_QWidget_Slider)
            bool_Enable = False
            self.func_CheckBox_Enable_Custom_Slider_Widget_Age_Cohorts(list_Custom_Widgets, list_Age_Cohorts, bool_Enable)
            pass
        pass    
    
        if self.checkBox_2.isChecked():
            list_Age_Cohorts = [x for x in range(1,self.qForm_Main.int_Species_Life_History_Max_Age+1)]
            list_Custom_Widgets = self.widget_Cohorts__FEMALE.findChildren(Ui_QWidget_Slider)
            bool_Enable = True
            self.func_CheckBox_Enable_Custom_Slider_Widget_Age_Cohorts(list_Custom_Widgets, list_Age_Cohorts, bool_Enable)
            pass
        else:
            list_Age_Cohorts = [x for x in range(1,self.qForm_Main.int_Species_Life_History_Max_Age+1)]
            list_Custom_Widgets = self.widget_Cohorts__FEMALE.findChildren(Ui_QWidget_Slider)
            bool_Enable = False
            self.func_CheckBox_Enable_Custom_Slider_Widget_Age_Cohorts(list_Custom_Widgets, list_Age_Cohorts, bool_Enable)
            pass
        pass    
    
        if self.checkBox.isChecked() or self.checkBox_2.isChecked():
            self.groupBox_4.setEnabled(True)
            self.groupBox_5.setEnabled(True)
            
            self.groupBox_4.setChecked(True)
            self.groupBox_5.setChecked(False)
            
            self.pushButton_2.setEnabled(True) 
        else:
            self.groupBox_4.setEnabled(False)
            self.groupBox_5.setEnabled(True) 
            
            self.groupBox_4.setChecked(False)
            self.groupBox_5.setChecked(False)  
            
            self.pushButton_2.setEnabled(False) 
            
#             ''' Uncheck and disable all custom slider widgets '''
#             for widget_Custom in self.widget_Cohorts__MALE.findChildren(Ui_QWidget_Slider):
#                 for widget_Custom_Child in widget_Custom.findChildren(QtGui.QCheckBox):
#                     if widget_Custom_Child.isChecked():
#                         widget_Custom_Child.setChecked(False)
#                         widget_Custom_Child.setEnabled(False)
#                     pass
#                 pass
#             pass            
                          
        pass
          
        
        return True
    
    
    '''
    -------------------------------------------------------------------------------
    Save buttons
    -------------------------------------------------------------------------------
    '''
    def func_QPushButton_Clicked__Apply_Distribution(self):

        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF
        
        bool_Success = False
        
        if self.groupBox_4.isChecked():
            '''QPushButton - Apply Distribution MALE'''
            if self.checkBox.isChecked():
                float_Value = self.doubleSpinBox.value()
        
                list_Widgets_With_Sliders_To_Apply_To = self.widget_Cohorts__MALE.findChildren(Ui_QWidget_Slider)
                
                self.func_Apply_Single_Value_From_SpinBox(list_Widgets_With_Sliders_To_Apply_To, float_Value)
            pass
        
            '''QPushButton - Apply Distribution FEMALE'''
            if self.checkBox_2.isChecked():
                float_Value = self.doubleSpinBox.value()
        
                list_Widgets_With_Sliders_To_Apply_To = self.widget_Cohorts__FEMALE.findChildren(Ui_QWidget_Slider)
                
                self.func_Apply_Single_Value_From_SpinBox(list_Widgets_With_Sliders_To_Apply_To, float_Value)
            pass
        elif self.groupBox_5.isChecked():
            int_Age_Min = 0
            int_Age_Max = self.qForm_Main.int_Species_Life_History_Max_Age-1            
            '''QPushButton - Apply Distribution MALE'''
            if self.checkBox.isChecked():
                #str_UnClean_TextBox_Contents = self.lineEdit.text()
                str_UnClean_TextBox_Contents = self.textEdit.toPlainText()
        
                list_Widgets_With_Sliders_To_Apply_To = self.widget_Cohorts__MALE.findChildren(Ui_QWidget_Slider)
                
                bool_Success = self.func_Apply_Distribution_From_TextBox(list_Widgets_With_Sliders_To_Apply_To, str_UnClean_TextBox_Contents, int_Age_Min, int_Age_Max)
            pass
        
            '''QPushButton - Apply Distribution FEMALE'''
            if self.checkBox_2.isChecked():
                #str_UnClean_TextBox_Contents = self.lineEdit.text()
                str_UnClean_TextBox_Contents = self.textEdit.toPlainText()
                
                list_Widgets_With_Sliders_To_Apply_To = self.widget_Cohorts__FEMALE.findChildren(Ui_QWidget_Slider)
                
                bool_Success = self.func_Apply_Distribution_From_TextBox(list_Widgets_With_Sliders_To_Apply_To, str_UnClean_TextBox_Contents, int_Age_Min, int_Age_Max)
            pass

            if bool_Success:
                str_MessageBox_Text = 'Distribution successfully applied.'
                messageBox_Reponse = QtGui.QMessageBox.information(self, 'Apply Distribution', str_MessageBox_Text, buttons=QtGui.QMessageBox.Ok, defaultButton=QtGui.QMessageBox.Ok)
            pass        
        pass

    
        return True   
    
    def func_QPushButton_Clicked__Copy_Distribution(self):

        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF
        
        bool_Success = False
        
        if self.checkBox.isChecked() and self.checkBox_2.isChecked():
            str_MessageBox_Text = 'Only a single sex can be copied at one time.\n\nPlease untick one of the sexes and try the Copy again.'
            messageBox_Reponse = QtGui.QMessageBox.information(self, 'Too many sexes selected', str_MessageBox_Text, buttons=QtGui.QMessageBox.Ok, defaultButton=QtGui.QMessageBox.Ok)
            return False
        pass
    
        if self.checkBox.isChecked():
            '''QPushButton - Copy Distribution MALE'''
            dict_Ages_And_Rates__MALE, _ = self.func_Get_Distribution()
            str_Heading_Suffix = 'Rate_Mort_M'
            bool_Success = self.func_Copy_Distribution_To_TAB_Delimited_List(dict_Ages_And_Rates__MALE, str_Heading_Suffix)
                
        elif self.checkBox_2.isChecked():
            '''QPushButton - Copy Distribution FEMALE'''
            _, dict_Ages_And_Rates__FEMALE = self.func_Get_Distribution()
            str_Heading_Suffix = 'Rate_Mort_F'
            bool_Success = self.func_Copy_Distribution_To_TAB_Delimited_List(dict_Ages_And_Rates__FEMALE, str_Heading_Suffix)
        else:
            str_MessageBox_Text = 'Tick a specific sex and try the copy again.\n\nNote that only one sex can be copied at a time.'
            messageBox_Reponse = QtGui.QMessageBox.information(self, 'No sex selected', str_MessageBox_Text, buttons=QtGui.QMessageBox.Ok, defaultButton=QtGui.QMessageBox.Ok)
            return False
        pass  

        if bool_Success:
            str_MessageBox_Text = 'Distribution successfully copied to the clipboard.\n\nPaste into the application of your choice.'
            messageBox_Reponse = QtGui.QMessageBox.information(self, 'Copy Distribution', str_MessageBox_Text, buttons=QtGui.QMessageBox.Ok, defaultButton=QtGui.QMessageBox.Ok)
        else:
            str_MessageBox_Text = 'Distribution could not be copied to the clipboard, sorry!'
            messageBox_Reponse = QtGui.QMessageBox.information(self, 'Copy Distribution', str_MessageBox_Text, buttons=QtGui.QMessageBox.Ok, defaultButton=QtGui.QMessageBox.Ok)
            return False
        pass
    
        return True   
    
    def func_QPushButton_Clicked__Apply_Distribution__MALE__RETIRE(self):

        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF
        
        str_UnClean_TextBox_Contents = self.lineEdit.text()

        list_Widgets_With_Sliders_To_Apply_To = self.widget_Cohorts__MALE.findChildren(Ui_QWidget_Slider)
        
        self.func_Apply_Distribution_From_TextBox(list_Widgets_With_Sliders_To_Apply_To, str_UnClean_TextBox_Contents)
            
        return True   
    
    def func_QPushButton_Clicked__Apply_Distribution__FEMALE__RETIRE(self):

        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF
        
        str_UnClean_TextBox_Contents = self.lineEdit_2.text()

        list_Widgets_With_Sliders_To_Apply_To = self.widget_Cohorts__FEMALE.findChildren(Ui_QWidget_Slider)
        
        self.func_Apply_Distribution_From_TextBox(list_Widgets_With_Sliders_To_Apply_To, str_UnClean_TextBox_Contents)
            
        return True   
    
    
    def func_QPushButton_Clicked__Save_Distribution(self):

        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF
                
        #bool_Success = False
        
        #self.dict_Species_Demographic_Natural_MORTALITY_CSV_Age_And_MORTALITY_Rate__MALE, self.dict_Species_Demographic_Natural_MORTALITY_CSV_Age_And_MORTALITY_Rate__FEMALE = self.func_Get_Distribution()
        self.qForm_Main.dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__MALE, self.qForm_Main.dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__FEMALE = self.func_Get_Distribution()
        
        self.qForm_Main.func_Update_Config__Age_And_Natural_Mortality_Rate__MALE()
        self.qForm_Main.func_Update_Config__Age_And_Natural_Mortality_Rate__FEMALE()
         
        return True   

    def func_QPushButton_Clicked__Cancel_And_Exit(self):   
        
        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF        

        self.close()
        
        return True
       
    '''
    -------------------------------------------------------------------------------
        Signal  downstream functions 
    -------------------------------------------------------------------------------
    ''' 
    def func_Apply_Single_Value_From_SpinBox(self, list_Widgets_With_Sliders_To_Apply_To, float_Value):
        
        #bool_Success = False

        ''' Apply value to list of slider widgets '''
        for widget_Custom in list_Widgets_With_Sliders_To_Apply_To:
            for widget_Custom_Child in widget_Custom.findChildren(QtGui.QCheckBox):
                if widget_Custom_Child.isChecked():
                    for widget_Custom_Child in widget_Custom.findChildren(QtGui.QDoubleSpinBox):
                        widget_Custom_Child.setValue(float_Value)
                        pass
                    pass
                pass
            pass
        pass            
                    
        return True
    
    def func_Apply_Distribution_From_TextBox(self, list_Widgets_With_Sliders_To_Apply_To, str_UnClean_TextBox_Contents, int_Age_Min, int_Age_Max):
        
        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF
        
        bool_Success = False

        def isInt(str_Value):
            try: 
                int(str_Value)
                return True
            except ValueError:
                return False
            pass
        pass
    
        def isFloat(str_Value):
            try: 
                float(str_Value)
                return True
            except ValueError:
                return False
            pass
        pass
    

        str_Dist_Text = str(str_UnClean_TextBox_Contents)

        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, 'str_Dist_Text: '  + str_Dist_Text)
        #DEBUG_OFF
                
        ''' Validate text '''
        regexp_Alphanumeric_0 = "^[a-zA-Z0-9-_.\t\n]*$"
        try:
            regex_Pattern = re.compile(regexp_Alphanumeric_0)
            bool_Success = True
        except:
            bool_Success = False
        pass
        if bool_Success:
            bool_Success = False
            bool_Success = bool(regex_Pattern.match(str_Dist_Text))
        
            str_Invalid_Chars = '|'
            if not bool_Success:
                for str_Char in list(str_Dist_Text):
                    bool_Char_Ok = False
                    bool_Char_Ok = bool(regex_Pattern.match(str_Char))
                    if not bool_Char_Ok:
                        str_Invalid_Chars += str_Char + '|'
                    pass
                pass
                ''' Display erroneous chars '''
                str_MessageBox_Text = 'Housten, we have a problem!  The supplied distribution has the following invalid characters (enclosed by |):\n\n' + str_Invalid_Chars +'\n\nValid visible characters are a-zA-Z0-9-_\n\nThe only valid invisible characters are TAB and LINEFEED (i.e. Return or Enter).  SPACE characters are not allowed.\n\nPlease fix the distribution and try again.'
                messageBox_Reponse = QtGui.QMessageBox.information(self, 'Apply Distribution', str_MessageBox_Text, buttons=QtGui.QMessageBox.Ok, defaultButton=QtGui.QMessageBox.Ok)
                return False    
            pass
        pass
    
        ''' Strip off excess \n's '''
        list_Delim_Text_To_Validate = str_Dist_Text.split('\n')
        list_Parsed_Dist = []
        for str_Value in list_Delim_Text_To_Validate:
            if str_Value != '':
                list_Parsed_Dist.append(str_Value)
            pass
        pass        
        str_Dist_Text_WO_n = '\t'.join(list_Parsed_Dist) 
        ''' Strip off excess \t's '''
        list_Delim_Text_To_Validate = str_Dist_Text_WO_n.split('\t')
        list_Parsed_Dist = []
        for str_Value in list_Delim_Text_To_Validate:
            if str_Value != '':
                list_Parsed_Dist.append(str_Value)
            pass
        pass      
     
        ''' Strip off the headings '''
        list_Valid_Ages = [x for x in range(int_Age_Min, int_Age_Max+1)]
        list_Validated_Dist = []
        int_Value_Counter = 0
        int_Row_Counter = 0
        int_Age_Counter = 0

        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, 'list_Valid_Ages: '  + str(list_Valid_Ages))
        self.qForm_Main.func_Debug_Logging(False, 2, 'list_Parsed_Dist: '  + str(list_Parsed_Dist))
        #DEBUG_OFF
                
        for str_Value in list_Parsed_Dist:
            int_Value_Counter += 1
            ''' Check if item count is odd or even '''               
            intOdd = int_Value_Counter & 0x1 
            if intOdd:
                int_Row_Counter += 1
            pass
            if int_Value_Counter <= 2:
                ''' This is a heading - Ignore'''
                if isInt(str_Value) or isFloat(str_Value):
                    ''' ERROR - Expecting anything but an int or float as headings '''
                    str_MessageBox_Text = 'For row ' + str(int_Row_Counter) + ',\n\na non-numeric heading was expected.\n\nBut got: ' + str_Value + '\n\nCheck that you have a non-numeric Heading for each TAB-delimited column of Age and Rate values.\n\nPlease fix your distribution and try again.'
                    QtGui.QMessageBox.critical(self, 'Delimited Distribution Error', str_MessageBox_Text, QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Cancel)
                    return False                         
                pass
            elif intOdd:
                ''' ODD - Should be an int '''
                if isInt(str_Value):
                    int_Age = int(str_Value)
                    int_Age_Counter += 1 
                    int_Age_Expected = list_Valid_Ages[int_Age_Counter-1]
                    if int_Age == int_Age_Expected:
                        ''' All good '''
                        list_Validated_Dist.append(int_Age)
                    else:                 
                        ''' ERROR - Ages are not in order or not in the expected range '''
                        str_MessageBox_Text = 'For row ' + str(int_Row_Counter) + ',\n\na positive integer, Age = ' + str(int_Age_Expected) + ' was expected.\n\nBut got Age = ' + str_Value + '\n\nCheck that your Age values range from ' + str(int_Age_Min) + ' to ' + str(int_Age_Max) + '.\n\nPlease fix your distribution and try again.'
                        QtGui.QMessageBox.critical(self, 'Delimited Distribution Error', str_MessageBox_Text, QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Cancel)
                        return False     
                    pass
                else:                 
                    ''' ERROR - Expecting integer at the first odd count '''
                    str_MessageBox_Text = 'For row ' + str(int_Row_Counter) + ',\n\na positive integer, Age = ' + str(int_Age_Expected) + ' was expected.\n\nBut got Age = ' + str_Value + '\n\nCheck that your Age values range from ' + str(int_Age_Min) + ' to ' + str(int_Age_Max) + '.\n\nPlease fix your distribution and try again.'
                    QtGui.QMessageBox.critical(self, 'Delimited Distribution Error', str_MessageBox_Text, QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Cancel)
                    return False     
                pass
            else:
                ''' EVEN - Should be an float '''     
                if isFloat(str_Value):
                    float_Rate = float(str_Value)
                    if float_Rate >= 0.0 and float_Rate <= 1.0:
                        ''' All good '''
                        list_Validated_Dist.append(float(str_Value))
                    else:
                        ''' ERROR - Rate is not in the expected range '''
                        str_MessageBox_Text = 'For row ' + str(int_Row_Counter) + ',\n\na positive decimal ranging from 0.0 to 1.0 was expected.\n\nBut got Rate = ' + str_Value + '\n\nPlease fix your distribution and try again.'
                        QtGui.QMessageBox.critical(self, 'Delimited Distribution Error', str_MessageBox_Text, QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Cancel)
                        return False     
                    pass                        
                else:                    
                    ''' ERROR - Expecting float at the first even count '''
                    str_MessageBox_Text = 'For row ' + str(int_Row_Counter) + ',\n\na positive decimal ranging from 0.0 to 1.0 was expected.' + '\n\n' + 'But got Rate = ' + str_Value + '\n\nPlease fix your distribution and try again.'
                    QtGui.QMessageBox.critical(self, 'Delimited Distribution Error', str_MessageBox_Text, QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Cancel)
                    return False     
                pass
            pass
        pass

        ''' Check that all expected ages are represented '''
        int_Total_Ages_Expected = len(list_Valid_Ages)
        if int_Age_Counter <> int_Total_Ages_Expected:
            str_MessageBox_Text = 'Total number of ages expected was : ' + str(int_Total_Ages_Expected) + '\n\nBut got Total ages = ' + str(int_Age_Counter) + '\n\nCheck that your Age values range from ' + str(int_Age_Min) + ' to ' + str(int_Age_Max) + '.\n\nPlease fix your distribution and try again.'
            QtGui.QMessageBox.critical(self, 'Delimited Distribution Error', str_MessageBox_Text, QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Cancel)
            return False     
        pass
    
        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, 'list_Validated_Dist: '  + str(list_Validated_Dist))
        #DEBUG_OFF
                    
        ''' Accumulate into a list of tuples '''
        int_Count = 0
        int_Age = 0
        float_Rate = 0
        tup_Age_And_Rate = ()
        list_tup_Validated_Dist = []
         
        for item in list_Validated_Dist:
            ''' Check if item count is odd or even '''               
            intOdd = int_Count & 0x1
            if intOdd == 1: 
                float_Rate = float(item)
                ''' Tuple complete - Save '''
                tup_Age_And_Rate = (int_Age, float_Rate)
                list_tup_Validated_Dist.append(tup_Age_And_Rate)
                
                ''' Tuple complete - Reset ''' 
                int_Age = 0
                float_Rate = 0
                tup_Age_And_Rate = ()
            else:
                int_Age = int(item)
            pass
            int_Count += 1
        pass

        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, 'list_tup_Validated_Dist: '  + str(list_tup_Validated_Dist))
        #DEBUG_OFF
                
        ''' Apply tuple distribution to list of slider widgets '''
        for (int_Age, float_Rate) in list_tup_Validated_Dist:
            widget_Custom = list_Widgets_With_Sliders_To_Apply_To[int_Age]
            for widget_Custom_Child in widget_Custom.findChildren(QtGui.QDoubleSpinBox):
                widget_Custom_Child.setValue(float_Rate)
                pass
            pass
        pass            
                    
        return True
    
    def func_Apply_Distribution_From_TextBox_OLD(self, list_Widgets_With_Sliders_To_Apply_To, str_UnClean_TextBox_Contents):
        
        #bool_Success = False

        ''' Get delimited string from textbox and parse into list of tuples '''
#         str_Dist_Text = str(str_UnClean_TextBox_Contents)
#         if str_Dist_Text[-1:] == '\n':
#             str_Dist_Text = str_Dist_Text[:-1]
#         pass
#         str_Dist_Text = "\t".join(str_Dist_Text.split('\n'))
#         list_Dist = str_Dist_Text.split('\t')
        str_Dist_Text = str(str_UnClean_TextBox_Contents)
        if str_Dist_Text[-1:] == '\n':
            str_Dist_Text = str_Dist_Text[:-1]
        pass
        if str_Dist_Text[:1] == '\n':
            str_Dist_Text = str_Dist_Text[1:]
        pass
        str_Dist_Text = ";".join(str_Dist_Text.split('\n'))
        list_Dist = str_Dist_Text.split(';')
        
        int_Count = 0
        int_Age = 0
        float_Mortality = 0
        tup_Age_And_Mortality = ()
        list_tup_Dist = []
        
        for item in list_Dist:
            ''' Check if item count is odd or even '''               
            intOdd = int_Count & 0x1
            if intOdd == 1: 
                float_Mortality = float(item)
                tup_Age_And_Mortality = (int_Age, float_Mortality)
                list_tup_Dist.append(tup_Age_And_Mortality)
                
                int_Age = 0
                float_Mortality = 0
                tup_Age_And_Mortality = ()
            else:
                int_Age = int(item)
            pass
        
            int_Count += 1
        pass
            
        
        ''' Apply tuple distribution to list of slider widgets '''
        for (int_Age, float_Mortality) in list_tup_Dist:
            widget_Custom = list_Widgets_With_Sliders_To_Apply_To[int_Age - 1]
            for widget_Custom_Child in widget_Custom.findChildren(QtGui.QSlider):
                widget_Custom_Child.setValue(int(round(self.int_Slider_Value_Step_Divisor*float_Mortality,0)))
                pass
            pass
        pass            
                    
        return True
    
    def func_Copy_Distribution_To_TAB_Delimited_List(self, dict_Ages_And_Rates, str_Heading_Suffix):
        
        bool_Success = False
        
        str_Ages_And_Rates__Delimited = '\n'.join(['\t'.join([str(key), str(val)]) for key, val in dict_Ages_And_Rates.items()])

        ''' Add headings '''
        str_Head_1 = 'Age'
        str_Head_2 = '' + str_Heading_Suffix
        str_Ages_And_Rates__Delimited = str_Head_1 + '\t' + str_Head_2 + '\n' + str_Ages_And_Rates__Delimited
        
        ''' Copy to clipboard '''
        try:
            tk_Clipboard = tkinter__Tk()
            tk_Clipboard.withdraw()
            tk_Clipboard.clipboard_clear()
            tk_Clipboard.clipboard_append(str_Ages_And_Rates__Delimited)
            tk_Clipboard.destroy() 
            bool_Success = True 
        except:
            bool_Success = False
        pass
    
        return bool_Success
            
    def func_Get_Distribution(self):
        
        #bool_Success = False
        
        ''' Get MALE dist '''
        int_Distribution_Count = 0
        for widget_Custom in self.widget_Cohorts__MALE.findChildren(Ui_QWidget_Slider):
            for widget_Custom_Child in widget_Custom.findChildren(QtGui.QDoubleSpinBox):
                self.dict_Species_Demographic_Natural_MORTALITY_CSV_Age_And_MORTALITY_Rate__MALE[int_Distribution_Count] = widget_Custom_Child.value()
                pass
            pass
            int_Distribution_Count += 1
        pass
    
        ''' Get FEMALE dist '''
        int_Distribution_Count = 0
        for widget_Custom in self.widget_Cohorts__FEMALE.findChildren(Ui_QWidget_Slider):
            for widget_Custom_Child in widget_Custom.findChildren(QtGui.QDoubleSpinBox):
                self.dict_Species_Demographic_Natural_MORTALITY_CSV_Age_And_MORTALITY_Rate__FEMALE[int_Distribution_Count] = widget_Custom_Child.value()
                pass
            pass
            int_Distribution_Count += 1
        pass
    
        return self.dict_Species_Demographic_Natural_MORTALITY_CSV_Age_And_MORTALITY_Rate__MALE, self.dict_Species_Demographic_Natural_MORTALITY_CSV_Age_And_MORTALITY_Rate__FEMALE

    def func_Populate_Widgits_With_Config_Data_RETIRE(self):

        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF

        bool_Exists = self.qForm_Main.bool_dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__MALE__FOUND
        if bool_Exists:
            ''' Get MALE dist '''
            int_Distribution_Count = 1
            for widget_Custom in self.widget_Cohorts__MALE.findChildren(Ui_QWidget_Slider):
                for widget_Custom_Child in widget_Custom.findChildren(QtGui.QDoubleSpinBox):
                    if int_Distribution_Count in self.qForm_Main.dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__MALE.keys():
                        float_Mortality = self.qForm_Main.dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__MALE[int_Distribution_Count]
                        float_Mortality = float(1) - float_Mortality 
                    else:
                        #float_Mortality = self.int_Slider_Value_Step_Divisor*self.int_Slider__Default_Value
                        float_Mortality = float(self.int_Slider__Default_Value)
                    pass
                    #widget_Custom_Child.setValue(int(round(self.int_Slider_Value_Step_Divisor*float_Mortality,0)))
                    widget_Custom_Child.setValue(float_Mortality)
                    pass
                pass
                int_Distribution_Count += 1
            pass
        else:
            pass
            ''' Widgets will initialise themselves '''
        pass
        
        bool_Exists = self.qForm_Main.bool_dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__FEMALE__FOUND
        if bool_Exists:
            ''' Get FEMALE dist '''
            int_Distribution_Count = 1
            for widget_Custom in self.widget_Cohorts__FEMALE.findChildren(Ui_QWidget_Slider):
                for widget_Custom_Child in widget_Custom.findChildren(QtGui.QDoubleSpinBox):
                    if int_Distribution_Count in self.qForm_Main.dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__FEMALE.keys():
                        float_Mortality = self.qForm_Main.dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__FEMALE[int_Distribution_Count]
                        float_Mortality = float(1) - float_Mortality 
                    else:
                        #float_Mortality = self.int_Slider_Value_Step_Divisor*self.int_Slider__Default_Value
                        float_Mortality = float(self.int_Slider__Default_Value)
                    pass
                    #widget_Custom_Child.setValue(int(round(self.int_Slider_Value_Step_Divisor*float_Mortality,0)))
                    widget_Custom_Child.setValue(float_Mortality)
                    pass
                pass
                int_Distribution_Count += 1
            pass
        else:
            pass
            ''' Widgets will initialise themselves '''
        pass

    def func_Populate_Widgits_With_Config_Data(self):

        #DEBUG_ON
        self.qForm_Main.func_Debug_Logging(False, 2, '')
        #DEBUG_OFF

        bool_Exists = self.qForm_Main.bool_dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__MALE__FOUND or self.qForm_Main.bool_dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__MALE__CHANGED
        if bool_Exists:
            ''' Get MALE dist '''
            int_Distribution_Count = 0
            for widget_Custom in self.widget_Cohorts__MALE.findChildren(Ui_QWidget_Slider):
                for widget_Custom_Child in widget_Custom.findChildren(QtGui.QDoubleSpinBox):
                    if int_Distribution_Count in self.qForm_Main.dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__MALE.keys():
                        float_Mortality = self.qForm_Main.dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__MALE[int_Distribution_Count]
                    else:
                        float_Mortality = float(self.int_Slider__Default_Value)
                    pass
                    widget_Custom_Child.setValue(float_Mortality)
                    pass
                pass
                int_Distribution_Count += 1
            pass
        else:
            pass
            ''' Widgets will initialise themselves '''
        pass
        
        bool_Exists = self.qForm_Main.bool_dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__FEMALE__FOUND or self.qForm_Main.bool_dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__FEMALE__CHANGED
        if bool_Exists:
            ''' Get FEMALE dist '''
            int_Distribution_Count = 0
            for widget_Custom in self.widget_Cohorts__FEMALE.findChildren(Ui_QWidget_Slider):
                for widget_Custom_Child in widget_Custom.findChildren(QtGui.QDoubleSpinBox):
                    if int_Distribution_Count in self.qForm_Main.dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__FEMALE.keys():
                        float_Mortality = self.qForm_Main.dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__FEMALE[int_Distribution_Count]
                    else:
                        float_Mortality = float(self.int_Slider__Default_Value)
                    pass
                    widget_Custom_Child.setValue(float_Mortality)
                    pass
                pass
                int_Distribution_Count += 1
            pass
        else:
            pass
            ''' Widgets will initialise themselves '''
        pass

    def func_UnSaved_Changes_Check(self):
        
        self.bool_Unsaved_Changes = False
        
        dict_Species_Demographic_Natural_MORTALITY_CSV_Age_And_MORTALITY_Rate__MALE, dict_Species_Demographic_Natural_MORTALITY_CSV_Age_And_MORTALITY_Rate__FEMALE = self.func_Get_Distribution()
                
        if dict_Species_Demographic_Natural_MORTALITY_CSV_Age_And_MORTALITY_Rate__MALE != self.qForm_Main.dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__MALE:
            self.bool_Unsaved_Changes = True
        pass
    
        if dict_Species_Demographic_Natural_MORTALITY_CSV_Age_And_MORTALITY_Rate__FEMALE != self.qForm_Main.dict_Species_Demographic_Natural_Mortality_CSV_Age_And_Mortality_Rate__FEMALE:
            self.bool_Unsaved_Changes = True
        pass
            
        return self.bool_Unsaved_Changes   

    '''
    --------------------------------------------------------------------------------------------------------
    # <<<<<<<<<<<<<<<<<< CLASS FINALIZATION
    --------------------------------------------------------------------------------------------------------
    '''       
    #def __exit__(self, type, value, traceback):
    def __exit__(self):
        
        return self.dict_Species_Demographic_Natural_MORTALITY_CSV_Age_And_MORTALITY_Rate__MALE, self.dict_Species_Demographic_Natural_MORTALITY_CSV_Age_And_MORTALITY_Rate__FEMALE
        