from rest_framework import serializers
from artist_profile.models import ArtistProfile
from artist_profile.models import Art

class ArtistProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistProfile
        fields = '__all__'

class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = '__all__'