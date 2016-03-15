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
	#firmware    = serializers.PrimaryKeyRelatedField(required=False,queryset=Firmware.objects.all())

	class Meta:
		model  = Manufacture
		fields = ('id','device_sn','device_type','pcba_srl','banner_srl','nimberlink_srl','enclosure_srl','radio_srl','qa_test_number','manufactured_by','date_created','date_last_edited')