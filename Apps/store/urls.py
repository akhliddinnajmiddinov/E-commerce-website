from django.urls import path
from .views import ProductDetailView, CategoryDetailView, SearchProductsView


app_name = 'store'
urlpatterns = [
    path("products/<slug:slug>/", ProductDetailView, name="product_detail"),
    path("categories/<slug:slug>/", CategoryDetailView, name="category_detail"),
    path("search/", SearchProductsView, name="search"),
]