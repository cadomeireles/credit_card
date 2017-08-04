import re


def has_repeated(number):
    '''
    Verifies is number doesn't have 4 or more consecutive repeated digits.
    '''
    # Remove separator
    number = number.replace('-', '')

    for counter, value in enumerate(number):
        # if counter get on index 13 isn't possible have 4 or more consecutive
        # repeated digits yet.
        if counter == 13:
            return False

        # Check if for next four chars are equal
        sub = number[counter:counter + 4]
        if sub.count(value) > 3:
            return True


def check_is_valid(number):
    '''
    Verifies is number:

    [by regex]
    - starts with 4, 5 or 6.
    - contains exactly 16 digits.
    - only consists of digits (0-9).
    - have digits in groups of 4, together or separated by one hyphen.

    [by has_repeated()]
    - doesn't have 4 or more consecutive repeated digits.
    '''
    regex = r'^([456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4})$'

    if re.match(regex, number) and not has_repeated(number):
        return True
    else:
        return False
