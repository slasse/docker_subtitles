from django.db import models
from django.urls import reverse

# Create your models here.

class movie_name(models.Model):
    id = models.AutoField(primary_key=True)
    moviename = models.CharField(max_length=100, unique=True)
    has_subtitle = models.BooleanField(default=False)

    def __str__(self):
        return str(self.moviename)

    def get_absolute_url(self):
        return reverse('viewer:detail_view', kwargs={'m_detail': self.moviename})

class file_list(models.Model):
    id = models.AutoField(primary_key=True)
    m_name = models.ForeignKey(movie_name, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=50, unique=True)
    file_path = models.CharField(max_length=80, unique=True)
    file_size = models.DecimalField(max_digits=30, decimal_places=2)
    file_date = models.DateField()
    is_subtitle = models.BooleanField(default=False)

    def __str__(self):
        return str(self.file_name)

    def save(self, *args, **kwargs):
        MB = int(1048576)
        self.file_size = (self.file_size/MB)
        super(file_list, self).save(*args, **kwargs)

class settings(models.Model):
    folder_path = models.CharField(max_length=50, unique=True)
    enabled = models.BooleanField(default=False)