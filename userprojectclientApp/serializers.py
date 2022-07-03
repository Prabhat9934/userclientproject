from rest_framework import serializers
from rest_framework.authtoken.models import Token

from userprojectclientApp.models import UserInfo, Client, Project, ProjectClient


class UserInfoSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'assignedProject_id']

    def create(self, validated_data):
        user = UserInfo(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'clientName']


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']


class ProjectClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectClient
        fields = ['id', 'projectId', 'takenByClient_id']


class TokenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['user_id']
