from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('project/', views.projectname, name='projectname'),
    path('newProject/', views.newProject, name='projectform'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
   
]