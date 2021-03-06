from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

import logging

from qualiCar_API import models


# Get an instance of a logger
logger = logging.getLogger(__name__)

class qualiCarSerializer (serializers.Serializer):
    """ Serializes a name field for testing our APIView """

    name = serializers.CharField (max_length=10)


class UserProfileSerializer (serializers.ModelSerializer):
    """
        Serializes a user profile object
        (This one used ModelSerializer because UserProfile already exists)
    """

    # Indicates the model that Serializer will point
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')

        # To make password READ ONLY
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # Overwrite create function to secure password field
    def create (self, validated_data):
        """ Create and return a new user """
        user = models.UserProfile.objects.create_user(
            email = validated_data ['email'],
            name = validated_data ['name'],
            password = validated_data ['password']
        )

        return user


class DateSerializer (serializers.ModelSerializer):
    """ Serializes Date items """

    class Meta:
        model = models.Date
        fields = ('id', 'startDate', 'endDate', 'create_on', 'description', 'author')

        # To make author and create_on READ ONLY
        extra_kwargs = {
            #'author': { 'read-only': True }
            #'create_on': { 'read-only': True }
        }


class PartSerializer (serializers.ModelSerializer):
    """ Serializes Part items """

    class Meta:
        model = models.Part
        fields = ('id', 'name', 'description', 'create_on', 'author')

        # To make author and create_on READ ONLY
        extra_kwargs = {
            #'author': { 'read-only': True }
            #'create_on': { 'read-only': True }
        }


class VehicleSerializer (serializers.ModelSerializer):
    """ Serializes Vehicle items """

    parts = PartSerializer(read_only=True, many=True, allow_empty=True)

    class Meta:
        model = models.Vehicle
        #fields = ('id', 'brand', 'model', 'create_on', 'author', 'parts')
        fields = '__all__'

        # To make author and create_on READ ONLY
        extra_kwargs = {
            #'author': { 'read-only': True }
            #'create_on': { 'read-only': True }
        }


class incidentSerializer (serializers.ModelSerializer):
    """ Serializes Incident items """
    part = serializers.PrimaryKeyRelatedField (
        queryset=models.Part.objects.all(),
        allow_null = True,
        allow_empty = True,
    )

    author = serializers.PrimaryKeyRelatedField (
        queryset=models.UserProfile.objects.all(),
        required=False,
        allow_null=True,
        default=None
    )

    permission_classes = (IsAuthenticated,)

    class Meta:
        model = models.Incident
        fields = '__all__'
        read_only_fields=(
            'id',
        )

    def validate_part (self, value):
        """ Custom part validator """
        logger.info ("Incident serializer -> validate_part method")
        logger.info ("    Value = %s", value)

        # TODO implement the part validation (if this part exists, i.e.)

        return value

    def validate_author (self, value):
        """ Custom author validator """
        logger.info ("Incident serializer -> validate_author method")
        logger.info ("    Value = %s", value)

        return self.context['request'].user

    # def to_internal_value (self, data):
    #     print ("to_internal_value")
    #     _mutable = data._mutable
    #
    #     data._mutable = True
    #     if data.get ('part', None) == '':
    #         data.pop ('part')
    #     data._mutable = _mutable
    #     return super(incidentSerializer, self).to_internal_value(data)

    # def perform_update(self, serializer):
    #     serializer.save (author = self.request.user)
    #
    # def perform_create (self, serializer):
    #     print ("perform_Create")
    #     #require = serializer.context ['request']
    #     part_data = self.request.pop
    #
    #     serializer.save (author = self.request.user)
    #
    # def create (self, validated_data):
    #     part_data = validated_data.pop ('part')
    #     print (validated_data)
    #     for keys,values in validated_data.items():
    #         print("  **KEY  " + keys)
    #         print("  **VALUE  " + values)
    #
    #     print ("        *****    " + part_data)
    #     part_instance = models.Part.objects.get (id = part_data)
    #
    #     incident = models.Incident.objects.create (**validated_data)
    #
    #     incident.part = part_instance
    #     incident.saVe ()
