#Jake Felzien
# homework 4 assignment

#from homework4_refined import *
#from SudukoData import *
from templateClasses import *

import sys

if __name__ == '__main__':
	#print len(sys.argv)
	if sys.argv[1] == '-h':
		print "command line arguments [1]  input text file name  [2]  output text file name "
		quit()
	else:
		#testingFile = "SamplePuzzles/Input/Puzzle-4x4-0001.txt"
		#testingFile = "SamplePuzzles/Input/Puzzle-9x9-0001.txt"
		#testingFile = "SamplePuzzles/Input/Puzzle-9x9-0206.txt"
		inputFile = sys.argv[1]
		outputFile = sys.argv[2]
		

		testPuzzle = SudukoData(inputFile)
		file = open(outputFile, 'w')

		for i in testPuzzle.puzzlearray:
			for j in i:
				file.write(str(j)+ '  ')
			file.write('\n')

		file.write('\n')
		file.write('\n')

		print '\n'
		print "missingIndeces" , testPuzzle.missingIndices

		print testPuzzle.possibleOptionsDict

		test = AlgorithmBasis(testPuzzle)
		print test

		newTest = OnlyOneOption(testPuzzle)

		newTest.logicPortion()

		while len(testPuzzle.missingIndices) > 0:
			for x in xrange(0, len(testPuzzle.missingIndices)):
				print newTest.getIndex()
				if not newTest.logicPortion():
					frontVal = testPuzzle.missingIndices.pop(0)
					testPuzzle.missingIndices.append(frontVal)
			testPuzzle.refreshArrays()

		file.write("Solved \n")
		for i in testPuzzle.puzzlearray:
			for j in i:
				file.write(str(j)+ '  ')
			file.write('\n')

