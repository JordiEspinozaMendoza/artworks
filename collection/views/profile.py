from collection.models import PackageOrder, Artwork, Favorites
from django.shortcuts import render
from collections import defaultdict
from django.http import HttpResponse
import json
import sys


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


def getMyFavorites(request):
    try:
        if request.user.is_anonymous:
            return render(
                request,
                "404.html",
                {
                    "message": "You are not logged in. Please login to view your artworks."
                },
            )

        favorites = Favorites.objects.filter(user=request.user)

        return render(
            request,
            "profile/favorites.html",
            {
                "favorites": favorites,
            },
        )
    except Exception as e:
        error = str(e)
        print(e, sys.exc_info()[-1].tb_lineno)
        return HttpResponse(json.dumps({"status": "error", "message": error}))


def addFavorite(request):
    try:
        if request.POST:
            data = json.loads(request.body)
            artwork_id = data["artwork_id"]

            favorite_exists = Favorites.objects.filter(
                user=request.user, artwork=artwork_id
            ).exists()

            if favorite_exists:
                return HttpResponse(
                    json.dumps(
                        {"status": "error", "message": "Artwork already favorited"}
                    )
                )

            artwork = Artwork.objects.get(pk=artwork_id)
            favorite = Favorites(user=request.user, artwork=artwork)
            favorite.save()

            return HttpResponse(
                json.dumps({"status": "success", "message": "Artwork favorited"})
            )

    except Exception as e:
        error = str(e)
        print(e, sys.exc_info()[-1].tb_lineno)
        return HttpResponse(json.dumps({"status": "error", "message": error}))


def removeFavorite(request):
    try:
        if request.POST:
            data = json.loads(request.body)
            artwork_id = data["artwork_id"]

            favorite_exists = Favorites.objects.filter(
                user=request.user, artwork=artwork_id
            ).exists()

            if not favorite_exists:
                return HttpResponse(
                    json.dumps({"status": "error", "message": "Artwork not favorited"})
                )

            artwork = Artwork.objects.get(pk=artwork_id)
            favorite = Favorites.objects.get(user=request.user, artwork=artwork)
            favorite.delete()

            return HttpResponse(
                json.dumps({"status": "success", "message": "Artwork unfavorited"})
            )

    except Exception as e:
        error = str(e)
        print(e, sys.exc_info()[-1].tb_lineno)
        return HttpResponse(json.dumps({"status": "error", "message": error}))
