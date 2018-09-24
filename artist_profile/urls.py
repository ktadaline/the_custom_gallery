from django.urls import path
from . import views

urlpatterns = [
    path('api/artist/', views.ArtistProfileListCreate.as_view()),
    path('api/art/', views.ArtListCreate.as_view()),
]
