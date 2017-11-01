#Jake Felzien

#cs5700 Hw 3

#unit tests 

import unittest

from pythonProto import *

class TestMethods(unittest.TestCase):
    
    def test_square_coord_one(self):
        tester = Class_Box(1,2,3,4,99)
        self.assertEqual(tester.x0, 1)
        print "Test Completed"
    
    def test_square_coord_two(self):
        tester = Class_Box(1,2,3,4,99)
        self.assertEqual(tester.x1, 3)
        print "Test Completed"

    def test_square_coord_three(self):
        tester = Class_Box(1,2,3,4,99)
        self.assertEqual(tester.y0, 2)
        print "Test Completed"

    def test_square_coord_four(self):
        tester = Class_Box(1,2,3,4,99)
        self.assertEqual(tester.y1, 4)
        print "Test Completed"

if __name__ == '__main__':
    unittest.main()