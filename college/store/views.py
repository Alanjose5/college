from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth

from .models import bio


# Create your views here.
def demo(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['txt']
        Email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        user = User.objects.create_user(username=name, password=password, email=Email)
        user.save()
        messages.info(request, 'Registerd successfully')
    return render(request, 'relo.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('bio')
        else:
            messages.info(request, 'INVALID PASSWORD')
            return redirect('log')
    return render(request, 'relo.html')


def detail(request):
    if request.method == 'POST':
        Name = request.POST.get('Name', )
        DOB = request.POST.get('DOB', )
        Age = request.POST.get('Age', )
        Gender = request.POST.get('Gender', )
        Phone = request.POST.get('Phone', )
        Email = request.POST.get('Email', )
        Address = request.POST.get('Address', )
        Department = request.POST.get('Department', )
        Material = request.POST.get('Material', )
        bio1 = bio(Name=Name, DOB=DOB, Age=Age, Gender=Gender, Phone=Phone, Email=Email, Address=Address,
                   Department=Department, Material=Material)
        bio1.save()

        messages.info(request, 'successfully submitted')
    return render(request, 'bio.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
