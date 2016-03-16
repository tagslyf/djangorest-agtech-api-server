import django_filters
from django.shortcuts import render
from django.contrib.auth.models import Permission
from rest_framework import viewsets, mixins, filters, status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from permission.serializers import *

# Create your views here.
class PermissionViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    # queryset = Group.objects.all()
    # serializer_class = GroupSerializer
    model               = Permission
    permission_classes  = [IsAuthenticated, IsAdminUser,]
    serializer_class    = PermissionSerializer
    queryset            = Permission.objects.all()