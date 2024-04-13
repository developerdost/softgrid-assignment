from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# .....
from .managers import UserManager


class User(AbstractUser):
    first_name = models.CharField(
        max_length=50,
        verbose_name=_('First Name'),
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name=_('Last Name'),
    )

    email = models.EmailField(
        verbose_name=_('Email Address'),
        max_length=150,
        unique=True,
        error_messages={'unique': _('A user with that email already exists.')},
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./_ only.'
        ),
    )
    
    # EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    # removes email from REQUIRED_FIELDS
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # Custome User Manager
    manager = UserManager()
    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self) -> str:
        return f'{self.email}'.lower()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.title()
    
