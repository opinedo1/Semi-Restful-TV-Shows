from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def edit(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'edit.html', context)

def view(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'view.html', context)