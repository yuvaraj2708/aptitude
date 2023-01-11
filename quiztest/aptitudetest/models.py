from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user

class Test(models.Model):
    department = models.CharField(max_length=50, null=True ,blank=True)
    role = models.CharField(max_length=50, null=True ,blank=True)
    topic = models.CharField(max_length=50, null=True ,blank=True)
    question = models.CharField(max_length=255, null=True ,blank=True)
    answeroption = models.CharField(max_length=50, null=True ,blank=True)
    a = models.CharField(max_length=50, null=True ,blank=True)
    b = models.CharField(max_length=50, null=True ,blank=True)
    c = models.CharField(max_length=50, null=True ,blank=True)
    d = models.CharField(max_length=50, null=True ,blank=True)
    def __str__(self):
        return self.department

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
    Department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Topic(models.Model):
    Role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
  
    # IT = 'IT'
    # ACCOUNTS = 'ACCOUNTS'
    # SALES = 'SALES'
    # CHOOSE_DEPARTMENT = [
    #     (IT , 'IT'),
    #     (ACCOUNTS , "ACCOUNTS"),
    #     (SALES , "SALES"),
    # ]
    # Department_of = models.CharField(max_length=225,choices=CHOOSE_DEPARTMENT,default=IT)
    # DEVELOPER='DEVELOPER'
    # ACCOUNTANT ='ACCOUNTANT'
    # PYTHON = 'PYTHON'
    # ACCOUNTANCY = 'ACCOUNTANCY'
    # CLIENT_AND_SUPPORT = 'CLIENT AND SUPPORT'
    # MARKETING = 'MARKETING'

    # IT = models.CharField(max_length=50,null=True,blank=True)
    # IT =[
    #         (DEVELOPER,'DEVELOPER'),
    #         (ACCOUNTANT,'ACCOUNTANT'),
    #         (MARKETING,'MARKETING'),
    #     ]
    # DEVELOPER = models.CharField(max_length = 50,null = True,blank = True)
    # DEVELOPER =[ 
    #         (PYTHON,'python'),
    #         (ACCOUNTANCY,'ACCOUNTANCY'),
    #         (CLIENT_AND_SUPPORT,'CLIENT AND SUPPORT'),
    #     ]
    # Choose_Field = models.CharField(max_length=225,choices=IT,default=DEVELOPER)
    # Domin = models.CharField(max_length=225,choices=DEVELOPER,default=PYTHON)
    # ACCOUNTS = models.CharField(max_length=50,null=True,blank= True)
   
    
    # ACCOUNTANT = models.CharField(max_length=50,null =True,blank=True)
    # SALES = models.CharField(max_length=50 ,null = True,blank = True)
    # MARKETING=models.CharField(max_length=50,null=True,blank=True)
    
    