from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=50,default='',null=False)
    img = models.ImageField(upload_to="categpry_img")
    def __str__(self):
        return f"{self.name}"

class item(models.Model):
    type = models.ForeignKey(category,related_name='type',on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    dis = models.TextField(max_length=1000,null=True,blank=True)
    price = models.FloatField()
    img1 = models.ImageField(upload_to="item_img")
    img2 = models.ImageField(upload_to="item_img",blank=True,null=True)
    is_buyed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User , related_name='created_by',on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    off = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name}"
    

class likeItem(models.Model):
    post_id = models.IntegerField()
    username = models.CharField(max_length=50)
