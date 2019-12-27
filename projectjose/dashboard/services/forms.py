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


from projectjose.services.models  import Service,AttributeService

__all__ = [
    'ServiceForm',
]

# ---------------------------------------------------------------------------- #
# Product Form
# ---------------------------------------------------------------------------- #
class ServiceForm(BaseForm):
    class Meta:
        model = Service
        fields = [
            'title',
            'icon',
            'content',
            'image',
        ]

        labels = {
            'title': 'Nombre',
            'icon': 'Icono',
            'content': 'Contenido',
            'image': 'Imagen',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            ProdabreFieldset(
                'Servicio',
                PrependedText(
                    'title',
                    #icon_label(icon='barcode'),
                ),
                PrependedText(
                    'icon',
                    #icon_label(icon='ticket-alt'),
                ),
                PrependedText(
                    'content',
                    #icon_label(icon='pen-square'),
                ),
                PrependedText(
                    'image',
                    #icon_label(icon='pen-square'),
                ),
            ),
        )

# ---------------------------------------------------------------------------- #
# AttributeServiceForm
# ---------------------------------------------------------------------------- #
class AttributeServiceForm(BaseForm):
    class Meta:
        model = AttributeService
        fields = [
            'service',
            'name',
        ]
        widgets = {
            'service': forms.HiddenInput(),
        }

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.helper.layout = Layout(
            'service',
            Field(
                'name'
            ),
        )
