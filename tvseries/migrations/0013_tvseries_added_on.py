# Generated by Django 4.0 on 2022-02-03 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvseries', '0012_episode_released'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvseries',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]