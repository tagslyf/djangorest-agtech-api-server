import django_filters
from django.shortcuts import render
from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, mixins, filters, status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from permission.serializers import *
from permission.models import *

# Create your views here.
class PermissionViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    # queryset = Group.objects.all()
    # serializer_class = GroupSerializer
    model               = AclPermission
    permission_classes  = [IsAuthenticated, IsAdminUser,]
    serializer_class    = ACLPermissionSerializer
    queryset            = AclPermission.objects.all()


class GroupPermissionViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    # queryset = Group.objects.all()
    # serializer_class = GroupSerializer
    model               = AclGroupPermission
    permission_classes  = [IsAuthenticated, IsAdminUser,]
    serializer_class    = ACLGroupPermissionSerializer
    queryset            = AclGroupPermission.objects.all()


class ContentTypeViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	API endpoint that allows content type to be viewed.
	"""
	model 				= ContentType
	contenttype_classes = [IsAuthenticated, IsAdminUser,]
	serializer_class    = ContentTypeSerializer
	queryset            = ContentType.objects.all()