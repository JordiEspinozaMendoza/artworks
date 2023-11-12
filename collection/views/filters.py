import artworks
from django_filters_facet import Facet, FacetedFilterSet

class SimpleFilter(FacetedFilterSet):
    class Meta:
        model = artworks
        fields = ["title"]
    def configure_facets(self):
        try:
            self.filters["title"].facet = Facet()
        except Exception as e:
            print(e)