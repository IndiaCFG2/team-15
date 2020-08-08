from django.shortcuts import render
from django.views.generic import TemplateView
from .models import uniqueContent
from .models import numberDailySchoolViews

# Create your views here.

currURL = ''


def inc_views(currURL):
 	for content in uniqueContent.all():
 		if currURL == content.content_unique_link:
 			matching_numberDailySchoolViews = numberDailySchoolViews.filter(content_name__content_unique_link=currURL)
 			matching_numberDailySchoolViews.views += 1
 			




