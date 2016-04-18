import django_filters
from device.models import *

class ManufactureSerializerFilter(django_filters.FilterSet):
    device_sn       = django_filters.CharFilter(name="device_sn", lookup_type="icontains")
    in_stock        = django_filters.MethodFilter(action='device_in_stock')
    manufactured_by = django_filters.CharFilter(name="manufactured_by", lookup_type="exact")

    def device_in_stock(self, queryset, value):
    	if value == False:
    		return queryset.filter(device_sn__in=Registration.objects.filter(status='A').values_list('device_sn', flat=True))
    	else:
    		return queryset.exclude(device_sn__in=Registration.objects.filter(status='A').values_list('device_sn', flat=True))

    class Meta:
        model  = Manufacture
        fields = ['device_sn','firmware','device_type','pcba_srl','in_stock','manufactured_by']

class DeviceRegistrationFilter(django_filters.FilterSet):
    device_sn    = django_filters.CharFilter(name="device_sn__device_sn", lookup_type="icontains")

    class Meta:
        model  = Registration
        fields = ['account','device_sn']