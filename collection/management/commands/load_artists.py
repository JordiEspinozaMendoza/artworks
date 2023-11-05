from django.core.management.base import BaseCommand, CommandError
from collection.models import Artist
import os
import environ
import sys
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            dir_path = os.path.dirname(os.path.realpath("artworks_data"))
            files = os.listdir(dir_path + "/artworks_data")
            artists = [f for f in files if "-art.csv" not in f]

            for a in artists:
                with open(dir_path + "/artworks_data/" + a, newline="") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        slug = row[0]
                        name = row[1]
                        born_date = row[2]

                        Artist.objects.create(slug=slug, name=name, born_date=born_date)

            print("Artists loaded successfully")
        except Exception as e:
            print(e)
            sys.exit(1)
