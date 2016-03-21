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
from device.filters import *
from device.models import *
# Create your views here

class ManufactureViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    List all device manufactured, or manufacture a new device.
    """
    
    model = Manufacture
    permission_classes = [IsAuthenticated, IsAdminUser,]
    serializer_class   = ManufactureDeviceSerializer
    queryset 		   = Manufacture.objects.all()
    filter_class       = ManufactureSerializerFilter
    filter_backends    = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_fields      = ('device_sn','device_type','pcba_srl')


class FirmwareViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    List all device manufactured, or manufacture a new device.
    """
    
    model = Firmware
    permission_classes = [IsAuthenticated, IsAdminUser,]
    serializer_class   = FirmwareSerializer
    queryset           = Firmware.objects.all()

class DeviceRegistrationViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    List all device registered, or register a new device.
    """
    
    model = Registration
    permission_classes = [IsAuthenticated, IsAdminUser,]
    serializer_class   = DeviceRegistrationSerializer
    queryset           = Registration.objects.all()
    filter_class       = DeviceRegistrationFilter
    filter_backends    = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_fields      = ('device_sn')

class AccountDeviceViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,viewsets.GenericViewSet):
    model = User
    permission_classes = [IsAuthenticated, IsAdminUser,]
    serializer_class   = AccountDeviceSerializer
    queryset           = User.objects.all()
