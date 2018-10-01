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
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Creates a view for handling GET and POST
class ArtistProfileListCreate(generics.ListCreateAPIView):
    queryset = ArtistProfile.objects.all()
    serializer_class = ArtistProfileSerializer

class ArtListCreate(generics.ListCreateAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer