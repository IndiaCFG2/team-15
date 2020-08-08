from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.


# view for rendering the url generator logic
def makeurl(request):
    return render(request,'urlpage.html')


# view for render
def sharepoint(request,st,lesson):
    lesson = lesson
    st = st.replace('`','/')
    return render(request,'urlsharepoint.html',context={"result":st,"lesson":lesson})

def result(request):

    url = request.GET['url']
    lesson = request.GET['lesson']

    url = url.replace('/','`')

    modified = "http://localhost:8000/urlmagic/sharepoint/"+lesson+'/'+ url

    # # TODO: this website-domain should be replaced and

    return render(request,'urlresult.html',context={"result":modified})
