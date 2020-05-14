#PythonAnywhere  

[https://www.pythonanywhere.com](https://www.pythonanywhere.com/)  

Итоговый сайт:  
[http://djangoreactexample.pythonanywhere.com](http://djangoreactexample.pythonanywhere.com/)  




###1. Регистрация на PythonAnywhere.  
* Создать аккаунт уровня "Beginner" на PythonAnywhere. Он бесплатный.  
***Примечание:*** URL сайта примет вид **yourusername.pythonanywhere.com**, поэтому при регистрации указать имя **djangoreactexample**.

####1.1. Создание API токена для PythonAnywhere.  
Это нужно будет сделать только один раз при регистрации.

```python
Ссылка "Account" (в правом верхнем углу)  
   Вкладка "API token"  
      Нажать кнопку "Create new API token"  
```



###2. Развертывание существующего проекта на PythonAnywhere.  

```python
Вкладка Dashboard:  
   "New console": "$ Bash"  

Открывшаяся консоль "Bash console 15799134" (или какой-то другой номер):  
   Загрузка кода из GitHub в PythonAnywhere:   
      ~$ git clone https://github.com/Volkova-Natalia/django_react_example.git 
  
   Создание виртуального окружения:   
      ~$ mkvirtualenv djangoreactexample.pythonanywhere.com --python=/usr/bin/python3.8  
   Установка всех требуемых библиотек python в новом окружении:  
      (djangoreactexample.pythonanywhere.com) ~/django_react_example/backend (master)$ pip3.8 install -r requirements.txt --user  
      (без --user почему-то была ошибка)  

   Выйти из виртуального окружения можно так:  
      (djangoreactexample.pythonanywhere.com) ~ $  deactivate  
   Войти в виртуальное окружение можно так:  
      ~ $ workon djangoreactexample.pythonanywhere.com  
```

####2.1. Настройка веб-приложения и файла WSGI.  


2.1.1. Создание веб-приложения с ручной настройкой.  
```python
Вкладка "Web":  
   Нажать кнопку "(+) Add a new web app"  
      Выбрать "Manual configuration (including virtualenvs)"  
      Выбрать "Python 3.8"  
   Нажать "Reload djangoreactexample.pythonanywhere.com"  
```

2.1.2. Текущее виртуальное окружение.  
```python
Вкладка "Web":  
   Раздел "Virtualenv":  
      Вввести имя данного virtualenv:  
         /home/djangoreactexample/.virtualenvs/djangoreactexample.pythonanywhere.com  
         и нажать "OK".  
```

2.1.3. Путь к коду.  
```python
Вкладка "Web":  
   Раздел "Code":  
      Вввести путь к коду:  
         /home/djangoreactexample/django_react_example  
```

2.1.4. Редактирование файла WSGI.  
***Примечание:*** Проект Django будет иметь внутри файл с именем wsgi.py.  
Это не то, что нужно изменить для настройки PythonAnywhere - система здесь игнорирует этот файл.  
```python
Вкладка "Web":  
   Раздел "Code":  
      Ссылка на wsgi файл "WSGI configuration file:"  
         Перейти к файлу wsgi по указанной ссылке:  
            /var/www/djangoreactexample_pythonanywhere_com_wsgi.py  
      Раскомментировать код Django,
         вставить правильные значения path и DJANGO_SETTINGS_MODULE,
         все остальное убрать  
      Получится что-то типа этого:  

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/djangoreactexample/mysite/mysite/settings.py'
# and your manage.py is is at '/home/djangoreactexample/mysite/manage.py'
path = '/home/djangoreactexample/django_react_example/backend'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```



###3. Внесение изменений в проект:  
```python
Вкладка "Files":
   Создать .env файл в соответствующей директории  
      /home/djangoreactexample/django_react_example/backend/backend/settings  
   с нужным наполнением (см. образец .env.sample),  
   выбрать APPLICATION_ENVIRONMENT = "staging"  
```



###4. Настройка базы данных:  



###5. Итоговый сайт:  
```python
Вкладка "Web":  
   Нажать "Reload djangoreactexample.pythonanywhere.com"  
```
[http://djangoreactexample.pythonanywhere.com](http://djangoreactexample.pythonanywhere.com/)  



