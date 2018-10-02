from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
#wire up ArtistProfileListCreate and ArtListCreate to api/artist/ and api/art/
urlpatterns = [
    path('api/artist/', views.ArtistProfileListCreate.as_view()),
    path('api/art/', csrf_exempt(views.ArtListCreate.as_view())),
]
