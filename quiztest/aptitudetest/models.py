from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user



class Hrlogin(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, null=True ,blank=True)
    auth_token = models.CharField(max_length=100 , null=True ,blank=True)
    is_verified = models.BooleanField(default=False, null=True ,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True ,blank=True)
    

class Department(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Role(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Topic(models.Model):
    Role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name


class Test(models.Model):
    department = models.CharField(max_length=50, null=True ,blank=True)
    role = models.CharField(max_length=50, null=True ,blank=True)
    topic = models.CharField(max_length=50, null=True ,blank=True)
    question = models.CharField(max_length=255, null=True ,blank=True)
    answeroption=models.CharField(max_length=200,blank=True,null=True)
    a = models.CharField(max_length=50, null=True ,blank=True)
    b = models.CharField(max_length=50, null=True ,blank=True)
    c = models.CharField(max_length=50, null=True ,blank=True)
    d = models.CharField(max_length=50, null=True ,blank=True)
    # cat=(('a','a'),('b','b'),('c','c'),('d','d'))
    

    def __str__(self):
        return self.department


class AptituteTest(models.Model):
    question_number = models.IntegerField(blank=True,null=True)
    testqueestion = models.ForeignKey(Test, on_delete=models.DO_NOTHING, related_name='test_question')
    candidate = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='candidate', blank=True, null=True)
    started_on = models.DateTimeField()
    ended_on = models.DateTimeField()

    def __str__(self):
        return f'Question {self.testqueestion.question} asked to {self.candidate.username}'


