from django.urls import path
from django.contrib.auth import views as generic_views
from django.urls import reverse_lazy

from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', generic_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', generic_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', generic_views.PasswordResetView.as_view(
        template_name='users/password_reset.html', email_template_name='users/password_reset_email.html', success_url=reverse_lazy('users:password-reset-done')), name='password-reset'),
    path('password-reset/done/', generic_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/', generic_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html', success_url=reverse_lazy('users:password-reset-complete')), name='password-reset-confirm'),
    path('password-reset-complete/', generic_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password-reset-complete'),
    path('profile/', views.profile, name='profile'),
]
