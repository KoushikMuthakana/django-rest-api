from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from . import serializers



class HelloAPI(APIView):
    """Test API View."""
    
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features."""
        api_pre=[
            'koushik',
            'Muthakana'
        ]
        users=[ u.name for u in UserProfile.objects.all()]

        return Response({'message':'hello..!!','api_pre':api_pre,'users':users})
    
    def post(self, request):
        """Create a hello message with our name."""
        serializer=serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            users=[ u.name for u in UserProfile.objects.all()]
            if name in users:
                msg='Hello  {0}'.format(name)
                return Response({'msg':msg})
            else:
                return Response ({'error':'User not found..!!'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handles updating an object """
        
        
        return Response({'Method':'Post'})


    def patch(self,request,pk=None):
        """ Patch request, only updatesfields provided in request """
        
        
        return Response({'Method':'patch'})


    def delete(self,request,pk=None):
        """ delete request, deleted an object """
        
        
        return Response({'Method':'delete'})


    

class HelloViewSet(viewsets.ViewSet):
    """ Rest API using ViewSet"""

    def list(self,request):
        ''' Returns a hello message'''
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)'
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message ': 'Hello ',' ViewsSets':a_viewset})
    
    def create(self,request,pk=None):
        
        serializer=serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            return Response({'Msg ':name})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        """ retrieve request, gets an object """
        
        
        return Response({'Method':'get'})
    
    def update(self,request,pk=None):
        """ update request, update an object """
        
        
        return Response({'Method':'update'})


    def partial_update(self,request,pk=None):
        """ Patch request, only updatesfields provided in request """
        
        
        return Response({'Method':'patch'})
    
        
    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})
        

