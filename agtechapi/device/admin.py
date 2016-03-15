from django.contrib import admin
from django.forms.widgets import Textarea
from django.contrib.gis import admin
from device.models import *

class FirmwareAdmin(admin.ModelAdmin):
    search_fields = ['version',]
    list_display = ['version','firmware_path','date_created','date_last_edited']

class ManufactureDeviceAdmin(admin.ModelAdmin):
	search_fields = ['device_sn',]
	list_display = ['device_sn','device_type','date_created','date_last_edited']

admin.site.register(Firmware, FirmwareAdmin)
admin.site.register(Manufacture, ManufactureDeviceAdmin)