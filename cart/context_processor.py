__author__ = 'Dave'

"""
for creating a context processor that we can use anywhere in our template

context processor is a function that receives the request object
as parameter, and returns a dictionary of objects that will be available to all the
templates rendered using RequestContext.
"""
from .cart import Cart


def cart(request):
    """
    Check if the product quantity is greater than 1 so that we dont count one product twice
    """
    """crt = Cart(request)
    for item in crt:
        if item['quantity'] > 1:
            item['quantity'] = 1"""
    return {'cart': Cart(request)}
