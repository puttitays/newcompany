from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from .models import *


def create_orders(request):
    if request.method == "POST":
        # Get data from POST request
        user=request.POST.get("user")
        Name=request.POST.get("Name")
        Phone = request.POST.get("Phone no.")
        Street = request.POST.get("Street")
        PostalCode = request.POST.get("Postal")
        City = request.POST.get("City")
        Note = request.POST.get("Note")
        img=request.POST.getlist("Image[]")
        product_name = request.POST.getlist("product_name[]")
        Width = request.POST.getlist("Width[]")
        Height = request.POST.getlist("Height[]")
        Quantity = request.POST.getlist("Quantity[]")
        Price = request.POST.getlist("Price[]")
        Type= request.POST.getlist("Type[]")
        Color= request.POST.getlist("Color[]")



        for i in range(len(product_name)):
            Orders.objects.create(
                user=user,
                Name=Name,
                Phone=Phone,
                Street=Street,
                PostalCode=PostalCode,
                City=City,
                Note=Note,
                img=img[i],
                product_name=product_name[i],
                Width=Width[i],
                Height=Height[i],
                Quantity=int(Quantity[i]),
                Price=float(Price[i]),
                total=int(Quantity[i])*float(Price[i]),
                Type=Type[i],
                Color=Color[i]

            )



        return render(request, "swishpayment.html")

        # Redirect to a success page (or any page you want after saving the product)
    # return redirect('success')  # Ensure you've defined a success page




def purchase(request) :

        if not request.session.session_key:
            request.session.create()
        order_id=request.session.session_key
        orders=Orders.objects.filter(user=order_id)
        return render(request, "purchase.html", {"user_order": orders})



def create_orders_from_user(request):
    if request.method == "POST":
        Order_from_offer.objects.create(
        user_name=request.POST.get("user_name"),
        Telephone=request.POST.get("Telephone"),
        Email = request.POST.get("Email"),
        Order = request.POST.get("Order"),
        # file = request.POST.get("file")
        )

    return render(request, "swishpayment.html")