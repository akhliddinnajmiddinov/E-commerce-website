from django.urls import path
from .views import MyAccountView

app_name = 'myaccount'
urlpatterns = [
	path('', MyAccountView, name='myaccount'),
]