from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters 
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken



from  profiles_api import serializers
from  profiles_api import models
from  profiles_api import permissions

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


class HelloViewSets(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer
    def list(self,request):
        a_viewset=[
            'uses actions [list,create,update,retrieve,update,partial_update]'
            'automatically maps to URLs using Routers',
            'provides more functionality with less code'
        ]
        return Response({'message':'hello', 'a_viewset':a_viewset})

    def create(self,request):
        serializer=self.serializer_class(date=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello: {name}!'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES   