from django.db import models


# Create your models here.

class numberDailySchoolViews(models.Model):
	content_name = models.CharField(max_length = 200)
	school_name = models.CharField(max_length = 200)
	date = models.DateField(auto_now = True)
	views = models.IntegerField()

class numberTeacherViews(models.Model):
	school_name = models.CharField(max_length = 200)
	date = models.DateField(auto_now = True)
	views = models.IntegerField()
