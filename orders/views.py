from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order, OrderItem

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()

    if request.method == "POST":
        order = Order.objects.create(user=request.user, total_price=cart.get_total_price())
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart.items.all().delete()
        return redirect("payment", order_id=order.id)

    return render(request, "checkout.html", {'cart': cart, 'cart_items': cart_items})

@login_required
def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == "POST":
        # Simulate payment logic
        return redirect('product_list')
    return render(request, 'payment.html', {'order': order})


