import csv

from django.core.management.base import BaseCommand
from django.utils import timezone
from tracker.models import Squirrel
import datetime

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path',type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path,encoding = 'utf-8') as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        squirrels = []
        for dict_ in data:
            squirrels.append(Squirrel(
                latitude=dict_['X'],
                longtitude = dict_['Y'],
                unique_id = dict_['Unique Squirrel ID'],
                shift = dict_['Shift'],
                date =datetime.date(int(dict_['Date'][5:8]),int(dict_['Date'][0:2]),int(dict_['Date'][2:4])),
                age = dict_['Age'],
                primary_fur_color = dict_['Primary Fur Color'],
                location = dict_['Location'],
                specific_location = dict_['Specific Location'],
                running = dict_['Running'],
                chasing = dict_['Chasing'],
                climbing = dict_['Climbing'],
                eating = dict_['Eating'],
                foraging = dict_['Foraging'],
                other_activities = dict_['Other Activities'],
                kuks = dict_['Kuks'],
                quaas = dict_['Quaas'],
                moans = dict_['Moans'],
                tail_flags = dict_['Tail flags'],
                tail_twitches = dict_['Tail twitches'],
                approaches = dict_['Approaches'],
                indifferent = dict_['Indifferent'],
                runs_from = dict_['Runs from']
                ))
            Squirrel.objects.bulk_create(squirrels)


            
