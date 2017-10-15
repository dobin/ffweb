from django.contrib import admin

from .models import Project, CrashData, NetworkMessage

admin.site.register(Project)
admin.site.register(CrashData)
admin.site.register(NetworkMessage)
