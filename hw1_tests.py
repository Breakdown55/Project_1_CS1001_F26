"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1

from math import sqrt

class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        text = "SkippE"
        expected = 2

        actual = hw1.vowel_count(text)

        self.assertEqual(actual, expected)
        

    def test_vowel_count_empty_string(self):
        text = ""
        expected = 0

        actual = hw1.vowel_count(text)

        self.assertEqual(actual, expected)


    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        test_list = [[9,5], [1,2,3], [], [5], [1,2], [1,2], [5,0], []]
        expected = [[9,5], [1,2], [1,2], [5,0]]

        actual = hw1.short_lists(test_list)

        self.assertEqual(actual, expected)

    def test_short_lists_no_matching_lengths(self):
        test_list = [[1,2,3], [5], []]
        expected = []

        actual = hw1.short_lists(test_list)

        self.assertEqual(actual, expected)



    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        test_list = [[1,2], [2,1], [3,4], [4,3]]
        expected = [[1,2], [1,2], [3,4], [3,4]]

        actual = hw1.ascending_pairs(test_list)

        self.assertEqual(actual, expected)


    def test_ascending_pairs_other_lengths_unchanged(self):
        test_list = [[1,2], [6,5,3], [2,1], [9,8,7,6,5], [3,4], [4,3]]
        expected = [[1,2], [6,5,3], [1,2], [9,8,7,6,5], [3,4], [3,4]]

        actual = hw1.ascending_pairs(test_list)

        self.assertEqual(actual, expected)

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        price1 = data.Price(3, 20)
        price2 = data.Price(5, 5)

        expected = data.Price(8, 25)

        actual = hw1.add_prices(price1, price2)

        self.assertEqual(expected, actual)


    def test_add_prices_with_cents_carry(self):
        price1 = data.Price(4, 80)
        price2 = data.Price(2, 55)

        expected = data.Price(7, 35)

        actual = hw1.add_prices(price1, price2)

        self.assertEqual(expected, actual)



    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        top_left_point = data.Point(5, 5)
        bottom_right_point = data.Point(10, 2)

        rectangle = data.Rectangle(top_left_point, bottom_right_point)

        expected = 15

        actual = hw1.rectangle_area(rectangle)

        self.assertEqual(expected, actual)


    def test_rectangle_area_negative_coordinates(self):
        top_left_point = data.Point(-3, -4)
        bottom_right_point = data.Point(5, 2)

        rectangle = data.Rectangle(top_left_point, bottom_right_point)

        expected = 48

        actual = hw1.rectangle_area(rectangle)

        self.assertEqual(expected, actual)
        


    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        book1 = data.Book(["Joe", "Lola", "Sam"], "The Adventures")
        book2 = data.Book(["Sam"], "The Man")
        book3 = data.Book(["Joe", "Lola"], "The Dynamic Duo: Us")
        test_books = [book1, book2, book3]

        expected = [book1, book2]

        actual = hw1.books_by_author("Sam", test_books)

        self.assertEqual(expected, actual)


    def test_books_by_author_no_matches(self):
        book1 = data.Book(["Joe", "Lola", "Sam"], "The Adventures")
        book2 = data.Book(["Sam"], "The Man")
        book3 = data.Book(["Joe", "Lola"], "The Dynamic Duo: Us")
        test_books = [book1, book2, book3]

        expected = []

        actual = hw1.books_by_author("Billy", test_books)

        self.assertEqual(expected, actual)

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        rect_top_left = data.Point(0, 5)
        rect_bottom_right = data.Point(5, 0)
        rectangle = data.Rectangle(rect_top_left, rect_bottom_right)

        expected_center_x = 2.5
        expected_center_y = 2.5
        expected_radius = sqrt(2.5*2.5 + 2.5*2.5)

        actual = hw1.circle_bound(rectangle)

        self.assertAlmostEqual(actual.center.x, expected_center_x)
        self.assertAlmostEqual(actual.center.y, expected_center_y)
        self.assertAlmostEqual(actual.radius, expected_radius)


    def test_circle_bound_non_square_rectangle(self):
        rect_top_left = data.Point(5, 5)
        rect_bottom_right = data.Point(9, 3)
        rectangle = data.Rectangle(rect_top_left, rect_bottom_right)

        expected_center_x = 7.0
        expected_center_y = 4.0
        expected_radius = sqrt(2.0*2.0 + 1.0*1.0)

        actual = hw1.circle_bound(rectangle)

        self.assertAlmostEqual(actual.center.x, expected_center_x)
        self.assertAlmostEqual(actual.center.y, expected_center_y)
        self.assertAlmostEqual(actual.radius, expected_radius)

    def test_circle_bound_negative_coordinates(self):
        rect_top_left = data.Point(-5, 8)
        rect_bottom_right = data.Point(3, -10)
        rectangle = data.Rectangle(rect_top_left, rect_bottom_right)

        expected_center_x = -1.0
        expected_center_y = -1.0
        expected_radius = sqrt(4.0*4.0 + 9.0*9.0)

        actual = hw1.circle_bound(rectangle)

        self.assertAlmostEqual(actual.center.x, expected_center_x)
        self.assertAlmostEqual(actual.center.y, expected_center_y)
        self.assertAlmostEqual(actual.radius, expected_radius)




    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):

        employees = [
            data.Employee("Howard", 43),
            data.Employee("Janie", 21),
            data.Employee("Sam", 84),
            data.Employee("Shelia", 54),
            data.Employee("John", 12)
        ]

        expected = ["Janie", "John"]

        actual = hw1.below_pay_average(employees)

        self.assertEqual(expected, actual)



        

    def test_below_pay_average_empty_list(self):
        employees = []

        expected = []

        actual = hw1.below_pay_average(employees)

        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
