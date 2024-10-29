#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import simuPOP modules
# PROD simuPOP
from simuPOP import *
import simuPOP as sim
from AutoVivificationHandler import AutoVivificationHandler
from FileHandler import FileHandler
from ErrorHandler import ErrorHandler
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Import python modules
#import copy
from collections import OrderedDict
from collections import Counter as collections__Counter
import numpy as np

gstringModuleName='SSInputHandler.py'
gstringClassName='SSInputOperation'

class SSInputHandler:
    """Handle SS Input Operations"""
    def __enter__(self):

        class SSInputOperation:

            def method_ImportAlleleFrequencies_FromARLEQUIN_AllAlleleFreqs_File(self, strFileName):
                '''
                Import allele freqs for all loci specified in Arlequin AllAlleleFreqs.txt file format (TAB delimited)
                Return a list of allele freqs for input to the allele freqs simulation parameter
                '''
                bool_Success = False
                
                odictLocus_AlleleName_AlleleFreqs = OrderedDict()
                
                with FileHandler() as objFileOperation:        
                    fileHandle = objFileOperation.fileOpen(strFileName, 'read')
            
                    intLineCount = 0
                    intLocusNumber = -1
                    intAlleleCount = 0
                    strLastLocusName = ''
                    #Read each line in the file and add to dict, breaking on each allele, and locus
                    for line in fileHandle.readlines():
                        # get all allele names
                        listParsedLineValues = line.split('\t')
                        
                        ''' Check if line is valid - it should contain exactly 4 parsed values '''
                        if len(listParsedLineValues) != 4:
                            ''' Line has an error '''
                            return bool_Success, intLocusNumber, odictLocus_AlleleName_AlleleFreqs
                        pass
                    
                        strLocusName = listParsedLineValues[0]
                        if intLocusNumber == -1:
                            strLastLocusName = strLocusName
                            intAlleleCount = 0
                            intLocusNumber = 0
                        elif strLocusName != strLastLocusName:
                            intLocusNumber += 1
                            intAlleleCount = 0
                            strLastLocusName = strLocusName
                            
                        #intLocusNumber = strLocusName.split('_')[1]
                        strAlleleName = listParsedLineValues[1]
                        ''' The first allele freq value in the Arlequin AllAlleleFreqs file is for population 1 the second for pop 2...etc '''
                        floatAlleleFreq = float(listParsedLineValues[2])
                        intLineCount += 1
                        if strAlleleName == '?':
                            #Skip these values
                            pass
                        else:
                            dict_AlleleName_AlleleFreq = {intAlleleCount: {'Locus_Name': strLocusName, 'Allele_Name': strAlleleName, 'Allele_Freq': floatAlleleFreq}}
                            if intLocusNumber in odictLocus_AlleleName_AlleleFreqs:
                                odictLocus_AlleleName_AlleleFreqs[intLocusNumber].update(dict_AlleleName_AlleleFreq)
                            else:
                                odictLocus_AlleleName_AlleleFreqs[intLocusNumber] = dict_AlleleName_AlleleFreq
                            pass
                        pass
                        intAlleleCount += 1
                    pass
                    
                    bool_Success = objFileOperation.fileClose(fileHandle)
                pass
