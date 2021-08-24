from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rent'
    verbose_name = _('Rent')
    verbose_name_plural = _('Rents')
