# python, django, pycharm
https://www.python.org/
https://www.djangoproject.com/
https://www.jetbrains.com/pycharm/

# Celery
- config settings.py: CELERY_XXX
- add celery.py
- add tasks.py
- add task_util.py
- add test_task_util.py

IDE:
- download and install pycharm

Env:
- download and install python, select "Add python into environment"
- [bash] ./pip_install.sh
- [bash] ./startproject.sh

Init app and config urls:
- [bash] ./startapp.sh
- [settings.py] Add it into the list of installed apps in settings.py
- [url] Add the urls.py and config it into dba/urls.py
- [view] Add functions and config in urls.py

Run server:
- [bash] ./runserver.sh
- http://127.0.0.1:8001/

Command:
- [bash] ./cmd.sh or python manage.py chk
- [app] management/commands/chk.py

Test:
- [bash] ./test.sh or python manage.py test [app].[file].[func]
- class ChkTest(TestCase): def test_xxx: xxx
