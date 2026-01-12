from django.shortcuts import render
from .models import *
# Create your views here.
def Mainview(request) :# new


    return render(request, "Homepage.html")

def Products_view(request) :# new
    return render(request, "productspages.html")
def cart_view(request) :# new
    if not request.session.session_key:
        request.session.create()
    session_id = request.session.session_key
    return render(request, "Cart.html",{"session_id": session_id})


def get_session(request):

    if not request.session.session_key:
        request.session.create()
    session_id = request.session.session_key
    print(f"Session ID: {session_id}")
    return render(request, "Cart.html", {"session_id": session_id})



def offer(request) :
    return render(request, "Offer.html")