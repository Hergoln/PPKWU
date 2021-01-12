from . import views
from django.urls import path

urlpatterns = [
    path('<string>', views.vcard, name='vcard')
] 