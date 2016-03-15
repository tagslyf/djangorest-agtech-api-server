from django.contrib.auth.models import User , Group , Permission
from rest_framework import serializers
from account.models import *
import json


class GroupSerializer(serializers.ModelSerializer):
	"""
	GroupSerializer - used to retrieve , create and update group.
	"""
	name 		= serializers.CharField(required=False, max_length=100)
	permissions = serializers.PrimaryKeyRelatedField(required=False,many=True,queryset=Permission.objects.all())

	# Validation if group name already exist
	def validate_name(self, value):
		duplicate = Group.objects.filter(name=value)
		if(duplicate.count() != 0):
			raise serializers.ValidationError("Group name already exist.")
		return value

	class Meta:
		model = Group
		fields = ('id','name','permissions')


class ProfileSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(required=True,max_length=50, help_text="Display name for the account")
    firstname 	 = serializers.CharField(max_length=30, help_text="First name for billing statement.")
    lastname 	 = serializers.CharField(max_length=30, help_text="Last name for billing statement.")
    email 		 = serializers.EmailField(max_length=100, help_text="Email for billing statement.")
    country 	 = serializers.CharField(max_length=3, default="USA", help_text="Country for billing address.")
    user         = serializers.PrimaryKeyRelatedField(required=False,queryset=User.objects.all())

    class Meta:
    	model  = Profile
    	fields = ('id','account_name','user',
    			   'email','firstname','lastname','phone_number','fax',
    			   'street_address1','street_address2','state',
    			   'city','zipcode','localization','tz_offset','country','billing_company','billing_contact',
    			   'billing_invoice_email','billing_phone','billing_company'
    			 )

    def validate(self, data):
    	request = self.context['request']

    	if request.method == 'POST':
    		if 'user' in data:
    			user_id = data['user']
    			if Profile.objects.filter(user=user_id).count():
    				raise serializers.ValidationError({"detail": "Profile already exists! Please update instead."})

    		if 'account_name' in data:
    			if Profile.objects.filter(account_name=data['account_name']).count():
    				raise serializers.ValidationError({"detail" : "Please try different account name."})

    	return data

class CustomerSerializer(serializers.ModelSerializer):
	groups   = serializers.PrimaryKeyRelatedField(required=False,many=True,queryset=Group.objects.filter(name="Customer"))
	profile  = ProfileSerializer(required=False)
        
	class Meta:
		model  = User
		fields = ('username','groups','profile')


	def create(self, validated_data):
		groups = validated_data.pop('groups');
		profile_data = validated_data.pop('profile', False);

		user = User.objects.create(**validated_data)

		if groups:
			for g in groups:
				user.groups.add(g)

		if profile_data:
			Profile.objects.create(user=user,**profile_data)

		return user
