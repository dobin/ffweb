from django.db import models
from django.utils import timezone


# Has: CrashData's
class Project(models.Model):
    name = models.TextField()
    comment = models.TextField()


# Has: NetworkMessage's
class CrashData(models.Model):
    seed = models.CharField(max_length=64)
    offset = models.IntegerField()
    module = models.CharField(max_length=1024)
    signal = models.IntegerField()
    asanoutput = models.TextField()
    time = models.DateTimeField()
    stdout = models.TextField()
    backtrace = models.TextField()

    fuzzerpos = models.CharField(max_length=16)
    reallydead = models.IntegerField()

    cause = models.TextField()
    cause_line = models.TextField()

    stackoff = models.IntegerField()
    stackaddr = models.IntegerField()
    codeoff = models.IntegerField()
    codeaddr = models.IntegerField()

    registers = models.TextField()

    project = models.ForeignKey('Project', related_name='crashDataList', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('time',)


class NetworkMessage(models.Model):
    crashData = models.ForeignKey('CrashData', related_name="messageList", on_delete=models.CASCADE, null=True)
    index = models.IntegerField()
    sentBy = models.CharField(max_length=16)
    msg = models.BinaryField()
    fuzzed = models.IntegerField()
