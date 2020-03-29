from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests (TestCase):

    def test_wait_for_db_ready (self):
        """ Test waiting for db when db is available """
        # This command replaces the behavior of __getitem__ as getitem and returns True
        with patch ('django.db.utils.ConnectionHandler.__getitem__') as getitem:
            getitem.return_value = True
            call_command ('wait_for_db')

            # The mock also counts how many times it was called
            self.assertEqual (getitem.call_count, 1)

    # This command makes the same as with patch, but before the function
    # definition
    @patch ('time.sleep', return_value = True)
    def test_wait_for_db (self, ts):
        """ Test waiting for db """
        with patch ('django.db.utils.ConnectionHandler.__getitem__') as getitem:
            # This command makes timeout 5 times and in sixth return True
            getitem.side_effect = [OperationalError] * 5 + [True]
            call_command ('wait_for_db')

            self.assertEqual (getitem.call_count, 6)
