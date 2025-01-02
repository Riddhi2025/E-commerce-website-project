from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import *
import os
import time
# Create your views here.

# admin reg

def adminreg(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if usertype == "admin":
            if (request.method == "POST"):
                obj = admindata()
                obj1 = logindata()

                nm = request.POST["T1"]
                ad = request.POST["T2"]
                co = request.POST["T3"]
                em = request.POST["T4"]
                pw = request.POST["T5"]

                am = "admin"
                obj.name = nm
                obj.address = ad
                obj.contact = co
                obj.email = em

                obj1.email = em
                obj1.password = pw

                obj1.usertype = am
                obj.save()
                obj1.save()
                return render(request, "adminreg.html", {"data": "success"})
            else:
                return render(request,"adminreg.html")
        else:
            return HttpResponseRedirect("../auth_error/")
    else:
        return HttpResponseRedirect("../auth_error/")


# show data
def showdata(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        email = request.session["email"]
        if usertype == "admin":
            obj = admindata.objects.filter(email=email)
            return render(request, "showdata.html", {"key1": obj})
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")



# seller reg

def seller_reg(request):
    if (request.method == "POST"):
        obj = sellerdata()
        obj1 = logindata()

        nm = request.POST["T1"]
        ad = request.POST["T2"]
        co = request.POST["T3"]
        em = request.POST["T4"]
        gst = request.POST["T5"]
        pin = request.POST["T6"]
        pw = request.POST["T7"]

        am = "sellerdata"

        obj.name = nm
        obj.address = ad
        obj.contact = co
        obj.email = em
        obj.gst_number = gst
        obj.pincode = pin

        obj1.email = em
        obj1.password = pw

        obj1.usertype = am
        obj.save()
        obj1.save()
        return render(request, "seller_reg.html", {"data": "success"})
    else:
        return render(request, "seller_reg.html")


# show seller data
def show_sellers(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if usertype == "admin":
            obj = sellerdata.objects.all()
            return render(request, "show_sellers.html", {"key1": obj})
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")
# edit seller
def edit_seller(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if usertype == "admin":
            if (request.method == "POST"):
                email = request.POST["H1"]
                obj = sellerdata.objects.filter(email=email)
                return render(request, "edit_seller.html", {"data": obj})
            else:
                return HttpResponseRedirect("/show_seller/")
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")

# edit seller1
def edit_seller1(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if usertype == "admin":
            if (request.method == "POST"):
                name = request.POST["T1"]
                address = request.POST["T2"]
                contact = request.POST["T3"]
                email = request.POST["T4"]
                gst_number = request.POST["T5"]
                pincode = request.POST["T6"]

                obj = sellerdata.objects.get(email=email)
                obj.name = name
                obj.address = address
                obj.contact = contact
                obj.gst_number = gst_number
                obj.pincode = pincode

                obj.save()
                return render(request, "edit_seller1.html", {"name": "saved"})
            else:
                return HttpResponseRedirect("/auth_error/")
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")



# delete seller
def delete_seller(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if usertype == "admin":
            if (request.method == "POST"):
                email = request.POST["H1"]
                obj = sellerdata.objects.filter(email=email)
                return render(request, "delete_seller.html", {"data": obj})
            else:
                return HttpResponseRedirect("/auth_error/")
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")

# delete seller1
def delete_seller1(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if usertype == "admin":
            if (request.method == "POST"):
                email = request.POST["email"]
                obj = sellerdata.objects.get(email=email)
                obj.delete()
                return render(request, "delete_seller1.html", {"name": "Data is deleted"})
            else:
                return HttpResponseRedirect("/auth_error/")
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")


# product reg

def product_reg(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        email = request.session["email"]
        if usertype == "sellerdata":
            if (request.method == "POST"):
                obj = itemdata()

                upload_photo = request.FILES["T1"]
                name = request.POST["T2"]
                category = request.POST["T3"]
                price = request.POST["T4"]
                inventory_quantity = request.POST["T5"]
                description = request.POST["T6"]

                obj.name = name
                obj.Category = category
                obj.price = price
                obj.inventory_quantity = inventory_quantity
                obj.Description = description
                obj.email_of_seller =email

                path = os.path.basename(upload_photo.name)
                file_ext = os.path.splitext(path)[1][1:]
                filename = str(int(time.time())) + '.' + file_ext
                fs = FileSystemStorage()
                fs.save(filename, upload_photo)
                obj.image_url = filename

                obj.save()

                return render(request, "product_reg.html", {"data": "success"})
            else:
                return render(request, "product_reg.html")
        else:
            return HttpResponseRedirect("../auth_error/")
    else:
        return HttpResponseRedirect("../auth_error/")

# show product data
def show_products(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        email = request.session["email"]
        if usertype == "sellerdata":
            obj = itemdata.objects.filter(email_of_seller=email)
            return render(request, "show_products.html", {"key1": obj})
        else:
            return HttpResponseRedirect("../auth_error/")
    else:
        return HttpResponseRedirect("../auth_error/")

# edit product
def edit_product(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if usertype == "sellerdata":
            if (request.method == "POST"):
                product_id = request.POST["H1"]
                obj = itemdata.objects.filter(product_id=product_id)
                return render(request, "edit_product.html", {"data": obj})
            else:
                return HttpResponseRedirect("/auth_error/")
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")
# edit product1
def edit_product1(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if usertype == "sellerdata":
            if (request.method == "POST"):
                product_id = request.POST["T0"]
                name = request.POST["T1"]
                category = request.POST["T2"]
                price = request.POST["T3"]
                inventory = request.POST["T4"]
                description = request.POST["T5"]

                obj = itemdata.objects.get(product_id=product_id)
                obj.name = name
                obj.Category = category
                obj.price = price
                obj.inventory_quantity = inventory
                obj.Description = description

                obj.save()
                return render(request, "edit_product1.html", {"name": "saved"})
            else:
                return HttpResponseRedirect("../auth_error/")
        else:
            return HttpResponseRedirect("../auth_error/")
    else:
        return HttpResponseRedirect("../auth_error/")


# delete product
def delete_product(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if usertype == "sellerdata":
            if (request.method == "POST"):
                product_id = request.POST["H1"]
                obj = itemdata.objects.filter(product_id=product_id)
                return render(request, "delete_product.html", {"data": obj})
            else:
                return HttpResponseRedirect("../auth_error/")
        else:
            return HttpResponseRedirect("../auth_error/")
    else:
        return HttpResponseRedirect("../auth_error/")


# delete product1
def delete_product1(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if usertype == "sellerdata":
            if (request.method == "POST"):
                product_id = request.POST["product_id"]
                obj = itemdata.objects.get(product_id=product_id)
                obj.delete()
                return render(request, "delete_product1.html", {"name": "Data is deleted"})
            else:
                return HttpResponseRedirect("../auth_error/")
        else:
            return HttpResponseRedirect("../auth_error/")
    else:
        return HttpResponseRedirect("../auth_error/")
# show all electronics
def show_all_electronics(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if(usertype=="customers"):
            obj = itemdata.objects.all().filter(Category="Electronics")
            return render(request, "show_all_electronics.html", {"data1": obj})
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")


# show all Beauty
def show_all_beauty(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if(usertype=="customers"):
            obj = itemdata.objects.all().filter(Category="Beauty")
            return render(request, "show_all_beauty.html", {"data1": obj})
        else:
            return HttpResponseRedirect("../auth_error/")
    else:
        return HttpResponseRedirect("../auth_error/")


# show all Furniture
def show_all_furniture(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if(usertype=="customers"):
            obj = itemdata.objects.all().filter(Category="Furniture")
            return render(request, "show_all_furniture.html", {"data1": obj})
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")


# show all Grocery
def show_all_grocery(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if(usertype=="customers"):
            obj = itemdata.objects.all().filter(Category="Grocery")
            return render(request, "show_all_grocery.html", {"data1": obj})
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")


# show all Kitchen
def show_all_kitchen(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if(usertype=="customers"):
            obj = itemdata.objects.all().filter(Category="Kitchen")
            return render(request, "show_all_kitchen.html", {"data1": obj})
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")

# show all Pharmacy
def show_all_pharmacy(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if(usertype=="customers"):
            obj = itemdata.objects.all().filter(Category="Pharmacy")
            return render(request, "show_all_pharmacy.html", {"data1": obj})
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")

# show all Books and toys
def show_all_books_toys(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if(usertype=="customers"):
            obj = itemdata.objects.all().filter(Category="Books and Toys")
            return render(request, "show_all_books_toys.html", {"data1": obj})
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")


# customer reg
def customer_reg(request):
    if (request.method == "POST"):
        obj = customers()
        obj1 = logindata()

        nm = request.POST["T1"]
        ad = request.POST["T2"]
        co = request.POST["T3"]
        em = request.POST["T4"]
        ci = request.POST["T5"]
        st = request.POST["T6"]
        pi = request.POST["T7"]
        pw = request.POST["T8"]

        am = "customers"

        obj.name = nm
        obj.address = ad
        obj.contact = co
        obj.email = em
        obj.city = ci
        obj.state = st
        obj.pincode = pi

        obj1.email = em
        obj1.password = pw

        obj1.usertype = am
        obj.save()
        obj1.save()
        return render(request, "customer_reg.html", {"data": "success"})
    else:
        return render(request, "customer_reg.html")

# show customers
def show_customers(request):
    obj = customers.objects.all()
    return render(request, "show_customers.html", {"key1": obj})

# edit customer
def edit_customer(request):
    if(request.method=="POST"):
        email = request.POST["H1"]
        obj = customers.objects.filter(email=email)
        return render(request,"edit_customer.html",{"data":obj})
    else:
        return HttpResponseRedirect("/show_customer/")
# edit customer1
def edit_customer1(request):
    if(request.method=="POST"):
        name = request.POST["T1"]
        address = request.POST["T2"]
        contact = request.POST["T3"]
        email = request.POST["T4"]
        city = request.POST["T5"]
        state = request.POST["T6"]
        pincode = request.POST["T7"]

        obj = customers.objects.get(email=email)
        obj.name = name
        obj.address = address
        obj.contact = contact
        obj.city = city
        obj.state = state
        obj.pincode = pincode

        obj.save()
        return render(request,"edit_customer1.html",{"name":"saved"})
    else:
        return HttpResponseRedirect("/show_customer/")

# delete customer
def delete_customer(request):
    if(request.method=="POST"):
        email = request.POST["H1"]
        obj = customers.objects.filter(email=email)
        return render(request,"delete_customer.html",{"data":obj})
    else:
        return HttpResponseRedirect("/show_customer/")
# delete Customer1
def delete_customer1(request):
    if(request.method=="POST"):
        email = request.POST["email"]
        obj = customers.objects.get(email=email)
        obj.delete()
        return render(request,"delete_customer1.html",{"name":"Data is deleted"})
    else:
        return HttpResponseRedirect("/show_customer/")



#add to cart
def add_to_cart(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if(usertype=="customers"):
            if(request.method=="POST"):
                product_id = request.POST["H1"]
                price = request.POST["H2"]


                email = request.session["email"]
                obj = cart()

                obj.product_id = product_id
                obj.total_price = price
                obj.email = email
                obj.quantity = 1
                obj.save()
                return HttpResponseRedirect("/show_carts/")
            else:
                return HttpResponseRedirect("/show_carts/")
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")

# show cart
def show_carts(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]

        if(usertype=="customers"):
            email = request.session["email"]
            obj = cart.objects.filter(email=email)
            return render(request, "show_carts.html", {"key1": obj})
        else:
            return HttpResponseRedirect("../auth_error/")
    else:
        return HttpResponseRedirect("../auth_error/")
# edit cart
def edit_cart(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if(usertype=="customers"):
            if (request.method == "POST"):
                cart_id = request.POST["H1"]
                obj = cart.objects.filter(cart_id=cart_id)
                return render(request, "edit_cart.html", {"data": obj})
            else:
                return HttpResponseRedirect("/show_carts/")
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")


# edit cart1
def edit_cart1(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if(usertype=="customers"):
            if (request.method == "POST"):

                cart_id = request.POST["T1"]
                total_price = request.POST["T2"]
                quantity = request.POST["T3"]

                obj = cart.objects.get(cart_id=cart_id)
                obj.total_price = total_price
                obj.quantity = quantity

                obj.save()
                return render(request, "edit_cart1.html", {"name": "saved"})
            else:
                return HttpResponseRedirect("/show_carts/")
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")


# delete cart
def delete_cart(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if(usertype=="customers"):
            if (request.method == "POST"):
                cart_id = request.POST["H1"]
                obj = cart.objects.filter(cart_id=cart_id)
                return render(request, "delete_cart.html", {"data": obj})
            else:
                return HttpResponseRedirect("/show_carts/")
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")
# delete Cart1
def delete_cart1(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if(usertype=="customers"):
            if (request.method == "POST"):
                cart_id = request.POST["cart_id"]
                obj = cart.objects.get(cart_id=cart_id)
                obj.delete()
                return render(request, "delete_cart1.html", {"name": "Data is deleted"})
            else:
                return HttpResponseRedirect("/show_carts/")
        else:
            return HttpResponseRedirect("../auth_error/")
    else:
        return HttpResponseRedirect("../auth_error/")


# orders
def your_orders(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if(usertype=="customers"):
            if (request.method == "POST"):
                product_id = request.POST["H1"]
                cart_id = request.POST["H2"]
                quantity = request.POST["H4"]
                total_price = request.POST["H3"]
                email = request.session["email"]
                obj = orders()


                obj.product_id = product_id
                obj.cart_id = cart_id
                obj.quantity = quantity
                obj.total_price = total_price
                obj.email = email
                obj.save()

                obj1 = cart.objects.filter(cart_id=cart_id)
                obj1.delete()


                pid=int(product_id)
                item=itemdata.objects.get(product_id=pid)
                item.inventory_quantity= item.inventory_quantity - int(quantity)
                item.save()



                return HttpResponseRedirect("../show_orders/")
            else:
                return HttpResponseRedirect("../show_orders/")
        else:
            return HttpResponseRedirect("../auth_error/")
    else:
        return HttpResponseRedirect("../auth_error/")


# show orders
def show_orders(request):
    if request.session.has_key("usertype"):
        usertype = request.session["usertype"]
        if usertype=="customers":
            email = request.session["email"]
            obj = orders.objects.filter(email=email)
            return render(request, "show_orders.html", {"key1": obj})
        else:
            return HttpResponseRedirect("/auth_error/")
    else:
        return HttpResponseRedirect("/auth_error/")

# login
def login(request):
    if(request.method=="POST"):
        email = request.POST["T1"]
        password = request.POST["T2"]
        obj = logindata.objects.get(email=email,password=password)
        usertype = obj.usertype
        request.session["usertype"]=usertype
        request.session["email"]=email
        if(usertype=="admin"):
            return HttpResponseRedirect("/admin_home/")
        elif(usertype=="sellerdata"):
            return HttpResponseRedirect("/seller_home/")
        elif(usertype=="customers"):
            return HttpResponseRedirect("/customer_home/")
    else:
        return render(request,"login.html")
# logout
def logout(request):
    try:
        del request.session["email"]
        del request.session["usertype"]
    except:
        pass
    return HttpResponseRedirect("/login/")


# admin home
def admin_home(request):
    if(request.session.has_key("usertype")):
        usertype=request.session["usertype"]
        if(usertype=="admin"):
            return render(request,"admin_home.html")
        else:
            return render(request,"auth_error.html")
    else:
        return HttpResponseRedirect("/auth_error/")

# seller home
def seller_home(request):
    if(request.session.has_key("usertype")):
        usertype=request.session["usertype"]
        if(usertype=="sellerdata"):
            return render(request,"seller_home.html")
        else:
            return render(request,"auth_error.html")
    else:
        return HttpResponseRedirect("/auth_error/")

# customer home
def customer_home(request):
    if(request.session.has_key("usertype")):
        usertype = request.session["usertype"]
        if(usertype=="customers"):
            return render(request,"customer_home.html")
        else:
            return render(request,"auth_error.html")
    else:
        return HttpResponseRedirect("/auth_error/")

def auth_error(request):
    return render(request,"auth_error.html")


def index(request):
    return render(request,"index.html")