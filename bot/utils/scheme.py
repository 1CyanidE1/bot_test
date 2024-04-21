import requests


def ensure_scheme(url):
    if not url.startswith(('http://', 'https://')):
        try:
            requests.get('https://' + url, timeout=10)
            return 'https://' + url
        except (requests.exceptions.RequestException, requests.exceptions.Timeout):
            try:
                requests.get('http://' + url, timeout=10)
                return 'http://' + url
            except (requests.exceptions.RequestException, requests.exceptions.Timeout):
                return False
    return url


def get_title(url):
    response = requests.get(url)
    start_title = response.text.find('<title>') + len('<title>')
    end_title = response.text.find('</title>')

    return response.text[start_title:end_title]
