from django.urls import path
from .views import artworks, auth, store

urlpatterns = [
    path("", auth.index, name="home"),
    path("accounts/profile/", auth.index, name="index"),
    path("accounts/register/", auth.register, name="register"),
    path("artworks/", artworks.getArtworksList, name="artworks"),
    path("artworks/<int:artwork_id>/", artworks.getArtwork, name="artwork"),
    path("store/", store.getArtworksPackages, name="packages"),
    path("api/store/package", store.saveArtPackageToUser, name="save_package"),
]
