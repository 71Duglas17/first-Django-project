from django.urls import path
# . - указываем, что импортируем файл из этой же директории (main_page)
from . import views

urlpatterns = [
    # '' - главная страница
    path('', views.index), # при переходе на главную страницу будет вызываться функция index из файла views
    path('about-us', views.about),
    path('create', views.create)
]