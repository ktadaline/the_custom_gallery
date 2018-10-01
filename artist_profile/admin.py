from django.contrib import admin
from .models import Art
from .models import ArtistProfile

# Register your models here.
admin.site.register(Art)
admin.site.register(ArtistProfile)

