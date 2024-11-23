from django.urls import path
from . import views


app_name = "core"
urlpatterns = [
    path('', views.FrontPageView, name='frontpage'),
    path('contact', views.ContactPageView, name='contact'),
    path('about', views.AboutPageView, name='about'),
]
