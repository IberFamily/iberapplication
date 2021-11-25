from django import forms
from django.db.models.fields import CharField

class statusCheck(forms.ModelForm):
    pending = forms.CheckboxInput()
    accepted = forms.CheckboxInput()
    rejected = forms.CheckboxInput()

