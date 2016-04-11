from django.contrib import admin
from permission.models import *
# Register your models here.

class PermissionAdmin(admin.ModelAdmin):
    search_fields = ['perm_name',]
    list_display  = ['id','perm_name','perm_key','perm_description','visible','date_created','date_last_edited']

class ACLGroupAdmin(admin.ModelAdmin):
    search_fields = ['group',]
    list_display  = ['id','group','value','date_created','date_last_edited']

class ACLUserAdmin(admin.ModelAdmin):
    search_fields = ['user',]
    list_display  = ['id','user','value','date_created','date_last_edited']

admin.site.register(AclPermission, PermissionAdmin)
admin.site.register(AclGroupPermission, ACLGroupAdmin)
admin.site.register(AclUserPermission, ACLUserAdmin)


