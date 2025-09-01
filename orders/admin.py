from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total_price", "is_paid", "created_at")  # ✅ now works

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
