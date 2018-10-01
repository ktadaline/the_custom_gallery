from django.db import models

# Create your models here. (model is an object representing the table's data)

class ArtistProfile(models.Model):
    artist_username = models.CharField(max_length=20)
    artist_first_name = models.CharField(max_length=100)
    artist_last_name = models.CharField(max_length=100)
    artist_email = models.EmailField()
    artist_profile_pic = models.CharField(max_length=1000)
    artist_genres = models.CharField(max_length=500)
    artist_description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.artist_username

class Art(models.Model):
    artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE)
    art_title = models.CharField(max_length=250)
    art_description = models.CharField(max_length=500)
    art_completion_date = models.CharField(max_length=30)
    medium = models.CharField(max_length=500)
    art_image = models.CharField(max_length=1000)
    file_type = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.art_title + '-' + self.art_image