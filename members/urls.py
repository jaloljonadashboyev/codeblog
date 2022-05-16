from re import template
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
#import success_url
#from django.urls import reverse_lazy
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password/', PasswordsChangeView.as_view(), name='password_change'),
    path('password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
]