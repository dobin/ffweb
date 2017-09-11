from rest_framework import serializers
from crashviewer.models import Project, CrashData, NetworkMessage



class NetworkMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkMessage
        fields = ('index', 'sentBy', 'msg', 'fuzzed', 'crashData')


class CrashDataSerializer(serializers.ModelSerializer):
    messageList = NetworkMessageSerializer(many=True, read_only=True)

    class Meta:
        model = CrashData
        fields = ('seed', 'offset', 'module', 'signal', 'asanoutput', 'time', 'stdout', 'filename', 'project', 'messageList')


class ProjectSerializer(serializers.ModelSerializer):
    crashDataList = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('name', 'comment', 'crashDataList')
