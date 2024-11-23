from django.conf import settings
from store.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        print('__iter__')
        for product_id in self.cart.keys():
            self.cart[product_id]['product'] = Product.objects.get(pk=product_id)
        
        for item in self.cart.values():
            yield item
            
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.pk)
        price = float(product.price)
        quantity = int(quantity)
        
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': price, 'id': product_id}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
            self.cart[product_id]['total_price'] = price * quantity
        else:
            self.cart[product_id]['quantity'] += 1
            if not self.cart[product_id].get('total_price'):
                self.cart[product_id]['total_price'] = price
            else:
                self.cart[product_id]['total_price'] += price
                
            
        self.save()

    def has_product(self, product_id):
        return str(product_id) in self.cart

    def delete(self, product_id):
        if product_id in self.cart:
            self.cart.pop(product_id)
            self.save()

    def clear(self):
        self.cart.clear()
        self.save()

    def save(self):
        print("save")
        self.session.modified = True

    def get_total_price(self):
        return sum(item['total_price'] for item in self.cart.values())
    
    def get_total_length(self):
        return str(sum(item['quantity'] for item in self.cart.values()))

    