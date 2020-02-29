from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests (TestCase):

    def setUp (self):
        self.client = Client ()
        self.admin_user = get_user_model ().objects.create_superuser (
            email = 'admin@gmail.com',
            name = 'administrator',
            password = 'password123'
        )

        self.client.force_login (self.admin_user)
        self.user = get_user_model ().objects.create_user (
            email = 'test@gmail.com',
            name = 'Full name test',
            password = 'password123'
        )

    def test_user_listed (self):
        """ Test that users are listed on user page """
        url = reverse ('admin:qualiCar_API_userprofile_changelist')
        response = self.client.get (url)

        self.assertContains (response, self.user.name)
        self.assertContains (response, self.user.email)
