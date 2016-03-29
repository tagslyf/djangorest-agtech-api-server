"""agtechapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from account import views as account
from device import views as manufacturer
from group import views as group
from permission import views as permission

router = routers.DefaultRouter()
router.register(r'profiles', account.ProfileViewSet)
router.register(r'customer', account.CustomersViewSet, base_name='customer')
router.register(r'auth', account.AuthUser, base_name='auth')
router.register(r'user', account.UserViewSet, base_name='user')
router.register(r'groups', group.GroupViewSet, base_name='groups')
router.register(r'permissions', permission.PermissionViewSet,base_name='permissions')
router.register(r'manufacturer', manufacturer.ManufactureViewSet,base_name='manufacturer')
router.register(r'devices', manufacturer.DeviceRegistrationViewSet,base_name='devices')
router.register(r'firmwares', manufacturer.FirmwareViewSet,base_name="firmwares") 
router.register(r'account/devices', manufacturer.AccountDeviceViewSet,base_name='account_devices')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #url(r'^api/docs/', include('rest_framework_swagger.urls')),
]
