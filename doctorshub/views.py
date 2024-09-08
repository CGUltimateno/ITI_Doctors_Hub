from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Doctor, Specialization, Area
from .forms import UserRegisterForm, SearchForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


@login_required
def home(request):
    form = SearchForm()
    return render(request, 'home.html', {'form': form})


@login_required
def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            specialization = form.cleaned_data['specialization']
            area = form.cleaned_data['area']
            doctors = Doctor.objects.filter(specialization=specialization, area=area)
            return render(request, 'search.html', {'doctors': doctors})
    return redirect('home')


@login_required
def doctor_details(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, 'doctor_details.html', {'doctor': doctor})


def user_logout(request):
    logout(request)
    return redirect('login')
