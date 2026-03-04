from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """test APIView"""

    def get(self,request,format=None):
        """returns a list of APIView features"""

        an_apiview=[
            "uses HTTP methods as function(get,post,put,delete)",
            "is similar to a traditional Django View",
            "gives you the most control over you applicationlogic",
            "Is mapped manually to URLs"
        ]

        return Response({'message':'hello', 'an_apiView':an_apiview})