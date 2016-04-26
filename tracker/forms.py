from django import forms
from .models import Employee, Companie, Log

class LoginForm(forms.ModelForm):

	class Meta:
		model = Log
		fields = ('employee','time_in',)