'''
  Test custom Django management commands
'''
from unittest.mock import patch  # to mock the behaivior of the database
from psycopg2 import OperationalError as Psycopg2Error  # one of the possible
# errors when the database is not ready
from django.core.management import call_command  # to simulate calling
# the command by the name
from django.db.utils import OperationalError
from django.test import SimpleTestCase


# the BaseCommand class it has a check method and that is why we are using
# it here
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    '''Test commands'''

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready."""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        '''Test waiting for db when getting operationalError '''
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
