from dotenv import load_dotenv
from os import getenv
from fetch_hubble import get_hubble_image_collection
from fetch_spacex import fetch_spacex_last_launch
from upload_to_instagram import upload_to_insta


if __name__ == '__main__':
    load_dotenv()
    insta_login = getenv('LOGIN')
    insta_password = getenv('PASSWORD')
    directory_for_images = 'images'

    fetch_spacex_last_launch(directory_for_images)
    get_hubble_image_collection('spacecraft', directory_for_images)
    upload_to_insta(insta_login, insta_password, directory_for_images)
