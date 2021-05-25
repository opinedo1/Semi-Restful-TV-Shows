from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def index(request):
    return redirect('/shows')

# For displaying all the existing shows in our database
def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

# Adding form validation to edit page
def edit(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'edit.html', context)

# Displays the content for an existing tv show
def view(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'view.html', context)

# Creayes a new show in our database and validates all the fields
def new(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    elif request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for (key, value) in errors.items():
                messages.error(request, value)
            return redirect('/shows/create')
        else:
            Show.objects.create(
                title = request.POST['title'],
                network = request.POST['network'],
                release_date = request.POST['release_date'],
                description = request.POST['description']
            )
            show_id = Show.objects.last().id
            return redirect("/shows/{}".format(show_id))

# Updates an existing show and validates data entry
def update(request, show_id):
    if request.method == 'GET':
        return redirect('/shows')
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for (key, value) in errors.items():
                messages.error(request, value)
        return redirect('/shows/{}/edit'.format(show_id))
    else:
        this_show = Show.objects.get(id=show_id)
        this_show.title = request.POST['title']
        this_show.release_date = request.POST['release_date']
        this_show.network = request.POST['network']
        this_show.description = request.POST['description']
        this_show.save()
        return redirect('/shows')

# Deletes a single show that is selected
def delete(request, show_id):
    if request.method == 'GET':
        return redirect('/shows')
    Show.objects.get(id=show_id).delete()
    return redirect('/shows')