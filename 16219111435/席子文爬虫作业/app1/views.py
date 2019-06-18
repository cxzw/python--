from django.shortcuts import render
from  app1.h import gk
from app1.models import app1
# Create your views here.
def gettitle(request):
    if app1.objects.count()==0:
        l=gk()
        for i in l:
            temp = app1(title=i)
            temp.save()
    ll=app1.objects.all()
    return render(request,'index.html',{'li':ll})