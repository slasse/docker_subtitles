# Generated by Django 2.0.2 on 2018-03-27 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0007_auto_20180327_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_name',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]