from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class AclPermission(models.Model):
	id				 = models.AutoField(primary_key=True)
	perm_name 		 = models.CharField(max_length=50, blank=True,null=True, help_text="Name of the permission.")
	perm_key 		 = models.CharField(max_length=50 ,blank=True,null=True , help_text="Key/Function name of the permission.")
	perm_icon        = models.CharField(max_length=20 ,blank=True,null=True , help_text="Sidebar menu class icon.")
	perm_description = models.CharField(max_length=100 ,blank=True,null=True, help_text="Description of the permission.")
	visible          = models.BooleanField(default=True, help_text="If visible in the sidebar menu.")
	date_created  	 = models.DateTimeField(auto_now=False, auto_now_add=True, help_text="Date the record was created")
	date_last_edited = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, help_text="Date the record was last edited.")

	def __unicode__(self):
		return u'%s' % (self.perm_key)

	class Meta:
		db_table = "acl_permission"

class AclGroupPermission(models.Model):
	id         		 = models.AutoField(primary_key=True)
	group      		 = models.OneToOneField(Group,related_name="access", help_text="Group that you want to have permission.")
	permission 		 = models.ManyToManyField(AclPermission)
	value      		 = models.BooleanField(default=True)
	date_created  	 = models.DateTimeField(auto_now=False, auto_now_add=True, help_text="Date the record was created")
	date_last_edited = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, help_text="Date the record was last edited.")

	def __unicode__(self):
		return u'%s-Permission' % (self.group)

	class Meta:
		db_table = "acl_group_permission"

class AclUserPermission(models.Model):
	id         		 = models.AutoField(primary_key=True)
	user      		 = models.OneToOneField(User,related_name="access", help_text="User that you want to have permission.")
	permission 		 = models.ManyToManyField(AclPermission,related_name="acl_user_permission", help_text="Permission id")
	value      		 = models.BooleanField(default=True)
	date_created  	 = models.DateTimeField(auto_now=False, auto_now_add=True, help_text="Date the record was created")
	date_last_edited = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, help_text="Date the record was last edited.")

	def __unicode__(self):
		return u'%s: %s' % (self.user, self.permission)
	
	class Meta:
		db_table = "acl_user_permission"



