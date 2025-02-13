from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    user_bio = models.TextField()
    user_profile_image = models.ImageField(upload_to='profile_custom')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','username']  # Add 'phone_number' to REQUIRED_FIELDS

    objects = UserManager()  # Assign the custom UserManager to the objects attribute