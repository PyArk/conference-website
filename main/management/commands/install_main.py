"""
Attempting to make my own management command to pre-populate
things for easier testing and install

Use "python manage.py install_main"
"""

import datetime

from django.core.management import call_command
from django.core.management.base import BaseCommand

from main.models import ConferenceDetail, ConferenceLocation, NavBarItem

DUMMY_POST_MESSAGE = """
            <p>
            Bacon ipsum dolor amet tenderloin jerky strip steak alcatra hamburger 
            salami doner t-bone flank pancetta kielbasa ball tip. Corned beef tail 
            frankfurter kevin cow chuck. T-bone short ribs beef filet mignon porchetta 
            drumstick pig short loin, frankfurter strip steak chuck fatback jowl. 
            Ribeye meatloaf ground round pancetta brisket. Tongue meatball salami swine 
            short loin filet mignon hamburger. Fatback sausage pancetta ground round 
            t-bone tail ham drumstick swine tenderloin picanha spare ribs. Pork belly 
            hamburger shank alcatra venison salami short ribs turkey capicola brisket.
            </p>
            <table>
            <tr>
                <td>TEST</td><td>TEST2</td><td>test3</td>
            </tr>
            <tr>
                <td>Thing</td><td>Thing2</td><td>Thing3</td>
            </td>
            </table><p>
            Short loin pastrami pork prosciutto, pig turkey tail. Shoulder pork belly
            tail alcatra, shank rump jerky short ribs salami ground round beef ribs frankfurter. 
            Bacon t-bone pancetta, ball tip meatloaf jowl doner salami biltong sirloin swine 
            burgdoggen fatback ground round. Pastrami pork loin beef fatback turkey tail 
            turducken spare ribs. Short ribs pancetta prosciutto, cupim cow capicola bacon turkey 
            boudin frankfurter shoulder beef ribs t-bone salami andouille. Venison strip steak 
            kielbasa, porchetta burgdoggen picanha pastrami jowl chuck biltong rump. Ham beef 
            chicken, pork capicola short loin shoulder.
            </p><p>
            Sausage tongue porchetta jowl pork loin hamburger. Fatback flank brisket, hamburger 
            meatloaf tenderloin sirloin tail beef porchetta drumstick pork chop meatball filet 
            mignon chicken. Ribeye alcatra picanha porchetta, t-bone kielbasa andouille. Rump
            sausage ham swine. Kevin beef ribs frankfurter spare ribs. Shankle jerky boudin 
            sausage meatball short ribs venison, tri-tip turducken. Brisket tenderloin venison 
            flank.
            </p>
            """


class Command(BaseCommand):
    args = '<param arg switch ...>'
    help = 'Help us Obi Wan, you\'re our only hope. '

    def _createDefaultDatabaseContent(self):
        dateFormatStr = "%m-%d-%Y %H:%M:%S"
        conferenceDate = "10-05-2019 10:00:00"

        # Conference Location
        conferenceLocation = ConferenceLocation()
        conferenceLocation.address = "123 somewhere Rd"
        conferenceLocation.city = "Somwhere City"
        conferenceLocation.name = "University Auditorium"
        conferenceLocation.zip_code = 72204
        conferenceLocation.save()

        # Conference Detail
        conferenceDetail = ConferenceDetail()
        conferenceDetail.start_dt = datetime.datetime.strptime(conferenceDate, dateFormatStr)
        conferenceDetail.title = "PyCon Arkansas 2019"
        conferenceDetail.location = conferenceLocation
        conferenceDetail.save()

        # Create the Home button on the nav bar
        navItem = NavBarItem()
        navItem.destinationPath = "#"
        navItem.display = "Home"
        navItem.isActive = True
        navItem.type = "LABEL"
        navItem.save()
        # TODO: Create some default objects and data
        pass

    def _create_user_interactive(self):
        print('...calling createsuperuser')
        call_command('createsuperuser')

    def _handle_migrations(self):
        print('...calling makemigrations')
        call_command('makemigrations')
        print('...calling migrate')
        call_command('migrate')
        print('Success!')

    def _collect_static_resources(self):
        print("collecting static resources for deployment")
        call_command('collectstatic')
        print('Success')

    def _start_application(self):
        print('Starting Server')
        call_command('runserver')

    def handle(self, *args, **options):
        # Clear the database, and re-apply schema
        self._handle_migrations()
        self._createDefaultDatabaseContent()
        # Pull in all the static resources
        self._collect_static_resources()
        # Populate the database
        # TODO: Create methods that create some default data, from file or otherwise.
        # Create Super user
        # self._create_user_interactive()
