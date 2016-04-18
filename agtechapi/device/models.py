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

STATUS_OPTIONS = (
    ('A', 'Active'),
    ('I', 'Inactive'),
    ('D', 'Deleted')
)

REGISTER_TYPE_OPTIONS = (
    ('B', 'on Boot'),
    ('E', 'on Edit of Configurations'),
    ('M', 'on Manual Registration'),
    ('R', 'on Request'),
    ('I', 'on Interval Post Execution'),
)

class Firmware(models.Model):
    id            = models.AutoField(primary_key=True)
    version       = models.CharField(max_length=30, unique=True, help_text="Firmware version. Ex. v1.0b, v2.0")
    firmware_path = models.FileField(upload_to='firmware', null=True, blank=True)
    date_created  = models.DateTimeField(auto_now=False, auto_now_add=True, help_text="Date the record was created")
    date_last_edited = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, help_text="Date the record was last edited.")

    def __unicode__(self):
        return u'%s' % (self.version)

class Manufacture(models.Model):
    id               = models.AutoField(primary_key=True)
    device_sn        = models.CharField(max_length=80, unique=True, help_text="Serial number, by default uuid4")
    device_type      = models.CharField(max_length=1, db_index=True, choices=DEVICE_TYPE_OPTIONS, help_text="Device type. N=Node,G=Gateway")
    pcba_srl         = models.CharField(max_length=30, null=True, blank=True,help_text="PCBA Serial Number of the Manufactured device.")
    banner_srl       = models.CharField(max_length=30,null=True, blank=True,help_text="Banner Serial Number of the Manufactured device.")
    nimberlink_srl   = models.CharField(max_length=30,null=True, blank=True,help_text="Nimberlink Serial Number of the Manufactured device.")
    enclosure_srl    = models.CharField(max_length=30,null=True, blank=True,help_text="Enclosure Serial Number of the Manufactured device.")
    radio_srl        = models.CharField(max_length=30,null=True, blank=True,help_text="Radio Serial Number of the Manufactured device.")
    qa_test_number   = models.CharField(max_length=30,null=True, blank=True,help_text="QA Test Number of the Manufactured device.")
    manufactured_by  = models.ForeignKey(User,related_name="created_devices", default="1", help_text="User who manufactured the device.")
    manufactured_status = models.CharField(max_length=1, db_index=True, default="M", null=True, blank=True,choices=MANUFACTURE_STATUS, help_text="Device manufactured status.")       
    firmware         = models.ForeignKey(Firmware,to_field="version",related_name="device_firmware", help_text="Current firmware version of the device.")
    date_created     = models.DateTimeField(auto_now_add=True, help_text="Date the record was created")
    date_last_edited = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, help_text="Date the record was last edited.")

    def __unicode__(self):
        return u'%s' % (self.device_sn)

class Registration(models.Model):
    id                    = models.AutoField(primary_key=True)
    account               = models.ForeignKey(User,related_name="device_account", help_text="Account who owns the device.")
    device_sn             = models.OneToOneField('Manufacture', to_field="device_sn", related_name="device_manufactured", help_text="Serial Number of the device manufactured.")   
    battery_status        = models.FloatField(null=True, blank=True, help_text="Battery status by percentage.")
    radio_signal_status   = models.FloatField(null=True, blank=True, help_text="Radio Signal strength by percentage.")
    cell_signal_status    = models.FloatField(null=True, blank=True, help_text="Cellular Network Signal strength by percentage.")
    memory_orig_size      = models.FloatField(null=True, blank=True, help_text="Memory original size in MB")
    memory_available_size = models.FloatField(null=True, blank=True, help_text="Memory available space in MB.")
    internal_temp_status  = models.FloatField(null=True, blank=True, help_text="Device inner temperature in celcius.")
    external_temp_status  = models.FloatField(null=True, blank=True, help_text="Device external temperature in celcius.")
    charging_status       = models.BooleanField(default=False, help_text="Battery charging status. True (1) or False (0).")
    accelerometer_status  = models.FloatField(null=True, blank=True, help_text="Accelerometer's azimuthal angle. Value is from 0 to 180 degrees.")
    registration_type     = models.CharField(max_length=1, db_index=True, default="B", choices=REGISTER_TYPE_OPTIONS, help_text="Action that triggers registration - B - on Boot (default), R - on Request, M - on Manual Registration, E - on Edit of Configurations")
    registered_ip         = models.GenericIPAddressField(null=True, blank=True, help_text="IP address of registered transmitter.")
    status                = models.CharField(max_length=1, db_index=True, default='A', choices=STATUS_OPTIONS, help_text="Active (default) / Inactive / Deleted")
    dealer                = models.ForeignKey(User,related_name="dealer_account", help_text="Dealer who assigns the device.", null=True, blank=True)
    date_created          = models.DateTimeField(auto_now=False, auto_now_add=True, help_text="Date the record was created")
    date_last_edited      = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, help_text="Date the record was last edited.")
    
    def __unicode__(self):
        return u'%s' % (self.device_sn)