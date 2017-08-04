from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Album(models.Model):
    artists = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField(default='/default_album.png')


    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.artists+" "+self.album_title


class Songs(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    file_type = models.CharField(max_length=20, default='mp3')
    song_file = models.FileField(default='/default_song.mp3')
    is_favourite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.album.id})

    def __str__(self):
        return self.song_title