from django.shortcuts import render
from django.http import HttpResponse
from Home.models import teacher

# Create your views here.
def first_line(request):
    return HttpResponse("Hey there this is Hasan")
def home(request):
    return render(request, 'Home/Home.html')

def teacher_info(request):
    teach = teacher.objects.all()
    return render(request, 'Home/t.html', {"tec": teach})