#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
#from pprint import pprint
#import pprint
#import datetime

class AutoVivificationHandler:
    '''Handle errors'''
    def __enter__(self):

        class AutoVivificationHandler(dict):
            """Implementation of perl's autovivification feature."""

            def __getitem__(self, item):
                try:
                    return dict.__getitem__(self, item)
                except KeyError:
                    value = self[item] = type(self)()
                    return value   

# -------------- Class specific routines

            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.class_AutoVivificationHandler = AutoVivificationHandler() 
        return self.class_AutoVivificationHandler
 
    def __exit__(self, type, value, traceback): 
        self.class_AutoVivificationHandler.classCleanUp()