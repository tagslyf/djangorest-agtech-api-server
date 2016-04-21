from __future__ import unicode_literals

from django.db import models

class Country(models.Model):
	id 					= models.AutoField(primary_key=True)
	country_short_name	= models.CharField(max_length=50)
	country_long_name	= models.CharField(max_length=100)
	country_iso2		= models.CharField(max_length=2)
	country_iso3		= models.CharField(max_length=3)
	country_numcode		= models.CharField(max_length=8)
	country_dial_code	= models.CharField(max_length=8)
	country_visible		= models.BooleanField(default=False)
	pass

	class Meta:
		db_table = "country"

	def __unicode__(self):
		return '%s' % (self.country_iso2)

class State(models.Model):
	id				= models.AutoField(primary_key=True)
	state_name 		= models.CharField(max_length=30)
	state_code 		= models.CharField(max_length=5)
	# city			= models.ForeignKey(City, related_name="city", null=True, blank=True)
	country			= models.ForeignKey(Country, related_name="state")
	pass

	def __unicode__(self):
		return '%s-%s' % (self.state_name, self.state_code)

class City(models.Model):
	id				= models.AutoField(primary_key=True)
	city_name 		= models.CharField(max_length=30)
	city_county		= models.CharField(max_length=30)
	city_zipcode	= models.CharField(max_length=30)
	state			= models.ForeignKey(State, related_name="city")
	pass

	class Meta:
		ordering = ['city_name']

	def __unicode__(self):
		return '%s-%s-%s' % (self.city_name.replace('\'', ''), self.city_county.replace('\'', ''), self.city_zipcode.replace('\'', ''))
