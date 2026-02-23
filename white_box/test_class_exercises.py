# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import divide, get_grade, is_even, is_triangle


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")

    def test_check_number_status_positive(self):
        """
        Checks if a number is positive.
        """
        self.assertEqual(check_number_status(10), "Positive")

    def test_check_number_status_negative(self):
        """
        Checks if a number is negative.
        """
        self.assertEqual(check_number_status(-5), "Negative")

    def test_check_number_status_zero(self):
        """
        Checks if a number is zero.
        """
        self.assertEqual(check_number_status(0), "Zero")

    def test_validate_password_yes(self):
        """
        Checks if a password is valid.
        """
        self.assertTrue(validate_password("Valid123!"))
    
    def test_validate_password_no_length(self):
        """
        Checks if a password is invalid due to length.
        """
        self.assertFalse(validate_password("Short1!"))
    
    def test_validate_password_no_uppercase(self):
        """
        Checks if a password is invalid due to missing uppercase letter.
        """
        self.assertFalse(validate_password("valid123!"))
    
    def test_validate_password_no_lowercase(self):
        """
        Checks if a password is invalid due to missing lowercase letter.
        """
        self.assertFalse(validate_password("INVALID123!"))
    
    def test_validate_password_no_digit(self):
        """
        Checks if a password is invalid due to missing digit.
        """
        self.assertFalse(validate_password("Invalid!"))
    
    def test_validate_password_no_special_character(self):
        """
        Checks if a password is invalid due to missing special character.
        """
        self.assertFalse(validate_password("Invalid123"))

    def test_calculate_total_discount_zero(self):
        """
        Checks the total discount calculation for an amount less than 100.
        """
        self.assertEqual(calculate_total_discount(99), 0)

    def test_calculate_total_discount_ten(self):
        """
        Checks the total discount calculation for an amount between 100 and 500.
        """
        self.assertEqual(calculate_total_discount(400), 40)
    
    def test_calculate_total_discount_twenty(self):
        """
        Checks the total discount calculation for an amount greater than 500.
        """
        self.assertEqual(calculate_total_discount(600), 120)

    def calculate_order_total_between_1_and_5(self):
        """
        Checks the total order calculation for a number of items between 1 and 5. 0% discount.
        """
        self.assertEqual(calculate_order_total([10, 20, 30, 40, 50]), 150)

    def test_calculate_order_total_between_6_and_10(self):
        """
        Checks the total order calculation for a number of items between 6 and 10. 5% discount.
        """
        self.assertEqual(calculate_order_total([10, 20, 30, 40, 50, 60]), 171)

