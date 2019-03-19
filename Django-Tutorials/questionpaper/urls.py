from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^rinstruct/$', views.Rinstruction, name="rinst"),
    url(r'^reading/$', views.ReadingPaper, name="reading"),
    url(r'^reading/(?P<part_id>[0-999999]+)/$', views.ReadingPaper, name="reading"),
    url(r'^linstruct/$', views.Linstruction, name="linst"),
    url(r'^listening/$', views.ListeningPaper, name="listening"),
    url(r'^listening/(?P<part_id>[0-999999]+)/$', views.ListeningPaper, name="listening"),
    url(r'^winstruct/$', views.Winstruction, name="winst"),
    url(r'^writing/$', views.WritingPaper, name="writing"),
    url(r'^writing/(?P<part_id>[0-999999]+)/$', views.WritingPaper, name="writing")
    ]
