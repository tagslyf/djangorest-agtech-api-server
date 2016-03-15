from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets, mixins, filters, status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView
from device.serializers import *
from device.models import *
# Create your views here
import django_filters

class ManufactureSerializerFilter(django_filters.FilterSet):
    device_sn    = django_filters.CharFilter(name="device_sn", lookup_type="icontains")

    class Meta:
        model  = Manufacture
        fields = ['device_sn','device_type','pcba_srl']

class ManufactureViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    List all device manufactured, or manufacture a new device.
    """
    
    model = Manufacture
    permission_classes = [IsAuthenticated, IsAdminUser,]
    serializer_class = ManufactureDeviceSerializer
    queryset 		 = Manufacture.objects.all()
    filter_class     = ManufactureSerializerFilter
    filter_backends  = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_fields    = ('device_sn','device_type','pcba_srl')

class DeviceRegistrationViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    List all device registered, or register a new device.
    """
    
    model = Registration
    permission_classes = [IsAuthenticated, IsAdminUser,]
    serializer_class   = DeviceRegistrationSerializer
    queryset           = Registration.objects.all()
    #filter_class     = ManufactureSerializerFilter
    #filter_backends  = (filters.OrderingFilter, filters.DjangoFilterBackend)
    #filter_fields    = ('device_sn','device_type','pcba_srl')
