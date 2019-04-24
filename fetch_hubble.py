import requests


def fetch_hubble_images(image_id):
    url_hubble_api = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    response = requests.get(url_hubble_api)
    response.raise_for_status()
    link_to_image = response.json()['image_files'][-1]['file_url']
    return link_to_image


def get_hubble_image_collection(collection_name):
    url_hubble_api = 'http://hubblesite.org/api/v3/images/{}'.format(collection_name)
    response = requests.get(url_hubble_api)
    response.raise_for_status()
    return [fetch_hubble_images(image['id']) for image in response.json()]

