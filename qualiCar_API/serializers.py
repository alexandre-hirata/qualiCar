from rest_framework import serializers

from qualiCar_API import models


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
