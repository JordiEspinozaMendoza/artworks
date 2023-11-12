from django.shortcuts import render
from collection.models import Artist, Artwork


def getArtistsList(request):
    artists = Artist.objects.all()

    return render(request, "artists/index.html", {"artists": artists})


def getArtist(request, artist_id):
    artist = Artist.objects.get(pk=artist_id)
    arts = Artwork.objects.filter(author=artist)

    if arts.count() == 0:
        return render(
            request, "404.html", {"message": "No artworks found for this artist"}
        )

    return render(request, "artworks/index.html", {"artworks": arts})
