import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class CarNameModel(models.Model):
    """ model CarNameModel (MTM) """

    RUSSIAN = 'RU'
    ENGLISH = 'EN'
    LANGUAGES = [
        (RUSSIAN, 'Русский'),
        (ENGLISH, 'English')
    ]
    lang = models.CharField(_('Lang'), max_length=2, choices=LANGUAGES, default=RUSSIAN)
    name = models.CharField(_('Name'), max_length=100)

    class Meta:
        verbose_name = _('Name')
        verbose_name_plural = _('Names')

    def __str__(self):
        return self.name


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class CarModel(models.Model):
    """ model CarModel """

    name = models.ManyToManyField(CarNameModel)
    year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1950), max_value_current_year])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

    def __str__(self):
        return str(self.year)
