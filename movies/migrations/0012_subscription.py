# Generated by Django 4.0 on 2022-04-08 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('movies', '0011_subplandiscount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=50)),
                ('reg_date', models.DateField(auto_now_add=True, null=True)),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.subplan')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
