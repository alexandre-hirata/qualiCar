from django.test import TestCase
from django.contrib.auth import get_user_model


class UserProfileTests (TestCase):

    def test_create_new_user_with_email_successful (self):
        """ Test creating a new user with an e-mail is successful """
        email = 'asdasd@gmail.com'
        password = 'Testpass123'
        name = 'TestName'
        user = get_user_model().objects.create_user (
            email = email,
            name = name,
            password = password
        )

        self.assertEqual (user.email, email)
        self.assertTrue (user.check_password (password))

    def test_new_user_email_normalized (self):
        """ Test the e-mail for a new user is normalized """
        email = 'asdasd@GMAIL.COM'
        name = 'TestName2'

        user = get_user_model().objects.create_user (
            email,
            name,
            'test123'
        )
        print (user.email)
        print (email.lower())
        self.assertEqual (user.email, email.lower())
