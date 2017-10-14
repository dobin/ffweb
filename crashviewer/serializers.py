from rest_framework import serializers
from crashviewer.models import Project, CrashData, NetworkMessage



class NetworkMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkMessage
        fields = ('index', 'sentBy', 'msg', 'fuzzed', 'crashData')


class CrashDataSerializer(serializers.ModelSerializer):
    messageList = NetworkMessageSerializer(many=True)

    class Meta:
        model = CrashData
        fields = ('pk', 'seed', 'offset', 'signal',
                  'asanoutput', 'time', 'stdout', 'backtrace',
                  'codeoff', 'codeaddr', 'fuzzerpos',
                  'reallydead', 'cause', 'cause_line', 'gdboutput',
                  'project', 'messageList')

    def create(self, validated_data):
        messageList_data = validated_data.pop('messageList')

        # if crashdata with the same seed exists, just delete
        # it, so we can write it fresh and new.
        # We dont want duplicates, but up to date data.
        cds = CrashData.objects.filter(seed=validated_data.get('seed', None))
        if len(cds) > 0:
            for cd in cds:
                cd.delete()

        crashData = CrashData.objects.create(**validated_data)
        for message in messageList_data:
            NetworkMessage.objects.create(crashData=crashData, **message)

        return crashData


class ProjectSerializer(serializers.ModelSerializer):
    crashDataList = CrashDataSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('pk', 'name', 'comment', 'crashDataList')
        #fields = ('pk', 'name', 'comment')
