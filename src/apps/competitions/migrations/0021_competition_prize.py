# Generated by Django 2.0 on 2018-03-06 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0020_auto_20180301_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='prize',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]