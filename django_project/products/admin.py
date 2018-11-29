from django.contrib import admin

# Register your models here.
from .models import Product, SubCategory, Category



admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Category)
