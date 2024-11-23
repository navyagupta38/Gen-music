from django.shortcuts import render,HttpResponse # install HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("this is homepage")
    context =  {  #context :- set of variables
        "variable1" : "HArrry is great",  # variable :- it is a variable,
        "variable2" : "Rohan is "
    }
    # messages.success(request, "this is a test message")
    return render(request, 'index.html', context)

def about(request): 
    return render(request, 'about.html')
    # return HttpResponse("This is aboutpage")

def services(request):
    return render(request, 'services.html')

    # return HttpResponse("this is service page")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())    # :- given above contact ka object ( to save a object)
        contact.save()
        messages.success(request, 'Your message has been sent!') # :- to pop up message when mesage has been submit
    return render(request, 'contact.html')

    # return HttpResponse("this is contact page")


