from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product

@login_required
def cart_detail(request):
    # Get or create the user's cart
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()

    # Calculate total per item
    for item in cart_items:
        item.total_price = item.product.price * item.quantity  # Attach total_price dynamically

    # Calculate grand total
    total = sum(item.total_price for item in cart_items)

    return render(request, "cart/cart_detail.html", {
        "cart_items": cart_items,
        "total": total,
    })


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    qty = int(request.POST.get('quantity', 1))
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += qty
    else:
        item.quantity = qty
    item.save()
    return redirect('cart_detail')


@login_required
def remove_from_cart(request, pk):
    cart = get_object_or_404(Cart, user=request.user)
    item = get_object_or_404(CartItem, cart=cart, product_id=pk)
    item.delete()
    return redirect('cart_detail')


@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.items.all()

    # Calculate total per item
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    total = sum(item.total_price for item in cart_items)

    payment_options = ["Bank Transfer", "Card Payment", "Pay on Delivery"]
    account_number = "1234567890"
    rider_options = ["No Preference", "Fastest Rider", "Specific Rider"]

    return render(request, "cart/checkout.html", {
        "cart_items": cart_items,
        "total": total,
        "payment_options": payment_options,
        "account_number": account_number,
        "rider_options": rider_options
    })
