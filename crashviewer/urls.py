from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from crashviewer import views

urlpatterns = [
    url(r'^$', views.project_overview, name='project_overview'),

    url(r'^projects/$', views.project_overview),
    url(r'^projects/(?P<pk>[0-9]+)$', views.project_detail, name='project_detail'),

    url(r'^api/projects/$', views.project_list_api),
    url(r'^api/projects/(?P<pk>[0-9]+)$', views.project_list_api),
]

urlpatterns = format_suffix_patterns(urlpatterns)
