#from this current(.) directory  import views which contain all the htmls
from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns =[
    #music/
    url(r'^$',views.IndexView.as_view(),name="index"),

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

]