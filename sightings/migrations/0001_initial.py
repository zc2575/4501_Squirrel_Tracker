# Generated by Django 3.1.7 on 2021-04-10 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(blank=True)),
                ('longitude', models.FloatField(blank=True)),
                ('unique_id', models.CharField(help_text='Unique id of the squirrel', max_length=100)),
                ('shift', models.CharField(blank=True, choices=[('PM', 'PM'), ('AM', 'AM')], max_length=16)),
                ('date', models.DateField(help_text='Enter the date')),
                ('age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Select the age that it is closest to', max_length=100)),
                ('primary_fur_color', models.CharField(blank=True, choices=[('Black', 'Black'), ('Gray', 'Gray'), ('Cinnamon', 'Cinnamon')], help_text='Select the color it is closest to', max_length=100)),
                ('location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], max_length=100)),
                ('specific_location', models.TextField(blank=True, help_text='Please describe the specific location')),
                ('running', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100)),
                ('chasing', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100)),
                ('climbing', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100)),
                ('eating', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100)),
                ('foraging', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100)),
                ('other_activities', models.TextField(blank=True, help_text='Please describe other activity that it has')),
                ('kuks', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100)),
                ('quaas', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100)),
                ('moans', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100)),
                ('tail_flags', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100)),
                ('tail_twitches', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100)),
                ('approaches', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100)),
                ('indifferent', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100)),
                ('runs_from', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100)),
            ],
        ),
    ]
