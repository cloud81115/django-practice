from django.shortcuts import render

# Create your views here.
def home(request):
	context={
	'text':'python'

	}
	return render(request,"home.html", context)

def contact(request):
	return render(request,"contact.html",{})