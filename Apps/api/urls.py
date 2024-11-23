from django.urls import path
from store.api import api_add_to_cart, api_remove_from_cart, api_checkout
from coupon.api import api_can_use
from newsletter.api import api_add_subscriber

urlpatterns = [
    path('add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
    path('checkout/', api_checkout, name='api_checkout'),
    path('api_can_use/', api_can_use, name = 'api_can_use'),
    path('add_subscriber/', api_add_subscriber, name='add_subscriber'),
]