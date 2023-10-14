from django.contrib.auth.models import AbstractUser
from django.db import models
from secrets import token_hex
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    pass