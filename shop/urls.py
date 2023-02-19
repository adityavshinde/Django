from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="About Us"),
    path('contact/', views.contact, name="Contact Us"),
    path('tracker/', views.tracker, name="Tracking Status"),
    path('search/', views.search, name="Search"),
    path('prodview/<int:myid>', views.prodview, name="Product Details"),
    path('checkout/', views.checkout, name="Check Out")
]