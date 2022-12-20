from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .forms import AdminLoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.template import loader
from django.urls import reverse
from django import template
from django.contrib.auth.models import User
from store.models import Product, User
from store.forms import ProductForm, UserForm
from django.contrib import messages
import os
# Create your views here.
#Admin 

@login_required(login_url="/admin/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/admin/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

#Admin Login
def admin_login(request):
    form = AdminLoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/dashboard/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

#Admin Register
def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            return redirect("/custom/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


#--------------Users ------------#
# Show All User
def show_user(request):
    usr = User.objects.all()
    return render(request, 'home/user.html',{'usr':usr,})


# This Is User Update/Edit
def update_user(request,id):
    fm = ""
    if request.method == 'POST':
      ur = User.objects.get(pk = id)
      fm = UserForm(request.POST) 
      if fm.is_valid():
          fm.save()
      else:
          ur = User.objects.get(pk= id)
          fm = UserForm(instance = ur)    
    return render(request,'users/user_edit.html',{'fm':fm})
    

# This User Delete
def delete_user(request, id):
    if request.method == 'POST':
        ur = User.objects.get(pk=id)
        ur.delete()
        return HttpResponseRedirect('/user/')



# ----------Product-------------#

#Product Show 
def show_product(request):
    prod = Product.objects.all()       
    return render(request,'home/tables.html' ,{'pro':prod})

# Add Product
def add_product(request):
    if request.method == 'POST':
        prod = Product()
        prod.title = request.POST.get('title')
        prod.selling_price = request.POST.get('selling_price')
        prod.discount_price = request.POST.get('discount_price')
        prod.brand = request.POST.get('brand')
        prod.category = request.POST.get('category')
        prod.product_image = request.POST.get('product_img')
        
        prod.save()
        return redirect('/tables/')
    return render(request,'product/insert.html' )


# This Is Product Update/Edit
def edit_product(request,id):
    prod = Product.objects.get(pk=id)
    if request.method == 'POST':
        if len(request.FILES) != 0 :
            if len(prod.product_image) > 0 :
                os.remove(prod.product_image.path)
                prod.product_image = request.FILES('product_image')
            prod.title = request.POST.get('title')
            prod.selling_price = request.POST.get('selling_price')
            prod.discount_price = request.POST.get('discount_price')
            prod.brand = request.POST.get('brand')
            prod.category = request.POST.get('category')
            prod.save()
          
            return redirect('/tables/')
    return render(request,'product/upadate_product.html',{'prod':prod})
    

# This Is Product  Delete
def delete_data(request, id):
    if request.method == 'POST':
        prod = Product.objects.get(pk=id)
        prod.delete()
        return HttpResponseRedirect('/tables/')




