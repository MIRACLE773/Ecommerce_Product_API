from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from orders.models import Order


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)

    if request.method == "POST":
        # Create an order from the cart
        order = Order.objects.create(user=request.user, total=cart.get_total_price())

        # After creating order, redirect to payment page
        return redirect("payment", order_id=order.id)

    return render(request, "checkout.html", {"cart": cart})


@login_required
def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if request.method == "POST":
        payment_method = request.POST.get("payment_method")

        if payment_method == "card":
            # integrate Paystack/Stripe/Flutterwave here
            return redirect("card_payment", order_id=order.id)

        elif payment_method == "transfer":
            # show bank account details
            return render(request, "transfer_payment.html", {"order": order})

    return render(request, "payment.html", {"order": order})
