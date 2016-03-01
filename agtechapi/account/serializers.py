from django.contrib.auth.models import User
from rest_framework import serializers
from account.models import *
import json

class ProfileSerializer(serializers.ModelSerializer):
	username        = serializers.CharField(source="user.username",required=False)
	account_name	= serializers.CharField(required=True,max_length=100)

	class Meta:
		model  = Profile
		fields = ('id','username','account_name','firstname','lastname','country')