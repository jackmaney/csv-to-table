import csv
import re
from numbers import Real
import random
from warnings import warn
from dateutil import parser as dateParser


class TypeGuesser(object):

    def __init__(self, fileName, header=False, sampleProbability=None,
                 delimiter=',', quotechar='"', tableName=None, columns=None,
                 lowercaseHeader=False):
        self.file = fileName
        self.hasHeader = header

        if sampleProbability is not None and not isinstance(sampleProbability, Real) and \
                (sampleProbability > 1 or sampleProbability < 0):
            raise ValueError(
                "The parameter sampleProbability must either be None or a number between 0 and 1")

        self.sampleProbability = sampleProbability
        self.delimiter = delimiter
        self.quoteChar = quotechar
        self.lowercaseHeader = lowercaseHeader
        self.fileSample = []

        self.types = []

        # The data types of the current row
        self._currentTypes = []

        # The data types of the previous row.
        # Once we get the types of the current row, we
        # compare to self.previousTypes and for each column,
        # we take the more general type.
        self._previousTypes = []

        if columns is None:
            self.columns = []
        else:
            self.columns = columns

        self.dispatch = {
            "boolean": self.isBool,
            "date": self.isDate,
            "timestamp": self.isTimestamp,
            "numeric": self.isNumeric,
            "int": self.isInteger
        }

        if tableName is None:
            self.tableName = self.file.replace(".csv", "")
        else:
            self.tableName = tableName

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
            reader = csv.reader(f, delimiter=self.delimiter,
                                quotechar=self.quoteChar)
            for row in reader:
                rowCounter += 1

                if colCount is None:
                    colCount = len(row)
                else:
                    if colCount != len(row):
                        raise Exception(
                            "Column count mismatch at row %d: (%d vs %d)" %
                            (rowCounter, colCount, len(row)))

                if rowCounter == 1 and self.hasHeader:
                    self.columns = self.tidyColumns(row)
                    if self.lowercaseHeader:
                        self.columns = [x.lower() for x in self.columns]
                    continue

                if self.sampleProbability is None or random.random() <= self.sampleProbability:
                    result.append(row)

        self.fileSample = result
        self.types = [None] * colCount

        if not self.hasHeader and not self.columns:
            self.columns = ["col" + str(i) for i in list(range(colCount))]

    @staticmethod
    def isBool(string):
        return string.lower() in ["true", "false", "t", "f", "0", "1"]

    @staticmethod
    def isTimestamp(string):
        try:
            dateParser.parse(string)
            return True
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
        try:
            float(string)
            return True
        except:
            return False

    @staticmethod
    def isInteger(string):
        try:
            a = float(string)
            n = int(a)

            return a == n
        except:
            return False

    @staticmethod
    def alterColumnName(name):
        return re.sub('[-\s]', '_', name)


    def tidyColumns(self, columns):
        return map(self.alterColumnName, columns)


    def guessType(self, s):

        # If our field is null, then we have no guess, so return None
        if not s:
            return None

        if self.isNumeric(s):
            if float(s) == int(float(s)):
                if s == "0" or s == "1":
                    return "boolean"

                if s[0] == "0":
                    return "text"

                if -32768 <= int(float(s)) <= 32767:
                    return "smallint"

                if -2147483648 <= int(float(s)) <= 2147483647:
                    return "int"
                else:
                    return "bigint"
            else:
                return "numeric"
        else:
            if self.isBool(s):
                return "boolean"

            if self.isTimestamp(s):
                if self.isDate(s):
                    return "date"
                else:
                    return "timestamp"

        return "text"

    def reconcileTypes(self):

        for i, currentType in enumerate(self._currentTypes):
            previousType = self._previousTypes[i]

            # The idea is that previousType is the most general datatype
            # of the rows that we've seen thus far.
            # So, easy case to deal with: previousType == currentType

            if currentType == previousType:
                # includes both being None
                self.types[i] = currentType
            else:
                # If one of currentType or previousType is None,
                # take whichever isn't None

                if previousType is None:
                    self.types[i] = currentType
                elif currentType is None:
                    self.types[i] = previousType

                # With that out of the way, we'll start with the largest type
                # first:

                if previousType == "text":
                    self.types[i] = "text"
                # Now, we'll worry about numeric, we switch only if currentType
                # is not a number.
                elif previousType == "numeric":
                    if currentType in ["numeric", "bigint", "int", "smallint", "boolean"]:
                        self.types[i] = previousType
                    else:
                        self.types[i] = "text"
                # For bigint, we switch only if currentType is numeric or not a
                # number
                elif previousType == "bigint":
                    if currentType in ["bigint", "int", "smallint", "boolean"]:
                        self.types[i] = previousType
                    elif currentType == "numeric":
                        self.types[i] = "numeric"
                    else:
                        self.types[i] = "text"
                # Same idea...
                elif previousType == "int":
                    if currentType in ["int", "smallint", "boolean"]:
                        self.types[i] = previousType
                    elif self.types[i] in ["numeric", "bigint"]:
                        self.types[i] = currentType
                    else:
                        self.types[i] = "text"
                # TODO: Set up a tree of types to replace this non-DRY
                # stuff....blarg...
                elif previousType == "smallint":
                    if currentType in ["smallint", "boolean"]:
                        self.types[i] = previousType
                    elif currentType in ["numeric", "bigint", "int"]:
                        self.types[i] = currentType
                    else:
                        self.types[i] = "text"
                elif previousType == "boolean":
                    if currentType in ["numeric", "bigint", "int", "smallint", "boolean"]:
                        self.types[i] = currentType
                    else:
                        self.types[i] = "text"
                # We just have two cases left...
                elif previousType == "timestamp":
                    if currentType in ["timestamp", "date"]:
                        self.types[i] = currentType
                    else:
                        self.types[i] = "text"

    def guessTypes(self):

        if not self.fileSample:

            self.sampleFile()

            if not self.fileSample:
                warn("No lines found in file %s" % self.file)
                return

        for row in self.fileSample:
            self._currentTypes = [None] * len(row)

            for i, field in enumerate(row):
                self._currentTypes[i] = self.guessType(field)

            if self._previousTypes:
                self.reconcileTypes()

            self._previousTypes = self._currentTypes

        # At this point, we *could* have Nones in self.types if a column has all null values.
        # In that case, we'll guess a type of "text".

        self.types = [x if x is not None else "text" for x in self.types]

    def getCreateStatement(self):
        if any([x is None for x in self.types]):
            self.guessTypes()

            if any([x is None for x in self.types]):
                raise Exception(
                    "Unable to guess types (got None for at least one data type)")

        lines = ["CREATE TABLE " + self.tableName + " ("]

        for i, column in enumerate(self.columns):
            nextLine = "\t" + column + " " + self.types[i]

            if i < len(self.columns) - 1:
                nextLine += ","

            lines.append(nextLine)

        lines.append(");")

        return "\n".join(lines)
