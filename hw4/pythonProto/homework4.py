# Jake Felzien
# homework 4 assignment

## proto for python code

from sets import Set
import math as m

class SudukoData:
    def __init__(self, fileName):
        self.puzzlearray = []
        self.possibleValuesArray = []
        self.size = 0
        self.missingIndices = []


        filer = open(fileName, 'r')
        for line in filer:
            if line != "" or line != "\n":
                print line
                #temp = []
                temp = line.rstrip('\n').split(' ')
                # for value in line:
                #     temp.append(value.rstrip('\n'))
                self.puzzlearray.append(temp)

        for x in self.puzzlearray:
            print x
        print self.puzzlearray

        print "going to pop the last element here"
        #self.puzzlearray.pop()

        print self.puzzlearray

        self.possibleValuesArray = self.puzzlearray[1]
        self.size = int(self.puzzlearray[0][0])
        print self.size

        print self.possibleValuesArray
        #print filer[0]
        #print filer[1]
        self.generateMissingSpots()
        print self.missingIndices

        #going to generate the different sub box pieces currentRow
        self.generateSubBoxes()
    def generateMissingSpots(self):
        self.puzzlearray.pop(0)
        self.puzzlearray.pop(0)
        for index1, i in enumerate(self.puzzlearray):
            for index2, j in enumerate(i):
                if self.puzzlearray[index1][index2] == '-':
                    self.missingIndices.append((index1, index2))

    def generateSubBoxes(self):
        for i in self.puzzlearray:
            print i
        self.subBoxes = {}
        for i in xrange(0, self.size):
            self.subBoxes[i] = []
        print self.subBoxes

        for x, i in enumerate(self.puzzlearray):
            for y, j in enumerate(self.puzzlearray):
                #print x , y
                if x <= 2 and y <= 2:
                    self.subBoxes[0].append((x,y))
                elif x <= 5 and x >= 3 and y <=2:
                    self.subBoxes[1].append((x,y))
                elif x <= 8 and x >= 6 and y <=2:
                    self.subBoxes[2].append((x,y))
                elif x <= 2 and y >= 3 and y <= 5:
                    self.subBoxes[3].append((x,y))
                elif x >= 3 and x <= 5 and y >= 3 and y <= 5:
                    self.subBoxes[4].append((x,y))
                elif x >= 6 and y >= 3 and y <= 5:
                    self.subBoxes[5].append((x,y))
                elif x >= 0 and x <= 2 and y >= 6 and y <= 8:
                    self.subBoxes[6].append((x,y))
                elif x >=3 and x <= 5 and y >= 6 and y <= 8:
                    self.subBoxes[7].append((x,y))
                elif x >= 6 and x <= 8 and y >= 6 and y <= 8:
                    self.subBoxes[8].append((x,y))
        for i in self.subBoxes:
            print i, self.subBoxes[i]



class AlgorithmBasis:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def applyalgo(self):
        pass


class RowFillIn(AlgorithmBasis):
    def __init__(self, puzzle, missingSlot):
        self.puzzle = puzzle
        self.missingSlot = missingSlot

    def applyalgo(self):
        rowIndex = self.missingSlot[0]
        print "the rowindex value", rowIndex
        for index1, i in enumerate(self.puzzle.puzzlearray):
            if index1 == rowIndex:
                temp = []
                for j in i:
                    if j not in temp and j != '-':
                        temp.append(j)
                for index2, j in enumerate(i):
                    if j == '-':
                        possibleVals = Set(self.puzzle.possibleValuesArray)
                        currentRow = Set(i)
                        print "length test", len(possibleVals.difference(currentRow))
                        if len(possibleVals.difference(currentRow)) == 1:
                            for i in possibleVals.difference(currentRow):
                                value = i
                            self.puzzle.puzzlearray[index1][index2] = value
                        else:
                            continue

class SingleBoxFillIn(AlgorithmBasis):
    def __init__(self, puzzle, missingSlot):
        self.puzzle = puzzle
        self.missingSlot = missingSlot
        self.boxLoc = None

    def applyalgo(self):
        for i in self.puzzle.subBoxes:
            if self.missingSlot in self.puzzle.subBoxes[i]:
                self.boxLoc = i

        print self.boxLoc

        tempBoxValues = []
        tempBoxIndexValues = []
        for x, i in enumerate(self.puzzle.puzzlearray):
            for y, j in enumerate(i):
                if (x,y) in self.puzzle.subBoxes[self.boxLoc]:
                    #print x,y
                    tempBoxValues.append(j)
                    tempBoxIndexValues.append((x,y))
        print tempBoxValues
        print tempBoxIndexValues
        #for i in tempBoxValues:

            #print i
        numberOfEmpties = self.returnNumberOfDashes(tempBoxValues)
        print numberOfEmpties


    def returnNumberOfDashes(self, array):
        count = 0
        for i in array:
            if i == '-':
                count += 1
        return count

