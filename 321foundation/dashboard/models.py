from django.db import models
from urlHits.models import uniqueContent

# Create your models here.

class numberDailySchoolViews(models.Model):
	content_name = models.ForeignKey(uniqueContent,default = 1,on_delete = models.SET_DEFAULT)
	school_name = models.CharField(max_length = 200)
	date = models.DateField(auto_now = True)
	views = models.IntegerField()

class numberTeacherViews(models.Model):
	school_name = models.CharField(max_length = 200)
	date = models.DateField(auto_now = True)
	views = models.IntegerField()
