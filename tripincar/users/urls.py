from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),

    path('auth/signup/', views.SignUp.as_view(), name='signup'),

    path(
      'auth/logout/',
      auth_views.LogoutView.as_view(
        template_name='users/logged_out.html'),
        name='logout'
    ),    
    
    path('auth/login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),

    path('auth/password_change/', auth_views.PasswordChangeView.as_view(
        template_name='users/password_change_form.html'),
        name='password_change'),
    path('auth/password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'),
        name='password_change_done'),

    path('auth/password_reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset_form.html'),
        name='password_reset'),
    path('auth/password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    path('auth/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('auth/reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
        name='password_reset_complete')
]
