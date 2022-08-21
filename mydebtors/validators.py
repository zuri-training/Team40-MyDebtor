from django.core.exceptions import ValidationError


def validate_file_size(file):
    max_size = 1000

    if file.size > max_size * 1024:
        raise ValidationError(f"File size cannot be larger than {max_size}MB")
    
    return file