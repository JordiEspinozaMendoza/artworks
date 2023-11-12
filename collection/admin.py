from django.contrib import admin
from collection.models import (
    Artwork,
    Artist,
    Style,
    Period,
    Genre,
    PackageOrder,
    ArtworksPackage,
)

admin.site.register(Artwork)
admin.site.register(Artist)
admin.site.register(Style)
admin.site.register(Period)
admin.site.register(Genre)
admin.site.register(PackageOrder)
admin.site.register(ArtworksPackage)
