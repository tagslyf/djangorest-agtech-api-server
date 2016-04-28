from django.contrib.auth.models import User , Group , Permission
from rest_framework import serializers
from account.models import *
import json

class GroupSerializer(serializers.ModelSerializer):
    """
    GroupSerializer - used to retrieve , create and update group.
    """
    name        = serializers.CharField(required=False, max_length=100)
    permissions = serializers.PrimaryKeyRelatedField(required=False,many=True,queryset=Permission.objects.all())

    # Validation if group name already exist
    def validate_name(self, value):
        duplicate = Group.objects.filter(name=value)
        if(duplicate.count() != 0):
            raise serializers.ValidationError("Group name already exist.")
        return value

    class Meta:
        model = Group
        fields = ('id','name','permissions')


class ProfileSerializer(serializers.ModelSerializer):
    account_name  = serializers.CharField(required=False,max_length=50, help_text="Display name for the account")
    reseller_name = serializers.CharField(required=False,max_length=50, default="",help_text="Display name for the account")
    firstname     = serializers.CharField(max_length=30, help_text="First name for billing statement.")
    lastname      = serializers.CharField(max_length=30, help_text="Last name for billing statement.")
    email         = serializers.EmailField(max_length=100, help_text="Email for billing statement.")
    country       = serializers.CharField(max_length=3, default="USA", help_text="Country for billing address.")
    user          = serializers.PrimaryKeyRelatedField(required=False,queryset=User.objects.all())
    email_onboarding = serializers.EmailField(max_length=100, default="",help_text="Email for billing statement.")
    billing_invoice_email = serializers.EmailField(max_length=100, default="",help_text="Billing invoice for billing statement.")

    class Meta:
        model  = Profile
        fields = ('id','account_name','user','reseller_name','company_name','email_onboarding',
                   'email','firstname','lastname','phone_number','fax',
                   'street_address1','street_address2','state',
                   'city','zipcode','localization','tz_offset','country','billing_company','billing_contact',
                   'billing_invoice_email','billing_phone','billing_company','created_by'
                 )

    def validate(self, data):
        request = self.context['request']

        if request.method == 'POST':
            if 'user' in data:
                user_id = data['user']
                if Profile.objects.filter(user=user_id).count():
                    raise serializers.ValidationError({"detail": "Profile already exists! Please update instead."})

            if 'account_name' in data:
                if Profile.objects.filter(account_name=data['account_name']).count():
                    raise serializers.ValidationError({"detail" : "Please try different account name."})

        return data

class OnFarmSerializer(serializers.ModelSerializer):
    customer     = serializers.PrimaryKeyRelatedField(required=True,queryset=User.objects.filter(groups__name="Customer"))
    firstname    = serializers.CharField(max_length=30, help_text="First name for the user account")
    lastname     = serializers.CharField(max_length=30, help_text="Last name for user account.")
    email        = serializers.EmailField(max_length=100,help_text="Email for user account.")
    
    class Meta:
        model = OnFarm
        fields = ('customer','firstname','lastname','email','access','access_instruction')

    # Validation if email already exist
    def validate_email(self, value):
        request = self.context['request']
        if request.method == 'POST':
            duplicate = OnFarm.objects.filter(email=value)
            if(duplicate.count() != 0):
                raise serializers.ValidationError("Email already exist. Please try different email.")
        return value

class CustomerSerializer(serializers.ModelSerializer):
    groups      = serializers.PrimaryKeyRelatedField(required=False,many=True,queryset=Group.objects.filter(name="Customer"),default=Group.objects.filter(name="Customer"))
    profile     = ProfileSerializer(required=False)
    onfarm_user = OnFarmSerializer(read_only=True,many=True)

    class Meta:
        model  = User
        fields = ('username','groups','profile','onfarm_user')


    def create(self, validated_data):
        groups = validated_data.pop('groups');
        profile_data = validated_data.pop('profile', False);

        user = User.objects.create(**validated_data)

        if groups:
            for g in groups:
                user.groups.add(g)

        if profile_data:
            Profile.objects.create(user=user,**profile_data)

        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.save()

        profile_data = validated_data.pop('profile')
        profile      = instance.profile
        
        profile.account_name     = profile_data.get('account_name',profile.account_name)
        profile.reseller_name    = profile_data.get('reseller_name',profile.reseller_name)
        profile.firstname        = profile_data.get('firstname',profile.firstname)
        profile.lastname         = profile_data.get('lastname',profile.lastname)
        profile.company_name     = profile_data.get('company_name',profile.company_name)
        profile.email_onboarding = profile_data.get('email_onboarding',profile.email_onboarding)
        profile.email            = profile_data.get('email',profile.email)
        profile.phone_number     = profile_data.get('phone_number',profile.phone_number)
        profile.fax              = profile_data.get('fax',profile.fax)
        profile.street_address1  = profile_data.get('street_address1',profile.street_address1)
        profile.street_address2  = profile_data.get('street_address2',profile.street_address2)
        profile.state            = profile_data.get('state',profile.state)
        profile.city             = profile_data.get('city',profile.city)
        profile.zipcode          = profile_data.get('zipcode',profile.zipcode)
        profile.localization     = profile_data.get('localization',profile.localization)
        profile.tz_offset        = profile_data.get('tz_offset',profile.tz_offset)
        profile.country          = profile_data.get('country',profile.country)
        profile.billing_company  = profile_data.get('billing_company',profile.billing_company)
        profile.billing_contact  = profile_data.get('billing_contact',profile.billing_contact)
        profile.billing_invoice_email = profile_data.get('billing_invoice_email',profile.billing_invoice_email)
        profile.billing_phone         = profile_data.get('billing_phone',profile.billing_phone)
        profile.save()

        return instance

class AuthSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True,max_length=50)
    password = serializers.CharField(required=True,max_length=100)
    groups   = serializers.PrimaryKeyRelatedField(required=False,queryset=Group.objects.all())

    class Meta:
        model = User
        exclude = ('password','user_permissions','groups')


    def to_representation(self,obj):
        return {
            'id'         : obj.id,
            'username'   : obj.username,
            'first_name' : obj.first_name,
            'last_name'  : obj.last_name,
            'email'      : obj.email,
            'groups'     : obj.groups.values()
        }

class UserSerializer(serializers.ModelSerializer):
    email        = serializers.EmailField(required=True)
    profile      = ProfileSerializer(required=False)

    class Meta:
        model = User
        exclude = ('is_superuser','user_permissions','last_login','date_joined',)
        extra_kwargs = {'password': {'write_only': True , 'required': False}}

    def create(self, validated_data):
        groups       = validated_data.pop('groups');
        profile_data = validated_data.pop('profile', False);
        
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        if groups:
            for g in groups:
                user.groups.add(g)

        if profile_data:
            Profile.objects.create(user=user,**profile_data)

        return user

class DealersSerializer(serializers.ModelSerializer):
    groups   = serializers.PrimaryKeyRelatedField(required=False,many=True,queryset=Group.objects.filter(name="Dealer"),default=Group.objects.filter(name="Dealer"))
    profile  = ProfileSerializer(required=False)
        
    class Meta:
        model  = User
        fields = ('id', 'username','groups','profile')
