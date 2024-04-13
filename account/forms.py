from django import forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# .....


User = get_user_model()




class UserCreationForm(auth_forms.UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control text-capitalize', 'placeholder': _('Enter First Name'), 'pattern': '[A-Za-z][A-Za-z0-9\s]+',
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control text-capitalize', 'placeholder': _('Enter Last Name'), 'pattern': '[A-Za-z][A-Za-z0-9\s]+',
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control text-lowercase', 'placeholder': _('Enter Email Address'),
        })
        
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 'placeholder': _('* * * * * * * *'),
        })
        
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 'placeholder': _('* * * * * * * *'),
        })

    
    def clean_first_name(self):
        return str(self.cleaned_data['first_name']).title()

    def clean_last_name(self):
        return str(self.cleaned_data['last_name']).title()

    def clean_email(self):
        return str(self.cleaned_data['email']).lower()




class UserLoginForm(auth_forms.AuthenticationForm):

    username = auth_forms.UsernameField(widget=forms.EmailInput(attrs={"autofocus": True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control', 'placeholder': _('Email Address'),
        })
        
        self.fields['password'].widget.attrs.update({
            'class': 'form-control', 'placeholder': _('* * * * * * * *'),
        })
