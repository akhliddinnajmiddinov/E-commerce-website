from itertools import product
from cart.cart import Cart
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.db.models import Q
import json

# Create your views here.
def ProductDetailView(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if product.parent_product:
        return redirect('store:product_detail', slug=product.parent_product.slug)

    allImages = [{ "image": product.image.url, "thumbnail": product.thumbnail.url }]
    allImages += [{ "image": image.image.url, "thumbnail": image.thumbnail.url } for image in product.images.all()]

    cart = Cart(request)

    inCart = str(product.pk) in cart.cart

    context = {
        "product": product,
        "allImages": json.dumps(allImages),
        "inCart": json.dumps({"inCart": inCart})
    }
    return render(request, "product_detail.html", context=context)


def CategoryDetailView(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(parent_product=None)

    context = {
        "category": category,
        "products": products
    }
    return render(request, "category_detail.html", context=context)


def SearchProductsView(request):
    query = request.GET.get('query')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    context = {
        "query": query,
        "products": products
    }
    print("MANAMAN")
    return render(request, "search.html", context=context)