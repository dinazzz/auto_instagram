from instabot import Bot
from os.path import join as join_path
from os import listdir


def get_pictures_from_directory(directory):
    pic_extensions = ('.jpg', '.jpeg', '.tiff', '.tif', '.png')
    return [join_path(directory, pic) for pic in listdir(directory) if pic.endswith(pic_extensions)]


def upload_to_insta(login, password, directory):
    pictures = get_pictures_from_directory(directory)
    bot = Bot()
    bot.login(username=login, password=password)
    unsuccess = []
    for i, pic in enumerate(pictures):
        print(f'\n{i+1}/{len(pictures)} Загружаем изображение {pic}')
        bot.upload_photo(pic, caption=f'Picture {i}')
        if bot.api.last_response.status_code != 200:
            unsuccess.append(pic)
    if unsuccess:
        print('\nНе удалось загрузить изображения:', *unsuccess, sep='\n')