from django.contrib import admin

# Register your models here.
from userprojectclientApp.models import UserInfo, Client, Project, UserClient, ProjectClient


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'assignedProject_id']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'clientName']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(ProjectClient)
class ProjectClient(admin.ModelAdmin):
    list_display = ['id', 'projectId', 'takenByClient_id']


@admin.register(UserClient)
class UserClientAdmin(admin.ModelAdmin):
    list_display = ['id']
