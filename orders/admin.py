from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product_name', 'product_id', 'price', 'quantity')
    extra = 0  # Do not show extra empty forms
    can_delete = False  # Prevent deleting from inline


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'id')
    readonly_fields = ('total_price', 'created_at')
    inlines = [OrderItemInline]
    ordering = ('-created_at',)
