from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# Has: CrashData's
class Project(models.Model):
    name = models.TextField()
    comment = models.TextField()


# Has: NetworkMessage's
class CrashData(models.Model):
    seed = models.CharField(max_length = 64)
    offset = models.IntegerField()
    module = models.CharField(max_length = 1024)
    signal = models.IntegerField()
    asanoutput = models.TextField()
    time = models.DateTimeField()
    stdout = models.TextField()
    filename = models.CharField(max_length = 1024)

    project = models.ForeignKey('Project', related_name='crashDataList', on_delete=models.CASCADE, null=True)

    class Meta:
         ordering = ('time',)


class NetworkMessage(models.Model):
    crashData = models.ForeignKey('CrashData', related_name="messageList", on_delete=models.CASCADE, null = True)
    index = models.IntegerField()
    sentBy = models.CharField(max_length = 16)
    msg = models.BinaryField()
    fuzzed = models.IntegerField()
