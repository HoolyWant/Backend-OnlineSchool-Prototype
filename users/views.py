from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from rest_framework_simplejwt.views import TokenObtainPairView

from school.permissions import IsStaff
from users.models import User
from users.serializers import MyTokenObtainPairSerializer, UserSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRetrieveApi(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [IsStaff | IsAdminUser]


