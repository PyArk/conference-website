# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import *

def sponsorForm(request):
    navbar = NavBarItem.objects.filter(isActive=True)
    speakers = Speaker.objects.all()
    schedule = Proposal.objects.filter(accepted=True)
    conferenceDetail = ConferenceDetail.objects.all()

    return render(request, "main/sponsorForm.html",{'speakers': speakers,
                   'schedule': schedule,
                   'banner': conferenceDetail[0],
                   'navbar': navbar})

def proposalForm(request):
    navbar = NavBarItem.objects.filter(isActive=True)
    speakers = Speaker.objects.all()
    schedule = Proposal.objects.filter(accepted=True)
    conferenceDetail = ConferenceDetail.objects.all()

    return render(request, "main/proposalForm.html",{'speakers': speakers,
                   'schedule': schedule,
                   'banner': conferenceDetail[0],
                   'navbar': navbar})

# TODO: Implement some views
def index(request):
    ''' home page 
    '''
    navbar = NavBarItem.objects.filter(isActive=True)
    speakers = Speaker.objects.all()
    schedule = Proposal.objects.filter(accepted=True)
    conferenceDetail = ConferenceDetail.objects.all()


    # TODO: Fix this so it's not so dangerous....
    return render(request, 'main/index.html',
                  {'speakers': speakers,
                   'schedule': schedule,
                   'banner': conferenceDetail[0],
                   'navbar': navbar})

def page(request, id=None, slug=None):
    ''' page renderer. 
            renderers a page and it's contents
    '''
    page = None
    page_title = 'Pages'
    if id:
        page = ConferencePage.objects.get(pk=int(id))
        page_title = page.title
    if slug:
        page = ConferencePage.objects.get(slug=slug)
        page_title = page.title

    return render(request, 'main/page.html',{
        'page_title':page_title,
        'page' : page,
        })

        