# from django.http import HttpResponse,Http404
from . models import Album,Songs
# from django.template import loader
from django.shortcuts import render,get_object_or_404

def index(request):
    all_albums= Album.objects.all()
    # template = loader.get_template("music/index.html")
    context = {
        'all_album' : all_albums,
    }
    return render(request,"music/index.html",context)
    # return HttpResponse(template.render(context,request))


def detail(request,album_id):
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("MESSED UP")
    album = get_object_or_404(Album,pk=album_id)
    return render(request,"music/detail.html",{'album':album})


def favourite(request,album_id):
    album = get_object_or_404(Album,pk=album_id)
    try:
        selected_song = album.songs_set.get(pk=request.POST['song'])
    except Songs.DoesNotExist:
        return render(request,"music/detail.html",{"album":album,"error_message":"Messed Up Something"})
    else:
        selected_song.is_favourite=True
        selected_song.save()
        return render(request, "music/detail.html", {'album': album})