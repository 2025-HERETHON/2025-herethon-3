from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):
    user_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=50)

    username = None  # 기존 username 제거

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['name', 'email']

