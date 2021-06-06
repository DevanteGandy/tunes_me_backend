from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics ,filters
from .models import Music
from rest_framework import status
from .serializers import MusicSerializer
from rest_framework import permissions


class ListMusicView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
   # permission_classes = (permissions.IsAuthenticated,)

class PostMusicView(APIView):
    def post(self,request ,*args,**kwargs):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)