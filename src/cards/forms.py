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

        # Check if the first line is corresponds to quantity of numbers
        if quantity != len(file.readlines()):
            raise forms.ValidationError(
                _('The first line must corresponds to quantity of numbers!')
            )

        # Set the cursor to begin of file
        file.seek(0)

        # Consume the first line to doesn't appear on results
        file.readline()

        return file
