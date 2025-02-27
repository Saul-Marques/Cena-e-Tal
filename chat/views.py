from django.shortcuts import render
from .pusher import pusher_client
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class MessageAPIView(APIView):

    def post(self, request):
        pusher_client.trigger('chat', 'message', {
            'username': request.data['username'],
            'message': request.data['message'],

        })
        
        return Response([])