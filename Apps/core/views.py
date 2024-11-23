from django.shortcuts import render
from store.models import Product

def FrontPageView(request):
    products = Product.objects.filter(is_featured=True)

    context = {
        "products": products
    }

    return render(request, 'frontpage.html', context=context)

def ContactPageView(request):
    return render(request, 'contact.html')


def AboutPageView(request):
    return render(request, 'about.html')
