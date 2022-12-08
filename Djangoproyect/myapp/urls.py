from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('tasks/', views.tasks, name="tasks"),
    path('projects/', views.projects, name="projects"),
    path('create-task/', views.create_task, name="create_Task"),
    path('crearnuevoprojecto/', views.create_Project, name="create_Project"),
]   