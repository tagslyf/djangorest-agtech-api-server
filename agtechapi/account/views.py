from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import filters
from rest_framework import viewsets, mixins, filters, status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView
from account.serializers import *
from account.models import *
# Create your views here.
import django_filters

class AccountFilter(django_filters.FilterSet):
    account_name = django_filters.CharFilter(name="account_name", lookup_type="icontains")
    first_name   = django_filters.CharFilter(name="first_name", lookup_type="icontains")

    class Meta:
        model  = Profile
        fields = ['account_name','firstname']

class ProfileViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    List all user, or create a new profile.
    """
    
    model = Profile
    permission_classes = [IsAuthenticated, IsAdminUser,]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_class    = AccountFilter
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_fields = ('id','account_name','firstname','lastname')

class CustomersViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    List all customers, or create a new customer.
    """

    model = User
    permission_classes = [IsAuthenticated, IsAdminUser,]
    serializer_class   = CustomerSerializer
    queryset = User.objects.filter(groups__name="Customer")

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

        if all(x in data for x in ['username','password']):
            username = data['username']
            password = data['password']

            try:
                auth = User.objects.get(username=username)
                if auth.check_password(password):
                    serializer       = AuthSerializer(auth)
                    status           = 200
                    response['data'] = serializer.data
                else:
                    status            = 400
                    response['error'] = 'Invalid Username and/or Password'
            except User.DoesNotExist:
                status = 400
                response['error'] = 'User does not exist'
        else:
            status = 400
            response['error'] = 'Incorrect Parameter/s'

        return Response(response, status=status)

class UserViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    List of all users. create and update user.
    """
    model               = User
    permission_classes  = [IsAuthenticated, IsAdminUser,]
    serializer_class    = UserSerializer
    queryset            = User.objects.all()