# class RowFillIn(AlgorithmBasis):
#     def __init__(self, puzzle):
#         self.puzzle = puzzle
#
#     def applyalgo(self):
#         for index1, i in enumerate(self.puzzle.puzzlearray):
#             temp = []
#             for j in i:
#                 if j not in temp and j != '-':
#                     temp.append(j)
#             for index2, j in enumerate(i):
#                 if j == '-':
#                     possibleVals = Set(self.puzzle.possibleValuesArray)
#                     currentRow = Set(i)
#                     print "length test", len(possibleVals.difference(currentRow))
#                     if len(possibleVals.difference(currentRow)) == 1:
#                         for i in possibleVals.difference(currentRow):
#                             value = i
#                         self.puzzle.puzzlearray[index1][index2] = value
#                     else:
#                         continue

class ColumnFillIn(AlgorithmBasis):
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def applyalgo(self):
        self.puzzle.puzzlearray.pop(0)
        self.puzzle.puzzlearray.pop(0)
        print "length:",  len(self.puzzle.puzzlearray)

        for index1, i in enumerate(self.puzzle.puzzlearray):
            for index2, j in enumerate(i):
                print self.puzzle.puzzlearray[index2][index1]
            print 'end of column'


class FindMisingIndices(AlgorithmBasis):
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.storeIndex = []
    def applyalgo(self):
        self.puzzle.puzzlearray.pop(0)
        self.puzzle.puzzlearray.pop(0)
        for index1, i in enumerate(self.puzzle.puzzlearray):
            for index2, j in enumerate(i):
                if self.puzzle.puzzlearray[index1][index2] == '-':
                    self.storeIndex.append((index1, index2))




# IDEA: i think here i want to do a better job of splitting stuff up. massive for loops is going to get ugly fast
# IDEA: i also think that it is going to be best to check rows and columns and have a specific thing for that
# IDEA: i think i want to be able to check stuff like rows and columns independently but im trying to envision the most productful way to do this
# IDEA: i also need to store the arrays as rows and columns i think...


# IDEA: here is another idea. lets store the positions of everything we want to solve and then from there treat the indices as the most important...
# from there it is super easy to grab the rows, and columns right around there
# i think i like that best so far..
# IDEA: but now i think i need to generate the box stuff from where we are. so for example i think i want to say, here you are, what box are you in and how do you do that

# IDEA: i think i also need to generate the different pieces of how to gather the box indices... i think storing those indices will be the best way to tackle that portion
# i think this could be a dictionary or something with a key that has an array of all of the index pairs or something like that
# because from the indices i will be able to extract everything from the 2-d array

if __name__ == "__main__":
    #testingFile = "SamplePuzzles/Input/Puzzle-4x4-0001.txt"
    testingFile = "SamplePuzzles/Input/Puzzle-9x9-0001.txt"
    testPuzzle = SudukoData(testingFile)


    rowFill = RowFillIn(testPuzzle, testPuzzle.missingIndices[0])
    rowFill.applyalgo()

    boxFill = SingleBoxFillIn(testPuzzle, testPuzzle.missingIndices[0])
    boxFill.applyalgo()

    # this is the format we are going to want until everything is filled in i believe (something along these lines)
    # for i in testPuzzle.missingIndices:
    #     # rowFill.applyalgo()
    #     # boxFill.applyalgo()
    #     rowFill = RowFillIn(testPuzzle, i)
    #     rowFill.applyalgo()
    #
    #     boxFill = SingleBoxFillIn(testPuzzle, i)
    #     boxFill.applyalgo()


    #store = FindMisingIndices(testPuzzle)
    #store.applyalgo()
    #print store.storeIndex

    # algo = RowFillIn(testPuzzle)
    #
    # algo.applyalgo()
    # print testPuzzle.puzzlearray
    #
    # algo2 = ColumnFillIn(testPuzzle)
    # algo2.applyalgo()
