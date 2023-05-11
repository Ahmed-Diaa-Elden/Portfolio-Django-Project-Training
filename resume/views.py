from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def resume(request):
    # today = datetime.datetime.now()
    return render(request, "resume.html")