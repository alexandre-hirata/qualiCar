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

    def test_create_part_successful (self):
        """ Test creating a new part """
        payload = {
            'name': 'Test part',
            'description': 'Test description'
        }
        self.client.post (PARTS_URL, payload)

        exists = Part.objects.filter (
            name = payload ['name']
        ).exists ()

        self.assertTrue (exists)

    def test_create_part_as_anonymous (self):
        """ Test if it is possible to create a part as anonymous """

        part = models.Part.objects.create (

            name = 'part name',
            description = 'part description'
        )
        response = self.client.get (PARTS_URL)

        self.assertEqual (response.status_code, status.HTTP_400_BAD_REQUEST)
