from django.db import models
from django.utils import timezone

class Companie(models.Model):
	company = models.CharField(max_length=30)

	def __str__(self):
		return self.company

class Employee(models.Model):
	user = models.ForeignKey('auth.User')
	employee = models.CharField(max_length=50)

	def __str__(self):
		return self.employee

class Log(models.Model):
	employee = models.ForeignKey('Employee')
	time_in = models.DateTimeField(auto_now_add=True)
	time_out = models.DateTimeField(blank=True, null=True)

	def isave(self):
		self.time_out = timezone.now()
		self.save()

	def __str__(self):
		return self.employee.employee