from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
	time=datetime.datetime.now()
	return render(request, 'index.html',locals())

def about(request):
	return render(request, 'about.html',locals())