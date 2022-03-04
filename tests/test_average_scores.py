"""
Assignment: Unit Tests Dictionaries Assignment
Program: main.py
Author: Colby Boell
Last date modified: 03/04/2022

The purpose of this assignment is to test our code with unit tests.

Previous assignment review:
The purpose of this program is to that prompts a user for test score inputs and stores
them in a dictionary (first function) and then uses a second function to return the average
test scores.
"""
import unittest
from main.main import average_scores
# from directory.filename import function (above)


# unit test provided
class MyTestCase(unittest.TestCase):
    def test_average(self):
        # Arrange
        self.scores_dict = {"Test 1": 31, "Test 2": 34, "Test 3": 54}
        expected = 39.66666666  # 7 decimal places, remove one and see the test fail
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual)

    # test for average of 5 scores
    def test_average_five(self):
        # Arrange
        self.scores_dict = {"Test 1": 45, "Test 2": 87, "Test 3": 67, "Test 4": 76, "Test 5": 57}
        expected = 66.4
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual)

    # test for if the dictionary is empty / throw Value error
    def test_average_zero(self):
        # Arrange
        self.scores_dict = {}
        # Act
        # Assert
        with self.assertRaises(ValueError):
            average_scores(self.scores_dict)


if __name__ == '__main__':
    unittest.main()
