from django.contrib.auth import user_logged_in
from django.contrib.auth.models import update_last_login
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView

from school.permissions import IsStaff
from users.models import User
from users.serializers import MyTokenObtainPairSerializer, UserSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class UserRetrieveApi(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsStaff | IsAdminUser]



