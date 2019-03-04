from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPI(APIView):
    
    def get(self,request,format=None):
        api_pre=[
            'koushik',
            'Muthakana'
        ]
        return Response({'message':'hello..!!','api_pre':api_pre})