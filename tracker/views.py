from django.shortcuts import render

def employee_list(request):
    return render(request, 'tracker/employee_list.html', {})