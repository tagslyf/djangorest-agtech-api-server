import django_filters
from account.models import *

class ProfileFilter(django_filters.FilterSet):
    account_name = django_filters.CharFilter(name="account_name", lookup_type="icontains")

    class Meta:
        model  = Profile
        fields = ['account_name','firstname','lastname','user']