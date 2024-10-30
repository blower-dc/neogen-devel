gstringModuleName='OutputHandler.py'
gstringClassName='OutputOperation'

class OutputHandler:
    """Handle OutputOperation objects"""
    def __enter__(self):
         
        class OutputOperation: 
            """Explicitly control all fundemental output operations"""

            def AutomaticLociNamesList(self, nLoci):

                listLociNames = []

                for i in range(1, nLoci+1):
                    strLociName = listLociNames.append('Locus-' + str(i))
        
                return listLociNames

            def method_AccumulateListValuesIntoDelimetedString(self, listValues, stringDelimiter):

                #Combine multiple values into a single value for output
                strDelimitedValues=''
                boolFirstValue=False
                for value in listValues:
                    if boolFirstValue == False:
                        boolFirstValue = True
                        strDelimitedValues = strDelimitedValues + str(value)
                    else:
                        strDelimitedValues = strDelimitedValues + stringDelimiter + str(value)
                
                return strDelimitedValues

            def method_FileOutput_WriteDelimitedValue(self, outputFileHandle, value, strDelimiter):

                #Pass a blank delimiter if none required
                outputFileHandle.write(strDelimiter)
                outputFileHandle.write(value)
                
                pass

            def method_ConsoleOutput_WriteDelimitedValue(self, objOutput, value, strDelimiter):

                intValueLength = len(value)
                intLeftJustify = 5 + intValueLength
                stringPadChar = '-'
                stringPadString = ''
                stringLeftJustifyFormat = '{:' + stringPadChar + '<' + str(intLeftJustify) + '}'
                
                #Pass a blank delimiter if none required
                #objOutput.write(strDelimiter)
                #objOutput.write(value)
                objOutput.write(stringLeftJustifyFormat.format(value) + stringPadString)
                pass

            def classCleanUp(self):
                # Add class clean up items here
                boolSuccessful=False

                return boolSuccessful
                        
        self.OutputOperation_obj = OutputOperation() 
        return self.OutputOperation_obj

    def __exit__(self, type, value, traceback): 
        self.OutputOperation_obj.classCleanUp()