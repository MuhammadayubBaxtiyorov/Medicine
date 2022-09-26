from django.shortcuts import render,redirect, get_object_or_404
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login as dj_login
from . import forms
from .models import *
from .models import Disease

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was create for ' + username)
            return redirect('login')
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            dj_login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Username or Password is incorrect')

        
    context = {}
    return render(request, 'login.html', context)



def home(request):
    return render(request, 'home.html')

def add(request):
    form = forms.DiseaseForm()
    if request.method == 'POST':
        form = forms.DiseaseForm(request.POST)
        if form.is_valid():
            book = form.save(commit = False)
            book.user = request.user
            book.save()
            return redirect('profile')
    context = {'form': form}

    return render(request, 'add.html', context)

def delete(request, pk):
    form = Disease.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('profile')
    context = {'item':form}
    return render(request, 'delete.html', context)


def profile(request):
    user = request.user
    diseases = Disease.objects.filter(user=user)

    context = {'addform': diseases}

    return render(request, 'profile.html', context)

def drug(request, pk):
    form = forms.MedicineForm()
    if request.method == 'POST':
        form = forms.MedicineForm(request.POST)
        if form.is_valid():
            disease = get_object_or_404(Disease.objects.filter(id=pk))
            name = request.POST.get('name')
            desc = request.POST.get('desc')
            Medicine.objects.create(name=name, desc=desc, disease=disease)            
            return redirect('drug', pk=pk)
    context = {
        'form': form,
        'medicine': Medicine.objects.filter(disease_id=pk)
    }
    return render(request, 'drug.html', context)