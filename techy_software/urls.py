from django.urls import path
from .views import *
# from techy_software import views

app_name = 'techy_software'
urlpatterns = [
    path('', index, name='index'),
    path('saveFeedback/', saveFeedback, name="saveFeedback"),
    path('subscribe/', subscribe, name="subscribe"),
    path('NoInformationAvailable', no_info, name="no_info"),
]