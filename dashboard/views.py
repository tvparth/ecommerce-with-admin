from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .forms import AdminLoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.template import loader
from django.urls import reverse
from django import template
from django.contrib.auth.models import User
from store.models import Product, User
from store.forms import ProductForm

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

#
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

            return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


#
def show_user(request):
    usr = User.objects.all()
    return render(request, 'home/user.html',{'usr':usr})


#
def show_product(request):
    prod = Product.objects.all()       
    return render(request,'home/tables.html' ,{'pro':prod})

#
def add_product(request):
    if request.method =='POST':
        fm = ProductForm(request.POST)
        if fm.is_valid():
           id = fm.cleaned_data['id']
           title = fm.cleaned_data['title']
           sell  = fm.cleaned_data['selling price']
           description = fm.cleaned_data['description'] 
           brand  = fm.cleaned_data['brand']
           nep = Product(id=id, title=title, sell=sell, description=description, brand=brand)
           nep.save()
           fm = ProductForm()    
    else:
        fm = ProductForm() 
    prod = Product.objects.all()       
    return render(request,'product/insert.html' ,{'form':fm,'pro':prod})

# This Function Will Update/Edit
def update_product(request,id):
    fm = ""
    if request.method == 'POST':
      pi = Product.objects.get(pk = id)
      fm = ProductForm(request.POST) 
      if fm.is_valid():
          fm.save()
      else:
          pi = Product.objects.get(pk= id)
          fm = ProductForm(instance = pi)    
    return render(request,'product/upadate_product.html',{'form':fm})
    

# This Functoin Will Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add_product/')




