# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import divide, get_grade, is_even, is_triangle, check_number_status, validate_password, calculate_total_discount, calculate_order_total, calculate_items_shipping_cost, validate_login, verify_age, categorize_product, validate_email, celsius_to_fahrenheit, validate_credit_card, validate_date, check_flight_eligibility, validate_url, calculate_quantity_discount, check_file_size, check_loan_eligibility, calculate_shipping_cost, grade_quiz, authenticate_user, get_weather_advisory


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

    def test_calculate_order_total_between_1_and_5(self):
        """
        Checks the total order calculation for a number of items between 1 and 5. 0% discount.
        """
        cart_items = [{"quantity": 5, "price": 30}]
        self.assertEqual(calculate_order_total(cart_items), 150)

    def test_calculate_order_total_between_6_and_10(self):
        """
        Checks the total order calculation for a number of items between 6 and 10. 5% discount.
        """
        cart_items = [{"quantity": 7, "price": 30}]
        self.assertAlmostEqual(calculate_order_total(cart_items), 199.5)

    def test_calculate_order_total_over_10(self):
        """
        Checks the total order calculation for a number of items over 10. 10% discount.
        """
        cart_items = [{"quantity": 12, "price": 30}]
        self.assertAlmostEqual(calculate_order_total(cart_items), 324.0)

    # 5
    def test_calculate_items_shipping_cost_standard_low(self):
        """
        Checks standard shipping cost for total weight <= 5.
        """
        items = [{"weight": 2}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_calculate_items_shipping_cost_standard_mid(self):
        """
        Checks standard shipping cost for total weight between 6 and 10.
        """
        items = [{"weight": 5}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_calculate_items_shipping_cost_standard_high(self):
        """
        Checks standard shipping cost for total weight > 10.
        """
        items = [{"weight": 6}, {"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_calculate_items_shipping_cost_express_low(self):
        """
        Checks express shipping cost for total weight <= 5.
        """
        items = [{"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_calculate_items_shipping_cost_express_mid(self):
        """
        Checks express shipping cost for total weight between 6 and 10.
        """
        items = [{"weight": 8}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_calculate_items_shipping_cost_express_high(self):
        """
        Checks express shipping cost for total weight > 10.
        """
        items = [{"weight": 15}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_calculate_items_shipping_cost_invalid_method(self):
        """
        Checks that an invalid shipping method raises a ValueError.
        """
        items = [{"weight": 5}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "drone")

    # 6
    def test_validate_login_success(self):
        """
        Checks successful login with valid lengths.
        """
        self.assertEqual(validate_login("user123", "password123"), "Login Successful")

    def test_validate_login_fail_username_short(self):
        """
        Checks login failure due to short username.
        """
        self.assertEqual(validate_login("usr", "password123"), "Login Failed")

    def test_validate_login_fail_password_short(self):
        """
        Checks login failure due to short password.
        """
        self.assertEqual(validate_login("user123", "pass"), "Login Failed")

    # 7
    def test_verify_age_eligible(self):
        """
        Checks age eligibility within range (18-65).
        """
        self.assertEqual(verify_age(30), "Eligible")

    def test_verify_age_not_eligible_young(self):
        """
        Checks age eligibility for someone under 18.
        """
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_verify_age_not_eligible_old(self):
        """
        Checks age eligibility for someone over 65.
        """
        self.assertEqual(verify_age(66), "Not Eligible")

    # 8
    def test_categorize_product_a(self):
        """
        Checks Category A (10-50).
        """
        self.assertEqual(categorize_product(30), "Category A")

    def test_categorize_product_b(self):
        """
        Checks Category B (51-100).
        """
        self.assertEqual(categorize_product(75), "Category B")

    def test_categorize_product_c(self):
        """
        Checks Category C (101-200).
        """
        self.assertEqual(categorize_product(150), "Category C")

    def test_categorize_product_d_high(self):
        """
        Checks Category D (over 200).
        """
        self.assertEqual(categorize_product(250), "Category D")

    def test_categorize_product_d_low(self):
        """
        Checks Category D (under 10).
        """
        self.assertEqual(categorize_product(5), "Category D")

    # 9
    def test_validate_email_valid(self):
        """
        Checks a valid email format.
        """
        self.assertEqual(validate_email("test@example.com"), "Valid Email")

    def test_validate_email_invalid_no_at(self):
        """
        Checks an email without an @ symbol.
        """
        self.assertEqual(validate_email("testexample.com"), "Invalid Email")

    def test_validate_email_invalid_no_dot(self):
        """
        Checks an email without a dot.
        """
        self.assertEqual(validate_email("test@examplecom"), "Invalid Email")

    def test_validate_email_invalid_too_short(self):
        """
        Checks an email that is too short.
        """
        self.assertEqual(validate_email("a@.c"), "Invalid Email")

    # 10
    def test_celsius_to_fahrenheit_valid(self):
        """
        Checks a valid conversion within bounds.
        """
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_invalid_high(self):
        """
        Checks an invalid temperature (too high).
        """
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")

    def test_celsius_to_fahrenheit_invalid_low(self):
        """
        Checks an invalid temperature (too low).
        """
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    # 11
    def test_validate_credit_card_valid(self):
        """
        Checks a valid card number.
        """
        self.assertEqual(validate_credit_card("123456789012345"), "Valid Card")

    def test_validate_credit_card_invalid_short(self):
        """
        Checks a card number that is too short.
        """
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_validate_credit_card_invalid_letters(self):
        """
        Checks a card number containing letters.
        """
        self.assertEqual(validate_credit_card("12345678901234a"), "Invalid Card")

    # 12
    def test_validate_date_valid(self):
        """
        Checks a valid date.
        """
        self.assertEqual(validate_date(2023, 10, 15), "Valid Date")

    def test_validate_date_invalid_year(self):
        """
        Checks an invalid year.
        """
        self.assertEqual(validate_date(1899, 10, 15), "Invalid Date")

    def test_validate_date_invalid_month(self):
        """
        Checks an invalid month.
        """
        self.assertEqual(validate_date(2023, 13, 15), "Invalid Date")

    def test_validate_date_invalid_day(self):
        """
        Checks an invalid day.
        """
        self.assertEqual(validate_date(2023, 10, 32), "Invalid Date")

    # 13
    def test_check_flight_eligibility_by_age(self):
        """
        Checks eligibility based on valid age.
        """
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_check_flight_eligibility_by_status(self):
        """
        Checks eligibility based on frequent flyer status despite age.
        """
        self.assertEqual(check_flight_eligibility(15, True), "Eligible to Book")

    def test_check_flight_eligibility_not_eligible(self):
        """
        Checks ineligibility due to age and no frequent flyer status.
        """
        self.assertEqual(check_flight_eligibility(15, False), "Not Eligible to Book")

    # 14
    def test_validate_url_valid_http(self):
        """
        Checks a valid http URL.
        """
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_validate_url_valid_https(self):
        """
        Checks a valid https URL.
        """
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_validate_url_invalid_start(self):
        """
        Checks an invalid URL starting incorrectly.
        """
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    def test_validate_url_invalid_length(self):
        """
        Checks an invalid URL that is too long.
        """
        long_url = "http://" + "a" * 250
        self.assertEqual(validate_url(long_url), "Invalid URL")

    # 15
    def test_calculate_quantity_discount_none(self):
        """
        Checks no discount for 1-5 items.
        """
        self.assertEqual(calculate_quantity_discount(3), "No Discount")

    def test_calculate_quantity_discount_five_percent(self):
        """
        Checks 5% discount for 6-10 items.
        """
        self.assertEqual(calculate_quantity_discount(8), "5% Discount")

    def test_calculate_quantity_discount_ten_percent(self):
        """
        Checks 10% discount for more than 10 items.
        """
        self.assertEqual(calculate_quantity_discount(15), "10% Discount")

    # 16
    def test_check_file_size_valid(self):
        """
        Checks valid file size.
        """
        self.assertEqual(check_file_size(500000), "Valid File Size")

    def test_check_file_size_invalid_large(self):
        """
        Checks invalid file size (too large).
        """
        self.assertEqual(check_file_size(2000000), "Invalid File Size")

    def test_check_file_size_invalid_negative(self):
        """
        Checks invalid file size (negative).
        """
        self.assertEqual(check_file_size(-10), "Invalid File Size")

    # 17
    def test_check_loan_eligibility_not_eligible(self):
        """
        Checks ineligibility due to low income.
        """
        self.assertEqual(check_loan_eligibility(25000, 800), "Not Eligible")

    def test_check_loan_eligibility_standard_mid_income(self):
        """
        Checks Standard Loan for mid income and good credit.
        """
        self.assertEqual(check_loan_eligibility(45000, 710), "Standard Loan")

    def test_check_loan_eligibility_secured_mid_income(self):
        """
        Checks Secured Loan for mid income and lower credit.
        """
        self.assertEqual(check_loan_eligibility(45000, 680), "Secured Loan")

    def test_check_loan_eligibility_premium_high_income(self):
        """
        Checks Premium Loan for high income and excellent credit.
        """
        self.assertEqual(check_loan_eligibility(80000, 760), "Premium Loan")

    def test_check_loan_eligibility_standard_high_income(self):
        """
        Checks Standard Loan for high income and lower credit.
        """
        self.assertEqual(check_loan_eligibility(80000, 700), "Standard Loan")

    # 18
    def test_calculate_shipping_cost_tier1(self):
        """
        Checks $5 shipping cost (weight<=1, dims<=10).
        """
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_calculate_shipping_cost_tier2(self):
        """
        Checks $10 shipping cost (1<weight<=5, dims 11-30).
        """
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 20), 10)

    def test_calculate_shipping_cost_default(self):
        """
        Checks default $20 shipping cost (outside other tiers).
        """
        self.assertEqual(calculate_shipping_cost(10, 50, 50, 50), 20)

    # 19
    def test_grade_quiz_pass(self):
        """
        Checks Pass condition (>=7 correct, <=2 incorrect).
        """
        self.assertEqual(grade_quiz(8, 1), "Pass")

    def test_grade_quiz_conditional_pass(self):
        """
        Checks Conditional Pass condition (>=5 correct, <=3 incorrect).
        """
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_grade_quiz_fail(self):
        """
        Checks Fail condition.
        """
        self.assertEqual(grade_quiz(4, 5), "Fail")

    # 20
    def test_authenticate_user_admin(self):
        """
        Checks Admin authentication.
        """
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_authenticate_user_normal(self):
        """
        Checks standard User authentication.
        """
        self.assertEqual(authenticate_user("user1", "password123"), "User")

    def test_authenticate_user_invalid(self):
        """
        Checks Invalid authentication.
        """
        self.assertEqual(authenticate_user("usr", "pass"), "Invalid")

    # 21
    def test_get_weather_advisory_hot(self):
        """
        Checks high temp/humidity advisory.
        """
        self.assertEqual(
            get_weather_advisory(35, 80),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_get_weather_advisory_cold(self):
        """
        Checks low temp advisory.
        """
        self.assertEqual(get_weather_advisory(-5, 50), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_normal(self):
        """
        Checks no specific advisory for normal weather.
        """
        self.assertEqual(get_weather_advisory(20, 40), "No Specific Advisory")
