from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LMX7DBnhm1C2FG1wObXa8y3Xj4zR9NEuzFzwv5O3TnpmJnEbD7ZU57XFYXRUlIeK9WIVsjus1rTAxFwkOwGdlMP00aweG111r',
        'client_secret' : 'test client secret',
    }

    return render(request, template, context)