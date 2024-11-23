from django.urls import path
from .views import CartDetailPageView, SuccessView

app_name = 'cart'
urlpatterns = [
    path("", CartDetailPageView, name='cart'),
    path("success", SuccessView, name='success'),
]