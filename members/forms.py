from django import forms
from members.models import StaffProfile
from django.db.models.fields import BLANK_CHOICE_DASH


class SI(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ['staff_no']
        labels = {'staff_no': 'Staff No'}
        widgets = {'staff_no': forms.TextInput(attrs={'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event', None)
        super(SI, self).__init__(*args, **kwargs)

    def clean(self):
        staff_no = self.cleaned_data.get("staff_no")

        if len(staff_no) < 5:
            self._errors['staff_no'] = self.error_class([
                '*** Minimum 5 characters required'])
        if staff_no is None:
            self._errors['staff_no'] = self.error_class([
                '*** enter staff no'])

        return self.cleaned_data
