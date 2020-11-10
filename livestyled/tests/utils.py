import os


def configure_mock_responses(requests_mock, mock_responses, fixtures_dir, content_type):
    for method, url, fixture, status_code in mock_responses:
        data = open(os.path.join(fixtures_dir, fixture), 'r').read()
        if method == 'GET':
            requests_mock.get(url, text=data, headers={'Content-Type': content_type}, status_code=status_code)
        elif method == 'POST':
            requests_mock.post(url, text=data, headers={'Content-Type': content_type}, status_code=status_code)
        elif method == 'PATCH':
            requests_mock.patch(url, text=data, headers={'Content-Type': content_type}, status_code=status_code)
