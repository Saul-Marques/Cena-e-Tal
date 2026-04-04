"""
Centralized validation utilities for consistent data validation across the project.
"""
import re
from decimal import Decimal, InvalidOperation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone_number(phone):
    """
    Validate Portuguese phone number format.
    Must start with 9 and have exactly 9 digits.
    """
    if not phone:
        return False, "Phone number is required"

    if not re.fullmatch(r"9\d{8}", str(phone)):
        return False, "Phone number must start with 9 and have exactly 9 digits"

    return True, None


def validate_price(price_str):
    """
    Validate and convert price string to Decimal.
    Handles both comma and dot decimal separators.
    """
    if not price_str:
        return None, "Price is required"

    try:
        # Replace comma with dot for decimal separator
        normalized = str(price_str).replace(",", ".")
        price = Decimal(normalized)

        if price <= 0:
            return None, "Price must be positive"

        if price > Decimal("99999.99"):
            return None, "Price cannot exceed 99999.99"

        return price, None

    except InvalidOperation:
        return None, "Invalid price format. Use numbers with up to 2 decimal places"


def validate_email(email):
    """
    Basic email validation.
    """
    if not email:
        return False, "Email is required"

    if len(email) < 5:
        return False, "Email must be at least 5 characters"

    # Basic email format check
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        return False, "Invalid email format"

    return True, None


def validate_name(name, field_name="Name"):
    """
    Validate names (first name, last name, etc.).
    """
    if not name:
        return False, f"{field_name} is required"

    if len(name) < 2:
        return False, f"{field_name} must be at least 2 characters"

    if len(name) > 50:
        return False, f"{field_name} cannot exceed 50 characters"

    # Allow letters, spaces, hyphens, and apostrophes
    if not re.match(r"^[a-zA-ZÀ-ÿ\s'-]+$", name):
        return False, f"{field_name} can only contain letters, spaces, hyphens, and apostrophes"

    return True, None


def validate_password(password):
    """
    Validate password strength.
    """
    if not password:
        return False, "Password is required"

    if len(password) < 8:
        return False, "Password must be at least 8 characters"

    # Check for at least one digit
    if not re.search(r"\d", password):
        return False, "Password must contain at least one number"

    # Check for at least one letter
    if not re.search(r"[a-zA-Z]", password):
        return False, "Password must contain at least one letter"

    return True, None


def validate_bid_amount(amount, current_max_bid, min_increment=0.01):
    """
    Validate bid amount for auctions.
    """
    try:
        bid_amount = Decimal(str(amount))

        if bid_amount <= 0:
            return False, "Bid amount must be positive"

        if bid_amount <= current_max_bid:
            return False, f"Bid must be higher than current maximum ({current_max_bid})"

        if bid_amount - current_max_bid < Decimal(str(min_increment)):
            return False, f"Minimum bid increment is {min_increment}"

        return True, None

    except (InvalidOperation, TypeError):
        return False, "Invalid bid amount"


def validate_city(city_code, valid_choices):
    """
    Validate city against valid choices.
    """
    if not city_code:
        return False, "City is required"

    valid_codes = [choice[0] for choice in valid_choices]
    if city_code not in valid_codes:
        return False, "Invalid city selection"

    return True, None