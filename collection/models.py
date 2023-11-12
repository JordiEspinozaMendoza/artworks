from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField()
    born_date = models.CharField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/artists/{self.slug}/"


class Genre(models.Model):
    name = models.CharField(unique=True)

    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(unique=True)

    def __str__(self):
        return self.name


class Period(models.Model):
    name = models.CharField(unique=True)

    def __str__(self):
        return self.name


class Artwork(models.Model):
    author = models.ForeignKey(Artist, on_delete=models.RESTRICT)
    path = models.CharField()
    title = models.CharField()
    date = models.CharField(null=True)
    style = models.ForeignKey(Style, null=True, on_delete=models.RESTRICT)
    period = models.ForeignKey(Period, null=True, on_delete=models.RESTRICT)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.RESTRICT)
    image_url = models.URLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/artworks/{self.id}/"


class ArtworksPackage(models.Model):
    name = models.CharField(unique=True)
    quantity = models.IntegerField()
    price = models.IntegerField(default=0)
    defaultArtwork = models.ForeignKey(Artwork, null=True, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class PackageOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(ArtworksPackage, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    artworks = models.ManyToManyField(Artwork)
    payment_intent = models.CharField(null=True)

    def __str__(self):
        return f"{self.user.username} - {self.package.name}"


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.artwork.title}"
