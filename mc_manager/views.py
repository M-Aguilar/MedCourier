from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

from .models import Route, Stop, Location, Item
from .forms import RouteForm, StopForm, LocationForm, ItemForm
# Create your views here.

def index(request):
	return render(request, 'mc_manager/index.html')