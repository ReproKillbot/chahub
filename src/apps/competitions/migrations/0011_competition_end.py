# Generated by Django 2.0 on 2018-02-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0010_competition_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
