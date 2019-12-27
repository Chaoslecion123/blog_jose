from django.db import models


def is_deletable(instance):
    fields = instance._meta.get_fields()
    fields = [
        f for f in fields if f.auto_created and not f.concrete
    ]
    fields = [
        f for f in fields if f.on_delete is models.PROTECT
    ]
    one_to_one_fields = [
        f.name for f in fields if f.one_to_one
    ]
    fields = [
        f.name for f in fields if not f.one_to_one
    ]
    one_to_one_values = [
        getattr(instance, f, None) for f in one_to_one_fields
    ]
    values = [
        getattr(instance, f, None) for f in fields
    ]
    checked_values = [
        (lambda x: x is None or x.exists())(v) for v in values
    ] + [
        v is None for v in one_to_one_values
    ]
    return all(checked_values)
