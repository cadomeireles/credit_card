import pytest

from src.cards.utils import check_is_valid, has_repeated


class TestUtilsFunctions:
    '''
    Suite of tests to utils functions
    '''
    @pytest.mark.parametrize('number, repeated', [
        ('6423074376429899', False),
        ('6423074376429999', True),
        ('5875-1065-7423-0184', False),
        ('5875-1066-6663-0184', True),
    ])
    def test_has_repeated(self, number, repeated):
        '''
        Test if function 'has_repeated' can identify a card number with
        4 or more consecutive repeated digits.
        '''
        assert has_repeated(number) == repeated

    @pytest.mark.parametrize('number, is_valid', [
        ('4423074376429899', True),
        ('5423107437642989', True),
        ('6423107437642989', True),
        ('0423107437642989', False),
        ('7423107437642989', False),
    ])
    def test_check_is_valid_first_number(self, number, is_valid):
        '''
        Test if function 'check_is_valid' can identify if card number
        starts with a valid number (4, 5 or 6).
        '''
        assert check_is_valid(number) == is_valid

    @pytest.mark.parametrize('number, is_valid', [
        ('6423074376429899', True),
        ('44231074376429899', False),
        ('5875-1065-7423-0184', True),
        ('5875-1065-74023-0184', False),
    ])
    def test_check_is_valid_length(self, number, is_valid):
        '''
        Test if function 'check_is_valid' can identify if card number
        has more than 16 digits.
        '''
        assert check_is_valid(number) == is_valid

    @pytest.mark.parametrize('number, is_valid', [
        ('6423074376429899', True),
        ('44231074a76429899', False),
        ('5875-1065-7423-0184', True),
        ('5875-106 -74023-0184', False),
    ])
    def test_check_is_valid_digits(self, number, is_valid):
        '''
        Test if function 'check_is_valid' can identify if card number
        has only digits.
        '''
        assert check_is_valid(number) == is_valid

    @pytest.mark.parametrize('number, is_valid', [
        ('6420074376329849', True),
        ('6420 0743 7632 9849', False),
        ('5875-1065-7423-0184', True),
        ('5875_1065_74023_0184', False),
    ])
    def test_check_is_valid_separator(self, number, is_valid):
        '''
        Test if function 'check_is_valid' can identify if card number
        has a invalid separator (not a hyphen).
        '''
        assert check_is_valid(number) == is_valid

    @pytest.mark.parametrize('number, is_valid', [
        ('5875-1065-7423-0184', True),
        ('5875-1065-74230-184', False),
        ('5875-1065-7423018-4', False),
    ])
    def test_check_is_valid_group(self, number, is_valid):
        '''
        Test if function 'check_is_valid' can identify if card number
        has a group without 4 digits.
        '''
        assert check_is_valid(number) == is_valid
