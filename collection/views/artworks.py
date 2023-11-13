from collection.models import Artwork
from django.shortcuts import render
from .filters import ft_artworks
from django.views.generic.list import ListView


def getArtworksList(request):
    artworks = Artwork.objects.all()

    return render(request, "artworks/index.html", {"artworks": artworks})


def getArtwork(request, artwork_id):
    artwork = Artwork.objects.get(pk=artwork_id)

    return render(request, "artworks/artwork.html", {"artwork": artwork})


def getSearch(request):
    try:
        search = request.GET.get("search")
        artworks = ft_artworks(search)

        return render(
            request,
            "artworks/search.html",
            {"artworks": artworks, "query": search},
        )

    except Exception as e:
        error = str(e)
        return render(
            request,
            "404.html",
            {"message": error},
        )
