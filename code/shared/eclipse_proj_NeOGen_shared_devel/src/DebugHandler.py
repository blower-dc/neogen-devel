#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
from pprint import pprint
import psutil
#import resource
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
from simuPOP import moduleInfo
#from simuPOP import *
import simuPOP as sim

class DebugHandler(object):
    """Handle FileOperation objects"""
    def __enter__(self):

        class DebugOperation(object):

            def displaySimuPOPModuleInfo(self):

                print('\n\n >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SimuPOP Environmental Options - BEGIN >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n')
                # ----------- Print CURRENT Options

                dictEnvironOptions = moduleInfo()['version']
                print((' ------> Environmental Options - version: ' + str(dictEnvironOptions)))

                dictEnvironOptions = moduleInfo()['revision']
                print((' ------> Environmental Options - revision: ' + str(dictEnvironOptions)))

                dictEnvironOptions = moduleInfo()['optimized']
                print((' ------> Environmental Options - optimized: ' + str(dictEnvironOptions)))

                dictEnvironOptions = moduleInfo()['threads']
                print((' ------> Environmental Options - threads: ' + str(dictEnvironOptions)))

                dictEnvironOptions = moduleInfo()['alleleType']
                print((' ------> Environmental Options - alleleType: ' + str(dictEnvironOptions)))

                dictEnvironOptions = moduleInfo()['maxAllele']
                print((' ------> Environmental Options - maxAllele: ' + str(dictEnvironOptions)))

                dictEnvironOptions = moduleInfo()['compiler']
                print((' ------> Environmental Options - compiler: ' + str(dictEnvironOptions)))

                dictEnvironOptions = moduleInfo()['date']
                print((' ------> Environmental Options - date: ' + str(dictEnvironOptions)))

                dictEnvironOptions = moduleInfo()['python']
                print((' ------> Environmental Options - python: ' + str(dictEnvironOptions)))

                dictEnvironOptions = moduleInfo()['platform']
                print((' ------> Environmental Options - platform: ' + str(dictEnvironOptions)))

                dictEnvironOptions = moduleInfo()['wordsize']
                print((' ------> Environmental Options - wordsize: ' + str(dictEnvironOptions)))

                dictEnvironOptions = moduleInfo()['alleleBits']
                print((' ------> Environmental Options - alleleBits: ' + str(dictEnvironOptions)))

                #dictEnvironOptions = moduleInfo()['maxNumSubPop']
                #print(' ------> Environmental Options - maxNumSubPop: ' + str(dictEnvironOptions))

                dictEnvironOptions = moduleInfo()['maxIndex']
                print((' ------> Environmental Options - maxIndex: ' + str(dictEnvironOptions)))

                dictEnvironOptions = moduleInfo()['debug']
                print(' ------> Environmental Options - debug: ')
                pprint(dictEnvironOptions)

                print('\n\n >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SimuPOP Environmental Options - END   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n')

                input("\n Review SimuPop environment information. Press return to close this window... \n")

#             def memory_usage_resource():
#                 #import resource
#                 rusage_denom = 1024.
#                 if sys.platform == 'darwin':
#                     # ... it seems that in OSX the output is different units ...
#                     rusage_denom = rusage_denom * rusage_denom
#                 mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
#                 return mem
            
            def memory_usage_psutil():
                # return the memory usage in MB
                #import psutil
                process = psutil.Process(os.getpid())
                mem = process.get_memory_info()[0] / float(2 ** 20)
                return mem
            
            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.debugOperation_obj = DebugOperation() 
        return self.debugOperation_obj
 
    def __exit__(self, type, value, traceback): 
        self.debugOperation_obj.classCleanUp()