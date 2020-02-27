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
