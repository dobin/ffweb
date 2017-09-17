from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from crashviewer import views

urlpatterns = [
    url(r'^$', views.project_overview, name='project_overview'),

    url(r'^projects/$', views.project_overview,
        name="project_overview"),
    url(r'^projects/(?P<pk>[0-9]+)$', views.project_detail,
        name='project_detail'),

    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/projects/(?P<pk>[0-9]+)$', views.ProjectDetail.as_view()),

    #url(r'^api/projects/(?P<pk>[0-9]+)/crashdata/$', views.CrashdataList.as_view()),
    url(r'^api/crashdata/$', views.CrashdataList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
