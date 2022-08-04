from django.db import models
from django.contrib.auth.models import AbstractUser 


# Create your models here.

class User(AbstractUser):
    #id = models.UUIDField()
    name = models.CharField(max_length = 200, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length = 200, unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    interest_one = models.CharField(max_length=200, null=True, blank=True)
    interest_two = models.CharField(max_length=200, null=True, blank=True)
    interest_three = models.CharField(max_length=200, null=True, blank=True)

    avatar = models.ImageField(null=True, default="avatar.svg", blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    logo = models.ImageField(null=True, default="avatar.svg", blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name        


class Job(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    industry = models.CharField(max_length=200, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    information = models.TextField()
    location = models.CharField(max_length=200)
    link = models.URLField(max_length=200, null=True)
    saved = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False) 

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name