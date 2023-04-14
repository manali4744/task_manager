from django.contrib import admin
from .models import Project,  Task, Task_Has_Reportee, Project_Has_Task, Project_Has_Reporter

# Register your models here.

class Task_Has_ReporteeAdmin(admin.ModelAdmin):
    list_display = ['Reporter','Reportee','task','status', 'Project', 'Priority', 'created_at', 'expected_at','submitted_at' ]

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task', 'created_at', 'submitted_at']

admin.site.register(Project)
admin.site.register(Task, TaskAdmin)
admin.site.register(Task_Has_Reportee, Task_Has_ReporteeAdmin)
admin.site.register(Project_Has_Reporter)
admin.site.register(Project_Has_Task)