# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]
