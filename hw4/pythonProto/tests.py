# Jake Felzien
# testing for homework 4
#
#
# tests see below


import unittest

from homework4main import *

class TestMethods(unittest.TestCase):

    def test_square_coord_one(self):
        self.assertEqual(1, 1)
        print "Test Completed"	
    
    def test_sudoku_structure(self):
        filename = "SamplePuzzles/Input/Puzzle-9x9-0001.txt"
	test = SudukoData(filename)
        self.assertEqual(test.puzzlearray[0][0], '4')
        print "Test Completed"

    def test_sudoku_structure_two(self):
        filename = "SamplePuzzles/Input/Puzzle-9x9-0001.txt"
	test = SudukoData(filename)
        self.assertEqual(test.puzzlearray[0][1], '9')
        print "Test Completed"
    
    def test_sudoku_structure_three(self):
        filename = "SamplePuzzles/Input/Puzzle-9x9-0001.txt"
	test = SudukoData(filename)
        self.assertNotEqual(test.missingIndices[0], 0)
        print "Test Completed"


    def test_sudoku_structure_four(self):
        filename = "SamplePuzzles/Input/Puzzle-9x9-0001.txt"
	test = SudukoData(filename)
	for i in test.missingIndices:
		self.assertNotEqual(len(i), 0)
        print "Test Completed"


if __name__ == '__main__':
    unittest.main()
