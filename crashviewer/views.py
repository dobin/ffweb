from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from crashviewer.serializers import ProjectSerializer
from crashviewer.serializers import CrashDataSerializer

from .models import Project
from .models import CrashData



def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return start


def project_overview(request):
    projects = Project.objects.order_by('name')
    return render(request, 'crashviewer/project_overview.html', { 'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    crashDataList = project.crashDataList.all()

    maxBacktraceIndex = 3
    maxBtParam = request.GET.get('maxbt')
    if maxBtParam is not None:
        maxBacktraceIndex = int(maxBtParam)

    # add fuzzed msg index to crashData
    for crashData in crashDataList:
        for msg in crashData.messageList.all():
            if msg.fuzzed == 1:
                crashData.fuzzedMsgIdx = msg.index
                break

        crashData.backtrace = crashData.backtrace[0:find_nth(crashData.backtrace, "\n", maxBacktraceIndex)]

    return render(request, 'crashviewer/project_detail.html', {'project': project, 'crashDataList': crashDataList})


def project_detail_u(request, pk):
    project = get_object_or_404(Project, pk=pk)
    crashDataList = set()
    lookup = {}

    maxBacktraceIndex = 3
    maxBtParam = request.GET.get('maxbt')
    if maxBtParam is not None:
        maxBacktraceIndex = int(maxBtParam)

    crashDataListX = project.crashDataList.all()
    for crashData in crashDataListX:
        if crashData.backtrace not in lookup:
            lookup[crashData.backtrace] = True
            crashDataList.add(crashData)

    # add fuzzed msg index to crashData
    for crashData in crashDataList:
        for msg in crashData.messageList.all():
            if msg.fuzzed == 1:
                crashData.fuzzedMsgIdx = msg.index
                break
        crashData.backtrace = crashData.backtrace[0:find_nth(crashData.backtrace, "\n", maxBacktraceIndex)]

    return render(request, 'crashviewer/project_detail.html', {'project': project, 'crashDataList': crashDataList})


class ProjectList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CrashdataList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    serializer_class = CrashDataSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
