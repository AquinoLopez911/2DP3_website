from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path("projects/<int:number>", views.project_description),
    path("login", views.login),
    path("login_action", views.login_action),
    path("register", views.register),
    path("register_action", views.register_action),
    path('logout', views.logout),
] 