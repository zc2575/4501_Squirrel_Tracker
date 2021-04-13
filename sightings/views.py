from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Avg, Max, Min, Count

from .models import Squirrel
from .forms import SquirrelForm


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
            return redirect(f'/sightings/{squirrel_id}')
    else:
	form = SquirrelForm(instance = squirrel)
    context ={
        	'form':form
    		}
    return render(request, 'sightings/update_form.html', context)


def add(request):
    if request.method=='Post':
	form = SquirrelForm(request.POST)
	if form.is_valid():
	    form.save()
            return redirect(f'/sightings/')
    else:
	form = SquirrelForm()
    context ={
	'form':form
		}
    return render(request, 'sightings/add.html', context)


def stats(request):
    total_squarrel = Squirrel.objects.count()
    adult = Squirrel.objects.filter(Age = 'Adult').count()
    juvenile = Squirrel.objects.filter(Age = 'Juvenile').count()
    primary_fur_color =list(squirrels.values_list('Primary_Fur_Color').annotate(Count('Primary_Fur_Color')))
    am = Squirrel.objects.filter(Shift = 'AM').count()
    pm = Squirrel.objects.filter(Shift = 'PM').count()
    location_above = Squirrels.objects.filter(location='Above Ground').count()
    location_plane = Squirrels.objects.filter(location='Ground Plane').count()
    lattitude = squirrels.aggregate(minimum=Min('Latitude'),maximum=Max('Latitude'))
    longitude = squirrels.aggregate(minimum=Min('Longitude'),maximum=Max('Longitude'))
    running = Squirrels.objects.filter(running=True).count()
    not_running = Squirrels.objects.filter(running=False).count()

    context = {'total': total,
                'adult':adult,
                'juvenile':juvenile,
                'primary_fur_color': primary_fur_color,
                'am':am,
                'pm':pm,
                'location_above': location_above,
                'location_plane': location_plane,
    		'lattitude': lattitude,
		'longitude': longitude,
		'primary_fur_color': primary_fur_color,
		'running': running,
                'not_running': not_running,
		}
    return render(request, 'sightings/stats.html', context)


def home(request):
    return render(request, 'sightings/home.html')

