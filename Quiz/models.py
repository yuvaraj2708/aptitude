from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your models here.
from django.db import models
 
# Create your models here.
class Test(models.Model):
    department =models.CharField(max_length=55,null=True,blank=True)
    role =models.CharField(max_length=55,null=True,blank=True)
    topic =models.CharField(max_length=55,null=True,blank=True)
    question = models.CharField(max_length=200,null=True)
    answeroption =models.CharField(max_length=55,null=True,blank=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.department)
        
class login(models.Model):
     username = models.CharField(max_length=100)
     password = models.CharField(max_length=100)

     def __str__(self):
         return self.username

   
class Depart(models.Model):
    IT ='IT'
    ACCOUNTS = 'ACCOUNTS'
    SALES = 'SALES'
    CHOOSE_DEPARTMENT = [
        (IT,'IT'),
        (ACCOUNTS,'ACCOUNTS'),
        (SALES,'SALES'),
    ]  
    Department_of = models.CharField(max_length=225,choices=CHOOSE_DEPARTMENT,default=IT)
       
    DEVELOPER ='DEVELOP'
    ACCOUNTANT ='ACCOUNT'
    MARKETING = 'MARKET'
    ROLE_CHOICE =[
        (DEVELOPER,'DEVELOPER'),
        (ACCOUNTANT,"ACCOUNTANT"),
        (MARKETING,'MARKETING'),
    ]
    Role_is =models.CharField(max_length=225,choices=ROLE_CHOICE,default=DEVELOPER)
    
    python = models.BooleanField("python",default=True)
    C =models.BooleanField("C++",default=True)
    Account = models.BooleanField("Accountancy",default=False)
    Product = models.BooleanField(" Product_Awareness",default=False)

    
    def is_upperclass(self):
        return self.Department_of in {self.ACCOUNTS,self.SALES}
     
#samples

