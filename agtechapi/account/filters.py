from django.contrib.auth.models import User
import django_filters
from account.models import *

class ProfileFilter(django_filters.FilterSet):
    account_name = django_filters.CharFilter(name="account_name", lookup_type="icontains")

    class Meta:
        model  = Profile
        fields = ['account_name','firstname','lastname','user']

class CustomerFilter(django_filters.FilterSet):
	reseller_name = django_filters.CharFilter(name="profile__reseller_name", lookup_type="icontains")
	company_name  = django_filters.CharFilter(name="profile__company_name", lookup_type="icontains")
	created_by    = django_filters.CharFilter(name="profile__created_by", lookup_type="exact")
	
	class Meta:
		model  = User
        fields = ['reseller_name','company_name','created_by']