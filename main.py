import requests
import os


def load_image(url, directory, filename):
    response = requests.get(url)
    os.makedirs(directory, exist_ok=True)
    path = '/'.join([directory, filename])
    with open(path, 'wb') as file:
        file.write(response.content)
        file.close()


def return_extension(url):
    return url.split('/')[-1].split('.')[-1]


def fetch_spacex_last_launch(directory_for_loading):
    url_space_x = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url_space_x)
    if response.ok:
        links = response.json()['links']['flickr_images']
        for i, link in enumerate(links):
            print('Загружено {} фотографий из {}'.format(i + 1, len(links)))
            filename = 'space_x_{}.jpg'.format(i)
            load_image(link, directory_for_loading, filename)


def fetch_hubble_images(image_id, directory):
    url_hubble_api = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    response = requests.get(url_hubble_api)
    if response.ok:
        link_to_image = response.json()['image_files'][-1]['file_url']
        file_extension = return_extension(link_to_image)
        load_image(link_to_image, directory, '{}.{}'.format(image_id, file_extension))


if __name__ == '__main__':
    directory_for_images = 'images'
    # fetch_spacex_last_launch(directory_for_images)
    fetch_hubble_images(1, directory_for_images)
