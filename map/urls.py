from django.urls import path
from . import views

urlpatterns = [
	path('map/', views.showmap, name='map'),
	]
