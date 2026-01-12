from .models import Offer


def offer_status(request):
    offer=Offer.objects.get(name="offer")
    return{
        "offer_status":offer.offer


    }