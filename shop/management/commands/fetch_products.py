import requests
from django.core.management.base import BaseCommand
from api.models import Product


class Command(BaseCommand):
    help = "Fetch products from DummyJSON API and populate the database"

    def handle(self, *args, **kwargs):
        url = "https://dummyjson.com/products?limit=20"  # fetch first 20
        response = requests.get(url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR("Failed to fetch products"))
            return

        data = response.json()
        products = data.get("products", [])

        for p in products:
            Product.objects.get_or_create(
                title=p["title"],
                defaults={
                    "description": p.get("description", ""),
                    "brand": p.get("brand", "Unknown"),
                    "price": p.get("price", 0.00),
                    "thumbnail": p["thumbnail"],
                },
            )

        self.stdout.write(self.style.SUCCESS(f"{len(products)} products fetched and saved!"))



