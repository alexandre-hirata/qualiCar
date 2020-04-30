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

    class Meta:
        model = models.Incident
        fields = ('id', 'description', 'part')