#                 else:
#                     with ErrorHandler() as objectErrorOperation:
#                         objectErrorOperation.propertyString_ErrorOriginModule= gstringModuleName
#                         objectErrorOperation.propertyString_ErrorOriginClass= gstringClassName
#                         objectErrorOperation.propertyString_ErrorMessage= 'File: ' + strFileName + ' cannot be found.'
#                         stringErrorMessageWithDetail=objectErrorOperation.methodConstructErrorMessageWithDetail()
#                     raise IOError(stringErrorMessageWithDetail)
#                 pass
            
                intLocusNumber += 1 
                
                return bool_Success, intLocusNumber, odictLocus_AlleleName_AlleleFreqs

            def method_ImportAlleleFrequencies_From_GENEPOP_File(self, strFileName, bool_Get_Locus_Number_Only):
                '''
                Import allele freqs for all loci specified in file format GENEPOP (Proprietry format)
                Return the locus number and list of allele freqs.
                '''
                bool_Success = False
                int_Loci_Number_In_Header = 0
                odict_Locus_Allele_Frequencies_Output = OrderedDict()
                odict_Locus_Allele_Frequencies = OrderedDict()
                str_Message = ''
                
                def func_Validate_Detail_Line(int_Line_Count, line_Current, int_Loci_Number_In_Header):
                                    
                    '''
                    Check the sample line is in the correct format
                    e.g. SAMPLE_NAME, 0101 0011 1010
                    '''
                    line_Formatted = line_Current.replace(',',' ')
                    list_Fields = line_Formatted.split(' ')
                    ''' Remove any empty strings '''
                    list_Fields = filter(None, list_Fields)
                    ''' Number of fields minus sample name should match the number of loci '''
                    list_Fields__Loci_Genotypes = list_Fields[1:]
                    int_Loci_Number_In_Detail_Line = len(list_Fields__Loci_Genotypes)
                    if int_Loci_Number_In_Header != int_Loci_Number_In_Detail_Line:
                        ''' We have an invalid detail line '''
                        str_Message = ''.join(['The number of loci in the first detail GENEPOP line (', str(int_Loci_Number_In_Detail_Line), ') does not match the number of loci named at the top of the file (', str(int_Loci_Number_In_Header), ')\n\nLine number: ', str(int_Line_Count), '; Line data: ', line_Current, '.\n\nPlease use valid GENEPOP formatting.'])
                        bool_Success = False
                        #return bool_Success, int_Loci_Number_In_Header, odict_Locus_AlleleName_AlleleFreqs, str_Message
                        return bool_Success, str_Message
                    pass
                    ''' Check that the allele freqs are all numeric'''
                    str_Sample_Name = list_Fields[0]
                    list_Lengths = []
                    int_Locus_Genotype_Count = 0
                    for item_Locus_Genotype in list_Fields__Loci_Genotypes:
                        int_Locus_Genotype_Count += 1 
                        list_Lengths.append(len(item_Locus_Genotype))
                        try: 
                            int(item_Locus_Genotype)
                        except ValueError:
                            ''' We have an invalid detail line '''
                            str_Message = ''.join(['Invalid locus genotype found. GENEPOP Genotypes may only contain integers.\n\nLine number: ', str(int_Line_Count), '; Sample name: ', str_Sample_Name, '; Locus number: ', str(int_Locus_Genotype_Count), ' = ', str(item_Locus_Genotype), ' but should be an integer.\n\nPlease use valid GENEPOP formatting.'])
                            bool_Success = False
                            #return bool_Success, int_Loci_Number_In_Header, odict_Locus_AlleleName_AlleleFreqs, str_Message
                            return bool_Success, str_Message
                        pass
                    pass
                    ''' Check that all the alleles are the same length in characters '''
                    bool_All_Lengths_Are_Equal = all(x == list_Lengths[0] for x in list_Lengths)
                    if not bool_All_Lengths_Are_Equal:
                        ''' We have an invalid detail line '''
                        str_Message = ''.join(['Invalid sample line found. GENEPOP locus genotypes must all be the same length.\n\nLine number: ', str(int_Line_Count), '; Line data: ', line_Current, '.\n\nPlease use valid GENEPOP formatting.'])
                        bool_Success = False
                        #return bool_Success, int_Loci_Number_In_Header, odict_Locus_AlleleName_AlleleFreqs, str_Message
                        return bool_Success, str_Message
                    pass
                    
                    return True, ''
                                
                with FileHandler() as objFileOperation:        
                    fileHandle = objFileOperation.fileOpen(strFileName, 'read')
            
                    str_Message = ''
                    int_File_Format = 1
                    
                    ''' Perform initial file validation '''
                    int_POP_Count = 0
                    int_Line_Count = 0
                    list_Lines = []
                    int_Loci_Number_In_Header = 0
                    int_Loci_Number_In_Detail_Line = 0
                    int_POP_1_Line_Count = 0
                    bool_POP_1 = False
                    list_Locus_Names = []
                    
                    for line in fileHandle.readlines():
                    
                        line_Current = line.strip('\n')
                        list_Lines.append(line_Current) 
                        int_Line_Count += 1
                        
                        '''
                        Count lines until you get the POP population data delimiter
                        This tells us the GENPOP format being used
                        Format_1: Loci are delimited by \n
                        Format_2: Loci are delimited by comma (,) 
                        '''
                        if line_Current.upper() == 'POP' and int_Line_Count > 2:
                            int_POP_Count +=1
                            if int_POP_Count > 1:
                                ''' Multiple POPs found - Error '''
                                bool_POP_1 = False
                                ''' We have multiple populations in the file '''
                                str_Message = 'Multiple populations found in the GENEPOP file. Please reconfigure to be only 1 population.'
                                bool_Success = False
                                return bool_Success, int_Loci_Number_In_Header, odict_Locus_Allele_Frequencies, str_Message
                            else:
                                ''' This the first time POP has been found '''                        
                                bool_POP_1 = True
                                int_POP_1_Line_Count = int_Line_Count
                                if int_POP_1_Line_Count == 3:
                                    int_File_Format = 2
                                    ''' Get the locus number and names '''
                                    list_Locus_Names = list_Lines[int_Line_Count-2].split(',')
                                    int_Loci_Number_In_Header = len(list_Locus_Names)
                                else:
                                    int_File_Format = 1
                                    ''' Get the locus number and names '''
                                    list_Locus_Names = [list_Lines[int_Count] for int_Count in range(1, int_Line_Count-1)]
                                    int_Loci_Number_In_Header = len(list_Locus_Names)
                                pass
                            pass
                        pass
                    
                        ''' Check the formatting of the line after the POP '''
                        if bool_POP_1 and int_POP_1_Line_Count+1 == int_Line_Count:
                            '''
                            Check the sample line is in the correct format
                            e.g. SAMPLE_NAME, 0101 0011 1010
                            '''
                            bool_Success, str_Message = func_Validate_Detail_Line(int_Line_Count, line_Current, int_Loci_Number_In_Header)
                            if not bool_Success:
                                return bool_Success, int_Loci_Number_In_Header, odict_Locus_Allele_Frequencies, str_Message
                            pass
                        
                            #''' Checks have finished so stop reading the lines '''
                            #break   
                        pass
                    pass
                    
                    ''' Check that POP was found '''
                    if not bool_POP_1:
                        ''' No populations in the file '''
                        str_Message = ''.join(['No populations were found in the GENEPOP file. At least one POP should exist. Please use valid GENEPOP formatting.'])
                        bool_Success = False
                        return bool_Success, int_Loci_Number_In_Header, odict_Locus_Allele_Frequencies, str_Message
                    pass     
                    
                    ''' If only locus number requested - return from this function withought getting allele freqs '''
                    if bool_Get_Locus_Number_Only:
                        return bool_Success, int_Loci_Number_In_Header, odict_Locus_Allele_Frequencies, str_Message
                    pass
            
                    ''' After initial validation - Read the detail lines and calculate allele frequencies '''
                    int_Line_Count = 0
                    list_Detail_Lines = [] 
                    
                    ''' Ignore all the lines until after the POP '''
                    fileHandle.seek(0)
                    for line in fileHandle.readlines():
                    
                        line_Current = line.strip('\n')
                        #list_Lines.append(line_Current) 
                        int_Line_Count += 1
                        
                        ''' Ignore all the lines until after the POP '''
                        if int_Line_Count > int_POP_1_Line_Count:

                            ''' Validate the detail line '''
                            '''
                            Check the sample line is in the correct format
                            e.g. SAMPLE_NAME, 0101 0011 1010
                            '''
                            bool_Success, str_Message = func_Validate_Detail_Line(int_Line_Count, line_Current, int_Loci_Number_In_Header)
                            if not bool_Success:
                                return bool_Success, int_Loci_Number_In_Header, odict_Locus_Allele_Frequencies, str_Message
                            pass
                            
                            ''' Validation passed - Accumulate data to calculate allele frequencies '''
                            
                            
                            line_Formatted = line_Current.replace(',',' ')
                            list_Fields = line_Formatted.split(' ')
                            ''' Remove any empty strings '''
                            list_Fields = filter(None, list_Fields)
                            #''' Separate genotypes and sample name '''
                            #list_Fields__Loci_Genotypes = list_Fields[1:]                            
                            #str_Sample_Name = list_Fields[0]

                            list_Detail_Lines.append(list_Fields) 
                        pass
                    pass
                
                    bool_Success = objFileOperation.fileClose(fileHandle)
                    
                    ''' Convert list of lists to array '''
                    np_array_Detail_Lines = np.asarray(list_Detail_Lines)

                    #DEBUG_ON
                    #np.set_printoptions(threshold=np.nan)
                    #print(np_array_Detail_Lines)
                    #DEBUG_OFF
                    
                    odict_Locus_Genotype_Freqs = OrderedDict()
                    
                    int_Rows, int_Cols = np_array_Detail_Lines.shape
                    for int_Col in range(1, int_Cols):
                        ''' Get the column '''
                        np_array_Col = np_array_Detail_Lines[:,int_Col]
                        
                        bool_Get_Genotype_Counts_And_Freqs = False
                        if bool_Get_Genotype_Counts_And_Freqs:
                            ''' Count the occurances of genotypes into dict '''
                            counter_Locus_Genotype_Counts = collections__Counter(np_array_Col)
                            dict_Locus_Genotype_Counts = dict(counter_Locus_Genotype_Counts)
                            
                            ''' Excluding missing data genotypes e.g. 000000 '''
                            [dict_Locus_Genotype_Counts.pop(key) for key in dict_Locus_Genotype_Counts.keys() if int(key) == 0]
                            ''' Convert into frequencies '''
                            int_Locus_Genotypes__Total = sum(dict_Locus_Genotype_Counts.values())
                            dict_Locus_Genotype_Freqs = dict([(str_Genotype, int_Count/float(int_Locus_Genotypes__Total)) for str_Genotype, int_Count in dict_Locus_Genotype_Counts.items()])
                            ''' Add to dict by locus name '''
                            str_Locus_Name = list_Locus_Names[int_Col-1]
                            odict_Locus_Genotype_Freqs[str_Locus_Name] = OrderedDict(sorted(dict_Locus_Genotype_Freqs.items()))
                        pass

                        bool_Get_Allele_Counts_And_Freqs = True
                        if bool_Get_Allele_Counts_And_Freqs:
                            ''' Determine the length of the alleles  '''
                            int_Genotype_Length = len(np_array_Col[0])
                            int_Allele_Length = int_Genotype_Length/2
                            ''' Split each genotype into alleles '''
                            list_tup_Alleles = [(str_Genotype[0:int_Allele_Length], str_Genotype[int_Allele_Length:int_Genotype_Length]) for str_Genotype in np_array_Col]
                            tup_Alleles_1, tup_Alleles_2 = zip(*list_tup_Alleles)
                            list_Alleles = list(tup_Alleles_1)
                            list_Alleles += list(tup_Alleles_2)
                            ''' Count the occurances of alleles into dict '''
                            counter_Locus_Allele_Counts = collections__Counter(list_Alleles)
                            dict_Locus_Allele_Counts = dict(counter_Locus_Allele_Counts)
                            ''' Excluding missing data alleles e.g. 000 '''
                            [dict_Locus_Allele_Counts.pop(key) for key in dict_Locus_Allele_Counts.keys() if int(key) == 0]
                            ''' Convert into frequencies '''
                            int_Locus_Alleles__Total = sum(dict_Locus_Allele_Counts.values())
                            dict_Locus_Genotype_Freqs = dict([(str_Allele, int_Count/float(int_Locus_Alleles__Total)) for str_Allele, int_Count in dict_Locus_Allele_Counts.items()])
                            ''' Add to dict by locus name '''
                            str_Locus_Name = list_Locus_Names[int_Col-1]
                            odict_Locus_Allele_Frequencies[str_Locus_Name] = OrderedDict(sorted(dict_Locus_Genotype_Freqs.items()))
                            
                            pass
                        pass
                    
                pass
                
                #DEBUG_ON
                bool_Debug = False
                if bool_Debug:
                    if bool_Get_Genotype_Counts_And_Freqs:
                        #print(odict_Locus_Genotype_Freqs)
                        for str_Locus, odict_Genotype_Frequencies in odict_Locus_Genotype_Freqs.items():
                            str_Message = str_Locus
                            for str_Genotype, float_Freq in odict_Genotype_Frequencies.items():
                                str_Message += ''.join(['; ', str_Genotype, ' = ', str(round(float_Freq,4)).zfill(5)])
                            pass
                            print(''.join([str_Message,'\n']))
                        pass
                    pass
                    if bool_Get_Allele_Counts_And_Freqs:
                        #print(odict_Locus_Allele_Freqs)
                        for str_Locus, odict_Allele_Frequencies in odict_Locus_Allele_Frequencies.items():
                            str_Message = str_Locus
                            for str_Allele, float_Freq in odict_Allele_Frequencies.items():
                                str_Message += ''.join(['; ', str_Allele, ' = ', '{0:.4f}'.format(round(float_Freq,4))])
                            pass
                            print(''.join([str_Message,'\n']))
                        pass
                    pass
                pass
                #DEBUG_OFF
                
                ''' Format allele freq dict to match legacy code '''
                int_Locus_Count = 0
                for str_Locus_Name, odict_Allele_Frequencies in odict_Locus_Allele_Frequencies.items():
                    
                    dict_Locus = {}
                    int_Allele_Count = 0
                    
                    for str_Allele, float_Freq in odict_Allele_Frequencies.items():
                        dict_Allele = {}
                        dict_Allele['Locus_Name'] = ''.join(['Locus_', str(int_Locus_Count+1)])
                        dict_Allele['Allele_Freq'] = float_Freq #round(float_Freq,7)
                        dict_Allele['Allele_Name'] = str_Allele
                        dict_Locus[int_Allele_Count] = dict_Allele
                        int_Allele_Count += 1
                    pass
                
                    #dict_Locus[int_Allele_Count] = dict_Allele_Dict
                    
                    
                    #dict_Locus_Dict[int_Locus_Count-1] = dict_Locus 
                    
                    odict_Locus_Allele_Frequencies_Output[int_Locus_Count] = dict_Locus
                    
                    int_Locus_Count += 1
                pass
            
                return bool_Success, int_Loci_Number_In_Header, odict_Locus_Allele_Frequencies_Output, str_Message

            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful

        self.SSInputOperation_obj = SSInputOperation() 
        return self.SSInputOperation_obj
 
    def __exit__(self, type, value, traceback): 
        self.SSInputOperation_obj.classCleanUp()