from django.contrib import admin
from . models import(Customer,Product,Cart,OrderPlaced,Order,OrderItem)
# Register your models here.

#Customer Site 
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display =['id','user','name','locality','city','zipcode','state']

# Product
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display =['id','title','selling_price','discount_price','brand','category','product_image']

#cart
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display =['id','user','product','quantity']

# Order placed
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display =['id','user','customer','product','quantity','order_date','status']

# Order placed
admin.site.register(Order)

admin.site.register(OrderItem)