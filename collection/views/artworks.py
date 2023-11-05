from collection.models import Artwork
from django.shortcuts import render


def getArtworksList(request):
    artworks = Artwork.objects.all()

    return render(request, "artworks/index.html", {"artworks": artworks})
