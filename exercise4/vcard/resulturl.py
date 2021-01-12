from . import views
from django.urls import path

urlpatterns = [
    path('result/<string>', views.vcard, name='result')
] 