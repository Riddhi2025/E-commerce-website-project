"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminreg/',adminreg),
    path("showdata/",showdata),
    path("seller_reg/",seller_reg),
    path("show_sellers/",show_sellers),
    path("edit_seller/",edit_seller),
    path("edit_seller1/",edit_seller1),
    path("delete_seller/",delete_seller),
    path("delete_seller1/",delete_seller1),
    path("product_reg/",product_reg),
    path("show_products/",show_products),
    path("edit_product/",edit_product),
    path("edit_product1/",edit_product1),
    path("delete_product/",delete_product),
    path("delete_product1/",delete_product1),
    path("customer_reg/",customer_reg),
    path("show_customers/",show_customers),
    path("edit_customer/",edit_customer),
    path("edit_customer1/",edit_customer1),
    path("delete_customer/",delete_customer),
    path("delete_customer1/",delete_customer1),
    path("add_to_cart/",add_to_cart),
    path("login/",login),
    path("logout/",logout),
    path("admin_home/",admin_home),
    path("seller_home/",seller_home),
    path("customer_home/",customer_home),
    path("show_carts/",show_carts),
    path("edit_cart/",edit_cart),
    path("edit_cart1/",edit_cart1),
    path("delete_cart/",delete_cart),
    path("delete_cart1/",delete_cart1),
    path("your_orders/",your_orders),
    path("show_orders/",show_orders),
    path("auth_error/",auth_error),
    path("show_all_electronics/",show_all_electronics),
    path("show_all_beauty/",show_all_beauty),
    path("show_all_books_toys/",show_all_books_toys),
    path("show_all_grocery/",show_all_grocery),
    path("show_all_kitchen/",show_all_kitchen),
    path("show_all_pharmacy/",show_all_pharmacy),
    path("show_all_furniture/",show_all_furniture),
    path("",index),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)