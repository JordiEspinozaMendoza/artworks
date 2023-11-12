from typing import Any
from django.views.generic.list import ListView
from .filters import SimpleFilter


class ArtWorkListView(ListView):
    def get_queryset(self):
        try:
            qs = super().get_queryset().self.filter_set = SimpleFilter(self.request.GET,queryset=qs)
            return self.filter_set.qs
        except Exception as e:
            print(e)