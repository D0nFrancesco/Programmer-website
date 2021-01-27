from django.shortcuts import render
import rest_framework

# Create your views here.
def index(request):
    return render(request, "index.html")
