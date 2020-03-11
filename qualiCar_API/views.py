from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from qualiCar_API import serializers
from qualiCar_API import models
from qualiCar_API import permissions


class BaseQualiCarViewSet (viewsets.GenericViewSet,
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin):
    """ Create base ViewSet to summarize the code """

    # Enable Authentication
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset (self):
        """ Return objects for the current authenticated user only """
        return self.queryset.filter (user=self.request.user).order_by ('-name')

    def perform_create (self, serializer):
        """ Create new object """
        serializer.save (user=self.request.user)



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


# Authentication
class UserLoginApiView (ObtainAuthToken):
    """ Handle creating user authentication tokens """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class DateViewSet (BaseQualiCarViewSet):
    """ Handle creating and update dates """

    queryset = models.Date.objects.all ()
    serializer_class = serializers.DateSerializer


class PartViewSet (BaseQualiCarViewSet):
    """ Handle creating and update dates """

    queryset = models.Part.objects.all ()
    serializer_class = serializers.PartSerializer


class VehicleViewSet (BaseQualiCarViewSet):
    """ Handle creating and update vehicles """

    queryset = models.Vehicle.objects.all ()
    serializer_class = serializers.VehicleSerializer
