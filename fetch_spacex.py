import requests

from os import makedirs
from os.path import join as join_path


def load_image(url, directory, filename):
    response = requests.get(url)
    makedirs(directory, exist_ok=True)
    path = join_path(directory, filename)
    with open(path, 'wb') as file:
        file.write(response.content)
        file.close()


def fetch_spacex_last_launch(directory_for_loading):
    url_space_x = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url_space_x)
    if response.ok:
        links = response.json()['links']['flickr_images']
        for i, link in enumerate(links):
            print('Загружено {} фотографий из {}'.format(i + 1, len(links)))
            filename = 'space_x_{}.jpg'.format(i)
            load_image(link, directory_for_loading, filename)