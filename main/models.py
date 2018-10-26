# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from redactor.fields import RedactorField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

''' Models for Conference Website
'''



# For CKEditor, use this -
#  message_body = RichTextField()

class ConferenceLocation(models.Model):
    ''' locations are places where events are held.
    '''
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=2, default='AR')
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=20, null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class ConferenceDetail(models.Model):
    ''' details about our conference.
    '''
    title = models.CharField(max_length=200)
    location = models.ForeignKey(ConferenceLocation)
    start_dt = models.DateTimeField(verbose_name='Start Date/Time')
    end_dt = models.DateTimeField(null=True, blank=True, verbose_name='End Date/Time')
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class ConferencePage(models.Model):
    ''' pages contain all the info for a page to be created.
    '''
    title = models.CharField(max_length=120)
    introduction = models.CharField(max_length=255, null=True, blank=True)
    body =RichTextField()
    sidebar = RichTextField()
    author = models.ForeignKey(User)
    slug = models.SlugField(unique=True) # make pages unique
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # saving the slug everytime from the title
        self.slug = slugify(self.title)
        super(ConferencePage, self).save(*args, **kwargs)


class Speaker(models.Model):
    ''' conference speakers 
    '''
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField()
    slug = models.SlugField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        self.slug = slugify("{} {}".format(self.first_name, self.last_name))
        super(Speaker, self).save(*args, **kwargs)


class SessionLocation(models.Model):
    ''' session location
            these are where talks will be held.
    '''
    room_name = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{} {}".format(self.building, self.room_name)

    def __str__(self):
        return "{} {}".format(self.building, self.room_name)

    def save(self, *args, **kwargs):
        self.slug = slugify("{} {}".format(self.building, self.room_name))
        super(SessionLocation, self).save(*args, **kwargs)


class Proposal(models.Model):
    ''' proposal 
            can be marked as a session with the 'accepted' flag
            can associate to a session location
    '''
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    speaker = models.ForeignKey(Speaker)
    accepted = models.BooleanField(default=False)
    session_location = models.ForeignKey(SessionLocation, null=True, blank=True)
    time = models.TimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Proposal, self).save(*args, **kwargs)


class Price(models.Model):
    ''' conference prices
    '''
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    amount = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Price, self).save(*args, **kwargs)


class ConferenceSponsor(models.Model):
    ''' conference sponsor model
    '''
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    img = models.ImageField()
    link = models.URLField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ConferenceSponsor, self).save(*args, **kwargs)


class NavBarItem(models.Model):
    ''' NabBarItem
            This represents any Navbar Item, link, dropdown, or dropdown item.
    '''
    _typeChoices = [
        ("LABEL", "LABEL"),
        ("DROPDOWN", "DROPDOWN"),
        ("HREF", "HREF"),
    ]
    
    display = models.CharField(max_length=36)
    slug = models.SlugField(blank=True)
    destinationPath = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, choices=_typeChoices, default="LABEL")
    parentItem = models.ForeignKey('self', null=True, blank=True, default=None)
    sortOrder = models.IntegerField(default=10)
    isActive = models.BooleanField(default=False)

    def __unicode__(self):
        return self.display

    def __str__(self):
        return self.display

    def save(self, *args, **kwargs):
        self.slug = slugify(self.display)
        super(NavBarItem, self).save(*args, **kwargs)
