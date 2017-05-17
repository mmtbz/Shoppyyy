from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'payment'

    verbrose_name = 'Payment'
    def ready(self):
        # import signal handlers
        import payment.signals