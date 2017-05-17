from celery import task
from django.core.mail import send_mail
from .models import Order

__author__ = 'Dave'
"""
tasks to be executed by celery
"""


@task
def order_created(order_id):
    """
Task to send an e-mail notification when an order is
successfully created.
"""

    order = Order.objects.get(id=order_id)
    subject = 'Order nr {}'.format(order.id)
    message = 'Muraho {},\n\nWamaze kugura ibicuruzwa kuri Caltbay.com\n' \
              'Umubare wa order yawe ni {}'.format(order.first_name, order.id)

    mail_sent = send_mail(subject, message, 'order@caltbay.com', [order.email])
    return mail_sent
