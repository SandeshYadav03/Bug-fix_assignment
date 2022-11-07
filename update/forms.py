from django import forms 
from .models import *

class EmployeeForms(forms.ModelForm):
    class Meta:
        model=AddEmployee
        fields='__all__'