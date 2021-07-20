from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

# Create your models here.

class Parameters(models.Model):
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE, primary_key=True, null=False, blank=False)
    ph = models.IntegerField(verbose_name=_('Ph_amount'), null = True, blank = True)
    temp = models.IntegerField(verbose_name=_('temperature'), null = True, blank = True)
    salinity = models.IntegerField(verbose_name=_('salinity'), null = True, blank = True)
