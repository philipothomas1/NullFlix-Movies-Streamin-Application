# Generated by Django 4.0 on 2022-02-01 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvseries', '0008_alter_episode_released_alter_tvseries_premiere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvseries',
            name='premiere',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
