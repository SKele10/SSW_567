# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testInvalidInputZero(self):
        self.assertEqual(classify_triangle(0, 0, 0), 'InvalidInput', '0,0,0 should return InvalidInput')
        
    def testInvalidInputNegative(self):
        self.assertEqual(classify_triangle(-1, -1, -1), 'InvalidInput', '-1,-1,-1 should return InvalidInput')
    
    def testInvalidInputExceedsMax(self):
        self.assertEqual(classify_triangle(201, 1, 1), 'InvalidInput', '201,1,1 should return InvalidInput')
    
    def testNonIntegerInput(self):
        self.assertEqual(classify_triangle(1.5, 2.5, 3.5), 'InvalidInput', '1.5, 2.5, 3.5 should return InvalidInput')

    def testNotATriangleA(self):
        self.assertEqual(classify_triangle(1, 2, 3), 'NotATriangle', '1,2,3 should not form a triangle')

    def testNotATriangleB(self):
        self.assertEqual(classify_triangle(5, 9, 14), 'NotATriangle', '5,9,14 should not form a triangle')
    
    def testIsoscelesTriangle(self):
        self.assertEqual(classify_triangle(5, 5, 8), 'Isosceles', '5,5,8 should be Isosceles')

    def testScaleneTriangle(self):
        self.assertEqual(classify_triangle(7, 8, 9), 'Scalene', '7,8,9 should be Scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

