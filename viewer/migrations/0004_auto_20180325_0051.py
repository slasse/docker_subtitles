# Generated by Django 2.0.2 on 2018-03-24 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_auto_20180325_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_list',
            name='file_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='file_list',
            name='file_path',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='movie_name',
            name='moviename',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
