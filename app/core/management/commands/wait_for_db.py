'''
Django command to wait for the database to be available
'''

from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError


class Command(BaseCommand):
    '''Django command to wait for the database to be available'''

    def handle(self, *args, **options):
        '''Entry point for command '''
        self.stdout.write('Waiting for Database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Available'))
