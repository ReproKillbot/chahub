# Generated by Django 2.0 on 2018-07-02 18:48

import requests

from django.db import migrations
from io import BytesIO


def download_and_replace_logos(apps, schema_editor):
    Competition = apps.get_model('competitions', 'Competition')
    for competition in Competition.objects.all():

        # Try to get logo for competition if it's not default, otherwise generate a
        # nice random logo
        if '/static/img/img-wireframe.png' in competition.logo:
            # This is the default image, replace it
            competition.generate_random_logo()
        else:
            resp = requests.get(competition.logo)
            if resp.status_code == 200:
                image = BytesIO()
                image.write(resp.content)
                file_name = competition.logo.split("/")[-1]
                file_name = file_name.split("?")[0]
                competition.logo_file.save(file_name, image)
            else:
                competition.generate_random_logo()
        competition.save()


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0029_competition_logo_file'),
    ]

    operations = [
        migrations.RunPython(download_and_replace_logos),
    ]
