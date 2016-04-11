from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from permission.models import *


class GroupPermissionSerializer(serializers.ModelSerializer):
    permission = serializers.SlugRelatedField(required=False ,many=True,slug_field='perm_key', queryset=AclPermission.objects.all())

    class Meta:
        model  = AclGroupPermission
        fields = ('permission',)

class GroupSerializer(serializers.ModelSerializer):
    """
    Create, update and retreive group.
    """
    name    = serializers.CharField(required=True, max_length=100)
    access  = GroupPermissionSerializer(required=False)
    # permissions = serializers.PrimaryKeyRelatedField(required=False,many=True,queryset=Permission.objects.all())
    
    # Validation if group name already exist
    def validate_name(self, value):
        request = self.context['request']
        if request.method == 'POST':
            duplicate = Group.objects.filter(name=value)
            if(duplicate.count() != 0):
                raise serializers.ValidationError("Group name already exist.")
        return value

    class Meta:
        model = Group
        fields = ('id', 'name', 'access')

    def create(self, validated_data):
        permission_data = validated_data.pop('access', False);

        group = Group.objects.create(**validated_data)

        if permission_data:
            group_permission = AclGroupPermission.objects.create(group=group)
            group_permission.permission = permission_data.get('permission')
            group_permission.save()
        else:
            group_permission = AclGroupPermission.objects.create(group=group)

        return group
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        if(validated_data.get('access')):
            permission_data  = validated_data.pop('access')
            try:
                group_permission = instance.access
                group_permission.permission = permission_data.get('permission',group_permission.permission)
                group_permission.save()
            except:
                group_permission = AclGroupPermission.objects.create(group=instance)
                group_permission.permission = permission_data.get('permission')
                group_permission.save()

        return instance