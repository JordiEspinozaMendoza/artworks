from collection.models import Artwork
from django.shortcuts import render
from django.contrib.postgres.search import SearchVector


def getArtworksList(request):
    artworks = Artwork.objects.all()

    return render(request, "artworks/index.html", {"artworks": artworks})


def getArtwork(request, artwork_id):
    artwork = Artwork.objects.get(pk=artwork_id)

    return render(request, "artworks/artwork.html", {"artwork": artwork})


def search(request):
    query = request.GET.get("query")

    artworks = Artwork.objects.annotate(
        search=SearchVector("title", "description")
    ).filter(search=query)

    return render(request, "artworks/index.html", {"artworks": artworks})
