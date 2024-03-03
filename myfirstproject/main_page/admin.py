from django.contrib import admin

# Register your models here.

from .models import Task # указываем, что мы импортируем из файла models таблицу Task

admin.site.register(Task) # регистрируем таблицу в панели администратора