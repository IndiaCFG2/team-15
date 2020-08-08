from django.shortcuts import render
from .models import numberTeacherViews,numberDailySchoolViews

# Create your views here.

def dashboard_page(request):
	return render(
					request,
					'',
					context = {'student_views':numberDailySchoolViews.objects.all(),'teacher_views':numberTeacherViews.objects.all()}
				)

