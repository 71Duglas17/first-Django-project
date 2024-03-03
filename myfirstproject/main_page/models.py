from django.db import models

# Create your models here.

class Task(models.Model): # таблица с названием Task
    #pass
    # CharField() - класс для текста до 255 символов
    title = models.CharField('Название', max_length = 50) # название поля = его описание: символьный класс (название поля, макс кол-во символов)
    task = models.TextField('Описание')

    def __str__(self): # метод будет вызываться, когда мы будем выводить на экран объект класса Task
        return self.title # теперь на экран будет выводиться поле title, а не его хэш-код 
    
    class Meta: # для смены названия таблицы
        verbose_name = 'Задача' # название в единсвенном числе
        verbose_name_plural = 'Задачи'# во множ. числе