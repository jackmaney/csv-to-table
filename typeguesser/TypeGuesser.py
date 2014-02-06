import csv
from numbers import Real
import random
from warnings import warn
from dateutil import parser as dateParser


class TypeGuesser(object):
    def __init__(self, fileName, hasHeader, sampleProbability=None, delimiter=',', quotechar='"'):
        self.file = fileName
        self.hasHeader = hasHeader

        if sampleProbability is not None and not isinstance(sampleProbability, Real) and \
                (sampleProbability > 1 or sampleProbability < 0):
            raise ValueError("The parameter sampleProbability must either be None or a number between 0 and 1")

        self.sampleProbability = sampleProbability
        self.delimiter = delimiter
        self.quoteChar = quotechar
        self.fileSample = []
        self.types = []

        self.dispatch = {
            "bool": self.isBool,
            "date": self.isDate,
            "timestamp": self.isTimestamp,
            "numeric": self.isNumeric,
            "int": self.isInteger
        }

    def sampleFile(self):
        """
        Grabs a list of lists representing a sample of the file.
        The sample is either sampleSize rows or all of the file
        depending on whether or not sampleSize is None.

        While reading through the file, we also make sure that each
        row belongs to the same number of columns.
        """
        result = []
        colCount = None
        rowCounter = 0

        with open(self.file) as f:
            reader = csv.reader(f, delimiter=self.delimiter, quotechar=self.quoteChar)
            for row in reader:
                rowCounter += 1

                if colCount is None:
                    colCount = len(row)
                else:
                    if colCount != len(row):
                        raise Exception("Column count mismatch at row %d: (%d vs %d)" %
                                        (rowCounter, colCount, len(row)))

                if rowCounter == 1 and self.hasHeader:
                    continue

                if self.sampleProbability is None or random.random() <= self.sampleProbability:
                    result.append(row)

        self.fileSample = result
        self.types = [None] * colCount

    @staticmethod
    def isBool(string):
        return string.lower() in ["true", "false", "t", "f"]

    @staticmethod
    def isTimestamp(string):
        try:
            dateParser.parse(string)
        except:
            return False

    @staticmethod
    def isDate(string):
        try:
            dt = dateParser.parse(string)
            return (dt.hour, dt.minute, dt.second) == (0, 0, 0)
        except:
            return False

    @staticmethod
    def isNumeric(string):

        # If there's a leading zero, then it probably shouldn't be a number...
        if string[0] not in "123456789.":
            return False

        try:
            float(string)
            return True
        except:
            return False

    @staticmethod
    def isInteger(string):
        if string[0] not in "123456789":
            return False

        try:
            a = float(string)
            n = int(a)
            
            return a == n
        except:
            return False

    def guessTypes(self):

        if not self.fileSample:

            self.sampleFile()

            if not self.fileSample:
                warn("No lines found in file %s" % self.file)
                return

        for row in self.fileSample:
            for i, dataType in enumerate(self.types):
                if dataType is None:
                    possibleTypes = ["bool", "date", "timestamp", "int", "bigint"]

                    for possibleType in possibleTypes:
                        if self.dispatch[possibleType](row[i]):
                            self.types[i] = possibleType
                            break

                    if self.types[i] is None:
                        self.types[i] = "text"

                elif dataType == "bool":
                    if not self.isBool(row[i]):
                        self.types[i] = "text"

                elif dataType == "date":
                    if not self.isDate(row[i]):
                        if self.isTimestamp(row[i]):
                            self.types[i] = "timestamp"
                        else:
                            self.types[i] = "text"

                elif dataType == "timestamp":
                    if not self.isTimestamp(row[i]):
                            self.types[i] = "text"

                elif dataType == "int":
                    if not self.isInteger(row[i]):
                        if self.isNumeric(row[i]):
                            self.types[i] = "numeric"
                        else:
                            self.types[i] = "int"




                            




