import re
from django.core.exceptions import ValidationError
      
def validate_only_contains_chars_and_space(value):
    if re.search(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ ]', value):
        raise ValidationError('El valor solo puede contener letras y espacios')
    
def validate_numbers_greater_than_zero(value):
    if value <= 0:
        raise ValidationError('El valor debe ser un numero mayor a 0')
