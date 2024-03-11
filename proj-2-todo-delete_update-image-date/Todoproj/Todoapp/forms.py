from .models import Task
from django import forms

class TodoForms(forms.ModelForm):
    class Meta:
        model=Task
        field=['name','priority','date','image']