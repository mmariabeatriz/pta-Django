from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import Classes

def index(request):
    queryset = Classes.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'index.html', context)

