from collection.models import Artwork
from django.shortcuts import render
from .filters import ArtworkFilterSet
from django.views.generic.list import ListView


def getArtworksList(request):
    artworks = Artwork.objects.all()

    return render(request, "artworks/index.html", {"artworks": artworks})


def getArtwork(request, artwork_id):
    artwork = Artwork.objects.get(pk=artwork_id)

    return render(request, "artworks/artwork.html", {"artwork": artwork})


class ArtWorkSearchView(ListView):
    model = Artwork
    ordering = "author"
    paginate_by = 25

    def get_queryset(self):
        qs = super().get_queryset()
        self.filter_set = ArtworkFilterSet(self.request.GET, queryset=qs)
        return self.filter_set.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filter_set
        return context


def getSearch(request):
    try:
        qs = Artwork.objects.all().order_by("author")

        filter_set = ArtworkFilterSet(request.GET, queryset=qs)

        artworks = filter_set.qs

        return render(
            request,
            "artworks/search.html",
            {"artworks": artworks, "filter": filter_set},
        )

    except Exception as e:
        error = str(e)
        return render(
            request,
            "404.html",
            {"message": error},
        )
