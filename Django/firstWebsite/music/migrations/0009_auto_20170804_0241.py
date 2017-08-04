# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20170804_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(default='/default_album.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='songs',
            name='song_file',
            field=models.FileField(default='/default_song.mp3', upload_to=''),
        ),
    ]
