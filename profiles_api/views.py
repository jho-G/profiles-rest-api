from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from  profiles_api import serializers

class HelloApiView(APIView):
    """test APIView"""
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """returns a list of APIView features"""

        an_apiview=[
            "uses HTTP methods as function(get,post,put,delete)",
            "is similar to a traditional Django View",
            "gives you the most control over you applicationlogic",
            "Is mapped manually to URLs"
        ]

        return Response({'message':'hello', 'an_apiView':an_apiview})

    def post(self,request):
        """create a hello message with our name"""

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})