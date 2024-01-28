from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
services = Service.objects.all()
portfolios = Portfolio.objects.all()
feedbacks = Feedback.objects.all()
blogs = Blog.objects.all()
team = Team.objects.all()

context = {
        'services': services,
        'portfolios': portfolios,
        'feedbacks': feedbacks,
        'blogs': blogs,
        'team':team
    } 
def index(request):
    return render(request, 'index.html', context)

def saveFeedback(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        feedbackform=SaveFeedback(name=name,email=email,message=message)
        feedbackform.save()
        messages.success(request,"Feedback Submitted Successfully")
    return render(request, 'index.html', context)

def subscribe(request):
    if request.method=='POST':
        email=request.POST.get('email')
        subscribe=Subscribe(email=email)
        subscribe.save()
        messages.success(request,"Subscribed Successfully")
    return render(request, 'index.html', context) 

def no_info(request):
      return render(request, 'no_info.html')