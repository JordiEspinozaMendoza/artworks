from collection.models import PackageOrder, ArtworksPackage, Artwork
from django.http import HttpResponse
from django.shortcuts import render
import json
import sys
import environ
import stripe


def getMyOrders(request):
    orders = PackageOrder.objects.filter(user=request.user)

    return render(request, "store/my_orders.html", {"orders": orders})


def getArtworksPackages(request):
    packages = ArtworksPackage.objects.all()

    return render(
        request,
        "store/index.html",
        {
            "stripe_publishable_key": environ.Env().str("STRIPE_PUBLISHABLE_KEY"),
            "packages": packages,
        },
    )


def saveArtPackageToUser(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            package = ArtworksPackage.objects.get(pk=data["package_id"])

            packageArtworks = [package.defaultArtwork]

            order = PackageOrder(
                user=request.user,
                package=package,
                payment_intent=data["payment_intent"],
            )
            order.save()

            for i in range(package.quantity):
                artwork = Artwork.objects.order_by("?").exclude(
                    pk__in=[artwork.pk for artwork in packageArtworks]
                )[0]

                packageArtworks.append(artwork)

            order.artworks.set(packageArtworks)

            return HttpResponse(
                json.dumps(
                    {
                        "status": "success",
                        "order_id": order.pk,
                        "artworks": json.dumps(
                            [
                                {
                                    "title": artwork.title,
                                    "image": artwork.image_url,
                                }
                                for artwork in packageArtworks
                            ]
                        ),
                    }
                )
            )

    except Exception as e:
        error = str(e)
        print(e, sys.exc_info()[-1].tb_lineno)
        return HttpResponse(json.dumps({"status": "error", "message": error}))


def getStripeClientSecret(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            package = ArtworksPackage.objects.get(pk=data["package_id"])

            stripe.api_key = environ.Env().str("STRIPE_SECRET_KEY")

            intent = stripe.PaymentIntent.create(
                amount=package.price * 100,
                currency="usd",
                metadata={"integration_check": "accept_a_payment"},
            )

            return HttpResponse(
                json.dumps({"status": "success", "client_secret": intent.client_secret})
            )

    except Exception as e:
        error = str(e)
        print(e, sys.exc_info()[-1].tb_lineno)
        return HttpResponse(json.dumps({"status": "error", "message": error}))
