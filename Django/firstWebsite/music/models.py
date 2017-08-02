from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Album(models.Model):
    artists = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=250)

    def __str__(self):
        return self.artists+" "+self.album_title


class Songs(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=20)
    song_title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title