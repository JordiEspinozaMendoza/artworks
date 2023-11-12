from typing import Any
from django.db.models.query import QuerySet
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
        self.filter_set = ArtworkFilterSet(self.request.GET,queryset=qs)
        return self.filter_set.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filter_set
        return context