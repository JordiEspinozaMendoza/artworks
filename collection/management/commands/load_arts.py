from django.core.management.base import BaseCommand
from collection.models import Artwork, Artist, Style, Period, Genre
import os
import environ
import sys
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            dir_path = os.path.dirname(os.path.realpath("artworks_data"))
            files = os.listdir(dir_path + "/artworks_data")
            artists = [f for f in files if "-art.csv" in f]

            for a in artists:
                with open(dir_path + "/artworks_data/" + a, newline="") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        artist_slug = row[0]
                        path = row[1]
                        title = row[2]
                        date = row[3]
                        image_url = row[7]
                        artist = Artist.objects.get(slug=artist_slug)
                        style = None
                        period = None
                        genre = None

                        if row[4] != "":
                            style = Style.objects.get_or_create(name=row[4])[0]
                        if row[5] != "":
                            period = row[5]
                            period = Period.objects.get_or_create(name=row[5])[0]
                        if row[6] != "":
                            genre = row[6]
                            genre = Genre.objects.get_or_create(name=row[6])[0]

                        Artwork.objects.create(
                            author=artist,
                            path=path,
                            title=title,
                            date=date,
                            style=style,
                            period=period,
                            genre=genre,
                            image_url=image_url,
                        )

            print("Arts loaded successfully")
        except Exception as e:
            print(e)
            sys.exit(1)
