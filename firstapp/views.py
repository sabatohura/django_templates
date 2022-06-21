from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from .models import Trainee

# Create your views here.

def testview(request):
    return HttpResponse("<h1>This is test</h1>")

def all_trainee(request):
    trainees = Trainee.objects.all()
    context = {
        'trainees':trainees,
    }
    return render(request,'index.html',context)
