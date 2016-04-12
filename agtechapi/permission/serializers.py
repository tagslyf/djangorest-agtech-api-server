from django.contrib.auth.models import Permission
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from permission.models import *

class ACLPermissionSerializer(serializers.ModelSerializer):
    visible = serializers.BooleanField(required=False,default=False)

    class Meta:
        model  = AclPermission
        fields = ('id', 'perm_name','perm_key','perm_icon','perm_description','visible')


class ACLGroupPermissionSerializer(serializers.ModelSerializer):
    permission = serializers.PrimaryKeyRelatedField(many=True , queryset=AclPermission.objects.all())

    class Meta:
        model  = AclGroupPermission
        fields = ('group','permission')

class ACLUserPermissionSerializer(serializers.ModelSerializer):
    permission = serializers.PrimaryKeyRelatedField(many=True , queryset=AclPermission.objects.all())

    class Meta:
        model  = AclUserPermission
        fields = ('user','permission')

class PermissionSerializer(serializers.ModelSerializer):
    """
    Create, update and retreive permission.
    """
    content_type = serializers.SlugRelatedField(required=True,slug_field='model',queryset=ContentType.objects.all())
    codename     = serializers.CharField(required=True,max_length=20)

    class Meta:
        model = Permission
        fields = ('id', 'name','codename','content_type')

class ContentTypeSerializer(serializers.ModelSerializer):
    """
    Create, update and retreive content type.
    """

    class Meta:
        model = ContentType
        fields = ('id', 'name', 'model')