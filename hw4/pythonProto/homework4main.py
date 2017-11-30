#Jake Felzien
# homework 4 assignment

#from homework4_refined import *
#from SudukoData import *
from templateClasses import *

if __name__ == '__main__':
	#testingFile = "SamplePuzzles/Input/Puzzle-4x4-0001.txt"
    #testingFile = "SamplePuzzles/Input/Puzzle-9x9-0001.txt"
    testingFile = "SamplePuzzles/Input/Puzzle-9x9-0206.txt"
    testPuzzle = SudukoData(testingFile)

    print '\n'
    print "missingIndeces" , testPuzzle.missingIndices

    print testPuzzle.possibleOptionsDict

    test = AlgorithmBasis(testPuzzle)
    print test

    newTest = OnlyOneOption(testPuzzle)

    newTest.logicPortion()

    # while len(testPuzzle.missingIndices) > 0:
    # 	for x in xrange(0, len(testPuzzle.missingIndices)):
    # 		print newTest.getIndex()
    # 		if not newTest.logicPortion():
    # 			frontVal = testPuzzle.missingIndices.pop(0)
    # 			testPuzzle.missingIndices.append(frontVal)
    # 	testPuzzle.refreshArrays()


    for i in testPuzzle.puzzlearray:
    	print i