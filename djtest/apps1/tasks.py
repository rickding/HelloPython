from __future__ import absolute_import

from celery import shared_task
from celery import task


# from celery.task import tasks
# from celery.task import Task


@task
def add2(x, y):
    print("add2: %d + %d = %d" % (x, y, x + y))
    return x + y


@task
def add(x, y):
    add2.delay(11, 22)
    print("%d + %d = %d" % (x, y, x + y))
    return x + y


def get_task_status(task_func, task_id):
    t = task_func.AsyncResult(task_id)
    status = t.state
    progress = 0

    if status == u'SUCCESS':
        progress = 100
    elif status == u'FAILURE':
        progress = 0
    elif status == 'PROGRESS':
        progress = t.info['progress']

    return {'status': status, 'progress': progress}


# class AddClass(Task):
#    def run(x,y):
#        print "%d + %d = %d"%(x,y,x+y)
#        return x+y
# tasks.register(AddClass)

@shared_task
def mul(x, y):
    print("%d * %d = %d" % (x, y, x * y))
    return x * y


@shared_task
def sub(x, y):
    print("%d - %d = %d" % (x, y, x - y))
    return x - y
