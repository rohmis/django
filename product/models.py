from django.contrib.auth.models import User
from django.db import models

# Model representing a Category
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name
    
# Model representing a Seller Profile
class Seller(models.Model):
    user_name = models.CharField(max_length=100, default='No Company')
    company_name = models.CharField(max_length=100, default='No Company')
    address = models.TextField(default='No Address')
    pincode = models.CharField(max_length=20,default='No Pincode')  # Added pincode field
    contact_number = models.CharField(max_length=20,default='No number')
    website = models.URLField(blank=True)
    email = models.EmailField(default='No email')
    password = models.CharField(max_length=100,default='No password')

    def __str__(self):
        return self.user_name

# Model representing a Product
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    # Other fields related to products

    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    user_name =  models.CharField(max_length=50)
    address = models.TextField(default='No Address')
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(default='No email')
    password = models.CharField(max_length=100,default='No password')
    
    # Additional fields for customer details

    def __str__(self):
        return self.user_name


# Model representing a Customer's Cart
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    # Other fields related to cart

    def __str__(self):
        return f"Cart for {self.customer.user_name}"

# Model representing a Customer's Wishlist
class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    # Other fields related to wishlist

    def __str__(self):
        return f"Wishlist for {self.customer.user_name}"




class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    