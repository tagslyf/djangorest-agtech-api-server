import django_filters
from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework import viewsets, mixins, filters, status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.http import Http404
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

    def update(self, request, pk, format=None):
    	try:
            groups       = Group.objects.get(pk=pk)
            serializer   = GroupSerializer(groups, data=request.data, context={'request': request})
            response     = {}
            if serializer.is_valid():
                serializer.save() 
                #return updated group details
                return Response(serializer.data,status=status.HTTP_200_OK) 
            #return error if data didn't passed the serialization.  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Group.DoesNotExist:
            raise Http404