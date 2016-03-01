from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets, mixins, filters, status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_gis.filters import InBBoxFilter
from account.serializers import *
from account.models import *
# Create your views here.
import django_filters

class AccountFilter(django_filters.FilterSet):
    account_name = django_filters.CharFilter(name="account_name", lookup_type="icontains")

    class Meta:
        model  = Profile
        fields = ['account_name','firstname']

class ProfileViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    List all profile, or create a new profile.
    """
    
    model = Profile
    permission_classes = [IsAuthenticated, IsAdminUser,]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_class    = AccountFilter
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_fields = ('account_name',)
