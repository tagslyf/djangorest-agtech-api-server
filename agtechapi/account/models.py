from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

TZ_OFFSET_OPTIONS = (
    ('+00:00','Dublin, London, Edinburgh'),
    ('+01:00','Amsterdam, Belgrade, Berlin'),
    ('+02:00','Athens, Cairo, Helsinki'),
    ('+03:00','Kuwait, Moscow, Nairobi'),
    ('+04:00','Kabul, Yerevan, Tbilisi'),
    ('+05:00','Islamabad, Karachi, Tashkent'),
    ('+05:30','New Delhi, Mumbai, Chennai'),
    ('+05:45','Kathmandu'),
    ('+06:00','Dhaka, Novosibirsk, Dhaka'),
    ('+06:30','Rangoon'),
    ('+07:00','Jakarta, Hanoi, Bangkok'),
    ('+08:00','Taipei, Singapore, Kuala Lumpur'),
    ('+09:00','Osaka, Seoul, Tokyo'),
    ('+09:30','Darwin, London, Edinburgh'),
    ('+10:00','Guam, Brisbane, Magadan'),
    ('+10:30','Adelaide'),
    ('+11:00','Sydney, Melbourne, Canberra'),
    ('+12:00','Kamchatka, Marshall Is.'),
    ('+13:00','Wellington, Auckland, Fiji'),
    ('+13:45','Chatham Is.'),
    ('+14:00','Samoa'),
    ('-01:00','Azores, Cape Verde Is.'),
    ('-02:00','Brasilia, Mid-Atlantic'),
    ('-03:00','Buenos Aires, Greenland, Santiago'),
    ('-03:30','Newfoundland'),
    ('-04:00','Atlantic Time (Canada), Georgetown, La Paz'),
    ('-04:30','Caracas'),
    ('-05:00','Bogota, Eastern Time (US & Canada), Indiana (East)'),
    ('-06:00','Central America, Central Time (US & Canada)'),
    ('-07:00','Arizona, Chihuahua, Mazatlan, Mountain Time (US & Canada) '),
    ('-08:00','Pacific Time (US & Canada), Tijuana '),
    ('-09:00','Alaska'),
    ('-10:00','Hawaii'),
    ('-11:00','American Samoa, International Date Line West, Midway Island'),
)

LOCALIZATION_OPTIONS = (
    ('fr_BE', 'French / Belgium'),
    ('fr_CA', 'French / Canada'),
    ('en_IN', 'English / India'),
    ('en_IE', 'English / Ireland'),
    ('en_ZA', 'English / Zimbabwe'),
)

ONFARM_ACCESS = (
    ('full', 'Full Access'),
    ('limited', 'Limited Access')
)

class Profile(models.Model):
    id                  = models.AutoField(primary_key=True)
    user                = models.OneToOneField(User,related_name="profile", help_text="User who owned the account.")
    account_name        = models.CharField(max_length=50, null=True, blank=True,help_text="Account name that will be displayed on the Dashboard.")
    reseller_name       = models.CharField(max_length=50, null=True, blank=True, help_text="Reseller name that will be displayed on the Dashboard.")
    company_name        = models.CharField(max_length=50, help_text="Company of the account holder")
    email_onboarding    = models.CharField(max_length=50, null=True, blank=True, help_text="Email for Onboarding Communication")
    firstname           = models.CharField(max_length=30, help_text="First name of the contact.")
    lastname            = models.CharField(max_length=30, help_text="Last name of the contact.")
    email               = models.EmailField(max_length=100, help_text="Primay email address of the contact.")
    phone_number        = models.CharField(max_length=20, null=True, blank=True, help_text="Phone number of the grower point of contact.")
    fax                 = models.CharField(max_length=20, null=True, blank=True, help_text="Fax Number for billing statement.")
    street_address1     = models.CharField(max_length=100, null=True, blank=True, help_text="Street Address 1 for billing address.")
    street_address2     = models.CharField(max_length=100, null=True, blank=True, help_text="Street Address 2 for billing address.")
    city                = models.CharField(max_length=50, null=True, blank=True, help_text="City for billing address.")
    state               = models.CharField(max_length=2, db_index=True, null=True, blank=True, help_text="State for billing address.")
    zipcode             = models.CharField(max_length=10, null=True, blank=True, help_text="Zip Code for billing address.")
    country             = models.CharField(max_length=3, default="USA", help_text="Country for billing address.")
    localization        = models.CharField(max_length=10, db_index=True, default="en_IE", choices=LOCALIZATION_OPTIONS, help_text="Default Language / Localization")
    tz_offset           = models.CharField(max_length=20, db_index=True, default="+08:00", choices=TZ_OFFSET_OPTIONS, help_text="Default Timezone Offset")
    #Billing Information
    billing_contact         = models.CharField(max_length=20, null=True, blank=True, help_text="Contact Number for billing statement.")
    billing_invoice_email   = models.EmailField(max_length=100, null=True, blank=True, help_text="Email address for the invoices.")
    billing_phone           = models.CharField(max_length=20, null=True, blank=True, help_text="Phone number of the grower point of contact.")
    billing_company         = models.CharField(max_length=100, null=True, blank=True, help_text="Company Name for billing statement.")
    created_by              = models.ForeignKey(User,related_name="account_created", help_text="User who created the account", null=True, blank=True)
    date_created            = models.DateTimeField(auto_now=False, auto_now_add=True, help_text="Date the record was created")
    date_last_edited        = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, help_text="Date the record was last edited.")

class OnFarm(models.Model):
    id                 = models.AutoField(primary_key=True)
    customer           = models.ForeignKey(User,related_name="onfarm_user", help_text="Customer of that owns the user.")
    firstname          = models.CharField(max_length=30, help_text="First name of the onfarm user.")
    lastname           = models.CharField(max_length=30, help_text="Last name of the onfarm user.")
    email              = models.EmailField(max_length=100,  unique=True, help_text="Primay email address of the onfarm user.")
    access             = models.CharField(max_length=10, db_index=True, default="en_IE", choices=ONFARM_ACCESS, help_text="User access to Onfarm.")
    access_instruction = models.TextField(null=True, blank=True)
    date_created       = models.DateTimeField(auto_now=False, auto_now_add=True, help_text="Date the record was created")
    date_last_edited   = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True, help_text="Date the record was last edited.")

