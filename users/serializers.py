from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from school.serializers import FollowingSerializer
from users.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token


class UserSerializer(serializers.ModelSerializer):
    following = FollowingSerializer(source=f'following_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'following', ]
