from django.urls import path
from . import views
from django.views.generic.base import TemplateView
#from django.contrib.auth.views import PasswordChangeView

from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView
)


urlpatterns = [

    path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',
         ClientDeleteView.as_view(), name='client_delete'),
    path('', ClientListView.as_view(), name='client_list'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
#     path('password_change', PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password-change_form'),
#     path('password_change/done', PasswordChangeView.as_view(template_name='registration/password_change_done.html'), name='password-change_done'),
    
]
