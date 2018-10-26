# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import ConferenceDetail, ConferenceLocation, ConferencePage, ConferenceSponsor, Speaker, SessionLocation, \
    Proposal, Price, NavBarItem

# TODO - beef up admin models

class ConferenceLocationAdmin(admin.ModelAdmin):
    pass

class ConferencePageAdmin(admin.ModelAdmin):
    exclude = ['slug']

class ConferenceSponsorAdmin(admin.ModelAdmin):
    exclude = ['slug']

class ConferenceDetailAdmin(admin.ModelAdmin):
    pass

class SpeakerAdmin(admin.ModelAdmin):
    exclude = ['slug']

class SessionLocationAdmin(admin.ModelAdmin):
    pass

class ProposalAdmin(admin.ModelAdmin):
    exclude = ['slug']

class PriceAdmin(admin.ModelAdmin):
    exclude = ['slug']

class NavBarItemAdmin(admin.ModelAdmin):
    exclude = ['slug']

# Register your models here.
admin.site.register(ConferenceLocation, ConferenceLocationAdmin)
admin.site.register(ConferencePage, ConferencePageAdmin)
admin.site.register(ConferenceSponsor, ConferenceSponsorAdmin)
admin.site.register(ConferenceDetail, ConferenceDetailAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(SessionLocation, SessionLocationAdmin)
admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(NavBarItem, NavBarItemAdmin)
