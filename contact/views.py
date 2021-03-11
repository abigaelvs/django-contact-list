from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home_view(request):
    profiles = Profile.objects.all()
    search_input = request.GET.get('search-area')

    if search_input:
        profiles = Profile.objects.filter(name__icontains=search_input)
    else:
        profiles = Profile.objects.all()
        search_input = ''
    
    context = {
        'profiles': profiles,
        'search_input': search_input
    }
    return render(request, 'index.html', context)


def contact_detail(request, slug):
    profile = Profile.objects.get(slug=slug)
    context = {
        'profile': profile,
    }
    return render(request, 'contact-detail.html', context)


def add_contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:home')

    context = {
        'form': form,
    }
    return render(request, 'add-contact.html', context)

def edit_contact(request, slug):
    profile = Profile.objects.get(slug=slug)
    form = ContactForm(instance=profile)

    if request.method == 'POST':
        form = ContactForm(request.POST or None, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('contact:home')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'edit-contact.html', context)


def delete_contact(request, slug):
    profile = Profile.objects.get(slug=slug)
    
    if request.method == 'POST':
        profile.delete()
        return redirect('contact:home')
    context = {
        'profile': profile,
    }
    return render(request, 'delete-contact.html', context)



