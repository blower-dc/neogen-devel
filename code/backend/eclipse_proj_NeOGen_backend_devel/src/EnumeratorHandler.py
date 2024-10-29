class EnumeratorHandler:
    """Handle OutputOperation objects"""
    def __enter__(self):
        
        class EnumeratorOperation: 
        
            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

            class MatingSchemeType:
                """possible MatingScheme types"""
                WF_Diploid_Sexual_Random_Mating=0
                Diploid_Dioecious_Random_Mating=1
                Diploid_Monecious_Random_Mating=2
                Diploid_Polygamous_Random_Mating=3
            class OffspringNumberSchemeType:
                """possible OffspringNumberScheme types"""
                EXACT=0
                POISSION=1
                
        self.EnumeratorOperation_obj = EnumeratorOperation() 
        return self.EnumeratorOperation_obj
 
    def __exit__(self, type, value, traceback): 
        self.EnumeratorOperation_obj.classCleanUp()
