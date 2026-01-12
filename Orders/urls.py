from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_orders, name='orders'),
    # path('success/', views.success_view, name='success'),
    # Add the path for get_session view
    path('/purchase', views.purchase, name='purchase'),
path('/product/offer/submitted', views.create_orders_from_user, name='order_from_offer'),
]
