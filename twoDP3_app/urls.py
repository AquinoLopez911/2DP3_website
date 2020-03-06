from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path("projects/<int:number>", views.project_description),
    path('start_project/<int:number>', views.start_project),
    path('started_projects', views.started_projects),
    path('completed_projects', views.completed_projects),
    path("login", views.login),
    path("login_action", views.login_action),
    path("register", views.register),
    path("register_action", views.register_action),
    path('logout', views.logout),
] 


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)