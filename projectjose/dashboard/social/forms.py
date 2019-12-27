from django import forms
from django.forms.models import inlineformset_factory
from django.utils.translation import pgettext_lazy

from crispy_forms.layout import (
    Row,
    Column,
    Layout,
    Field,
    MultiField,
    Fieldset
)
from projectjose.core.forms import (
    BaseForm,
    AjaxSelect2ChoiceField,
    PrependedText,
    Checkbox,
    Fieldset as ProdabreFieldset
)

from projectjose.core.utils.text import icon_label


from projectjose.social.models  import Link

__all__ = [
    'LinkForm',
]

# ---------------------------------------------------------------------------- #
# Product Form
# ---------------------------------------------------------------------------- #
class LinkForm(BaseForm):
    class Meta:
        model = Link
        fields = [
            'key',
            'name',
            'url',
        ]

        labels = {
            'key': 'Llave',
            'name': 'Nombre',
            'url': 'link de la red social',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            ProdabreFieldset(
                'Red Social',
                 PrependedText(
                    'key',
                    icon_label(icon='barcode'),
                 ),
                 PrependedText(
                    'name',
                    icon_label(icon='ticket-alt'),
                 ),
                 PrependedText(
                    'url',
                    icon_label(icon='pen-square'),
                 ),
            ),
        )
