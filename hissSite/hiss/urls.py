from django.urls import path

from . import views


urlpatterns = [ 
    path('userLoggedIn/', views.userLoggedIn),
    path('login/', views.login),
]