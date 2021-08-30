from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = 'userapp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name ='userapp/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='userapp/logout.html'), name='logout')
]
