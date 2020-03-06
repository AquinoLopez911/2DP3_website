from django.shortcuts import render, redirect
from .models import Project, User
from django.contrib import messages
import bcrypt
import datetime
import random


def home_page(request):
    if 'id' not in request.session:
        return redirect('/login')
    else:
        #find all unstarted projects
        #ex: obj1  obj4  obj6  obj7  obj9
        not_started_projects = Project.objects.filter(started="False")
        print(not_started_projects)

        #number of unstarted projects
        # 5
        number_of_projects = not_started_projects.count()

        #get 4 random id of unstarted projects from the DB
        # arr to hold location of project in not_started_projects arr
        #ex: obj1 obj9 obj6 obj4 
        final_project_arr = []

        # need 4 unique ids
        while(len(final_project_arr) < 4):
            # randomly generated number  0 - number_of_projects - 1
            project_index = random.randint(0, number_of_projects - 1)

            # check if object at index "project_index" from not_started_projects arr is in the final_project_arr
            # adds object to final_project_arr if not already added
            if(not_started_projects[project_index] not in final_project_arr):
                final_project_arr.append(not_started_projects[project_index])
    


        context = {

            'final_project_arr' : final_project_arr,

        }
        return render(request, 'home_page.html', context)



def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

        

def login_action(request):
    login_errors = User.objects.login_validator(request.POST)
    if len(login_errors) > 0:
        for key, value in login_errors.items():
            messages.error(request, value)
        return redirect('/')   
    request.session['id'] = User.objects.filter(email = request.POST['email'].lower())[0].id
    request.session['name'] = User.objects.filter(email = request.POST['email'].lower())[0].name
    return redirect('/')


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

def logout(request):
    request.session.clear()
    return redirect('/')
    
# loads the page with the specific project info
def project_description(request, number):
    project_displayed = Project.objects.get(id=number)

    context = {
        'project' : project_displayed
    }
    return render(request, 'project_info.html', context)

# marks specific project as started
def start_project(request, number):
    project_displayed = Project.objects.get(id=number)

    project_displayed.started = True

    project_displayed.save()

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