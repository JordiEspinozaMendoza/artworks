from django.shortcuts import render
from collection.models import Artist

def getArtistsList(request):
    artists = Artist.objects.all()

    return render(request, "artists/index.html", {"artists": artists})


def getArtist(request, artist_id):
    artist = Artist.objects.get(pk=artist_id)

    return render(request, "artists/artists.html", {"artist": artist})
