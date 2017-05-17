__author__ = 'Dave'

from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.models import valid_ipn_received
from orders.models import Order


def payment_notification(sender, **kwargs):
    ipn_object = sender
    if ipn_object.payment_status == ST_PP_COMPLETED:
        # payment was successfull
        order = get_object_or_404(Order, id=ipn_object.invoice)
        # mark the order as paid
        order.paid = True
        order.save()


valid_ipn_received.connect(payment_notification)
