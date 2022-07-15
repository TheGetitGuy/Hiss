from django.urls import path
from django.views.generic import RedirectView

from . import views


urlpatterns = [ 
    path('home/', views.home, name='home'),
    path('login/', views.login, name ='login'),
    path('register/', views.register, name ='register'),
    path('logout/', views.register, name ='logout'),
    path('', RedirectView.as_view(url='login/'),),
]