# API для мобильного приложения Перевал.Online

Приложение предназначено для туристов, которые хотят добавить перевал в базу данных.
В данном проекте реализован API для создания, сохранения, просмотра и редактирования базы данных.
[Ссылка на Перевал.Online](https://pereval.online/)

---

##### Реализованные методы:
* _Post_ для сохранение нового объекта "Pereval_added", "User", "Coordinates", "Activities", "Pereval_areas", "Pereval_images" в БД
  *   Пример структуры объекта Pereval_added: 
    ```    
        "id": 1,
        "beautyTitle": "пер.",
        "title": "CCCCCC",
        "other_titles": "Ноа",
        "connect": "DDDDD",
        "winter_lvl": "1А",
        "summer_lvl": "2А",
        "autumn_lvl": "3А",
        "spring_lvl": "4Ф",
        "user_added": "http://127.0.0.1:8000/users/1/",
        "coord_id": "http://127.0.0.1:8000/coordinates/1/",
        "status": "new"  
    ```
* _Get pereval_added/id/_ - возвращает JSON объект типа Pereval_added
* _ PATCH pereval_added/id _ - изменяет поля Pereval_added. Возвращает JSON объект:
  ```
  {
      "state": 1,
      "message": "Successfully updated pereval!"
  }
  ```
  1 — если успешно удалось отредактировать запись в базе данных.
  0 — в противном случае.
* _GET /submitData/?user__email=email_ - список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер.


##### Использованная База Данных:
* _PostgreSQL_

---

### Как это использовать?

1. Скачайте все файлы из репозитория
2. Создайте виртуальное окружение
3. Установите туда все из requirements.txt
4. В файле setting.py найдите список DATABASES и измените его:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Используем postgres
        'NAME': 'my_db', # Ваши данные сюда
        'USER': os.getenv("FSTR_DB_LOGIN"), # Ваши данные сюда
        'PASSWORD': os.getenv("FSTR_DB_PASS"), # Ваши данные сюда
        'HOST':  os.getenv("FSTR_DB_HOST"), # Ваши данные сюда
        'PORT': os.getenv("FSTR_DB_PORT"), # Ваши данные сюда
    },
}
```
5. Все готово. Запустите localhost в терминале (python manage.py runserver). Перейдя по [ссылке](http://127.0.0.1:8000/) вы увидите возможные эндпоинты

---

# API for mobile application Перевал.Online

Application is made for tourists who want to add a new pass to database.
In this project API is created for viewing, creating, saving and changing passes
[Link to Перевал.Online](https://pereval.online/)

---

##### Created methods:
* _Post_ to save new object of "Pereval_added", "User", "Coordinates", "Activities", "Pereval_areas", "Pereval_images" instances to database
  *   Example of "Pereval_added" object's structure: 
    ```    
        "id": 1,
        "beautyTitle": "пер.",
        "title": "CCCCCC",
        "other_titles": "Ноа",
        "connect": "DDDDD",
        "winter_lvl": "1А",
        "summer_lvl": "2А",
        "autumn_lvl": "3А",
        "spring_lvl": "4Ф",
        "user_added": "http://127.0.0.1:8000/users/1/",
        "coord_id": "http://127.0.0.1:8000/coordinates/1/",
        "status": "new"  
    ```
* _Get pereval_added/id/_ - returns JSON of Pereval_added object's type
* _ PATCH pereval_added/id _ - alters Pereval_added object's fields. Returns JSON object like this:
  ```
  {
      "state": 1,
      "message": "Successfully updated pereval!"
  }
  ```
  1 — if altering object was successful.
  0 — otherwise.
* _GET /submitData/?user__email=email_ - list of all objects created by user who has <email> email.


##### Database used in the project:
* _PostgreSQL_

---

### How does it work?

1. Download all files from repository
2. Create virtual environment
3. Install there everything included in requirements.txt
4. In _setting.py_ find _DATABASES_ and change it as follows:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Используем postgres
        'NAME': 'my_db', # Ваши данные сюда
        'USER': os.getenv("FSTR_DB_LOGIN"), # Ваши данные сюда
        'PASSWORD': os.getenv("FSTR_DB_PASS"), # Ваши данные сюда
        'HOST':  os.getenv("FSTR_DB_HOST"), # Ваши данные сюда
        'PORT': os.getenv("FSTR_DB_PORT"), # Ваши данные сюда
    },
}
```
5. Project's setup is ready. Run localhost (python manage.py runserver). Follow the [link](http://127.0.0.1:8000/) and you will see all endpoints.

---
