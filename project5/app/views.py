from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':10,'b':20}
    return render(request,'condition.html',context=d)


def loop(request):
    d={'name':'Animesh'}
    return render(request,'loop.html',context=d)