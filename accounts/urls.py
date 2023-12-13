from django.urls import path
from .import views
from django.contrib import admin
from .views import home, profile, signin, signup, explore, groups,logout


urlpatterns = [
path('signin/', views.signin, name='signin' ),
path('signup/', views.signup, name='signup' ),
path('profile/', views.profile, name='profile' ),  
path('', views.home, name='home' ),  
path('groups/', views.groups, name='groups' ),
path('explore/', views.explore, name='explore' ),
path('logout/', views.logout, name='logout' ),
]