from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser
from rest_framework import filters
from rest_framework import viewsets, mixins, filters, status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from account.serializers import *
from account.filters import *
from account.models import *
# Create your views here.
import django_filters

class ProfileViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    List all user, or create a new profile.
    """
    
    model              = Profile
    permission_classes = [IsAuthenticated, IsAdminUser,]
    serializer_class   = ProfileSerializer
    queryset           = Profile.objects.all()
    filter_class       = ProfileFilter
    filter_backends    = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_fields      = ('id','account_name','firstname','lastname','user')

    def retrieve(self, request, pk=None):
        try:
            account    = Profile.objects.get(user=pk)
            serializer = ProfileSerializer(account)
            response   = {}
            response   = serializer.data
            return Response(response,status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            raise Http404
    
    def update(self, request, pk, format=None):
        try:
            account      = Profile.objects.get(user=pk)
            serializer   = ProfileSerializer(account, data=request.data, context={'request': request})
            response     = {}
            if serializer.is_valid():
                serializer.save() 
                #return updated profile details
                return Response(serializer.data,status=status.HTTP_200_OK) 
            #return error if data didn't passed the serialization.  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            raise Http404
    
class CustomersViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    List all customers, or create a new customer.
    """

    model = User
    permission_classes = [IsAuthenticated, IsAdminUser,]
    serializer_class   = CustomerSerializer
    queryset           = User.objects.filter(groups__name="Customer")
    filter_class       = CustomerFilter
    filter_backends    = (filters.OrderingFilter, filters.DjangoFilterBackend)

class AuthUser(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Login Authentication
    """
    model               = User
    permission_classes  = [IsAuthenticated, IsAdminUser,]
    serializer_class    = AuthSerializer
    queryset            = User.objects.all()

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        response = {}
        serializer = AuthSerializer(data=data)
        
        if serializer.is_valid():
            username = data['username']
            password = data['password']

            auth = authenticate(username=username, password=password)
            
            if auth:
                if auth.is_active:
                    serializer = AuthSerializer(auth)
                    return Response(serializer.data,status=status.HTTP_200_OK)
                else:
                    response['error'] = 'User is inactive.'
                    return Response(response,status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    auth = User.objects.get(email=username)
                    if auth.check_password(password):
                        if auth.is_active:
                            serializer = AuthSerializer(auth)
                            return Response(serializer.data,status=status.HTTP_200_OK)
                        else:
                           response['error'] = 'User is inactive.'
                           return Response(response,status=status.HTTP_400_BAD_REQUEST)
                    else:
                        response['error'] = 'Invalid Username and/or Password'
                        return Response(response,status=status.HTTP_400_BAD_REQUEST)
                except User.DoesNotExist:
                    response['error'] = 'User does not exist'
                    return Response(response,status=status.HTTP_400_BAD_REQUEST)

        response['error'] = serializer.errors 
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
     
class UserViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    List of all users. create and update user.
    """
    model               = User
    permission_classes  = [IsAuthenticated, IsAdminUser,]
    serializer_class    = UserSerializer
    queryset            = User.objects.all()
