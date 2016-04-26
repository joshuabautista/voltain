from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.employee_list, name='employee_list'),
    url(r'^post/(?P<pk>\d+)/$', views.employee_detail, name='employee_detail'),
]