import requests


def fetch_spacex_last_launch():
    url_space_x = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url_space_x)
    response.raise_for_status()
    return response.json()['links']['flickr_images']