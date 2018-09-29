# dba
Python 3.6.3, PyCharm 2017.2, Django 1.11.6, mysqlclient 1.3.12

https://www.python.org/
https://www.djangoproject.com/
https://www.jetbrains.com/pycharm/
https://pypi.python.org/pypi/MySQL-python

Setup:
- download and install python， select "Add python into environment"
- pip install django==2.0.6
- pip install -r requirement.txt

- pip freeze > requirements.txt
- download and install pycharm

Setup for redis:
- pip install redis==2.10.6

Setup for rabbitMQ:
- pip install pika==0.12.0

Setup for celery:
- pip install celery==3.1.20
- pip install django-celery==3.2.2
- pip install flower==0.9.2

Setup for MySQL:
- pip install mysqlclient==1.3.12

Http Multipart Upload:
- pip install requests-toolbelt==0.8.0

Init app and config db:
- [bat] startapp.bat
- [settings.py] Add it into the list of installed apps in settings.py
- [settings.py] Config the db in the database list in settings.py
- [conf] Add the .cnf for db.
- [router] Add the router.py 
- [settings.py] Add the router into the router list in settings.py
- [url] Add the urls.py and config it into dba/urls.py
- [view] Add functions and config in urls.py

Sync models from db(optional):
- [bat] inspectdb.bat
- [models] Update Meta: replace 'managed = False' as 'managed = True'
- [bat] makemigrations.bat

Config admin(optional):
- [admin]admin.py

Migrate after necessary changes or new ones:
- [models] Update or add new models or fields.
- [bat] makemigrations.bat
- [bat] migrate.bat

Run server(admin):
- python manage.py migrate --database=default
- [bat] createsuperuser.bat
	- admin/superuser
- [bat] runserver.bat
- http://127.0.0.1:8000/admin

Command:
- python manage.py chk
- [app] management/commands/chk.py

Test:
- python manage.py test [app].[file].[func]
- class ChkTest(TestCase): def test_xxx: xxx
