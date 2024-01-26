from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
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

    return render(request, 'index.html', context)