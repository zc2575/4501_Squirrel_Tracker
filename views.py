from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Squirrel
from .forms import SquirrelForm

def showmap(request):
    sightings = Squirrels.objects.all()
    context = {
        'sightings': sightings
    }
    return render(request, 'map/map.html', context)

def all_squirrels(request):
    squirrel_list = Squirrels.objects.all()
    context = {
        'squirrels': squirrels
    }
    return render(request, 'sightings/squirrel_list.html', context)

def update(request, squirrel_id):
    Squirrel = get_object_or_404(Squirrels, Unique_squirrel_id=squirrel_id)
    if request.method == "POST":
        form = SquirrelForm(request.POST,instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect('tracker:all')
    else:
	form = SquirrelForm(instance = squirrel)
	context ={
		'form':form
			}
        return render(request, 'sightings/update_form.html', context)
