from django.db import models
from store.models import Product
from django.contrib.auth.models import User

class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    coupon_code = models.CharField(max_length=50, blank=True, null=True)

    user = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    
    paid = models.BooleanField(default=False)
    paid_amount = models.FloatField(blank=True, null=True)

    shipped_date = models.DateTimeField(blank=True, null=True)

    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    ARRIVED = 'arrive'
    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped'),
        (ARRIVED, 'Arrived')
        )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default = ORDERED)
    

    def get_total_quantity(self):
        return sum(orderitem.quantity for orderitem in self.items.all())

    def __str__(self):
        return self.first_name
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  related_name='items', on_delete=models.DO_NOTHING)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return "%s" % self.pk