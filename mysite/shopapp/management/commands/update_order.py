from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Order, Product


class Command(BaseCommand):
    """Создает новые заказ"""

    def handle(self, *args, **options):
        order = Order.objects.first()
        if not order:
            self.stdout.write(f"Нет заказа")
            return

        products = Product.objects.all()
        for product in products:
            order.products.add(product)
        order.save()
        self.stdout.write(self.style.SUCCESS(f"Добавлены продукы {order.products.all()}"))
