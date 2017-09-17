from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404


from crashviewer.models import Project
from crashviewer.serializers import ProjectSerializer

from crashviewer.models import CrashData
from crashviewer.serializers import CrashDataSerializer

from .models import Project
from .models import CrashData


def project_overview(request):
    projects = Project.objects.order_by('name')
    return render(request, 'crashviewer/project_overview.html', { 'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    crashDataList = project.crashDataList.all()

    return render(request, 'crashviewer/project_detail.html', {'project': project, 'crashDataList': crashDataList})


@api_view(['GET', 'POST'])
def project_list_api(request):
    """
    List all project, or create a new project.
    """
    if request.method == 'GET':
        crashviewer = Project.objects.all()
        serializer = ProjectSerializer(crashviewer, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def project_detail_api(request, pk):
    """
    Retrieve, update or delete a project instance.
    """
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def crashdata_list_api(request):
    """
    List all crashviewer, or create a new crashdata.
    """
    if request.method == 'GET':
        crashviewer = CrashData.objects.all()
        serializer = CrashDataSerializer(crashviewer, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CrashDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def crashdata_detail_api(request, pk):
    """
    Retrieve, update or delete a crashdata instance.
    """
    try:
        crashdata = CrashData.objects.get(pk=pk)
    except CrashData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CrashDataSerializer(crashdata)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CrashDataSerializer(crashdata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        crashdata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
