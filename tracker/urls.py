from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^employeelist/', views.employee_log, name='employee_log'), #for all emloyees
    url(r'^$', views.employee_list, name='employee_list'),
    url(r'^post/(?P<pk>\d+)/$', views.employee_detail, name='employee_detail'),
    url(r'^employee/time_in/$', views.time_in, name='time_in'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
]