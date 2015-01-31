# from django.forms import ModelForm
from django.contrib.admin import widgets
from django import forms
from events.models import *


class EventCreateForm( forms.ModelForm ):
	date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))

	class Meta:
		model = Event
		fields = ('date',)
		# fields = ('date', 'location', 'time', 'people', 'description',)