#Jake Felzien
# homework 4 assignment

#from homework4_refined import *
#from SudukoData import *
from templateClasses import *

if __name__ == '__main__':
	#testingFile = "SamplePuzzles/Input/Puzzle-4x4-0001.txt"
    testingFile = "SamplePuzzles/Input/Puzzle-9x9-0001.txt"
    testPuzzle = SudukoData(testingFile)

    print '\n'
    print "missingIndeces" , testPuzzle.missingIndices

    print testPuzzle.possibleOptionsDict

    test = AlgorithmBasis(testPuzzle)
    print test

    newTest = SquareCancellationFillIn(testPuzzle)

    print newTest.getIndex()