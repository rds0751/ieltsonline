from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^delete/(?P<part_id>[0-9]+)/$', views.delete_assign, name='delete_assign'),
    url(r'^add', views.addStudent, name='addStudent'),
    # url(r'^delete/', views.delete_studentprofile, name='delete_studentprofile'),
    url(r'^add/delete/(?P<part_id>[0-9]+)/$', views.delete_studentprofile, name='delete_studentprofile'),
    ]
