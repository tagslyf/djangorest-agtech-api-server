from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.forms.widgets import Textarea
from django.contrib.gis import admin
from account.models import *

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['account_name',]
    list_display = ['account_name','firstname','lastname','email','date_created','date_last_edited']

admin.site.register(Profile, ProfileAdmin)
