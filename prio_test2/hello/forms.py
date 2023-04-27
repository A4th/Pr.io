from django import forms
from .models import Subject

class Subjectform(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subName', 'numUnits','subStart','subEnd'] 