from rest_framework import serializers
from artist_profile.models import ArtistProfile
from artist_profile.models import Art
#converts models to JSON

class ArtistProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistProfile
        fields = '__all__'

class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = ('art_title', 'art_description', 'art_completion_date', 'medium', 'art_image', 'file_type', 'created_at', 'artist')