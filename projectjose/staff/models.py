from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy

from django.db import models
from django.contrib.auth.models import User

class Staff(User):
    class Meta:
        proxy = True
        verbose_name = pgettext_lazy(
            'Affiliation Activity model name',
            'empleado'
        )
        verbose_name_plural = pgettext_lazy(
            'Affiliation Activity model name',
            'empleados'
        )

    def save(self, *args, **kwargs):
        self.is_staff = True
        super().save(*args, **kwargs)
