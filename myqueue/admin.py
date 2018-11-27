from django.contrib import admin
from .models import Lab, LabPart, Group, Status

admin.site.register(Lab)
admin.site.register(LabPart)
admin.site.register(Group)
admin.site.register(Status)