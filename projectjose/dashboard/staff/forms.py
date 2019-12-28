from django import forms
from django.forms.models import inlineformset_factory
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _

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


from projectjose.staff.models  import Staff
from django.contrib.auth.models import User


__all__ = [
    'StaffForm',
]

# ---------------------------------------------------------------------------- #
# Product Form
# ---------------------------------------------------------------------------- #
class StaffForm(BaseForm):
    password = forms.CharField(
                label='Contraseña',
                required=True,
                widget=forms.PasswordInput)
    password2 = forms.CharField(
                label='confimar contraseña',
                required=True,
                widget=forms.PasswordInput)

    class Meta:
        model = Staff
        fields = [
            'username',
            'email',
            'password',
            'password2',
        ]

        labels = {
            'username': 'Usuario',
            'email': 'Correo electronico',
            'password': 'Contraseña',
            'password2': 'Contraseña confirmacion',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            ProdabreFieldset(
                'Personal',
                PrependedText(
                    'username',
                    icon_label(icon='barcode'),
                ),
                PrependedText(
                    'email',
                    icon_label(icon='ticket-alt'),
                ),
                PrependedText(
                    'password',
                    icon_label(icon='pen-square'),
                ),
                PrependedText(
                    'password2',
                    icon_label(icon='pen-square'),
                ),
            ),
        )


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username se encuentra en uso.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email se encuentra en uso.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2','El password no coincide')

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')

        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class StaffEditForm(BaseForm):
    class Meta:
        model = Staff
        fields = [
            'first_name',
            'last_name',
            'email',
        ]

        labels = {
            'first_name': 'Nombre',
            'last_name': 'apellido',
            'email': 'Correo electronico',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            ProdabreFieldset(
                'Personal',
                PrependedText(
                    'first_name',
                    icon_label(icon='barcode'),
                ),
                PrependedText(
                    'last_name',
                    icon_label(icon='pen-square'),
                ),
                PrependedText(
                    'email',
                    icon_label(icon='ticket-alt'),
                ),
            ),
        )



class StaffChangePasswordForm(BaseForm):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(
        label=_("Contraseña nueva"),
        widget=forms.PasswordInput
    )
    new_password2 = forms.CharField(
        label=_("Confirmar contraseña nueva"),
        widget=forms.PasswordInput
    )
    send_notification = forms.BooleanField(
        label='Enviar notificacion al usuario',
        required=False,
        initial=False,
    )

    class Meta:
        model = Staff
        fields = []

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Field(
                PrependedText(
                    'new_password1',
                    icon_label(icon='id-card'),
                ),
            ),
            Field(
                PrependedText(
                    'new_password2',
                    icon_label(icon='id-card'),
                ),
            ),
            Checkbox(
                'send_notification'
            ),
        )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('new_password1', None)
        password2 = cleaned_data.get('new_password2', None)
        if password1 and password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    forms.ValidationError(
                        self.error_messages['password_mismatch'],
                        code='password_mismatch',
                    )
                )
        return cleaned_data

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user
