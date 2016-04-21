from django.contrib.auth.models import Group
from rest_framework import serializers
from country.models import *
import json

class CitySerializer(serializers.ModelSerializer):

	class Meta:
		model = City
		fields = (
			'city_name',
			'city_zipcode'
		)	

class StateSerializer(serializers.ModelSerializer):
	city = serializers.StringRelatedField(many=True)

	class Meta:
		model = State
		fields = (
			'id', 
			'state_name',
			'state_code',
			'city'
		)	
	

class CountrySerializer(serializers.ModelSerializer):
	state = StateSerializer(many=True, read_only=True)

	class Meta:
		model = Country
		fields = (
			'id', 
			'country_short_name', 
			'country_long_name', 
			'country_iso2', 
			'country_iso3', 
			'country_numcode', 
			'country_dial_code', 
			'country_visible',
			'state'
		)	