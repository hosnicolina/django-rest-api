from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


class HelloAPIView(APIView):
    """Test Apiviews"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return of list APIViews features"""
        an_apiview = [
            'Use HTTP methods as function (get, post, pacth, put, delete)',
            'Is similar to a traditional view Django',
            'Give you the most control over you aplication logic',
            'Is mapped manually to URLS',
        ]

        return Response( { 'message': 'Hello!', 'an_apiview': an_apiview } )

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response( { 'message' : message } )
        else:
            return Response(
                serializer.errors, 
                status= status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """"Handle updating an object"""
        return Response( { 'method': 'PUT' } )

    def patch(self, request, pk=None):
        """"Handle a partial update of an object"""
        return Response( { 'method': 'PUT' } )

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response( { 'method': 'DELETE' } )