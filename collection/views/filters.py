from collection.models import Artwork
from django_filters_facet import Facet, FacetedFilterSet
import django_filters
from django.contrib.postgres import search


class ArtworkFilterSet(FacetedFilterSet):
    search = django_filters.CharFilter(method="filter_search", label="Search")

    class Meta:
        model = Artwork
        fields = ["author__name", "genre__name", "title"]

    def configure_facets(self):
        self.filters["author__name"].facet = Facet()
        self.filters["genre__name"].facet = Facet()
        self.filters["title"].facet = Facet()

    def filter_search(self, queryset, name, value):
        vector = search.SearchVector("title", "author__name", "genre__name")

        query = search.SearchQuery(value, search_type="phrase")

        return queryset.annotate(search=vector).filter(search=query)
