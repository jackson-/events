from django.conf.urls import patterns, include, url
from django.contrib import admin
from events.views import *


urlpatterns = patterns('',
    url(r'^past$', Past.as_view(), name='past'),
    url(r'^current', Current.as_view(), name='current'),
    url(r'^delete/(?P<pk>\d+)', Delete.as_view(), name='delete'),
    url(r'^pastdelete/(?P<pk>\d+)', PastDelete.as_view(), name='pastdelete'),
    url(r'^edit/(?P<pk>\d+)', Edit.as_view(), name='edit'),
    url(r'^$', Index.as_view(), name='index'),
)
