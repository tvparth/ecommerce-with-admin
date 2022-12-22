from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator ,MinValueValidator
# Create your models here.
STATE_CHOIES =(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa ','Goa '),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh ','Himachal Pradesh '),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    
)


# Create A Customer Models in Back and Side Dynamic
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOIES,max_length=50)

    """ This Function Is Returns A Id """
    def __str__(self):
        return str(self.id)
    
# Product Filter
CATEGORY_CHOICES =(
    ('Lp','Leptop'),
    ('Dtp','Desktop'),
    ('Tw','Topviewer'),
    ('Sh','SecondHand'),

)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField() 
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES ,max_length=3)
    product_image = models.ImageField(upload_to='product_img')
    
    # """ This Function Is Returns A Id """
    # def __str__(self):
    #     return str(self.id)
    

# Cart
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    """ This Function Is Returns A Id """
    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price


# Orderplaced
STATUS_CHOICES =(
    
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancle','Cancle'),
)
class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price



class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=150,null=False)
    lname = models.CharField(max_length=150,null=False)
    email = models.EmailField(max_length=150,null=False)
    phone = models.CharField(max_length=150,null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150,null=False)
    state = models.CharField(max_length=150,null=False)
    countory = models.CharField(max_length=150,null=False)
    pincode = models.CharField(max_length=150,null=False)
    total_price = models.FloatField(null=False)
    payment_mode  = models.CharField(max_length=150,null=False)
    payment_id  = models.CharField(max_length=150,null=False)
    orderstatuses =(
        ('Panding','Panding'),
        ('Out Of Shipping','Out Of Shipping'),
        ('Completed','Completed'),

    )
    status  = models.CharField(max_length=150,choices=orderstatuses,null=False)
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150,null=False)
    created_at = models.DateTimeField(max_length=150,null=False)
    updated_at = models.DateTimeField(max_length=150,null=False)
    
    def __str__(self) -> str:
        return '{} - {}'.format(self.id, self.tracking_no)


class OrderItem(models.Model):
    order  = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price  = models.FloatField(null=True)
    quantity = models.ImageField(null=True)

    def __str__(self) -> str:
        return '{} - {}'.format(self.id, self.tracking_no)