# this will be for all of my template classes
# the algorithm portion

from SudukoData import *


class AlgorithmBasis:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def getIndex(self):
    	return self.puzzle.missingIndices[0]

    def logicPortion(self):
    	pass

    def valueSelection(self):
    	pass

    def generateNewPuzzle(self):
    	pass

    def putPuzzleOnQueue(self):
    	pass


class RowFillIn(AlgorithmBasis):
	pass

class ColumnFillIn(AlgorithmBasis):
	pass

class SquareCancellationFillIn(AlgorithmBasis):
	def test(self):
		print 'hello'

