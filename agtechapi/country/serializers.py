from django.contrib.auth.models import Group
from rest_framework import serializers
from country.models import *
import json

class StateSerializer(serializers.ModelSerializer):

	class Meta:
		model = State

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
			'country_visible',
			'state'
		)	