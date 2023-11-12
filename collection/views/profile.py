from collection.models import PackageOrder
from django.shortcuts import render
from collections import defaultdict


def getMyArtworks(request):
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
