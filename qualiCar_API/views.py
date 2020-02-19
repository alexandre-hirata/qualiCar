from rest_framework.views import APIView
from rest_framework.response import Response


class qualiCarApiView (APIView):
    """ qualiCar API View """

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
