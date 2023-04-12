from django.db import models
from task_app.models import Reportee, Reporter
# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=255)
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


class Project_Has_Reporter(models.Model):
    Project_Reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    Project_Name = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return str(f"{self.Project_Reporter}/{self.Project_Name}")
    
    class Meta:
        unique_together = (('Project_Reporter', 'Project_Name'),)


class Task_Has_Reportee(models.Model):
    STATUS = (
        ('ToDo', 'ToDo'),
        ('In Progress', 'In Progress'), 
        ('Done', 'Done'), 
     )
    Project_info = models.ForeignKey(Project_Has_Reporter, on_delete=models.CASCADE)
    Reportee = models.ForeignKey(Reportee, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=250,  choices=STATUS, default='ToDo')         

    def __str__(self):
        return str(f"{self.Project_info.Project_Name.title}/{self.task.task}/{self.Reportee.Reportee.email}_")






    

    

    