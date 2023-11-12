from django.urls import path
from .views import artworks, auth, store, profile,search

urlpatterns = [
    path("", artworks.getArtworksList, name="home"),
    path("accounts/profile/", profile.getMyArtworks, name="profile"),
    path("accounts/profile/favorites", profile.getMyFavorites, name="favorites"),
    path("accounts/register/", auth.register, name="register"),
    path("artworks/", artworks.getArtworksList, name="artworks"),
    path("artworks/<int:artwork_id>/", artworks.getArtwork, name="artwork"),
    path("store/", store.getArtworksPackages, name="store"),
    path(
        "api/store/create-payment/", store.getStripeClientSecret, name="client_secret"
    ),
    path("api/store/package", store.saveArtPackageToUser, name="save_package"),
    path("", search.ArtWorkListView.as_view(),name="art-list"),
    path("api/profile/favorite/add", profile.addFavorite, name="add_favorite"),
    path("api/profile/favorite/remove", profile.removeFavorite, name="remove_favorite"),
]
