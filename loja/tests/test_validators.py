"""
Tests for the centralized validation utilities.
"""
from django.test import TestCase
from ..utils.validators import (
    validate_phone_number,
    validate_price,
    validate_email,
    validate_name,
    validate_password,
    validate_bid_amount,
    validate_city
)


class ValidatorTests(TestCase):
    def test_validate_phone_number(self):
        """Test phone number validation."""
        # Valid phone numbers
        self.assertEqual(validate_phone_number("912345678"), (True, None))
        self.assertEqual(validate_phone_number("923456789"), (True, None))

        # Invalid phone numbers
        self.assertEqual(validate_phone_number(""), (False, "Phone number is required"))
        self.assertEqual(validate_phone_number("812345678"), (False, "Phone number must start with 9 and have exactly 9 digits"))
        self.assertEqual(validate_phone_number("91234567"), (False, "Phone number must start with 9 and have exactly 9 digits"))
        self.assertEqual(validate_phone_number("9123456789"), (False, "Phone number must start with 9 and have exactly 9 digits"))
        self.assertEqual(validate_phone_number("abc"), (False, "Phone number must start with 9 and have exactly 9 digits"))

    def test_validate_price(self):
        """Test price validation."""
        # Valid prices
        price, error = validate_price("10.50")
        self.assertIsNotNone(price)
        self.assertIsNone(error)
        self.assertEqual(float(price), 10.50)

        price, error = validate_price("10,50")
        self.assertIsNotNone(price)
        self.assertIsNone(error)
        self.assertEqual(float(price), 10.50)

        price, error = validate_price("0.01")
        self.assertIsNotNone(price)
        self.assertIsNone(error)

        # Invalid prices
        price, error = validate_price("")
        self.assertIsNone(price)
        self.assertEqual(error, "Price is required")

        price, error = validate_price("abc")
        self.assertIsNone(price)
        self.assertEqual(error, "Invalid price format. Use numbers with up to 2 decimal places")

        price, error = validate_price("-10.50")
        self.assertIsNone(price)
        self.assertEqual(error, "Price must be positive")

        price, error = validate_price("100000.00")
        self.assertIsNone(price)
        self.assertEqual(error, "Price cannot exceed 99999.99")

    def test_validate_email(self):
        """Test email validation."""
        # Valid emails
        self.assertEqual(validate_email("test@example.com"), (True, None))
        self.assertEqual(validate_email("user.name@domain.co.uk"), (True, None))

        # Invalid emails
        self.assertEqual(validate_email(""), (False, "Email is required"))
        self.assertEqual(validate_email("test"), (False, "Email must be at least 5 characters"))
        self.assertEqual(validate_email("a@b.c"), (True, None))  # This is actually valid
        self.assertEqual(validate_email("test@"), (False, "Invalid email format"))
        self.assertEqual(validate_email("@example.com"), (False, "Invalid email format"))

    def test_validate_name(self):
        """Test name validation."""
        # Valid names
        self.assertEqual(validate_name("John", "Name"), (True, None))
        self.assertEqual(validate_name("Maria João", "Name"), (True, None))
        self.assertEqual(validate_name("O'Connor", "Name"), (True, None))

        # Invalid names
        self.assertEqual(validate_name("", "Name"), (False, "Name is required"))
        self.assertEqual(validate_name("A", "Name"), (False, "Name must be at least 2 characters"))
        self.assertEqual(validate_name("A" * 51, "Name"), (False, "Name cannot exceed 50 characters"))
        self.assertEqual(validate_name("John123", "Name"), (False, "Name can only contain letters, spaces, hyphens, and apostrophes"))

    def test_validate_password(self):
        """Test password validation."""
        # Valid passwords
        self.assertEqual(validate_password("Password123"), (True, None))
        self.assertEqual(validate_password("12345678Ab"), (True, None))

        # Invalid passwords
        self.assertEqual(validate_password(""), (False, "Password is required"))
        self.assertEqual(validate_password("short"), (False, "Password must be at least 8 characters"))
        self.assertEqual(validate_password("nouppercase123"), (False, "Password must contain at least one letter"))
        self.assertEqual(validate_password("NOLOWERCASE123"), (False, "Password must contain at least one letter"))
        self.assertEqual(validate_password("NoNumbersHere"), (False, "Password must contain at least one number"))

    def test_validate_bid_amount(self):
        """Test bid amount validation."""
        # Valid bids
        self.assertEqual(validate_bid_amount(20.50, 10.00), (True, None))
        self.assertEqual(validate_bid_amount(10.01, 10.00), (True, None))

        # Invalid bids
        self.assertEqual(validate_bid_amount(0, 10.00), (False, "Bid amount must be positive"))
        self.assertEqual(validate_bid_amount(-5, 10.00), (False, "Bid amount must be positive"))
        self.assertEqual(validate_bid_amount(10.00, 10.00), (False, "Bid must be higher than current maximum (10.00)"))
        self.assertEqual(validate_bid_amount(9.99, 10.00), (False, "Bid must be higher than current maximum (10.00)"))
        self.assertEqual(validate_bid_amount(10.005, 10.00), (False, "Minimum bid increment is 0.01"))

    def test_validate_city(self):
        """Test city validation."""
        valid_choices = [
            ('lisboa', 'Lisboa'),
            ('porto', 'Porto'),
            ('coimbra', 'Coimbra')
        ]

        # Valid cities
        self.assertEqual(validate_city('lisboa', valid_choices), (True, None))
        self.assertEqual(validate_city('porto', valid_choices), (True, None))

        # Invalid cities
        self.assertEqual(validate_city('', valid_choices), (False, "City is required"))
        self.assertEqual(validate_city('invalid', valid_choices), (False, "Invalid city selection"))