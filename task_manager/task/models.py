from django.db import models
from task_app.models import Reportee, Reporter
# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=255, unique=True)
    task_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.task)

class Project(models.Model):
    title = models.CharField(max_length=255, unique=True)
    detail = models.CharField(max_length=1024, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class Project_Has_Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ManyToManyField(Task)

    def __str__(self):
        return str(self.project.title)

class Project_Has_Reporter(models.Model):
    Project_Reporter = models.OneToOneField(Reporter, on_delete=models.CASCADE)
    Project_Name = models.ManyToManyField(Project_Has_Task)

    def __str__(self) -> str:
        return str(self.Project_Reporter.admin.email)


class Task_Has_Reportee(models.Model):
    STATUS = (
        ('ToDo', 'ToDo'),
        ('In Progress', 'In Progress'), 
        ('Done', 'Done'), 
     )
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    Reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, null=True)
    Reportee = models.ForeignKey(Reportee, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=250,  choices=STATUS, default='ToDo')         

    def __str__(self):
        return str(f"{self.Project.title}/{self.task.task}/{self.Reportee.Reportee.email}_")
0




    

    

    