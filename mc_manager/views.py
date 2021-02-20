from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

from .models import Route, Stop, Location, Item, Frequency, Temperature
from .forms import RouteForm, StopForm, LocationForm, ItemForm
# Create your views here.

def setup():
	f = Frequency.objects.all().count()
	if f == 0:
		for day in Frequency.DAYS:
			d = Frequency(frequency=day)
			d.save()
	t = Temperature.objects.all().count()
	if t == 0:
		for temp in Temperature.TEMPS:
			lt = Temperature(temp=temp)
			lt.save()

def index(request):
	return render(request, 'mc_manager/index.html')

def routes(request):
	routes = Route.objects.all()
	context = {'routes':routes}
	return render(request, 'mc_manager/routes.html', context)

def route(request, route_id):
	route = get_object_or_404(Route, id=route_id)
	context = {'route': route}
	return render(request, 'mc_manager/route.html', context)

def new_route(request):
	setup()
	if request.method != 'POST':
		form = RouteForm()
	else:
		form = RouteForm(data=request.POST)
		if form.is_valid():
			new_route = form.save()
			return HttpResponseRedirect(reverse('route', args=[new_route.id]))
	context = {'form':form}
	return render(request, 'mc_manager/new_route.html', context)

def edit_route(request, route_id):
	route = get_object_or_404(Route, id=route_id)
	if request.method != 'POST':
		data = {'route':route}
		form = RouteForm(initial=data)
	else:
		form = RouteForm(instance=route, data=request.POST)
		if form.is_valid():
			edited_route = form.save()
			return HttpResponseRedirect(render('route', args=[edited_route.id]))
	context = {'form':form,'route': route}
	return render(request, 'mc_manager/edit_route.html', context)

def locations(request):
	locations = Location.objects.all()
	context = {'locations':locations}
	return render(request, 'mc_manager/locations.html', context)

def new_location(request):
	if request.method != 'POST':
		form = LocationForm()
	else:
		form = LocationForm(data=request.POST)
		if form.is_valid():
			new_loc = form.save()
			return HttpResponseRedirect(reverse('location', args=[new_loc.id]))
	context = {'form':form}
	return render(request, 'mc_manager/new_location.html', context)

def location(request, location_id):
	location = get_object_or_404(Location, id=location_id)
	context = {'location':location}
	return render(request, 'mc_manager/location.html', context)

def edit_location(request, location_id):
	loc = get_object_or_404(Location, id=location_id)
	if request.method != 'POST':
		form = LocationForm(instance=loc)
	else:
		form = LocationForm(instace=loc, data=request.POST)
		if form.is_valid():
			edited_loc = form.save()
			return HttpResponseRedirect(reverse('location', args=[edited_loc.id]))
	context = {'form':form, 'location': loc}
	return render(request, 'mc_manager/edit_location.html', context)