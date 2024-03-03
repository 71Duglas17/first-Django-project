from .models import Task
from django.forms import ModelForm, TextInput, Textarea  # подключаем дополнительно сами

class TaskForm(ModelForm):
    class Meta: # в этом классе указываем какие нибудь доп. настройки
        model = Task # указываем что мы работаем с моделью Task
        fields = ["title", "task"] # указываем какие поля будут в нашей форме
        # доп поле
        widgest = {
            "title": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Введите название таска"
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Vvedite opisanie'
            }),
        }
