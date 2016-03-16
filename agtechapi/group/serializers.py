from django.contrib.auth.models import Group, Permission
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    """
    Create, update and retreive group.
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
        fields = ('id', 'name', 'permissions')