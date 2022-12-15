from pickle import FALSE
from django.shortcuts import render,redirect
from django.views import View
from . models import Customer,Product,Cart,OrderPlaced
from . forms import CustomerRegistraionForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
# Product View
class ProductView(View):
    def get(self,request):
        topviewer =Product.objects.filter(category = 'Tw')
        laptop =Product.objects.filter(category = 'Lp')
        desktok = Product.objects.filter(category = 'Dtp')
        secondhand = Product.objects.filter(category = 'Sh')
        return render(request,'store/home.html',{'topviewer': topviewer,
        'laptop':laptop,'desktok':desktok,'secondhand':secondhand})



# Product Details
class ProductDetailView(View):
    def get (self,request,pk):
     product =Product.objects.get(pk=pk)
     item_already_in_cart =False
     
     if request.user.is_authenticated:
        item_already_in_cart = Cart.objects.filter(Q(product=product.id)& 
        Q(user=request.user)).exists()
     return render(request,'store/productdetil.html',{'product':product,
     'item_already_in_cart ':item_already_in_cart })



# Add To Cart View
@login_required
def add_to_cart(request):
    user= request.user
    product_id = request.GET.get('prod_id')
    product=Product.objects.get(id= product_id)
    Cart(user=user,product =product).save()
    return redirect('/cart')


@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart =Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amouunt = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        
        if cart_product:
            for p in cart_product:
                tempamount =(p.quantity * p.product.selling_price)
                amount += tempamount
                totalamount = amount+shipping_amouunt
            return render(request,'store/addtocart.html',
            {'carts':cart,'totalamount':totalamount,'amount':amount})
        else:
             return render(request,'store/emptycart.html')


#Plus Quantity 
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
                tempamount =(p.quantity * p.product.selling_price)
                amount += tempamount
                data ={
                    'quantity':c.quantity,
                    'amount':amount,
                    'totalamount':amount + shipping_amount,
                }
        return JsonResponse(data)

# Minuscart
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.quantity -=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
                tempamount =(p.quantity * p.product.selling_price)
                amount += tempamount
                data ={
                    'quantity':c.quantity,
                    'amount':amount,
                    'totalamount': amount + shipping_amount,
                }
        return JsonResponse(data)

# Removed Cart
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
                tempamount =(p.quantity * p.product.selling_price)
                amount += tempamount
                
        data ={
            'amount':amount,
            'totalamount':amount + shipping_amount
                }
        return JsonResponse(data)



#Buy-Now
def buy_now(request):
    return render(request,'store/buynow.html')


#Profile View
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get (self,request):
        form = CustomerProfileForm()
        return render(request,'store/profile.html',{'form':form,'active':'btn-primery'})
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name =form.cleaned_data['name']
            locality =form.cleaned_data['locality']
            city =form.cleaned_data['city']
            state=form.cleaned_data['state']
            zipcode =form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulations Profile Updated.....')
        return render(request,'store/profile.html',{'form':form,'active':'btn-primery'})

        
# Address
def address(request):
    add = Customer.objects.filter(user= request.user)
    return render(request,'store/address.html',{'add':add,'active':'btn-primery'})

#Order
@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request,'store/order.html',{'order_placed':op})


# Change Password
# def change_password(request):
#     return render(request,'store/changepass.html')


# Leptop Filter
def leptop(request,data=None):
    if data == None:
        leptop = Product.objects.filter(category='Lp')
    elif data =='mac' or data == 'hp':
        leptop = Product.objects.filter(category='Lp').filter(brand=data)
    return render(request,'store/leptop.html',{'leptop':leptop})


# Customer Login 
""" Login Is In inbilt Function Used"""
# def customer_login(request):
#     return render(request,'store/login.html')


# Customer Registration
class CustomerRegistrationView(View):
    def get (self,request):
        form = CustomerRegistraionForm()
        return render(request,'store/registration.html',{'form':form})
    def post (self,request):
        form = CustomerRegistraionForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratualtions Registraion Successfully !!! ')
            form.save()
        return render(request,'store/registration.html',{'form':form})


# CheckOut
@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=request.user)
    print(add)
    cart_items =Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount =(p.quantity * p.product.selling_price)
            amount += tempamount
        totalamount=amount + shipping_amount
    return render(request,'store/checkout.html',{'add':add,'totalamount':totalamount,'cart_items':cart_items})


# Payment Done
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id = custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer = customer,product = c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")
