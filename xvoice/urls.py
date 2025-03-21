from django.urls import path
from .views import CustomLoginView
from . import views
from .views import register
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    # Redirect the root URL to the login page
    path('', RedirectView.as_view(url='login/'), name='root_redirect'),
    # path('messaging/', views.messaging_view, name='messaging'),

    path('login/', lambda request: redirect('/accounts/login/')),  # Redirect /login to /accounts/login/
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Add this line
    path('accounts/register/', views.register, name='register'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        html_email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt'
    ), name='password_reset'),
]
