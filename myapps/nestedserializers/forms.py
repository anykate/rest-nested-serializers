from django import forms
from .models import Marks


class MarksInsertForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = '__all__'
