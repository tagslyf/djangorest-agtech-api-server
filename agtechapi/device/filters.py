import django_filters
from device.models import *

class ManufactureSerializerFilter(django_filters.FilterSet):
    device_sn    = django_filters.CharFilter(name="device_sn", lookup_type="icontains")

    class Meta:
        model  = Manufacture
        fields = ['device_sn','device_type','pcba_srl']

class DeviceRegistrationFilter(django_filters.FilterSet):
    device_sn    = django_filters.CharFilter(name="device_sn__device_sn", lookup_type="icontains")

    class Meta:
        model  = Registration
        fields = ['account','device_sn']