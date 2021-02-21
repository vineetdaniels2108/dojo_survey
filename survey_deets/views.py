from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse("getting ready to create form")

def home(request):
    return render(request, 'home.html')

def display(request):
    context = {
        'name' : request.POST ['name'],
        'location': request.POST['location'],
        'lang' : request.POST['lang'],
        'comment' : request.POST['comment'],
    }
    return render(request, 'display.html', context)
