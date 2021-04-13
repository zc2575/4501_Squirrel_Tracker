
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('map/',views.showmap, name ='map'),
    path('sightings/', views.all_squirrels, name='all_squirrels'),
    path('sightings/<str:squirrel_id>/', views.update, name='update'),
    path('sightings/add/', views.add, name = 'add'),
    path('sightings/stats/', views.stats, name = 'stats'),
]
