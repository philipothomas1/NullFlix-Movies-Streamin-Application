# Generated by Django 4.0 on 2022-02-07 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvseries', '0013_tvseries_added_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvseries',
            name='added_on',
        ),
    ]
