# Generated by Django 2.0 on 2018-02-02 03:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('producers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='api_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]