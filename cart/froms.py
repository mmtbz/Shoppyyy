__author__ = 'Dave'
from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QTY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QTY_CHOICES, coerce=int, label=_('Quantity'))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    # update to specify if the cart is being updated or initialized

