# django_geoloc

## Installation

To start this project, you need to setup a working python 3 environment with Django. I recommend installing virtualenv.
Next, create your virtual env and then clone the project as follow:

```bash
user@hostname ~ $ git clone https://github.com/PLWagner/django_geoloc.git  
user@hostname ~ $ cd django_geoloc  
user@hostname ~/django_geoloc $ source ~/virtualenv/bin/activate  
(virtualenv) user@hostname ~/django_geoloc $ pip install django
(virtualenv) ~/django_geoloc $ python manage.py makemigrations
(virtualenv) ~/django_geoloc $ python manage.py migrate
(virtualenv) ~/django_geoloc $ python manage.py shell
```

Insert the data into de sqlite3 database:

```python
>>> from utils.parser import Parser as p
>>> p.insert_data()
>>> exit()
```

Start the django server:

```bash
(virtualenv) ~/django_geoloc $ python manage.py runserver
```

Next, open a browser and go to `http://127.0.0.1:8000`