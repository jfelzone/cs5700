
from sets import Set
import math as m

class SudukoData:
    def __init__(self, fileName):
        self.puzzlearray = []
        self.possibleValuesArray = []
        self.size = 0
        self.missingIndices = []
        self.possibleOptionsDict = {}


        filer = open(fileName, 'r')
        for line in filer:
            if line != "" or line != "\n":
                print line
                #temp = []
                temp = line.rstrip('\n').split(' ')
                # for value in line:
                #     temp.append(value.rstrip('\n'))
                self.puzzlearray.append(temp)

        self.possibleValuesArray = self.puzzlearray[1]
        self.size = int(self.puzzlearray[0][0])
        print self.size

        print self.possibleValuesArray

        #pop off the values that we don't need
        self.puzzlearray.pop(0)
        self.puzzlearray.pop(0)

        #print filer[0]
        #print filer[1]
        self.generateMissingSpots()
        print self.missingIndices

        #going to generate the different sub box pieces currentRow
        self.generateSubBoxes()
        #now we need to generate all the blank possibilities
        self.generatePossibilities()


    def generateMissingSpots(self):
        self.missingIndices = []
        # self.puzzlearray.pop(0)
        # self.puzzlearray.pop(0)
        for index1, i in enumerate(self.puzzlearray):
            for index2, j in enumerate(i):
                if self.puzzlearray[index1][index2] == '-':
                    self.missingIndices.append((index1, index2))
                    #it is at this point that we want to generate the possible values
                    # or perhaps i'll just make this 2 dimensional

    def generateSubBoxes(self):
        print "Printing puzzlearray"
        for i in self.puzzlearray:
            print i
        self.subBoxes = {}
        for i in xrange(0, self.size):
            self.subBoxes[i] = []
        print self.subBoxes

        for x, i in enumerate(self.puzzlearray):
            for y, j in enumerate(self.puzzlearray):
                #print x , y

                # this is all wrong

                # i need to not only fix this but make it much much better
                if x <= 2 and y <= 2:
                    self.subBoxes[0].append((x,y))
                elif x <= 2 and y <=5 and y >= 3:
                    self.subBoxes[1].append((x,y))
                elif x <= 2 and y <=8 and y >= 6:
                    self.subBoxes[2].append((x,y))
                elif x >= 3 and x <= 5 and y <= 2 and y >= 0:
                    self.subBoxes[3].append((x,y))
                elif x >= 3 and x <= 5 and y >= 3 and y <= 5:
                    self.subBoxes[4].append((x,y))
                elif x >= 3 and x <=5 and y >= 6 and y <= 8:
                    self.subBoxes[5].append((x,y))
                elif x >= 6 and x <= 8 and y >= 0 and y <= 2:
                    self.subBoxes[6].append((x,y))
                elif x >= 6 and x <= 8 and y >= 3 and y <= 5:
                    self.subBoxes[7].append((x,y))
                elif x >= 6 and x <= 8 and y >= 6 and y <= 8:
                    self.subBoxes[8].append((x,y))
        for i in self.subBoxes:
            print i, self.subBoxes[i]

    def findSubBoxValue(self, row, col):
        tempTuple = (row, col)
        tempSubBoxNumber = None
        for i in self.subBoxes:
            for j in self.subBoxes[i]:
                if j == tempTuple:
                    tempSubBoxNumber = i
                    return tempSubBoxNumber

    # im thinking for these i simply want to return the set
    # mostly becuase i can get the length of the set no problem
    def findRowPossibilities(self, rowIndex):
        currentRow = self.puzzlearray[rowIndex]
        #print rowIndex , currentRow
        totalVals = Set(self.possibleValuesArray)
        tempRow = Set(currentRow)
        #print "missing:" , totalVals - tempRow
        return totalVals - tempRow

    def findColumnPossibilities(self, columnIndex):
        currentColumn = []
        for x , i in enumerate(self.puzzlearray):
            for y , j in enumerate(i):
                if y == columnIndex:
                    currentColumn.append(j)
        #print currentColumn

        totalVals = Set(self.possibleValuesArray)
        tempCol = Set(currentColumn)
        #print "missing:" , totalVals - tempCol
        #print len(totalVals - tempCol)
        return totalVals - tempCol
        
    def findBoxPossibilities(self, rowIndex, columnIndex):
        tempSubBoxNumber = self.findSubBoxValue(rowIndex, columnIndex)
        #print "tempSubBoxNumber,", tempSubBoxNumber

        #now finding all values within that sub-box to perform set difference
        # array used to store the values in the box
        tempValuesInBox = []
        for index, i in enumerate(self.puzzlearray):
            for index2 , j in enumerate(i):
                if self.findSubBoxValue(index, index2) == tempSubBoxNumber:
                    tempValuesInBox.append(j)
        #print "indices", rowIndex, columnIndex
        #print "tempValuesInBox" , tempValuesInBox

        totalVals = Set(self.possibleValuesArray)
        tempBox = Set(tempValuesInBox)
        #print "missing:" , totalVals - tempBox
        #print len(totalVals - tempBox)

        return totalVals - tempBox

    def generatePossibilities(self):
        self.possibleOptionsDict = {}
        print '\n'
        
        for i in self.missingIndices:
            rowSet = self.findRowPossibilities(i[0])
            columnSet = self.findColumnPossibilities(i[1])
            boxSet = self.findBoxPossibilities(i[0], i[1])

            setsArray = [rowSet, columnSet, boxSet]
            print setsArray

            #smallest set logic was incorrect. we want the intersection (that is what is important)
            # minSize = 999

            # for x in setsArray:
            #     if len(x) < minSize:
            #         minSize = len(x)
            #         smallestSet = x

            smallestSet = rowSet.intersection(columnSet).intersection(boxSet)

            print "smallestSet", smallestSet
            arrayOfSmallestSet = []
            for j in smallestSet:
                arrayOfSmallestSet.append(j)


            self.possibleOptionsDict[i] = arrayOfSmallestSet
            print '\n'

        #print "self.possibleOptionsDict", self.possibleOptionsDict
        for value in self.possibleOptionsDict:
            print value, self.possibleOptionsDict[value]

    def refreshArrays(self):
        self.generateMissingSpots()
        self.generatePossibilities()





