# Космический Инстаграм

С помощью этой утилиты вы сможете автоматизировать скачивание фото на космическую тематику и загрузку их в свой
Instagram-аккаунт.

Модуль `fetch_hubble.py` использует API телескопа Hubble для загрузки фотографии коллекции фотографий. Пример запуска
скрипта:
```
python3 main.py images -c wallpaper
```
Вывод:
```
Start downloading wallpaper photos from Hubble
Downloading image 0/14...
Downloading image 1/14...

```
 
Модуль `fetch_spacex.py` использует API телескопа проекта Space X для загрузки фотографий с последнего запуска ракеты.
Пример запуска скрипта:
```
python3 main.py images -x
```
Вывод:
```
Start downloading last Space X launch photos
Downloading image 0/9...
Downloading image 1/9...
Downloading image 2/9...
Downloading image 3/9...
```

Модуль `upload_to_instagram.py` заливает все изображения из указанной в качестве аргумента директории в аккаунт
Instagram. Пример запуска скрипта:
```
python3 main.py images -u
```
Вывод:
```
Start uploading images from images to Instagram dinar_dvmn
2019-04-24 23:28:53,455 - INFO - Instabot Started
2019-04-24 23:28:54,948 - INFO - Logged-in successfully as 'dinar_dvmn'!
Analizing `images/3813.tif`
.
.
.
```
Возможно запустить скачивание и загрузку одной командой:
```
python3 main.py images -c wallpaper -x -u
```

### Как установить

Для работы требуется Python не ниже версии 3.6.
Затем используйте `pip3`  для установки зависимостей:
```
pip install -r requirements.txt
```
В директории утилиты необходимо создать файл `.env`, в котором в переменных `LOGIN` и `PASSWORD` будут хранится 
соответственно логин и пароль вашего Instagram-аккаунта, необхомые для аутентификации при загрузке фото.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).