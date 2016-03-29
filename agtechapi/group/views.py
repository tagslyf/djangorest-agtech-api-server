import django_filters
from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework import viewsets, mixins, filters, status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from group.serializers import *

# Create your views here.
class GroupViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    # queryset = Group.objects.all()
    # serializer_class = GroupSerializer
    model               = Group
    permission_classes  = [IsAuthenticated, IsAdminUser,]
    serializer_class    = GroupSerializer
    queryset            = Group.objects.all()