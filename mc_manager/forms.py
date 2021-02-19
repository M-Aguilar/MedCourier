from django import forms

from .models import Route, Stop, Location, Item, Address

class RouteForm(forms.ModelForm):
	class Meta:
		model = Route
		fields = ['name', 'frequency']

class StopForm(forms.ModelForm):
	class Meta:
		model = Stop
		fields = ['route','location','scheduled_time','on_call']
		widgets = {
			'scheduled_time': forms.TimeInput(attrs={'format':'%H:%M'})
		}

class LocationForm(forms.ModelForm):
	class Meta:
		model = Location
		fields = ['name','phone_number','street_number','street','city','state','postal_code']

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['code']
