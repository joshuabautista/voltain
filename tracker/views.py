from django.shortcuts import render
from django.utils import timezone
from .models import Companie, Employee, Log

def employee_list(request):
	company = Companie.objects.all()
	employees = Employee.objects.all()
	log = Log.objects.all()
	return render(request, 'tracker/employee_list.html', {'employees': employees, 'company' : company, 'log' : log})