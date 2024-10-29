'''
Created on 29 Jan 2015

@author: Dean C Blower
'''
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< RELEASE INFO
from version import version
__project__ = version.__project__
__author__ = version.__author__
__version__ = version.__version__
__date__ = version.__date__
__copyright__ = version.__copyright__
__license__ = version.__license__
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PACKAGE IMPORTS
#
#------------------< Import python modules
from PyQt4 import QtGui
import sys
#
#------------------< Import DCB_General modules
#
#------------------< Import SharkSimFE modules
from object_SSFEFormMain import Ui_MainWindow
#
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASS DEFINITION
class SSFEGUIOperation(object):

    '''
    --------------------------------------------------------------------------------------------------------
    # <<<<<<<<<<<<<<<<<< CLASS INIT
    --------------------------------------------------------------------------------------------------------
    '''   

    def __enter__(self):
        
        return self 
         
    def __init__(self, objSSFEParametersLocal):
        '''
        Constructor
        '''
 
        self.obj_SSFEParams = objSSFEParametersLocal
        
        return None         
    
    '''
    --------------------------------------------------------------------------------------------------------
    # Main Processing
    --------------------------------------------------------------------------------------------------------
    '''
       
    def func_Main(self):

        app = QtGui.QApplication(sys.argv)
        app.setOrganizationName("Dean")
        app.setOrganizationDomain("blah.com")
        app.setApplicationName("NeSharkSim")
        window = Ui_MainWindow(self.obj_SSFEParams.str_Application_Working_Path \
                               , self.obj_SSFEParams.str_Application_Settings_Path_And_File \
                               , self.obj_SSFEParams.bool_App_Arg_Debug_Logging \
                               , None)
        window.show()
        ''' Bring the window to the front '''
        window.activateWindow()
        sys.exit(app.exec_())
        
        return True
    
    '''
    --------------------------------------------------------------------------------------------------------
    # <<<<<<<<<<<<<<<<<< CLASS FINALIZATION
    --------------------------------------------------------------------------------------------------------
    '''       
    def __exit__(self, type, value, traceback):
         
        pass
    