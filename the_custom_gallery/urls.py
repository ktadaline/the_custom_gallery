"""the_custom_gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from artist_profile import views
from rest_framework_jwt.views import refresh_jwt_token

#wire up ArtistProfileListCreate and ArtListCreate to api/artist/ and api/art/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('artist_profile.urls')),
    path('', include('frontend.urls')),
    path('artists_/', views.Artist_List.as_view(), name='artists_'),
    path('art_/', views.Art_List.as_view(), name='art_'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('refresh-token/', refresh_jwt_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
