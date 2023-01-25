import re

def validate_password(value):
    password = value
    min_length = 8
    special_characters = " !@#$%^&*()-+?_=,<>/ "
    r= "1234567890"
    errors = ''
    if len(password) < min_length:
        errors += 'Password must be at least 8 characters long. '
    if not any(character.isupper() for character in password):
        errors += 'Password should contain at least one uppercase character.'
    if not any(character.islower() for character in password):
        errors += 'Password should contain at least one lowercase character.'
    if not any (character in special_characters for character in password):
        errors += 'Password should contain at least one special characters.'
    if not any (character in r for character in password):
        errors += 'Password should contain at least one integer.'
    if errors:
        raise ValueError(errors)  
    return value


def validate_mobile(value):
    n=value
    r=re.fullmatch('[6-9][0-9]{9}',n)
    errors = '' 
    if r is None:
        errors += 'Not a valid number'
    if errors:
        raise ValueError(errors)
    return value


def merge(a , b):
    return(a.update(b))
