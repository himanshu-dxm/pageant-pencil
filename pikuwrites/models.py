from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class IpModel(models.Model):
    ip=models.CharField(max_length=100)
    
    def __str__(self):
        return self.ip

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Author")
    body = models.TextField()
    type = models.CharField(max_length=255,default="poem")
    likes = models.ManyToManyField(IpModel,related_name="poem_like",blank=True)
    language = models.CharField(max_length=255,default="hindi")
    image = models.ImageField(upload_to='media')
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def total_likes(self):
        return self.likes.count()