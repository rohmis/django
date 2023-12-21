from django.contrib import admin
from .models import Seller,Category,Product,Cart,Wishlist,Customer,Todo

admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Todo)
