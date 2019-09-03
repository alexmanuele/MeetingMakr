from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', views.meetingmakr, name='index'),
    path('create/', views.CreatePerson.as_view(), name='create'),
    re_path(r'^select/(?P<lab_id>\d+)/$', views.select, name="select"),
    path('labcreate/', views.lab_create, name='lab_create'),
    re_path(r'^personcreate/(?P<lab_id>\d+)/$', views.person_create, name='person_create'),
    re_path(r'^(?P<pk>\d+)/update/$', views.person_update, name='person_update'),
    re_path(r'^(?P<pk>\d+)/present/$', views.person_present, name='person_present'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.person_delete, name='person_delete'),
]
