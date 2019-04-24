import requests
import argparse


from dotenv import load_dotenv
from os import getenv, makedirs
from os.path import join as join_path
from fetch_hubble import get_hubble_image_collection
from fetch_spacex import fetch_spacex_last_launch
from upload_to_instagram import upload_to_insta


def download_image(url, directory, filename):
    response = requests.get(url)
    response.raise_for_status()
    makedirs(directory, exist_ok=True)
    path = join_path(directory, filename)
    with open(path, 'wb') as file:
        file.write(response.content)


def return_extension(url):
    return url.split('/')[-1].split('.')[-1]


def download_collection(image_collection, directory, mask_name):
    images_count = len(image_collection)
    if image_collection:
        for i, image_url in enumerate(image_collection):
            file_extension = return_extension(image_url)
            filename = f'{mask_name}_{i}.{file_extension}'
            print(f'Downloading image {i}/{images_count}...')
            download_image(image_url, directory, filename)
    else:
        raise IndexError


def parse_arguments():
    parser = argparse.ArgumentParser(description='Auto-Instagram Utility',
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('directory', help='Directory for downloading or uploading images')
    parser.add_argument('-c', '--collection', help='Name of needed Hubble images collection')
    parser.add_argument('-u', '--upload', action='store_true', help='Need to upload to your Instagram account')
    parser.add_argument('-x', '--spacex', action='store_true', help='Need to download last Space X launch')
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = parse_arguments()
    load_dotenv()
    insta_login = getenv('LOGIN')
    insta_password = getenv('PASSWORD')
    directory_for_images = args.directory
    try:
        if args.spacex:
            space_x_last_images = fetch_spacex_last_launch()
            print('Start downloading last Space X launch photos')
            download_collection(space_x_last_images, directory_for_images, 'space_X')

        if args.collection:
            collection = args.collection
            hubble_collection = get_hubble_image_collection(collection)
            print(f'Start downloading {collection} photos from Hubble')
            download_collection(hubble_collection, directory_for_images, 'from_hubble')

        if args.upload:
            print(f'Start uploading images from {directory_for_images} to Instagram {insta_login}')
            result = upload_to_insta(insta_login, insta_password, directory_for_images)
            if result:
                print('\nUploading of the following images is unsuccessful:', *result, sep='\n')

    except requests.exceptions.HTTPError as http_error:
        print('The request failed', http_error)
    except IndexError as ie:
        print('Probably there is no such collection')
