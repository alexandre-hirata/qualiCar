from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from qualiCar_API import models
from qualiCar_API.models import Part


PARTS_URL = reverse ('qualiCar_API:part-list')


class PublicPartsApiTests (TestCase):
    """ Test the public available parts API """

    def setUp (self):
        self.client = APIClient ()

    def test_login_required (self):
        """ Test that login is not required for retrieving parts"""
        response = self.client.get (PARTS_URL)

        self.assertEqual (response.status_code, status.HTTP_200_OK)
