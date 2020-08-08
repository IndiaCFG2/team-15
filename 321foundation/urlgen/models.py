from django.db import models

class UrlData(models.Model):

   school = models.CharField(max_length = 50)
   lesson = models.CharField(max_length = 50)
   urlgenerated = models.CharField(max_length=255)
   hitcount = models.IntegerField(default=0)
   dateofhits = models.DateTimeField()

   def __str__(self):
      return self.lesson

