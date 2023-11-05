from django.urls import path
from .views import artworks, auth

urlpatterns = [
    path("", auth.index, name="index"),
    path("accounts/profile/", auth.index, name="index"),
    path("accounts/register/", auth.register, name="register"),
    path("artworks/", artworks.getArtworksList, name="artworks"),
]
