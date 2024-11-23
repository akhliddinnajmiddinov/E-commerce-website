from django.shortcuts import render
from .cart import Cart
import json

def CartDetailPageView(request):
    cart = Cart(request)
    products = []
    for item in cart:
        products.append({'id': item['id'], 
                     'title': item['product'].title,
                     'price': item['price'], 
                     'quantity': item['quantity'], 
                     'total_price': item['total_price'],
                     'thumbnail': item['product'].thumbnail.url,
                     'url': f"/store/products/{item['product'].slug}",
                     })
    
    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
    else:
        first_name = last_name = email = ''


    context = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'productsList': json.dumps(products),
    }
    print(context['productsList'])
    
    return render(request, 'cart.html', context=context)


def SuccessView(request):
    return render(request, "success.html")