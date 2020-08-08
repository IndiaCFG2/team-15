from django.db import models
from dashboard.models import numberDailySchoolViews

# Create your models here.

class uniqueContent(models.Model):
	content_name = models.CharField(max_length = 200)
	school_name = models.CharField(max_length = 200)
	content_unique_link = models.ForeignKey(numberDailySchoolViews,default = 1,on_delete = models.SET_DEFAULT)

	def __str__(self):
		return self.content_name



