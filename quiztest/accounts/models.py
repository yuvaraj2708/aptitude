from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Person(models.Model):
    department = models.CharField(max_length=50, null=True ,blank=True)
    role = models.CharField(max_length=50, null=True ,blank=True)
    topic = models.CharField(max_length=50, null=True ,blank=True)
    question = models.CharField(max_length=255, null=True ,blank=True)
    answeroption = models.CharField(max_length=50, null=True ,blank=True)
    a = models.CharField(max_length=50, null=True ,blank=True)
    b = models.CharField(max_length=50, null=True ,blank=True)
    c = models.CharField(max_length=50, null=True ,blank=True)
    d = models.CharField(max_length=50, null=True ,blank=True)
    

