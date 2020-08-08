
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AdminUser(models.Model):
	adminname = models.CharField(max_length = 20,unique = True);
	password = models.CharField(max_length = 20,unique = True);
	
class School(models.Model):
	SchoolName = models.CharField(max_length = 40,unique = True);
	PhoneNumber = models.CharField(max_length = 40,unique = True);
	Board = models.CharField(max_length = 40,unique = True);
	Password = models.CharField(max_length = 20,unique = True);
	#ConfirmPassword = models.CharField(max_length = 20,unique = True);
