#from this current(.) directory  import views which contain all the htmls
from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns =[
    #music/
    url(r'^$',views.index,name="index"),

    #mucis/423/
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name="detail"),

    #music/2343/favourite
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name="favourite")
]