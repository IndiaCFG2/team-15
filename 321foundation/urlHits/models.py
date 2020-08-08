from django.db import models

# Create your models here.

class uniqueContent(models.Model):
	content_name = models.CharField(max_length = 200)
	school_name = models.CharField(max_length = 200)
	content_unique_link=models.CharField(max_length = 200)


	def __str__(self):
		return self.content_name
