# Celery

https://blog.csdn.net/yeyingcai/article/details/78647553
https://blog.csdn.net/liyingke112/article/details/78389403
https://blog.csdn.net/dipolar/article/details/22162863

Setup for celery:
- pip install celery==3.1.20
- pip install django-celery==3.2.2
- pip install flower==0.9.2

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8001 #启动django的应用，可以动态的使用django-admin来管理任务
python manage.py celery worker -c 6 -l debug  #任务执行进程，worker进程
python manage.py celeryd -l info

python manage.py celery beat #应该是用来监控任务变化的
python manage.py celery flower

http://localhost:8001/admin
http://localhost:5555 # flower
