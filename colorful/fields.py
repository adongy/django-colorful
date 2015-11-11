from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db.models import CharField

from . import forms


class RGBColorField(CharField):
    """Field for database models"""
    default_validators = [RegexValidator(regex=forms.RGB_REGEX)]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 7
        super(RGBColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.RGBColorField,
        }
        defaults.update(kwargs)
        return super(RGBColorField, self).formfield(**defaults)

    def deconstruct(self):
        name, path, args, kwargs = super(RGBColorField, self).deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs
        
    def to_python(self, value):
        value = super(RGBColorField, self).to_python(value)
        if value is None or value.startswith('#'):
            return value
        return '#{}'.format(value)
