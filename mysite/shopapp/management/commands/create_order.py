from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Order


class Command(BaseCommand):
    """Создает новые заказ"""

    def handle(self, *args, **options):
        self.stdout.write("Создаем заказ")
        user = User.objects.get(username="admin")
        order = Order.objects.get_or_create(
            delivery_address="Aaa st.",
            promocode="PROMO",
            user=user,
        )
        self.stdout.write(f"Создан заказ {order}")

        self.stdout.write(self.style.SUCCESS("Заказ создан"))
