# Generated by Django 4.0 on 2022-01-14 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('actor', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_number', models.IntegerField(blank=True, null=True)),
                ('episode_theme', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, max_length=3000)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, '1 - Trash'), (2, '2 - Horrible'), (3, '3 - Terrible'), (4, '4 - Bad'), (5, '5 - OK'), (6, '6 - Watchable'), (7, '7 - Good'), (8, '8 - Very Good'), (9, '9 - Perfect'), (10, '10 - Master Piece')])),
                ('likes', models.PositiveIntegerField(default=0)),
                ('unlikes', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TVSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tv_series_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'TVSeries',
            },
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Awards',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='BoxOffice',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='DVD',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Genre',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Metascore',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Poster_url',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Production',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Rated',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Ratings',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Runtime',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Website',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='imdbID',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='imdbRating',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='imdbVotes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='totalSeasons',
        ),
        migrations.AddField(
            model_name='movie',
            name='Actors',
            field=models.ManyToManyField(blank=True, to='actor.Actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='Description',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_trailer',
            field=models.FileField(blank=True, null=True, upload_to='movies/videos/trailers'),
        ),
        migrations.AddField(
            model_name='movie',
            name='parental_gardian',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='quality',
            field=models.CharField(blank=True, choices=[('1080HD', '1080HD'), ('720HD', '720HD'), ('480P', '480P'), ('3GP', '3GP')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Language',
            field=models.CharField(blank=True, choices=[('EN', 'ENGLISH'), ('FR', 'FRENCH'), ('SP', 'SPANISH'), ('IT', 'ITALIANO'), ('CHN', 'CHINESE'), ('JPN', 'JAPANESE'), ('RS', 'RUSSIAN'), ('SW', 'SWAHILI')], max_length=300),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Released',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Year',
            field=models.DateField(),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.AddField(
            model_name='season',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.tvseries'),
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.season'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.moviegenre'),
        ),
    ]
