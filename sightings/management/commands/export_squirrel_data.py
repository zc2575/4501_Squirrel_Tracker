from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import pandas as pd

class Command(BaseCommand):
    
    
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
        
    def handle(self, *args, **options):
        path = options['path']
        squirrels = Squirrel.objects.all().values()
        df = pd.DataFrame(squirrels)
        df.to_csv(path)
