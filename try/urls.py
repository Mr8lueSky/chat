from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postmessage/', views.create_link, name='create'),
    path('file/', views.file, name='file'),
]