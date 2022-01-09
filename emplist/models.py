from django.db import models

# Create your models here.

class Employee(models.Model):
	firstname_text = models.CharField(max_length=200)
	lastname_text = models.CharField(max_length=200)

	address_text = models.CharField(max_length=200)

	phone_text = models.CharField(max_length=200)

	def __str__(self):
		return self.firstname_text + ' ' + self.lastname_text
	
