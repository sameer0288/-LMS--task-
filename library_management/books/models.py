# books/models.py

from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    college = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
