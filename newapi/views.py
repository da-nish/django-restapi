from .models import users
from .serializer import UserSSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import users

# Create your views here.


class userlist(APIView):
    def get(self,request, format=None):

        us = users.objects.all()
        serializer = UserSSerializer(us, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userdata(APIView):
    """
    Retrieve, update or delete a snippet instance.
    
    """
    def get_object(self, pk):
        try:
            print("----->",pk)
            return users.objects.get(username=pk)
        except users.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)