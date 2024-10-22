from django.db import models
from project_types.models import ProjectType


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    registered_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)
    deleted_status = models.BooleanField(default=False)
    finishing_date = models.DateField(null=True)
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class ProjectDocuments(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    deleted_status = models.BooleanField(default=False)
    file = models.FileField(null=True)
