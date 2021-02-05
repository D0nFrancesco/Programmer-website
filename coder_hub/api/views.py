from django.shortcuts import render
from django.http import HttpResponse
import rest_framework

from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return TemplateView.as_view(template_name="index.html")

# Home page api endpoint
def home(request): 
    return TemplateView.as_view(template_name="index.html")

# Social page api endpoint
def social(request):
    return TemplateView.as_view(template_name="index.html")

# Project page api endpoint
def project(request):
    return TemplateView.as_view(template_name="index.html")

# Newproject page api endpoint
def newproject(request):
    return TemplateView.as_view(template_name="index.html")


# Settigns page api endpoint
def settings(request):
    return TemplateView.as_view(template_name="index.html")



# Login page api endpoint
def login(request):
    return TemplateView.as_view(template_name="index.html")


# Register page api endpoint
def register(request):
    return TemplateView.as_view(template_name="index.html")

# Logout page api endpoint
def logout(request):
    return TemplateView.as_view(template_name="index.html")











