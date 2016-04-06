from django.contrib.auth.models import User
from rest_framework import serializers
from device.models import *
import uuid

class FirmwareSerializer(serializers.ModelSerializer):
	
	class Meta:
		model  = Firmware
		fields = ('id','version','firmware_path')

class ManufactureDeviceSerializer(serializers.ModelSerializer):
	device_sn   = serializers.UUIDField(required=False,read_only=True)
	device_type = serializers.ChoiceField(required=True,choices=DEVICE_TYPE_OPTIONS)
	manufactured_by = serializers.PrimaryKeyRelatedField(required=True,queryset=User.objects.filter(groups__name="Manufacturer"))
	
	class Meta:
		model  = Manufacture
		fields = ('id','device_sn','device_type','pcba_srl','banner_srl','nimberlink_srl','enclosure_srl','radio_srl','qa_test_number','manufactured_status','manufactured_by','date_created','date_last_edited')
	def create(self, validated_data):
		validated_data['device_sn'] = uuid.uuid4()
		return Manufacture.objects.create(**validated_data)


class DeviceRegistrationSerializer(serializers.ModelSerializer):
	account    = serializers.PrimaryKeyRelatedField(required=True,queryset=User.objects.filter(groups__name="Customer"))
	device_sn  = serializers.PrimaryKeyRelatedField(required=True,queryset=Manufacture.objects.exclude(device_sn__in=Registration.objects.filter(status='A').values_list('device_sn', flat=True)))

	class Meta:
		model  = Registration
		fields = ('account','device_sn','firmware','battery_status','radio_signal_status','cell_signal_status','memory_orig_size','memory_available_size','internal_temp_status','external_temp_status','accelerometer_status','charging_status','registration_type','registered_ip','status','date_created','date_last_edited')

	def to_representation(self,obj):
		return {
			'account_id'     : obj.account.id,
			'device_sn'      : obj.device_sn.device_sn,
			'device_type'    : dict(DEVICE_TYPE_OPTIONS)[obj.device_sn.device_type],
			'firmware'       : obj.firmware.version,
			'battery_status' : obj.battery_status,
			'radio_signal_status'   : obj.radio_signal_status,
			'cell_signal_status'    : obj.cell_signal_status,
			'memory_orig_size' 	    : obj.memory_orig_size,
			'memory_available_size' : obj.memory_available_size,
			'internal_temp_status'  : obj.internal_temp_status,
			'external_temp_status'  : obj.external_temp_status,
			'accelerometer_status'  : obj.accelerometer_status,
			'charging_status'       : obj.charging_status,
			'registration_type'     : dict(REGISTER_TYPE_OPTIONS)[obj.registration_type],
			'registered_ip'         : obj.registered_ip,
			'serial_numbers' : {
				'pcba_srl'   : obj.device_sn.pcba_srl,
				'banner_srl' : obj.device_sn.banner_srl,
				'nimberlink_srl' : obj.device_sn.nimberlink_srl,
				'enclosure_srl'  : obj.device_sn.enclosure_srl,
				'radio_srl'      : obj.device_sn.radio_srl,
				'qa_test_number' : obj.device_sn.qa_test_number

			}
		}



class AccountDeviceSerializer(serializers.ModelSerializer):
	device_account = DeviceRegistrationSerializer(required=False,many=True)

	class Meta:
		model  = User