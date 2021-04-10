from django.db import models
from django.utils.translation import gettext as _


# Create your models here.

class Squirrel(models.Model):
    latitude = models.FloatField(
            blank= True
            )

    longitude = models.FloatField(
            blank = True
            )
    unique_id = models.CharField(
            max_length = 100,
            help_text = _('Unique id of the squirrel'),
            )
    PM = 'PM'
    AM = 'AM'

    shift_choice = [
            (PM,'PM'),
            (AM,'AM'),
            ]
    shift = models.CharField(
            max_length = 16,
            choices = shift_choice,
            blank = True,
            )
    date = models.DateField(
            help_text =_( 'Enter the date'),
            )
    Adult = 'Adult'
    Juvenile = 'Juvenile'

    age_choice = [
            (Adult,'Adult'),
            (Juvenile,'Juvenile'),
            ]
    age = models.CharField(
            max_length = 100,
            choices = age_choice,
            help_text = _('Select the age that it is closest to'),
            blank = True,
            )
    Black = 'Black'
    Gray = 'Gray'
    Cinnamon = 'Cinnamon'

    color_choice = [
            (Black,'Black'),
            (Gray,'Gray'),
            (Cinnamon,'Cinnamon'),
            ]


    primary_fur_color = models.CharField(
            max_length = 100,
            choices = color_choice,
            help_text = _('Select the color it is closest to'),
            blank = True,
    
        )

    Ground_plane = 'Ground Plane'
    Above_ground = 'Above Ground'

    location_choices = [
            (Ground_plane,'Ground Plane'),
            (Above_ground,'Above Ground'),
            ]
    location = models.CharField(
            max_length = 100,
            choices = location_choices,
            blank = True,
            )
    specific_location = models.TextField(
            help_text = _('Please describe the specific location'),
            blank = True,
            )
    TRUE = 'TRUE'
    FALSE = 'FALSE'
    choice_ls = [
            (TRUE,'TRUE'),
            (FALSE,'FALSE'),
            ]
    running = models.CharField(
            max_length = 100,
            choices = choice_ls,
            blank = True,
            )
    chasing = models.CharField(
            max_length = 100,
            choices = choice_ls,
            blank = True,
            )
    climbing = models.CharField(
            max_length = 100,
            choices = choice_ls,
            blank = True,
            )
    eating = models.CharField(
            max_length = 100,
            choices = choice_ls,
            blank = True,
            )
    foraging = models.CharField(
            max_length = 100,
            choices = choice_ls,
            blank = True,
            )
    other_activities = models.TextField(
            help_text = _('Please describe other activity that it has'),
            blank = True,
            )
    kuks = models.CharField(
            max_length = 100,
            choices = choice_ls,
            blank = True,
            )
    quaas = models.CharField(
            max_length = 100,
            choices = choice_ls,
            blank = True,
            )
    moans = models.CharField(
            max_length = 100,
            choices = choice_ls,
            blank = True,
            )
    tail_flags = models.CharField(
            max_length = 100,
            choices = choice_ls,
            blank = True,
            )
    tail_twitches = models.CharField(
            max_length = 100,
            choices = choice_ls,
            blank = True,
            )
    approaches = models.CharField(
            max_length = 100,
            choices = choice_ls,
            blank = True,
            )
    indifferent = models.CharField(
            max_length = 100,
            choices = choice_ls,
            blank = True,
            )
    runs_from = models.CharField(
            max_length = 100,
            choices = choice_ls,
            blank = True,
            )


