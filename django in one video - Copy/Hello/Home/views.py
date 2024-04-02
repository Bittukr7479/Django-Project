from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    messages.success(request, "this is a test message")
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
    # return HttpResponse("This is about page")

def services(request):
    return render(request, "services.html")
    # return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name= name, email= email, phone= phone, date= datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.") 

    return render(request, "contact.html")
    # return HttpResponse("This is contact page")