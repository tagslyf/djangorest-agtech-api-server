from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.decorators import detail_route, list_route
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework_gis.filters import InBBoxFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins, filters, status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework import status
from account.serializers import *
from account.models import *
# Create your views here.


class ProfileViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    List all user, or create a new user.
    """
    
    model = Profile
    permission_classes = [IsAuthenticated, IsAdminUser,]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def list(self,request):
    	serializers = ProfileSerializer(self.queryset,many=True)
    	response = {
    		'data' : serializers.data,
    		'status' : 200
    	}

    	return Response(response,status=status.HTTP_200_OK)