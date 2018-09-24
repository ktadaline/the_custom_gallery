from django.shortcuts import render
from artist_profile.models import ArtistProfile
from artist_profile.models import Art
from artist_profile.serializers import ArtistProfileSerializer
from artist_profile.serializers import ArtSerializer
from rest_framework import generics

# Create your views here.

class ArtistProfileListCreate(generics.ListCreateAPIView):
    queryset = ArtistProfile.objects.all()
    serializer_class = ArtistProfileSerializer

class ArtListCreate(generics.ListCreateAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer