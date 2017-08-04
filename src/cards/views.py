from django.shortcuts import render
from django.views.generic import FormView

from .forms import UploadCardsForm
from .utils import check_is_valid


class UploadCardsView(FormView):
    '''
    Processes the card numbers and return the result
    '''
    form_class = UploadCardsForm
    template_name = 'cards/upload.html'

    def form_valid(self, form, **kwargs):
        '''
        Checks each card number and return a dict with the numbers
        and if are valid or not
        '''
        file = self.request.FILES.get('file')
        cards = {}

        # Read file lines
        for line in file.readlines():
            line = str(line, 'utf-8').replace('\n', '')
            # Call check_is_valid to verify
            cards[line] = check_is_valid(line)

        # Return the results
        context = {
            'form': form,
            'cards': cards,
        }

        return render(self.request, 'cards/upload.html', context)
