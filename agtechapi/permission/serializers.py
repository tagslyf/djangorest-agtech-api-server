from django.contrib.auth.models import Permission
from rest_framework import serializers

class PermissionSerializer(serializers.ModelSerializer):
    """
    Create, update and retreive group.
    """
    # Validation if group name already exist
    class Meta:
        model = Permission
        fields = ('id', 'name')