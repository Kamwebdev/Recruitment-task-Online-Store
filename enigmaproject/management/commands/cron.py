from datetime import datetime

import kronos
from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand

from shop.models import Cart, Order, Product


@kronos.register('0 0 * * *')
class Command(BaseCommand):
    def handle(self, *args, **options):
        obj = Order.objects.all().filter(paymentDate__gte=datetime.now())
        for item in obj:
            email = EmailMessage(
                'Reminder',
                'Reminder about payment',
                'from@example.com',
                [item.client.email, ]
            )
            email.send()
