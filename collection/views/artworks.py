from collection.models import Artwork
from django.shortcuts import render


def getArtworksList(request):
    artworks = Artwork.objects.all()

    return render(request, "artworks/index.html", {"artworks": artworks})


def getArtwork(request, artwork_id):
    artwork = Artwork.objects.get(pk=artwork_id)

    return render(request, "artworks/artwork.html", {"artwork": artwork})
