from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test Apiviews"""

    def get(self, request, format=None):
        """Return of list APIViews features"""
        an_apiview = [
            'Use HTTP methods as function (get, post, pacth, put, delete)',
            'Is similar to a traditional view Django',
            'Give you the most control over you aplication logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
