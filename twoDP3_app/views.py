from django.shortcuts import render, redirect
from .models import Project, User
from django.contrib import messages
import bcrypt
import datetime
import random

# RENDER FUNCTIONS

# renders home_page.html
# if no id is the session, user will be redirected to login page
#
# the home page has 4 "cards" at the bottom of the page
# the 4 cards require unique Projects from the DB to be passed to each
def home_page(request):
    if 'id' not in request.session:
        return redirect('/login')
    else:
        #find all unstarted projects from the DB
        not_started_projects = Project.objects.filter(started="False")

        #number of unstarted projects
        number_of_projects = not_started_projects.count()

        #arr to hold the 4 random projects to be sent to the cards in the front end 
        final_project_arr = []

        # adding 4 unique Projects to final_project_arr
        while(len(final_project_arr) < 4):
            #  generate random number in the range of:  0 - number_of_projects - 1
            project_index = random.randint(0, number_of_projects - 1)

            # checks if object at index "project_index" from not_started_projects arr is in the final_project_arr
            # adds object to final_project_arr if not already added
            if(not_started_projects[project_index] not in final_project_arr):
                final_project_arr.append(not_started_projects[project_index])
    
        context = {

            'final_project_arr' : final_project_arr,

        }
        return render(request, 'home_page.html', context)


# renders 'login.html'
def login(request):
    return render(request, 'login.html')

# renders 'Register.html'
def register(request):
    return render(request, 'register.html')
    

# renders project_info.html with the specific project info
def project_description(request, number):
    # query for the project with an ID that matches the number parameter 
    project_displayed = Project.objects.get(id=number)

    context = {
        'project' : project_displayed
    }
    return render(request, 'project_info.html', context)

def started_projects(request):
    startedProjects = Project.objects.filter(started = True)
   

    context = {
        'startedProjects' : startedProjects
    }

    return render(request, 'started_projects.html', context)

    

def completed_projects(request):
    completedProjects = Project.objects.filter(complete = True)
   
    context = {
        'completedProjects' : completedProjects
    }

    return render(request, 'completed_projects.html', context) 

        


# REDIRECT FUNCTIONS

# verifies the user attempting to login
def login_action(request):
    # send the users submited login post to login_validator
    login_errors = User.objects.login_validator(request.POST)

    # if erros are found in login_errors, add each on to messages.error to be passed to the front end
    if len(login_errors) > 0:
        for key, value in login_errors.items():
            messages.error(request, value)
        # redirects to login page and displays message.errors
        return redirect('/login') 


    # if no errors were found, query for the user with the email entered

    # OLD WAY
    # I MADE TWO CALLS TO DB 
    # request.session['id'] = User.objects.filter(email = request.POST['email'].lower())[0].id
    # request.session['name'] = User.objects.filter(email = request.POST['email'].lower())[0].name

    # NEW WAY
    # ONE CALL TO DB SAVED TO VARIABLE
    user = User.objects.filter(email = request.POST['email'].lower())[0]

    request.session['id'] = user.id
    request.session['name'] = user.name


    # redirect to home route
    return redirect('/')

# registers a new user if form post is valid
def register_action(request):
    # send the users submited login post to registration_validator
    errors_from_Validator = User.objects.registration_validator(request.POST)
     # if erros are found in login_errors, add each on to messages.error to be passed to the front end
    if len(errors_from_Validator) > 0:
        for key, value in errors_from_Validator.items():
            messages.error(request, value)
        # redirects to registration page and displays message.errors
        return redirect('/register')
    # if no errors are found in errors_from_Validator, 
    else:
        # create hash with password given by regerestring user
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        # add a new user to the User Table in DB 
        user = User.objects.create(name=request.POST['name'], alias=request.POST['username'], email=request.POST['email'].lower(), password=hash1.decode() )
        print(f"created user: {user}")

        # adding user ID to session 
        request.session['id'] = user.id

        # redirecting to home route
        return redirect('/')

# logs user out and redirects to login
def logout(request):
    # clears session (ID)
    request.session.clear()
    return redirect('/login')


# marks specific project as started and renders 'project_info.html'
def start_project(request, number):
    # query for the project with an ID that matches the number parameter 
    project_displayed = Project.objects.get(id=number)

    #change Projects 'started' property from false to true
    project_displayed.started = True

    # save changes
    project_displayed.save()

    context = {
        'project' : project_displayed
    }

    return render(request, 'project_info.html', context)
