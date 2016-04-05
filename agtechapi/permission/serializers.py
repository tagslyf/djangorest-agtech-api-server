from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

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