"""
File validation utilities for secure file uploads.
"""
import os
import imghdr
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .sanitizers import sanitize_filename


def validate_image_file(file, max_size_mb=5, allowed_types=None):
    """
    Validate image file uploads.

    Args:
        file: Django File object
        max_size_mb: Maximum file size in MB
        allowed_types: List of allowed image types (default: jpeg, png, gif, webp)

    Returns:
        tuple: (is_valid, error_message)
    """
    if allowed_types is None:
        allowed_types = ['jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp']

    # Check file exists
    if not file:
        return False, "No file provided"

    # Check file size
    max_size_bytes = max_size_mb * 1024 * 1024
    if file.size > max_size_bytes:
        return False, f"File too large. Maximum size is {max_size_mb}MB"

    # Check file name
    original_name = file.name
    sanitized_name = sanitize_filename(original_name)
    if sanitized_name != original_name:
        return False, "Invalid filename"

    # Check content type
    if not file.content_type.startswith('image/'):
        return False, "File is not an image"

    # Check file extension
    ext = os.path.splitext(original_name)[1].lower()
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    if ext not in allowed_extensions:
        return False, f"Unsupported file format. Allowed: {', '.join(allowed_extensions)}"

    # Verify image signature
    try:
        # Reset file pointer to beginning
        if hasattr(file, 'seekable') and file.seekable():
            file.seek(0)

        image_type = imghdr.what(file)
        if image_type not in allowed_types:
            return False, f"Invalid image signature. Detected: {image_type}"

        # Reset file pointer again for further processing
        if hasattr(file, 'seekable') and file.seekable():
            file.seek(0)

    except Exception as e:
        return False, f"Error validating image: {str(e)}"

    return True, None


def validate_multiple_images(files, max_size_mb=5, max_count=10):
    """
    Validate multiple image files.

    Args:
        files: List of Django File objects
        max_size_mb: Maximum file size per image in MB
        max_count: Maximum number of images allowed

    Returns:
        tuple: (is_valid, error_message, valid_files)
    """
    if not files:
        return True, None, []

    if len(files) > max_count:
        return False, f"Too many files. Maximum is {max_count}", []

    valid_files = []
    for i, file in enumerate(files):
        is_valid, error = validate_image_file(file, max_size_mb)
        if not is_valid:
            return False, f"File {i+1}: {error}", []

        valid_files.append(file)

    return True, None, valid_files


def get_safe_filename(file, prefix="", suffix=""):
    """
    Generate a safe filename for storage.

    Args:
        file: Django File object
        prefix: Optional prefix for filename
        suffix: Optional suffix for filename

    Returns:
        Safe filename
    """
    original_name = file.name
    sanitized = sanitize_filename(original_name)

    # Add prefix and suffix if provided
    if prefix:
        sanitized = f"{prefix}_{sanitized}"
    if suffix:
        name, ext = os.path.splitext(sanitized)
        sanitized = f"{name}{suffix}{ext}"

    return sanitized


def validate_file_extension(filename, allowed_extensions):
    """
    Validate file extension against allowed list.

    Args:
        filename: Name of the file
        allowed_extensions: List of allowed extensions (with dots)

    Returns:
        bool: True if extension is allowed
    """
    ext = os.path.splitext(filename)[1].lower()
    return ext in allowed_extensions


def get_file_size_mb(file):
    """
    Get file size in MB.

    Args:
        file: Django File object

    Returns:
        float: File size in MB
    """
    return file.size / (1024 * 1024)