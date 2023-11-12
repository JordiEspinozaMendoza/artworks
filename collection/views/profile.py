from collection.models import PackageOrder
from django.shortcuts import render


def getMyArtworks(request):
    artworksPackage = PackageOrder.objects.filter(user=request.user)

    artworks = []

    for package in artworksPackage:
        artworks.extend(package.artworks.all())

    artworks = list(set(artworks))

    return render(
        request, "profile/index.html", {"artworks": artworks, "quantity": len(artworks)}
    )
