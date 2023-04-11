from django.contrib import admin
from .models import Project, Project_Has_Reporter, Task, Task_Has_Reportee

# Register your models here.




admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Task_Has_Reportee)
admin.site.register(Project_Has_Reporter)