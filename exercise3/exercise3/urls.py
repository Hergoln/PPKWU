from django.urls import path, include

urlpatterns = [
	path('calendar/', include('mobile_calendar_weeia.urls')),
]
