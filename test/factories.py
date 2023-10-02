import factory
import pytest

from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from inventory import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        """
        Define a model that we're gonna use
        """
        model = models.Category

    # lexify позволит подставлять символы вместо '?'
    # name = fake.lexify(text="category_name_????")  # >>> cat_name_XwCI > cat_name_FfFh
    slug = fake.lexify(text="category_slug_????")
    # is_active = fake.lexify()  # factory by default set for bool type - true

    # но есть проблема, потому что позже мы захотим использовать уникальные поля
    # и т.к. lexify автоматом вставлять данные в "?", то потом будут иошибки при вставке (потенциально)
    # поєтому используем "последовательность"
    name = factory.Sequence(lambda n: "category_slug_%d" % n)  # cat_slug_0 > cat_slug_1


class ProductFactory(factory.django.DjangoModelFactory):
    """make factory by ablog of category"""

    class Meta:
        model = models.Product

    web_id = factory.Sequence(lambda n: "web_id_%d" % n)
    slug = fake.lexify(text="product_slug_????")
    name = fake.lexify(text="product_name_????")
    description = fake.text()
    is_active = True
    created_at = "2022-01-01 14:18:33"
    updated_at = "2022-01-01 14:18:33"

    @factory.post_generation
    def category(self, create, extracted,
                 **kwargs):  # product_factory.create(category=(1, 36,)) from test_db_fixtures.py
        """
        нужно законектить при создание нового продукта к категории (ипользуя post_generation, как сигнал)

        https://factoryboy.readthedocs.io/en/stable/reference.html#factory.post_generation

        create is a boolean indicating which strategy was used
        [create — це логічне значення, яке вказує, яку стратегію було використано]

        extracted is None unless a value was passed in for the PostGeneration declaration at Factory declaration time
        [extracted is None, якщо значення не було передано для декларації PostGeneration під час декларації Factory]

        UserFactory.build()                  # Nothing was created
        UserFactory.create()                 # Creates dir /tmp/mbox/john
        UserFactory.create(login='jack')     # Creates dir /tmp/mbox/jack
        UserFactory.create(mbox='/tmp/alt')  # Creates dir /tmp/alt

        т.е. в exctracted попадают катагории, которые мы хотим добавить (к продукту)
        а в create  катагории, которые мы хотим создать
        """
        if not create or not extracted:  # если нет катгорий, то ничего не далаем(хотя можем)
            return  # if we don't create any data - we don't need do anything

        if extracted:  # if pass over some categries we want to add
            for category in extracted:  # wee will add catagry that was passed into the func
                self.category.add(category)

        # path = extracted or os.path.join('/tmp/mbox/', self.login)
        # os.path.makedirs(path)


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductType

    name = factory.Sequence(lambda n: "type_%d" % n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand

    name = factory.Sequence(lambda n: "brand_%d" % n)


class ProductInventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductInventory

    sku = factory.Sequence(lambda n: "sku_%d" % n)
    upc = factory.Sequence(lambda n: "upc_%d" % n)
    product_type = factory.SubFactory(ProductTypeFactory)  # create a link
    product = factory.SubFactory(ProductFactory)  # create a link
    brand = factory.SubFactory(BrandFactory)  # create a link
    is_active = 1
    retail_price = 97
    store_price = 92
    sale_price = 46
    weight = 987


register(CategoryFactory)
register(ProductFactory)
register(ProductTypeFactory)
register(BrandFactory)
register(ProductInventoryFactory)
register(ProductFactory)
