# Generated by Django 4.0 on 2022-01-27 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_alter_moviegenre_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='tv_series',
        ),
        migrations.DeleteModel(
            name='Episode',
        ),
        migrations.DeleteModel(
            name='Season',
        ),
        migrations.DeleteModel(
            name='TVSeries',
        ),
    ]
