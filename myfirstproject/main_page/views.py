from django.shortcuts import render, redirect
from .models import Task # импорт класса Task из файла models
from .forms import TaskForm

#from django.http import HttpResponse

# Create your views here.

""" def index(request): # функция которая будет вызываться при переходе на главную страницу ('')
    return HttpResponse("<h4>Hello</h4>") """

""" def index(request): # вывод с помощью штмл шаблона, который находится в папке templates
    # прежде чем отобразить шаблон, сначала нужно получить данные из модели
    tasks = Task.objects.all() # в модели Таск обращаемся к объектам:
        # all() - взять все объекты
        # find() - например, найти по id
        # order_by() - сортировать
    # переменная tasks будет списком

    # третьим параметром делаем словарь, в котором будут значения, которые мы хотим передать в шаблон
    return render(request, 'main_page/index.html', {'title': 'Главная страница сайта', 'tasks': tasks}) """

def index(request): # вывод с помощью штмл шаблона, который находится в папке templates
    # прежде чем отобразить шаблон, сначала нужно получить данные из модели
    tasks = Task.objects.order_by('id') # 
    return render(request, 'main_page/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main_page/about.html')

def create(request):
    error = ''
    if request.method == 'POST': # если форма была отправлена методом POST
        form = TaskForm(request.POST) # переменная содержит объект, содержащий данные из формы
        if form.is_valid(): # проверка, если все поля формы заполнены корректно
            form.save() # сохраняем данные как новую запись в БД
            return redirect('/')
        else:
            error = 'Форма заполнена неверно!'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main_page/create.html', context) # словарь можно передавать в виде переменной