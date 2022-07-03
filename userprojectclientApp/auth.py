from django.contrib.auth.models import update_last_login
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from userprojectclientApp.models import UserInfo
from userprojectclientApp.serializers import UserInfoSerializers


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        try:
            serializer.is_valid(raise_exception=False)
            user = serializer.validated_data['user']
        except:
            return Response({'responseCode': 110, 'responseMessage': 'Wrong Username/Password'})

        update_last_login(None, user)
        print("user:", user)

        userInfo = UserInfo.objects.filter(id=user.id)
        serializer = UserInfoSerializers(userInfo, many=True)

        Token.objects.filter(user=user).delete()
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {'responseCode': 0, 'responseMessage': 'Success', 'userToken': token.key, 'userData': serializer.data})
