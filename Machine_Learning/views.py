from django.shortcuts import render

# Create your views here.
def machine(request):
    wh = {'what' : 'Machine Learning'}
    return render(request, "Machine_Learning/Machine.html", context= wh)

def dt(request):
    return render(request, 'Machine_Learning/dt.html')
def knn(request):
    return render(request, 'Machine_Learning/knn.html')