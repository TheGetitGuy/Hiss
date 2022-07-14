from django.urls import path
from django.views.generic import RedirectView

from . import views


urlpatterns = [ 
    path('userLoggedIn/', views.userLoggedIn),
    path('login/', views.login, name ='login'),
    path('register/', views.register, name ='register'),
    path('', RedirectView.as_view(url='login/')),
]