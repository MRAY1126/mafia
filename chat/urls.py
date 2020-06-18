#chat/urls.py

from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'mafia Game'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<room_name>[^/]+)/$',views.room,name='room'),
]
