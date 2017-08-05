#from this current(.) directory  import views which contain all the htmls
from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns =[
    #music/
    url(r'^$',views.IndexView.as_view(),name="index"),

    url(r'^register/$',views.UserFormView.as_view(),name="register"),

    #mucis/423/
    # url(r'^(?P<album_id>[0-9]+)/$',views.detail,name="detail"),

    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name="detail"),

    #music/2343/favourite
    # url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name="favourite")

    url(r'^add/album/$',views.AlbumCreate.as_view(),name="albumadd"),

    # music/album/update/6
    url(r'^update/album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name="albumupdate"),

    #music/album/delete/6
    url(r'^delete/album/(?P<pk>[0-9]+)/$',views.AlbumDelete.as_view(),name="albumdelete"),

    #music/album/6/songadd
    url(r'^album/(?P<album_id>[0-9]+)/songadd/$',views.SongsCreate.as_view(),name="addsong"),

    #music/album/6/songdelete/3   url(r'^album/(?P<album_id>[0-9]+)/delete/song/(?P<pk>[0-9]+)/$',views.SongsDelete.as_view(),name="deletesong"),
    # url(r'^delete/song/(?P<pk>[0-9]+)/$',views.SongsDelete.as_view(),name="deletesong"),
    url(r'^album/(?P<album_id>[0-9]+)/delete/song/(?P<pk>[0-9]+)/$',views.SongsDelete,name="deletesong"),
]