
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    

class MyNimapInfo(models.Model):
    client_name=models.CharField(null=True,max_length=200)
    project = models.CharField(null=True,max_length=100)
    project_created=models.CharField(null=True,max_length=100)
    date = models.DateField()

class Clientinfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

    


