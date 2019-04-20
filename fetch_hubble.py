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


def return_extension(url):
    return url.split('/')[-1].split('.')[-1]


def fetch_hubble_images(image_id, directory):
    url_hubble_api = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    response = requests.get(url_hubble_api)
    if response.ok:
        link_to_image = response.json()['image_files'][-1]['file_url']
        file_extension = return_extension(link_to_image)
        load_image(link_to_image, directory, '{}.{}'.format(image_id, file_extension))


def get_hubble_image_collection(collection_name, directory):
    url_hubble_api = 'http://hubblesite.org/api/v3/images/{}'.format(collection_name)
    response = requests.get(url_hubble_api)
    if response.ok:
        for i, image in enumerate(response.json()):
            print('Загружается {} фотография из {}'.format(i + 1, len(response.json())))
            fetch_hubble_images(image['id'], directory)