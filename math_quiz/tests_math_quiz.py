import unittest
from math_quiz import get_random_number, get_random_operation, math_generator


class TestMathGame(unittest.TestCase):

    def test_get_random_number(self):
        """
        Test if random numbers generated are within the specified range.
        Return (bool): True or False.
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operation(self):
        """
        Test if random math operations are addition, substraction and multiplication only.
        Return (bool): True or False.
        """
        op_list = ['+', '-', '*']
        for _ in range(10):  # Test ten times.
            rand_op = get_random_operation()
            self.assertTrue(rand_op in op_list)

    def test_math_generator(self):
        """
        Test if math operations are executed correctly.
        Return (bool): True or False.
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5,  2, '*', '5 * 2', 10),
            (3, 3, '+', '3 + 3', 6)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            mathgen_answer = math_generator(num1, num2, operator)
            self.assertTrue(mathgen_answer == expected_answer)

if __name__ == "__main__":
    unittest.main()