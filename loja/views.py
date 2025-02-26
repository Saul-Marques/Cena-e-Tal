from django.shortcuts import render
from django.contrib import admin 
from django.urls import path 
from .views.home import Index, loja 
from .views.signup import Signup 
from .views.login import Login, logout 
from .middlewares.auth import auth_middleware 


urlpatterns = [ 
	path('', Index.as_view(), name='homepage'), 
	path('loja', loja, name='loja'), 

	path('signup', Signup.as_view(), name='signup'), 
	path('login', Login.as_view(), name='login'), 
	path('logout', logout, name='logout'),
] 
