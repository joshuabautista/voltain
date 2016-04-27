from django.shortcuts import render
from django.utils import timezone
from .models import Companie, Employee, Log
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import LoginForm
from django.shortcuts import redirect

@login_required
def employee_list(request):
	company = Companie.objects.all()
	employees = Employee.objects.all()
	log = Log.objects.filter(time_out=None)
	log2 = Log.objects.all()
	#import pdb
	#pdb.set_trace()
	return render(request, 'tracker/employee_list.html', {'company' : company, 'log' : log, 'log2' : log2})

@login_required
def employee_detail(request, pk):
    l = get_object_or_404(Log, pk=pk)
    return render(request, 'tracker/employee_detail.html', {'l': l})

@login_required
def time_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.employee.employee = request.user
            post.time_in = timezone.now()
            post.save()
            return redirect('employee_list')
    else:
        form = LoginForm() 
    return render(request, 'tracker/employee_in.html', {'form': form})

def post_publish(request, pk):
    post = get_object_or_404(Log, pk=pk)
    post.isave()
    return redirect('tracker.views.employee_detail', pk=pk)

def employee_log(request):
    emp = Employee.objects.all()
    return render(request, 'tracker/employees.html', {'emp' : emp})    