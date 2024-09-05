from django.shortcuts import render

# Create your views here.
def london (request):
    return render(request,'london.html')

def uk(request):
    return render(request,'uk.html')