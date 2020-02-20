from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from qualiCar_API import serializers
from qualiCar_API import models
from qualiCar_API import permissions


class qualiCarApiView (APIView):
    """ qualiCar API View """
    serializer_class = serializers.qualiCarSerializer

    def get (self, request, format=None):
        """ Returns a list of APIView feature """

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a tradicional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS',
        ]

        # It converts the response to JSon
        return Response ({'message': 'Hello!', 'an_apiview': an_apiview})

    def post (self, request):
        """ Create a hello message with our name """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response ({'message': message})
        else:
            return Response (
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class UserProfileViewSet (viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()

    autentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )

    # Search field
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )
