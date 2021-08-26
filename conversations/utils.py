import requests

def get_request(search_url, headers, params = None):
    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response
