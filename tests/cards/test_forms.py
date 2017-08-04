from .utils import generate_file


class TestUploadCardsForm:
    '''
    Suite of tests to UploadCardsForm.
    '''

    def test_first_line_valid(self, client, url):
        '''
        The first line must have an number.
        '''
        # Make request
        resp = client.post(url, {'file': generate_file(qt_lines='A')})
        content = str(resp.content, 'utf-8')

        assert 'The first line of file must be a valid number!' in content

    def test_first_line_range(self, client, url):
        '''
        The number must be between 1 and 99.
        '''
        # Make request
        resp = client.post(url, {'file': generate_file(qt_lines=0)})
        content = str(resp.content, 'utf-8')

        # Check inferior limit
        assert (
            'The first line must have a number between 1 and 99!' in content
        )

        # Make request
        resp = client.post(url, {'file': generate_file(qt_lines=100)})
        content = str(resp.content, 'utf-8')

        # Check superior limit
        assert (
            'The first line must have a number between 1 and 99!' in content
        )

    def test_first_line_quantity(self, client, url):
        '''
        The first line must correspond to the quantity of numbers on file.
        '''
        # Make request
        resp = client.post(url, {'file': generate_file(qt_lines=15)})
        content = str(resp.content, 'utf-8')

        assert (
            'The first line must corresponds to quantity of numbers!'
            in content
        )
