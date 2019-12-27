import re
import json
from django import forms
from crispy_forms.helper import FormHelper as LegacyFormHelper
from crispy_forms.layout import (
    Field,
    Fieldset as LegacyFieldset
)
from crispy_forms.bootstrap import (
    AppendedText as LegacyAppendedText,
    PrependedText as LegacyPrependedText,
)
from crispy_forms.utils import TEMPLATE_PACK


# ------------------------------------------------------------------------------
# Crispy Layout Fields
# ------------------------------------------------------------------------------
class FormHelper(LegacyFormHelper):
    def get_attributes(self, template_pack=TEMPLATE_PACK):
        attributes = super().get_attributes(template_pack=template_pack)
        bootstrap_size_match = re.findall(
            'col-(xl|lg|md|sm|xs)-(\d+)', self.label_class)
        if bootstrap_size_match:
            if template_pack == 'bootstrap4':
                offset_pattern = 'offset-%s-%s'
            else:
                offset_pattern = 'col-%s-offset-%s'
            attributes['bootstrap_checkbox_offsets'] = [
                offset_pattern % m for m in bootstrap_size_match]

        return attributes


class Checkbox(Field):
    template = 'dashboard/_forms/_checkbox.html'


class AppendedText(LegacyAppendedText):
    template = 'dashboard/_forms/_prepended_appended_text.html'


class PrependedText(LegacyPrependedText):
    template = 'dashboard/_forms/_prepended_appended_text.html'


class Fieldset(LegacyFieldset):
    template = 'dashboard/_forms/_fieldset.html'


class IsolatedFieldset(LegacyFieldset):
    template = 'dashboard/_forms/_isolated_fieldset.html'


# ------------------------------------------------------------------------------
# Django Form Utilities
# ------------------------------------------------------------------------------
def get_initial_for_ajax_field(form, field_name, field_klass, field_default=None, **kwargs):
    data = kwargs.get('data', {})
    prefix = kwargs.get('prefix', None)
    item = None

    if prefix:
        attr_name = f'{prefix}-{field_name}'
    else:
        attr_name = field_name

    item_id = data.get(attr_name, None)

    if item_id:
        item = field_klass.objects.filter(id=item_id).first()
    else:
        instance = getattr(form, 'instance', None)
        item = getattr(instance, field_name, None)

    if not item and field_default:
        item = field_default

    return item


# ------------------------------------------------------------------------------
# Django Form Fields
# ------------------------------------------------------------------------------
class AjaxSelect2ChoiceField(forms.ChoiceField):
    """An AJAX-based choice field using Select2.

    fetch_data_url - specifies url, from which select2 will fetch data
    initial - initial object
    """

    def __init__(
            self,
            fetch_data_url='',
            initial=None,
            min_input=2,
            *args,
            **kwargs):
        self.queryset = kwargs.pop('queryset', None)
        super().__init__(*args, **kwargs)
        self.widget.attrs['class'] = 'enable-ajax-select2'
        self.widget.attrs['data-url'] = fetch_data_url
        self.widget.attrs['data-min-input'] = min_input

        if initial:
            self.set_initial(initial)

    def to_python(self, value):
        if value in self.empty_values:
            return None
        try:
            value = self.queryset.get(pk=value)
        except (ValueError, TypeError, self.queryset.model.DoesNotExist):
            raise forms.ValidationError(
                self.error_messages['invalid_choice'], code='invalid_choice')
        return value

    def valid_value(self, value):
        forms.Field.validate(self, value)
        return True

    def set_initial(self, obj, obj_id=None, label=None):
        """Set initially selected objects on field's widget."""
        selected = {
            'id': obj_id if obj_id is not None else obj.pk,
            'text': label if label else str(obj)}
        self.widget.attrs['data-initial'] = json.dumps(
            selected, ensure_ascii=False)

    def set_fetch_data_url(self, fetch_data_url):
        self.widget.attrs['data-url'] = fetch_data_url


class AjaxSelect2CombinedChoiceField(AjaxSelect2ChoiceField):
    """An AJAX-based choice field using Select2 for multiple querysets.

    Value passed to a field is of format '<obj.id>_<obj.__class__.__name__>',
    e. g. '17_Collection' for Collection object with id 17.

    fetch_data_url - specifies url, from which select2 will fetch data
    initial - initial object
    """

    def __init__(self, *args, **kwargs):
        self.querysets = kwargs.pop('querysets')
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if value in self.empty_values:
            return None

        pk, model_name = value.split('_')
        queryset = next(
            (qs for qs in self.querysets if qs.model.__name__ == model_name),
            None)

        value = queryset.filter(pk=pk).first() if queryset else None

        if not value:
            raise forms.ValidationError(
                self.error_messages['invalid_choice'],
                code='invalid_choice')
        return value


# ------------------------------------------------------------------------------
# Django Reusable Forms
# ------------------------------------------------------------------------------
class BaseFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.label_class = ' '.join([
            'col-12',
        ])
        self.helper.field_class = ' '.join([
            'col-12',
        ])

    def _get_initial_for_ajax_field(self, field_name, field_klass, field_default=None, **kwargs):
        return get_initial_for_ajax_field(self, field_name, field_klass, field_default=None, **kwargs)


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.label_class = ' '.join([
            'col-12',
            'col-sm-12',
            'col-md-12',
            'col-lg-4',
            'col-xl-3',
            'text-left',
            'text-lg-right',
        ])
        self.helper.field_class = ' '.join([
            'col-12',
            'col-sm-12',
            'col-md-12',
            'col-lg-6',
            'col-xl-5',
        ])

    def _get_initial_for_ajax_field(self, field_name, field_klass, field_default=None, **kwargs):
        return get_initial_for_ajax_field(self, field_name, field_klass, field_default=None, **kwargs)
