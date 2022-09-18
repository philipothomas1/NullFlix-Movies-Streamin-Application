# Generated by Django 4.0 on 2022-02-01 09:27

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tvseries', '0003_season_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='language',
            field=models.CharField(blank=True, choices=[('ENGLISH', 'ENGLISH'), ('FRENCH', 'FRENCH'), ('SPANISH', 'SPANISH'), ('ITALIANO', 'ITALIANO'), ('CHINESE', 'CHINESE'), ('JAPANESE', 'JAPANESE'), ('RUSSIAN', 'RUSSIAN'), ('SWAHILI', 'SWAHILI')], max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='episode',
            name='parental_gardian',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='episode',
            name='plot',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='episode',
            name='quality',
            field=models.CharField(blank=True, choices=[('1080HD', '1080HD'), ('720HD', '720HD'), ('480P', '480P'), ('3GP', '3GP')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='episode',
            name='released',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tvseries',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='tvseries',
            name='genre',
            field=models.CharField(blank=True, choices=[('COMEDY', 'COMEDY'), ('SCI-FI', 'SCI-FI'), ('ACTION', 'ACTION'), ('ROMANCE', 'ROMANCE'), ('ROMCOMEDY', 'ROMCOMEDY'), ('ADVENTURE', 'ADVENTURE'), ('DRAMA', 'DRAMA'), ('HORROR', 'HORROR'), ('ANIMATION', 'ANIMATION')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tvseries',
            name='premiere',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tvseries',
            name='status',
            field=models.CharField(blank=True, choices=[('IN PRODUCTION', 'IN PRODUCTION'), ('ENDED', 'ENDED'), ('CANCELLED', 'CANCELLED')], max_length=100, null=True),
        ),
    ]