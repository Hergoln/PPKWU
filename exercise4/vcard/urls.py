from . import views
from django.urls import path

urlpatterns = [
    path('vcard/<string>', views.vcard, name='vcard')
] 