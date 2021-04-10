from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Squirrel
from .forms import Squirrelform



def showmap(request):
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings
    }
    return render(request, 'sightings/map.html', context)

def all_squirrels(request):
    squirrel_list = Squirrel.objects.all()
    context = {
        'squirrels': squirrels
    }
    return render(request, 'sightings/squirrel_list.html', context)

def update(request, unique_id):
    Squirrel = get_object_or_404(Squirrel, unique_id=unique_id)
    if request.method == 'POST':
        form = Squirrelform(request.POST, instance=Squirrel)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
        form = Squirrelform(instance=Squirrel)
        context = {
	    'form': form
                } 
        return render(request, 'sightings/update_form.html', context)

