from django.urls import path
from . import views
#wire up ArtistProfileListCreate and ArtListCreate to api/artist/ and api/art/
urlpatterns = [
    path('api/artist/', views.ArtistProfileListCreate.as_view()),
    path('api/art/', views.ArtListCreate.as_view()),
]
