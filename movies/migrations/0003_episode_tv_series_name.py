# Generated by Django 4.0 on 2022-01-14 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_episode_moviegenre_review_season_tvseries_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='tv_series_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.tvseries'),
        ),
    ]
