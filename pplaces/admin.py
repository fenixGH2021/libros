from django.contrib import admin

# Register your models here.
from .models import PriorityPlacesREF, ProjectLocation, Project

# Register your models here.
admin.site.register(PriorityPlacesREF)
admin.site.register(ProjectLocation)
admin.site.register(Project)