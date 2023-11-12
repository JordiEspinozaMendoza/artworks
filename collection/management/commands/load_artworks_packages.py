from django.core.management.base import BaseCommand
from collection.models import Artwork, ArtworksPackage
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Packages names generated with GitHub Copilot
        packagesNames = [
            "The Best of Renaissance",
            "The Best of Baroque",
            "The Best of Romanticism",
            "The Best of Impressionism",
            "The Best of Post-Impressionism",
            "The Best of Expressionism",
            "The Best of Cubism",
            "The Best of Surrealism",
        ]
        try:
            for name in packagesNames:
                randomDefaultArtwork = Artwork.objects.order_by("?").first()
                randomPrice = fake.pyint(min_value=100, max_value=1000)

                artworksPackage = ArtworksPackage(
                    name=name, quantity=5, price=randomPrice
                )
                artworksPackage.defaultArtwork = randomDefaultArtwork
                artworksPackage.save()

                print(f"Artworks package {name} created")
        except Exception as e:
            print(e)
            print("Error creating artworks packages")
            return
