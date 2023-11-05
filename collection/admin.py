from django.contrib import admin
from collection.models import Artwork, Artist, Style, Period, Genre

admin.site.register(Artwork)
admin.site.register(Artist)
admin.site.register(Style)
admin.site.register(Period)
admin.site.register(Genre)
