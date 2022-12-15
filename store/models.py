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
    
    """ This Function Is Returns A Id """
    def __str__(self):
        return str(self.id)
    

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
