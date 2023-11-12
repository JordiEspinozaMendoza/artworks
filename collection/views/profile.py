from collection.models import PackageOrder, Artwork, Favorites
from django.shortcuts import render
from collections import defaultdict
from django.http import HttpResponse
import json


def getMyArtworks(request):
    if request.user.is_anonymous:
        return render(
            request,
            "404.html",
            {"message": "You are not logged in. Please login to view your artworks."},
        )

    artworksPackage = PackageOrder.objects.filter(user=request.user)

    artworks = defaultdict(int)

    for package in artworksPackage:
        for artwork in package.artworks.all():
            print(artwork.title)
            key = (artwork.title, artwork.image_url, artwork.id)
            artworks[key] += 1

    return render(
        request,
        "profile/index.html",
        {
            "artworks": dict(artworks),
        },
    )


def addFavorite(request):
    if request.POST:
        artwork_id = request.POST.get("artwork_id")
        artwork = Artwork.objects.get(pk=artwork_id)
        favorite = Favorites(user=request.user, artwork=artwork)
        favorite.save()

        return HttpResponse(json.dumps({"status": "success"}))
