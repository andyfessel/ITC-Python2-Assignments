from django.urls import path
from . import views
urlpatterns=[
    path('', views.index,name='index'),
    path('restype/', views.restype, name='restype'),
    path('meetingtitle/', views.meetingtitle, name='meetingtitle'),
    path('meetingid/', views.meetingid, name='meetingid'),
    path('newMeeting/', views.newMeeting, name='meetingform'),
    path('newResource/', views.newResource, name='resourceform'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]   
