from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'projectjose.dashboard'
    label = 'dashboard'
    verbose_name = _('Dashboard')
