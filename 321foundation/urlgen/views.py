from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from urlgen.models import UrlData
from datetime import date

# Create your views here.

# view for rendering the url generator logic
def makeurl(request):
    return render(request,'urlpage.html')


# view for render
def sharepoint(request,st,lesson):
    lesson = lesson

    obj=UrlData.objects.get(lesson=lesson)
    obj.hitcount+=1

    # hit counter logic
    obj.save()
    st = st.replace('`','/')
    return render(request,'urlsharepoint.html',context={"result":st,"lesson":lesson})

def result(request):

    if not request.user.is_authenticated:
        username = 'demo'
    else:
        username=request.user.username

    url = request.GET['url']
    lesson = request.GET['lesson']
    url = url.replace('/','`')
    modified = "http://localhost:8000/urlmagic/sharepoint/"+lesson+'/'+ url
    today = date.today()


    checkobj=UrlData.objects.filter(urlgenerated=modified).filter(dateofhits=today).count()

    if not checkobj:
        obj = UrlData(school=username,lesson=lesson,urlgenerated=modified,dateofhits=today)
        obj.save()

    # checking for already object else push to the data base


    # # TODO: this website-domain should be replaced and

    return render(request,'urlresult.html',context={"result":modified})
