from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(_(r'^cart/'), include('cart.url', namespace='cart', app_name='cart')),
    url(_(r'^order/'), include('orders.url', namespace='order', app_name='orders')),
    # paypal url
    url(r'^paypal/', include('paypal.standard.ipn.urls', )),
    url(r'^rosetta/', include('rosetta.urls')),

    url(_(r'^payment/'), include('payment.url', namespace='payment')),
    url(_(r'^coupon/'), include('coupons.url', namespace='coupons')),
    url(r'^', include('shop.url', namespace='shop', app_name='shop')),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
