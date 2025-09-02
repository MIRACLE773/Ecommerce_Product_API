from django.contrib import admin
from .models import Product, Category

# Register models to appear in the admin site
admin.site.register(Category)
admin.site.register(Product)
