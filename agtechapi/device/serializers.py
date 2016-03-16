from django.contrib.auth.models import User
from rest_framework import serializers
from device.models import *
import uuid

class FirmwareSerializer(serializers.ModelSerializer):
	
	class Meta:
		model  = Firmware
		fields = ('version','firmware_path')

class ManufactureDeviceSerializer(serializers.ModelSerializer):
	device_sn   = serializers.UUIDField(required=False,default=uuid.uuid4,read_only=True)
	device_type = serializers.ChoiceField(required=True,choices=DEVICE_TYPE_OPTIONS)
	manufactured_by = serializers.PrimaryKeyRelatedField(required=True,queryset=User.objects.filter(groups__name="Manufacturer"))
	
	class Meta:
		model  = Manufacture
		fields = ('id','device_sn','device_type','pcba_srl','banner_srl','nimberlink_srl','enclosure_srl','radio_srl','qa_test_number','manufactured_by','date_created','date_last_edited')

class DeviceRegistrationSerializer(serializers.ModelSerializer):
	account    = serializers.PrimaryKeyRelatedField(required=True,queryset=User.objects.filter(groups__name="Customer"))
	
	class Meta:
		model  = Registration
		fields = ('id','account','device_sn','firmware','battery_status','radio_signal_status','cell_signal_status','memory_orig_size','memory_available_size','internal_temp_status','external_temp_status','accelerometer_status','charging_status','registration_type','status','date_created','date_last_edited')

