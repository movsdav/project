from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Patient


class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Create'))

    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'age', 'diagnosis')


class PatientUUIDForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PatientUUIDForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', "Find"))

    uuid = forms.UUIDField()
