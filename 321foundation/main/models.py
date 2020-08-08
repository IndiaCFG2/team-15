from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class SchoolReq(models.Model):
	schoolname = models.CharField(max_length = 20,unique = True);
	#link = models.CharField(max_length = 20,unique = True);

    #created_at = models.TimeField(_(u"Conversation Time"), auto_now_add=True, blank=True);
	