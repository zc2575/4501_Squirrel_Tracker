from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('map/', views.showmap, name='showmap'),
    path('sightings/', views.all_squirrels, name='all_squirrels'),
    path('sightings/add/', views.add, name = 'add'),
    path('sightings/stats/', views.stats, name = 'stats'),
    path('sightings/<str:unique_id>/', views.update, name='update'),
]
