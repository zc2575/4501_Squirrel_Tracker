from django.forms import ModelForm

from .models import Squirrel


class Squirrelform(ModelForm):
    class Meta:
        model = Squirrel
        # All other fields are handled in the background
        fields = '__all__'
