from django.core.management import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    """Создает новые продукты"""

    def handle(self, *args, **options):
        self.stdout.write("Создаем продукты")

        products = [
            "Laptop",
            "Desktop",
            "Smartphone",
        ]

        for product_name in products:
            product, created = Product.objects.get_or_create(name=product_name)
            self.stdout.write(f"Создан продукт {product} {created}")

        self.stdout.write(self.style.SUCCESS("Продукты созданы"))
