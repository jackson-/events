from django.db import models

# Create your models here.
class Event( models.Model ):
	description = models.TextField()
	date = models.DateField()
	location = models.CharField(max_length=70)
	time = models.TimeField()
	people = models.CharField(max_length=70)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class CurrentEvent( Event ):
	pass

class PastEvent( Event ):
	pass