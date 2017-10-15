from django.db import models
from django.utils import timezone


# Has: CrashData's
class Project(models.Model):
    name = models.TextField()
    comment = models.TextField()
    commandline = models.TextField()
    version = models.TextField()
    fuzzingrun = models.TextField()

    def __str__(self):
        return self.name


# Has: NetworkMessage's
class CrashData(models.Model):
    seed = models.CharField(max_length=64)

    time = models.DateTimeField()
    signal = models.IntegerField()

    fuzzerpos = models.CharField(max_length=16)
    reallydead = models.IntegerField()

    stdout = models.TextField(blank=True)
    asanoutput = models.TextField(blank=True)
    gdboutput = models.TextField(blank=True)
    backtrace = models.TextField()

    cause = models.TextField()
    cause_line = models.TextField(blank=True)
    codeoff = models.IntegerField(blank=True)
    codeaddr = models.IntegerField()

    project = models.ForeignKey('Project', related_name='crashDataList', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('time',)

    def __str__(self):
        return self.seed


class NetworkMessage(models.Model):
    crashData = models.ForeignKey('CrashData', related_name="messageList", on_delete=models.CASCADE, null=True)
    index = models.IntegerField()
    sentBy = models.CharField(max_length=16)
    msg = models.TextField()
    fuzzed = models.IntegerField()

    def __str__(self):
        return self.pk
