#Jake Felzien

#cs5700 Hw 3

#unit tests

import unittest

from homework3 import *

class TestMethods(unittest.TestCase):

    def test_square_coord_one(self):
        tester = Class_Box(1,2,3,4,99,99)
        self.assertEqual(tester.x0, 1)
        print "Test Completed"

    def test_square_coord_two(self):
        tester = Class_Box(1,2,3,4,99,99)
        self.assertEqual(tester.x1, 3)
        print "Test Completed"

    def test_square_coord_three(self):
        tester = Class_Box(1,2,3,4,99,99)
        self.assertEqual(tester.y0, 2)
        print "Test Completed"

    def test_square_coord_four(self):
        tester = Class_Box(1,2,3,4,99,99)
        self.assertEqual(tester.y1, 4)
        print "Test Completed"

    def test_binary_association_one(self):
        tester = Binary_Association(1,2,3,4,5)
        self.assertEqual(tester.x0, 1)
        print "Test Completed"

    def test_binary_association_two(self):
        tester = Binary_Association(1,2,3,4,5)
        self.assertEqual(tester.x1, 3)
        print "Test Completed"

    def test_binary_association_three(self):
        tester = Binary_Association(1,2,3,4,5)
        self.assertEqual(tester.y0, 2)
        print "Test Completed"

    def test_binary_association_four(self):
        tester = Binary_Association(1,2,3,4,5)
        self.assertEqual(tester.canvasObject, 5)
        print "Test Completed"

    def test_dependency_association_one(self):
        tester = Dependency_Association(1,2,3,4,5)
        self.assertEqual(tester.x0, 1)
        print "Test Completed"

    def test_dependency_association_two(self):
        tester = Dependency_Association(1,2,3,4,5)
        self.assertEqual(tester.x1, 3)
        print "Test Completed"

    def test_dependency_association_three(self):
        tester = Dependency_Association(1,2,3,4,5)
        self.assertEqual(tester.y0, 2)
        print "Test Completed"

    def test_dependency_association_four(self):
        tester = Dependency_Association(1,2,3,4,5)
        self.assertEqual(tester.canvasObject, 5)
        print "Test Completed"

    def test_stack_one(self):
        tester = UndoStack()
        sample = CommandStack()
        sample2 = CommandStack()
        tester.addExecutionChainCommand(sample)
        tester.addExecutionChainCommand(sample2)
        self.assertEqual(len(tester.stack),2)
        print "Test Completed"

    def test_stack_two(self):
        tester = UndoStack()
        sample = CommandStack()
        tester.addExecutionChainCommand(sample)
        self.assertEqual(len(tester.stack),1)
        print "Test Completed"

    def test_stack_three(self):
        tester = UndoStack()
        sample = CommandStack()
        tester.addExecutionChainCommand(sample)
        self.assertNotEqual(len(tester.stack),2)
        print "Test Completed"

    def test_stack_four(self):
        tester = UndoStack()
        sample = CommandStack()
        tester.addExecutionChainCommand(sample)
        self.assertNotEqual(len(tester.stack),4)
        print "Test Completed"

if __name__ == '__main__':
    unittest.main()
