from . import views
from django.urls import path

urlpatterns = [
    path('', views.stringAPI, name='stringAPI')
]