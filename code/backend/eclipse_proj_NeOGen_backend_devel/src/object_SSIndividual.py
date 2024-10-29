#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
#from simuPOP
#import simuPOP as sim
from AutoVivificationHandler import AutoVivificationHandler
from SSAnalysisHandler import SSAnalysisHandler

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
#from collections import defaultdict

class object_SSIndividual:
    """Contains SS Simulation level properties and methods"""
    def __enter__(self):

        class obj_SSIndividual():

# -------------- Class specific routines

            __slots__ = ('stringDelimiter'
                         ,'stringDelimiter2'
                         ,'objSSParametersLocal'
                         ,'intLevel'
                         ,'pop'
                         ,'intSubPop'
                         ,'intIndivCount'
                         ,'dictDataSectionNotesLevels'
                        ,'dict_LevelIndivKey'
                        ,'dict_Individual_ID'
                        ,'dict_Father_ID'
                        ,'dict_Mother_ID'
                        ,'dict_Sex'
                        ,'dict_Affection_not_working'
                        ,'dict_Age'
                        ,'dict_Age_in_months'
                        ,'dict_Birth_Generation'
                        ,'dict_NumLoci'
                        ,'dict_Genotype'
                        )

            def __init__(self):
                
                self.stringDelimiter = ';'
                self.stringDelimiter2 = ','

                self.objSSParametersLocal = None

                self.intLevel = 5
                
                self.intSubPop = 0

                self.pop = None
                
                self.dictDataSectionNotesLevels = AutoVivificationHandler()

                self.intIndivCount = 0

                self.dict_LevelIndivKey = {}
                
                self.dict_Individual_ID = {}
                    
                self.dict_Father_ID = {}
                    
                self.dict_Mother_ID = {}
                
                self.dict_Sex = {}
                    
                self.dict_Affection_not_working = {}
                    
                self.dict_Age = {}
                
                self.dict_Age_in_months = {}
                
                self.dict_Birth_Generation = {}

                self.dict_NumLoci = {}

                self.dict_Genotype = AutoVivificationHandler()

            def method_PopulateProperties(self, simupopIndividual):
                    
                
                self.dictDataSectionNotesLevels[self.intLevel]['Data_Section_Note_' + str(self.intLevel)] = 'Indiv_Level_Params'
                
                self.dict_LevelIndivKey['Level_Indiv_Key'] = self.intIndivCount
                
                self.dict_Individual_ID['Individual_ID'] = int(simupopIndividual.ind_id)
                    
                self.dict_Father_ID['Father_ID'] = int(simupopIndividual.father_id)
                    
                self.dict_Mother_ID['Mother_ID'] = int(simupopIndividual.mother_id)
                
                if simupopIndividual.sex() == 1:
                    stringSex = 'M'
                elif simupopIndividual.sex() == 2:
                    stringSex = 'F'
                else:
                    stringSex = 'U'    
                self.dict_Sex['Sex'] = stringSex
                    
                self.dict_Affection_not_working['Affection_not_working'] = 'X'
                
                self.dict_Age['Age'] = int(simupopIndividual.age)
                
                self.dict_Age_in_months['Age_in_months'] = int(simupopIndividual.age_in_months)
                
                self.dict_Birth_Generation['Birth_Generation'] = int(simupopIndividual.birth_generation)

                intNumLoci = self.pop.totNumLoci()
                self.dict_NumLoci['Number_of_Loci'] = intNumLoci

                listLoci = list(range(intNumLoci))
                for intLocus in listLoci:
                    
                    strLocusName = self.pop.locusName(intLocus)    
                    
                    '''
                    Simupops Allele object for an individuals is:
                    
                    pop.individual.allele(locus-index, ploidy, chromosome),
                                        
                    where for a diplod ploidy is either AlleleA or AlleleB.
                    For two alleles per locus AlleleA= 0 or 1 and AlleleB= 1 or 0
                      
                    e.g. for allele A at locus 1 pop.individual.allele(1,0).
                    Where locus-index=1, & ploidy=0 (equvalent to saying AlleleA),
                    and chromosome is not required as we put each locus on a separate chromosome
                    
                    '''
                    
                    intPloidy0 = 0
                    intPloidy1 = 1

                    intAlleleA = simupopIndividual.allele(intLocus, intPloidy0) # Chromosome not required here as we only put 1 locus per chromosome
                    intAlleleB = simupopIndividual.allele(intLocus, intPloidy1)

                    self.dict_Genotype[intLocus][strLocusName][intPloidy0] = intAlleleA
                    self.dict_Genotype[intLocus][strLocusName][intPloidy1] = intAlleleB

                pass


# -------------- Class specific routines

            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.class_obj_SSIndividual = obj_SSIndividual() 
        return self.class_obj_SSIndividual
 
    def __exit__(self, type, value, traceback): 
        self.class_obj_SSIndividual.classCleanUp()