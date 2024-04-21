import requests


api_url = 'http://ip-api.com/json/'


def get_whois(url):
    response = requests.get(api_url+url)
    return response.json()
