from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "/Users/nick-v/PycharmProjects/e_commerce/dashboard/fixtures/db_admin_fixture.json")
        call_command("loaddata", "/Users/nick-v/PycharmProjects/e_commerce/inventory/fixtures/db_category_fixture.json")
        call_command("loaddata", "/Users/nick-v/PycharmProjects/e_commerce/inventory/fixtures/db_product_fixture.json")

        # порядок имеет значение
        call_command("loaddata", "/Users/nick-v/PycharmProjects/e_commerce/inventory/fixtures/db_brand_fixture.json")
        call_command("loaddata", "/Users/nick-v/PycharmProjects/e_commerce/inventory/fixtures/db_type_fixture.json")
        call_command("loaddata", "/Users/nick-v/PycharmProjects/e_commerce/inventory/fixtures/db_product_inventory_fixture.json")



