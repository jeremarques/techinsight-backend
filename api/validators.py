import re

def validate_username(value):
    invalid = re.search(r'[^\w._]+', value)
    if invalid:
        return False
    else: 
        return True

