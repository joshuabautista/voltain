from django import forms

from .models import Employee, Companie, Log

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'