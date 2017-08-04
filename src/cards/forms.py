import re

from django import forms
from django.utils.translation import ugettext_lazy as _


class UploadCardsForm(forms.Form):
    '''
    Form used to receive a text file with card numbers.
    '''
    file = forms.FileField()

    def clean_file(self):
        '''
        Verifies if the first line of file have a valid number.
        '''
        file = self.cleaned_data['file']

        # Read first line
        quantity = str(file.readline(), 'utf-8')

        # The first line must be a number
        if not re.match(r'\d+\n', quantity):
            raise forms.ValidationError(
                _('The first line of file must be a valid number!')
            )

        quantity = int(quantity)

        # The number must be between 1 and 99
        if quantity < 1 or quantity > 99:
            raise forms.ValidationError(
                _('The first line must have a number between 1 and 99!')
            )

        return file
