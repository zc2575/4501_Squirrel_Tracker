from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect


from .models import Squirrel

def showmap(request):
    sightings = Squirrels.objects.all()
    context = {
        'sightings': sightings
    }
    return render(request, 'map/map.html', context)
