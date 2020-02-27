from django.urls import path
#from . import views
from templates import registration
from .views import SignUpView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password-reset', PasswordResetView.as_view(template_name='registration/forgot_password.html'), name='password-reset'),
    # path('password-reset-done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password-reset-done'),
    # path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password-reset-confirm'),
    # path('password-reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password-reset-complete'),
   
]
