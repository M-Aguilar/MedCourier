from django.urls import path

from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('routes', views.routes, name='routes'),
	path('route/<route_id>', views.route, name='route'),
	path('new_route', views.new_route, name='new_route'),
	path('edit_route/<route_id>', views.edit_route, name='edit_route'),
	path('locations', views.locations, name='locations'),
	path('location/<location_id>', views.location, name='location'),
	path('new_location', views.new_location, name='new_location'),
	path('edit_location/<location_id>', views.edit_location, name='edit_location'),
]