from django.contrib.auth.models import AbstractUser
from django.db import models
from secrets import token_hex
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    # verify_token = models.CharField(default=token_hex(6))
    # is_active = models.BooleanField(default=False, verbose_name='активен')
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
