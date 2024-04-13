from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import views as auth_views
from django.views.generic import CreateView
# ...
from .forms import (UserCreationForm, UserLoginForm, User)



class RegisterView(CreateView):
    template_name = 'account/register.html'
    model = User
    form_class = UserCreationForm
    extra_context = {
        'title': _('Register')
    }
    success_url = reverse_lazy('dashboard')


class LoginView(auth_views.LoginView):
    template_name = 'account/login.html'
    form_class = UserLoginForm
    next_page = 'dashboard'
    extra_context = {
        'title': _('Login')
    }



class LogoutView(auth_views.LogoutView):
    # next_page = ''
    template_name = 'account/logout.html'
    extra_context = {
        'title': _('Logout')
    }
