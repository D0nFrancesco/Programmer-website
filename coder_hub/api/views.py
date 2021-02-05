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


def social(request):
    return TemplateView.as_view(template_name="index.html")


def project(request):
    return TemplateView.as_view(template_name="index.html")

def newproject(request):
    return TemplateView.as_view(template_name="index.html")

def settings(request):
    return TemplateView.as_view(template_name="index.html")


def login(request):
    return TemplateView.as_view(template_name="index.html")



def register(request):
    return TemplateView.as_view(template_name="index.html")


def logout(request):
    return TemplateView.as_view(template_name="index.html")











