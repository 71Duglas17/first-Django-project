from django.urls import path
# . - указываем, что импортируем файл из этой же директории
from . import views

urlpatterns = [
    # '' - главная страница
    #path('', views.index), # при переходе на главную страницу будет вызываться функция index из файла views
    path('logins', views.logins_page),
    #path('create', views.create)
]