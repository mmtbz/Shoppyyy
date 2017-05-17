from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from .models import OrderItem, Order
from .froms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created


# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid:
            # save order but wait for commit, so that we can store the cupon used
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order = form.save()

            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['products'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id  # redirect to the payment
            return redirect('payment:process')
            # return render(request, 'order/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/order/create.html', {'cart': cart, 'form': form})


'''
a custom view that can be accessed by staff member only, means like vendor..

'''


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'adminn/orders/order/detail.html', {'order': order})
