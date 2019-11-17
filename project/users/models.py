from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from auto.models import CarModel


class User(AbstractUser):
    """ model User """
    RUSSIAN = 'RU'
    ENGLISH = 'EN'
    LANGUAGES = [
        (RUSSIAN, 'Русский'),
        (ENGLISH, 'English')
    ]

    username = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    lang = models.CharField(max_length=2, choices=LANGUAGES, default=RUSSIAN)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    """ model Profile """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


class UserCars(models.Model):
    """ model UserCars """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cars')
    car = models.ManyToManyField(CarModel, related_name='usercars_car')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('User car')
        verbose_name_plural = _('User cars')

    def __str__(self):
        return str(self.created_at)
