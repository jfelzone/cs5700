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
                print x,y




class AlgorithmBasis:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def applyalgo(self):
        pass


class RowFillIn(AlgorithmBasis):
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def applyalgo(self):
        for index1, i in enumerate(self.puzzle.puzzlearray):
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
