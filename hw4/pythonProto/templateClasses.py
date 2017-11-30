# this will be for all of my template classes
# the algorithm portion

from SudukoData import *


class AlgorithmBasis:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def getIndex(self):
    	return self.puzzle.missingIndices[0]

    def getPossibleValues(self):
    	return self.puzzle.possibleOptionsDict[self.getIndex()]

    def getOtherPossibleValues(self, row, col):
    	return self.puzzle.possibleOptionsDict[(row,col)]

    def logicPortion(self):
    	pass

    def valueSelection(self):
    	pass

    def generateNewPuzzle(self):
    	pass

    def putPuzzleOnQueue(self):
    	pass


class OnlyOneOption(AlgorithmBasis):
	def logicPortion(self):
		print "missing indices", self.puzzle.missingIndices
		
		index = self.getIndex()
		subBoxSquare = self.puzzle.findSubBoxValue(index[0], index[1])
		#print subBoxSquare
		#works
		#print self.getPossibleValues()

		if len(self.getPossibleValues()) == 1:
			self.puzzle.puzzlearray[index[0]][index[1]] = self.getPossibleValues()[0]
			#self.puzzle.missingIndices.pop(0)
			return True

		else:
			return False


# this will be used for guessing (just put the first one if we are unsure of what to put.)
class GuessOption(AlgorithmBasis):
	def logicPortion(self):
		index = self.getIndex()
		subBoxSquare = self.puzzle.findSubBoxValue(index[0], index[1])

		if len(self.getPossibleValues()) > 1:
			self.puzzle.puzzlearray[index[0]][index[1]] = self.getPossibleValues()[0]
			return True

		else:
			return False

		

class RowFillIn(AlgorithmBasis):
	pass

class ColumnFillIn(AlgorithmBasis):
	pass

class SquareCancellationFillIn(AlgorithmBasis):
	def test(self):
		print 'hello'

	def logicPortion(self):
		index = self.getIndex()
		subBoxSquare = self.puzzle.findSubBoxValue(index[0], index[1])
		#print subBoxSquare
		#works
		#print self.getPossibleValues()

		tempAllOptions = []
		for index , i in enumerate(self.puzzle.puzzlearray):
			for index2 , j in enumerate(i):
				if self.puzzle.findSubBoxValue(index, index2) == subBoxSquare and j == '-' and index != self.getIndex()[0] and index != self.getIndex()[1]:
					tempAllOptions.append(self.getOtherPossibleValues(index, index2))

		#print tempAllOptions
		print "missing indices", self.puzzle.missingIndices

