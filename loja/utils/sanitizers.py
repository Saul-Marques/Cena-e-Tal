"""
Input sanitization utilities to prevent XSS and other injection attacks.
"""
from django.utils.html import escape
import bleach
import re
import os


def sanitize_text(text, allow_basic_html=False):
    """
    Sanitize text input to prevent XSS attacks.

    Args:
        text: The text to sanitize
        allow_basic_html: If True, allows basic HTML tags (b, i, u, p, br)

    Returns:
        Sanitized text
    """
    if not text:
        return ""

    # Always escape first for safety
    escaped = escape(text)

    if allow_basic_html:
        # Allow only very basic formatting tags
        allowed_tags = ['b', 'i', 'u', 'em', 'strong', 'p', 'br', 'span']
        allowed_attributes = {
            'span': ['class', 'style'],
            'p': ['class', 'style']
        }

        # Clean with bleach
        cleaned = bleach.clean(
            escaped,
            tags=allowed_tags,
            attributes=allowed_attributes,
            strip=True
        )
        return cleaned

    return escaped


def sanitize_filename(filename):
    """
    Sanitize filename to prevent path traversal and other attacks.

    Args:
        filename: Original filename

    Returns:
        Sanitized filename
    """
    if not filename:
        return ""

    # Remove directory path components
    basename = os.path.basename(filename)

    # Replace spaces with underscores
    basename = basename.replace(" ", "_")

    # Remove any non-alphanumeric characters except dots, hyphens, and underscores
    basename = re.sub(r'[^a-zA-Z0-9._-]', '', basename)

    # Limit length
    if len(basename) > 255:
        name, ext = os.path.splitext(basename)
        basename = name[:255 - len(ext)] + ext

    return basename


def sanitize_user_input(data_dict, fields_to_sanitize=None, allow_html_fields=None):
    """
    Sanitize multiple fields in a dictionary of user input.

    Args:
        data_dict: Dictionary containing user input
        fields_to_sanitize: List of field names to sanitize (if None, sanitize all string fields)
        allow_html_fields: List of field names where basic HTML is allowed

    Returns:
        Dictionary with sanitized values
    """
    if not data_dict:
        return {}

    if allow_html_fields is None:
        allow_html_fields = []

    if fields_to_sanitize is None:
        fields_to_sanitize = list(data_dict.keys())

    sanitized = {}

    for field, value in data_dict.items():
        if field not in fields_to_sanitize:
            sanitized[field] = value
            continue

        if isinstance(value, str):
            allow_html = field in allow_html_fields
            sanitized[field] = sanitize_text(value, allow_html)
        else:
            sanitized[field] = value

    return sanitized


def sanitize_chat_message(message):
    """
    Specialized sanitization for chat messages.
    Allows basic formatting but prevents XSS.
    """
    if not message:
        return ""

    # Remove any script tags and event handlers
    message = re.sub(r'<script.*?>.*?</script>', '', message, flags=re.IGNORECASE | re.DOTALL)
    message = re.sub(r'on\w+=".*?"', '', message)
    message = re.sub(r"on\w+='.*?'", '', message)

    # Allow basic formatting
    allowed_tags = ['b', 'i', 'u', 'em', 'strong', 'br', 'code', 'pre']
    allowed_attributes = {}

    cleaned = bleach.clean(
        message,
        tags=allowed_tags,
        attributes=allowed_attributes,
        strip=True
    )

    # Limit length
    if len(cleaned) > 1000:
        cleaned = cleaned[:1000] + "..."

    return cleaned


def sanitize_product_description(description):
    """
    Sanitize product descriptions.
    Allows slightly more HTML than chat messages.
    """
    if not description:
        return ""

    allowed_tags = ['b', 'i', 'u', 'em', 'strong', 'br', 'p', 'ul', 'ol', 'li', 'h3', 'h4']
    allowed_attributes = {
        'p': ['class'],
        'span': ['class']
    }

    cleaned = bleach.clean(
        description,
        tags=allowed_tags,
        attributes=allowed_attributes,
        strip=True
    )

    # Limit length
    if len(cleaned) > 5000:
        cleaned = cleaned[:5000] + "..."

    return cleaned