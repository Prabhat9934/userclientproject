# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from userprojectclientApp.models import UserInfo, Client
from userprojectclientApp.serializers import UserInfoSerializers, ClientSerializers, ProjectClientSerializers


@api_view(['GET', 'POST'])
def registerApi(request, pk=None):
    if request.method == 'GET':
        try:
            if pk is not None:
                registerUserObject = UserInfo.objects.get(id=pk)
                serializer = UserInfoSerializers(registerUserObject)
                return Response({'responseCode': 0, 'responseMessage': "Success", 'responseData': serializer.data})
        except Exception as ex:
            return Response({'responseCode': -1, 'responseMessage': ex})

        registerUserAllObjects = UserInfo.objects.all().exclude(id=1)
        serializer = UserInfoSerializers(registerUserAllObjects, many=True)
        return Response({'responseCode': 0, 'responseMessage': 'Success', 'responseData': serializer.data})

    if request.method == 'POST':

        serializer = UserInfoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                {'responseCode': 0, 'responseMessage': "You have registered Successfully",
                 "responseData": serializer.data})
        return Response({'responseCode': 111, 'responseMessage': "Invalid Data"})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def clientApi(request, pk=None):
    if request.method == 'GET':
        try:
            if pk is not None:
                clientObject = Client.objects.get(id=pk)
                serializer = ClientSerializers(clientObject)
                return Response({'responseCode': 0, 'responseMessage': "Success", 'responseData': serializer.data})
        except Exception as ex:
            return Response({'responseCode': -1, 'responseMessage': ex})

        clientAllObjects = Client.objects.all()
        serializer = ClientSerializers(clientAllObjects, many=True)
        return Response({'responseCode': 0, 'responseMessage': 'Success', 'responseData': serializer.data})

    if request.method == 'POST':
        serializer = ClientSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'responseCode': 0, 'responseMessage': "Client registered successfully",
                             "responseData": serializer.data})
        return Response({'responseCode': 111, 'responseMessage': "Invalid Data"})

    if request.method == 'PUT':
        try:
            clientObject = Client.objects.get(id=pk)
            serializer = ClientSerializers(clientObject, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'responseCode': 0, 'responseMessage': "Client updated successfully",
                                 "responseData": serializer.data})
        except Exception as ex:
            return Response({'responseCode': -1, 'responseMessage': ex})

        serializer = ClientSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'responseCode': 0, 'responseMessage': "Client registered successfully",
                             "responseData": serializer.data})
        return Response({'responseCode': 111, 'responseMessage': "Invalid Data"})

    if request.method == 'DELETE':
        try:
            Client.objects.get(id=pk).delete()
            return Response({'responseCode': 0, 'responseMessage': "Client deleted successfully"})
        except Exception as ex:
            return Response({'responseCode': -1, 'responseMessage': ex})


@api_view(['POST'])
def addNewProjectToClient(request, client_id=None):
    if request.method == 'POST':
        serializer = ProjectClientSerializers(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(takenByClient_id=client_id)
                return Response({'responseCode': 0, 'responseMessage': "Project added successfully",
                                 "responseData": serializer.data})
            except Exception as ex:
                return Response({'responseCode': -1, 'responseMessage': ex})

        return Response({'responseCode': 111, 'responseMessage': serializer.errors})


@api_view(['PATCH'])
def assignedProjectToUser(request, user_id=None):
    if request.method == 'PATCH':
        if UserInfo.objects.filter(id=user_id).exists():
            userObject = UserInfo.objects.get(id=user_id)
            serializer = UserInfoSerializers(userObject, data=request.data, partial=True)
            if serializer.is_valid():
                try:
                    serializer.save(assignedProject_id=request.data["assignedProject_id"])
                    return Response({'responseCode': 0, 'responseMessage': "Project assigned to user successfully"})
                except Exception as ex:
                    return Response({'responseCode': -1, 'responseMessage': ex})

        else:
            return Response({'responseCode': 111, 'responseMessage': "No user with given username exist"})

        return Response({'responseCode': 111, 'responseMessage': serializer.errors})
