from django.shortcuts import render
from django.http import HttpResponse
import rest_framework

from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return TemplateView.as_view(template_name="index.html")
