from django.urls import path
from .views import artworks, auth, store, profile

urlpatterns = [
    path("", artworks.getArtworksList, name="home"),
    path("accounts/profile/", profile.getMyArtworks, name="profile"),
    path("accounts/register/", auth.register, name="register"),
    path("artworks/", artworks.getArtworksList, name="artworks"),
    path("artworks/<int:artwork_id>/", artworks.getArtwork, name="artwork"),
    path("store/", store.getArtworksPackages, name="store"),
    path("api/store/package", store.saveArtPackageToUser, name="save_package"),
]
