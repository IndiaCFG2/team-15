from django.db import models

class urlMap(models.Model):
   lesson = models.CharField(max_length=200)
   url = models.CharField(max_length=200)