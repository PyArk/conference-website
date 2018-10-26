# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from main.models import *
from main.views import *

import datetime, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class MainViewTest(TestCase):
    ''' View Tests
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

        ConferencePage.objects.create(
            title = 'Test Page',
            introduction = 'my test introduction',
            body = "<b>Here is some bod with html in it</b>",
            sidebar = None,
            author = test_user
        )
    
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_page_by_slug(self):
        response = self.client.get('/pages/test-page/')
        self.assertEqual(response.status_code, 200)

    def test_page_by_id(self):
        response = self.client.get('/pages/1/')
        self.assertEqual(response.status_code, 200)
