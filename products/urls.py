from django.urls import path
from .views import *

urlpatterns = [
    path("", Mainview, name="Mainview"),
path("products/", Products_view,name="Products"),
path("products/cart", cart_view,name="cart"),
path("product/offer",offer,name="offer"),



]