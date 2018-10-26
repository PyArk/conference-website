# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.contrib.auth.models import User
from main.models import *

import datetime, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class ConferenceLocationTest(TestCase):
    ''' Conference Location Tests
    '''
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user = User.objects.create_user(username='testuser', email='test@pyark.org', password='holycowbatman')

        ConferenceLocation.objects.create(
            name = 'Test Location',
            address = '123 address street',
            city = 'Little Rock',
            state = 'AR',
            zip_code = '72201',
            phone = '501-222-1111',
            latitude = 35.233,
            longitude = -92.454,
            author = test_user
        )

    def test_name_label(self):
        conference_location = ConferenceLocation.objects.get(id=1)
        field_label = conference_location._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_location_has_author(self):
        conference_location = ConferenceLocation.objects.get(id=1)
        author = conference_location.author
        self.assertTrue(author != None)

class ConferenceDetailTest(TestCase):
    ''' Conference Detail Tests
    '''
    @classmethod
    def setUpTestData(cls):
        start_dt = datetime.datetime.strptime("09/25/2018", "%m/%d/%Y")
        end_dt = start_dt + datetime.timedelta(days=5)

        test_user = User.objects.create_user(
            username='testuser',
            email='test@pyark.org', 
            password='holycowbatman'
        )

        test_location = ConferenceLocation.objects.create(
            name = 'Test Location',
            address = '123 address street',
            city = 'Little Rock',
            state = 'AR',
            zip_code = '72201',
            phone = '501-222-1111',
            latitude = 35.233,
            longitude = -92.454,
            author = test_user
        )


        ConferenceDetail.objects.create(
            title = 'Test Location',
            location = test_location,
            start_dt = start_dt,
            end_dt = end_dt
        )
    
    def test_start_dt_label(self):
        conference_detail = ConferenceDetail.objects.get(id=1)
        field_label = conference_detail._meta.get_field('start_dt').verbose_name
        self.assertEquals(field_label, "Start Date/Time")

    def test_end_dt_label(self):
        conference_detail = ConferenceDetail.objects.get(id=1)
        field_label = conference_detail._meta.get_field('end_dt').verbose_name
        self.assertEquals(field_label, "End Date/Time")

class ConferencePageTest(TestCase):
    ''' Conference Page Tests
    '''
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='testuser',
            email='test@pyark.org', 
            password='holycowbatman'
        )


        ConferencePage.objects.create(
            title = 'Test Page',
            introduction = 'my test introduction',
            body = "<b>Here is some bod with html in it</b>",
            sidebar = None,
            author = test_user
        )
    
    def test_page_slug(self):
        conference_page = ConferencePage.objects.get(id=1)
        self.assertEquals(conference_page.slug, "test-page")

    def test_body_has_html(self):
        conference_page = ConferencePage.objects.get(id=1)
        self.assertInHTML("Here is some bod with html in it", conference_page.body)

class SpeakerTest(TestCase):
    ''' Speaker Tests
    '''
    @classmethod
    def setUpTestData(cls):
        Speaker.objects.create(
            first_name = 'Micheal',
            last_name = 'Scott',
            description ='just a little stichious',
            img = File(open(os.path.join(BASE_DIR, 'tests', 'profile.png'))),
            phone = '501-111-2222',
            email = 'mscott@dundermifflin.com',
            facebook = 'https://facebook.com/micheal.scott',
            twitter = 'https://twitter.com/micheal.scott',
            github = 'https://github.com/micheal.scott',
            linkedin = 'https://linkedin.com/micheal.scott'
        )
    
    def test_speaker_slug(self):
        speaker = Speaker.objects.get(id=1)
        self.assertEquals(speaker.slug, "micheal-scott")

    def test_speaker_profile_img(self):
        speaker = Speaker.objects.get(id=1)
        self.failUnless(open(speaker.img.path), 'file not found')

class SessionLocationTest(TestCase):
    ''' Session Location Tests
    '''
    @classmethod
    def setUpTestData(cls):
        SessionLocation.objects.create(
            room_name = 'cains ballroom',
            building = 'The Main Building'
        )
    
    def test_speaker_slug(self):
        session_location = SessionLocation.objects.get(id=1)
        self.assertEquals(session_location.room_name, "cains ballroom")

class ProposalTest(TestCase):
    ''' Proposal Tests
    '''
    @classmethod
    def setUpTestData(cls):
        speaker = Speaker.objects.create(
            first_name = 'Micheal',
            last_name = 'Scott',
            description ='just a little stichious',
            img = File(open(os.path.join(BASE_DIR, 'tests', 'profile.png'))),
            phone = '501-111-2222',
            email = 'mscott@dundermifflin.com',
            facebook = 'https://facebook.com/micheal.scott',
            twitter = 'https://twitter.com/micheal.scott',
            github = 'https://github.com/micheal.scott',
            linkedin = 'https://linkedin.com/micheal.scott'
        )

        session_loc = SessionLocation.objects.create(
            room_name = 'cains ballroom',
            building = 'The Main Building'
        )        

        Proposal.objects.create(
            title = 'GIS with GeoDjango',
            description = 'something nice to say about G.I.S.',
            speaker = speaker,
            session_location = session_loc,
            time = datetime.time(3, 0, 0)
        )
    
    def test_proposal_slug(self):
        proposal = Proposal.objects.get(id=1)
        self.assertEquals(proposal.slug, "gis-with-geodjango")

class PriceTest(TestCase):
    ''' Price Tests
    '''
    @classmethod
    def setUpTestData(cls):
        Price.objects.create(
            title = 'Platnium Tier',
            description = 'for platnium folks',
            amount = 200
        )

    def test_price_slug(self):
        price = Price.objects.get(id=1)
        self.assertEqual(price.slug, 'platnium-tier')

class ConferenceSponsorTest(TestCase):
    ''' Conference Sponsor Tests
    '''
    @classmethod
    def setUpTestData(cls):
        ConferenceSponsor.objects.create(
            name = 'coolest company',
            img = File(open(os.path.join(BASE_DIR, 'tests', 'profile.png'))),
            link = 'https://coolcompany.co',
            description = 'a very nice description of a sponsor'
        )

    def test_conference_sponsor_slug(self):
        conference_sponsor = ConferenceSponsor.objects.get(id=1)
        self.assertEqual(conference_sponsor.slug, 'coolest-company')

    def test_sponsor_logo_img(self):
        conference_sponsor = ConferenceSponsor.objects.get(id=1)
        self.failUnless(open(conference_sponsor.img.path), 'file not found')

class NavBarItemTest(TestCase):
    ''' NavBarItem tests
    '''
    @classmethod
    def setUpTestData(cls):
        first_item = NavBarItem.objects.create(
            display = 'nav item',
            sortOrder = 1,
            isActive = True
        )

        NavBarItem.objects.create(
            display = 'nav item 2',
            sortOrder = 2,
            isActive = True,
            parentItem = first_item
        )


    def test_looking_at_navitems(self):
        nav_bar_item = NavBarItem.objects.get(id=1)
        self.assertEqual(nav_bar_item.slug, 'nav-item')
