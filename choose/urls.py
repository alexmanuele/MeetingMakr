from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.MeetingMaker.as_view(), name='index'),
    path('create/', views.CreatePerson.as_view(), name='create'),
    path('select/', views.select, name="select"),
    re_path(r'^(?P<pk>\d+)/update/$', views.person_update, name='person_update'),
    re_path(r'^(?P<pk>\d+)/present/$', views.person_present, name='person_present')
]