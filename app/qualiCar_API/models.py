from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager (BaseUserManager):
    """ Manager for user profiles """

    def create_user (self, email, name, password=None):
        """ Create a new user profile """

        if not email:
            raise ValueError ('User must have an e-mail address')

        email = self.normalize_email (email)
        user = self.model (email=email, name=name)

        user.set_password (password)

        # Standard way to save objects in Django
        user.save (using=self._db)

        return user

    def create_superuser (self, email, name, password):
        """ Create and save a new superuser with given details """

        user = self.create_user (email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save (using=self._db)

        return user


class UserProfile (AbstractBaseUser, PermissionsMixin):
    """ Database model for user in the system """

    # Fields
    email = models.EmailField (max_length=255, unique=True)
    name = models.CharField (max_length=255)
    is_active = models.BooleanField (default=True)
    is_staff = models.BooleanField (default=False)

    objects = UserProfileManager ()

    # Overwrite
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name (self):
        """ Retrieve full name of user """
        return self.name

    def get_short_name (self):
        """ Retrieve short name of user """
        return self.name.partition (' ')[0]

    def __str__ (self):
        """ Return string representation of user """
        return self.email


class Date (models.Model):
    """ Datetime of maintanance """

    # Make a reference from settings file to the profile user (author)
    author = models.ForeignKey (
        settings.AUTH_USER_MODEL,
        on_delete = models.SET_NULL,
        null=True
    )

    create_on = models.DateTimeField (auto_now_add=True)
    last_change_on = models.DateTimeField (auto_now_add=True)
    startDate = models.DateTimeField (null=False)
    endDate = models.DateTimeField (null=False)

    description = models.CharField (max_length=50)

    def get_start_date (self):
        """ Retrieve start date """
        return self.startDate

    def get_end_date (self):
        """ Retrieve end date """
        return self.endDate

    def __str__ (self):
        """ Return string representation of date """
        return self.description


class Part (models.Model):
    """ Parts of vehicles """
    # Make a reference from settings file to the profile user (author)
    author = models.ForeignKey (
        settings.AUTH_USER_MODEL,
        on_delete = models.SET_NULL,
        null = True,
    )

    create_on = models.DateTimeField (auto_now_add=True)
    last_change_on = models.DateTimeField (auto_now_add=True)

    name = models.CharField (max_length=50)
    description = models.CharField (max_length=150)

    def __str__ (self):
        """ Return string representation of part """
        return self.name

    def get_description (self):
        """ Return description part """
        return self.description

    def get_name (self):
        """ Return name part """
        return self.name


class Vehicle (models.Model):
    """ Vehicles model """
    # Make a reference from settings file to the profile user (author)
    author = models.ForeignKey (
        settings.AUTH_USER_MODEL,
        on_delete = models.SET_NULL,
        null=True
    )

    create_on = models.DateTimeField (auto_now_add=True)
    last_change_on = models.DateTimeField (auto_now_add=True)

    brand = models.CharField (max_length=50)
    model = models.CharField (max_length=50)

    # Parts that has in vehicle
    parts = models.ManyToManyField(Part)

    def __str__ (self):
        """ Return string representation of vehicle """
        return self.brand + self.model

    def get_brand (self):
        """ Return brand vehicle """
        return self.brand

    def get_model (self):
        """ Return model vehicle """
        return self.model


class Incident (models.Model):
    """ Incident model """
    # Make a reference from settings file to the profile user (author)
    author = models.ForeignKey (
        settings.AUTH_USER_MODEL,
        on_delete = models.SET_NULL,
        null=True
    )
    # ForeignKey that represent the part in the incident
    part = models.ForeignKey (
        Part,
        on_delete=models.CASCADE
    )

    description = models.CharField (max_length=150)

    def __str__ (self):
        """ Return string representation of incident """
        return self.description

    def get_parts (self):
        return self.parts
