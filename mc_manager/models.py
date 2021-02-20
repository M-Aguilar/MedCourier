from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Frequency(models.Model):
	MONDAY = 'M'
	TUESDAY = 'T'
	WEDNESDAY = 'W'
	THURSDAY = 'Th'
	FRIDAY = 'F'
	SATURDAY = 'Sa'
	SUNDAY = 'Su'
	DAYS = [
		(MONDAY, 'Monday'),
		(TUESDAY, 'Tuesday'),
		(WEDNESDAY, 'Wednesday'),
		(THURSDAY, 'Thursday'),
		(FRIDAY, 'Friday'),
		(SATURDAY, 'Saturday'),
		(SUNDAY, 'Sunday'),
	]
	frequency = models.CharField(max_length=2, choices=DAYS, blank=True)

	def __str__(self):
		return self.get_frequency_display()

class Temperature(models.Model):
	AMBIENT = 'AMB'
	REFRIGERATED = 'REF'
	FROZEN = 'FZN'
	FROZEN_MINUS_70 = 'F70'

	TEMPS = [
		(AMBIENT,'Ambient'),
		(REFRIGERATED, 'Refrigerated'),
		(FROZEN, 'Frozen'),
		(FROZEN_MINUS_70, 'Frozen (-70)'),
	]
	temp = models.CharField(max_length=3, choices=TEMPS, default=AMBIENT)

class Route(models.Model):
	name = models.CharField(max_length=30, blank=True)
	frequency = models.ManyToManyField(Frequency)

	class Meta:
		verbose_name_plural = 'routes'

	def __str__(self):
		return '{0}'.format(self.name)

	@property
	def freq(self):
		return self.frequency.all()

class Address(models.Model):
	street_number = models.IntegerField(blank=True)
	street = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=100, blank=True)
	state = models.CharField(max_length=100, blank=True)
	postal_code = models.IntegerField(validators=[MaxValueValidator(99999)], blank=True)

	@property
	def gaddr(self):
		return '{0}+{1}+{2}%2C+{3}+{4}'.format(self.street_number, self.street.replace(' ','+'), self.city, self.state, self.postal_code)

	@property
	def addr(self):
		return '{0} {1} {2}, {3} {4}'.format(self.street_number, self.street, self.city, self.state, self.postal_code)

	class Meta:
		abstract = True

class Location(Address):
	name = models.CharField(max_length=100, blank=True)
	phone_number = models.PositiveIntegerField(validators=[MinValueValidator(1111111111)], blank=True, null=True)

	def phone(self):
		return '{0}-{1}-{2}'.format(str(self.phone_number)[0:3], str(self.phone_number)[3:6], str(self.phone_number[6:]))

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'locations'

class Stop(models.Model):
	route = models.ForeignKey(Route, on_delete=models.CASCADE)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	scheduled_time = models.DateTimeField()
	on_call = models.BooleanField(default=False)
	completed = models.BooleanField(default=False)
	time_completed = models.DateTimeField()

	def __str__(self):
		return self.location

	class Meta:
		verbose_name_plural = 'stops'

class Item(models.Model):
	code = models.CharField(max_length=100)
	pickup_location = models.ForeignKey(Stop, on_delete=models.CASCADE,related_name='pickup_item')
	delivery_location = models.ForeignKey(Stop, on_delete=models.CASCADE,related_name='delivery_item')
	pickup_time = models.DateTimeField()
	delivery_time = models.DateTimeField()

	def __str__(self):
		return self.code

	class Meta:
		verbose_name_plural = 'items'