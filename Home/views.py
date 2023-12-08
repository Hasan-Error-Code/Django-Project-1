from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_line(request):
    return HttpResponse("Hey there this is Hasan")
def home(request):
    return render(request, 'Home/Home.html')