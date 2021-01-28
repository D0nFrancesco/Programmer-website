from django.shortcuts import render
from django.views.generic import TemplateView

# this is deffinitly not final
def index(request, path=''):
    return render(request, template_name='index.html')
