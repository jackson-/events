import json
import datetime
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from events.models import *

# Create your views here.

class Index( View ):
	template_name = 'events/index.html'

	def get( self, request ):
		events = Event.objects.all()
		request.context_dict['events'] = Event.objects.all()
		events_json = events.values()
		request.context_dict['events_json'] = events_json
		return render( request, self.template_name, request.context_dict )

	def post( self, request ):
		description = request.POST['description']
		date = request.POST['date']
		location = request.POST['location']
		time = request.POST['time']
		people = request.POST['people']
		CurrentEvent.objects.create(description=description, date=date, location=location, time=time, people=people)
		return redirect( '/current' )

class Past( View ):
	template_name = 'events/past.html'

	def get( self, request ):
		request.context_dict['events'] = PastEvent.objects.all()
		return render( request, self.template_name, request.context_dict )

	def post( self, request ):
		description = request.POST['description']
		date = request.POST['date']
		location = request.POST['location']
		time = request.POST['time']
		people = request.POST['people']
		PastEvent.objects.create(description=description, date=date, location=location, time=time, people=people)
		return redirect( '/past' )

class Current( View ):
	template_name = 'events/index.html'

	def get( self, request ):
		request.context_dict['events'] = CurrentEvent.objects.all()
		return render( request, self.template_name, request.context_dict )

	def post( self, request ):
		description = request.POST['description']
		date = request.POST['date']
		location = request.POST['location']
		time = request.POST['time']
		people = request.POST['people']
		CurrentEvent.objects.create(description=description, date=date, location=location, time=time, people=people)
		return redirect( '/current' )


class Edit( View ):

	def get( self, request, pk ):
		event = Event.objects.get(pk=pk)
		return JsonResponse({"id":event.id, "date":event.date, "time":event.time, "people":event.people, "location":event.location, "description":event.description, })

	def post( self, request, pk ):
		print(request.POST)
		event = Event.objects.get(pk=pk)
		event.description = request.POST['description']
		event.date = request.POST['date']
		event.location = request.POST['location']
		event.time = request.POST['time']
		event.people = request.POST['people']
		event.save()
		return JsonResponse({"edited":'true'})

class Delete( View ):

	def post( self, request, pk ):
		event = Event.objects.get(pk=pk)
		PastEvent.objects.create(time=event.time, date=event.date, location=event.location, people=event.people, description=event.description)
		event.delete()
		return JsonResponse({"deleted":"true"})

class PastDelete( View ):

	def post( self, request, pk ):
		event = PastEvent.objects.get(pk=pk)
		event.delete()
		return JsonResponse({"deleted":"true"})