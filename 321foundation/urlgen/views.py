from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from urlgen.models import UrlData
from datetime import date
import datetime
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


mockdata = {
  "users": [
    {
      "lesson": "loyola",
      "url": "https://www.webforefront.com/django/namedjangourls.html",
      "modified":"to be generated"
    },
    {
      "lesson": "snhhs",
      "url": "https://www.webforefront.com",
      "modified":"to be generated"
    },
        {
      "lesson": "sfrdd",
      "url": "https://www.webforddeefront.com",
      "modified":"to be generated"
    },
    
  ]
}


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["LittleFlower", "DPS", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='chart.html')
line_chart_json = LineChartJSONView.as_view()

# Create your views here.

# view for rendering the url generator logic 1
def makeurl(request):
    return render(request,'urlgenerator.html')


# view for render  2
def sharepoint(request,st,lesson):
    lesson = lesson

    obj=UrlData.objects.get(lesson=lesson)
    obj.hitcount+=1

    # hit counter logic
    obj.save()
    st = st.replace('`','/')
    return render(request,'urlsharepoint.html',context={"result":st,"lesson":lesson})


# render the modified url for the teacher to be shared with student using Whatsapp API
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

def rangechart(request):    
    return render(request,'rangechart.html')

def rangechartdata(request):

    startdate = str(request.GET['startdate'])
    enddate = str(request.GET['enddate'])

    sty=int(startdate[0:4])
    std=int(startdate[5:7])
    stm=int(startdate[8:])
    ety=int(enddate[0:4])
    etd=int(enddate[5:7])
    etm=int(enddate[8:])

    startdate = datetime.date(sty,std,stm)
    enddate = datetime.date(ety,etd,etm)

    a = UrlData.objects.filter(dateofhits__range=(startdate, enddate))

    context = {
        'startdate' : startdate,
        'enddate' : enddate,
        'data':a
    }


    return render(request,'rangechartdata.html',context=context)

def dburls(request):

    if not request.user.is_authenticated:
        username = 'demo'
    else:
        username=request.user.username
    data = mockdata['users']
    for i in range(len(data)):
        url = data[i]['url']
        lesson = data[i]['lesson']
        url = url.replace('/','`')
        today = date.today()
        data[i]['modified'] = "http://localhost:8000/urlmagic/sharepoint/"+lesson+'/'+ url
        checkobj=UrlData.objects.filter(urlgenerated=data[i]['modified']).filter(dateofhits=today).count()

        if not checkobj:
            obj = UrlData(school=username,lesson=lesson,urlgenerated=data[i]['modified'],dateofhits=today)
            obj.save() 
    context ={
        'data':data
    } 
    


    return render(request,'urlgenfromdb.html',context=context)






