
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from django.shortcuts import render
from rest_framework import viewsets, mixins
from country.serializers import *
from country.models import *

class CountryViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

    model               = Country
    permission_classes  = [IsAuthenticated, IsAdminUser,]
    serializer_class    = CountrySerializer
    queryset            = Country.objects.all()

class StateViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

    model               = State
    permission_classes  = [IsAuthenticated, IsAdminUser,]
    serializer_class    = StateSerializer
    queryset            = State.objects.all()