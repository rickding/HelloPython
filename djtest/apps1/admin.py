from django.contrib import admin

from .tasks import add

add.delay(11, 44)

# Register your models here.
