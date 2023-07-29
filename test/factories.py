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
    # name = fake.lexify(text="cat_name_????")  # >>> cat_name_XwCI > cat_name_FfFh
    slug = fake.lexify(text="cat_slug_????")
    # is_active = fake.lexify()  # factory by default set for bool type - true

    # но есть проблема, потому что позже мы захотим использовать уникальные поля
    # и т.к. lexify автоматом вставлять данные в "?", то потом будут иошибки при вставке (потенциально)
    # поєтому используем "последовательность"
    name = factory.Sequence(lambda n: "cat_slug_%d" % n)  # cat_slug_0 > cat_slug_1


register(CategoryFactory)
