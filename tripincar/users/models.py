from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class UserRole:
    USER = 'user'
    DRIVER = 'driver'
    ADMIN = 'admin'


class User(AbstractUser):
    ROLES = (
        (UserRole.USER, 'USER'),
        (UserRole.DRIVER, 'DRIVER'),
        (UserRole.ADMIN, 'ADMIN')
    )
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer.'
            'Letters, digits and @/./+/-/_ only.'
        ),
        validators=[validators.RegexValidator(regex=r'^[\w.@+-]+\Z')],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    email = models.EmailField(
        _('email'),
        max_length=254,
        unique=True,
    )
    
    telephone = PhoneNumberField(
        _('phone'),
        region='RU'
    )

    role = models.CharField(
        _('role'),
        max_length=9,
        choices=ROLES,
        default=UserRole.USER
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_name'
            ),
        ]

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return (self.role == UserRole.ADMIN
                or self.is_staff
                or self.is_superuser)

    @property
    def is_user(self):
        return self.role == UserRole.USER

    @property
    def is_driver(self):
        return self.role == UserRole.DRIVER
