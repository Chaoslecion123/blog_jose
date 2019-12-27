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


from projectjose.posts.models  import Post,PostImage

__all__ = [
    'PostForm',
]

# ---------------------------------------------------------------------------- #
# Product Form
# ---------------------------------------------------------------------------- #
class PostForm(BaseForm):
    class Meta:
        model = Post
        fields = [
            'slug',
            'title',
            'subtitle',
            'content',
        ]

        labels = {
            'slug': 'Nombre',
            'title': 'Titulo',
            'subtitle': 'Sub titulo',
            'content': 'Contenido',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            ProdabreFieldset(
                'Proyecto',
                PrependedText(
                    'slug',
                    icon_label(icon='barcode'),
                ),
                PrependedText(
                    'title',
                    icon_label(icon='ticket-alt'),
                ),
                PrependedText(
                    'subtitle',
                    icon_label(icon='pen-square'),
                ),
                PrependedText(
                    'content',
                    icon_label(icon='pen-square'),
                ),
            ),
        )

# ---------------------------------------------------------------------------- #
# Postg Image Form
# ---------------------------------------------------------------------------- #
class PostImageForm(BaseForm):
    class Meta:
        model = PostImage
        fields = [
            'post',
            'image',
            'alt',
        ]
        widgets = {
            'post': forms.HiddenInput(),
        }

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.helper.layout = Layout(
            'post',
            Field(
                'image'
            ),
            Field(
                'alt'
            ),
        )
