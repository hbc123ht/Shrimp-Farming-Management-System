from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

# Create your models here.

class Parameters(models.Model):
    user             = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE, primary_key=True, null=False, blank=False)
    ph               = models.DecimalField(decimal_places=2, max_digits=1000, verbose_name=_('Ph_amount'), null = True, blank = True)
    temp             = models.DecimalField(decimal_places=2, max_digits=1000, verbose_name=_('temperature'), null = True, blank = True)
    salinity         = models.DecimalField(decimal_places=2, max_digits=1000, verbose_name=_('salinity'), null = True, blank = True)
    alkalinity       = models.DecimalField(decimal_places=2, max_digits=1000, verbose_name=_('alkalinity'), null = True, blank = True)
    oxygen           = models.DecimalField(decimal_places=2, max_digits=1000, verbose_name=_('oxygen'), null = True, blank = True)
    hydrogen_sulfide = models.DecimalField(decimal_places=2, max_digits=1000, verbose_name=_('hydrogen_sulfide'), null = True, blank = True)
    amonia           = models.DecimalField(decimal_places=2, max_digits=1000, verbose_name=_('amonia'), null = True, blank = True)
    nitrit           = models.DecimalField(decimal_places=2, max_digits=1000, verbose_name=_('nitrit'), null = True, blank = True)