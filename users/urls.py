from django.urls import path
from django.contrib.auth import views as generic_views

from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', generic_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', generic_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
