# Jake Felzien
# homework 4 assignment

## proto for python code

from sets import Set

class SudukoData:
    def __init__(self, fileName):
        self.puzzlearray = []
        self.possibleValuesArray = []
        self.size = 0


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


        self.puzzlearray.pop()

        print self.puzzlearray

        self.possibleValuesArray = self.puzzlearray[1]
        self.size = int(self.puzzlearray[0][0])
        print self.size
        print self.possibleValuesArray
        #print filer[0]
        #print filer[1]




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
                        pass

class ColumnFillIn(AlgorithmBasis):
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def applyalgo(self):
        self.puzzle.puzzlearray.pop(0)
        self.puzzle.puzzlearray.pop(0)

        for index1, i in enumerate(self.puzzle.puzzlearray):
            for index2, j in enumerate(i):
                print self.puzzle.puzzlearray[index2][index1]
            print 'end of column'


# IDEA: i think here i want to do a better job of splitting stuff up. massive for loops is going to get ugly fast
# IDEA: i also think that it is going to be best to check rows and columns and have a specific thing for that
# IDEA: i think i want to be able to check stuff like rows and columns independently but im trying to envision the most productful way to do this

if __name__ == "__main__":
    testingFile = "SamplePuzzles/Input/Puzzle-4x4-0001.txt"
    testPuzzle = SudukoData(testingFile)

    algo = RowFillIn(testPuzzle)

    algo.applyalgo()
    print testPuzzle.puzzlearray

    algo2 = ColumnFillIn(testPuzzle)
    algo2.applyalgo()
