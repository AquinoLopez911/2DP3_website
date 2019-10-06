from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
import datetime
import random


def home_page(request):
    if 'id' not in request.session:
        return redirect('/login')
    else:
        number_of_projects = Project.objects.count()

        p1 = int(random.random()*number_of_projects)+1
        card1 = Project.objects.get(id = p1)
        p2 = int(random.random()*number_of_projects)+1
        card2 = Project.objects.get(id = p2)
        p3 = int(random.random()*number_of_projects)+1
        card3 = Project.objects.get(id = p3)
        p4 = int(random.random()*number_of_projects)+1
        card4 = Project.objects.get(id = p4)

        cards = [card1, card2, card3, card4]
        for card in cards:
            print('*'*80)
            print(card)
            print('*'*80)
        #didnt pass in context so i did the most
        context = {
            'cards' : cards,
            'card1' : card1,
            'card2' : card2,
            'card3' : card3,
            'card4' : card4,
        }
        return render(request, 'home_page.html', context)

def project_description(request, number):
    project_displayed = Project.objects.get(id=number)

    context = {
        'project' : project_displayed
    }
    return render(request, 'project_info.html', context)


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


def register_action(request):
    if request.POST:
        print(request.POST)
        errors_from_Validator = User.objects.registration_validator(request.POST)
        if len(errors_from_Validator) > 0:
            for key, value in errors_from_Validator.items():
                messages.error(request, value)
            return redirect('/register')
        else:
            hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

            user = User.objects.create(name=request.POST['name'], alias=request.POST['username'], email=request.POST['email'].lower(), password=hash1.decode() )
            print(f"created user: {user}")

            request.session['id'] = user.id

            user = User.objects.get(id = request.session['id'])
            return redirect('/')
        

def login_action(request):
    login_errors = User.objects.login_validator(request.POST)
    if len(login_errors) > 0:
        for key, value in login_errors.items():
            messages.error(request, value)
        return redirect('/')   
    request.session['id'] = User.objects.filter(email = request.POST['email'].lower())[0].id
    request.session['name'] = User.objects.filter(email = request.POST['email'].lower())[0].name
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')