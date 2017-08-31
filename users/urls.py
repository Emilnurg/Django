"""Определяет схемы URL для пользователей"""

from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    #страница входа
    url(r'^login/$',login, {'template_name' : 'users/login.html'}, name='login'),

    #страница выхода
    url(r'^logout/$', views.logout_view, name='logout'),

    #регистрация
    url(r'^register/$', views.register, name='register'),
]
