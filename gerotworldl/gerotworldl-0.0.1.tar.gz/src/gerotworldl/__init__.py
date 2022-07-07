import requests


def customrequest(url):
    try:
        connection = requests.get(url)
    except requests.exceptions.ConnectionError:
        return None
    return connection.content
