from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel
from .forms import Squirrelform
from django.db.models import Avg, Max, Min, Count
from django.shortcuts import redirect

def showmap(request):
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings
    }
    return render(request, 'sightings/map.html', context)

def all_squirrels(request):
    squirrel_list = Squirrel.objects.all()
    context = {
        'squirrels': squirrel_list
    }
    return render(request, 'sightings/squirrel_list.html', context)

def update(request, unique_id):
    squirrel = get_object_or_404(Squirrel, unique_id=unique_id)
    if request.method == 'POST':
        form = Squirrelform(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
        form = Squirrelform(instance=squirrel)
        context = {
	    'form': form
                } 
        return render(request, 'sightings/update_form.html', context)

def add(request):
    if request.method=='Post':
        form = Squirrelform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = Squirrelform()
    context ={
	'form':form
		}
    return render(request, 'sightings/add.html', context)


def stats(request):
    total_squirrel = Squirrel.objects.count()
    adult = Squirrel.objects.filter(age = 'Adult').count()
    juvenile = Squirrel.objects.filter(age = 'Juvenile').count()
    black = Squirrel.objects.filter(primary_fur_color = 'black').count()
    cinnamon = Squirrel.objects.filter(primary_fur_color = 'cinnamon').count()
    gray = Squirrel.objects.filter(primary_fur_color = 'gray').count()
    am = Squirrel.objects.filter(shift = 'AM').count()
    pm = Squirrel.objects.filter(shift = 'PM').count()
    location_above = Squirrel.objects.filter(location='Above Ground').count()
    location_plane = Squirrel.objects.filter(location='Ground Plane').count()
    latitude = Squirrel.objects.aggregate(minimum=Min('latitude'),maximum=Max('latitude'))
    longitude = Squirrel.objects.aggregate(minimum=Min('longitude'),maximum=Max('longitude'))
    running = Squirrel.objects.filter(running='TRUE').count()
    not_running = Squirrel.objects.filter(running='FALSE').count()

    context = {'total': total_squirrel,
                'adult':adult,
                'juvenile':juvenile,
                'black':black,
                'cinnamon':cinnamon,
                'gray':gray,
                'am':am,
                'pm':pm,
                'location_above': location_above,
                'location_plane': location_plane,
    		    'latitude': latitude,
		        'longitude': longitude,
		        'running': running,
                'not_running': not_running,
		}
    return render(request, 'sightings/stats.html', context)
