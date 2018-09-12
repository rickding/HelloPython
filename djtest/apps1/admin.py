from django.contrib import admin

from .tasks import add, get_task_status
import time

t = add.delay(time.time(), 44)
print('task status: %s' % get_task_status(add, t.id))
t.wait()

# Register your models here.
