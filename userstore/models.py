from datetime import datetime

from django.core.validators import EmailValidator
from django.db import models




# Create your models here.
class UserCredentials(models.Model):
	email=models.CharField(max_length=30,null=False,unique=True,validators=[EmailValidator])
	password=models.CharField(max_length=200,null=False)
#	age=models.IntegerField(null=True,blank=True)

	def __str__(self):
		return self.email,self.password
