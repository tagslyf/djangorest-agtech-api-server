from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	id				= models.AutoField(primary_key=True)
	user 			= models.OneToOneField(User,related_name='profile', help_text="Refrence on auth_user")
	first_name 		= models.CharField(max_length=50,blank=True,null=True,  help_text="First name of the account holder.")
	last_name 		= models.CharField(max_length=50,blank=True,null=True,  help_text="Last name of the account holder.")
	contact1 		= models.CharField(max_length=20,blank=True,null=True,  help_text="Primary Contanct Number.")
	contact2 		= models.CharField(max_length=20,blank=True,null=True,  help_text="Seconday Contanct Number.")
	work_address 	= models.CharField(max_length=100,blank=True,null=True, help_text="Work Address of the account.")
	billing_address = models.CharField(max_length=100,blank=True,null=True, help_text="Billing Address of the account.")
	parent 			= models.ForeignKey(User, blank=True,null=True, related_name="account_parent", help_text="Parent id associated with this account.")
	confirmed       = models.BooleanField(default=False, help_text="Email confirmation. True (1) or False (0).")
	created 		= models.DateTimeField(auto_now_add=True, help_text="Date the record was created")
	last_edited     = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, help_text="Date the record was last edited.")
	pass

	class Meta:
		db_table = "userprofile"

