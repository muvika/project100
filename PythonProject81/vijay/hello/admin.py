from django.contrib import admin
from .models import Developer, Project, Task

admin.site.register(Developer)
admin.site.register(Project)
admin.site.register(Task)