from django.contrib.auth.models import User
from rest_framework import serializers
from account.models import *
import json

class ProfileSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(required=True,max_length=50, help_text="Display name for the account")
    firstname 	 = serializers.CharField(max_length=30, help_text="First name for billing statement.")
    lastname 	 = serializers.CharField(max_length=30, help_text="Last name for billing statement.")
    email 		 = serializers.EmailField(max_length=100, help_text="Email for billing statement.")
    country 	 = serializers.CharField(max_length=3, default="USA", help_text="Country for billing address.")
    user         = serializers.PrimaryKeyRelatedField(required=True,queryset=User.objects.all())

    class Meta:
    	model  = Profile
    	fields = ('id','account_name','user',
    			   'email','firstname','lastname','company','phone_number','fax',
    			   'street_address1','street_address2','state','province',
    			   'city','zipcode','localization','tz_offset','country'
    			 )

   #  def to_representation(self,obj):
   #  	return {
			# 'profile_id'   : obj.id,
			# 'account_name' : obj.account_name,
			# 'firstname'    : obj.firstname,
			# 'username'     : obj.user.username,
			# 'lastname'     : obj.lastname,
			# 'company'      : obj.company,
			# 'phone_number' : obj.phone_number,
			# 'email'        : obj.email,
			# 'address'      : obj.street_address1,
			# 'address2'     : obj.street_address2,
			# 'city'         : obj.city,
			# 'country'      : obj.country,
			# 'date_created' : obj.date_created,
			# 'date_last_edited' : obj.date_last_edited
			# }
	
    def validate(self, data):
    	request = self.context['request']

    	user_id = data['user']

    	if request.method == 'POST':
    		if 'account_name' in data:
    			if Profile.objects.filter(account_name=data['account_name']).count():
    				raise serializers.ValidationError({"detail" : "Please try different account name."})

    			if Profile.objects.filter(user=user_id).count():
    				raise serializers.ValidationError({"detail": "Profile already exists! Please update instead."})

    	return data