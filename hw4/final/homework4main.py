#Jake Felzien
# homework 4 assignment

#from homework4_refined import *
#from SudukoData import *
from templateClasses import *

import sys
import time

if __name__ == '__main__':
	start_time = time.time()
	#print len(sys.argv)
	if sys.argv[1] == '-h':
		print "command line arguments [1]  input text file name  [2]  output text file name "
		quit()
	else:
		#testingFile = "SamplePuzzles/Input/Puzzle-4x4-0001.txt"
		#########testingFile = "SamplePuzzles/Input/Puzzle-9x9-0001.txt"
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

		file.write('\n')
		file.write('\n')

		file.write("Total Time: " + str(time.time() - start_time))
		file.write('\n')
		file.write('\n')


		file.write("Strategy \t\t\t Uses \t\t Time\n")
		file.write(newTest.name+ "\t\t\t"+str(newTest.iterations)+"\t\t"+str(newTest.time))
