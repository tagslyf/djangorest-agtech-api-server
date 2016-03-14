from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

DEVICE_TYPE_OPTIONS = (
    ('N', 'Node'),
    ('G', 'Gateway')
)

MANUFACTURE_STATUS = (
    ('M', 'Manufactured'),
    ('T', 'Taken'),
    ('D', 'Deployed')
)

class Firmware(models.Model):
	id = models.AutoField(primary_key=True)
	version 	  = models.CharField(max_length=30, unique=True, help_text="Firmware version. Ex. v1.0b, v2.0")
	firmware_path = models.FileField(upload_to='firmware', null=True, blank=True)
	date_created  = models.DateTimeField(auto_now=False, auto_now_add=True, help_text="Date the record was created")
	date_last_edited = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, help_text="Date the record was last edited.")

	def __unicode__(self):
		return u'%s' % (self.version)

class Manufacture(models.Model):
    id = models.AutoField(primary_key=True)
    device_sn = models.CharField(max_length=80, unique=True, help_text="Serial number, by default uuid4")
    device_type = models.CharField(max_length=1, db_index=True, choices=DEVICE_TYPE_OPTIONS, help_text="Device type. N=Node,G=Gateway")
    pcba_srl = models.CharField(max_length=30, null=True, blank=True,help_text="PCBA Serial Number of the Manufactured device.")
    banner_srl = models.CharField(max_length=30,null=True, blank=True,help_text="Banner Serial Number of the Manufactured device.")
    nimberlink_srl = models.CharField(max_length=30,null=True, blank=True,help_text="Nimberlink Serial Number of the Manufactured device.")
    enclosure_srl = models.CharField(max_length=30,null=True, blank=True,help_text="Enclosure Serial Number of the Manufactured device.")
    radio_srl = models.CharField(max_length=30,null=True, blank=True,help_text="Radio Serial Number of the Manufactured device.")
    qa_test_number = models.CharField(max_length=30,null=True, blank=True,help_text="QA Test Number of the Manufactured device.")
    firmware = models.ForeignKey(Firmware,related_name="firmware_version", default="1", null=True, blank=True,help_text="Current Firmware Version of the device.")
    manufactured_by  = models.ForeignKey(User,related_name="created_devices", default="1", help_text="User who manufactured the device.")
    manufactured_status = models.CharField(max_length=1, db_index=True, default="M", choices=MANUFACTURE_STATUS, help_text="Device manufactured status.")       
    date_created     = models.DateTimeField(auto_now_add=True, help_text="Date the record was created")
    date_last_edited = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, help_text="Date the record was last edited.")

    def __unicode__(self):
        return u'%s' % (self.device_sn)