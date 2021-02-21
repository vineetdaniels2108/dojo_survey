from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse("getting ready to create form")

def home(request):
    return render(request, 'home.html')

def formsubmission(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['lang'] = request.POST['lang']
    request.session['comment'] = request.POST['comment']    
    return redirect('/display')

def display(request):
    context = {
        'name' : request.session ['name'],
        'location': request.session['location'],
        'lang' : request.session['lang'],
        'comment' : request.session['comment'],
    }
    return render(request, 'display.html', context)
