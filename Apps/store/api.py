from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Product
from cart.cart import Cart
from order.models import Order, OrderItem
from order.utils import checkout
from coupon.models import Coupon
from django.core.mail import send_mail
import json

def api_checkout(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    address = data.get('address')
    zipcode = data.get('zipcode')
    place = data.get('place')
    coupon_code = data.get('coupon_code')
    coupon_value = 0

    if coupon_code:
        try:
            coupon = Coupon.objects.get(code = coupon_code)
            if coupon.can_use():
                coupon_value = coupon.value
                coupon.use()
        except:
            print("Invalid coupon!")
    
    cart = Cart(request)
    if int(cart.get_total_length()) == 0:
        return JsonResponse({"error": True})
    else:
        order_id = checkout(request, first_name, last_name, email, address, zipcode, place, coupon_code)
        
        paid = True
        
        if paid:
            order = Order.objects.get(pk=order_id)
            order.paid = True
            order.paid_amount = cart.get_total_price()
            if coupon_value:
                order.paid_amount *= coupon_value / 100

            order.save()
            # send_mail(
            #     "Subject here",
            #     "Here is the message.",
            #     "najmiddinovahliddin04@gmail.com",
            #     ["akhliddinnajmiddinov04@gmail.com"],
            #     fail_silently=False,
            # )
            cart.clear()
            
        return JsonResponse(jsonresponse)
        

def api_add_to_cart(request):
    data = json.loads(request.body)
    
    jsonresponse = {'success': True}
    product_id = data.get('product_id')
    update = data.get('update')
    quantity = data.get('quantity', 1)

    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)

    if quantity > product.num_available:
        jsonresponse['success'] = False
    else:
        cart.add(product=product, quantity=quantity, update_quantity=update)
    return JsonResponse(jsonresponse)


def api_remove_from_cart(request):
    data = json.loads(request.body)
    
    jsonresponse = {'success': True}
    product_id = str(data.get('product_id'))
    
    cart = Cart(request)
    cart.delete(product_id)
    return JsonResponse(jsonresponse)