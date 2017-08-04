# # from django.http import HttpResponse,Http404
# from . models import Album,Songs
# # from django.template import loader
# from django.shortcuts import render,get_object_or_404
#
# def index(request):
#     all_albums= Album.objects.all()
#     # template = loader.get_template("music/index.html")
#     context = {
#         'all_album' : all_albums,
#     }
#     return render(request,"music/index.html",context)
#     # return HttpResponse(template.render(context,request))
#
#
# def detail(request,album_id):
#     # try:
#     #     album = Album.objects.get(pk=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("MESSED UP")
#     album = get_object_or_404(Album,pk=album_id)
#     return render(request,"music/detail.html",{'album':album})
#
#
# # def favourite(request,album_id):
# #     album = get_object_or_404(Album,pk=album_id)
# #     try:
# #         selected_song = album.songs_set.get(pk=request.POST['song'])
# #     except Songs.DoesNotExist:
# #         return render(request,"music/detail.html",{"album":album,"error_message":"Messed Up Something"})
# #     else:
# #         selected_song.is_favourite=True
# #         selected_song.save()
# #         return render(request, "music/detail.html", {'album': album})
from django.views import generic
from . models import Album,Songs
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_album'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = [ 'artists', 'album_title' ,'genre' ,'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = [ 'artists', 'album_title' ,'genre' ,'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class SongsCreate(CreateView):
    model = Songs
    fields = ['album','song_title','file_type','song_file','is_favourite']

# class SongsDelete(DeleteView):
#     model = Album
#     success_url = reverse_lazy('music:index')

def SongsDelete(request,album_id,pk):
    album = Album.objects.get(pk = album_id)
    selected_song = album.songs_set.get(pk=pk)
    # selected_song.song_file.delete()
    selected_song.delete()
    album.save()
    return render(request , "music/detail.html", {'album':album} )

