from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<str:id>', views.deleteEntry, name='delete'),
    path('download', views.downloadRecords, name='download')
]
