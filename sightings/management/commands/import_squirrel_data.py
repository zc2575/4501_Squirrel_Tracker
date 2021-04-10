import csv

from django.core.management.base import BaseCommand
from django.utils import timezone
from sightings.models import Squirrel
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
        for row in data:
            squirrels.append(Squirrel(
                latitude=float(row['X']),
                longitude =float(row['Y']),
                unique_id = row['Unique Squirrel ID'],
                shift = row['Shift'],
                date =datetime.date(int(row['Date'][4:8]),int(row['Date'][0:2]),int(row['Date'][2:4])),
                age = row['Age'],
                primary_fur_color = row['Primary Fur Color'],
                location = row['Location'],
                specific_location = row['Specific Location'],
                running = row['Running'].upper(),
                chasing = row['Chasing'].upper(),
                climbing = row['Climbing'].upper(),
                eating = row['Eating'].upper(),
                foraging = row['Foraging'].upper(),
                other_activities = row['Other Activities'],
                kuks = row['Kuks'].upper(),
                quaas = row['Quaas'].upper(),
                moans = row['Moans'].upper(),
                tail_flags = row['Tail flags'].upper(),
                tail_twitches = row['Tail twitches'].upper(),
                approaches = row['Approaches'].upper(),
                indifferent = row['Indifferent'].upper(),
                runs_from = row['Runs from'].upper(),
                ))

        Squirrel.objects.bulk_create(squirrels)


            
