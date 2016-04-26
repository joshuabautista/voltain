from django.shortcuts import render
from django.utils import timezone
from .models import Companie, Employee, Log
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import EmployeeForm

@login_required
def employee_list(request):
	company = Companie.objects.all()
	employees = Employee.objects.all()
	log = Log.objects.filter(time_out=None)
	log2 = Log.objects.all()
	#import pdb
	#pdb.set_trace()
	return render(request, 'tracker/employee_list.html', {'company' : company, 'log' : log, 'log2' : log2})

def employee_detail(request, pk):
    l = get_object_or_404(Log, pk=pk)
    return render(request, 'tracker/employee_detail.html', {'l': l})