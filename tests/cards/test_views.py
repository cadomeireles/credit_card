from .utils import generate_file


class TestUploadCardsView:
    '''
    Suite of tests to UploadCardsView.
    '''

    def test_view_status_code(self, client, url):
        '''
        Teste if status code is 200 (sucess).
        '''
        # Make request
        resp = client.get(url)

        assert resp.status_code == 200

    def test_view_template(self, client, url):
        '''
        Test if page has the necessary elements to work correctly.
        '''
        # Make request
        resp = client.get(url)
        content = str(resp.content, 'utf-8')

        # Must have the form supporting upload
        assert (
            'action="" method="POST" enctype="multipart/form-data"' in content
        )

        # Must have CSRF token
        assert "type='hidden' name='csrfmiddlewaretoken'" in content

        # Must have an input to file
        assert 'type="file" name="file"' in content

        # Must have the button to submit
        assert 'type="submit"' in content

    def test_view_required_field(self, client, url):
        '''
        Test if input file field is required.
        '''
        # Make request
        resp = client.post(url, {})
        content = str(resp.content, 'utf-8')

        assert 'This field is required.' in content

    def test_view_results(self, client, url):
        '''
        Test if result contains the numbers and if are valid or not.
        '''
        # Make request
        resp = client.post(url, {'file': generate_file()})
        content = str(resp.content, 'utf-8')

        data = {
            '4253625879615786': 'Yes',
            '4424424424442444': 'Yes',
            '5122-2368-7954-3214': 'Yes',
            '4123456789123456': 'Yes',
            '5123-4567-8912-3456': 'Yes',
            '4123356789123456': 'Yes',
            '42536258796157867': 'No',
            '4424444424442444': 'No',
            '5122-2368-7954 - 3214': 'No',
            '44244x4424442444': 'No',
            '0525362587961578': 'No',
            '61234-567-8912-3456': 'No',
            '5133-3367-8912-3456': 'No',
            '5123 - 3567 - 8912 - 3456': 'No',
        }

        for number, is_valid in data.items():
            assert f'<td>{number}</td><td>{is_valid}</td>' in content
