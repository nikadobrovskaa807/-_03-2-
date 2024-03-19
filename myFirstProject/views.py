from django.shortcuts import render, HttpResponse


# Create your views here.


def index (request):
    return HttpResponse("<h1> hello, World!</h1>")


def Second_page (request):
    return render(request, 'Second_page.html')

def page1 (request):
    return render(request, 'page1.html')

def page2 (request):
    return render(request, 'page2.html')

def page3 (request):
    return render(request, 'page3.html')

def page4 (request):
    return render(request, 'page4.html')

