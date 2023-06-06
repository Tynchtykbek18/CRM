from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    POSITIONS = (('администратор', 'Администратор'),
                 ('менеджер', 'Менеджер'),
                 ('сотрудник', 'Сотрудник'),
                 )
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    email = models.EmailField(_("email address"), unique=True)
    position = models.CharField(max_length=30, choices=POSITIONS)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Client(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='имя')
    last_name = models.CharField(max_length=30, verbose_name='фамилия')
    password = models.CharField(max_length=30, )
    email = models.EmailField(max_length=30, verbose_name='email')
    contacts = models.CharField(max_length=200, verbose_name='контакты')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'Клиенты'
