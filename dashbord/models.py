from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class UserInfo(models.Model):
    user = models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    gender = models.CharField(max_length=6,choices=[('Male','Male'),('Famle','Famle')])
    profile = models.ImageField(upload_to='usersProfile',default='user.jpg',blank=True)
    bio = models.TextField(max_length=200,blank=True)

    github = models.CharField(max_length=100,null=True)
    telegram = models.CharField(max_length=100,null=True)
    website = models.CharField(max_length=100,null=True,)
    instagram = models.CharField(max_length=100,null=True)
    def __str__(self):
        return f"{self.user.username}"

class Follow(models.Model):
    follower = models.CharField(max_length=150)
    user = models.CharField(max_length=150)
    def __str__(self):
        return f"{self.follower}"


class typeBanner(models.Model):
    name = models.CharField(max_length=70)
    def __str__(self):
        return f"{self.name}"

class Banner(models.Model):
    type = models.ForeignKey(typeBanner,related_name="type" , on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    dis = models.TextField(max_length=150,blank=True)
    img = models.ImageField(upload_to="Banners")
    def __str__(self):
        return f"{self.name}"

    