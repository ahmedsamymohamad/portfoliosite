from django.urls import path
from .views import MyLoginView

from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('admin/login/', MyLoginView.as_view(redirect_authenticated_user=True),name='login'),
    path('admin/logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('password-reset/', 
        PasswordResetView.as_view(
            template_name='user/password_reset.html',
            html_email_template_name='user/password_reset_email.html'
        ),
        name='password-reset'
    ),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),
]


