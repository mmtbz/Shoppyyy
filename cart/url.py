__author__ = 'Dave'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cart_detail, name='detail'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='remove'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='add'),
]
