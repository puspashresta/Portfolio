from .views import home,about,portfolio,contact,service,price,bloghome
from django.urls import path
app_name='home'

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('portfolio',portfolio, name='portfoilio'),
    path('contact',contact,name='contact'),
    path('services',service,name='services'),
    path('price',price,name='price')
]

