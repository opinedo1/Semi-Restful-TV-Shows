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

def new(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    elif request.method == 'POST':
        Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            description = request.POST['description']  
        )
        show_id = Show.objects.last().id
        return redirect("/shows/{}".format(show_id))

def update(request, show_id):
    if request.method == 'GET':
        return redirect('/shows')
    this_show = Show.objects.get(id=show_id)
    this_show.title = request.POST['title']
    this_show.release_date = request.POST['release_date']
    this_show.network = request.POST['network']
    this_show.description = request.POST['description']
    this_show.save()
    return redirect('/shows')
    