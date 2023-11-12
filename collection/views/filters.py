from collection.models import Artwork
from django_filters_facet import Facet, FacetedFilterSet
import django_filters
from django.contrib.postgres import search

class ArtworkFilterSet(FacetedFilterSet):
    search = django_filters.CharFilter(method="filter_search",label="Search")

    class Meta:
        model = Artwork
        fields = ["author","genre"]
    
    def configure_facets(self):
        self.filters["author"].facet = Facet()
        self.filters["genre"].facet = Facet()
    
    def filter_search(self,queryset,name,value):
        vector = (
            search.SearchVector("author", weight="A")+
            search.SearchVector("genre", weight="B")
        )
        query = search.SearchQuery(value,search_type="websearch")
        return (
            queryset.annotate(
                search=vector,
                rank=search.SearchRank(vector,query),
            ).filter(search=query).order_by("-rank")
        )