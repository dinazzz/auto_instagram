# Космический Инстаграм

С помощью этой утилиты вы сможете автоматизировать скачивание фото на космическую тематику и загрузку их в свой
Instagram-аккаунт.

Модуль `fetch_hubble.py` использует API телескопа Hubble для загрузки фотографии (функция `fetch_hubble_images`, 
 в качестве аргумента принимает `id` фотографии) либо коллекции фотографий (функция `get_hubble_image_collection`,
 в качестве аргумента принимает название коллеции фотографий). Также в качестве второго аргумента указывается директория, 
 в которую будут загружены фото:
 ```python
collection = 'wallpaper'
directory_for_images  = 'test_directory'
get_hubble_image_collection(collection, directory_for_images)
```
Результат работы `get_hubble_image_collection`:
```python
Загружено 1 фотографий из 2
Загружено 2 фотографий из 2
```
 
Модуль `fetch_spacex.py` использует API телескопа проекта Space X для загрузки фотографий с последнего запуска ракеты.
Единственный аргумент - директория для загрузки:
```python
directory_for_images  = 'test_directory'
fetch_spacex_last_launch(directory_for_images)
```
Результат работы `fetch_spacex.py` аналогичный:
```python
Загружено 1 фотографий из 2
Загружено 2 фотографий из 2
```
Модуль `upload_to_instagram.py` заливает все изображения из указанной в качестве аргумента директории в аккаунт Instagram:
```python
load_dotenv()
insta_login = getenv('LOGIN')
insta_password = getenv('PASSWORD')
directory_for_images = 'test_directory'
upload_to_insta(insta_login, insta_password, directory_for_images)
```
Результат работы `upload_to_instagram.py`:
```python
2019-04-23 21:43:16,483 - INFO - Instabot Started
2019-04-23 21:43:18,251 - INFO - Logged-in successfully as 'dinar_dvmn'!

1/10 Загружаем изображение test_directory/space_x_6.jpg
Analizing `test_directory/space_x_6.jpg`
FOUND w:2000, h:3000, ratio=0.6666666666666666
Vertical image
Cropping image
Resizing image
Saving new image w:864 h:1080 to `test_directory/space_x_6.jpg.CONVERTED.jpg`
FOUND: w:864 h:1080 r:0.8
2019-04-23 21:43:23,673 - INFO - Photo 'test_directory/space_x_6.jpg' is uploaded.
```

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
В директории утилиты необходимо создать файл `.env`, в котором в переменных `LOGIN` и `PASSWORD` будут хранится 
соответственно логин и пароль вашего Instagram-аккаунта.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).