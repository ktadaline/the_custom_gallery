from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from artist_profile.models import ArtistProfile
from artist_profile.models import Art
from artist_profile.serializers import ArtistProfileSerializer
from artist_profile.serializers import ArtSerializer
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from functools import wraps
from django.utils.decorators import available_attrs, decorator_from_middleware
# Create your views here.
#Lists all art/artists or creates a new one
# artists_/
# art_/






class Artist_List(APIView):

    def get(self, request):
        artists_ = ArtistProfile.objects.all()
        serializer = ArtistProfileSerializer(artists_, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class Art_List(APIView):

    def get(self, request):
        art_ = Art.objects.all()
        serializer = ArtSerializer(art_, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Creates a view for handling GET and POST

class ArtistProfileListCreate(generics.ListCreateAPIView):
    queryset = ArtistProfile.objects.all()
    serializer_class = ArtistProfileSerializer

class ArtListCreate(generics.ListCreateAPIView):
    # obtain a CSRF token.
    #def csrf_clear(view_func):

        #def wrapped_view(*args, **kwargs):
        #    request = args[0]
        #    request.csrf_processing_done = True
         #   return view_func(*args, **kwargs)

        #return wraps(view_func, assigned=available_attrs(view_func))(wrapped_view)
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
