from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Client(models.Model):
    objects = models.Manager()
    clientName = models.CharField(max_length=100)

    def __str__(self):
        return self.clientName


class Project(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProjectClient(models.Model):
    objects = models.Manager()
    takenByClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE)


class UserInfo(AbstractUser):
    assignedProject = models.ForeignKey(Project, on_delete=models.PROTECT, null=True)


class UserClient(models.Model):
    objects = models.Manager()
    client = models.ManyToManyField(UserInfo)
