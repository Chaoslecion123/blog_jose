import re

from django.utils.safestring import mark_safe


__all__ = [
    'normalize_name',
    'icon_label'
]


def normalize_name(name):
    return re.sub(' +', ' ', name).strip()


def icon_label(label='', icon=None, icon_type='fas'):
    return mark_safe(f'<i class="{icon_type} fa-fw fa-{icon}"></i> {label}'.strip())
