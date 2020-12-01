from . import views
from django.urls import path

urlpatterns = [
	path('<month>', views.calendar, name='calendar'),
	path('', views.calendar_no_month, name='calendar_no_month')
]