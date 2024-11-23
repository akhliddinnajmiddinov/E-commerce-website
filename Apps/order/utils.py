from .models import Order, OrderItem
from cart.cart import Cart


def checkout(request, first_name, last_name, email, address, zipcode, place, coupon_code):
    order = Order(first_name=first_name, last_name=last_name, email=email, address=address, zipcode=zipcode, place=place, coupon_code=coupon_code)
    
    if request.user.is_authenticated:
        order.user = request.user

    order.save()
    
    cart = Cart(request)
    
    for item in cart:
        item['product'].num_available = item['product'].num_available - item['quantity']
        item['product'].save()
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
        
    return order.pk
    